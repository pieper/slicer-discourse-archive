# How to make RTBeamNode or VolumeNode sensitive to patient support rotation from UI?

**Topic ID**: 10410
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/how-to-make-rtbeamnode-or-volumenode-sensitive-to-patient-support-rotation-from-ui/10410

---

## Post #1 by @Mik (2020-02-24 05:47 UTC)

<p>When i change patient support rotation angle in “Beams” module or “Room’s Eye View” it changes the position of patient support but CT volume node is still on the same place. How to make a volume node or rt beam sensitive to that rotation from UI not using “Transform” module?</p>
<p>That is required for correct MLC opening calculation and RTImage calculation.</p>
<p>Screen shot example: Patient Support is rotated, but CT series data are still on the same place.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d07847343e2f4ba4e96c7b3519b7ba124b440d2a.png" data-download-href="/uploads/short-url/tKd0wZi4IbnpoyXfgjFAccoIwVY.png?dl=1" title="ScreenshotExample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d07847343e2f4ba4e96c7b3519b7ba124b440d2a_2_690x461.png" alt="ScreenshotExample" data-base62-sha1="tKd0wZi4IbnpoyXfgjFAccoIwVY" width="690" height="461" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d07847343e2f4ba4e96c7b3519b7ba124b440d2a_2_690x461.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d07847343e2f4ba4e96c7b3519b7ba124b440d2a_2_1035x691.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d07847343e2f4ba4e96c7b3519b7ba124b440d2a_2_1380x922.png 2x" data-dominant-color="484243"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotExample</span><span class="informations">4200×2811 514 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2020-02-24 09:18 UTC)

<p>This is a known issue that patient support rotation does not affect moving the patient as it should. This is one of the many things that would need to be improved around beams and plans in SlicerRT. Treatment planning features are still quite rudimentary due to the lack of funds to continue development. We are in the process of writing a grant just for this, but that is a lengthy process, so if you prefer not to wait, then you may consider contributing.</p>

---

## Post #3 by @Mik (2020-02-24 09:47 UTC)

<p>There is no rush, but that’s a must have feature in my case. I’m ready to help in this issue.</p>
<p>I have tried myself but i haven’t found how to get a proper transformation node between Patient Support or Table Top to RAS in IECTransformLogic.</p>

---

## Post #4 by @cpinter (2020-02-24 13:56 UTC)

<p>You can get the transformation using</p>
<p><code>vtkSlicerIECTransformLogic::GetTransformBetween(vtkSlicerIECTransformLogic::PatientSupport, vtkSlicerIECTransformLogic::RAS, outputTransform)</code></p>
<p>It should also be possible to define the patient for the plan, and have the whole patient (CT, segmentation, fiducials, all of that) transformed accordingly when the patient support is moved. However, that is a larger task to do it properly, in a future-proof way.</p>

---

## Post #5 by @Mik (2020-03-01 17:11 UTC)

<p>I managed to solve this problem partially, at least now with rotation of patient support the patient CT and segmentation rotated as well.</p>
<p>Another issue is a camera control to fix slice views on table top position.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f45733631bd8f859c7eb3ad65eac09028cacd599.png" data-download-href="/uploads/short-url/yRxkqzGuzEzpMRDmE4iyNlOILuV.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f45733631bd8f859c7eb3ad65eac09028cacd599_2_690x465.png" alt="Screenshot" data-base62-sha1="yRxkqzGuzEzpMRDmE4iyNlOILuV" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f45733631bd8f859c7eb3ad65eac09028cacd599_2_690x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f45733631bd8f859c7eb3ad65eac09028cacd599_2_1035x697.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f45733631bd8f859c7eb3ad65eac09028cacd599_2_1380x930.png 2x" data-dominant-color="3A393F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1389×937 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2020-03-01 19:19 UTC)

<p>You bcan use Volume Reslice Driver module (in SlicerIGT extension) to move slice views by transforms. You can combine transforms and as the transforms change, the slice views are updated in real-time.</p>

---

## Post #7 by @Mik (2020-03-02 08:02 UTC)

<p>Thank you for suggestion of using IGT extension.</p>
<p>As another approach it is possible to create a reverse transforms from IEC, e.g. everything (table support, gantry, etc) rotates and translates around still CT data?</p>

---

## Post #8 by @cpinter (2020-03-02 09:56 UTC)

<aside class="quote no-group" data-username="Mik" data-post="7" data-topic="10410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>As another approach it is possible to create a reverse transforms from IEC, e.g. everything (table support, gantry, etc) rotates and translates around still CT data?</p>
</blockquote>
</aside>
<p>Yes, and actually this is what I imagine to be a proper fix for considering the patient support transform. What this would imply is that the reference in terms of IEC will be the patient support and not the world (FixedReference / RAS). However, this would take time to implement in a proper and maintainable manner, which requires funding (see my first comment).</p>

---

## Post #9 by @Mik (2020-03-02 10:58 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="8" data-topic="10410">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>However, this would take time to implement in a proper and maintainable manner</p>
</blockquote>
</aside>
<p>I understood that, and that is good to know that reverse transforms is a proper way.</p>

---

## Post #10 by @lassoan (2020-03-03 02:53 UTC)

<p>I don’t know if it helps, but you can compute inverse transform (and compute relative transform between any two coordinate systems) using “Transform processor” module in SlicerIGT extension. The computed transform is updated in real-time when any of the input transforms are changed.</p>

---

## Post #11 by @Mik (2020-03-08 07:20 UTC)

<p>I have made a dynamic IEC hierarchy matrix transformation calculation, and i can make a PR if this is interesting.</p>
<p>Transformation for Collimator to Patient looks like:</p>
<p>Collimator → Gantry → fixedReference → patientSupport → tableTopEccentric → tableTop → Patient (RAS)</p>
<ol>
<li>Works with “Beams” and “External Beam Plan” modules</li>
<li>Doesn’t break compatibility with “Room’s Eye View” module</li>
</ol>
<p>Gantry and patient support angles:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05947e938543f2a3ef9688915923bb7140830a14.png" alt="image" data-base62-sha1="NmxbnLWPQ2bMLDtlPu9frXmBne" width="518" height="339"></p>
<p>RTBeamNode transformation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351d9079187bc92ef49f6367a9ed367fae9ae0b9.png" data-download-href="/uploads/short-url/7zSE83pBe4eel3vxuenza5sLUKd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351d9079187bc92ef49f6367a9ed367fae9ae0b9_2_275x500.png" alt="image" data-base62-sha1="7zSE83pBe4eel3vxuenza5sLUKd" width="275" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351d9079187bc92ef49f6367a9ed367fae9ae0b9_2_275x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351d9079187bc92ef49f6367a9ed367fae9ae0b9_2_412x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351d9079187bc92ef49f6367a9ed367fae9ae0b9.png 2x" data-dominant-color="F2F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">425×770 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a4552f04014f722bc694e875f885ae9518d9ff7.jpeg" data-download-href="/uploads/short-url/8judAHpOLFGBEexpLCpWvpKiQWH.jpeg?dl=1" title="Screenshot4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a4552f04014f722bc694e875f885ae9518d9ff7_2_690x416.jpeg" alt="Screenshot4" data-base62-sha1="8judAHpOLFGBEexpLCpWvpKiQWH" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a4552f04014f722bc694e875f885ae9518d9ff7_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a4552f04014f722bc694e875f885ae9518d9ff7_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a4552f04014f722bc694e875f885ae9518d9ff7_2_1380x832.jpeg 2x" data-dominant-color="42514F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot4</span><span class="informations">1554×937 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2020-03-09 02:03 UTC)

<p>Looks very nice. Please submit a pull request so the implementation can be reviewed and integrated.</p>

---

## Post #13 by @Mik (2020-03-09 17:29 UTC)

<p>Pull request that partially fix that issue: <a href="https://github.com/SlicerRt/SlicerRT/pull/133" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/pull/133</a></p>

---
