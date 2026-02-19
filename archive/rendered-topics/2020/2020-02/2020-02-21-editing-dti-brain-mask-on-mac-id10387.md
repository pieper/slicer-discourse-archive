---
topic_id: 10387
title: "Editing Dti Brain Mask On Mac"
date: 2020-02-21
url: https://discourse.slicer.org/t/10387
---

# Editing DTI brain mask on Mac

**Topic ID**: 10387
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/editing-dti-brain-mask-on-mac/10387

---

## Post #1 by @LearningSlicerYay (2020-02-21 20:20 UTC)

<p>Operating system: Mac<br>
Slicer version: 4.10.2<br>
Expected behavior: Has editor module<br>
Actual behavior: No editor module</p>
<p>Hi everyone<br>
I normally run my DTI analysis using Windows, but wanted to try out whitematteranalysis and moved to a Mac to test it out. Normally on Windows (running 4.10.1) when I run “Diffusion Brain Masking” I am able to edit the mask to include extra areas (optic nerves). However, this module is not available on 4.10.2. Moving forward, I’m wondering if there’s another way I can edit the brain mask generated without downgrading to 4.10.1?</p>
<p>Thanks,<br>
AC</p>

---

## Post #2 by @pieper (2020-02-24 16:46 UTC)

<p>Maybe this is the same question as this issue:</p>
<aside class="quote quote-modified" data-post="4" data-topic="10408">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/where-can-i-found-editor-module/10408/4">Where can I found Editor module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You may search it or click the all modules: 
[image]
  </blockquote>
</aside>


---

## Post #3 by @LearningSlicerYay (2020-02-24 18:41 UTC)

<p>Thanks Steve<br>
I’m not sure how I missed it before…</p>
<p>However, I know the Editor module is being replaced by Segment Editor. I tried editing the mask using the Segment Editor but there’s no option to do so. Is it possible?</p>

---

## Post #4 by @pieper (2020-02-24 19:46 UTC)

<p><a class="mention" href="/u/learningsliceryay">@LearningSlicerYay</a> - at the bottom of the Segmentations module there’s an import/export option that lets you bring in labelmaps as segmentations.  Then you can export them again if you need a labelmap for other processing.</p>

---

## Post #5 by @lassoan (2020-02-25 00:24 UTC)

<p>To convert with 2 mouse clicks, you can also go to Data module and right-click on the labelmap or segmentation node and choose to convert to segmentation or labelmap.</p>

---

## Post #6 by @LearningSlicerYay (2020-03-03 17:20 UTC)

<p>Hi all,</p>
<p>I’ve tried running this a couple times but every time I edit the brainmask and then try to run the DTI estimation, I get the following error:</p>
<blockquote>
<p>Diffusion Tensor Estimation standard error:<br>
C:/…/NA-MIC/Extensions-27931/SlicerDMRI/lib/Slicer-4.10/cli-modules/DWIToDTIEstimation.exe: Error reading Mask file, wrong coordinate space</p>
</blockquote>
<p>This occurs regardless if I use the segmentations module to convert/edit/export the mask, or use the data module to convert/edit/export the mask. I’ve also tried editing the mask using the baseline and dwi as my master volumes but still get this error.</p>
<p>I am not sure how to overcome this one… Does anyone have any ideas?<br>
(However, using the Editor module to edit the brainmask does not seem to result in this error).</p>

---

## Post #7 by @pieper (2020-03-03 17:45 UTC)

<p>You can check the <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/CLI/DWIToDTIEstimation/DWIToDTIEstimation.cxx#L117-L122">tensor estimation code is checking the transforms</a>.  You can look at this in the Volume Information tab of the Volumes module.  The exported labelmap should match the master volume used to generate the segmentation.</p>

---

## Post #8 by @LearningSlicerYay (2020-03-03 18:07 UTC)

<p>Hi Steve,</p>
<p>Thanks for your response. I’m not sure how to check whether the code is checking the transforms due to my limited coding/programming knowledge…</p>
<p>However, I think you’re on the right track as my dwi, baseline, and brainmask have the same spacing and origin (with some floating number differences), whereas the ones I converted have very different origins. I tried centering my dwi and the converted/exported brain masks but the origin is still different from my DWI. Manually changing the origin of the masks to the dwi / baseline still gives me the error above, and visually in the viewer shifts the mask significantly AWAY from the brain from my dwi/baseline.</p>
<p>EDIT: I actually noticed an extra menu on the export portion of the segmentation module where I can specify the master volume. Ensuring this is the DWI seems to have fixed the problem! : )</p>

---
