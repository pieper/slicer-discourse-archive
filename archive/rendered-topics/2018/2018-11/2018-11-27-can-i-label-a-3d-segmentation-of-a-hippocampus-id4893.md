---
topic_id: 4893
title: "Can I Label A 3D Segmentation Of A Hippocampus"
date: 2018-11-27
url: https://discourse.slicer.org/t/4893
---

# Can I label a 3D segmentation of a hippocampus?

**Topic ID**: 4893
**Date**: 2018-11-27
**URL**: https://discourse.slicer.org/t/can-i-label-a-3d-segmentation-of-a-hippocampus/4893

---

## Post #1 by @abiorac (2018-11-27 16:39 UTC)

<p>Operating system: Mac OS Mojave<br>
Slicer version: 4.10<br>
Expected behavior: I want to be able to place a label on certain structures on a 3D view of the hippocampus (using the editor module) and have the label appear when looking at the hippocampus from the sagittal and coronal planes.<br>
Actual behavior:<br>
Hi,</p>
<p>I’m currently working on a project that requires identifying dentations on the inferior aspect of the hippocampus. I’ve been able to label points on the hippocampus using the editor module from the  sagittal and coronal views on 3D slicer, but it is easier to view these structures in 3D.</p>
<p>I’ve only recently received my laptop from the shop, so I haven’t been able to attempt this myself, but I’m curious as to whether or not I’m able to label a 3D hippocampus and have the label appear when looking at slices from other planes. If it is not, is there perhaps some other tool or program that could do this?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-11-29 05:25 UTC)

<p>Yes, painting segments on image slices and seeing it in other slices and in 3D view is readily available (make sure you use “Segment Editor module” not the legacy “Editor” module). To get started with segmentation, check out these tutorials: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>

---

## Post #3 by @abiorac (2018-12-03 21:38 UTC)

<p>Hi,</p>
<p>Thanks for your response. I’ve been able to label slices and see the labels appear in other slices and 3D view, so my question is it possible to label the 3D view of the hippocampus first, and then see those labels appear in the other slices?</p>

---

## Post #4 by @cpinter (2018-12-03 21:53 UTC)

<p>You can use some Segment Editor effects for segmentation in the 3D view such as Paint with a sphere brush or Scissors. However</p>
<ol>
<li>All effects work in the slice views, so you have much more options that way.</li>
<li>For segmentation you need to see the underlying anatomical volume, which is possible in the slice views, but not possible in the 3D view.</li>
</ol>
<p>What do you have in mind? I have a hard time imagining why you’d want to segment in the 3D view.</p>

---

## Post #5 by @abiorac (2018-12-03 22:26 UTC)

<p>So I’m currently looking at identifying hippocampal dentations in MRI scans. Up until this point, I’ve been labeling the dentations through the slice views. This method works, but it is difficult to know if we’ve missed some dentations, or labeled the same one more than once because I have have to look through a number of slices (which may have ‘smudges’ as people move around at times in the MRI). I’ve been able to view the hippocampus in 3D thanks to another student’s efforts in manually segmenting a hippocampus, and viewing these structures is much easier and more clear-cut in the 3D view. Therefore, I’m looking to see if I can label these dentations from the 3D view, as it is easier to visualize, and will help in the future when comparing inter-rater reliability.</p>

---

## Post #6 by @lassoan (2018-12-03 23:04 UTC)

<p>Yes, you can split up segments in the 3D view. Use Scissors effect, fill inside mode, and in masking settings select editable area to be “inside all segments”. See the <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/" rel="nofollow noopener">Craniotomy segmentation recipe</a> for an example.</p>

---
