---
topic_id: 15062
title: "3D Slicer Vmtk Extension On Mri Time Of Flight For Cerebrova"
date: 2020-12-14
url: https://discourse.slicer.org/t/15062
---

# 3D Slicer + VMTK extension on MRI Time-of-flight for cerebrovascular segmentation

**Topic ID**: 15062
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/3d-slicer-vmtk-extension-on-mri-time-of-flight-for-cerebrovascular-segmentation/15062

---

## Post #1 by @Jebs_Maf (2020-12-14 21:57 UTC)

<p>Operating system: Mac OS v.10.14.6<br>
Slicer version: v.4.11<br>
Expected behavior: I tried to segment the cerebrovasculature from MRI ToF images using the local threshold feature on “Segmentation”, as seen in this youtube tutorial <a href="https://youtu.be/caEuwJ7pCWs" rel="noopener nofollow ugc">here</a>. The tutorial uses CT images, but I wanted to repeat the same process on MRI ToF<br>
Actual behavior: The process got stuck on the “3D show” step as it wouldn’t recreate the volume rendering after the local threshold step.</p>
<p>Many of the other automated segmentations in 3D slicer use Houndsfield units, appropriate for CT, but I am trying to segment cerebrovasculature from MRI time-of-flight images.</p>
<p>Eventually, the goal is to take the segmented cerebrovasculature and run them through the VMTK extension in 3D slicer to take advantage of the vascular measures available as part of VMTK.</p>
<p>Any guidance on this would be much appreciated<br>
Thank you</p>

---

## Post #2 by @lassoan (2020-12-14 21:59 UTC)

<p>Can you post a few screenshots of your data set and how it appears in Slicer?</p>

---
