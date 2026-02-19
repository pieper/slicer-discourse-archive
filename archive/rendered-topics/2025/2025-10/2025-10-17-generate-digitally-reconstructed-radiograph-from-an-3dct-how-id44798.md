---
topic_id: 44798
title: "Generate Digitally Reconstructed Radiograph From An 3Dct How"
date: 2025-10-17
url: https://discourse.slicer.org/t/44798
---

# Generate digitally reconstructed radiograph from an 3DCT. How to choose different controllpoints of an arc beam?

**Topic ID**: 44798
**Date**: 2025-10-17
**URL**: https://discourse.slicer.org/t/generate-digitally-reconstructed-radiograph-from-an-3dct-how-to-choose-different-controllpoints-of-an-arc-beam/44798

---

## Post #1 by @ruju (2025-10-17 11:59 UTC)

<p>Hello,</p>
<p>I would like to create some DRRs from a 3DCT. I have one arc beam with some different controllpoints. If I want to generate a DRR with DDR Image Computation of this beam, it only generates a DRR for the first beam position. For me it is not possible to choose one of the other beam-controllpoints. Is there any possibility to select the other controllpoints?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2025-10-17 18:55 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> do you have any insights?</p>

---

## Post #3 by @Mik (2025-10-18 18:53 UTC)

<p>Arc beam sequence doesn’t have correct support, because i can’t find a test dataset to test it. If you need to calculate DRR images for a particular set of control points (beam angles, isocenter positions), its easier to execute a small script in python console.</p>
<p>See <a href="https://github.com/SlicerRt/SlicerRT/blob/master/Docs/user_guide/modules/drr.md" rel="noopener nofollow ugc">Example 3 (CT Volume only, beam is set manually, isocenter is set manually)</a></p>
<p>If you can share DICOM files with defined arc beam control points in RTPLAN, then support for arc beams can be done quite fast.</p>

---

## Post #4 by @cpinter (2025-10-19 19:04 UTC)

<p>Thanks for bringing this up! <a class="mention" href="/u/ruju">@ruju</a> a set of anonymized VMAT plan data would be a lot of help for us! <a class="mention" href="/u/mik">@Mik</a> I’ll ask a few new partners in case they can help us.</p>

---

## Post #5 by @ruju (2025-10-22 10:00 UTC)

<p>Thank you!</p>
<p>Here is one data set of a phantom with CT and an arc beam in RTplan. <a href="https://www.swisstransfer.com/d/09f869a6-6c16-4970-ab2c-bcbf3d303d40" class="inline-onebox" rel="noopener nofollow ugc">SwissTransfer - Send large files securely and free of charge</a></p>

---

## Post #6 by @Mik (2025-10-22 11:29 UTC)

<p>For the dataset above the beam parameters are loaded as a sequence, you can choose <code>Sequences→Sequences</code>in modules menu. There you can press <code>Play/Pause</code>button, and see the behavior (movement) of the beam. Beam parameters are available for each control point via <code>Beams</code> module. DRR image will be calculated for corresponding beam orientation (control point).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3335dfd479fef7d13eb9e185a56d91352236c5ba.png" data-download-href="/uploads/short-url/7j1M7OcmeiNEKAEwt4fpssV7d0K.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3335dfd479fef7d13eb9e185a56d91352236c5ba_2_480x500.png" alt="image" data-base62-sha1="7j1M7OcmeiNEKAEwt4fpssV7d0K" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3335dfd479fef7d13eb9e185a56d91352236c5ba_2_480x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3335dfd479fef7d13eb9e185a56d91352236c5ba.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3335dfd479fef7d13eb9e185a56d91352236c5ba.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">545×567 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Beam parameters for the last control point:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca8dc5d02520b095c27b7ab661d2c1e31abf0d6c.png" data-download-href="/uploads/short-url/sTSc867cEoXZk5ja6b7HLzQ0FM8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca8dc5d02520b095c27b7ab661d2c1e31abf0d6c_2_690x334.png" alt="image" data-base62-sha1="sTSc867cEoXZk5ja6b7HLzQ0FM8" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca8dc5d02520b095c27b7ab661d2c1e31abf0d6c_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca8dc5d02520b095c27b7ab661d2c1e31abf0d6c_2_1035x501.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca8dc5d02520b095c27b7ab661d2c1e31abf0d6c.png 2x" data-dominant-color="909085"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1235×599 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Mik (2025-10-22 13:07 UTC)

<p>Minor correction, in your data SourceAxisDistance is 1000 mm, but <code>Beams</code> module says that the  source distance is 2000 mm (which is wrong), you can set correct parameter in GUI interface, and get correct beam representation and DRR calculation.</p>

---
