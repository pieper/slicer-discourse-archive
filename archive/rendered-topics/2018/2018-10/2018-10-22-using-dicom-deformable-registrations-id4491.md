# Using DICOM deformable registrations

**Topic ID**: 4491
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/using-dicom-deformable-registrations/4491

---

## Post #1 by @stephan (2018-10-22 20:50 UTC)

<p>Slicer version: 4.10.0<br>
SlicerRT: 0.18.0</p>
<p>Hi there,<br>
I wonder if there are known issues with loading deformable registration DICOM objects using SlicerRT.<br>
I have 2 CT volumes (“baseline” and “end”) which were registered in an external software suite (MIM 6.8.3) in a two-step process: A manual rigid registration followed by an automated (intensity based) deformable registration. Both registrations were then exported as DICOM objects and loaded into Slicer.<br>
The rigid registration is converted correctly into a LinearTransform.<br>
The deformable registration becomes two transforms: “1: DeformableReg: Intensity-based BL CT to ES CT [1]_DeformableRegistrationGrid” and “1: DeformableReg: Intensity-based BL CT to ES CT [1]_PostDeformationMatrix” (the latter being the identity transformation matrix).<br>
When I apply the rigid registration and the deformable registration to the baseline volume, the result doesn’t even display (it generates some noisy patterns, but nothing like the result in MIM). Furthermore, although the volumes were more or less aligned after the rigid registration, they do not even overlap anymore as soon as the deformable registration is applied.</p>
<p>I might just get things wrong from the start, so I wonder if someone could point me to a tutorial or something (I didn’t find post similar to my issue here on the discourse board). I would also be happy to share screenshots or the original files, if that helps.</p>
<p>Thanks for any hints.<br>
Stephan</p>

---

## Post #2 by @pieper (2018-10-22 21:11 UTC)

<p><a class="mention" href="/u/stephan">@stephan</a>  I know that <a class="mention" href="/u/gcsharp">@gcsharp</a> had created some sample datasets, I believe using MIM, but I’m not sure how widely things been tested with various configurations etc.  If you have data (no PHI) to share that illustrates any issues I’m sure that would be welcome.</p>

---

## Post #3 by @gcsharp (2018-10-22 21:52 UTC)

<p>Hi Stephen,<br>
I’m not sure of the current status of DICOM deformable registration objects.  I think it is still work in progress.  But, maybe you can try dragging the post-deformation matrix onto the deformable grid, and then drag the image onto the post-deformation matrix, until it looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e1273b8c85dd9df85be0731ed1180930df8c429.png" alt="Selection_206" data-base62-sha1="mymYmFQbjrWnlF4WulOWlcC2Z4J" width="625" height="207"></p>
<p>Greg</p>

---

## Post #4 by @stephan (2018-10-23 01:37 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/gcsharp">@gcsharp</a>.</p>
<p>I will try to share the raw data tomorrow (when I’m back at the lab). Fortunately, PHI is not an issue, as it’s an animal study and the pigs told me they won’t mind.</p>
<p>Greg, I had tried your suggestion before, in both orders (DeformableRegistrationGrid as parent of PostDeformationMatrix and vice versa), with and without the additional rigid transformation.<br>
Interestingly, the PostDeformationMatrix is diag(1,1,1,1), so it simply does not change anything.</p>
<p>Of course it might also be that MIM exports non-standard DICOM SROs. Are you by any chance aware of another free DICOM viewer that understands deformable registrations? I might then just double-check if the files can be read correctly there.<br>
The viewer I use for quickly scrolling through a CT doesn’t do image fusion or anything beyond basic display.</p>
<p>Again, thank you so much for your quick replies.<br>
Stephan</p>

---

## Post #5 by @stephan (2018-10-23 12:47 UTC)

<p>Here some screenshots to illustrate the issue:<br>
Original in MIM<br>
(top row: deformed baseline CT (rigid transform + deformable reg),<br>
center: end study CT,<br>
bottom: fusion)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4706e112744e789ec26af9275be9ed9679a6e41.jpeg" data-download-href="/uploads/short-url/ySpnJEEIbebmD2xkifdkdalKDMB.jpeg?dl=1" title="MIM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4706e112744e789ec26af9275be9ed9679a6e41_2_690x420.jpeg" alt="MIM" data-base62-sha1="ySpnJEEIbebmD2xkifdkdalKDMB" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4706e112744e789ec26af9275be9ed9679a6e41_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4706e112744e789ec26af9275be9ed9679a6e41_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4706e112744e789ec26af9275be9ed9679a6e41_2_1380x840.jpeg 2x" data-dominant-color="5E5250"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MIM</span><span class="informations">1920×1170 475 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Baseline and end study CT in slicer after applying the rigid transformation exported from MIM:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fecc83f74ebca4e07218afae84ec324eec0d55c9.jpeg" data-download-href="/uploads/short-url/Am3rTtumS4qb2Ix9ZJkpUgl9eFr.jpeg?dl=1" title="Slicer_after_rigidtransform" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fecc83f74ebca4e07218afae84ec324eec0d55c9_2_690x420.jpeg" alt="Slicer_after_rigidtransform" data-base62-sha1="Am3rTtumS4qb2Ix9ZJkpUgl9eFr" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fecc83f74ebca4e07218afae84ec324eec0d55c9_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fecc83f74ebca4e07218afae84ec324eec0d55c9_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fecc83f74ebca4e07218afae84ec324eec0d55c9_2_1380x840.jpeg 2x" data-dominant-color="414142"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_after_rigidtransform</span><span class="informations">1920×1170 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Baseline CT (viewport reset to volume limits and rotated to slice orientation) with the additional deformable registration:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fee86e416c154604c9e30a039d113e719e8a3626.jpeg" data-download-href="/uploads/short-url/An1fZwIrec5fd9V8PDkAzPjaHKm.jpeg?dl=1" title="Slicer_after_DIR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fee86e416c154604c9e30a039d113e719e8a3626_2_690x420.jpeg" alt="Slicer_after_DIR" data-base62-sha1="An1fZwIrec5fd9V8PDkAzPjaHKm" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fee86e416c154604c9e30a039d113e719e8a3626_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fee86e416c154604c9e30a039d113e719e8a3626_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fee86e416c154604c9e30a039d113e719e8a3626_2_1380x840.jpeg 2x" data-dominant-color="232324"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_after_DIR</span><span class="informations">1920×1170 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When leaving out the rigid transformation (or applying it above the deformable one, instead of below), the result is less noisy, but still does not at all reproduce the deformation in MIM.</p>
<p>Link to the original files to reproduce the issue:<br>
<a href="https://drive.google.com/drive/folders/1AdXOQUyAI8FHn_ui8MddPg7dmTWdqs5Q" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1AdXOQUyAI8FHn_ui8MddPg7dmTWdqs5Q</a></p>
<p>Please let me know if there is anything else you need.</p>
<p>Also, should I file a bug report in Mantis? If so, I would probably simply link to this thread there.</p>
<p>Thank you<br>
Stephan</p>

---

## Post #6 by @cpinter (2018-10-23 14:06 UTC)

<p><a class="mention" href="/u/stephan">@stephan</a> Import of deformable DICOM SROs is implemented but not well tested by any means. Also, export of such objects is not yet added. Luckily we have funding for fixing and improving this feature in SlicerRT, and according ot the timeline, it will be done quite soon (Nov 15 to Dec 31). Once we get there, I will fix loading of this object for your dataset as well.</p>
<p>In the meantime can you please send us the log after you load the deformable SRO? It’s in About / Report a problem. Thanks!</p>

---

## Post #7 by @lassoan (2018-10-23 15:31 UTC)

<p>Could you also send the original DICOM CTs to be able to verify the original frames of reference?</p>

---

## Post #8 by @stephan (2018-10-23 17:32 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Luckily we have funding for fixing and improving this feature in SlicerRT, and according ot the timeline, it will be done quite soon (Nov 15 to Dec 31). Once we get there, I will fix loading of this object for your dataset as well.</p>
</blockquote>
</aside>
<p>Wow, that’s really great timing!</p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>In the meantime can you please send us the log after you load the deformable SRO? It’s in About / Report a problem. Thanks!</p>
</blockquote>
</aside>
<p>The log file was too long to paste it here (mainly because the two lines</p>
<pre><code>[CRITICAL][Stream] 23.10.2018 12:19:28 [] (unknown:0) - W: Found element (3751,0104) with VR UN and undefined length, reading a sequence with transfer syntax LittleEndianImplicit (CP-246)
[CRITICAL][Stream] 23.10.2018 12:19:28 [] (unknown:0) - W: Found element (3751,0105) with VR UN and undefined length, reading a sequence with transfer syntax LittleEndianImplicit (CP-246)
</code></pre>
<p>are repeated roughly 250 times). I uploaded the log file to the <a href="https://drive.google.com/drive/folders/1AdXOQUyAI8FHn_ui8MddPg7dmTWdqs5Q" rel="noopener nofollow ugc">google drive</a> linked above.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="4491" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you also send the original DICOM CTs to be able to verify the original frames of reference?</p>
</blockquote>
</aside>
<p>I will upload them to the google drive later today.</p>
<p>Thank you all.<br>
Stephan</p>

---

## Post #9 by @lassoan (2018-10-23 23:33 UTC)

<p>I’ve checked the data sets and found the followings:</p>
<ul>
<li>The two CTs are very far from each other and also rotated by 180 deg (probably the pig was put in head-first in one image and feet-first in the other image), which results in larger and more complicated transform as usual. It is not a problem per se, but makes registration a bit harder and may cause complications in some (see below). For future scans, try to place the subject in the scanner in approximately the same position and orientation (up to 45 deg rotation and a few 10 cm translation is fine).</li>
<li>Deformable (grid) transform includes large translation and rotation. This is an issue, as grid transform is only defined in a small region (at the region of the baseline image) undefined everywhere else, which causes issues computing transformation near the region’s boundary and computing inverted transform (that is needed for transforming target points, meshes, or performing various quantifications).</li>
</ul>
<p>As a next step, configure MIM to separate transformation to bulk pre/post rigid component and a remaining deformable component. Large translation and rotation must not be included in the deformable transform component. There might be additional issues but it is difficult to investigate the issue with a deformable transform that does not behave well.</p>
<p>You may also check out SlicerElastix extension for intensity-based image registration. All you need is to rotate one of the images by 180deg to compensate for the head-first/feet-first mismatch and SlicerElastix registers the two volumes fully automatically, quite accurately, even with just using the default settings. See this animation that compares the “baseline” image registered to the “base” image:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2c81301285e91be7b7689f3665ed7536f74a569.gif" alt="HeartCtRegistration" data-base62-sha1="ne20s0LTxL8I7qJXQL9654YxuPv" width="398" height="410"></p>
<p>It seems that the deformation is mainly a change in size:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee0c2fe251c9bd7acd5b1f076b6720f7ffb8edcc.png" alt="image" data-base62-sha1="xXRKpB7CcfESfvyEtrUfaKDnuCE" width="586" height="437"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/720b992311b5a40ef7736edbe3ba35f1ec63f35d.png" alt="image" data-base62-sha1="ggThoMKmgQzwCgwYxd0tXZEi1nT" width="591" height="437"></p>

---

## Post #10 by @stephan (2018-10-24 13:04 UTC)

<p>Thank you for this thorough analysis.<br>
The fact that the volumes are flipped head-first vs. feet-first is indeed unfortunate, but I would have thought that this is taken care of by the rigid (bulk) transformation.<br>
A colleague performs the registration in MIM and I double checked with her that she first created the rigid transform to roughly align the two volumes and ran the deformable registration on the aligned volumes.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Deformable (grid) transform includes large translation and rotation.</p>
</blockquote>
</aside>
<p>So does this mean that these components, which we thought to be covered by the rigid transform, are somehow duplicated in the deformation? That would be unexpected, but if that’s the case, we would have to dig into it in MIM.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You may also check out SlicerElastix extension for intensity-based image registration.</p>
</blockquote>
</aside>
<p>Thank you for the hint. I struggled with PlastiMatch a while ago, but have not tried Elastix. The thing is that my colleague performs these registrations anyway (in MIM), so for consistency as well as to save some work, it would be really good if we could get the MIM → Slicer workflow running for this project. For other projects, however, I will definitely have a closer look at Elastix. The results in your images look great.</p>
<p>So, to conclude, would you say that the whole issue is because the deformable (grid) transform as exported by MIM is not sufficiently well-defined?<br>
Or is this just an extreme case within the limits of the DICOM standard which is not yet handled correctly by SlicerRT?<br>
I ask because there is a real chance that we can’t do much about how MIM exports these registrations, and so I wonder if we should then just wait and hope for the SlicerRT update or if I would have to start re-doing everything in Elastix.</p>
<p>Thank you very much<br>
Stephan</p>

---

## Post #11 by @lassoan (2018-10-24 15:53 UTC)

<aside class="quote no-group" data-username="stephan" data-post="10" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>So does this mean that these components, which we thought to be covered by the rigid transform, are somehow duplicated in the deformation?</p>
</blockquote>
</aside>
<p>Exactly. I’ve tested this specifically and found that the large translation and rotation component in the deformable transform is the same as the separate linear transform, so the deformable transform already contains the same rigid transform, but baked into the displacement field. If there is no option in MIM to save the rigid component in pre/post transform or as a separate transform then it should be reported as a bug to MIM developers.</p>
<aside class="quote no-group" data-username="stephan" data-post="10" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>So, to conclude, would you say that the whole issue is because the deformable (grid) transform as exported by MIM is not sufficiently well-defined?</p>
</blockquote>
</aside>
<p>The grid transform is certainly not well conditioned. It may be still usable for some things, for example, transform the moving image that it was created from, but not for much else.</p>
<aside class="quote no-group" data-username="stephan" data-post="10" data-topic="4491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephan/48/2444_2.png" class="avatar"> stephan:</div>
<blockquote>
<p>Or is this just an extreme case within the limits of the DICOM standard which is not yet handled correctly by SlicerRT?</p>
</blockquote>
</aside>
<p>From what I can tell, SlicerRT seem to imports the transform correctly. However, it is odd that we cannot even make it work for transforming one image to the other, so maybe something else is wrong, too, but investigation is difficult because the transform is not well behaved.</p>
<p>The best would be to play a bit more with MIM to see if you can get a better deformable transform out of it. Also, please share the (anonymized) DICOM images as well, to make sure that there is no error in the DICOM-&gt;NRRD conversion.</p>

---

## Post #12 by @stephan (2018-10-24 16:05 UTC)

<p>Thank you for these clarifications.<br>
I will play with MIM then and try to separate the rigid transform from the deformable one.<br>
I’ll keep you posted on the progress.</p>

---
