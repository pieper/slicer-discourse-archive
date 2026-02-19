---
topic_id: 30314
title: "Multiple Tractography File Selection For Visualization And 2"
date: 2023-06-29
url: https://discourse.slicer.org/t/30314
---

# Multiple tractography file selection for visualization and 2D vs 3D visualization toggles

**Topic ID**: 30314
**Date**: 2023-06-29
**URL**: https://discourse.slicer.org/t/multiple-tractography-file-selection-for-visualization-and-2d-vs-3d-visualization-toggles/30314

---

## Post #1 by @jhlegarreta (2023-06-29 23:33 UTC)

<p>Hi,<br>
when having multiple bundle data loaded onto Slicer, is there a way to select multiple files at the same time and to change the visualization type (under <code>Diffusion/Tractography/Tractography Display</code>) to <code>Tubes</code> instead of <code>Slices</code>?</p>
<p>Slightly related, when trying to visualize the 2D interesection of the streamlines, clicking on the <code>Tubes Slice</code> toggle has no effect unless I also select the <code>Tubes</code> visualization mode for the 3D scene. Is this expected? Can this be improved (i.e. not requiring the 3D visualization to be set to <code>Tubes</code> manually, or by making the 3D visualization automatically switch to <code>Tubes</code>)?</p>
<p>I am using Slicer 5.2.2.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-06-30 11:27 UTC)

<p>Would you like to always use Tubes mode by default?</p>

---

## Post #3 by @jhlegarreta (2023-06-30 12:43 UTC)

<blockquote>
<p>Would you like to always use Tubes mode by default?</p>
</blockquote>
<p>Not necessarily.</p>

---

## Post #4 by @pieper (2023-06-30 15:33 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="30314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Slightly related, when trying to visualize the 2D interesection of the streamlines, clicking on the <code>Tubes Slice</code> toggle has no effect unless I also select the <code>Tubes</code> visualization mode for the 3D scene. Is this expected? Can this be improved (i.e. not requiring the 3D visualization to be set to <code>Tubes</code> manually, or by making the 3D visualization automatically switch to <code>Tubes</code>)?</p>
</blockquote>
</aside>
<p>yes - this is expected.</p>
<p>Most of the interaction modes in the Tractograpy Display module were designed before we started working with hundreds of bundles, so they are more suited to working with a few manually created tracts.  If you want to control lots of tracts in bulk the best way is to write little custom python scripts that set up things in the way you want.</p>

---
