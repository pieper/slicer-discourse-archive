---
topic_id: 35604
title: "Create A Segment With A List Of Points That Are Segment Boun"
date: 2024-04-18
url: https://discourse.slicer.org/t/35604
---

# Create a segment with a list of points that are segment boundaries

**Topic ID**: 35604
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/create-a-segment-with-a-list-of-points-that-are-segment-boundaries/35604

---

## Post #1 by @sima (2024-04-18 15:15 UTC)

<p><strong>Hi to all</strong><br>
I have a list of points in each CT slice that is obtained from python scripts.<br>
My ultimate goal is to have a closed surface segment where these points precisely define its boundaries. In other words, the space enclosed by the points should be filled, and the area outside should be empty.</p>
<p>In my attempt, I connected these points to form a closed markups curve like picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23df0b22fea963f95dd2e3423d1f969a299008e7.jpeg" data-download-href="/uploads/short-url/57kzXoetqVbQo3xRbaiRaewhkwv.jpeg?dl=1" title="markups" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23df0b22fea963f95dd2e3423d1f969a299008e7_2_690x411.jpeg" alt="markups" data-base62-sha1="57kzXoetqVbQo3xRbaiRaewhkwv" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23df0b22fea963f95dd2e3423d1f969a299008e7_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23df0b22fea963f95dd2e3423d1f969a299008e7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23df0b22fea963f95dd2e3423d1f969a299008e7.jpeg 2x" data-dominant-color="828282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">markups</span><span class="informations">927×553 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
then converted it to a model and then to a segment. However, the resulting segment appeared as a narrow closed strip with an empty interior like below picture, so I did not achieve the ultimate goal I had in mind.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d60d179766950f40b381e9fef86047adbe260d.jpeg" data-download-href="/uploads/short-url/mWOZRgfwGL7Ktqb6C0Q5fxUDM3H.jpeg?dl=1" title="segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d179766950f40b381e9fef86047adbe260d_2_690x410.jpeg" alt="segment" data-base62-sha1="mWOZRgfwGL7Ktqb6C0Q5fxUDM3H" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a0d60d179766950f40b381e9fef86047adbe260d_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d60d179766950f40b381e9fef86047adbe260d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0d60d179766950f40b381e9fef86047adbe260d.jpeg 2x" data-dominant-color="8C8C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment</span><span class="informations">849×505 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone have any ideas or solutions on how to create a closed surface segment using list of points?</p>
<p>It’s important to say that my list of points varies in each slice, and ultimately, I want to combine the segments obtained from each slice to create a three-dimensional segment.</p>
<p>I would be very happy if someone could help me achieve this goal.</p>

---

## Post #2 by @LeidyMoraV (2024-04-23 19:17 UTC)

<p>Maybe ‘Dinamic Modeler’ Module can help you.</p>

---

## Post #3 by @cpinter (2024-04-29 11:38 UTC)

<p>If you want to do this in 3D, I suggest the Surface Cut effect from the SegmentEditorExtraEffects extension (download from Extensions Manager).</p>
<p>If it’s 2D, my only idea is the Draw effect in Segment Editor.</p>

---

## Post #4 by @lassoan (2024-04-30 02:17 UTC)

<p>If your contour points are ordered then you can create a parallel contour segment representation from them - see how it is implemented on the ImportOsirixROI module in Sandbox extension.</p>
<p>If you have very dense boundary point set the  you can use VTK surface reconstruction filters.</p>
<p>This is a pretty rare need, so there is a chance that you could find a better overall approach to solve your task. Can you tell a bit about why are you considering reconstructing a 3d shape from surface points?</p>
<p>Are you starting from a 3D image? Is the goal 3D segmentation? Have you tried nn-UNet and MONAI Auto3DSeg models? They are almost guaranteed to learn any 3D segmentation task if you provide enough training samples.</p>

---

## Post #5 by @sima (2024-05-07 09:16 UTC)

<p>thank you Leidy Mora for your answer <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"><br>
unfortunately this module was not useful for my problem but it was very attractive and I think I can use it for other purposes later.</p>

---

## Post #6 by @sima (2024-05-07 09:18 UTC)

<p>thanks a lot Mr Pinter for your answer</p>

---

## Post #7 by @sima (2024-05-13 05:59 UTC)

<p>thank you Mr Lasso for your answer</p>
<p>I can find the answer of my problem</p>
<p>Actually I am trying to design a module to make bolus electron.<br>
for this purpose, I considered  PTV model and a isodose level that I want to match it to distal surface of PTV ( to spare normal tissues under the PTV). it seems, I could find boundary points of the bolus on the surface in each slice.</p>
<p>Fortunately, I can find useful codes in the SlicerSkinMouldGenerator module to convert the boundary points into a final bolus. Now I am trying to remove the bugs in my code by applying it to PTVs in different conditions.<br>
But, I have no experience for next steps and I do not know how to convert my code into a usable module in 3d Slicer. I want to know if you can help me?</p>

---

## Post #8 by @lassoan (2024-05-13 23:05 UTC)

<p>Skin mould generator is already a working Slicer module, so one approach toj could take is to improve this module, add features that you need, while keeling the module in working condition.</p>

---
