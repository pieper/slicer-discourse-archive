---
topic_id: 13670
title: "Change Opacity Of Parts Of A Model"
date: 2020-09-23
url: https://discourse.slicer.org/t/13670
---

# Change Opacity of Parts of a Model

**Topic ID**: 13670
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/change-opacity-of-parts-of-a-model/13670

---

## Post #1 by @CB1 (2020-09-23 14:14 UTC)

<p>I’m trying to adjust the opacity of everything but a small range of intensities on a 3d model made of MRI slices. It’s a .nii.gz file. I have one small part of my images that is intensity ~8000 and everything else is around 200-400. I’m very new to slicer.</p>

---

## Post #2 by @cpinter (2020-09-23 14:19 UTC)

<p>Thanks for creating the new topic! However, I don’t know much more than before.</p>
<p>First things first:</p>
<ul>
<li>What is your <em>overall</em> goal?</li>
<li>What do you mean exactly by “3d model made of MRI slices”?</li>
</ul>

---

## Post #3 by @CB1 (2020-09-23 14:26 UTC)

<p>The eventual goal is to create a 3d model of a brain where you can see through the outer layers to visualize a specific highlighted area on the interior. I have a set of 2D MRI slices where the specific interior area is already highlighted by having a much greater intensity, so now I think I just need to make all other intensities have a lower opacity.</p>
<p>The issue is when I export the MRI slices to a 3D model, it just gives me a model of the outer surface of the brain, whereas I need to be able to see inside while still having the outer layer semi-visible.</p>

---

## Post #4 by @cpinter (2020-09-23 14:29 UTC)

<aside class="quote no-group" data-username="CB1" data-post="3" data-topic="13670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cb1/48/6511_2.png" class="avatar"> CB1:</div>
<blockquote>
<p>export the MRI slices to a 3D model</p>
</blockquote>
</aside>
<p>I’m sorry but I’m completely lost at what you mean by 3D model here. In Slicer we have Segmentations, Models, Volume rendering… Can you describe what tool you use to create this “3D model”?</p>

---

## Post #5 by @CB1 (2020-09-23 14:34 UTC)

<p>I’m trying to create a 3D model of a brain. The file format is .nii.gz, which can be exported to a 3D model using various programs (I used the program mipav). But that should be the easier part for me… What I’m asking is more about changing the opacity of specific sections of an MRI.</p>

---

## Post #6 by @cpinter (2020-09-23 14:40 UTC)

<p>Please look at this page: <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>
<p>Which data type is your “3D model”? Without giving us enough information to understand your question we cannot help you.</p>

---

## Post #7 by @CB1 (2020-09-23 14:57 UTC)

<p>The eventual 3D model is a .ply, but that was generated using a different program. The MRI volume can be initially loaded into slicer as a .nii.gz or DICOM. What other information do you need?</p>

---

## Post #8 by @lassoan (2020-09-23 15:02 UTC)

<p>If you want to make certain intensity range visible and others transparent then you can do it using volume rendering module, by editing Advanced / Volume properties / Scalar opacity mapping function accordingly.</p>
<p>Alternatively, you can segment each region using Segment Editor module, Threshold effect. You can adjust opacity of each segment separately in Segmentations module / Display / Advanced section.</p>

---

## Post #9 by @CB1 (2020-09-23 15:09 UTC)

<p>That sounds like exactly what I want. What specifically would I have to do to make everything with intensity &lt;8000 have opacity of .5? I see the opacity slider but I’m not sure how to affect only certain intensity ranges.</p>

---

## Post #10 by @lassoan (2020-09-23 15:10 UTC)

<p>Which method are you planning to try? Volume rendering or segmentation?</p>

---

## Post #11 by @CB1 (2020-09-23 15:12 UTC)

<p>I was planning on volume rendering, but whichever is simpler is best.</p>

---

## Post #12 by @lassoan (2020-09-23 15:27 UTC)

<p>If you only need visualization then volume rendering is fine. You can start from a preset by selecting a preset and use “Shift” slider (optional, as you can just start from the default transfer functions, too). Then click on the “Scalar Opacity Mapping” function line to add points and click-and-drag points to move them to achieve the intensity-&gt;opacity mapping you want.</p>

---
