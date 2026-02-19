---
topic_id: 38334
title: "Computing Intersection Between Volume And Segmentation"
date: 2024-09-11
url: https://discourse.slicer.org/t/38334
---

# Computing intersection between volume and segmentation

**Topic ID**: 38334
**Date**: 2024-09-11
**URL**: https://discourse.slicer.org/t/computing-intersection-between-volume-and-segmentation/38334

---

## Post #1 by @Josh_Gregory (2024-09-11 21:03 UTC)

<p>Hi everyone,</p>
<p>I am dealing with some skull-stripped CTA scans that I have imported as a Volume and the corresponding segmentations imported as a Segmentation. I have some parts of the segmentation that do not map to the skull-stripped scan (i.e. the segmentation is of the neck but the skull-stripped scan does not have this). Is there a way edit the segmentation so that only the segmentations are the ones that intersect the CTA scans? I’ve attached an image of what I would like to do; the red circles show the segmentations that I would like to delete, and the green circles show the segmentations (around the brain stem) that I would like to keep.</p>
<p>Does anyone have any suggestions for how to do this?<br>
Thanks!</p>

---

## Post #2 by @pieper (2024-09-11 23:48 UTC)

<p>Not seeing the images - repost?</p>
<p>In any case you should be able to do what you describe with the Segment Editor and logical operations.</p>

---

## Post #3 by @Josh_Gregory (2024-09-12 00:05 UTC)

<p>Oops, sorry about that!</p>
<p>Here’s the image.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2802da4eace22f8d08326aacca251379f1a42e0f.png" alt="seg" data-base62-sha1="5HXd4rL7xlA1qazrx3B7oycaGvR" width="179" height="263"></p>
<p>I tried doing it with the Segment Editor, but it seemed as though i was running into issues due to the segmentations being a Segmentation and the scans being a Volume. I tried converting it to a LabelMapVolume and then that to a Segmentation, but each pixel was segmented instead.</p>

---

## Post #4 by @pieper (2024-09-12 00:23 UTC)

<p>You should just make a new segment and use the Threshold tool to select just the brain allowing overlap with the vessels.  Then use the logical operators to keep just the vessels that are also in the brain.  Use the CTA as the reference volume for thresholding.</p>

---

## Post #5 by @cpinter (2024-09-13 08:28 UTC)

<p>The figure in this section helps understanding the way how different data types interact in Slicer<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#review-loaded-data" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#review-loaded-data</a></p>
<p>We just released a new tutorial for segmentation. I think it would be helpful</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/Slicer/SlicerSegmentationFor3DPrintingTutorial">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSegmentationFor3DPrintingTutorial" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/862c2fa1b53412d2f648290bc35a5625/Slicer/SlicerSegmentationFor3DPrintingTutorial" class="thumbnail">

  <h3><a href="https://github.com/Slicer/SlicerSegmentationFor3DPrintingTutorial" target="_blank" rel="noopener">GitHub - Slicer/SlicerSegmentationFor3DPrintingTutorial: Segmentation for 3D Printing Tutorial for 3D...</a></h3>

    <p><span class="github-repo-description">Segmentation for 3D Printing Tutorial for 3D Slicer</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I suggest reading this page as well<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>

---
