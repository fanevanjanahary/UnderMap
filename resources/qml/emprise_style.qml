<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+8" simplifyMaxScale="1" version="3.2.3-Bonn" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="0" readOnly="0" simplifyDrawingTol="1" simplifyDrawingHints="1" simplifyLocal="1" labelsEnabled="0" maxScale="0">
  <renderer-v2 enableorderby="0" symbollevels="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol alpha="1" clip_to_extent="1" name="0" type="fill">
        <layer class="SimpleFill" pass="0" locked="0" enabled="1">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="145,82,45,2" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="129,48,12,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory height="15" enabled="0" minimumSize="0" width="15" maxScaleDenominator="1e+8" barWidth="5" penColor="#000000" rotationOffset="270" scaleBasedVisibility="0" sizeScale="3x:0,0,0,0,0,0" lineSizeScale="3x:0,0,0,0,0,0" sizeType="MM" scaleDependency="Area" backgroundAlpha="255" lineSizeType="MM" diagramOrientation="Up" penAlpha="255" minScaleDenominator="0" penWidth="0" opacity="1" labelPlacementMethod="XHeight" backgroundColor="#ffffff">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings showAll="1" priority="0" dist="0" obstacle="0" linePlacementFlags="18" zIndex="0" placement="1">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <fieldConfiguration>
    <field name="Name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="descriptio">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="timestamp">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="begin">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="end">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altitudeMo">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tessellate">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="extrude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="visibility">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="drawOrder">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="icon">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="Name"/>
    <alias index="1" name="" field="descriptio"/>
    <alias index="2" name="" field="timestamp"/>
    <alias index="3" name="" field="begin"/>
    <alias index="4" name="" field="end"/>
    <alias index="5" name="" field="altitudeMo"/>
    <alias index="6" name="" field="tessellate"/>
    <alias index="7" name="" field="extrude"/>
    <alias index="8" name="" field="visibility"/>
    <alias index="9" name="" field="drawOrder"/>
    <alias index="10" name="" field="icon"/>
    <alias index="11" name="" field="id"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="Name"/>
    <default applyOnUpdate="0" expression="" field="descriptio"/>
    <default applyOnUpdate="0" expression="" field="timestamp"/>
    <default applyOnUpdate="0" expression="" field="begin"/>
    <default applyOnUpdate="0" expression="" field="end"/>
    <default applyOnUpdate="0" expression="" field="altitudeMo"/>
    <default applyOnUpdate="0" expression="" field="tessellate"/>
    <default applyOnUpdate="0" expression="" field="extrude"/>
    <default applyOnUpdate="0" expression="" field="visibility"/>
    <default applyOnUpdate="0" expression="" field="drawOrder"/>
    <default applyOnUpdate="0" expression="" field="icon"/>
    <default applyOnUpdate="0" expression="" field="id"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="Name" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="descriptio" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="timestamp" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="begin" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="end" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="altitudeMo" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="tessellate" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="extrude" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="visibility" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="drawOrder" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="icon" constraints="0"/>
    <constraint exp_strength="0" notnull_strength="0" unique_strength="0" field="id" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="Name"/>
    <constraint desc="" exp="" field="descriptio"/>
    <constraint desc="" exp="" field="timestamp"/>
    <constraint desc="" exp="" field="begin"/>
    <constraint desc="" exp="" field="end"/>
    <constraint desc="" exp="" field="altitudeMo"/>
    <constraint desc="" exp="" field="tessellate"/>
    <constraint desc="" exp="" field="extrude"/>
    <constraint desc="" exp="" field="visibility"/>
    <constraint desc="" exp="" field="drawOrder"/>
    <constraint desc="" exp="" field="icon"/>
    <constraint desc="" exp="" field="id"/>
  </constraintExpressions>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column hidden="0" width="-1" name="Name" type="field"/>
      <column hidden="0" width="-1" name="descriptio" type="field"/>
      <column hidden="0" width="-1" name="timestamp" type="field"/>
      <column hidden="0" width="-1" name="begin" type="field"/>
      <column hidden="0" width="-1" name="end" type="field"/>
      <column hidden="0" width="-1" name="altitudeMo" type="field"/>
      <column hidden="0" width="-1" name="tessellate" type="field"/>
      <column hidden="0" width="-1" name="extrude" type="field"/>
      <column hidden="0" width="-1" name="visibility" type="field"/>
      <column hidden="0" width="-1" name="drawOrder" type="field"/>
      <column hidden="0" width="-1" name="icon" type="field"/>
      <column hidden="0" width="-1" name="id" type="field"/>
      <column hidden="1" width="-1" type="actions"/>
    </columns>
  </attributetableconfig>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="Name"/>
    <field editable="1" name="altitudeMo"/>
    <field editable="1" name="begin"/>
    <field editable="1" name="descriptio"/>
    <field editable="1" name="drawOrder"/>
    <field editable="1" name="end"/>
    <field editable="1" name="extrude"/>
    <field editable="1" name="icon"/>
    <field editable="1" name="id"/>
    <field editable="1" name="tessellate"/>
    <field editable="1" name="timestamp"/>
    <field editable="1" name="visibility"/>
  </editable>
  <labelOnTop>
    <field name="Name" labelOnTop="0"/>
    <field name="altitudeMo" labelOnTop="0"/>
    <field name="begin" labelOnTop="0"/>
    <field name="descriptio" labelOnTop="0"/>
    <field name="drawOrder" labelOnTop="0"/>
    <field name="end" labelOnTop="0"/>
    <field name="extrude" labelOnTop="0"/>
    <field name="icon" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="tessellate" labelOnTop="0"/>
    <field name="timestamp" labelOnTop="0"/>
    <field name="visibility" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <expressionfields/>
  <previewExpression>Name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
