/***************************************************************************
                         qgsprocessingoutputs.cpp
                         -------------------------
    begin                : May 2017
    copyright            : (C) 2017 by Nyall Dawson
    email                : nyall dot dawson at gmail dot com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

#include "qgsprocessingoutputs.h"

QgsProcessingOutputDefinition::QgsProcessingOutputDefinition( const QString &name, const QString &description )
  : mName( name )
  , mDescription( description )
{

}

QgsProcessingOutputVectorLayer::QgsProcessingOutputVectorLayer( const QString &name, const QString &description, QgsProcessingParameterDefinition::LayerType type )
  : QgsProcessingOutputDefinition( name, description )
  , mDataType( type )
{}

QgsProcessingParameterDefinition::LayerType QgsProcessingOutputVectorLayer::dataType() const
{
  return mDataType;
}

void QgsProcessingOutputVectorLayer::setDataType( QgsProcessingParameterDefinition::LayerType type )
{
  mDataType = type;
}

QgsProcessingOutputRasterLayer::QgsProcessingOutputRasterLayer( const QString &name, const QString &description )
  : QgsProcessingOutputDefinition( name, description )
{}

QgsProcessingOutputHtml::QgsProcessingOutputHtml( const QString &name, const QString &description )
  : QgsProcessingOutputDefinition( name, description )
{}

QgsProcessingOutputNumber::QgsProcessingOutputNumber( const QString &name, const QString &description )
  : QgsProcessingOutputDefinition( name, description )
{}

QgsProcessingOutputString::QgsProcessingOutputString( const QString &name, const QString &description )
  : QgsProcessingOutputDefinition( name, description )
{}

QgsProcessingOutputFolder::QgsProcessingOutputFolder( const QString &name, const QString &description )
  : QgsProcessingOutputDefinition( name, description )
{
}
