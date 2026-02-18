# 3D print CT of a skull without holes

**Topic ID**: 43095
**Date**: 2025-05-25
**URL**: https://discourse.slicer.org/t/3d-print-ct-of-a-skull-without-holes/43095

---

## Post #1 by @hoteh (2025-05-25 19:46 UTC)

<p>I would like to 3D print a CT of a skull. The problem is, there are a lot of holes and islands in the scan. Is there any automatic tool to help?</p>
<p>Other than manually filling the holes with “Paint” and removing the easy islands with “Islands”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c46db8bc43cbbec13f29a0812a7041e0de4503bf.png" data-download-href="/uploads/short-url/s1GF1zKsA9oBxlkFq7Aw0tToWfB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c46db8bc43cbbec13f29a0812a7041e0de4503bf.png" alt="image" data-base62-sha1="s1GF1zKsA9oBxlkFq7Aw0tToWfB" width="238" height="334"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">238×334 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In this picture you can see the part above the nose (sorry not for using medical terms, I’m not from that field) and in the eye socket. They have a few holes. The actual bone is continuous, so I assume that issue is that the scan is not perfect. I tried playing around with smoothing (fill holes) but I’m looking for something more automatic, if exists. In addition, I want to remove the spine.</p>
<p>Previously, when I wanted to isolate the brain, it was pretty easy with <a href="https://lassoan.github.io/SlicerSegmentationRecipes/CTSkullStripping/" class="inline-onebox" rel="noopener nofollow ugc">Overview | 3D Slicer segmentation recipes</a> . And when I had an MRI, I was able to get a really good image of just the brain using freesurfer’s <code>recon-all</code> (and even with 3D slicer using SlicerSwissSkullStripper, although with some more manual fixing). Does something somewhat automatic exit for a skull CT?</p>

---

## Post #2 by @lassoan (2025-05-25 20:04 UTC)

<p>It seems that this scan is highly anisotropic and voxel spacing is quite large. You would be able to get smoother surface and less holes if you crop and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">resample the source volume before you start segmentation</a>.</p>
<p>You can fill holes using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>.</p>
<p>You can also give the NNInteractive extension a try, which should be able to provide a smooth, no-hole segmentation by a few clicks on the skull.</p>

---

## Post #3 by @hoteh (2025-05-28 12:25 UTC)

<p>Thanks!<br>
I tried SurfaceWrapSolidify and it worked relatively well. I want the skull to be empty, but I can later process that. I will have to wait for NNInteractive until I have access to a strong server.</p>

---

## Post #4 by @hoteh (2025-06-01 15:50 UTC)

<p>Do you happen to know of a solution that does not require such a powerful server?<br>
Cropping the model doesn’t offer a better output than simply running the “threshold” option in segment editor. SurfaceWrapSolidify helped make a single skull piece. But I’m left with a bunch of holes. Manually filling each hole is very tedious, so I would like to avoid that, if possible</p>

---

## Post #5 by @lassoan (2025-06-01 16:43 UTC)

<p>SurfaceWrapSolidify does not leave any holes behind. Please provide screenshots and more explanation of how you use the tool and we may be able to give advice on how to improve your results.</p>
<p>nnInteractive does not require a particularly strong computer, but for the current version you need an NVIDIA GPU.</p>

---

## Post #6 by @hoteh (2025-06-02 19:27 UTC)

<p>Steps to reproduce:</p>
<ol>
<li>Load DICOM</li>
<li>Segment editor, Add</li>
<li>Threshold (min range 350), otherwise <code>Wrap solidify failed: Input segment closed surface representation is empty</code></li>
<li>Islands - <code>keep largest island</code></li>
<li>SurfaceWrapSolidify (called Wrap Solidify in the segment editor)</li>
</ol>
<p>Without <code>Carve holes</code> I get a filled in skull, which I do not want. With <code>Carve holes</code> (10mm) it fills most of the holes, but creates new ones. (less than 10 doesn’t fill in as many holes, more than 10 creates larger holes)<br>
Before:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8bab360140cb815b2c48d7d65fc6ac3e3a9a727.jpeg" data-download-href="/uploads/short-url/xcOMcLXDDjbmV2jMXNLIsULKEx9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8bab360140cb815b2c48d7d65fc6ac3e3a9a727_2_345x189.jpeg" alt="image" data-base62-sha1="xcOMcLXDDjbmV2jMXNLIsULKEx9" width="345" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8bab360140cb815b2c48d7d65fc6ac3e3a9a727_2_345x189.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8bab360140cb815b2c48d7d65fc6ac3e3a9a727_2_517x283.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8bab360140cb815b2c48d7d65fc6ac3e3a9a727_2_690x378.jpeg 2x" data-dominant-color="648763"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×399 72.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97aa1853479abdbf2f3086e9b3f31d304f5f2969.jpeg" data-download-href="/uploads/short-url/lDGwxRFCWqbg5GmmAvu4mngFCuR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aa1853479abdbf2f3086e9b3f31d304f5f2969_2_345x184.jpeg" alt="image" data-base62-sha1="lDGwxRFCWqbg5GmmAvu4mngFCuR" width="345" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aa1853479abdbf2f3086e9b3f31d304f5f2969_2_345x184.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aa1853479abdbf2f3086e9b3f31d304f5f2969_2_517x276.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97aa1853479abdbf2f3086e9b3f31d304f5f2969_2_690x368.jpeg 2x" data-dominant-color="628462"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">765×408 82.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would you recommend that I play with the other options (such as <code>largest cavity</code> or <code>create shell</code>)? I tried them, but I either end up getting a filled in skull, or one with more holes than the <code>Outer surface</code> option.</p>

---

## Post #7 by @lassoan (2025-06-03 05:17 UTC)

<p>These cracks on the image seems to be due to low resolution (large spacing between image slices). If you crop&amp;resample the volume to have isotropic resolution then they should go away.</p>
<p>After thresholding, always apply “Smoothing” effect with “Closing” operation.</p>

---

## Post #8 by @hoteh (2025-06-03 06:22 UTC)

<p>Thank you. The crop&amp;resample with isotropic resolution seemed to work. I kept largest island between threshold and smoothing, and then WrapSolidify filled in virtually all of the remaining holes.</p>
<p>Not all of them,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00980aeafec3323e0fcb9790e88488c843c7abb2.jpeg" data-download-href="/uploads/short-url/5fKuvnt7w7nWj9WVx7FGZ8q5vc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00980aeafec3323e0fcb9790e88488c843c7abb2_2_345x222.jpeg" alt="image" data-base62-sha1="5fKuvnt7w7nWj9WVx7FGZ8q5vc" width="345" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00980aeafec3323e0fcb9790e88488c843c7abb2_2_345x222.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00980aeafec3323e0fcb9790e88488c843c7abb2_2_517x333.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00980aeafec3323e0fcb9790e88488c843c7abb2_2_690x444.jpeg 2x" data-dominant-color="738B7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×453 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But it’s better.</p>
<p>I tried smoothing-&gt;closing (fill holes) with a larger kernel (10), but that makes the top of the skull flat. So I’m not sure if that is the correct method.</p>
<p>Is there another automatic tool to close the small holes, like the 2 in the nasal bone (pictured)?</p>

---
