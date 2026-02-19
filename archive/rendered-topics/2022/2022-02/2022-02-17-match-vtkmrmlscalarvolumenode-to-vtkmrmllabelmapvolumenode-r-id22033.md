---
topic_id: 22033
title: "Match Vtkmrmlscalarvolumenode To Vtkmrmllabelmapvolumenode R"
date: 2022-02-17
url: https://discourse.slicer.org/t/22033
---

# Match vtkMRMLScalarVolumeNode to vtkMRMLLabelMapVolumeNode retrieved from vtkMRMLSegmentationNode

**Topic ID**: 22033
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/match-vtkmrmlscalarvolumenode-to-vtkmrmllabelmapvolumenode-retrieved-from-vtkmrmlsegmentationnode/22033

---

## Post #1 by @tetyanaloskutova (2022-02-17 21:59 UTC)

<p>Hi, I have 23 scan images (vtkMRMLScalarVolumeNode ) and matching to some of them 13 vtkMRMLLabelMapVolumeNode retrieved from vtkMRMLSegmentationNode. They are not in order, i.e. 1st vtkMRMLScalarVolumeNode  matches 7th vtkMRMLLabelMapVolumeNode. I can see which of them match in Slicer front end but I do not know which class field created from reading  *.dcm files contain this information.<br>
Can someone point me in the right direction? Thanks!</p>

---

## Post #2 by @lassoan (2022-02-17 23:04 UTC)

<p>It all depends how you organized your data in your scene. For example, you can associate nodes using MRML node references, subject hierarchy folders, or DICOM UIDs. Can you post a screenshot of the tree in the Data module?</p>

---

## Post #3 by @tetyanaloskutova (2022-02-17 23:23 UTC)

<p>Hi Andras, thanks for your answer! I attach the screenshot from the Scene if that is what you meant… However, I do not create or load the scene when I read the files, so preferably I would like to match the data in two folders (“Ax T2 FSE” and “Ax T2 FSE Giloma Segmentation Corrected” on the screenshot) without referencing the scene. Would DICOM UID be the right approach? I can literally see the references in the dcm files but parsing them manually sounds like reinventing the wheel…<br>
Thanks a lot!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84cc21131aeceec04540efc2be39c9ec46392648.png" data-download-href="/uploads/short-url/iWMmZH6VvOPyPG2WEajnkM6AXaM.png?dl=1" title="Screenshot 2022-02-17 181333" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84cc21131aeceec04540efc2be39c9ec46392648_2_690x399.png" alt="Screenshot 2022-02-17 181333" data-base62-sha1="iWMmZH6VvOPyPG2WEajnkM6AXaM" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84cc21131aeceec04540efc2be39c9ec46392648_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84cc21131aeceec04540efc2be39c9ec46392648_2_1035x598.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84cc21131aeceec04540efc2be39c9ec46392648.png 2x" data-dominant-color="E6EEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-02-17 181333</span><span class="informations">1127×652 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-02-18 01:16 UTC)

<p>DICOM Segmentation Object refers to a DICOM image file at many levels (see <code>ReferencedSOPInstanceUID</code> and <code>SeriesInstanceUID</code> tags by right-clicking on the segmentation object and choosing “View DICOM metadata”).</p>
<p>I had a quick look and it seemed that Slicer’s DICOM Segmentation Object importer uses the <a href="https://dicom.innolitics.com/ciods/segmentation/common-instance-reference/00081115">SeriesInstanceUID</a> in the first ReferencedSeriesSequence.</p>

---

## Post #5 by @tetyanaloskutova (2022-02-18 23:19 UTC)

<p>Thanks Andras, the links you gave helped! Finally, it turned out that reading the segmentation file using pydicom gives the correct sequence.</p>

---
