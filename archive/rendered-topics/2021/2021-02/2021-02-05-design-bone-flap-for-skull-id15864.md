---
topic_id: 15864
title: "Design Bone Flap For Skull"
date: 2021-02-05
url: https://discourse.slicer.org/t/15864
---

# Design bone flap for skull

**Topic ID**: 15864
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/design-bone-flap-for-skull/15864

---

## Post #1 by @slicer365 (2021-02-05 13:02 UTC)

<p>Dear teachers, as you can see, I made a bone flap, but there is a little bulge. Is there any tool to change the curvature of the model so that it will be perfect?Or is there a way to reshape the model like an iron wire, which can be twisted<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10d23eea2950f5eb5bb6fab79adb8428f8d3b27.jpeg" data-download-href="/uploads/short-url/rxOiTZoqvGxGnN2vUWjkrH6Nor5.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c10d23eea2950f5eb5bb6fab79adb8428f8d3b27_2_535x500.jpeg" alt="捕获" data-base62-sha1="rxOiTZoqvGxGnN2vUWjkrH6Nor5" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c10d23eea2950f5eb5bb6fab79adb8428f8d3b27_2_535x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10d23eea2950f5eb5bb6fab79adb8428f8d3b27.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10d23eea2950f5eb5bb6fab79adb8428f8d3b27.jpeg 2x" data-dominant-color="302E35"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">656×612 55.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-05 15:26 UTC)

<p>You can warp your segmentation using Fiducial registration wizard (in SlicerIGT extension). It allows you to define landmark positions on your current segmentation (“From”) and define a target position for each of those landmarks in another list (“To”).</p>
<p>A completely different approach could be to mirror this CT along the left-right axis (or warp a healthy individual’s head CT to this one) using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">image registration</a>. This new volume will have bone at the location where you previously had a hole, so if you choose this new volume as master volume, you can easily fill in the hole using Paint effect (with “Sphere brush” option enabled and “Editable intensity range” in Masking section set to include only bone).</p>

---

## Post #3 by @slicer365 (2021-02-05 15:38 UTC)

<p>A good way. I tested it and the result was perfect. Thank you very much Professor Andras Lasso</p>

---

## Post #4 by @lassoan (2021-02-05 15:38 UTC)

<p>Which method did you end up using successfully?</p>

---

## Post #5 by @slicer365 (2021-02-05 15:46 UTC)

<p>I use the skulls of healthy people to rigidly match, and then segment them. Very good results can be obtained. For some patients with frontal bone defects, the mirror method is not acceptable, but normal skulls can be matched and subtracted.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7afca499c1bceaa75ec0b48c0a41cf8f1acc7a8.jpeg" alt="捕获" data-base62-sha1="uM3hF5sb3AvuAmce3gUkoYgX240" width="536" height="383"></p>

---

## Post #6 by @slicer365 (2021-02-05 15:50 UTC)

<p>One way in Minics is to draw some curves on the edge, and then generate a surface based on the curves</p>

---

## Post #7 by @lassoan (2021-02-05 15:51 UTC)

<p>Thank you. It looks nice! If you ever need to touch up the boundaries between the patient and template, you can use the recently added <a href="https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577">smoothing brush</a> feature.</p>

---

## Post #8 by @slicer365 (2021-02-05 15:54 UTC)

<p>I don’t know why version 4.13 is a beta version, so I still prefer to use the stable version 4.11.I hope to use the stable version  4.13 <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #9 by @lassoan (2021-02-05 16:26 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="6" data-topic="15864" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>One way in Minics is to draw some curves on the edge, and then generate a surface based on the curves</p>
</blockquote>
</aside>
<p>We have that feature implemented in several modules that have not been publicly released yet (the PI prefers to get publication out before making the module available). Probably they will be out in about 6 months. In parallel, <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is working on new markups for curved surface editing. Since we have multiple funded projects to add/improve surface editing capabilities to Slicer, I would expect that we will have multiple new tools available within a year.</p>
<aside class="quote no-group" data-username="slicer365" data-post="8" data-topic="15864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>I don’t know why version 4.13 is a beta version, so I still prefer to use the stable version 4.11.I hope to use the stable version 4.13</p>
</blockquote>
</aside>
<p>We are close to fixing all the regressions that recent developments introduced. Probably the new stable will be out within weeks.</p>

---

## Post #10 by @Pinslahore (2021-11-11 12:46 UTC)

<p>Hi sir</p>
<p>I need your help to reconstruct this defect in skull <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5856c3c7bc8164fca2354e5bf097bf9feec4c92.jpeg" data-download-href="/uploads/short-url/sblUXv26BqNakqQMb6r0kYMvffI.jpeg?dl=1" title="20211111_160116" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5856c3c7bc8164fca2354e5bf097bf9feec4c92_2_690x310.jpeg" alt="20211111_160116" data-base62-sha1="sblUXv26BqNakqQMb6r0kYMvffI" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5856c3c7bc8164fca2354e5bf097bf9feec4c92_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5856c3c7bc8164fca2354e5bf097bf9feec4c92_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c5856c3c7bc8164fca2354e5bf097bf9feec4c92_2_1380x620.jpeg 2x" data-dominant-color="36373D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211111_160116</span><span class="informations">1920×864 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a605f348f955a6d7e1b93491295be1e4f300f3be.jpeg" data-download-href="/uploads/short-url/nGI0x909ddtZtcEMJJMoJju99Se.jpeg?dl=1" title="20211111_160128" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a605f348f955a6d7e1b93491295be1e4f300f3be_2_690x310.jpeg" alt="20211111_160128" data-base62-sha1="nGI0x909ddtZtcEMJJMoJju99Se" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a605f348f955a6d7e1b93491295be1e4f300f3be_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a605f348f955a6d7e1b93491295be1e4f300f3be_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a605f348f955a6d7e1b93491295be1e4f300f3be_2_1380x620.jpeg 2x" data-dominant-color="363B45"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211111_160128</span><span class="informations">1920×864 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
of a patient and need a file for 3d printing . I donot have much knowledge to use this softwear i want you to guide me in this regard i am gratefull .</p>

---

## Post #11 by @lassoan (2021-11-11 13:06 UTC)

<p>The missing area is so large that mirroring the other side of the skull would probably work better - as described above:</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="15864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A completely different approach could be to mirror this CT along the left-right axis (or warp a healthy individual’s head CT to this one) using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">image registration </a>. This new volume will have bone at the location where you previously had a hole, so if you choose this new volume as master volume, you can easily fill in the hole using Paint effect (with “Sphere brush” option enabled and “Editable intensity range” in Masking section set to include only bone).</p>
</blockquote>
</aside>
<p>Is your input a CT image?</p>

---

## Post #12 by @Pinslahore (2021-11-11 14:00 UTC)

<p>Yes i am Using CT SCAN BRAIN WITH 3D RECONST</p>

---

## Post #13 by @lassoan (2021-11-11 14:34 UTC)

<p>If you have a CT image as input then then a workflow like this should work:</p>
<ul>
<li>Import the CT</li>
<li>Create a copy of the CT (by going to right-click and click Clone)</li>
<li>Mirror the CT around the LR axis by applying a transform in Transforms module that has <code>-1</code> in the top-left corner and then click the harden button to harden that transform on the volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0ab4352514fc2263628fc766a1d0e528b68fdc1.png" data-download-href="/uploads/short-url/pcSXLJpV18XcayhiRre9XhEviAp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0ab4352514fc2263628fc766a1d0e528b68fdc1_2_428x500.png" alt="image" data-base62-sha1="pcSXLJpV18XcayhiRre9XhEviAp" width="428" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0ab4352514fc2263628fc766a1d0e528b68fdc1_2_428x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0ab4352514fc2263628fc766a1d0e528b68fdc1_2_642x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0ab4352514fc2263628fc766a1d0e528b68fdc1_2_856x1000.png 2x" data-dominant-color="EEEEED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1029×1202 63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>If the original and mirrored CTs are not aligned then harden the needed, align the original and the cloned image using registration method described on <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">this page</a></li>
<li>Select the original CT as background volume (by clicking on the eye icon in Data module)</li>
<li>Go to Segment Editor module</li>
<li>Create a new segment, segment the skull using Threshold effect</li>
<li>Click “Show 3D” button to see the bone in the 3D view</li>
<li>Select the mirrored CT as master volume</li>
<li>Create a new segment</li>
<li>Use Threshold effect to specify editable intensity range (to limit painting to bone region)</li>
<li>Select Scissors effect</li>
<li>Choose Fill inside mode (so that region that are circled will be filled in the segment)</li>
<li>Choose Masking / Editable area → Outside all segments (to prevent the new segment overwriting the original bone shape)</li>
<li>Trace the boundary of the defect using Scissors in the 3D view</li>
</ul>

---

## Post #14 by @Pinslahore (2021-11-11 16:08 UTC)

<p>Sir can you a vedio tutorial for the above mention procedure</p>

---

## Post #15 by @Pinslahore (2021-11-11 16:09 UTC)

<p>I had tried it but unsuccessfull</p>

---

## Post #16 by @slicer365 (2021-11-11 17:04 UTC)

<p>Are you willing to share the data?</p>

---

## Post #17 by @Pinslahore (2021-11-11 17:55 UTC)

<p>Ist it look like this <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc4a72d7f9649daf2e94304754b9ae82cce8c576.jpeg" data-download-href="/uploads/short-url/zZRPkG5OFAONZquFhVXv4X88BqS.jpeg?dl=1" title="20211111_225220" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc4a72d7f9649daf2e94304754b9ae82cce8c576_2_690x310.jpeg" alt="20211111_225220" data-base62-sha1="zZRPkG5OFAONZquFhVXv4X88BqS" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc4a72d7f9649daf2e94304754b9ae82cce8c576_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc4a72d7f9649daf2e94304754b9ae82cce8c576_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc4a72d7f9649daf2e94304754b9ae82cce8c576_2_1380x620.jpeg 2x" data-dominant-color="7276AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211111_225220</span><span class="informations">1920×864 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And when yo rotate the 3d it look like this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d7508e20a884838e7463d6e8cfd07c90f776f30.jpeg" data-download-href="/uploads/short-url/4cAAIUGWuQ968jnnt4ezAhKlM7C.jpeg?dl=1" title="20211111_225005" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d7508e20a884838e7463d6e8cfd07c90f776f30_2_690x310.jpeg" alt="20211111_225005" data-base62-sha1="4cAAIUGWuQ968jnnt4ezAhKlM7C" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d7508e20a884838e7463d6e8cfd07c90f776f30_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d7508e20a884838e7463d6e8cfd07c90f776f30_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d7508e20a884838e7463d6e8cfd07c90f776f30_2_1380x620.jpeg 2x" data-dominant-color="757599"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20211111_225005</span><span class="informations">1920×864 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can it be corrected</p>
<p>Ho can i get finally saved reconstructed image in stl file .</p>

---

## Post #18 by @lassoan (2021-11-11 18:34 UTC)

<p>It seems that you have missed this step:</p>
<blockquote>
<ul>
<li>Use Threshold effect to specify editable intensity range (to limit painting to bone region)</li>
</ul>
</blockquote>
<p>Select the bone intensity range and then click “Use for masking”. After this, Scissors effect will only fill where there is bone in the master volume.</p>

---

## Post #19 by @johny723 (2024-02-10 12:14 UTC)

<p>What would you do if the defect was bilateral or located in the midline? This procedure would not work. Does 3d Slicer have any method of reconstructing such defects? Thanks!</p>

---

## Post #20 by @lassoan (2024-02-10 17:00 UTC)

<p>You can register a similar patient’s skull with deformable image registration, or create a flap from scratch using Baffle planner module (provided by SlicerHear extension):</p>
<aside class="quote quote-modified" data-post="1" data-topic="16799">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">New module: Baffle planner - for designing surface patches</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    A new <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md">Baffle planner module</a> has been added in <a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer">SlicerHeart extension</a> that can be generally used whenever a smooth surface patch needed that conforms to pre-existing anatomical boundary. By default a “soap-bubble” surface is created for the specified curve but the surface shape can be edited by specifying additional surface points in either slice or 3D views. 
The module can generate an infinitely thin open surface, or a closed surface with specified thickness. 
The module can also generate a flat…
  </blockquote>
</aside>


---
