---
topic_id: 9411
title: "Stl File Conversion"
date: 2019-12-06
url: https://discourse.slicer.org/t/9411
---

# Stl file conversion

**Topic ID**: 9411
**Date**: 2019-12-06
**URL**: https://discourse.slicer.org/t/stl-file-conversion/9411

---

## Post #1 by @arun_gopinathan (2019-12-06 13:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: I need to export the 3D model to .stl file<br>
Actual behavior: No option</p>
<p>Hello,<br>
I have started to use 3D Slicer for the past 3 days. I need to convert CT .jpg image file to a 3d model. after I have converted, I was unable to save it in .stl file format. There is no stl option have come.</p>
<p>Please kindly suggest me the suitable way to do it. I tried many youtube tutorials but no use.</p>
<p>Awaiting your esteemed support.</p>
<p>With Regards,<br>
Arun</p>

---

## Post #2 by @pieper (2019-12-06 15:15 UTC)

<p>Hi Arun -</p>
<p>Did you try the tutorials here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Image_Segmentation</a></p>
<p>Which step specifically didn’t work for you?</p>
<p>If you start with jpgs of a CT you’ll need to use this module: <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/VectorToScalarVolume">https://www.slicer.org/wiki/Documentation/4.10/Modules/VectorToScalarVolume</a></p>
<p>But in general jpg is a very bad format for CT since it loses detail and is only 8 bit instead of the normal 12 bit.  Try to get DICOM if you want a good model.</p>

---
