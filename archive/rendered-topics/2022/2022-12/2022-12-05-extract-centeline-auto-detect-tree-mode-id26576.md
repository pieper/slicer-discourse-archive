# Extract centeline Auto-detect tree mode

**Topic ID**: 26576
**Date**: 2022-12-05
**URL**: https://discourse.slicer.org/t/extract-centeline-auto-detect-tree-mode/26576

---

## Post #1 by @bserrano (2022-12-05 11:50 UTC)

<p>Hello,</p>
<p>I am using the Extact Centerline module with Endpoints Autodetect to generate the centerlines over all the vessels of a coronary tree. For this I use the tree option.<br>
After a couple of attempts and smoothing the geometry I have obtained something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/411d3e0d141bb72bd75d33c12c0f10a05a453927.png" data-download-href="/uploads/short-url/9i1GBefk98HlfSdeASPPwKZPZGf.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/411d3e0d141bb72bd75d33c12c0f10a05a453927_2_690x303.png" alt="imagen" data-base62-sha1="9i1GBefk98HlfSdeASPPwKZPZGf" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/411d3e0d141bb72bd75d33c12c0f10a05a453927_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/411d3e0d141bb72bd75d33c12c0f10a05a453927_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/411d3e0d141bb72bd75d33c12c0f10a05a453927.png 2x" data-dominant-color="38384E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1197×527 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, I am trying with other patients and I am not able to get all the curves. The program gives me the model but only 1 centreline.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d222d20178670de6c52d0f2f00dfc2d1d14f55.jpeg" data-download-href="/uploads/short-url/nEUZOkr9h2VD939xHbqDte5zbwN.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d222d20178670de6c52d0f2f00dfc2d1d14f55_2_418x500.jpeg" alt="imagen" data-base62-sha1="nEUZOkr9h2VD939xHbqDte5zbwN" width="418" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5d222d20178670de6c52d0f2f00dfc2d1d14f55_2_418x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d222d20178670de6c52d0f2f00dfc2d1d14f55.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5d222d20178670de6c52d0f2f00dfc2d1d14f55.jpeg 2x" data-dominant-color="4A5969"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">531×635 67.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can i get all centrelines?<br>
The module is very unstable and causes the application to close suddenly on numerous occasions.<br>
I’m using Slicer 5.0.3.</p>

---

## Post #2 by @lassoan (2022-12-06 17:04 UTC)

<p>The automatic centerline endpoint detection results are editable. Feel free to move the points to more appropriate locations (for example, move the first point to the center of the aorta, remove the seemingly spurious endpoint slightly above the valve, …). Also make sure the aorta endpoint is marked as inflow (unselected - cyan by default), while others are outflow (selected - red by default).</p>
<p>If all the endpoints are set correctly and the centerline model looks good, but you only get a single curve then it means that topological analysis of the centerline tree failed.</p>
<p>You may try to increase “Target point count” to 10-20k and/or reduce “Decimation aggressiveness” in Advanced section.</p>
<p>No failure should lead to crashing of the application. We haven’t received any reports of VMTK crashing while detecting the centerline, so we are confident that it is robust, but of course there can be always some special cases that may triggered by some unexpected input data. If you can reproduce a crash with the latest stable version (Slicer-5.2) then please upload the input segmentation data somewhere (dropbox, onedrive, etc.) and post the link here so that we can investigate.</p>

---

## Post #3 by @bserrano (2022-12-07 16:32 UTC)

<p>Hello,</p>
<p>I have downloaded the new version of slicer (5.2.1) and the problem persists. For example, for this segmentation with parameters “Target point count” 10k and  “Decimation aggressiveness” 3, the program quits unexpectedly.</p>
<p>I don’t know where to change the inflow and outflow parameters for the endpoints. I’ll check if I can upload the example.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5760d2555a4214ceaedd3f8a8f4164f46469be0.jpeg" alt="imagen" data-base62-sha1="usmCKIX3epQ5kQQ10bncmZm4NFe" width="464" height="426"></p>
<p>Thanks,</p>

---

## Post #4 by @lassoan (2022-12-08 03:26 UTC)

<p>Yes, please upload the segmentation and I can have a look.</p>

---

## Post #5 by @bserrano (2023-01-02 15:19 UTC)

<p>Hi,</p>
<p>Unfortunately I can’t upload the geometry at the moment. However, I have noticed that in order to avoid unexpected behaviour it is advisable to smooth the geometry and place the endpoints a bit before the end of the vessels.</p>
<p>I have not yet found where to change the endpoint type (inflow/outflow).</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @bserrano (2023-03-17 07:56 UTC)

<p>Hi, I experimented the same problem with an aorta in this case.<br>
The geometry is extremely smooth, but Extract Centerline module continues to crash every time, closing Slicer.</p>
<p>What I want is a centerline between the endpoints as shown below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd026b48ba885dedabe728b60f6ca8da78394829.png" alt="imagen" data-base62-sha1="qY3qkNMPQSaZeDHmFOqCEe3gHeF" width="315" height="266"></p>
<p>You can find the stl here: <a href="https://nubeusc-my.sharepoint.com/:u:/g/personal/belen_serrano_anton_rai_usc_es/Eee9otPKvzZCnX-RdCxCBU0BL1B4uq6TNofL46nn8f6igg?e=jEENhn" class="inline-onebox" rel="noopener nofollow ugc">Sign in to your account</a></p>

---

## Post #7 by @lassoan (2023-03-18 04:17 UTC)

<p>The crash was due to a bug in VTK that I’ve fixed a couple of months ago, but that fix was not yet backported into Slicer’s VTK. I’ve now <a href="https://github.com/Slicer/Slicer/commit/396c8e5d0ac6bcacf413103c3cb358211a9d5d8c">backported it</a>, so centerline extraction will work robustly in Slicer Preview Release that you download on 2023-03-19 or later.</p>

---

## Post #8 by @bserrano (2023-03-20 09:28 UTC)

<p>Many thanks, so it is not yet available on Windows, right?</p>

---

## Post #9 by @lassoan (2023-03-20 12:06 UTC)

<p>The fix is already available in the latest Slicer Preview Releases on all operating systems.</p>

---

## Post #10 by @bserrano (2023-03-20 12:12 UTC)

<p>But the last preview release for Windows is from 2023-03-16<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f239a761d366b4b27d0c5bf8d632de5727f6ed4.png" data-download-href="/uploads/short-url/dzDDEqEbQ9I6h9vL0sPtmfDVa3G.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f239a761d366b4b27d0c5bf8d632de5727f6ed4.png" alt="imagen" data-base62-sha1="dzDDEqEbQ9I6h9vL0sPtmfDVa3G" width="690" height="299" data-dominant-color="F2F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">916×397 18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2023-03-20 13:19 UTC)

<p>There has been an error in the Windows builds. We’ll investigate.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could you have a look at this <a href="https://slicer.cdash.org/viewBuildError.php?onlydeltap&amp;buildid=2973787">build error on Windows due to generate_pyi.py</a>?</p>

---
