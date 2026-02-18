# Segmenting the nose on multiple scans

**Topic ID**: 1002
**Date**: 2017-09-04
**URL**: https://discourse.slicer.org/t/segmenting-the-nose-on-multiple-scans/1002

---

## Post #1 by @919 (2017-09-04 18:36 UTC)

<p>I have group of 300 scans (mixture of T1 MRI, T2 MRI and head/face CT) that I want to segment the nose and generate a 3D surface model for each nose from all 300 scans. Can someone tell me if this is the correct or most efficient method to go about this process?</p>
<ol>
<li>
<p>Use a CT scan or volumetric T1 MRI of the head (this will be called “head model”) to segment out the nose using the segment editor to generate a baseline anatomical model or atlas for the nose. This will be called “nose model”</p>
</li>
<li>
<p>Use the “Brains” or “Elastix” registration modules to register the “nose model” to each individual scan. The settings will be to non rigidly register the “head model” to each of the 300 scans, with the “head model” being the moving image volume and scan that I want to create the nose model from as the fixed image. That way the size and proportion of the nose from each of the 300 scans is maintained. I was planning on using Rigid + Afiine, then BSpline for the non rigid registration.</p>
</li>
<li>
<p>Once the “head model” has been non rigidly registered to each of the 300 scans I would then use transformation matrix to for each scan to non rigidly align the “nose model” segment as well.</p>
</li>
</ol>
<p>Am I on the right path?<br>
Is using the segment editor the best way to generate an atlas for the nose?<br>
Is Bspline the best method to non rigidly register the nose atlas to the individual scans?</p>
<p>Appreciate any advice or tips</p>

---

## Post #2 by @lassoan (2017-09-05 19:46 UTC)

<p>This plan makes sense overall. I have just one comment: if you only need the skin surface, then automatic segmentation (using seeds automatically generated from approximate linear registration) could be more accurate and more robust than warping a selected patient’s nose to match all the others using non-rigid registration. It would be hard to match subtle details between different patients.</p>

---

## Post #3 by @919 (2017-09-06 01:10 UTC)

<p>How do I go about using the method of automatically generating seeds from linear regiistration? Do you have a link to a tutorial?</p>

---

## Post #4 by @lassoan (2017-09-06 01:37 UTC)

<p>The idea is that you do a crude registration (probably linear is enough) that you just use to align “seed” segments with the image. Probably two segments would be enough: air and tissue. Then you run “Grow from seeds” registration (see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a>).</p>
<p>It is new/research work, so there is no tutorial, but there are examples in the Slicer core, extensions, and Python script repository that you can learn from.</p>

---

## Post #5 by @919 (2017-09-12 14:15 UTC)

<p>I’m not sure I completely follow. So I use my atlas with  “seed” segments for the nose tissue and air, align this using linear registration to the new dataset that needs the nose segmented? Then “grow from seeds” on the new dataset?<br>
How do I restrict the growth to just the nose and not surrounding soft tissue with similar values?</p>

---

## Post #6 by @lassoan (2017-09-12 15:09 UTC)

<aside class="quote no-group" data-username="919" data-post="5" data-topic="1002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/919/48/3818_2.png" class="avatar"> 919:</div>
<blockquote>
<p>So I use my atlas with  “seed” segments for the nose tissue and air, align this using linear registration to the new dataset that needs the nose segmented? Then “grow from seeds” on the new dataset?</p>
</blockquote>
</aside>
<p>Correct.</p>
<aside class="quote no-group" data-username="919" data-post="5" data-topic="1002">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/919/48/3818_2.png" class="avatar"> 919:</div>
<blockquote>
<p>How do I restrict the growth to just the nose and not surrounding soft tissue with similar values?</p>
</blockquote>
</aside>
<p>Grow from seeds can separate air, soft tissues, bones, etc. It won’t be able to separate the nose from the face. I would handle separation of the nose as a next step after segmentation. The nose has no clear boundaries, so difficulty of the task is highly dependent on how you define the boundaries and what errors you can tolerate. We can give further advice if you describe the end goal of your project.</p>

---
