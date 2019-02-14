<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyLocal="1" simplifyMaxScale="1" maxScale="0" styleCategories="AllStyleCategories" version="3.4.4-Madeira" simplifyAlgorithm="0" simplifyDrawingTol="1" readOnly="0" labelsEnabled="0" minScale="1e+08" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" type="RuleRenderer" enableorderby="0">
    <rules key="{c11348db-65c3-4127-958f-f439370b53d0}">
      <rule filter=" &quot;Abandon&quot;  =  1" symbol="0" label="Abandonné" key="{0a52c78f-2d03-46b2-a0fd-23072fe2ab6c}">
        <rule filter="&quot;Reseau&quot; = 'ELEC'" symbol="1" label="Electricité BT, HTA ou HTB, éclairage " key="{d5de1a67-d2d6-402b-b859-11ea330a821e}"/>
        <rule filter="&quot;Reseau&quot; = 'GAZ'" symbol="2" label="Gaz combustible et hydrocarbures" key="{18d99ea3-dbd3-46bc-a378-12fc828420d5}"/>
        <rule filter="&quot;Reseau&quot; = 'PC'" symbol="3" label="Produits chimiques et autres gaz" key="{151f2703-aec2-4257-829e-ef8b5f5c8a51}"/>
        <rule filter="&quot;Reseau&quot; = 'EP'" symbol="4" label="Eau potable" key="{9b122b47-afee-47f2-b03f-5cd3d62b989e}"/>
        <rule filter="&quot;Reseau&quot; = 'ASS'" symbol="5" label="Assainissement et pluvial" key="{33b329a0-acef-4517-9140-f42c0a585bfd}"/>
        <rule filter="&quot;Reseau&quot; = 'CC'" symbol="6" label="Chauffage et climatisation" key="{113b8728-2162-4db4-9a2a-c43065becc0c}"/>
        <rule filter="&quot;Reseau&quot; = 'TEL'" symbol="7" label="Télécommunications" key="{a133cf2a-d4fe-47a6-8889-bf9b43952804}"/>
        <rule filter="&quot;Reseau&quot; = 'SIG'" symbol="8" label="Signalisation routière" key="{35f48f99-9187-47c3-8566-b7af13348bdc}"/>
        <rule filter="&quot;Reseau&quot; = 'MR'" symbol="9" label="Multi réseau ou divers" key="{87ca4554-17a7-4d14-a874-d252755ad94f}"/>
      </rule>
      <rule filter=" &quot;Abandon&quot;  =  0" symbol="10" label="En Service" key="{a936a430-c2da-4b17-8383-4abdf4233f80}">
        <rule filter="&quot;Reseau&quot; = 'ELEC'" symbol="11" label="Electricité BT, HTA ou HTB, éclairage " key="{96d88daa-a578-4ab0-9b2c-b66d1bfa7014}"/>
        <rule filter="&quot;Reseau&quot; = 'GAZ'" symbol="12" label="Gaz combustible et hydrocarbures" key="{60e883b2-6648-431a-936e-5f3c337baa40}"/>
        <rule filter="&quot;Reseau&quot; = 'PC'" symbol="13" label="Produits chimiques et autres gaz" key="{3406402d-8901-49bc-a084-536ec73f89a0}"/>
        <rule filter="&quot;Reseau&quot; = 'EP'" symbol="14" label="Eau potable" key="{5e485477-ef76-4745-8421-63303909bb9f}"/>
        <rule filter="&quot;Reseau&quot; = 'ASS'" symbol="15" label="Assainissement et pluvial" key="{2c796692-0679-4fee-8d85-e68a1549b884}"/>
        <rule filter="&quot;Reseau&quot; = 'CC'" symbol="16" label="Chauffage et climatisation" key="{8e95ac60-a13c-449f-9625-d01abe4ab14e}"/>
        <rule filter="&quot;Reseau&quot; = 'TEL'" symbol="17" label="Télécommunications" key="{6c8919d8-c125-4527-a6a3-ba757859d76c}"/>
        <rule filter="&quot;Reseau&quot; = 'SIG'" symbol="18" label="Signalisation routière" key="{22e2502b-6b23-4f19-b7a1-430c20e0649e}"/>
        <rule filter="&quot;Reseau&quot; = 'MR'" symbol="19" label="Multi réseau ou divers" key="{1c14b80d-9d39-48b6-b87a-280fd4e62815}"/>
      </rule>
    </rules>
    <symbols>
      <symbol name="0" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="183,72,75,0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="no"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="no"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,0,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="10" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="183,72,75,0"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="no"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="no"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="11" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,0,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="12" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,255,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="13" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,165,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="14" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,0,255,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="15" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="129,48,12,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="16" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="128,0,128,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="17" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,128,0,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="18" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,255,255,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="19" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,192,203,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,0"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,255,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,165,0,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,0,255,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="5" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="129,48,12,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="6" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="128,0,128,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="7" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="0,128,0,127"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="8" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,255,255,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="false" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="9" clip_to_extent="1" type="fill" force_rhr="0" alpha="1">
        <layer class="SimpleFill" enabled="1" pass="0" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="255,192,203,128"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="b_diagonal"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="outlineColor" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="CASE &#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ELEC' THEN 'red'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'GAZ' THEN 'yellow'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'PC' THEN 'orange'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'EP' THEN 'blue'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'ASS' THEN '#81300c'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'CC' THEN 'purple'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'SIG' THEN 'white'&#xd;&#xa;WHEN &quot;Reseau&quot; LIKE 'MR' THEN 'pink'&#xd;&#xa;ELSE 'green'&#xd;&#xa;END" name="expression" type="QString"/>
                  <Option value="3" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory backgroundAlpha="255" labelPlacementMethod="XHeight" barWidth="5" width="15" minimumSize="0" sizeType="MM" lineSizeType="MM" backgroundColor="#ffffff" penWidth="0" enabled="0" penColor="#000000" diagramOrientation="Up" opacity="1" scaleBasedVisibility="0" lineSizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" penAlpha="255" maxScaleDenominator="1e+08" sizeScale="3x:0,0,0,0,0,0" height="15" rotationOffset="270" minScaleDenominator="0">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="" color="#000000" field=""/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings linePlacementFlags="18" dist="0" priority="0" placement="1" zIndex="0" obstacle="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="Operateur">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Reseau">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Abandon">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="aaa">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="Operateur"/>
    <alias index="1" name="" field="Reseau"/>
    <alias index="2" name="" field="Abandon"/>
    <alias index="3" name="" field="aaa"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="Operateur"/>
    <default applyOnUpdate="0" expression="" field="Reseau"/>
    <default applyOnUpdate="0" expression="" field="Abandon"/>
    <default applyOnUpdate="0" expression="" field="aaa"/>
  </defaults>
  <constraints>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="Operateur" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="Reseau" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="Abandon" exp_strength="0"/>
    <constraint constraints="0" unique_strength="0" notnull_strength="0" field="aaa" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="Operateur"/>
    <constraint exp="" desc="" field="Reseau"/>
    <constraint exp="" desc="" field="Abandon"/>
    <constraint exp="" desc="" field="aaa"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column name="Operateur" hidden="0" type="field" width="-1"/>
      <column name="Reseau" hidden="0" type="field" width="-1"/>
      <column name="Abandon" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
      <column name="aaa" hidden="0" type="field" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="Abandon"/>
    <field editable="1" name="Operateur"/>
    <field editable="1" name="Reseau"/>
    <field editable="1" name="aaa"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="Abandon"/>
    <field labelOnTop="0" name="Operateur"/>
    <field labelOnTop="0" name="Reseau"/>
    <field labelOnTop="0" name="aaa"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>Operateur</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
