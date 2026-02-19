---
topic_id: 42182
title: "Disabling Surface Constraints Snap For Activated Markups Nod"
date: 2025-03-17
url: https://discourse.slicer.org/t/42182
---

# Disabling Surface Constraints Snap for Activated Markups Node

**Topic ID**: 42182
**Date**: 2025-03-17
**URL**: https://discourse.slicer.org/t/disabling-surface-constraints-snap-for-activated-markups-node/42182

---

## Post #1 by @jhan1245 (2025-03-17 08:01 UTC)

<p>Hi, I am currently using 3D Slicer 5.8.0 and developing scripted modules. As part of my work, I would like to know if there is an option to disable the automatic snapping to surface constraints when a Markups node is activated. While working with Markups, I have noticed that the control points tend to snap to the nearest surface, which is affecting the intended placement of the points. I am looking for a way to prevent this behavior.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d405f6c39f298448dbf3f5a0e6ee955679bc78.png" data-download-href="/uploads/short-url/g67JxrRJF9Bljsgl2i0jpP0Lu0o.png?dl=1" title="2025-03-17 165145" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d405f6c39f298448dbf3f5a0e6ee955679bc78.png" alt="2025-03-17 165145" data-base62-sha1="g67JxrRJF9Bljsgl2i0jpP0Lu0o" width="312" height="214"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-03-17 165145</span><span class="informations">312×214 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Additionally, as shown in the attached image, there is a polydata that follows the control points of the Markups. However, when moving the control points, they attempt to snap to the mesh surface, causing both the mesh and the control points to move closer in the Near Plane direction. This unintended snapping behavior is interfering with the expected positioning of the control points.</p>
<p>Could you please advise if there is a way to disable this feature, either through the UI or via scripting? Any guidance would be greatly appreciated.</p>
<p>Thank you for your time and support.</p>

---

## Post #2 by @rfenioux (2025-03-17 11:09 UTC)

<p>In the python console you can do:</p>
<pre><code class="lang-auto">model = getNode("ModelName")
model.SetSelectable(False)
</code></pre>

---

## Post #3 by @lassoan (2025-03-17 20:41 UTC)

<p><code>SetSelectable</code> prevents control points being snapped to the node, and you can also completely disable snapping for a markup in the Markups module GUI (Display / Advanced / 3D Display / Placement mode → unconstrained) or using Python scripting (modifying the markup display node properties). If you are defining curves on a surface then you can select a single model that the curve will snap to (anywhere on the surface), using Curve settings / Constrain to model.</p>

---

## Post #4 by @jhan1245 (2025-03-18 23:11 UTC)

<p>After applying the solution, the markup nodes no longer snap to the model nodes that should be ignored. I truly appreciate your assistance in resolving the issue.</p>
<p>Thank you once again for your support.</p>

---
