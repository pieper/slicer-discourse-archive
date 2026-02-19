---
topic_id: 1021
title: "Issue With Segmentation On Non Axial Volume"
date: 2017-09-08
url: https://discourse.slicer.org/t/1021
---

# Issue with segmentation on non-axial volume

**Topic ID**: 1021
**Date**: 2017-09-08
**URL**: https://discourse.slicer.org/t/issue-with-segmentation-on-non-axial-volume/1021

---

## Post #1 by @sleep_research (2017-09-08 13:18 UTC)

<p>I have been trying to segment a series of MRI scans however when I use the paint tool to highlight a section on a single slice it seems to get split over neighbouring slices.<br>
I have attached a screenshot to help explain.</p>
<p>Would anyone please be able to help me figure out what is going on?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47f289fe1a28d2686e84349b28cbccdf71fb06e6.jpeg" data-download-href="/uploads/short-url/agtxlCZ6B37bpgGQN2ewf2NpLqm.jpg?dl=1" title="Segmentation issue (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/47f289fe1a28d2686e84349b28cbccdf71fb06e6_2_690x376.jpg" alt="Segmentation issue (1)" data-base62-sha1="agtxlCZ6B37bpgGQN2ewf2NpLqm" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/47f289fe1a28d2686e84349b28cbccdf71fb06e6_2_690x376.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/47f289fe1a28d2686e84349b28cbccdf71fb06e6_2_1035x564.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/47f289fe1a28d2686e84349b28cbccdf71fb06e6_2_1380x752.jpg 2x" data-dominant-color="8A8B8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segmentation issue (1)</span><span class="informations">1500×819 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-09-08 13:29 UTC)

<p>You have a non-axis-aligned volume. For slice-by-slice segmentation it may be easier to align slice views with the image plane as described in this topic:</p>
<aside class="quote quote-modified" data-post="3" data-topic="546">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/display-issue-with-rt-structs-and-mr-volume/546/3">Display issue with RT structs and MR volume</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It seems that your MR volume axes are not aligned with patient anatomical axes. It’s not a problem, Slicer just shows slice viewers aligned with anatomical axes by default. Click “Rotate to volume plane” button in the slice view controller to align slice viewers to volume planes: 
[image] 
In the treatment planning software, did you draw contours with variable distance between them?
  </blockquote>
</aside>


---

## Post #3 by @sleep_research (2017-09-12 01:57 UTC)

<p>Hi, thank you so much for this!! It seems to have solved our problem, I never realised that button was there to align the scans.</p>
<p>Thanks again, your help is greatly appreciated!</p>

---
