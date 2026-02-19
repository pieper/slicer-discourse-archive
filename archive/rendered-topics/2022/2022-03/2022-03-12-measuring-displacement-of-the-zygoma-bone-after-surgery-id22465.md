---
topic_id: 22465
title: "Measuring Displacement Of The Zygoma Bone After Surgery"
date: 2022-03-12
url: https://discourse.slicer.org/t/22465
---

# Measuring displacement of the zygoma bone after surgery

**Topic ID**: 22465
**Date**: 2022-03-12
**URL**: https://discourse.slicer.org/t/measuring-displacement-of-the-zygoma-bone-after-surgery/22465

---

## Post #1 by @Moh_d_Al-Watary (2022-03-12 11:53 UTC)

<p>Dear friends, wish you all are doing well and fine. Thank you for reading this request. My work is to measure if there is any displacement of the zygoma bone after being surgically repositioned into a new position.<br>
I am comparing the position of the zygoma bone using T1: one-week postoperative CT, and T2: at least 6 months postoperatively.<br>
1st I collect the CT in DICOM format, imported them into Dolphin software to:</p>
<ol>
<li>Superimposition of both CT (using the cranial base as a reference)</li>
<li>Created surface volume for T1 and registered T2</li>
<li>Exported them as .stl file</li>
<li>Imported them to 3D Slicer, then:<br>
a.	Most of the time the two models have opened far away from each other* (although superimposed in the 1 step)</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15aa6f34f1cea5895bcb5c2949f5f623de8599f0.png" alt="image" data-base62-sha1="35FbdnJqedynzCEJMb5t9wjid5C" width="332" height="322"></p>
<p>i.	So, I start with semi-automatic registration: Surface registration under CMS module<br>
ii.	Or I used manual registration….Fiducial registration wizard under Slicer IGI extension)<br>
iii.	Then start doing:</p>
<ol>
<li>Pick’n paint: select ROI</li>
<li>Model to model distance (most of the time: either terminate with error message appeared or too long time with no success then I tried again till succeed (after too many trials!).</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/462f28485adf2878eb5c8334ef764f8489202fd7.jpeg" data-download-href="/uploads/short-url/a0Ssl4TKVfkHzk8fVuU5n9NI7J5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/462f28485adf2878eb5c8334ef764f8489202fd7_2_690x414.jpeg" alt="image" data-base62-sha1="a0Ssl4TKVfkHzk8fVuU5n9NI7J5" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/462f28485adf2878eb5c8334ef764f8489202fd7_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/462f28485adf2878eb5c8334ef764f8489202fd7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/462f28485adf2878eb5c8334ef764f8489202fd7.jpeg 2x" data-dominant-color="D0D2DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">935×561 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f8fce16c543d54105027a6efe0369fcdc5cec39.jpeg" data-download-href="/uploads/short-url/2dFgiFX91mw9fxQ51V4NPZWrNFv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f8fce16c543d54105027a6efe0369fcdc5cec39_2_642x500.jpeg" alt="image" data-base62-sha1="2dFgiFX91mw9fxQ51V4NPZWrNFv" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f8fce16c543d54105027a6efe0369fcdc5cec39_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f8fce16c543d54105027a6efe0369fcdc5cec39.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f8fce16c543d54105027a6efe0369fcdc5cec39.jpeg 2x" data-dominant-color="C4CFCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">931×725 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Very high values?!?</p>
<ol start="3">
<li>Mesh statistics to get the values.<br>
Now I want to ask these questions:<br>
Do I select the proper way to achieve my goals (measuring the amount of displacement that happened in T2 compared to T1 CT)?<br>
How could I solve such problems of not matching models or too long time of mode to model distance module?<br>
What are your recommendations to make this mission easier?</li>
</ol>
<p>Thank you so much for your highly appreciated help…<br>
Sincerely,</p>
<p>Mohammed</p>

---

## Post #2 by @muratmaga (2022-03-13 02:02 UTC)

<aside class="quote no-group" data-username="Moh_d_Al-Watary" data-post="1" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/moh_d_al-watary/48/14124_2.png" class="avatar"> Moh_d_Al-Watary:</div>
<blockquote>
<p>1st I collect the CT in DICOM format, imported them into Dolphin software to:</p>
</blockquote>
</aside>
<p>If your original data are in DICOM, I would suggest doing all the steps in Slicer (including the 3D model generation).</p>
<ol>
<li>You can import the DICOMs</li>
<li>If the 3D images of two dicoms sets do not occupy the same space (i.e., they do not overlap), do a a rigid registration via Elastix extensions.</li>
<li>Confirm the results of your registration.</li>
<li>Then proceed with segmentation and model building and derive your statistics.</li>
</ol>

---

## Post #3 by @MAXFAXSURGEON (2022-03-14 13:46 UTC)

<p>Thank you so much for your suggestion, but please cold you explain more in regard:</p>
<p>I have downloaded Elastix extension (in version 4.13.0 3D Slicer), but I do not know how to use it, if you could explain in more details would be so great?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24de2b513e921d7c021bb5ecece1a0d2f401181e.jpeg" data-download-href="/uploads/short-url/5g9bqkHcXGOFYAfgyg80ldwm1Wu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24de2b513e921d7c021bb5ecece1a0d2f401181e_2_690x387.jpeg" alt="image" data-base62-sha1="5g9bqkHcXGOFYAfgyg80ldwm1Wu" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24de2b513e921d7c021bb5ecece1a0d2f401181e_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24de2b513e921d7c021bb5ecece1a0d2f401181e_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24de2b513e921d7c021bb5ecece1a0d2f401181e.jpeg 2x" data-dominant-color="9A9CAB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
as you can see in this screen shot:<br>
I have imported both DICOMs into 3D Slicer, and start using Elastix extension: but here what should I choose? And is it normal that it takes too long time to execute the order?<br>
Thank you again and wish you all the best.</p>

---

## Post #4 by @muratmaga (2022-03-15 16:43 UTC)

<p>In this menu fixed image means the image that defines the coordinate system and the orientation, moving image is the one that will be rotated to match that orientation. I don’t think it makes any difference whether you choose your t1 or t2 timepoints as either.</p>
<p>Given that this intrasubject registration, you should choose the “generic rigid” to register them.</p>

---

## Post #5 by @MAXFAXSURGEON (2022-03-20 04:05 UTC)

<p>Thank you so much for your comments.<br>
Please could you explain in further details the following:</p>
<ol>
<li>when I imported the two DICOMs (T1 and T2) and did a rigid registration with Elastix extension: A. What should I save to be used for the segmentation step?:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f17951affea82ada7c8cc203058c9e451790b9e7.png" data-download-href="/uploads/short-url/ysaZI3PH9IycKLekwDH9qCemjxJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f17951affea82ada7c8cc203058c9e451790b9e7_2_690x387.png" alt="image" data-base62-sha1="ysaZI3PH9IycKLekwDH9qCemjxJ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f17951affea82ada7c8cc203058c9e451790b9e7_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f17951affea82ada7c8cc203058c9e451790b9e7_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f17951affea82ada7c8cc203058c9e451790b9e7.png 2x" data-dominant-color="B7B8C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbcde922830755661cc8a1d1acd1326d2f2f2939.jpeg" data-download-href="/uploads/short-url/vmtJ711fztIQRhJ0vZgd4EMKQCB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbcde922830755661cc8a1d1acd1326d2f2f2939_2_690x387.jpeg" alt="image" data-base62-sha1="vmtJ711fztIQRhJ0vZgd4EMKQCB" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbcde922830755661cc8a1d1acd1326d2f2f2939_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dbcde922830755661cc8a1d1acd1326d2f2f2939_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbcde922830755661cc8a1d1acd1326d2f2f2939.jpeg 2x" data-dominant-color="9D9FAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You mentioned in the 3rd step to proceed with segmentation: do you mean that I need to segment the ROI (zygoma bone here)? how could this be done?<br>
finally: you advised me to do modelling: you mean after doing the segmentation of ROI, I need to convert this segmented part to model? and how drive the statistics (do you mean to do the same steps mentioned in my first post: Pick’n paint, model to model distance and mesh statistics?)<br>
If you could send me your e.mail for quicker communication would be so help full.<br>
Thank you so much for your help and waiting to hearing from you soon.<br>
Sincerely,<br>
Mohammed</p>

---

## Post #6 by @muratmaga (2022-03-20 22:01 UTC)

<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="5" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>when I imported the two DICOMs (T1 and T2) and did a rigid registration with Elastix extension: A. What should I save to be used for the segmentation step?:</p>
</blockquote>
</aside>
<p>If the rigid registration is successful, the output Volume (Volume) should be now in the same space as the T1 Oriented CT. So you should use those two to segment.</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="5" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>You mentioned in the 3rd step to proceed with segmentation: do you mean that I need to segment the ROI (zygoma bone here)? how could this be done?</p>
</blockquote>
</aside>
<p>In your original post you mentioned you created surfaces, that’s what I meant by segmentation. That’s how you generate a surface model from a voxel data, via the Segmentation.</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="5" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>(do you mean to do the same steps mentioned in my first post: Pick’n paint, model to model distance and mesh statistics?)</p>
</blockquote>
</aside>
<p>That depends on what you wanted to do. If you want to visualize the displacement in the skulls prior and after the surgery, yes model to model distance is an efficient way to achieve that.</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="5" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>If you could send me your e.mail for quicker communication would be so help full.</p>
</blockquote>
</aside>
<p>We try to keep the communications public on the forum, so that others benefit from these discussions as well.</p>

---

## Post #7 by @MAXFAXSURGEON (2022-03-21 15:09 UTC)

<p>Thank you so much for you informative replies.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If the rigid registration is successful, the output Volume (Volume) should be now in the same space as the T1 Oriented CT. So you should use those two to segment.</p>
</blockquote>
</aside>
<p>So, when I finished doing RIGID REGISTRATION I need to save Volume as seen in the attached screenshot ( in which format should be saved?)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ace9d2c6c1da640ff537daeaf340520bd1b7e492.png" data-download-href="/uploads/short-url/oFF5wALMp2hukmMeLZJCxVvtqRI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ace9d2c6c1da640ff537daeaf340520bd1b7e492_2_690x387.png" alt="image" data-base62-sha1="oFF5wALMp2hukmMeLZJCxVvtqRI" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ace9d2c6c1da640ff537daeaf340520bd1b7e492_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ace9d2c6c1da640ff537daeaf340520bd1b7e492_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ace9d2c6c1da640ff537daeaf340520bd1b7e492.png 2x" data-dominant-color="B7B8C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In your original post you mentioned you created surfaces, that’s what I meant by segmentation. That’s how you generate a surface model from a voxel data, via the Segmentation.</p>
</blockquote>
</aside>
<p>After saving the required output, the next step to do segmentation for both Oriented T1 and saved output volume: should be done for each one separately or can be done for both of them?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d14b8532c2fe63bb0b6f2a7468e1aebaa612fb6.jpeg" data-download-href="/uploads/short-url/fyYr4JrXo4HMJiMYOapxGJuVVum.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d14b8532c2fe63bb0b6f2a7468e1aebaa612fb6_2_690x387.jpeg" alt="image" data-base62-sha1="fyYr4JrXo4HMJiMYOapxGJuVVum" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d14b8532c2fe63bb0b6f2a7468e1aebaa612fb6_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d14b8532c2fe63bb0b6f2a7468e1aebaa612fb6_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d14b8532c2fe63bb0b6f2a7468e1aebaa612fb6.jpeg 2x" data-dominant-color="9EA1AD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>in which format should I save the segmentation to be modelled in the next step? I can not see here .stl format.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ed557c40db368f6e374eb6452fafd4fab22c4c9.png" data-download-href="/uploads/short-url/6Gj30ExEYf1cj8Ns6QSWVEvBzSx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed557c40db368f6e374eb6452fafd4fab22c4c9_2_690x387.png" alt="image" data-base62-sha1="6Gj30ExEYf1cj8Ns6QSWVEvBzSx" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed557c40db368f6e374eb6452fafd4fab22c4c9_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed557c40db368f6e374eb6452fafd4fab22c4c9_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ed557c40db368f6e374eb6452fafd4fab22c4c9.png 2x" data-dominant-color="A9ADB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After saving the proper format afte segmentation, what is the next step tp create a model for Oriented T1 and output volume?</p>
<p>Thank you so much for your help.</p>

---

## Post #8 by @muratmaga (2022-03-21 21:34 UTC)

<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="7" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>So, when I finished doing RIGID REGISTRATION I need to save Volume as seen in the attached screenshot ( in which format should be saved?)</p>
</blockquote>
</aside>
<p>Use NRRD, which is the default format in Slicer.</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="7" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>After saving the required output, the next step to do segmentation for both Oriented T1 and saved output volume: should be done for each one separately or can be done for both of them?</p>
</blockquote>
</aside>
<p>You need to clean the thin shell around the skull. If you are not familiar with segmentation in Slicer, you probably need to read this documentation first:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a><br>
and this<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html</a></p>
<p>You need to do this both for your new volume and T1</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="7" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>in which format should I save the segmentation to be modelled in the next step? I can not see here .stl format.</p>
</blockquote>
</aside>
<p>seg.nrrd is the default format for segmentation</p>
<aside class="quote no-group" data-username="MAXFAXSURGEON" data-post="7" data-topic="22465">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxfaxsurgeon/48/13377_2.png" class="avatar"> MAXFAXSURGEON:</div>
<blockquote>
<p>After saving the proper format afte segmentation, what is the next step tp create a model for Oriented T1 and output volume?</p>
</blockquote>
</aside>
<p>You can go to the <code>Segmentations</code> module and export your segmentation as a 3D model with a single click (Import/Export tab).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778c0a6505bb44aac339190979d0afea370dea45.png" data-download-href="/uploads/short-url/h3yQZ3BR33Ynpucq3J8lQI9307r.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778c0a6505bb44aac339190979d0afea370dea45_2_345x134.png" alt="image" data-base62-sha1="h3yQZ3BR33Ynpucq3J8lQI9307r" width="345" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778c0a6505bb44aac339190979d0afea370dea45_2_345x134.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778c0a6505bb44aac339190979d0afea370dea45_2_517x201.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/778c0a6505bb44aac339190979d0afea370dea45_2_690x268.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1109×432 9.05 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
