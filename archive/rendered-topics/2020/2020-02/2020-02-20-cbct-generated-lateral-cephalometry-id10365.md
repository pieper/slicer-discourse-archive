---
topic_id: 10365
title: "Cbct Generated Lateral Cephalometry"
date: 2020-02-20
url: https://discourse.slicer.org/t/10365
---

# CBCT generated Lateral Cephalometry

**Topic ID**: 10365
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/cbct-generated-lateral-cephalometry/10365

---

## Post #1 by @manjula (2020-02-20 15:03 UTC)

<p>One of my colleagues came across this <a href="https://drive.google.com/open?id=1WfDbTtEtOaPJefcx2miPo1_Fp6Yk-rSA" rel="noopener nofollow ugc">article</a> and we tried to do the same with 3D Slicer. I</p>
<p>It says two algorithms are used for generation of cephalograms from CBCT data.</p>
<ol>
<li>
<p>maximum intensity projection</p>
</li>
<li>
<p>RayCast –  3D data are visualized by summing all values of the voxels from the viewpoint to the plane of projection and dividing this number by the number of voxels</p>
</li>
</ol>
<p>I think we achived the MIP part,  (Masking was not done nicely … was in a hurry to see it works )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c429ae0988053b9aac267825da12c2953f70b312.jpeg" data-download-href="/uploads/short-url/rZkSJD4t3WOUQrWdKzeAK3NgQYa.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429ae0988053b9aac267825da12c2953f70b312_2_416x500.jpeg" alt="Screenshot_1" data-base62-sha1="rZkSJD4t3WOUQrWdKzeAK3NgQYa" width="416" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c429ae0988053b9aac267825da12c2953f70b312_2_416x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c429ae0988053b9aac267825da12c2953f70b312.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c429ae0988053b9aac267825da12c2953f70b312.jpeg 2x" data-dominant-color="646464"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">439×527 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And we use volume render to get this image, thinking this is the RayCasting as it says “VTK GPU raycasting” .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97f642aaa7f2acd62e63d32f0a3273fff00bfc03.png" data-download-href="/uploads/short-url/lGjHVEyou3hZhiDG9tivFVV4YNB.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97f642aaa7f2acd62e63d32f0a3273fff00bfc03_2_690x276.png" alt="Screenshot" data-base62-sha1="lGjHVEyou3hZhiDG9tivFVV4YNB" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97f642aaa7f2acd62e63d32f0a3273fff00bfc03_2_690x276.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97f642aaa7f2acd62e63d32f0a3273fff00bfc03_2_1035x414.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97f642aaa7f2acd62e63d32f0a3273fff00bfc03.png 2x" data-dominant-color="292829"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1319×528 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So,</p>
<ol>
<li>
<p>Is our MIP is correct ?</p>
</li>
<li>
<p>Is our RayCasting is correct ?</p>
</li>
<li>
<p>Is there any other way of generating cephalograms from CBCT data ? a better technique ?</p>
</li>
</ol>

---

## Post #2 by @lassoan (2020-02-25 00:03 UTC)

<p>The authors use quite strange terminology. Both methods are based on raycasting - in one case you use maximum value along the ray, in the other case you use the mean value. If you use the mean value then it is an X-ray-like image, which I’ll call mean Digitally Reconstructed Radiograph (DRR). I don’t see any reason why anyone would even consider using MIP for finding anatomical landmarks and planes on bony anatomy, but nevertheless, you can get DRR and MIP images in both slice and 3D views quite easily.</p>
<p><strong>Slice views:</strong> Advantage is that you get a 2D planar image that you can directly measure things on. It uses parallel projection, so the distances that you measure are correct (do not depend on distance from source). Disadvantage that it is computed entirely in the CPU, so it is slow. You can generate it using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections">this script</a>. Use “SetSlabModeToMean” for getting DRR and “SetSlabModeToMax” for getting MIP.</p>
<p><strong>3D views:</strong> Use Volume Rendering module with “CT-X-ray” rendering preset and set view background to black to get DRR. Switch to “CT-MIP” volume rendering preset and set Advanced / Techniques / Advanced rendering properties / Technique -&gt; Maximum Intensity Projection.</p>

---

## Post #3 by @manjula (2020-02-25 21:32 UTC)

<p>Dear Prof Lasso, Thank you for your detailed explanation on this.  I tried all recipes.</p>
<p>When it comes to MIP it works the same.</p>
<p>But when it comes to DRR, we do not see the outline of the orbits which is essential for lateral ceph analysis. So in the article it must be something else that they have used for this as the orbital out line is very nice.<br>
However in the bottom photo  i attached above which is from the 3D view we can get it to see the orbital outline as well. So that is why we were thinking this must be what they have done also under what is mentioned as “raycasting technique”. But as you said it would be very inaccurate to measure in the 3D view.</p>

---

## Post #4 by @lassoan (2020-02-25 23:48 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="10365">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>But when it comes to DRR, we do not see the outline of the orbits</p>
</blockquote>
</aside>
<p>In 3D views, you need to adjust the scalar opacity transfer function to optimize visibility of the structures you are interested in - the same way as you would adjust X-ray exposure parameters depending on patient thickness and details that you want to visualize - bones, soft tissues, etc.</p>
<p>In slice views, you may need to adjust window/level. If that is not sufficient then you may apply some non-linear image intensity transformation to emphasize certain structures while suppress others. The simplest would be a ramp function (similar to the one used as scalar opacity transfer function). You can apply a function to the voxel array using numpy, as shown in examples in the script repository.</p>

---
