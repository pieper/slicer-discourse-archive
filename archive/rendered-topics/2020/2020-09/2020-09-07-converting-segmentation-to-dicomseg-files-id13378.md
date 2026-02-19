---
topic_id: 13378
title: "Converting Segmentation To Dicomseg Files"
date: 2020-09-07
url: https://discourse.slicer.org/t/13378
---

# Converting segmentation to DICOMSeg files

**Topic ID**: 13378
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/converting-segmentation-to-dicomseg-files/13378

---

## Post #1 by @Gabriel_T (2020-09-07 17:23 UTC)

<p>I am trying to convert nrrd files to dicom seg files.<br>
My primary volume is a CT volume in .nrrd format which I converted from numpy format. I saved the segmentation to numpy format which I also converted to nrrd format. So basically I am loading two nrrd files, one the CT volume and the other the segmentation volume. Then I loaded the CT Volume as volume and segmentation as labelmap. I have the Quantitative Reporting extension installed.<br>
I selected the CT volume as primary volume like below screenshot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684000f00238d8b3efa5ecb53472baeb436d16f0.png" data-download-href="/uploads/short-url/eSeMCeFqFd3Q2vleQVyLbkJmL1m.png?dl=1" title="segmenteditor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684000f00238d8b3efa5ecb53472baeb436d16f0_2_690x233.png" alt="segmenteditor" data-base62-sha1="eSeMCeFqFd3Q2vleQVyLbkJmL1m" width="690" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684000f00238d8b3efa5ecb53472baeb436d16f0_2_690x233.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684000f00238d8b3efa5ecb53472baeb436d16f0_2_1035x349.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684000f00238d8b3efa5ecb53472baeb436d16f0_2_1380x466.png 2x" data-dominant-color="DFE8ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmenteditor</span><span class="informations">1899×642 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83c1c77bc1e1e2ae5061e732cd5a2806d43a3f0.png" data-download-href="/uploads/short-url/x8ryLIsVOLpOMTvLyOHCvArmha0.png?dl=1" title="hierarchy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83c1c77bc1e1e2ae5061e732cd5a2806d43a3f0_2_690x272.png" alt="hierarchy" data-base62-sha1="x8ryLIsVOLpOMTvLyOHCvArmha0" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83c1c77bc1e1e2ae5061e732cd5a2806d43a3f0_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83c1c77bc1e1e2ae5061e732cd5a2806d43a3f0_2_1035x408.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83c1c77bc1e1e2ae5061e732cd5a2806d43a3f0_2_1380x544.png 2x" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">hierarchy</span><span class="informations">1949×769 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when I try to export it I get error<br>
File “”, line 2, in <br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 350, in export<br>
exporter.export(exportable.directory, segFileName, metadata)<br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 499, in export<br>
absolutePaths=True)<br>
File “C:/Users/gabri/AppData/Roaming/NA-MIC/Extensions-29335/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules/DICOMSegmentationPlugin.py”, line 575, in getDICOMFileList<br>
instanceUIDs = volumeNode.GetAttribute(attributeName)<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetAttribute’</p>
<p>and nothing gets exported. I can send the corresponding files along if it helps.</p>

---

## Post #2 by @lassoan (2020-09-07 17:32 UTC)

<p>Ok, if you save your scene as a .mrb file, upload it somewhere, and post the link here then I’ll have a look.</p>

---

## Post #3 by @Gabriel_T (2020-09-07 17:46 UTC)

<p>Thank you!</p>
<p>I uploaded the .mrb file here<br>
<a href="https://easyupload.io/6664f9" class="onebox" target="_blank" rel="nofollow noopener">https://easyupload.io/6664f9</a></p>

---
