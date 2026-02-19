---
topic_id: 28816
title: "How To Set Clipping Method Of Vtkmrmlclipmodelsnode"
date: 2023-04-09
url: https://discourse.slicer.org/t/28816
---

# How to set clipping method of vtkMRMLClipModelsNode

**Topic ID**: 28816
**Date**: 2023-04-09
**URL**: https://discourse.slicer.org/t/how-to-set-clipping-method-of-vtkmrmlclipmodelsnode/28816

---

## Post #1 by @danpak94 (2023-04-09 13:47 UTC)

<p>Hello,</p>
<p>As the title suggests, I’m having trouble finding the right way to programmatically set the clipping method of vtkMRMLClipModelsNode. Code snippet to demonstrate issue:</p>
<pre><code class="lang-auto">clipModelNode = slicer.util.getFirstNodeByClassByName('vtkMRMLClipModelsNode', 'ClipModels')
clipModelNode.SetClipType(clipModelNode.ClipIntersection) # works fine
clipModelNode.SetRedSliceClipState(clipModelNode.ClipOff) # works fine
clipModelNode.SetYellowSliceClipState(clipModelNode.ClipPositiveSpace) # works fine
clipModelNode.SetGreenSliceClipState(clipModelNode.ClipNegativeSpace) # works fine
clipModelNode.SetClippingMethod # no attribute error
</code></pre>
<p>Any suggestions would be greatly appreciated.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2023-04-11 04:42 UTC)

<p>Good catch, the method was not Python-wrapped due to an incorrectly defined enumerated type. The problem is fixed now: <a href="https://github.com/Slicer/Slicer/pull/6935" class="inline-onebox">BUG: Fix Python wrapping of methods using enum arguments by lassoan · Pull Request #6935 · Slicer/Slicer · GitHub</a></p>
<p>The <code>SetClippingMethod</code> will be available in Slicer Preview Release downloaded on 2023-04-12 or later.</p>

---

## Post #3 by @danpak94 (2023-04-11 11:04 UTC)

<p>Awesome, thank you for the quick fix!</p>

---
