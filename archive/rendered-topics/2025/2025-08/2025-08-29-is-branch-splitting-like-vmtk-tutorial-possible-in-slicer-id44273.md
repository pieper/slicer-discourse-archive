# Is branch splitting like VMTK tutorial possible in Slicer?

**Topic ID**: 44273
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/is-branch-splitting-like-vmtk-tutorial-possible-in-slicer/44273

---

## Post #1 by @mikebind (2025-08-29 20:48 UTC)

<p>I am interested in carrying out branch splitting exactly as shown in this tutorial:  <a href="http://www.vmtk.org/tutorials/BranchSplitting.html" rel="noopener nofollow ugc">Branch Splitting | vmtk - the Vascular Modelling Toolkit</a></p>
<p>I am familiar with using vmtk for single centerlines, and am now exploring it for branching trees. I see that I can get individual branches, bifurcations, and centerlines to each endpoint using the Centerline Disassembly module after the ExtractCenterline module. However, the tutorial linked to above, goes one step further and uses these centerline piece groupings to divide up the original surface into branch territories in a very nice way.  What is the best way to achieve this in Slicer?</p>

---

## Post #2 by @chir.set (2025-08-29 21:07 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="44273">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>divide up the original surface into branch territories</p>
</blockquote>
</aside>
<p>Have you checked the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/BranchClipper.md" rel="noopener nofollow ugc">Branch clipper</a> module?</p>

---

## Post #3 by @mikebind (2025-08-29 22:21 UTC)

<p>Thanks, I had skipped over that one because I misinterpreted the module name to mean it was about clipping the ends of vessels (e.g. for flow extensions) rather than splitting a surface into branch segments.  Thanks for the quick answer, this is exactly what I was looking for.</p>

---
