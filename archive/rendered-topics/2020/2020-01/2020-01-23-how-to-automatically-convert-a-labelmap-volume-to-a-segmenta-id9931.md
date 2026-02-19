---
topic_id: 9931
title: "How To Automatically Convert A Labelmap Volume To A Segmenta"
date: 2020-01-23
url: https://discourse.slicer.org/t/9931
---

# How to automatically convert a labelmap volume to a segmentation node upon loading labelmap volume

**Topic ID**: 9931
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/how-to-automatically-convert-a-labelmap-volume-to-a-segmentation-node-upon-loading-labelmap-volume/9931

---

## Post #1 by @Vincent_C (2020-01-23 22:43 UTC)

<p>Hi,</p>
<p>I want to script Slicer to automatically convert labelmap volume to a segmentation node when I load the labelmap volume, rather than having to right-click and convert it through the GUI. How can I achieve this? Can this be done in .slicerrc.py?</p>
<p>Thanks</p>

---

## Post #2 by @aiden.zhu (2020-01-23 23:16 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D</a></p>

---

## Post #3 by @lassoan (2020-01-23 23:28 UTC)

<p>If you use a recent Slicer Preview version then you can load nrrd and nifti files directly as segmentation (just choose <code>Segmentation</code> in the Description column in Add Data dialog). If you make the segmentation filename end with <code>.seg.nrrd</code> then Segmentation is selected automatically.</p>

---

## Post #4 by @Vincent_C (2020-01-24 00:17 UTC)

<p>Hi Aiden,</p>
<p>Thanks for the reply - Yes I have copied and pasted that script into .slicerrc.py. Although when I load a volume as a LabelMap, it does not automatically get converted to a segmentation node. I am a novice user - is there something I need to specify in the script?</p>
<p>Thanks</p>

---

## Post #5 by @aiden.zhu (2020-01-24 00:44 UTC)

<aside class="quote no-group" data-username="Vincent_C" data-post="4" data-topic="9931">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincent_c/48/5759_2.png" class="avatar"> Vincent_C:</div>
<blockquote>
<p>novice</p>
</blockquote>
</aside>
<p>Do you use python? if yes, maybe I may try to send you a loadable python script so you may do it by just clicking a button.</p>

---

## Post #6 by @Vincent_C (2020-01-24 01:16 UTC)

<p>Hi Aiden,</p>
<p>That is a kind offer! But I do not use python. I am hoping for a solution that can be directly applied to the slicerrc.py.</p>
<p>To give more context, I am loading pairs of volumes: one Scalar and one LabelMap volume - all one after the other. It is tedious to have to right click and convert the LabelMap volume to a segmentation node to perform edits. Is there a way that I can script slicerrc.py to automatically convert all LabelMap volume data to a segmentation node?</p>
<p>Thanks</p>

---

## Post #7 by @lassoan (2020-01-24 01:19 UTC)

<p>It sounds like you need CaseIterator extension, which is developed for iterating through a set of volumes and labelmaps. We use this for AI segmentation for generating training data and quality check and recently got grant funding to improve it further, based on what users need. So, if you have any feedback or suggestion then let us know.</p>

---

## Post #8 by @Vincent_C (2020-01-25 01:34 UTC)

<p>Hi,</p>
<p>So, the script below only allows me to convert a labelmap volume that has already been added to the scene. Is there a way to modify the script so that it applies to all LabelMap volumes I load even if they have not been added to the scene?</p>
<p>labelmapVolumeNode = getNode(‘my_labelmap_name’)<br>
seg = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLSegmentationNode’)<br>
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, seg)</p>

---

## Post #9 by @lassoan (2020-01-25 01:37 UTC)

<p>In recent Slicer Preview releases, you can load the volume file directly as segmentation node. No need for an intermediate labelmap.</p>

---
