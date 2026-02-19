---
topic_id: 25786
title: "Multiple Partial Volumes Reconstruction"
date: 2022-10-20
url: https://discourse.slicer.org/t/25786
---

# Multiple partial volumes reconstruction

**Topic ID**: 25786
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/multiple-partial-volumes-reconstruction/25786

---

## Post #1 by @Young_Wang (2022-10-20 00:37 UTC)

<p>Hi there, I’m trying to synthesize one full volume from multiple partial volumes(smaller FOV) of the same objects. I wonder if anyone else has explored this topic, and happy to hear any thoughts on what would be the best approach to this.</p>
<p>I appreciate any ideas and advice on things to do or not to do.</p>

---

## Post #2 by @lassoan (2022-10-20 15:07 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for this purpose. It is available in Sandbox extension.</p>

---

## Post #3 by @Young_Wang (2022-10-25 03:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you for your reply. I didn’t find much documentation on this module. I assume we first align the volumes through fiducial registration and then run this module?</p>

---

## Post #4 by @lassoan (2022-10-25 03:40 UTC)

<p>Yes, you need to align the volumes in advance, but the module takes care of resampling and blending. If you find that some information is missing then please add the missing details (click the edit button in the github repository, make your changes, and when Github asks you then choose to create a pull request).</p>

---

## Post #5 by @Young_Wang (2022-10-25 16:14 UTC)

<p>Great. So this is a fancy version of add volume, if I understand it correctly? I will document what I do and submit a pull request once I’m done.</p>

---

## Post #6 by @lassoan (2022-10-25 16:52 UTC)

<p>The module does not add (compute sum of) voxel values of multiple volumes, but it stitches multiple volumes (by resampling, padding, cropping, and blending).</p>

---

## Post #7 by @mikebind (2022-10-26 15:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> is correct, the image volumes you want to stitch together must already be positioned where you want them in space.  Then, you need an ROI which defines the region that the stitched volume should fill.  I typically create this in two steps,</p>
<ul>
<li>go to “CropVolumes” module, select first volume to stitch as input volume, select ‘Create new ROI’ as ROI, and then click “Fit to Volume”.  This creates an ROI which is oriented the same way and with the same dimensions as the input volume. (I don’t crop the volume, just use CropVolumes because of the handy “Fit to Volume” button)</li>
<li>next, extend the ROI as needed to encompass the desired regions of all image volumes to stitch using the interaction handles in the slice views or in 3D</li>
</ul>
<p>This is how I usually do it because I typically am connecting a series of image volumes along one axis (e.g. a series of bed positions) and it works well to mostly extend an ROI in one direction (and often also bring in the sides to reduce the number of air voxels), but you can create a rectilinear ROI any way that works well for your purposes.</p>
<p>Once you have your ROI created, go to the “Stitch Volumes” module, select your image volumes you want to stitch together, select your ROI, select or create the output to put the stitched volume in, and click the “Create Stitched Volume” button.  The selected output will be a new image volume with the same orientation and extent as the ROI, with the same voxel size as the first image volume listed to stitch.</p>

---

## Post #8 by @Young_Wang (2022-10-30 00:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/mikebind">@mikebind</a><br>
I just give stitch volumes a try. Unfortunately, I couldn’t find it when I did a module finder search after I installed the sandbox module.However, I can find the remove CT table module within sandbox.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5839e6397ef2a418b51d83b7a7a2d16b5b1a36b2.jpeg" data-download-href="/uploads/short-url/cAu467IOebzwGhjLr3yHxDQNsf8.jpeg?dl=1" title="Screenshot 2022-10-29 at 21.35.51" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5839e6397ef2a418b51d83b7a7a2d16b5b1a36b2_2_690x448.jpeg" alt="Screenshot 2022-10-29 at 21.35.51" data-base62-sha1="cAu467IOebzwGhjLr3yHxDQNsf8" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5839e6397ef2a418b51d83b7a7a2d16b5b1a36b2_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5839e6397ef2a418b51d83b7a7a2d16b5b1a36b2_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/5839e6397ef2a418b51d83b7a7a2d16b5b1a36b2_2_1380x896.jpeg 2x" data-dominant-color="C5C6DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-10-29 at 21.35.51</span><span class="informations">1920×1247 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Platform; MacBook Pro<br>
OS: macOS Ventura 13.0<br>
Slicer 5.0.2</p>

---

## Post #9 by @lassoan (2022-10-30 02:05 UTC)

<p>Latest extensions are provided only for the latest Slicer Stable Release (currently 5.0.3) and latest Slicer Preview Release.</p>
<p>You need to update from 5.0.2 to 5.0.3 to get this new module in the Sandbox extension.</p>

---

## Post #10 by @Young_Wang (2022-10-30 18:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks. I just updated from 5.0.2 to 5.0.3. And it works. But all the previously installed extensions were gone. I wonder if Slicer3D supports update in a way that could still retain installed extensions</p>

---

## Post #11 by @lassoan (2022-10-30 18:45 UTC)

<aside class="quote no-group" data-username="Young_Wang" data-post="10" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>I wonder if Slicer3D supports update in a way that could still retain installed extensions</p>
</blockquote>
</aside>
<p>Yes, this feature was added to Slicer-5.0.3 (you can bookmark favorite extensions and you can reinstall them by a single click).</p>

---

## Post #12 by @Young_Wang (2022-10-30 18:47 UTC)

<p>Once again, thank you for all the help!</p>

---

## Post #13 by @Young_Wang (2022-10-31 13:53 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/mikebind">@mikebind</a><br>
Apologies for keeping this issue open. I noticed some interesting behaviour of the stitch volume module, which could arise from my incorrect usage. I have some partial volumes of the same anatomy, the human ear, which I want to stitch together to construct a volume with a holistic view.</p>
<p>From left to right, overlaid segmentations merged models and stitched volumes where I was hoping the stitched volumes would look more like the merged models.</p>
<p>I wonder what would cause the inconsistency between the merged model and the stitched volume where you can notice a significant gap in the stitched volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c5f64efcc35bae84630f7e94c08dd25bed4bfe.jpeg" data-download-href="/uploads/short-url/kWpQf218eJSji88awo4l8lCznLo.jpeg?dl=1" title="Demo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c5f64efcc35bae84630f7e94c08dd25bed4bfe_2_690x256.jpeg" alt="Demo" data-base62-sha1="kWpQf218eJSji88awo4l8lCznLo" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c5f64efcc35bae84630f7e94c08dd25bed4bfe_2_690x256.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c5f64efcc35bae84630f7e94c08dd25bed4bfe_2_1035x384.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92c5f64efcc35bae84630f7e94c08dd25bed4bfe_2_1380x512.jpeg 2x" data-dominant-color="4E4A42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Demo</span><span class="informations">1920×715 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @mikebind (2022-10-31 16:07 UTC)

<p>Do the image volumes have transforms applied to them?  If so, these transforms need to be hardened before stitching. If you don’t want the transforms to be hardened on the original image volumes, then you can clone them, apply the transforms, and harden the transforms on the clones.  Many of the basic modules of Slicer ignore soft-applied transforms during processing, so I followed that convention for this module.  When writing modules for my own processing, I usually build in the clone-and-harden step on any inputs which might be transformed because I always want to treat soft-applied transforms as applied, but perhaps other users have other use cases where it makes sense to treat them as not-applied.</p>

---

## Post #15 by @lassoan (2022-10-31 17:05 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="14" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Many of the basic modules of Slicer ignore soft-applied transforms during processing, so I followed that convention for this module.</p>
</blockquote>
</aside>
<p>All Slicer core modules and most well-established modules in extensions take into account the parent transform. The only exception are CLI modules, which consistently “ignore” the parent transform (parent transforms are not sent to the modules); I’m not sure what is the rationale behind that, but this is how it has always been.</p>
<p>Therefore, <strong>ignoring the parent transform is not a convention to follow</strong> but a limitation. A module can still be very useful even if it has some known limitations, just we need to make sure the limitation is documented - or even better, a meaningful message is displayed to the user when the module cannot do something that a user might assume it can do.</p>
<hr>
<p><a class="mention" href="/u/mikebind">@mikebind</a> If you don’t want to spend time now with adding support for transformed input images (e.g., by cloning volumes and hardening transform on them) then it could make sense to show an error message to the user if a parent transform is specified for any of the input volumes (or at least describe this limitation in the module documentation).</p>

---

## Post #16 by @mikebind (2022-10-31 17:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, great, I’ll update the Stitch Volumes module to check for parent transforms and clone, harden, stitch, and clean up.  I should be able to get that done by the end of this week.  Is the right way to do that to fork the current Sandbox, update with my new code, and then create a pull request?</p>

---

## Post #17 by @mikebind (2022-10-31 18:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The only exception are CLI modules, which consistently “ignore” the parent transform</p>
</blockquote>
</aside>
<p>Is there a way to automatically add a warning of some kind to CLI modules if a user tries to select a transformed node as an input?  It is not always obvious to end users that a module they select is a CLI module behind the scenes, and even if they did know, it is not obvious that soft transforms are ignored for these modules.  I’ve unexpectedly run into that multiple times over the years before I learned to check for it (so much so that, as you can see above, I assumed that it might be a Slicer convention for basic modules!).  I understand that adding machinery to automatically force CLI to respect soft transforms (by clone/hardening before passing inputs to CLI) would be a backwards-incompatible change (though I personally don’t see where it would be a problem), simply adding a warning to let users know that soft transforms will be ignored shouldn’t break anyone’s workflow and would be very helpful to most users.</p>

---

## Post #18 by @Young_Wang (2022-10-31 18:55 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a>, thanks for the quick reply. Yes, I aligned those volumes, followed by applying and hardening the corresponding transforms.</p>

---

## Post #19 by @lassoan (2022-10-31 19:22 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="16" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Is the right way to do that to fork the current Sandbox, update with my new code, and then create a pull request?</p>
</blockquote>
</aside>
<p>Yes. Thank you!</p>
<aside class="quote no-group" data-username="mikebind" data-post="17" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Is there a way to automatically add a warning of some kind to CLI modules if a user tries to select a transformed node as an input? It is not always obvious to end users that a module they select is a CLI module behind the scenes, and even if they did know, it is not obvious that soft transforms are ignored for these modules.</p>
</blockquote>
</aside>
<p>I agree, it would make sense. I’ve created a <a href="https://discourse.slicer.org/t/cli-modules-ignore-parent-transform/25987">new topic to discuss this</a>.</p>
<aside class="quote no-group" data-username="Young_Wang" data-post="18" data-topic="25786">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>I aligned those volumes, followed by applying and hardening the corresponding transforms.</p>
</blockquote>
</aside>
<p>The module currently stitches the volumes by splitting them along one of the 3 image axes. In the example above, the images seem to overlap in a very complex pattern. To accommodate such cases, the module could be updated to compute a weighted average of all the input images. The distance map computed from non-empty voxel locations could be used as weighting coefficients.</p>

---

## Post #20 by @Young_Wang (2022-10-31 19:24 UTC)

<p>that makes a lot of senes!</p>

---

## Post #21 by @mikebind (2022-11-08 01:16 UTC)

<p>I updated the StitchVolumes module to respect soft-applied transforms in this PR: <a href="https://github.com/PerkLab/SlicerSandbox/pull/15" class="inline-onebox" rel="noopener nofollow ugc">update to respect soft-applied transforms by mikebind · Pull Request #15 · PerkLab/SlicerSandbox · GitHub</a>.</p>
<p>Blending multiple overlapping image volumes where the overlaps could be in arbitrary directions is much more complicated, and I don’t have time to implement it now, but I will make a note of it and perhaps be able to implement it in the future. I realize that doesn’t solve your current problem, <a class="mention" href="/u/young_wang">@Young_Wang</a>, but perhaps you can take a look at the existing code for the module for inspiration about how to best approach what you would like to accomplish.  Ideas which could make sense to me would be resampling to a common voxel grid, and then perhaps doing some type of thresholded image math to assemble the final image volume.</p>
<p>I don’t clearly understand where your data comes from or what it looks like (particularly in 3D), but if you want to start in this direction and can share some more about your problem I’d be happy to try to offer more specific suggestions.</p>

---

## Post #22 by @Young_Wang (2022-11-30 17:25 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a>, thanks for looking into this for me. I’m working on optical coherence tomography data of the human middle ear. This imaging modality is like ultrasound the image you see is kind of speckly.</p>

---

## Post #23 by @lassoan (2023-01-07 00:22 UTC)

<p>A post was split to a new topic: <a href="/t/merge-3-mri-volumes-with-different-orientations-into-one/27089">Merge 3 MRI volumes with different orientations into one</a></p>

---
