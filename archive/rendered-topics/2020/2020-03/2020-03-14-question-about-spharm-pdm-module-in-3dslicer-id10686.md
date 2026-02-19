---
topic_id: 10686
title: "Question About Spharm Pdm Module In 3Dslicer"
date: 2020-03-14
url: https://discourse.slicer.org/t/10686
---

# Question about spharm-pdm module in 3DSlicer

**Topic ID**: 10686
**Date**: 2020-03-14
**URL**: https://discourse.slicer.org/t/question-about-spharm-pdm-module-in-3dslicer/10686

---

## Post #1 by @pecca (2020-03-14 15:50 UTC)

<p>Operating system:win10<br>
Slicer version:3dslicer 4.8.0<br>
i want to use SPHARM-PDM to analysis nii format data,when i run ShapeAnalysisMoudle it shows error in step 0:SegPostProcessStatus:compeleted with errors.Detials say that “No input data assigned to “Input Image”” ,how can i solve it?thx to tell<br>
:</p>

---

## Post #2 by @pecca (2020-03-14 15:50 UTC)

<p>when i use spharm-pdm moudle to analysis nii format data,run ShapeAnalysisMoudle shows error like this<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebeb3c3798854de8e1ea200ad46d3f4a2ba1f52f.png" alt="Q2" data-base62-sha1="xF2c4pMacuwHynoTkJL5GOEDvrx" width="476" height="123"><br>
detials shows this<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82f4e120a6d552005ecc72b528665200f1ca0bb7.png" alt="Q22" data-base62-sha1="iGuIOGrzO0bZKMvaxduxtdrguZF" width="479" height="106"> saying that no input data assigned to “Input Image”<br>
how can i solve it?<br>
thx for tell</p>

---

## Post #3 by @lassoan (2020-03-18 03:19 UTC)

<p>Selecting an input image should fix the issue.</p>

---

## Post #4 by @pecca (2020-03-18 04:03 UTC)

<p>But I have choose the right path,slicer just can’t read the data file.<br>
Here is my data path <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0f0d995597dd8c3f7f7d235ae5fa6027463b1f5.png" alt="dataloc" data-base62-sha1="tOnkBYqHgNCShLkPCwBvG22NkON" width="420" height="343"><br>
And here is slicer input <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85676ddd755bf75d92f1fbc2e7b6c210cc6b899f.png" alt="path" data-base62-sha1="j296azlEdgNvSHoVLPUkTpOhSY7" width="593" height="121"></p>

---

## Post #5 by @lassoan (2020-03-18 04:11 UTC)

<p>Have you tried to follow the exact steps described in <a href="http://salt.slicer.org/documentation/">SlicerSALT tutorials</a>?</p>
<p><a class="mention" href="/u/bpaniagua">@bpaniagua</a> do you have any specific suggestion?</p>

---

## Post #6 by @pecca (2020-03-18 04:52 UTC)

<p>Yes,i follow the tutorials step by step but always shows the same question.<br>
Does slicer need other software installed like QT or VTK?</p>

---

## Post #7 by @lassoan (2020-03-18 04:56 UTC)

<p>Slicer and required extensions are all you need. SlicerSALT has all the required extensions bundled.</p>

---

## Post #8 by @pecca (2020-03-18 10:34 UTC)

<p>thank you very much!However,another question appears when i use SAPHARM-PDM in slicesault(version2.2.1),first step output nrrd format data which expected to be nii format data,<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21124f70d139bddc99d2d9837a89859fbdfade95.png" alt="2" data-base62-sha1="4IyZ8VHabWJADz3OvkMWGO45xQx" width="528" height="133"><br>
How can i solve it?</p>

---

## Post #9 by @lassoan (2020-03-18 13:19 UTC)

<p>Nifti (.nii) and NRRD file formats should work equally well. If you suspect that spharm expects one or the other then you can convert your images by loading them into Slicer and saving them - choosing the preferred format in “File format” column.</p>

---
