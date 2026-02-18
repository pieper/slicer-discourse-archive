# Changing View Group of a Node in View Controllers using Python

**Topic ID**: 3450
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/changing-view-group-of-a-node-in-view-controllers-using-python/3450

---

## Post #1 by @cphillips (2018-07-10 18:04 UTC)

<p>I want to change the view group of a bunch of different nodes in the View Controllers module as part of a Python script.</p>
<p>So far I have only managed to get that vc = slicer.modules.viewcontrollers gives me access to the View Controllers module, but am unsure how to change the view group (which is under View Controllers --&gt; Advanced)</p>

---

## Post #2 by @lassoan (2018-07-10 20:34 UTC)

<p>Most properties you can modify directly in the MRML node. For example, you can set the <code>Red</code> slice view node group to <code>1</code> by this call:</p>
<pre><code>slicer.app.layoutManager().sliceWidget('Red').mrmlSliceNode().SetViewGroup(1)</code></pre>

---
