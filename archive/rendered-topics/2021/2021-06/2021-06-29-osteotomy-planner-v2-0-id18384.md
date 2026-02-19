---
topic_id: 18384
title: "Osteotomy Planner V2 0"
date: 2021-06-29
url: https://discourse.slicer.org/t/18384
---

# Osteotomy Planner v2.0

**Topic ID**: 18384
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/osteotomy-planner-v2-0/18384

---

## Post #1 by @Fluvio_Lobo (2021-06-29 02:27 UTC)

<p>Hello,</p>
<p>I was testing out the <strong>osteotomy planner</strong> module but seems like version 2.0 is different from the one shown in this <a href="https://vimeo.com/260831228" rel="noopener nofollow ugc">video</a>.</p>
<p>I can easily create <strong>plane cuts</strong>, <strong>curve cuts</strong>, and perform <strong>local transforms</strong>, but I am not able to perform any <strong>bending on the bone segments</strong>. I hate to say it, but this is like the one feature I am looking forward to the most <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=12" title=":joy:" class="emoji" alt=":joy:" loading="lazy" width="20" height="20"></p>
<p>The module also does not have some of the basic visibility and model selection options shown in the original video, but I am guessing the module is currently being re-worked.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18c5ba62f3a4253333d19cc6c56de918f0d596f8.jpeg" data-download-href="/uploads/short-url/3x95yVFBrCExMQa8WfZmKkNoaDe.jpeg?dl=1" title="osteotomytest.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18c5ba62f3a4253333d19cc6c56de918f0d596f8_2_345x186.jpeg" alt="osteotomytest.PNG" data-base62-sha1="3x95yVFBrCExMQa8WfZmKkNoaDe" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18c5ba62f3a4253333d19cc6c56de918f0d596f8_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18c5ba62f3a4253333d19cc6c56de918f0d596f8_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18c5ba62f3a4253333d19cc6c56de918f0d596f8_2_690x372.jpeg 2x" data-dominant-color="292D2B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">osteotomytest.PNG</span><span class="informations">1920×1040 237 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a prior build I can use?<br>
Do I need to downgrade my Slicer version? <em>(currently on the 4.13.0-2021-05-22)</em></p>
<p>Thank you!</p>

---

## Post #2 by @Fluvio_Lobo (2021-07-04 14:03 UTC)

<p>Hello,</p>
<p>I wanted to come back to this in case anyone was interested into <strong>craniosynostosis planning</strong>. Hopefully someone will find this useful!</p>
<p>My original goal was to re-create the workflow presented by <a href="https://www.nature.com/articles/s41598-019-54148-4" rel="noopener nofollow ugc">García-Mato et al.</a>, but the <strong>Kitware Osteotomy Planner</strong> was not working as expected. Either way, I realized later that I <em>personally</em> like using the <strong>Transforms</strong> module more than using the local transformations/interactions the <strong>Kitware Osteotomy Planner</strong> uses.</p>
<p><strong>Step-by-step:</strong></p>
<ol>
<li>
<p>I used the <strong>Dynamic Modeler</strong> to <em>recreate the Osteotomies</em> as indicated by the Surgeon. I mostly used <strong>plane cuts</strong> for the osteotomies.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c5099e03686ea6e39fde3019e28da3e4b4561c4.jpeg" data-download-href="/uploads/short-url/miPaGIfqU1B2eANrVpBcEWHKVbS.jpeg?dl=1" title="figure_anterior_view_osteotomies.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5099e03686ea6e39fde3019e28da3e4b4561c4_2_217x250.jpeg" alt="figure_anterior_view_osteotomies.PNG" data-base62-sha1="miPaGIfqU1B2eANrVpBcEWHKVbS" width="217" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5099e03686ea6e39fde3019e28da3e4b4561c4_2_217x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5099e03686ea6e39fde3019e28da3e4b4561c4_2_325x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c5099e03686ea6e39fde3019e28da3e4b4561c4_2_434x500.jpeg 2x" data-dominant-color="C4BBAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_anterior_view_osteotomies.PNG</span><span class="informations">658×755 93.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>For <em>relative translations</em> of the bone segments I used the <strong>Transform</strong> module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59930da84f8914054599e68bb15f62efdc66f46c.png" data-download-href="/uploads/short-url/cMpyqg228jveD2cslePMCnYH9hy.png?dl=1" title="figure_orbital_advancement" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59930da84f8914054599e68bb15f62efdc66f46c_2_345x222.png" alt="figure_orbital_advancement" data-base62-sha1="cMpyqg228jveD2cslePMCnYH9hy" width="345" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59930da84f8914054599e68bb15f62efdc66f46c_2_345x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59930da84f8914054599e68bb15f62efdc66f46c_2_517x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59930da84f8914054599e68bb15f62efdc66f46c_2_690x444.png 2x" data-dominant-color="C6BDB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_orbital_advancement</span><span class="informations">931×601 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>Advancement of the Orbital Segments, Superior View</em></p>
</li>
<li>
<p>For <em>local rotations</em>, I had to create my own <strong>Axis of Rotation</strong> or <strong>Pivot Axis</strong> by creating a vertical <strong>Line</strong> on the midsagittal plane and coincident with the anterior edge of the advanced orbital segments. To perform the actual rotation, I then used <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-line" rel="noopener nofollow ugc">this script</a> from the Slicer doc.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a246b3792152642ca06c620d6c33b0ed5cd2df1.png" data-download-href="/uploads/short-url/lZByyEZDA2isl29zfKgTeBB0t3j.png?dl=1" title="figure_anterior_view_orbital_rotation_about_midsaggital_axis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a246b3792152642ca06c620d6c33b0ed5cd2df1_2_345x224.png" alt="figure_anterior_view_orbital_rotation_about_midsaggital_axis" data-base62-sha1="lZByyEZDA2isl29zfKgTeBB0t3j" width="345" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a246b3792152642ca06c620d6c33b0ed5cd2df1_2_345x224.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a246b3792152642ca06c620d6c33b0ed5cd2df1_2_517x336.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a246b3792152642ca06c620d6c33b0ed5cd2df1_2_690x448.png 2x" data-dominant-color="BEB5AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_anterior_view_orbital_rotation_about_midsaggital_axis</span><span class="informations">921×598 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>Local Rotation of the Left Orbital Segments, Superior View</em></p>
<ol start="4">
<li>I kept repeating steps (2-3) to recreate the motions and rotations indicated by the Surgeon. This required two additional pivot axes. We generated two different positions of the Bandeau, one more aggressive than the other.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5d26cadfacc77206067188a56077fb276cab158.png" data-download-href="/uploads/short-url/uvyx5td0U5rTngqBCA18cOW5jwk.png?dl=1" title="figure_bandeau_compariosn_duperior_view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5d26cadfacc77206067188a56077fb276cab158_2_345x238.png" alt="figure_bandeau_compariosn_duperior_view" data-base62-sha1="uvyx5td0U5rTngqBCA18cOW5jwk" width="345" height="238" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5d26cadfacc77206067188a56077fb276cab158_2_345x238.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5d26cadfacc77206067188a56077fb276cab158_2_517x357.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5d26cadfacc77206067188a56077fb276cab158_2_690x476.png 2x" data-dominant-color="C6C5BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_bandeau_compariosn_duperior_view</span><span class="informations">877×606 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="5">
<li><strong>Experimental</strong>: Finally, we overlaid the Bandeau onto the soft-tissue segmentations to <strong>“see”</strong> the degree of improvements on the orbits. Would be nice to do something with displacement maps! (working on this now, will update later)</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c81dc0880741423d2279f0aecfd59dc561bdf1.jpeg" data-download-href="/uploads/short-url/ne261LKt8E1WzJ6zCkOSbdYPaz7.jpeg?dl=1" title="figure_soft_tissue_overlay.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2c81dc0880741423d2279f0aecfd59dc561bdf1_2_345x214.jpeg" alt="figure_soft_tissue_overlay.PNG" data-base62-sha1="ne261LKt8E1WzJ6zCkOSbdYPaz7" width="345" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2c81dc0880741423d2279f0aecfd59dc561bdf1_2_345x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2c81dc0880741423d2279f0aecfd59dc561bdf1_2_517x321.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2c81dc0880741423d2279f0aecfd59dc561bdf1_2_690x428.jpeg 2x" data-dominant-color="83A58F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_soft_tissue_overlay.PNG</span><span class="informations">696×433 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Challenges moving forth:</strong></p>
<ol>
<li>
<p>For every rotation I had to use the script from the doc. <strong>Is there a more elegant way of indicating a local rotation on the Transforms module?</strong> Is the solution to convert the script into a Python module/function that I just call every time? (instead of copying and pasting)</p>
</li>
<li>
<p>Is there a way of <strong>“linking”</strong> or <strong>“creating dependencies”</strong> on the transformations? My goal is to update the initial advancement (for instance) and allow for slicer to make all of the updates downstream, does that make sense?</p>
</li>
<li>
<p>Is there a way of using a <strong>Displacement Map</strong> generated from <strong>Model to Model Distance</strong> to then warp another model, say the soft tissue in step 5?</p>
</li>
</ol>
<p><strong>Thank you!</strong></p>

---

## Post #3 by @pieper (2021-07-07 16:55 UTC)

<p>Hi -</p>
<p>The answers to all three questions is yes, with some effort and programming.  The first one is probably the easiest, if you can define a workflow and user interface that would simplify the interaction you could make a scripted modules that exposes exactly the controls needed.  This module could also enforce dependencies or manage a transform hierarchy like you mention in your second question.  It’s also pretty easy to define warping transforms based on landmarks.  There is a lot of example code for all of these things.</p>
<p>If you aren’t able to learn or do the programming yourself, perhaps you can find a colleague or student who can help or you an hire a programmer with the right skills to implement what you need.</p>

---

## Post #4 by @Sam_Horvath (2021-07-07 17:16 UTC)

<p>Hi,</p>
<p>Sorry that I missed your previous messages.  We are in the process of pushing updates (including bending) to the Osteotomy Planner, so they should be available in the nest week.</p>

---

## Post #5 by @Fluvio_Lobo (2021-07-08 13:09 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>,</p>
<p>Thank you! I will keep an eye for the updates. I have another case coming up!</p>

---

## Post #6 by @Fluvio_Lobo (2021-07-08 14:45 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Thank you for your response!</p>
<blockquote>
<p>The answers to all three questions is yes, with some effort and programming. The first one is probably the easiest, if you can define a workflow and user interface that would simplify the interaction you could make a scripted modules that exposes exactly the controls needed. This module could also enforce dependencies or manage a transform hierarchy like you mention in your second question.</p>
</blockquote>
<p>I figured I would have to build something, just wanted to know if someone had already looked into it and save me some time <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>It’s also pretty easy to define warping transforms based on landmarks. There is a lot of example code for all of these things.</p>
</blockquote>
<p>So I tried this the other day, but it did not work as expected. I believe (could be wrong) the warping transform is affected by the number of fiducials used. I felt like I was using fiducials on arbitrary points on the model’s surface instead of landmarks, just so the warping transform wrapped around that feature better. Does that make sense? I am going to re-test this and create a new post.</p>

---

## Post #7 by @pieper (2021-07-08 14:51 UTC)

<p><a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> it sounds like there might be a lot of what you need in the code that Sam is going to push, so it’ll be worth testing and looking through that.  Perhaps you can contribute any extra features to that code base.  It’s true that warping transforms (e.g. thin plate spline) are complex and usually you need to carefully match landmarks.  Using a lower dimensional transform might work better.</p>

---

## Post #8 by @lassoan (2021-07-08 15:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="18384">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Using a lower dimensional transform might work better.</p>
</blockquote>
</aside>
<p>I agree. While developing the “Curved Planar Reformat” bending module (currently in Sandbox extension) I spent quite a bit of time with this. First I used thin plate spline (TPS) and b-spline transform and the forward transform worked mostly OK, but the inverse computation was very unstable. Then I switched to grid transform (same as b-spline transform but uses linear interpolation between grid points) and the inverse computation has become stable for all reasonable inputs.</p>
<p>Inverse computation is very important because when you warp models or markups then you need the forward (a.k.a. modeling) transform but when you warp an image then you need the inverse (a.k.a. resampling) transform. Inverse transform is also useful so that you can synchronize any information between the original and warped space (you can specify landmark points, cutting curves, etc. in either of the spaces and transform it to the other).</p>

---

## Post #9 by @Fluvio_Lobo (2021-07-12 01:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Below is my approach at using <strong>Fiducial Registration</strong> to create a <strong>Warping</strong> transform and deform the skin of the model to match the motion of the osteotomies.</p>
<ol>
<li>I appended the model of the Skull to both the Original Orbital Bandeau and the Advanced/Modified Bandeau, creating a “Source” and “Target” model. My goal here is to ensure that the transformation  requires a deformation of the model, rather than simply resulting in a translation.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83fce191b1cde4af3dd5141e759ce75b7b35f10d.png" data-download-href="/uploads/short-url/iPClk8RpDjrZQwdAPsVT64PS8J7.png?dl=1" title="source" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fce191b1cde4af3dd5141e759ce75b7b35f10d_2_345x210.png" alt="source" data-base62-sha1="iPClk8RpDjrZQwdAPsVT64PS8J7" width="345" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fce191b1cde4af3dd5141e759ce75b7b35f10d_2_345x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fce191b1cde4af3dd5141e759ce75b7b35f10d_2_517x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fce191b1cde4af3dd5141e759ce75b7b35f10d_2_690x420.png 2x" data-dominant-color="4C442E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">source</span><span class="informations">1165×712 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55d2d3307bfe4cf37a81c513c18911537c7db156.png" data-download-href="/uploads/short-url/cfeh4ysqNSpushSonokalnvadSe.png?dl=1" title="target" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55d2d3307bfe4cf37a81c513c18911537c7db156_2_345x216.png" alt="target" data-base62-sha1="cfeh4ysqNSpushSonokalnvadSe" width="345" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55d2d3307bfe4cf37a81c513c18911537c7db156_2_345x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55d2d3307bfe4cf37a81c513c18911537c7db156_2_517x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55d2d3307bfe4cf37a81c513c18911537c7db156_2_690x432.png 2x" data-dominant-color="4F4630"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">target</span><span class="informations">1138×715 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>I added “From” and “To” Fiducials to both the “Source” and “Target” models, with some of these coinciding on the Skull</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8098f8a87e2d70e63e1becd0cf53571910a8c59f.jpeg" data-download-href="/uploads/short-url/ilCR3xQYUtT230KGC0K8aHv1HwH.jpeg?dl=1" title="source_with_fiducials.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8098f8a87e2d70e63e1becd0cf53571910a8c59f_2_341x250.jpeg" alt="source_with_fiducials.PNG" data-base62-sha1="ilCR3xQYUtT230KGC0K8aHv1HwH" width="341" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8098f8a87e2d70e63e1becd0cf53571910a8c59f_2_341x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8098f8a87e2d70e63e1becd0cf53571910a8c59f_2_511x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8098f8a87e2d70e63e1becd0cf53571910a8c59f_2_682x500.jpeg 2x" data-dominant-color="3C3524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">source_with_fiducials.PNG</span><span class="informations">1222×894 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a57ef26e6307ebb650d70eadc518c848d4a4631.jpeg" data-download-href="/uploads/short-url/jJQhV6yQAUnNzFvx9qnoJcZjhoB.jpeg?dl=1" title="target_with_fiducials.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a57ef26e6307ebb650d70eadc518c848d4a4631_2_341x250.jpeg" alt="target_with_fiducials.PNG" data-base62-sha1="jJQhV6yQAUnNzFvx9qnoJcZjhoB" width="341" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a57ef26e6307ebb650d70eadc518c848d4a4631_2_341x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a57ef26e6307ebb650d70eadc518c848d4a4631_2_511x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8a57ef26e6307ebb650d70eadc518c848d4a4631_2_682x500.jpeg 2x" data-dominant-color="3C3625"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">target_with_fiducials.PNG</span><span class="informations">1222×894 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>I generated a “Warping” transform using the Fiducial Registration Module and applied it to a model of the patient’s soft tissue.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/2259ffa15a38b9b2e8e04e630ef5d11d3c5e4740.jpeg" data-download-href="/uploads/short-url/4TT3psQr1mNpHdFHHlVJ252mfhm.jpeg?dl=1" title="source_screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2259ffa15a38b9b2e8e04e630ef5d11d3c5e4740_2_341x250.jpeg" alt="source_screen" data-base62-sha1="4TT3psQr1mNpHdFHHlVJ252mfhm" width="341" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2259ffa15a38b9b2e8e04e630ef5d11d3c5e4740_2_341x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2259ffa15a38b9b2e8e04e630ef5d11d3c5e4740_2_511x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2259ffa15a38b9b2e8e04e630ef5d11d3c5e4740_2_682x500.jpeg 2x" data-dominant-color="355A38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">source_screen</span><span class="informations">1222×894 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71d30091129f47127d91ab36f5f2d28b68386885.jpeg" data-download-href="/uploads/short-url/geW1vtMLfvRJ4ELGxwDDIouOmyx.jpeg?dl=1" title="target_skin_screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d30091129f47127d91ab36f5f2d28b68386885_2_341x250.jpeg" alt="target_skin_screen" data-base62-sha1="geW1vtMLfvRJ4ELGxwDDIouOmyx" width="341" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d30091129f47127d91ab36f5f2d28b68386885_2_341x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d30091129f47127d91ab36f5f2d28b68386885_2_511x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d30091129f47127d91ab36f5f2d28b68386885_2_682x500.jpeg 2x" data-dominant-color="355B38"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">target_skin_screen</span><span class="informations">1222×894 87.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This seemed to work but I believe it is influenced by areas with more fiducials. The right orbit of the skull model has like 2-3 more fiducials and there seems to be more deformation on that side. A simple overlay of the two models shows this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a90c2e25f38c89eceafd3a95467c9ec8134a298e.jpeg" data-download-href="/uploads/short-url/o7sMTp3HGrUIPnlQOn7ca8SBnae.jpeg?dl=1" title="skin_overlay" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_512x375.jpeg" alt="skin_overlay" data-base62-sha1="o7sMTp3HGrUIPnlQOn7ca8SBnae" width="512" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_512x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_768x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_1024x750.jpeg 2x" data-dominant-color="33462D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">skin_overlay</span><span class="informations">1222×894 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, my questions are:</p>
<ol>
<li>Is this a valid approach?</li>
<li>Is this an efficient approach? or, is there a more generalized solution?</li>
<li>Is there a way of using the surface vertices of the models as fiducials?</li>
</ol>
<p>Thank you!</p>

---

## Post #10 by @manjula (2021-07-13 15:51 UTC)

<p>Hi <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> , thank you for sharing the information and the workflow. I find this very helpful. Right now workflow I feel a bit too complicated for me to use but it get the work done.  Once you have this workflow mastered please share it with us.</p>
<p>Few of my comments if it is any help for you.<br>
About the soft tissue prediction, are you applying the same amount of transformation to the soft tissue as the bone segments? Usually, the soft tissue response is less than the hard tissue movement and generally around 50 % but this depends on the area of the face. So will it be possible to adjust to this?</p>
<p>Is it not possible to implement a  proportional transformation from the fiducial points to the skin?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc4e41ef6c46e0b57c8a68a771561148fc927b5b.gif" alt="output" data-base62-sha1="vqUHZuSWTvOYQXOoRsAi4fSYOkr" width="345" height="194" class="animated"></p>
<p>Thank you once again for sharing.</p>

---

## Post #11 by @Fluvio_Lobo (2021-07-13 22:29 UTC)

<p>Hey <a class="mention" href="/u/manjula">@manjula</a>! Glad you found this useful. I am trying to make some adjustments and update this post. My goal is to get something a little more streamlined before the next procedure.</p>
<blockquote>
<p>Few of my comments if it is any help for you.<br>
About the soft tissue prediction, are you applying the same amount of transformation to the soft tissue as the bone segments? Usually, the soft tissue response is less than the hard tissue movement and generally around 50 % but this depends on the area of the face. So will it be possible to adjust to this?</p>
</blockquote>
<p>Part of the discussion on this step of the workflow is <a href="https://discourse.slicer.org/t/using-displacement-map-to-deform-or-morph-a-segment-model/18552">here</a>. I don’t have anything new at the moment but you are correct, a straight warping transformation wont yield an accurate result. At this point I am mostly experimenting. I will likely end-up using an FEA solution to really simulate the deformation of the skin.</p>
<blockquote>
<p>Is it not possible to implement a proportional transformation from the fiducial points to the skin?</p>
</blockquote>
<p>Do not know enough yet but I do not see why not. You can probably scale the transform matrix programmatically.</p>

---

## Post #12 by @pieper (2021-07-14 14:57 UTC)

<p>Hi <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> can you give a little background on your goals?  Will you be doing this frequently?</p>

---

## Post #13 by @Fluvio_Lobo (2021-07-14 17:11 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I currently support the CMF team at Orlando Health (Orlando, FL). We are hoping to bring planning and 3D printing in-house, which we are already in the process of doing.</p>
<p>CMF surgeons wanted to explore planning and printing solutions for Craniosynostosis cases. Specifically two procedures so far: <strong>Cranial Vault Remodeling (CVR)</strong> and <strong>Fronto-Orbital Advancement (FOA)</strong>. There are more, but these are the ones I have worked on.</p>
<blockquote>
<p>Hi <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a> can you give a little background on your goals?</p>
</blockquote>
<p>My <strong>main</strong> goal is to establish a workflow for planning and 3D printing of anatomical replicas resulting from said planning. For instance, a printed model of the <strong>Orbital Bandeau</strong> that was modeled through the planning.</p>
<p>Here is a picture of what that looks like;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ec4d317bc9f89ee58d4fada15623e8beb0069ae.jpeg" data-download-href="/uploads/short-url/8Xhit4YswWlZPMHYXGeUkf59md8.jpeg?dl=1" title="image0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec4d317bc9f89ee58d4fada15623e8beb0069ae_2_187x250.jpeg" alt="image0" data-base62-sha1="8Xhit4YswWlZPMHYXGeUkf59md8" width="187" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec4d317bc9f89ee58d4fada15623e8beb0069ae_2_187x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec4d317bc9f89ee58d4fada15623e8beb0069ae_2_280x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec4d317bc9f89ee58d4fada15623e8beb0069ae_2_374x500.jpeg 2x" data-dominant-color="857E7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image0</span><span class="informations">3024×4032 1.6 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A <strong>secondary goal</strong> is to <strong>estimate</strong> the post surgical appearance of the patient’s skin after the advancement. This is the reason why I am playing around with warping transforms and will soon have to use FEA. I still want to explore a non-realistic warping method as “guesstimation” <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20"></p>
<p>I am working on a few tricks based on your feedback and other feedback I got <a href="https://discourse.slicer.org/t/using-displacement-map-to-deform-or-morph-a-segment-model/18552">here</a>. I have not had a chance to test/update this post, but will do before then end of the week</p>
<blockquote>
<p>Will you be doing this frequently?</p>
</blockquote>
<p>Depends on your definition of frequently.</p>
<p>The latest estimate is 8-12 craniosynostosis cases per year (2-3 for <strong>FOA</strong>). The CMF crew has another <strong>FOA</strong> and two <strong>CVRs</strong> this summer. I think 8-12 and 2-3 are underestimates.</p>
<p>These procedures do not have the volume of say Orthognathic surgery and this is the reason why it is so underserved by commercial applications.</p>

---

## Post #14 by @pieper (2021-07-14 18:01 UTC)

<p>Thanks for the extra background <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a>, yes, that answers my question.  I was curious if this was a one-time test or something you would be doing multiple times and it does sound like something where some time investment on custom development could great improve the workflow and accuracy of the analysis and hopefully the surgery too.</p>
<p>I worked on a somewhat related topic for my <a href="https://isomics.com/caps/">PhD some years ago</a> so I’m really interested in seeing what can be done with the current generation of hardware and software together with all the new interactivity in Slicer (VR, XR, etc).</p>

---

## Post #15 by @Fluvio_Lobo (2021-07-15 00:52 UTC)

<blockquote>
<p>I was curious if this was a one-time test or something you would be doing multiple times and it does sound like something where some time investment on custom development could great improve the workflow and accuracy of the analysis and hopefully the surgery too.</p>
</blockquote>
<p>I am trying to identify procedures that I think need workflow optimization and maybe a custom solutions. Craniosynostosis seems to be one of those procedures.</p>
<blockquote>
<p>I worked on a somewhat related topic for my <a href="https://isomics.com/caps/" rel="noopener nofollow ugc">PhD some years ago</a> so I’m really interested in seeing what can be done with the current generation of hardware and software together with all the new interactivity in Slicer (VR, XR, etc).</p>
</blockquote>
<p>This is really cool work and waaaay ahead of its time! Those pictures made me think of N64 Goldeneye <img src="https://emoji.discourse-cdn.com/twitter/rofl.png?v=12" title=":rofl:" class="emoji" alt=":rofl:" loading="lazy" width="20" height="20"></p>
<p>I still need to make some time this week to work more on the skin warping and hopefully simulating. I am hoping to update this post with findings and I may tag you if that is ok!</p>

---

## Post #16 by @pieper (2021-07-15 14:52 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="15" data-topic="18384">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>I may tag you if that is ok!</p>
</blockquote>
</aside>
<p>Yes, definitely - very interested to see this develop!</p>

---
