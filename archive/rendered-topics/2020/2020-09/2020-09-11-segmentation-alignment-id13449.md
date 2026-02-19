---
topic_id: 13449
title: "Segmentation Alignment"
date: 2020-09-11
url: https://discourse.slicer.org/t/13449
---

# Segmentation Alignment

**Topic ID**: 13449
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/segmentation-alignment/13449

---

## Post #1 by @yoomi (2020-09-11 19:32 UTC)

<p>Hi everyone,</p>
<p>I have a pre-determined VOI segmentation and DCE MRI sequence in DICOM format, and want to overlay/align them. What is the best way to go about this? I was thinking about converting the VOI segmentation to a labelmap volume matched to reference geometry of the DCE MRI’s. Would this work to align?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-09-12 02:00 UTC)

<p>Yes, you should be able to load the segmentation as a segmentation node and the MRI as a volume node and Slicer will overlay them correctly. There are many visualization parameters that you can tune in Segmentations module’s Display section.</p>

---

## Post #3 by @yoomi (2020-09-13 00:03 UTC)

<p>Hi Andras,</p>
<p>When I try to do this, I load the MRI as a volume using slicer.util.loadVolume(), and then want to use the code below. However, I’m not sure how to (1) get the MRML node of the loaded MRI volume and (2) load the segmentation before getting the segmentation node as below. Thanks!</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, referenceVolumeNode)
</code></pre>

---

## Post #4 by @lassoan (2020-09-13 00:48 UTC)

<p>Does everything work correctly using the GUI?</p>
<p>What are the input files on disk that you would like to load using Python?</p>

---

## Post #5 by @yoomi (2020-09-15 01:56 UTC)

<p>Hi Andras,</p>
<p>I am able to load the MRI dicom’s as a volume, but I am having trouble loading the segmentation. The segmentation file is also in dicom format, so I am trying to load as labelmap through GUI following instructions (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html</a>) but I don’t see this option. What do you recommend?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2020-09-15 03:35 UTC)

<aside class="quote no-group" data-username="yoomi" data-post="5" data-topic="13449">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a6a055/48.png" class="avatar"> yoomi:</div>
<blockquote>
<p>The segmentation file is also in dicom format</p>
</blockquote>
</aside>
<p>What information object is used for storing the segmentation: DICOM RT structure set or DICOM Segmentation Object?</p>

---

## Post #7 by @yoomi (2020-09-15 03:37 UTC)

<p>DICOM segmentation object</p>

---

## Post #8 by @lassoan (2020-09-15 03:39 UTC)

<p>DICOM segmentation object must be loaded via DICOM module and it requires Quantitative Reporting extension.</p>

---

## Post #10 by @yoomi (2020-09-15 03:52 UTC)

<p>Hi Andras,</p>
<p>Please ignore my last reply, I was able to get it to work by putting the seg files in the same folder. The new problem I have is that 2 of the segmentation files (specifically PE segmentations) are not able to load as a DICOMsegmentation-- do you know why this could be? Thanks</p>

---

## Post #11 by @lassoan (2020-09-15 04:07 UTC)

<p>Use the latest Slicer Preview Release. If the import still does not work as expected then check if there are any errors or warnings in the log.</p>

---

## Post #12 by @yoomi (2020-09-23 13:33 UTC)

<p>Hi Andras,</p>
<p>Luckily this worked – thank you. I have a follow - up question: to export a labelmap volume (based on the aligned MRI volume reference geometry with the segmentation file) to a file, what are the settings I should use in the segmentations module? Thank you</p>

---

## Post #13 by @lassoan (2020-09-23 15:06 UTC)

<p>In general, if you don’t need any special behavior, use default settings. To set a reference geometry for export, select the reference volume in Segmentations module / Export/import… / Advanced / Reference volume.</p>

---

## Post #14 by @yoomi (2020-09-23 15:13 UTC)

<p>What is the difference between the section to “export/import models and labelmaps” and “export to files”?</p>

---

## Post #15 by @lassoan (2020-09-23 15:31 UTC)

<p>Export/import models and labelmaps exports to nodes in the scene (that you can later save to files using Save data… window). “Export to files” saves directly to files.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> what geometry is used by “Export to files” when exporting nrrd/nifti? Probably we should add a reference volume selector there, too.</p>

---

## Post #16 by @Sunderlandkyl (2020-09-23 15:45 UTC)

<p>Export to file currently uses the reference geometry string. I believe it’s the same with both export to labelmap and export to files (with the exception of the reference volume selector). I’ll add a combo box to choose the reference volume.</p>

---

## Post #17 by @lassoan (2020-09-23 16:13 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="16" data-topic="13449">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>I’ll add a combo box to choose the reference volume.</p>
</blockquote>
</aside>
<p>That would be great, thank you!</p>

---
