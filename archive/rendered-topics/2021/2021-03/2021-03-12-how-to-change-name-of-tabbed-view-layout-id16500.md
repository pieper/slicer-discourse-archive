---
topic_id: 16500
title: "How To Change Name Of Tabbed View Layout"
date: 2021-03-12
url: https://discourse.slicer.org/t/16500
---

# How to change name of tabbed view layout?

**Topic ID**: 16500
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/how-to-change-name-of-tabbed-view-layout/16500

---

## Post #1 by @akshay_pillai (2021-03-12 17:20 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.11</p>
<p>In the layout menu in the tabbed slices view option the tabs are named as Red, Green, yellow. Is there any way I can rename the tabs to - for example, axial, coronal, sagittal?</p>

---

## Post #2 by @lassoan (2021-03-14 05:58 UTC)

<p>You can either <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">create your own layout</a> with view names you like or rename existing slice view nodes:</p>
<pre><code class="lang-python">sliceNodes=slicer.util.getNodesByClass('vtkMRMLSliceNode')
sliceNodes[0].SetName('Axial')
sliceNodes[1].SetName('Coronal')
sliceNodes[2].SetName('Sagittal')
</code></pre>
<p>Note that the user can set any slice viewer to any orientation, so nothing guarantees that the view that you name “Axial” view will always show axial slice.</p>

---
