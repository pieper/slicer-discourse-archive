---
topic_id: 48121
title: "Correct workflow for loading 4D CT cardiac data"
date: 2026-09-11
url: https://discourse.slicer.org/t/48121
last_bumped: 2026-09-14T08:41:53.407Z
---

# Correct workflow for loading 4D CT cardiac data

**Topic ID**: 48121
**Date**: 2026-09-11
**URL**: https://discourse.slicer.org/t/correct-workflow-for-loading-4d-ct-cardiac-data/48121

---

## Post #1 by @arumiat (2026-09-11 10:01 UTC)

<p>Hi Slicer Community,</p>
<p>I have a .nii file which is a 4D-gated cardiac CT but I am struggling to load it in Slicer in a way whereby I can watch the heart beating. Is there a specific workflow I need to follow.</p>
<p>So far I have</p>
<ul>
<li>Add Data</li>
<li>make sure ‘Volume’ is checked</li>
<li>go to Sequences module</li>
</ul>
<p>But I am not seeing any of the green buttons for playing the sequence - they are all greyed out.</p>
<p>It could be the case the file is missing the header or something?</p>
<p>Happy to share the file if needed.</p>

---

## Post #2 by @pieper (2026-09-11 16:10 UTC)

<p>See this conversation for context: <a href="https://discourse.slicer.org/t/4d-nifti-flipped-and-rotated-about-90-deg/48056" class="inline-onebox">4D NifTi flipped and rotated about 90-deg</a></p>

---

## Post #3 by @Deep_Learning (2026-09-11 19:34 UTC)

<p>I would suggest making an nii.gz for each phase.  These are read in normally.  Then they are added to a Sequence.  This definately works.</p>

---

## Post #4 by @lassoan (2026-09-14 04:16 UTC)

<p>Do you still have the original DICOM image of the 4D cardiac CT? You can load that directly into Slicer using the DICOM module.</p>
<p>We have refused to add better support for nifti, as it is such a problematic image file format (quite complex yet very limited). However, nowadays we could much more easily add new features and maintain them, so I’m leaning towards improving a few things - including enable reading/writing of 4D/5D nifti images.</p>

---

## Post #5 by @arumiat (2026-09-14 08:41 UTC)

<p>Thanks all for the responses. What is unexpected is that I can load the .nii here and the sequence is recognised and played: <a href="https://brainbrowser.cbrain.mcgill.ca/volume-viewer" class="inline-onebox" rel="noopener nofollow ugc">BrainBrowser Volume Viewer v2.5.2</a></p>
<p>Is there anyone that might be willing to download the volume if I DMed a link, and try it to see if it is just my user error rather than an issue with the data itself?</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fecbd937c4b16018cfcc934a4cf6c11c6da79fea.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c6c3fa7bcc659e282a9d5c203370cb16b96d1d7.jpeg" data-video-base62-sha1="Am21imBDVeur9IBUv2Ijuq4HKr0.mp4">
  </div><p></p>

---
