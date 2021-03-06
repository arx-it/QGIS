/************************************************************************
 * This file has been generated automatically from                      *
 *                                                                      *
 * src/core/symbology-ng/qgsnullsymbolrenderer.h                        *
 *                                                                      *
 * Do not edit manually ! Edit header and run scripts/sipify.pl again   *
 ************************************************************************/



class QgsNullSymbolRenderer : QgsFeatureRenderer
{
%Docstring
 Null symbol renderer. Renderer which draws no symbols for features by default, but allows for labeling
 and diagrams for the layer. Selected features will also be drawn with a default symbol.
.. versionadded:: 2.16
%End

%TypeHeaderCode
#include "qgsnullsymbolrenderer.h"
%End
  public:

    QgsNullSymbolRenderer();

    virtual QgsSymbol *symbolForFeature( QgsFeature &feature, QgsRenderContext &context );
    virtual QgsSymbol *originalSymbolForFeature( QgsFeature &feature, QgsRenderContext &context );

    virtual bool renderFeature( QgsFeature &feature, QgsRenderContext &context, int layer = -1, bool selected = false, bool drawVertexMarker = false );
    virtual void startRender( QgsRenderContext &context, const QgsFields &fields );
    virtual void stopRender( QgsRenderContext &context );
    virtual bool willRenderFeature( QgsFeature &feat, QgsRenderContext &context );

    virtual QSet<QString> usedAttributes( const QgsRenderContext &context ) const;
    virtual QString dump() const;
    virtual QgsFeatureRenderer *clone() const /Factory/;
    virtual QgsSymbolList symbols( QgsRenderContext &context );

    static QgsFeatureRenderer *create( QDomElement &element, const QgsReadWriteContext &context ) /Factory/;
%Docstring
 Creates a null renderer from XML element.
 \param element DOM element
 \param context reading context
 :return: new null symbol renderer
 :rtype: QgsFeatureRenderer
%End

    virtual QDomElement save( QDomDocument &doc, const QgsReadWriteContext &context );

    static QgsNullSymbolRenderer *convertFromRenderer( const QgsFeatureRenderer *renderer ) /Factory/;
%Docstring
 Creates a QgsNullSymbolRenderer from an existing renderer.
 \param renderer renderer to convert from
 :return: a new renderer if the conversion was possible, otherwise None.
 :rtype: QgsNullSymbolRenderer
%End

};

/************************************************************************
 * This file has been generated automatically from                      *
 *                                                                      *
 * src/core/symbology-ng/qgsnullsymbolrenderer.h                        *
 *                                                                      *
 * Do not edit manually ! Edit header and run scripts/sipify.pl again   *
 ************************************************************************/
