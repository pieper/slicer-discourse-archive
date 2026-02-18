# Exporting Segmentations to DICOM

**Topic ID**: 251
**Date**: 2017-05-02
**URL**: https://discourse.slicer.org/t/exporting-segmentations-to-dicom/251

---

## Post #1 by @SLautenschlaeger (2017-05-02 20:30 UTC)

<p>Hi together,</p>
<p>I’d like to export segmentations to DICOM to import them in other planing systems. However I can only export the CT-Data Set and not the corresponding segmentations. Quantitative reporting and SlicerRT are installed.<br>
Any ideas what might be the problem ?</p>
<p>Best regards<br>
Stefan</p>

---

## Post #2 by @gcsharp (2017-05-02 22:58 UTC)

<p>Hi Stefan,<br>
Since you say “planning system,” I assume you want RT Structure Set.<br>
In that case, I think you need to create a study, put the segmentation into the same study as<br>
the CT, and then export the study (right click on study, choose export).<br>
Greg</p>

---

## Post #3 by @JK_Kim (2017-08-08 19:40 UTC)

<p>I am also having the same issue. I exported a CT and a RTSTRUCT from a planning system (Varian Eclipse), imported to Slicer (4.6.2), modified the structure, and then when I export the CT and modified segmentation it only exports the CT image. I opened the python inspector and I see the following error… It basically saying it cannot find vtkSegmentationCore. Is there anything that I am missing. I installed SlicerRT and Reporting modules.</p>
<p>=======<br>
Traceback (most recent call last):<br>
File “”, line 2, in <br>
File “C:/Users/jkim20/AppData/Roaming/NA-MIC/Extensions-25516/Reporting/lib/Slicer-4.6/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 339, in export<br>
self.exportAsDICOMSEG(exportablesCollection)<br>
File “C:/Users/jkim20/AppData/Roaming/NA-MIC/Extensions-25516/Reporting/lib/Slicer-4.6/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 374, in exportAsDICOMSEG<br>
import vtkSegmentationCore<br>
ImportError: No module named vtkSegmentationCore</p>

---

## Post #4 by @cpinter (2017-08-08 19:54 UTC)

<p><a class="mention" href="/u/jk_kim">@JK_Kim</a> It seems you’re actually exporting to DICOM SEG, not DICOM RTSS. Make sure you have the segmentation and the CT under the same study (which must have a patient parent), right click the study in Data module, select Export to DICOM… and make sure that RT is selected on the left under the tree.</p>
<p>Also I strongly recommend downloading a recent nightly.</p>

---

## Post #5 by @JK_Kim (2017-08-08 21:15 UTC)

<p>Thanks for the quick reply. It works well with the “RT” selected as the<br>
export type.<br>
Best regards,<br>
Jinkoo</p>

---

## Post #6 by @Hanaana (2017-08-09 13:11 UTC)

<p>Hello everyone,</p>
<p>I need your support. I am trying to convert my NIfTI data to DICOM data but<br>
until now I couldn’t do it in slicer while exporting my data.</p>
<p>The exported format is .sql . so it is possible to export my data as .dcm ?</p>
<p>Looking forward to hearing from you,</p>
<p>Hanaa</p>

---

## Post #7 by @cpinter (2017-08-09 13:35 UTC)

<p>Please follow the instructions two comments above.</p>
<p>In order to have a segmentation to export from nifti, you need to import the loaded labelmap volume to a segmentation in the Segmentations module’s Import/Export section at the bottom.</p>

---

## Post #8 by @lassoan (2017-08-29 13:44 UTC)

<p>A post was split to a new topic: <a href="/t/improve-an-existing-segmentation/964">Improve an existing segmentation</a></p>

---

## Post #9 by @Moran_Artzi (2019-02-28 11:48 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="251">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>ou need to import the loaded labelmap volume to a segmentation in the Segmentations module’s Impor</p>
</blockquote>
</aside>
<p>Going to Segmentations module’s Import/Export section without prior actio?<br>
Use the Segmentations modules Import/Export section without prior operation?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e70b0b5cac5b5be79a5f9f7d860ce2e000a0a7a4.png" alt="image" data-base62-sha1="wXTXp97xaFaChcNLjDv2GirWWri" width="532" height="167"></p>
<p>I can not import the file from there</p>

---
