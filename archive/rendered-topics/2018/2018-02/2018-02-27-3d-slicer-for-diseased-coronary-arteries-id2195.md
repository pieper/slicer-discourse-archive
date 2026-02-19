---
topic_id: 2195
title: "3D Slicer For Diseased Coronary Arteries"
date: 2018-02-27
url: https://discourse.slicer.org/t/2195
---

# 3D Slicer for Diseased Coronary Arteries

**Topic ID**: 2195
**Date**: 2018-02-27
**URL**: https://discourse.slicer.org/t/3d-slicer-for-diseased-coronary-arteries/2195

---

## Post #1 by @Kaitlin_Logie (2018-02-27 01:29 UTC)

<p>Hi there,</p>
<p>I am a research assistant working on a project called the Coronary Atlas. As part of this project we extract coronary arteries from CT scans. We currently use the vmtk module for 3D slicer for this without any issues with normal cases. However for diseased cases it is a lot different. I was wondering if anyone is working on or know of someone who is working on something similar and has any pointers on how we can efficiently and accurately segment coronary arteries that have disease and high calcification out of CT scans.</p>
<p>Looking forward to your reply,<br>
Kaitlin</p>

---

## Post #2 by @Chiara_Quartana (2020-04-03 07:53 UTC)

<p>Hi <a class="mention" href="/u/kaitlin_logie">@Kaitlin_Logie</a>, I’m a biomedical engineering student. I’m trying to learn how to obtain a femoral-coronary artery path segmentation from CT_Thorax_Abdomen images. Do you have any advice about which tools I should use? Moreover, do you know what are the methods (or the algorithms) that 3d slicer uses to reach this segmentation?</p>

---

## Post #3 by @lassoan (2020-04-04 21:00 UTC)

<p>If you have contrasted image then this is an easy segmentation task. See for example the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/">two “aorta segmentation” segmentation recipes</a>. For more information about segmentation, check out these <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">segmentation tutorials</a>.</p>

---

## Post #5 by @ames (2021-09-22 13:46 UTC)

<p>Hi Kaitlin,</p>
<p>At the moment I am also working with CT of coronary arteries with a high amount of calcification. Did you manage to solve your problem?</p>

---

## Post #6 by @lassoan (2021-09-23 01:10 UTC)

<p>You can also have a look at this tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="aeOFl19fh_c" data-video-title="Coronary vessel segmentation on cardiac CT images" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=aeOFl19fh_c" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/aeOFl19fh_c/maxresdefault.jpg" title="Coronary vessel segmentation on cardiac CT images" width="" height="">
  </a>
</div>

<p>If this does not help and you don’t get other answers here then I would recommend to create a new post and describe your problem in more detail, with the main challenges illustrated with a few images.</p>

---

## Post #7 by @ames (2021-09-23 06:08 UTC)

<p>Thanks Andras for your suggestion, but I have tried to replicate this video before, but it is not what I am looking for. I have created a new post with more details about my problem <a href="https://discourse.slicer.org/t/3d-slicer-for-segmentation-of-lima-lad-bypass-with-severe-calcification/19820" class="inline-onebox">3D Slicer for segmentation of LIMA-LAD Bypass with severe calcification</a></p>

---
