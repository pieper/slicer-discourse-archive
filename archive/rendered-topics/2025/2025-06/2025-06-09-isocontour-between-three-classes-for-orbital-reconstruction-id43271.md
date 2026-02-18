# Isocontour between three classes for orbital reconstruction

**Topic ID**: 43271
**Date**: 2025-06-09
**URL**: https://discourse.slicer.org/t/isocontour-between-three-classes-for-orbital-reconstruction/43271

---

## Post #1 by @Motrolol (2025-06-09 15:23 UTC)

<p>Dear All,</p>
<p>I have been reading the forums to improve orbital bone reconstructions, and thank you for the active community to coming together and solutions proposed.</p>
<p>I am trying to reconstruct the orbit from CT scans without resampling, or wraping which creates anatomical artefacts. This is my current workflow</p>
<p>Step 1. Class 1 - Bone. Using standard segmentation of bone windows - I note the reported issue of orbital wall defects (medial wall and floor - which are very thin sub 0.4 mm)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c717255a285ef7c6e222cdf856310e43953a7e24.jpeg" data-download-href="/uploads/short-url/speBBn2XPj1CqR3WT4jOYNz1wna.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c717255a285ef7c6e222cdf856310e43953a7e24_2_556x500.jpeg" alt="image" data-base62-sha1="speBBn2XPj1CqR3WT4jOYNz1wna" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c717255a285ef7c6e222cdf856310e43953a7e24_2_556x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c717255a285ef7c6e222cdf856310e43953a7e24.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c717255a285ef7c6e222cdf856310e43953a7e24.jpeg 2x" data-dominant-color="A8A7A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×576 71.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Step 2. Class 2 - Air. What I noted is that if I create another segmentation of the air in the sinuses (segment air, and remove the islands (dead space around the skull)). The result is the air fills the area of defect.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b68e13837ab4571ab3e32a5abad142a1981713e2.jpeg" data-download-href="/uploads/short-url/q2XinRmJ0OVIxNmExnIEyjUv0hs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e13837ab4571ab3e32a5abad142a1981713e2_2_579x500.jpeg" alt="image" data-base62-sha1="q2XinRmJ0OVIxNmExnIEyjUv0hs" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e13837ab4571ab3e32a5abad142a1981713e2_2_579x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e13837ab4571ab3e32a5abad142a1981713e2_2_868x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b68e13837ab4571ab3e32a5abad142a1981713e2_2_1158x1000.jpeg 2x" data-dominant-color="ABA2A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1327×1145 76.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Step 3. Optional Class 3 - Tissue, I can create a tissue window which is the segmentation between Air and bone.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/972589d188a9686f0e1c5b64ef0fac86018de9b5.jpeg" data-download-href="/uploads/short-url/lz6wsFYjhYU90TUpTsgOWxknUEZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972589d188a9686f0e1c5b64ef0fac86018de9b5_2_690x378.jpeg" alt="image" data-base62-sha1="lz6wsFYjhYU90TUpTsgOWxknUEZ" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972589d188a9686f0e1c5b64ef0fac86018de9b5_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972589d188a9686f0e1c5b64ef0fac86018de9b5_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/972589d188a9686f0e1c5b64ef0fac86018de9b5_2_1380x756.jpeg 2x" data-dominant-color="485F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1615×885 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One simple solution is to merge-combine, class 1 and 2. Which is what I am currently doing. However, I note that class 2 stops at boundary of the missing bone, thus creating an step in the 3d model. Which is then filled by class 3 due to partial volume effect (image 3).</p>
<p><strong>Is there a tool using (surface net or alternative) to rebuild the missing bone - i.e. predict the interface between class 1 and class 2, and class 1 and class 3, and class 2 and 3?</strong></p>
<p>So that the step is eliminated or class 1 is filled.</p>
<p>Thanks</p>
<p>(I am a medical doctor by background, so new to coding and understanding 3D slicer)</p>

---

## Post #2 by @pieper (2025-06-09 17:42 UTC)

<p>One suggestion is to supersample your segmentation (it’s easy, just click the Segment Geometry button, then pick your CT and then pick an oversample of 2 (or maybe higher if you have enough memory.  You can also crop first to work on just the eyes in high resolution).  Segmenting at higher resolution is helpful because thin bones may only be a voxel or less thick.  This should also make your whole segmentation look better.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65eeb0e3cd5c8b02c67eb2856ebf2867940dbb21.png" alt="image" data-base62-sha1="exJChWUrepljmBfck1YzdvLzFQJ" width="64" height="50"></p>
<p>The other thing you can do is crop just the eye and then I would think that the sinus air (red) should never touch the soft tissue (green), so grow a margin around the red of whatever thickness you think the bone should be and allow it to overlap the green segment.  Then you can use the logical operators to get the part that is both red and green and then add it to the bone.</p>

---

## Post #3 by @Motrolol (2025-06-11 22:52 UTC)

<p>Thanks Steve,</p>
<p>I have explored various forms of supersampling methods (based on the forum), issue is, I do gain some bone definition but loose the anatomical detail. The margin trick oddly does work well for preserving the natural foramen and filling the defect.</p>
<p>Thanks - but welcome any more suggestions from the community.</p>

---

## Post #4 by @pieper (2025-06-11 22:55 UTC)

<p>Hmm, supersampling the segmentation shouldn’t lose any detail.  If anything it should increase it.  Maybe you can share some images of what you are seeing.</p>

---
