---
topic_id: 4260
title: "Dcm To Obj Conversion"
date: 2018-10-02
url: https://discourse.slicer.org/t/4260
---

# .dcm to .obj conversion

**Topic ID**: 4260
**Date**: 2018-10-02
**URL**: https://discourse.slicer.org/t/dcm-to-obj-conversion/4260

---

## Post #1 by @kinda.h (2018-10-02 15:34 UTC)

<p>How can i convert .dcm to .obj (both 3d colored) in slicer</p>

---

## Post #2 by @lassoan (2018-10-02 18:08 UTC)

<p>You need to segment structures that you are interested in. See tutorials about how to do that using Slicer here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #3 by @kinda.h (2018-10-02 19:32 UTC)

<p>Thank you for your reply. But it seems I cant import my .dcm 3D model into slicer by dragging and dropping.</p>

---

## Post #4 by @kinda.h (2018-10-02 19:56 UTC)

<p>Can you please check the file i need to import and help put <a href="https://we.tl/t-emV0N6Qq2h" rel="nofollow noopener">https://we.tl/t-emV0N6Qq2h</a></p>

---

## Post #5 by @lassoan (2018-10-02 20:49 UTC)

<p>This file is not in DICOM format at all. It looks like an XML-based file that contains a textured surface scan.</p>
<details>
<summary>
File content summary</summary>
<pre><code>&lt;HPS version="1.1"&gt;
  &lt;Packed_geometry&gt;
    &lt;Schema&gt;CE&lt;/Schema&gt;
    &lt;Binary_data&gt;
      &lt;CE version="1.0"&gt;
        &lt;Facets facet_count="210785" base64_encoded_bytes="230074" color="8421504"&gt;…&lt;/Facets&gt;
        &lt;Vertices vertex_count="106388" base64_encoded_bytes="1276656" check_value="1503019551"&gt;...&lt;/Vertices&gt;
      &lt;/CE&gt;
    &lt;/Binary_data&gt;
  &lt;/Packed_geometry&gt;
  &lt;SignatureHash&gt;468746363166DB9BC44B79AB1E07BCE00BDD09CF&lt;/SignatureHash&gt;
  &lt;TextureData2&gt;
    &lt;TextureSetIDs IndexCount="1" Base64EncodedBytes="4"&gt;AAAAAA==&lt;/TextureSetIDs&gt;
    &lt;PerVertexTextureCoord Base64EncodedBytes="531980" Key="1"&gt;...&lt;/PerVertexTextureCoord&gt;
    &lt;TextureImages&gt;
      &lt;TextureImage Width="2048" Height="2048" TextureName="Texture" TextureCoordSet="0" BytesPerPixel="3" Base64EncodedBytes="294270"&gt;...&lt;/TextureImage&gt;
    &lt;/TextureImages&gt;
  &lt;/TextureData2&gt;
  &lt;FacetMarks&gt;
&lt;/FacetMarks&gt;
  &lt;Annotations&gt;
    &lt;Annotation type="CoordinateTransform"&gt;
      &lt;String name="TransformID" value="Focus2FinalTrans" /&gt;
      &lt;Matrix4x4 name="TransformMatrix" m00="0.113340572" m01="-0.979611039" m02="0.165879682" m03="27.2143612" m10="-0.981021166" m11="-0.08390312" m12="0.174807817" m13="-6.56699562" m20="-0.157325849" m21="-0.1825443" m22="-0.9705288" m23="-19.03727" m30="0" m31="0" m32="0" m33="1" /&gt;
      &lt;Property name="Misc" value="0" /&gt;
    &lt;/Annotation&gt;
  &lt;/Annotations&gt;
  &lt;Objects /&gt;
  &lt;Splines /&gt;
  &lt;Properties&gt;
    &lt;Property name="TranscodeProperties" value="EKID;SiteDongle" /&gt;
    &lt;Property name="SiteDongle" value="1596591929" /&gt;
    &lt;Property name="EKID" value="1" /&gt;
    &lt;Property name="Application" value="TRIOS 1.3.3.1" /&gt;
    &lt;Property name="AVNRTime" value="15" /&gt;
    &lt;Property name="ChrominanceVariance" value="113" /&gt;
    &lt;Property name="ColorCalibrationKitVersion" value="1" /&gt;
    &lt;Property name="ComputerName" value="BECKTOR" /&gt;
    &lt;Property name="DaysSinceCalibration" value="0" /&gt;
    &lt;Property name="DistributorID" value="11" /&gt;
    &lt;Property name="DongleNumber" value="1463509418" /&gt;
    &lt;Property name="Transcode_EKID" value="1" /&gt;
    &lt;Property name="FusedDiff" value="-1" /&gt;
    &lt;Property name="HighResSubscanCount" value="0" /&gt;
    &lt;Property name="NormContrast" value="-1" /&gt;
    &lt;Property name="ParamContrast" value="8.75259675950082716" /&gt;
    &lt;Property name="PostProcessTime" value="190.306s" /&gt;
    &lt;Property name="ScannerDisplayName" value="Color-P13 Shade" /&gt;
    &lt;Property name="ScannerFirmware" value="1.3.2" /&gt;
    &lt;Property name="ScannerRGBCalibrationAge" value="12.8305745717589" /&gt;
    &lt;Property name="ScannerSerialNumber" value="t1503c13013b" /&gt;
    &lt;Property name="ScanSource" value="TRIOS" /&gt;
    &lt;Property name="ScanTime" value="00:04:17.2219900" /&gt;
    &lt;Property name="SiteID" value="73906" /&gt;
    &lt;Property name="SubscanCount" value="680" /&gt;
    &lt;Property name="SupportsShadeMeasurement2" value="True" /&gt;
    &lt;Property name="SurfaceArea" value="3389" /&gt;
    &lt;Property name="TimeStampUTC" value="2015-03-31 07:27:58" /&gt;
    &lt;Property name="SourceApp" value="TRIOS.exe#206342 - 2014-12-02 15:04:08 (build 1.3.3.1)#2014-12-02 14.05[NS]+OrthoAnalyzer.exe#Orthodontics 2013-1 (build 1.5.1.3)#2014-10-29 01.14" /&gt;
  &lt;/Properties&gt;
&lt;/HPS&gt;
</code></pre>
</details>
<p>Try to save this data set in .obj or .ply format directly from your scanning software.</p>
<p>The file format is quite easy to decode, so implementing a reader for it would take probably only a couple of days.</p>

---
