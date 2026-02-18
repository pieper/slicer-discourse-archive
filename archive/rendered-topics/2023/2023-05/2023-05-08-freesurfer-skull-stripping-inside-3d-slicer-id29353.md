# FreeSurfer skull stripping inside 3D Slicer

**Topic ID**: 29353
**Date**: 2023-05-08
**URL**: https://discourse.slicer.org/t/freesurfer-skull-stripping-inside-3d-slicer/29353

---

## Post #1 by @benzwick (2023-05-08 13:09 UTC)

<p>Does anyone know if there is a module to perform skull stripping using FreeSurfer (Watershed and SynthStrip methods) within 3D Slicer?</p>
<p>If not, are there any existing extensions where such a module could be added (e.g. <a href="https://github.com/PerkLab/SlicerFreeSurfer" rel="noopener nofollow ugc">SlicerFreeSurfer</a>), or should I create a new extension for this purpose? One consideration is that it would depend on FreeSurfer, which is quite a large software and is not a dependency of any existing FreeSurfer 3D Slicer extensions/modules that I have found so far.</p>

---

## Post #2 by @pieper (2023-05-09 13:21 UTC)

<p>It’s not wrapped as a Slicer extension, but it’s pretty easy to install and use <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a> in an external python environment.  The results can be used for SkullStripping (and more) and it’s very robust.</p>
<p>If someone feels like taking it on, adding a SlicerSynthSeg extension would be worth doing, although as we’ve seen with TotalSegmentator there is likely to be a lot of installation support as people try to use it on various systems.</p>

---

## Post #3 by @benzwick (2023-05-10 02:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="29353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It’s not wrapped as a Slicer extension, but it’s pretty easy to install and use <a href="https://github.com/BBillot/SynthSeg" rel="noopener nofollow ugc">SynthSeg</a> in an external python environment. The results can be used for SkullStripping (and more) and it’s very robust.</p>
</blockquote>
</aside>
<p>One potential limitation of SynthSeg is that “SynthSeg always give results at 1mm isotropic resolution, regardless of the input.”</p>
<p>I’ve started developing an extension with Python CLI modules that uses a user’s existing FreeSurfer installation to run the FreeSurfer commands while handling the conversion between Slicer and FreeSurfer image types. This would allow any FreeSurfer commands to be added as modules in Slicer (including SynthSeg, which is now included in FreeSurfer as well).</p>

---

## Post #4 by @lassoan (2023-05-10 02:55 UTC)

<p>There several skull strippers in Slicer already: SkullStripper, SwissSkullStripper, HDBrainExtraction. If you have a GPU then I would recommend HDBrainExtraction, computation then takes about 20 seconds. It does not resample to 1mm isotropic resolution and it can provide the brain mask, too.</p>

---

## Post #5 by @benzwick (2023-05-12 05:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="29353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you have a GPU then I would recommend HDBrainExtraction, computation then takes about 20 seconds.</p>
</blockquote>
</aside>
<p>I tried using HDBrainExtraction but ran out of GPU memory. Using the CPU it took about 12 min. SynthStrip takes about 12 sec using the CPU.</p>

---

## Post #6 by @lassoan (2023-05-13 01:40 UTC)

<p>What are the dimensions of the brain MRI image?<br>
How much GPU RAM do you have?</p>

---

## Post #7 by @benzwick (2023-05-15 04:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="29353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What are the dimensions of the brain MRI image?</p>
</blockquote>
</aside>
<p>256 x 256 x 60</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="29353">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How much GPU RAM do you have?</p>
</blockquote>
</aside>
<p>I’m using a NVIDIA Quadro P1000 that has 4 GB GPU RAM.</p>

---

## Post #8 by @lassoan (2023-05-15 10:54 UTC)

<p>4GB is only suitable for visualization but insufficient for running most neural networks. If you want to use your GPU for data processing then get one with at least 16GB memory, but if you want to use it for a few years then it safer to buy one with 24GB.</p>

---
