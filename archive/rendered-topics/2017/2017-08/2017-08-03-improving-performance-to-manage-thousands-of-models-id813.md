# Improving performance to manage thousands of models

**Topic ID**: 813
**Date**: 2017-08-03
**URL**: https://discourse.slicer.org/t/improving-performance-to-manage-thousands-of-models/813

---

## Post #1 by @jcfr (2017-08-03 15:22 UTC)

<p>This topic was created to capture discussion from <a href="https://github.com/Slicer/Slicer/pull/490#issuecomment-223869817">https://github.com/Slicer/Slicer/pull/490#issuecomment-223869817</a></p>
<p>As suggested by <a class="mention" href="/u/lassoan">@lassoan</a>, if someone was time to invest, here are suggestions to address two specific bottlenecks:</p>
<ul>
<li>
<p>(1) <strong>Scene model</strong>: A complete scene model is created in many MRML widgets (e.g., in each MRML node selector and node tree), with lots of observers on many nodes. Having a single scene model that contains all necessary information about all nodes in the scene (and a couple of filters&amp;proxies) used by all widgets would probably make things scalable much better.</p>
</li>
<li>
<p>(2) <strong>Model hierarchies</strong>: Slicer doesn’t store low-level each low-level item (such as a fiducial point, a label, or segment) in a separate node for good reasons - mainly for performance for simplicity for module developers.<br>
For example, at some point fiducials were attempted to be stored as “one node per fiducial” but it was complex to use and it was terribly slow. Changing fiducial management to have multiple markups in a single node solved the problems.<br>
I think model nodes should work the same way: they should be able to manage many meshes internally (probably not just in a flat list but organized using tags or parent/children relationships), we should not require a separate node for each.</p>
</li>
</ul>
<p>By investing a couple of weeks into either 1 and/or 2, you might achieve 10-100x performance improvement in managing large number of models (vs an optimistic 2-10x performance improvement by further general optimization of scene management).</p>

---

## Post #2 by @lassoan (2017-08-03 15:46 UTC)

<p>In the past year <a class="mention" href="/u/cpinter">@cpinter</a> has made huge improvements in subject hierarchy:</p>
<ul>
<li>it is a hierarchy that can handle all kinds of nodes (new node types and actions can be defined via plugins)</li>
<li>stores hierarchy information in a single MRML node (so there is no need for creating a hierarchy node for each model/annotation/etc. data node)</li>
<li>it can show internals of a MRML node in the tree (for example, segments of a are shown in the tree as child items of the segment node)</li>
<li>it can store the full state of the tree (order of elements, open/closed branch, etc. in contrast to model hierarchies, where this never worked correctly)</li>
</ul>
<p>This single hierarchy can replace all other hierarchies (displayable, model, annotations) and it is much faster. I think in we should retire all the old hierarchies in Slicer 5 and switch to this one and then we would only need to implement the shared Qt scene model for a single hierarchy type.</p>

---

## Post #3 by @cpinter (2017-08-03 16:32 UTC)

<blockquote>
<p>model nodes should work the same way: they should be able to manage many meshes internally (probably not just in a flat list but organized using tags or parent/children relationships), we should not require a separate node for each.</p>
</blockquote>
<p>This is exactly what Segmentation nodes do, except that they do more (representations, conversions, etc). I’d really feel it unnecessary to reinvent the wheel and create a third type of node in between Models and Segmentations, providing a subset of the Segmentation node’s features. If there is something this node should know that Segmentations doesn’t, then we should rather add that one feature to Segmentations.</p>
<p>Adding to <a class="mention" href="/u/lassoan">@lassoan</a>’s comment, SH2.0 is also fully compatible with the current model hierarchies, so this would make transition easier from the model hierarchies.</p>

---
