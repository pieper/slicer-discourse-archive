# Automatic vessel endpoints detection

**Topic ID**: 16435
**Date**: 2021-03-08
**URL**: https://discourse.slicer.org/t/automatic-vessel-endpoints-detection/16435

---

## Post #1 by @fuentesdt (2021-03-08 19:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3487">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/compute-centerlines-without-choosing-start-points-subject-independent/3487/2">Compute centerlines without choosing start points (subject independent)?</a></div>
<blockquote>
<p>VMTK extension’s centerline computation module requires only one root point as input and it returns all centerline endpoints as output</p>
</blockquote>
</aside>
<p>i started off with the VMTK package directly before I was aware of this VMTK slicer extension. Endpoints seemed to need to be manually chosen in the interface released with the original vmtk packages. What algorithm are you using to automagically select endpoints? This dramatically improves the usability of VMTK. perhaps also post the slicer extension to the vmtk website ? <a href="http://www.vmtk.org/" rel="noopener nofollow ugc">http://www.vmtk.org/</a></p>

---

## Post #2 by @lassoan (2021-03-08 20:19 UTC)

<aside class="quote no-group" data-username="fuentesdt" data-post="1" data-topic="16435">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fuentesdt/48/9361_2.png" class="avatar"> fuentesdt:</div>
<blockquote>
<p>What algorithm are you using to automagically select endpoints?</p>
</blockquote>
</aside>
<p>It is all VMTK under the hood - see implementation here: <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/3787ea4a300da28ec5f0824f0715f2713b631155/ExtractCenterline/ExtractCenterline.py#L746" class="inline-onebox">SlicerExtension-VMTK/ExtractCenterline/ExtractCenterline.py at 3787ea4a300da28ec5f0824f0715f2713b631155 · vmtk/SlicerExtension-VMTK · GitHub</a></p>
<aside class="quote no-group" data-username="fuentesdt" data-post="1" data-topic="16435">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fuentesdt/48/9361_2.png" class="avatar"> fuentesdt:</div>
<blockquote>
<p>This dramatically improves the usability of VMTK. perhaps also post the slicer extension to the vmtk website ?</p>
</blockquote>
</aside>
<p>VMTK is a library, so to make it useful for end users you almost always need to add some more application-specific code on top of it. This higher-level code that does not have to be as generic as the library classes, may work with some assumptions, and apply heuristics, so it does not really belong to the library, but it could be added to the examples or documentation.</p>
<p>If you have any suggestions for changing VMTK code or documentation or adding more examples then please submit a pull request to the VMTK repository.</p>

---
