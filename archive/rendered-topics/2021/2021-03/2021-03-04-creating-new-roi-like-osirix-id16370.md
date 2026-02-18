# Creating new ROI like Osirix

**Topic ID**: 16370
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/creating-new-roi-like-osirix/16370

---

## Post #1 by @titotitoide (2021-03-04 16:59 UTC)

<p>Hi everyone! I need help because I am quite desesperating traying to create a free lung segmentation. I have tried with segment editor --&gt;Draw tube, Markups, Markups to model…But no one works…I am working with severely lung injured so trying to create a segmentation from seeds or using threshold doesn’t work. I am not so good with informatics so I put a YouTube link where it is explained with osirix what I want to do exactly with 3DSlicer. I want an easy solution step by step because I am so clumsy hehe<br>
I have posted previously about this topic but I am quite desesperating because I can’t do it!!<br>
Thank you so much for your remarkable and huge contributions to science and 3Dslice community.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xLjYE2cnqIc" data-video-title="Performing Region of Interest ROI Segmentation with OsiriX 5 9 HD" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xLjYE2cnqIc" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xLjYE2cnqIc/maxresdefault.jpg" title="Performing Region of Interest ROI Segmentation with OsiriX 5 9 HD" width="" height="">
  </a>
</div>


---

## Post #2 by @lassoan (2021-03-04 17:11 UTC)

<p>Segment Editor can do this so much better! You can draw the contours on as many slices as you want using Paint or Draw effect, then get a full 3D segmentation using “Fill between slices” effect.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u93kI1MG6Ic" data-video-title="Quick manual segmentation with contour interpolation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u93kI1MG6Ic" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u93kI1MG6Ic/maxresdefault.jpg" title="Quick manual segmentation with contour interpolation" width="" height="">
  </a>
</div>

<p>In Slicer, there is no need to waste time with things like renaming ROIs. You can also save a lot of time and get higher quality segmentations by using auto-update in “Fill between slices”: if you make changes in any slices then all contours are recomputed in 3D.</p>

---

## Post #3 by @titotitoide (2021-03-04 17:35 UTC)

<p>Thank you so much lassoan for your time! I will try this method.<br>
Is there any possibility that instead of using the drawing tool to create de ROI area, use dots as in Draw tube function or Makups?</p>

---

## Post #4 by @lassoan (2021-03-04 17:54 UTC)

<p>Draw tool allows you to draw line segments (no need to hold down the mouse button). You ca also set an intensity range (using Threshold effect, “Use for masking”) and then you can only need to pay attention to the contour where you are separating between tissue with the same density.</p>
<p>If you share a data set (but at least a few screenshots) then we can give you more specific advice. Probably “Grow from seeds” method would work very well, too. You can also try the AI-based brain tumor segmentation algorithm (in NvidiaAIAssistedAnnotation extension), which only requires you to click 6 points.</p>

---

## Post #5 by @titotitoide (2021-03-04 18:10 UTC)

<p>Lassoan thanks for your reply!<br>
I mean…Instead of picture 1 (draw tool) to delimit de ROI area, use dots (only 1 “click” ) to delimit ROI segment, picture 2.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b043cd303a2484be8e5d7cf484b1d3a7d60f488.png" alt="1" data-base62-sha1="3QZYboH6v9ULJiyFNg827sQin56" width="688" height="472"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcc99e66d1edbd825cd7088bdbdfb8c3571452cc.png" data-download-href="/uploads/short-url/qW5JizrX03i4Ty3l904htuIxS0Y.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcc99e66d1edbd825cd7088bdbdfb8c3571452cc.png" alt="2" data-base62-sha1="qW5JizrX03i4Ty3l904htuIxS0Y" width="690" height="431" data-dominant-color="BEBCBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">725×453 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
IMO the problem using grow from seed or threshold tool for this patients is that the basal zone or more injured zones the results are no so good as in healthy lungs, for this reason my interest in segmenting manually the ROI.<br>
Thanks you so much again!</p>

---

## Post #6 by @lassoan (2021-03-04 18:52 UTC)

<p>All the above that I wrote about is for tumor segmentation. For segmentation of the lung, you can use this automated tool:</p>
<aside class="quote quote-modified" data-post="1" data-topic="15006">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">LungCTAnalyzer extension for lung CT segmentation and analysis for COVID-19 assessment</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    New extension is added for lung CT segmentation and analysis for COVID-19 assessment. It is developed by Prof. Rudolf Bumm (<a class="mention" href="/u/rbumm">@rbumm</a>), a clinician in KSGR (Chur, Switzerland; with some help from Slicer core developers to polish things up), which is a nice demonstration of how Python scripting in Slicer allows users to quickly develop clinically deployable tools from their ideas. 
The extension offers a quick (1-minute) lung segmentation wizard and quantitative volumetric analysis of the lungs with…
  </blockquote>
</aside>


---
