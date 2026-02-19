---
topic_id: 11961
title: "Curve Label Name In 3D View"
date: 2020-06-09
url: https://discourse.slicer.org/t/11961
---

# Curve label name in 3D view?

**Topic ID**: 11961
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/curve-label-name-in-3d-view/11961

---

## Post #1 by @hherhold (2020-06-09 16:12 UTC)

<p>Is it possible to display the label name for a curve? I know you can show the point labels for the control points, but is it possible to display the curve label name in the 3D view, somewhere along the curve?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-06-09 16:18 UTC)

<p>Right now we only display markups node name for angles and lines, but we could enable this for curves as well (we would just need to expose an option on the GUI to allow to show/hide it). To make it work well, we would also need to make the label movable (and connect to the label to the markup by a thin line), which would be some more work.</p>
<p>For now, you can right-click the curve to show it in Markups module and you can change its color or show/hide in Markups module to find a node in the views. You can also add a label to any of the control points to make it easier to find.</p>
<p>Can you write a bit about your workflow and how would you use the labels?</p>

---

## Post #3 by @hherhold (2020-06-09 17:02 UTC)

<p>I’m using curves to diagram internal anatomy of various vessels (tubes) and it’s working great. I’d like to be able to have a name of a particular vessel, DAA for example (dorsal abdominal arch), displayed along with the curve. I can show the control points, as you mentioned, as DAA_1, DAA_2, and so on, but it gets pretty crowded. I’d like to be able to just show DAA somewhere along the curve. As a workaround I guess I could define one of the control points to be the “label”, and change the “Name” field to DAA.</p>
<p>Do you think this would be generally useful?</p>
<p>Thanks!<br>
-Hollister</p>

---

## Post #4 by @hherhold (2020-06-09 17:04 UTC)

<p>I guess I skipped one important part - the curve is a schematic representation of the vessel in question, and the goal is to create a network/tree-like representation of the vessel architecture. The goal is to be able to compare architectures between different specimens, so having the names visible would be particularly useful.</p>
<p>Hope this clarifies some!</p>

---

## Post #5 by @lassoan (2020-06-09 17:30 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="3" data-topic="11961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I could define one of the control points to be the “label”, and change the “Name” field to DAA. Do you think this would be generally useful?</p>
</blockquote>
</aside>
<p>Yes, showing a label for a markups node (and one or more measurement or other extra information) in a label makes sense and we’ll implement this soon.</p>
<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="11961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>goal is to create a network/tree-like representation of the vessel architecture</p>
</blockquote>
</aside>
<p>VMTK uses a model node to represent vessel trees. It is nice because you can assign arbitrary scalars to points or cells (branches) and you can use VTK filters to process it. However, model nodes are hard to create or edit manually (add/modify/delete points, branches, etc.), that’s why representing the tree using curve nodes could be useful. In the end, probably the best would be to implement lossless conversion between model node and curve hierarchy in both ways.</p>
<aside class="quote no-group" data-username="hherhold" data-post="4" data-topic="11961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>The goal is to be able to compare architectures between different specimens, so having the names visible would be particularly useful.</p>
</blockquote>
</aside>
<p>How do you compare architectures? By visual assessment, showing two trees side by side? Or compare branch properties (radius, length, curvature, torsion, tortuosity) of corresponding branches?</p>

---

## Post #6 by @hherhold (2020-06-09 17:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="11961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you compare architectures? By visual assessment, showing two trees side by side? Or compare branch properties (radius, length, curvature, torsion, tortuosity) of corresponding branches?</p>
</blockquote>
</aside>
<p>Visually at this point, comparing trees/architectures side by side. It’s largely morphological differences between specimens (orders and families) that we’re looking at, and mostly connectivity. We also want to look at vessel diameter/thickness, but overall network/connectivity is the first step.</p>

---
