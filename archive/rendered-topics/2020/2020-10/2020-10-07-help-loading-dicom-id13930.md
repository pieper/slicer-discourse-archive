# Help loading DICOM

**Topic ID**: 13930
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/help-loading-dicom/13930

---

## Post #1 by @Felipe_Suntaxi (2020-10-07 21:04 UTC)

<p>Hello. I’m new to the Slicer DMRI. I’m trying to load some dicom data but I get this error.<br>
Diffusion-weighted DICOM Import (DWIConvert) standard error:</p>
<p>Exception thrown while reading DICOM volume</p>
<p>itk::InvalidRequestedRegionError (0000000790CFADE8)<br>
Location: “unknown”<br>
File: d:\d\p\slicer-0-build\itk\modules\io\imagebase\include\itkImageFileReader.hxx<br>
Line: 343<br>
Description: ImageIO returns IO region that does not fully contain the requested regionRequested region: ImageRegion (0000000790CFADB0)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [896, 896, 1]<br>
StreamableRegion region: ImageRegion (0000000790CFAE10)<br>
Dimension: 3<br>
Index: [0, 0, 0]<br>
Size: [257, 214, 1]</p>
<p>Any help will be appreciated. Thanks</p>

---

## Post #2 by @zhangfanmark (2020-10-08 19:43 UTC)

<p>Hi <a class="mention" href="/u/felipe_suntaxi">@Felipe_Suntaxi</a></p>
<p>I am not sure what is going wrong here. Can you try to load your data using our new module, DCM2NiixGui? It is available in the nightly release.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @yuquant (2022-06-01 08:51 UTC)

<p>I read some DX dicom images using SimpleITK,and got the same error.Just because the series uid is the same and actually they are independent series, SimpleITK regards them like one series.I read the image one by one,problem solved.</p>

---
