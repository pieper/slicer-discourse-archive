---
topic_id: 46877
title: "How To Show A Transform In Only One View"
date: 2026-04-30
url: https://discourse.slicer.org/t/46877
---

# How to show a transform in only one view

**Topic ID**: 46877
**Date**: 2026-04-30
**URL**: https://discourse.slicer.org/t/how-to-show-a-transform-in-only-one-view/46877

---

## Post #1 by @koeglfryderyk (2026-04-30 11:35 UTC)

<p>I have a Displacement field Transform and I want to visualise it only in <strong>one</strong> 2D view. I couldn’t find it in the UI and I couldn’t figure out how to do it in python.</p>
<p>Is there a way to do that?</p>

---

## Post #2 by @ebrahim (2026-04-30 14:22 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post contains AI-generated content.</p>
</blockquote>
<p>In the <strong>Transforms</strong> module, first turn on “Visible in 2D view” (under <em>Display</em> → <em>Visualization</em>) so a transform display node exists and slice visualization is enabled. Then in the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">transformNode = getNode("YourTransform")             # or pick by ID
displayNode = transformNode.GetDisplayNode()         # created when 2D vis is toggled on

# Restrict to a single slice view (e.g., Red):
displayNode.SetViewNodeIDs(["vtkMRMLSliceNodeRed"])
</code></pre>
<p>To go back to “all views”, clear the list:</p>
<pre data-code-wrap="python"><code class="lang-python">displayNode.RemoveAllViewNodeIDs()
</code></pre>
<p>Notes:</p>
<ul>
<li>The IDs for the default slice views are <code>vtkMRMLSliceNodeRed</code>, <code>vtkMRMLSliceNodeYellow</code>, <code>vtkMRMLSliceNodeGreen</code>. For a custom view, grab <code>sliceNode.GetID()</code>.</li>
<li>If <code>GetDisplayNode()</code> returns <code>None</code>, call <code>transformNode.CreateDefaultDisplayNodes()</code> first, or just toggle the 2D-visible checkbox once in the Transforms module.</li>
<li>This restriction also applies to the visualization region/ROI — only the listed view will render the grid/glyph/contour.</li>
</ul>

---

## Post #3 by @koeglfryderyk (2026-04-30 14:39 UTC)

<p>This doesn’t work for me. In which Slicer version has this worked for you? I’m in the stable release 5.10.0</p>
<ol>
<li>there is no “Visible in 2D view”, I only see “Visibility:”, “Visibility in slice view:” and “Visibility in 3D view:” - I have all of them checked</li>
<li>no matter what ViewNodeIDs I set, it always remains visible in all views</li>
</ol>

---

## Post #4 by @ebrahim (2026-04-30 15:24 UTC)

<blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/robot.png?v=15" title=":robot:" class="emoji" alt=":robot:" loading="lazy" width="20" height="20"> This post was written with AI assistance.</p>
</blockquote>
<p>I am also in 5.10 but had not tried the snippet.</p>
<p>(“Visibility in slice view” is the correct label, thanks)</p>
<p>When I tried it, indeed the grid/glyph/contour remains visible in all slice views.</p>
<p>It took some trickery, here is the ai generated snippet that finally worked:</p>
<pre data-code-wrap="py"><code class="lang-py">transformNode = getNode("YourTransform")
old = transformNode.GetDisplayNode()
if old:
    slicer.mrmlScene.RemoveNode(old)

# Create and configure the display node BEFORE attaching it to the transform.
# Until it's linked, no displayable manager will process it, so we can set
# the view filter and visibility flags safely.
dn = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformDisplayNode")
dn.SetViewNodeIDs(["vtkMRMLSliceNodeRed"])
dn.SetVisibility(True)
dn.SetVisibility2D(True)
dn.SetVisibility3D(False)

# Link last — this is the moment UseDisplayNode() runs in each slice manager,
# and only the Red one will pass the IsDisplayableInView() check.
transformNode.SetAndObserveDisplayNodeID(dn.GetID())
</code></pre>
<p>The problem was that the transform 2D displayable manager is not noticing changes to the view filter. We could add to <a href="https://github.com/Slicer/Slicer/blob/a087af0c6cb44789dcd6df06cf6291d1ecd561a2/Modules/Loadable/Transforms/MRMLDM/vtkMRMLTransformsDisplayableManager2D.cxx#L149">vtkMRMLTransformsDisplayableManager2D.cxx#L149</a> a <code>&amp;&amp; displayNode-&gt;IsDisplayableInView(this-&gt;SliceNode-&gt;GetID())</code></p>

---

## Post #5 by @mikebind (2026-04-30 20:39 UTC)

<p>Often, you can get an update to be noticed in Slicer by calling <code>node.Modified()</code>.  You could try that on the transform node (or maybe the display node).</p>

---
