---
topic_id: 10347
title: "Mammographic Density Segmentation"
date: 2020-02-19
url: https://discourse.slicer.org/t/10347
---

# Mammographic density segmentation

**Topic ID**: 10347
**Date**: 2020-02-19
**URL**: https://discourse.slicer.org/t/mammographic-density-segmentation/10347

---

## Post #1 by @paolaco (2020-02-19 00:30 UTC)

<p>Operating system: Windows 10<br>
Slicer version:  4.10.2</p>
<p>Hi, how to do a mammographic density segmentation in order to show automatic identification of breast density?</p>
<p>Thank you,<br>
Paola</p>

---

## Post #2 by @lassoan (2020-02-19 02:20 UTC)

<p>Slicer has many tools for this kind of analysis. If you can write a bit more about what you would like to achieve (or provide reference to a paper that describes a workflow that is similar to what you would like to implement) then we can give more specific advice.</p>

---

## Post #3 by @paolaco (2020-02-19 08:59 UTC)

<p>I would like to achieve an automated brest density assessement. In the work I mention below the software automatically identified on the mammogram the pixel with higher intensities. The density was measured in percentage. It’s what I am willing to reproduce.</p>
<p>Thank you</p>
<p>DOI 10.25259/JCIS_70_2019</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/286fad20e68044a3d3c57bfa02085599ad07c272.png" data-download-href="/uploads/short-url/5LImzNtgV4eqi71WeOJYl1j2wrE.png?dl=1" title="a-Left-craniocaudal-mammogram-of-a-41-year-old-woman-with-a-negative-screening-exam-b.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/286fad20e68044a3d3c57bfa02085599ad07c272.png" alt="a-Left-craniocaudal-mammogram-of-a-41-year-old-woman-with-a-negative-screening-exam-b.png" data-base62-sha1="5LImzNtgV4eqi71WeOJYl1j2wrE" width="690" height="484" data-dominant-color="353732"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a-Left-craniocaudal-mammogram-of-a-41-year-old-woman-with-a-negative-screening-exam-b.png</span><span class="informations">727×510 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @timeanddoctor (2020-02-19 13:25 UTC)

<p>You can segment the ROI(the white area and green area in your picture) and then get the each area statistic in segment statistic module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2abdfc776f93732f35c732fa145099948af899e1.png" alt="image" data-base62-sha1="667623BHH4wE7ZXKZM6LBKlKE5H" width="630" height="442"></p>

---

## Post #5 by @timeanddoctor (2020-02-19 13:27 UTC)

<aside class="quote" data-post="6" data-topic="9220">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-for-measuring-user-statistics/9220/6">New module for measuring user statistics</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the feedback. I’ve added a button to the user information popup to disable User statistics by a single button click (and tables are not created anymore if the feature is disabled). I’ve added a <a href="https://github.com/PerkLab/SlicerSandbox/issues/5" rel="noopener nofollow ugc">bug report to track the slowdown issue</a>.
  </blockquote>
</aside>


---

## Post #6 by @paolaco (2020-02-19 16:50 UTC)

<p>Thank you. I am wondering if there is a way to segment automatically the ROI and to let the software calculate the pixel with higher density within that ROI.</p>

---

## Post #7 by @lassoan (2020-02-20 04:00 UTC)

<p>If simple thresholding can segment the high-density area then the process can be made fully automatic very easily by writing a short Python script. See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>
<p>You may find <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37">“create fat/muscle/bone segment by thresholding and report volume of each segment”</a> example particularly relevant. If the script works well then you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">make a Python scripted module out of it</a>.</p>

---

## Post #8 by @paolaco (2020-02-20 17:32 UTC)

<p>By thresholding the segmentation seems suboptimal. In the picture I posted the author could “colour” just the fibroglandular breast parenchyma.<br>
Thank you</p>

---

## Post #9 by @lassoan (2020-02-20 18:50 UTC)

<p>The screenshot in the image indicates that the authors used “Level tracing” effect in Editor module (which correspongs to “Segment Editor” module in current Slicer version).</p>

---

## Post #10 by @paolaco (2020-02-20 19:11 UTC)

<p>I had the same intuition but selecting “Level tracing”, the program don’t let me do any operation on the DICOM file. I thought there was the need of doing something  else before but can’t find it.<br>
Thank you</p>

---

## Post #11 by @lassoan (2020-02-20 19:16 UTC)

<p>Once you have your segment highlighting the region of interest, you can follow the steps described <a href="https://discourse.slicer.org/t/mammographic-density-segmentation/10347/5">above</a> to get the density. Would you expect to do any other operation on the DICOM file?</p>

---

## Post #12 by @SOFIA_R (2023-08-18 01:20 UTC)

<p>Hi, i want to know how to make dense tissue segmentation from tomosynthesis images?<br>
thank you</p>

---

## Post #13 by @lassoan (2023-08-18 21:01 UTC)

<p>If dense tissue appears bright then you can segment it using Threshold effect in Segment Editor module.</p>

---

## Post #14 by @SOFIA_R (2023-08-20 01:38 UTC)

<p>Ok but i will have to do that on every slice, i’m guessing ?</p>

---

## Post #15 by @lassoan (2023-08-20 07:22 UTC)

<p>Thresholding is performed for the entire 3D volume. No need to do it for every slice.</p>
<p>In general, in 3D Slicer all data is specified in 3D and all operations (with very few exceptions) are performed in 3D.</p>

---

## Post #16 by @SOFIA_R (2023-08-20 14:17 UTC)

<p>Ok. And how do i make a 3D volume from the tomosynthesis images? I’m starting to use 3D slicer for the first time, so if you could post a screenshot of the steps i have to do, i’d be very grateful.</p>

---
