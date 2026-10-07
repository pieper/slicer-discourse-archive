---
topic_id: 48374
title: "Small screen-space \"dash\" appears at curve midpoint after cloning a Markups curve (Markups → Clone)"
date: 2026-10-01
url: https://discourse.slicer.org/t/48374
last_bumped: 2026-10-06T21:44:44.521Z
---

# Small screen-space "dash" appears at curve midpoint after cloning a Markups curve (Markups → Clone)

**Topic ID**: 48374
**Date**: 2026-10-01
**URL**: https://discourse.slicer.org/t/small-screen-space-dash-appears-at-curve-midpoint-after-cloning-a-markups-curve-markups-clone/48374

---

## Post #1 by @evan1 (2026-10-01 14:51 UTC)

<p><strong>Environment:</strong> 3D Slicer 5.12.3, Windows 11</p>
<p><strong>Summary</strong></p>
<p>After cloning a Markups curve via the Markups module (right-click a curve node in the list → <strong>Clone</strong>), the cloned curve displays a small horizontal line (“dash”) at (or very near) the <strong>curve’s midpoint</strong>. The original curve does not show it. It reproduces reliably, including with a freshly drawn dummy curve (4 arbitrary points).</p>
<p>The midpoint location is confirmed by the control point counts: most of my curves have 4 points, and their dash sits next to the <strong>second</strong> control point; one curve has 5 points, and its dash sits next to the <strong>third</strong> control point (its exact middle). So the dash tracks the curve’s midpoint, not a specific control point.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da2001947ac2ba7f62fe0beefdd03492b425c8d.png" data-download-href="/uploads/short-url/4e8VIg5g1XIhxP6wmPmFZVAsSQt.png?dl=1" title="Screenshot 2026-09-30 170005" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da2001947ac2ba7f62fe0beefdd03492b425c8d.png" alt="Screenshot 2026-09-30 170005" data-base62-sha1="4e8VIg5g1XIhxP6wmPmFZVAsSQt" width="339" height="280"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-30 170005</span><span class="informations">339×280 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7aaa2886308a9bed92156d3c19f1bf124741de6.png" data-download-href="/uploads/short-url/sukBd8L6m5CgNOydFzwmEMY3CvA.png?dl=1" title="Screenshot 2026-09-30 131415" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7aaa2886308a9bed92156d3c19f1bf124741de6.png" alt="Screenshot 2026-09-30 131415" data-base62-sha1="sukBd8L6m5CgNOydFzwmEMY3CvA" width="242" height="249"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-09-30 131415</span><span class="informations">242×249 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Observed behavior</strong></p>
<ul>
<li>
<p>The dash is always screen-horizontal and projects to the right of the curve regardless of camera angle — suggesting a 2D/screen-space actor rather than 3D scene geometry. It is also always the same pixel size no matter how much I have zoomed in or out on the 3D scene.</p>
</li>
<li>
<p>It follows the curve’s midpoint wherever the geometry goes: moving any control point — including programmatically via <code>SetNthControlPointPosition()</code> — moves the dash along with the curve. Initially it looked tied to control point 2, because on my 4-point curves the midpoint happens to sit right next to that point; the 5-point curve (dash at its middle point) confirms it tracks the midpoint.</p>
</li>
<li>
<p>It appears immediately upon cloning, before any geometry or display changes.</p>
</li>
<li>
<p>It highlights (active color) together with the curve when hovering the curve, but is not individually clickable/selectable.</p>
</li>
<li>
<p>Toggling the clone’s display node visibility hides the dash together with the curve; restoring visibility brings it back.</p>
</li>
</ul>
<p><strong>What I ruled out</strong> (all compared between original and clone, all identical):</p>
<ul>
<li>
<p>Display node properties: point label visibility (off), text scale (0), glyph type (Sphere3D), glyph scale, line thickness, curve line size mode, fill/outline/occluded visibility, rotation/translation/scale handle visibility, interaction handle scale.</p>
</li>
<li>
<p>No measurements exist on either node (“no measurements” in the Markups Measurements section).</p>
</li>
<li>
<p>Per-point properties: labels, position status (all defined), locked and selected flags — identical on all 4 points of both nodes.</p>
</li>
<li>
<p>Node class is identical (<code>vtkMRMLMarkupsCurveNode</code>) and the two nodes have <strong>separate</strong> display nodes (not shared).</p>
</li>
<li>
<p>Changing the curve type (spline → polynomial / Kochanek) does not remove the dash.</p>
</li>
<li>
<p>Changing point spacing/geometry (including widening the gap between points 1 and 2) does not remove the dash.</p>
</li>
</ul>
<p><strong>Renderer inspection</strong></p>
<p>Iterating the 3D view renderer’s visible props near the curve shows <strong>two</strong> <code>vtkSlicerCurveRepresentation3D</code> instances with nearly identical bounds:</p>
<pre><code class="lang-auto">3D: vtkSlicerCurveRepresentation3D | bounds: [6.6, 15.3, -79.2, -67.8, -221.2, -211.8]
3D: vtkSlicerCurveRepresentation3D | bounds: [5.8, 14.3, -86.6, -73.5, -242.8, -233.0]
</code></pre>
<p>(The bounds above reflect the curve after control point positions were moved during testing.)</p>
<p><strong>My chatbot’s suspicion</strong></p>
<p>The Markups “clone” operation appears to leave behind (or create an extra) curve widget/representation in the view, which renders a small screen-space element anchored to the <strong>curve’s midpoint</strong> — the same location where the markups interaction-handle widget places its center elements. Because this element is drawn by a stale/duplicated representation rather than the live display node, changing display properties (handle visibility, glyph type, labels, measurements) has no effect on it. It could be a degenerate center/handle/label actor that the duplicated representation never cleans up.</p>
<p><strong>Questions</strong></p>
<ol>
<li>
<p>Is this a known issue with the Markups “clone” operation?</p>
</li>
<li>
<p>Is there a workaround to remove the stray element without deleting and recreating the cloned nodes?</p>
</li>
<li>
<p>Is there additional diagnostic information I could collect that would help pin this down (e.g., a way to identify which of the two <code>vtkSlicerCurveRepresentation3D</code> instances draws the dash)?</p>
</li>
</ol>
<p>I’ve checked the 5.12 release changelog including the 5.12.4 patch notes and found no mention of a related fix. The new arrow glyph types (Arrow2D etc.) are not in use here — both nodes’ glyph type is Sphere3D.</p>
<p>Thank you!</p>

---

## Post #2 by @evan1 (2026-10-06 21:44 UTC)

<p><strong>Solved: the dash is the curve’s Properties Label</strong></p>
<p>Resolved. For anyone who finds this later, the small dash at the curve midpoint is the curve’s <strong>Properties Label</strong> (the label that displays the node name + measurements, anchored at the curve’s midpoint).</p>
<p><strong>What I saw:</strong> After cloning a Markups curve (Markups → Clone) — and, as I noted in my update, also after simply renaming the curve node — a small dash appeared at the curve’s midpoint. It stayed at the midpoint when rotating the camera (so world-anchored, not actually a screen-space overlay as my title suggested), and it appeared in saved screenshots. Renaming a freshly drawn curve in an empty scene reproduced it.</p>
<p><strong>Root cause:</strong> My saved markups display defaults use text size 0%, so the properties label’s text is invisible — but the label itself was still enabled, and a small piece of its geometry renders at the anchor point when the label is regenerated (which is why it appeared after clone and rename). With normal text size you’d simply see the label text at that spot.</p>
<p><strong>Workaround:</strong> Markups module → Display → Advanced → uncheck <strong>Properties Label</strong>. To turn it off for all markups at once:</p>
<p>python</p>
<p>Copy</p>
<pre><code class="lang-auto">for n in slicer.mrmlScene.GetNodesByClass('vtkMRMLNode'):
    if n.IsA('vtkMRMLMarkupsNode') and n.GetDisplayNode():
        n.GetDisplayNode().SetPropertiesLabelVisibility(False)
</code></pre>
<p>Possibly worth a look from developers: should any label geometry render when the text size is 0? Version 5.12.3, Windows 11</p>

---
