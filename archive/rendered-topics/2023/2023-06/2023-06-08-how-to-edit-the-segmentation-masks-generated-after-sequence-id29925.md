---
topic_id: 29925
title: "How To Edit The Segmentation Masks Generated After Sequence"
date: 2023-06-08
url: https://discourse.slicer.org/t/29925
---

# How to edit the segmentation masks generated after sequence registration

**Topic ID**: 29925
**Date**: 2023-06-08
**URL**: https://discourse.slicer.org/t/how-to-edit-the-segmentation-masks-generated-after-sequence-registration/29925

---

## Post #1 by @Sanjib_Gurung (2023-06-08 22:11 UTC)

<p>Hi, I applied the sequence registration to apply segmentation to series of images. However, I cannot edit the generated masks by using the tools in the segment editor. Is there a way to edit the segmentation masks after applying the sequence registration? Thanks!</p>

---

## Post #2 by @lassoan (2023-06-16 14:55 UTC)

<p>What did you do exactly? What did you expect to happen? What happened instead?</p>

---

## Post #3 by @Sanjib_Gurung (2023-06-16 21:44 UTC)

<p>Thanks for the response! I have a volume sequence of MRI dicom images. I want to segment the heart along the time sequence and get the warped stl surface mesh of heart along the time sequence. I followed the steps shown in (<a href="https://www.youtube.com/watch?v=qVgXdXEEVFU&amp;ab_channel=PerkLabResearch" class="inline-onebox" rel="noopener nofollow ugc">Create an animated 4D surface model by segmenting a single 3D frame - YouTube</a>) e.g. segment heart at one of the time frame, apply registration to the volume sequence, apply the calculated transform to the segmentation sequence. I got the dynamic warped mesh along the sequence but the segmentations obtained at each time frame is not accurate. Is there any way to modify the automatically generated segmentation at each time frame? The segment editor tool do not seem to modify the automatically generated segmentation mask. Thanks!</p>

---

## Post #4 by @Liam_S (2023-07-14 18:11 UTC)

<p>Hi Sanjib. Did you find the solution to this?</p>
<p>I found that you can ‘harden’ the transform at a given time point which alters the segmentation mask itself and this should be editable.</p>
<p>I am not an expert and am currently struggling with altering the segmentation at all time points though. I think my problem is (and perhaps the moderators can help) that the transform is computed relative to the frame you use as reference (let’s say tref). And so once you harden the transform to adjust the segmentation mask to a different time (let’s say tref + 2) then the application of the original transform to that mask starts to create error as it is now warping the segmentation at tref +2  as if it were the segmentation at tref -which isn’t the case.</p>
<p>Did you find this to be the case and did you find a work around?</p>
<p>I might be missing some knowledge about handling sequences but the (cumbersome) workaround might be to clone your segmentation as many times as there are time points and harden the transform to each clone segmentation at its respective time point.</p>
<p>A nice feature would be to be able to switch the transform from being all relative to one time frame to being relative to its previous frame but in my naiveté this might be a big ask.</p>

---

## Post #5 by @lassoan (2023-07-15 15:32 UTC)

<p>To create a sequence of warped models and segmentations (that you can edit or save), you need to clone the node and harden the transform on it for each time point.</p>
<p>Doing this manually can be somewhat tedious so it may worth writing a short Python script for it, something similar to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-nodes-warped-by-transform-sequence">this</a>.</p>
<p>It could make sense to write a small module that can create a warped sequence from an input node and a transform sequence. <a class="mention" href="/u/che85">@che85</a> do I remember correctly that we talked about this and you might implement such a module?</p>

---
