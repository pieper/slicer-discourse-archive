# Change series name

**Topic ID**: 22406
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/change-series-name/22406

---

## Post #1 by @TommyTurner (2022-03-09 13:30 UTC)

<p>Hello everyone ! I am a French student in biomechanical engineering and i am new to the DICOM images treatment field. I am using 3D Slicer for bone segmentation and I wanted to export some image series to ImageJ from Slicer to measure some parameters. I have today 4 different DICOM series of acquisition and for 3 of them I used the “export to file system” to do so. But for the final one, it displays me an error.<br>
I think that this is due to the series name with a “ç” which maybe canno’t be ridden.<br>
So my question is : is there a way to change the name to the serie or directly the tag from the image sequence files of the DICOM ? I saw some topic on internet about this but seems complicated for such a simple thing…<br>
I tried to bypass this problem by using the “export to DICOM” after loading the file but the quality of the images is really weird ( round image with brown tint) …<br>
Thanks for your help !</p>

---

## Post #2 by @lassoan (2022-03-09 14:54 UTC)

<p>DICOM support of ImageJ is very poor. I would recommend to export to nrrd, nifti, or mha file format instead.</p>
<p>What analysis you would like to do in ImageJ? You might be able to do those in Slicer and that could simplify your workflow.</p>

---

## Post #3 by @TommyTurner (2022-03-09 14:59 UTC)

<p>Hello Iassoan ! Thanks for your reactivity ! Actually, ImageJ is a software that i used quite a bit this year, so i feel comfortable with it. I am doing images density calibration on it as well as grey scale measurement and binarization curve plotting.<br>
I will try your pieces of advice and will give you a feedback !<br>
Thanks</p>

---

## Post #4 by @lassoan (2022-03-09 16:47 UTC)

<p>ImageJ is very nice software if you work with 2D images but it is extremely limited for 3D visualization and analysis. Another issue is that it is implemented in Java, so you cannot easily bring in tools from the vast Python ecosystem.</p>
<p>Density calibration, grayscale measurements, plots, etc. are all supported in Slicer. Let us know if you want to explore these.</p>

---
