# -*- coding: utf-8 -*-

"""
***************************************************************************
    SnapGeometries.py
    -----------------
    Date                 : October 2016
    Copyright            : (C) 2016 by Nyall Dawson
    Email                : nyall dot dawson at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nyall Dawson'
__date__ = 'October 2016'
__copyright__ = '(C) 2016, Nyall Dawson'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.analysis import (QgsGeometrySnapper,
                           QgsInternalGeometrySnapper)
from qgis.core import (QgsApplication,
                       QgsFeature,
                       QgsFeatureSink,
                       QgsProcessingUtils)

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from processing.core.parameters import ParameterVector, ParameterNumber, ParameterSelection
from processing.core.outputs import OutputVector


class SnapGeometriesToLayer(QgisAlgorithm):

    INPUT = 'INPUT'
    REFERENCE_LAYER = 'REFERENCE_LAYER'
    TOLERANCE = 'TOLERANCE'
    OUTPUT = 'OUTPUT'
    BEHAVIOR = 'BEHAVIOR'

    def group(self):
        return self.tr('Vector geometry tools')

    def __init__(self):
        super().__init__()
        self.addParameter(ParameterVector(self.INPUT, self.tr('Input layer')))
        self.addParameter(ParameterVector(self.REFERENCE_LAYER, self.tr('Reference layer')))
        self.addParameter(ParameterNumber(self.TOLERANCE, self.tr('Tolerance (layer units)'), 0.00000001, 9999999999, default=10.0))

        self.modes = [self.tr('Prefer aligning nodes'),
                      self.tr('Prefer closest point'),
                      self.tr('Move end points only, prefer aligning nodes'),
                      self.tr('Move end points only, prefer closest point'),
                      self.tr('Snap end points to end points only')]
        self.addParameter(ParameterSelection(
            self.BEHAVIOR,
            self.tr('Behavior'),
            self.modes, default=0))
        self.addOutput(OutputVector(self.OUTPUT, self.tr('Snapped geometries')))

    def name(self):
        return 'snapgeometries'

    def displayName(self):
        return self.tr('Snap geometries to layer')

    def processAlgorithm(self, parameters, context, feedback):
        layer = QgsProcessingUtils.mapLayerFromString(self.getParameterValue(self.INPUT), context)
        reference_layer = QgsProcessingUtils.mapLayerFromString(self.getParameterValue(self.REFERENCE_LAYER), context)
        tolerance = self.getParameterValue(self.TOLERANCE)
        mode = self.getParameterValue(self.BEHAVIOR)

        writer = self.getOutputFromName(self.OUTPUT).getVectorWriter(layer.fields(), layer.wkbType(), layer.crs(),
                                                                     context)

        features = QgsProcessingUtils.getFeatures(layer, context)

        self.processed = 0
        self.feedback = feedback
        self.total = 100.0 / layer.featureCount() if layer.featureCount() else 0

        if self.getParameterValue(self.INPUT) != self.getParameterValue(self.REFERENCE_LAYER):
            snapper = QgsGeometrySnapper(reference_layer)
            snapper.featureSnapped.connect(self.featureSnapped)
            snapped_features = snapper.snapFeatures(features, tolerance, mode)
            for f in snapped_features:
                writer.addFeature(f, QgsFeatureSink.FastInsert)
        else:
            # snapping internally
            snapper = QgsInternalGeometrySnapper(tolerance, mode)
            processed = 0
            for f in features:
                out_feature = f
                out_feature.setGeometry(snapper.snapFeature(f))
                writer.addFeature(out_feature, QgsFeatureSink.FastInsert)
                processed += 1
                feedback.setProgress(processed * self.total)

        del writer

    def featureSnapped(self):
        self.processed += 1
        self.feedback.setProgress(int(self.processed * self.total))
