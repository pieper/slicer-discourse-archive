---
topic_id: 4916
title: "Gradient Artifact With Mask Volume Effect From Editor Extra"
date: 2018-11-30
url: https://discourse.slicer.org/t/4916
---

# Gradient artifact with Mask Volume effect from Editor Extra Effects?

**Topic ID**: 4916
**Date**: 2018-11-30
**URL**: https://discourse.slicer.org/t/gradient-artifact-with-mask-volume-effect-from-editor-extra-effects/4916

---

## Post #1 by @hherhold (2018-11-30 00:26 UTC)

<p>This is on MacOS, nightly build from October 22. A little old, but not ancient.</p>
<p>I’m seeing a strange “gradient” effect when using Mask Volume in Editor Extra Effects. Rather than a sharp cutoff from the inside to the outside of the masked volume, there’s this odd gradient from the normal values in the “kept” volume to the zero values outside. I’ve attached a screenshot - this gradient was NOT present in my original data. Any ideas what’s causing this? It’s kind of annoying because I use a threshold effect after masking and it causes an “envelope” to appear around my entire volume, caused by this gradient artifact.</p>
<p>Thanks in advance for any ideas! I’ll check to see if this also happens in 4.8…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b731e595a17ca5b42acc792ec0b62b72530f2595.png" alt="21%20PM" data-base62-sha1="q8ChokJUS4lCBeTb7YjFoFzNspf" width="586" height="389"></p>

---

## Post #2 by @lassoan (2018-11-30 01:46 UTC)

<p>By default, linear image interpolation is used in slice viewers: each displayed pixel is computed as a weighted average of voxels surrounding that 3D position. So, unless the slice is positioned exactly in the center of a voxel, you always see blending of two neighbor slices. Since masking creates huge intensity change at the boundary, the effect of this interpolation becomes more visible. So, what you see is normal and should not be a problem.</p>
<p>You can disable slice interpolation or position slice viewer in the center of the voxel (for example, by holding down shift button while moving the mouse in an orthogonal view).</p>

---

## Post #3 by @hherhold (2018-11-30 02:06 UTC)

<p>Hi Andras, thanks for the reply.</p>
<p>I’m not sure that slice interpolation is the issue - I turn it off and I still see this gradient. Let me outline what I did from the beginning and maybe that will help:</p>
<ol>
<li>Load in a big microCT volume. Specimen is fossil insect in amber.</li>
<li>Outline specimen area in slices to prep for “Fill between slices”.</li>
<li>Use fill between slices to create segment containing only insect.</li>
<li>Use Mask Volume to mask off anything not containing insect.</li>
<li>Use threshold to “select” insect.</li>
</ol>
<p>This is where I see these “gradient” areas at the border created by Fill Between Slices.</p>
<p>What do you think?</p>
<p>Thanks in advance for your time!!!</p>
<p>-Hollister</p>

---

## Post #4 by @lassoan (2018-11-30 02:14 UTC)

<p>Can you share the scene (or reproduce it on a sample data set and share that scene)?</p>

---

## Post #5 by @hherhold (2018-12-05 15:34 UTC)

<p>Ugh. I had a test scene that I <em>thought</em> reproduced what I was seeing, and I was writing up the procedure and now I can’t reproduce it.</p>
<p>I do have one question - does “Mask Volume” in Segment Editor Extra Effects operate differently depending on whether or not interpolation is enabled for the master volume in question? Or is interpolation just for <em>viewing</em> in slice viewers?</p>
<p>Thank you, and sorry for the confusion!</p>
<p>-Hollister</p>

---

## Post #6 by @muratmaga (2018-12-05 16:35 UTC)

<p>My understanding is that it is onle for viewing in slice viewers:</p>
<aside class="quote" data-post="2" data-topic="1604">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/what-is-the-underlying-function-of-interpolate-option-of-volumes-module/1604/2">What is the underlying function of 'interpolate' option of Volumes module</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    That option controls how the image is sampled when scaled for display: nearest neighbor / linear (see <a href="https://en.wikipedia.org/wiki/Image_scaling">https://en.wikipedia.org/wiki/Image_scaling</a> for details). There is nothing to save - what you see is still the original volume.
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="5" data-topic="2808">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-interpolation/2808/5">Slice Interpolation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You always see the real image. The coordinates (both the anatomical/patient coordinates and voxel coordinates) are also all real and correct. You may turn off interpolation (Volumes module / Display / Interpolate checkbox) if you want to make sure that at a certain position in the image you see the contribution of exactly one pixel of the image slices. 
If you could tell what your application (anatomy, procedure, imaging modality, etc) and your concerns are then we could give more specific answ…
  </blockquote>
</aside>


---

## Post #7 by @hherhold (2019-02-18 14:36 UTC)

<p>OK, after many weeks, I finally got back to this and verified that it was indeed “problem between chair and keyboard”, as they say. I was switching between viewing several volumes and lost track of which ones had interpolation turned on.</p>
<p>Sorry for any confusion!</p>
<p>-Hollister</p>

---
