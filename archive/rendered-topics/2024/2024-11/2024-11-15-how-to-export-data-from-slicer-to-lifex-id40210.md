---
topic_id: 40210
title: "How To Export Data From Slicer To Lifex"
date: 2024-11-15
url: https://discourse.slicer.org/t/40210
---

# How to export data from Slicer to LifeX?

**Topic ID**: 40210
**Date**: 2024-11-15
**URL**: https://discourse.slicer.org/t/how-to-export-data-from-slicer-to-lifex/40210

---

## Post #1 by @Ann_Jacob (2024-11-15 06:05 UTC)

<p>Hello,<br>
I need to export brain ROIs from Slicer and then use them in LifeX. However, something goes wrong and LifeX doesn’t display the ROIs, on top of flashing the “Inconsistent ROI size” warning.<br>
Both images (patient head + ROIs) have the same size: 176x256x256, so that’s not where the issue comes from.</p>
<p>So far I have been trying to:</p>
<ul>
<li>import the ROI file as a binary label map (+ the corresponding table),</li>
<li>convert it to segmentation mode so I can delete the ROIs I don’t need, then back to binary map,</li>
<li>export it to files as Nifti.<br>
I have tried also to make sure the MRI patient image is set as the reference geometry for the structure set in Segmentations module (as per that post: <a href="https://discourse.slicer.org/t/issue-with-mask-exported-from-slicer/16517/6" class="inline-onebox">Issue with mask exported from Slicer  - #6 by lassoan</a>) but it didn’t help.</li>
</ul>
<p>So, does anyone know how to export suitable data for LifeX from Slicer?</p>
<p>Thanks in advance.<br>
Best regards,<br>
A. Jacob</p>

---

## Post #2 by @Ann_Jacob (2024-11-18 13:50 UTC)

<p>In case someone else runs into the same issue later on: Slicer doesn’t take into account the image rotation (common for neurological scans), while LifeX does. The error therefore stems from the fact the base image is rotated while the segmentation isn’t.</p>
<p>To fix it, you need to uncheck the box in LIFEx : Settings/Series/IOP. (IOP should be “false”)</p>

---

## Post #3 by @pieper (2024-11-18 13:58 UTC)

<p>I’m glad you got this to work, and thanks for reporting back to help future users <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Of course Slicer does take into account the orientation of the image acquisition, so the underlying issue is probably different assumptions in LifeX about what the nifti file means.  If you are interested to look further you could use the Volume Information panel in the Volumes module of Slicer to look at the orientations of the dicom and nifti data to confirm that they are rotated according to the acquisition and line up in Slicer.  If ignoring the ImageOrientationPatient makes it work in LifeX that’s okay, but in general it can be important not to lose that information since you may want to overlay other images that are in the same FrameOfReference but acquired at different orientations (or spacings, fields of view, etc).</p>
<p>Sorry but I don’t think folks here have experience with or access to LifeX.</p>

---

## Post #4 by @Ann_Jacob (2024-11-18 15:19 UTC)

<p>According to Slicer (in the Volume Information panel), the base image and the exported segmentation file have the same dimensions and orientation. I guess LifeX must read the header info differently…</p>

---
