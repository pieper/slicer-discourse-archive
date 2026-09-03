---
topic_id: 48040
title: "Resetting a transform in an existing node"
date: 2026-09-02
url: https://discourse.slicer.org/t/48040
last_bumped: 2026-09-02T15:02:19.733Z
---

# Resetting a transform in an existing node

**Topic ID**: 48040
**Date**: 2026-09-02
**URL**: https://discourse.slicer.org/t/resetting-a-transform-in-an-existing-node/48040

---

## Post #1 by @shai-ikko (2026-09-02 13:58 UTC)

<p>Hi,</p>
<p>In my extension, in some context, I need to reset a transform to Identity, without changing its node otherwise (that is, I need to keep its state wrt volumes, display-nodes etc). When I first wrote this, a few years ago, I found an effective way to do this was by calling</p>
<pre data-code-wrap="python"><code class="lang-python">transformNode.GetTransformToParent().Identity()
</code></pre>
<p>But recently, I found that (at least as of Slicer 5.8.1, maybe even before that) there’s a problem with this: after<code>slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")</code>, the transform to parent is not initialized, and <code>transformNode.GetTransformToParent()</code> returns <code>None</code>.</p>
<p>An obvious workaround is:</p>
<pre data-code-wrap="python"><code class="lang-python">if to_parent := transformNode.GetTransformToParent():
    to_parent.Identity()
</code></pre>
<p>But it feels dirty. Is there a cleaner way?</p>

---

## Post #2 by @Sunderlandkyl (2026-09-02 15:02 UTC)

<p>You can set the transform matrix to identity with:</p>
<pre><code class="lang-auto">transformNode.SetMatrixTransformToParent(vtk.vtkMatrix4x4())
</code></pre>
<p>This is the way that it’s done from the transform module widget: <a href="https://github.com/Slicer/Slicer/blob/feeb45346728c3a37115783aa40e03da3bfb2bf2/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx#L478-L479" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.cxx at feeb45346728c3a37115783aa40e03da3bfb2bf2 · Slicer/Slicer · GitHub</a></p>

---
