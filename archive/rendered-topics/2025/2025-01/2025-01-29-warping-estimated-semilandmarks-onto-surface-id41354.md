---
topic_id: 41354
title: "Warping Estimated Semilandmarks Onto Surface"
date: 2025-01-29
url: https://discourse.slicer.org/t/41354
---

# Warping estimated semilandmarks onto surface

**Topic ID**: 41354
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/warping-estimated-semilandmarks-onto-surface/41354

---

## Post #1 by @stineblom (2025-01-29 13:58 UTC)

<p>Hello!</p>
<p>Using pseudoLMgenerator and ALPACA, I have produced 499 pseudolandmarks on a sample of scapulae from different species that cover the whole surface/shape. From these, I made an ancestral shape reconstruction (ASR), estimating the landmarks of a non-existing scapula. I am trying to translate these landmarks into a surface, but it seems to be challenging with only sliding semilandmarks, no point landmarks or curves. So far, I have gotten this using Markups to Model, but assuming the ancestor is not a cubic organism, I wonder if you know or have experience with other tools to create an artificial surface from pseudolandmarks?<br>
Here you can see the template model+landmarks and the markups to modul and the ASR landmarks:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e635cae406769aec1c92208156ccc70b23b2ccf.png" data-download-href="/uploads/short-url/fKxp2GFPaNOuC6lWyCHUqnewtZl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e635cae406769aec1c92208156ccc70b23b2ccf_2_335x499.png" alt="image" data-base62-sha1="fKxp2GFPaNOuC6lWyCHUqnewtZl" width="335" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e635cae406769aec1c92208156ccc70b23b2ccf_2_335x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e635cae406769aec1c92208156ccc70b23b2ccf_2_502x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e635cae406769aec1c92208156ccc70b23b2ccf.png 2x" data-dominant-color="AEA17E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">650×968 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c9f6fa24d6e26c33212e39b8d890dbb30bb59b0.png" data-download-href="/uploads/short-url/k40r2feeU7q5xbsOaDjiRTDSBRC.png?dl=1" title="template_model_LM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9f6fa24d6e26c33212e39b8d890dbb30bb59b0_2_226x500.png" alt="template_model_LM" data-base62-sha1="k40r2feeU7q5xbsOaDjiRTDSBRC" width="226" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9f6fa24d6e26c33212e39b8d890dbb30bb59b0_2_226x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9f6fa24d6e26c33212e39b8d890dbb30bb59b0_2_339x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c9f6fa24d6e26c33212e39b8d890dbb30bb59b0.png 2x" data-dominant-color="A99983"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">template_model_LM</span><span class="informations">416×918 292 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, should I run a GPA on the ASR prior to the warping?</p>
<p>Thank you in advance,<br>
Stine</p>

---

## Post #2 by @muratmaga (2025-01-29 14:56 UTC)

<p>I am not familiar with ASR. Does that mean you are trying to estimate what the shape would be given a set of estimated landmark?</p>
<p>If that’s the case, you should use a set of reference LMs and shape to start the process. Then you will create a warping transform using that maps the reference points into the space of the estimated points. Then you will take the resultant transform and apply it to the reference shape, which will deform it based on that mapping.</p>
<p>You can do all of these using the IGT extensions Fiducial Registration Wizard module.</p>

---

## Post #3 by @stineblom (2025-01-30 10:13 UTC)

<p>Hi Murat!</p>
<p>Thank you for your rapid response. Yes, you are correct, I am trying to estimate the shape from estimated landmarks and I also think you are absolutely right about using the ‘Fiducial Registration Wizard’. However, I encounter errors that I have trouble identifying.</p>
<p>Both the manual and automatic warping transform seem to fail. I think it is either because of the number of landmarks (which the error states) or something with the actual landmarks (they are tiny in the visualization wondow, but zooming in they are similar to the reference). Can it be because the reference scap and LM are prior to GPA, while the estimated ASR LM are made after GPA and based on the consensus of all specimens in my sample?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cea4a5cac09505575b498e053ee3cce83ea29f3.jpeg" data-download-href="/uploads/short-url/6pkYn1iPfsgXNWkQ0UboMJSlcI3.jpeg?dl=1" title="slicer_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cea4a5cac09505575b498e053ee3cce83ea29f3_2_690x316.jpeg" alt="slicer_error" data-base62-sha1="6pkYn1iPfsgXNWkQ0UboMJSlcI3" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cea4a5cac09505575b498e053ee3cce83ea29f3_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cea4a5cac09505575b498e053ee3cce83ea29f3_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cea4a5cac09505575b498e053ee3cce83ea29f3_2_1380x632.jpeg 2x" data-dominant-color="D7D4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_error</span><span class="informations">1920×880 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I hope I am explaining this well enough, I have trouble understanding what is going on myself…</p>
<p>Thank you!<br>
Stine</p>

---

## Post #4 by @muratmaga (2025-01-30 10:59 UTC)

<aside class="quote no-group" data-username="stineblom" data-post="3" data-topic="41354">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/d6d6ee/48.png" class="avatar"> stineblom:</div>
<blockquote>
<p>(they are tiny in the visualization wondow, but zooming in they are similar to the reference).</p>
</blockquote>
</aside>
<p>I can’t quite read the full error message. But to rule out loss of precision due to very small numbers, perhaps you can scale the reference model and reference landmarks by 1000 prior to running the Fiducial registration wizard.</p>

---

## Post #5 by @stineblom (2025-01-30 16:01 UTC)

<p>I scaled the reference model and landmarks as you said. At least they are the same size now.</p>
<p>When trying to make a Transform warping manually, it says: Status: Registration Complete. RMS Error: 0.000919. When trying automatically, it shows this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5479fb0322abf112dcc549dce5e8177d51526d1.png" data-download-href="/uploads/short-url/nA8eCGpglEhSzXC1fLrq3BVbUU9.png?dl=1" title="slicer_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5479fb0322abf112dcc549dce5e8177d51526d1_2_689x295.png" alt="slicer_error" data-base62-sha1="nA8eCGpglEhSzXC1fLrq3BVbUU9" width="689" height="295" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5479fb0322abf112dcc549dce5e8177d51526d1_2_689x295.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5479fb0322abf112dcc549dce5e8177d51526d1_2_1033x442.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5479fb0322abf112dcc549dce5e8177d51526d1_2_1378x590.png 2x" data-dominant-color="D6D6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_error</span><span class="informations">2533×1084 363 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If 499 LM too much or am I doing something else incorrectly?</p>

---

## Post #6 by @muratmaga (2025-01-30 16:13 UTC)

<p>I don’t think you are doing anything wrong. It actually completed the TPS, but somehow wasn’t able to create the transform (as I understood from the error message).</p>
<p>Is it possible to share the scene with:</p>
<ol>
<li>Estimates LMs</li>
<li>Reference LM and model</li>
</ol>

---

## Post #7 by @stineblom (2025-01-31 08:11 UTC)

<p>I sent you the data via email. Thanks!!</p>

---

## Post #8 by @muratmaga (2025-01-31 10:01 UTC)

<p>OK, i got your data. There are few issues:</p>
<ol>
<li>One of your LMs is from a left scapula, and the other one is a right one. You cannot mix L and R samples in a landmark shape analysis. You need to reflect one side to the other.</li>
<li>I proceed to do with that (I reflect the great ape ancestor to match that of model), and I also arbitrarily scaled everything by 100 to make visualizations easier.</li>
</ol>
<p>Then, things worked out as it should. The image on the left (and landmarks) are your reference model you have provided, and the one on the right is the deformed model to match the ancestral state. You can see the shape of scapula is altered. Howeverr, there is a non-sensical deformation taking one point and stretching to the infinity. I suspect if your original results from which you estimated the landmark points, may have mixed L/R specimen, which would invalidate the analysis.</p>
<p>Anyways, all I can say things are working as it should, but you should have all your samples in one orientation, repeat the whole GPA and then rerun the thing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d8e8544715622cd12e07843ff4efc713413544.jpeg" data-download-href="/uploads/short-url/zdIb9QZxPiqxzLJVRzl6g1tmzQw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6d8e8544715622cd12e07843ff4efc713413544_2_690x308.jpeg" alt="image" data-base62-sha1="zdIb9QZxPiqxzLJVRzl6g1tmzQw" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6d8e8544715622cd12e07843ff4efc713413544_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6d8e8544715622cd12e07843ff4efc713413544_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d8e8544715622cd12e07843ff4efc713413544.jpeg 2x" data-dominant-color="A59AAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1314×587 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @stineblom (2025-02-05 13:47 UTC)

<p>Amazing - I finally got it to work! Thank you so much for the time and help! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
