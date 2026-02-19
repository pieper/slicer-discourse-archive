---
topic_id: 40500
title: "Restoring Sceneviews Breaks Subject Hierarchy And Volume Ren"
date: 2024-12-03
url: https://discourse.slicer.org/t/40500
---

# Restoring sceneviews breaks subject hierarchy and volume rendering presets not changing

**Topic ID**: 40500
**Date**: 2024-12-03
**URL**: https://discourse.slicer.org/t/restoring-sceneviews-breaks-subject-hierarchy-and-volume-rendering-presets-not-changing/40500

---

## Post #1 by @muratmaga (2024-12-03 17:38 UTC)

<p>We have discovered these issues in the preview (from two days ago), and I don’t have time time report it on github as I am about to go into the workshop:</p>
<p>Scene view breaks subkect hierarcy:</p>
<ol>
<li>Load MRHead, set some visuals (shadows, different presets),</li>
<li>Use the scene view to capture the state,</li>
<li>Change the visual properties of MRhead (e.g., turn off shadows)</li>
<li>Save the scene, reset the scene and reload from disk</li>
<li>Right click on the scene view you saved in step 2 and choose restore scene.<br>
Find the all items in the subject hierarch is now collapsed and cannot be expanded. Reproduces in mac and linux with R33134</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7e7871134de70c2ea1fe04d37aed0d977f1972d.png" data-download-href="/uploads/short-url/x5wl9TaMpwpiinAPbDQ8sZpX3xb.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7e7871134de70c2ea1fe04d37aed0d977f1972d.png" alt="image" data-base62-sha1="x5wl9TaMpwpiinAPbDQ8sZpX3xb" width="425" height="112"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">425×112 7.53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unrelated bug. Choosing a different preset in the volume rendering changes the visual, but the displayed Volume Property remains the whatever the initial setting was (screenshot is after choosing CT-Bone preset)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d48a6fce81fcbae359acf7ef8b535bf4aaea07bd.jpeg" data-download-href="/uploads/short-url/ukdP1Y7sy5wUp4WkTRvfYoQyBXL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d48a6fce81fcbae359acf7ef8b535bf4aaea07bd_2_589x500.jpeg" alt="image" data-base62-sha1="ukdP1Y7sy5wUp4WkTRvfYoQyBXL" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d48a6fce81fcbae359acf7ef8b535bf4aaea07bd_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d48a6fce81fcbae359acf7ef8b535bf4aaea07bd_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d48a6fce81fcbae359acf7ef8b535bf4aaea07bd.jpeg 2x" data-dominant-color="A68D99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×917 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @lassoan (2024-12-03 18:09 UTC)

<p>Scene views have never worked reliably and there have been no chance to fix all the issues, partly because its behavior (what states of what nodes need to be saved and restored) has not been clearly defined. Right now I would not recommend to use scene views.</p>
<p>The good news is that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is currently working on <a href="https://github.com/Slicer/Slicer/issues/4841">revamping scene views to use sequences</a>, so it will be robust and it will be very clearly defined what is included in scene views. The full implementation may take months, but there may be something to test by the project week in January.</p>

---
