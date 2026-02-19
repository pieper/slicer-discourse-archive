---
topic_id: 29085
title: "Rename Vtkmrmlmarkupsfiducialnode"
date: 2023-04-24
url: https://discourse.slicer.org/t/29085
---

# Rename vtkMRMLMarkupsFiducialNode

**Topic ID**: 29085
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/rename-vtkmrmlmarkupsfiducialnode/29085

---

## Post #1 by @dsa934 (2023-04-24 08:32 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>In the case of ‘vtkCurve’ and ‘vtkClosedCurve’ nodes, changing their ‘<strong>name</strong>’ is reflected on the screen in real time. However, in the case of 'vtkMRMLMarkupsFiducialNode, even if the ‘<strong>name</strong>’ is changed, it is not reflected in real time, and it is reflected in real time only when the <strong>name of ’ Control point’</strong> in a is changed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd8aebc279c25d331258170f0c042eaed4569a79.png" data-download-href="/uploads/short-url/vBR9McTve3GccqUUggocoyKD1Bn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8aebc279c25d331258170f0c042eaed4569a79_2_690x219.png" alt="image" data-base62-sha1="vBR9McTve3GccqUUggocoyKD1Bn" width="690" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8aebc279c25d331258170f0c042eaed4569a79_2_690x219.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8aebc279c25d331258170f0c042eaed4569a79_2_1035x328.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd8aebc279c25d331258170f0c042eaed4569a79_2_1380x438.png 2x" data-dominant-color="6B6B72"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×607 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When changing the name of ‘vtkMRMLMarkupsFiducialNode’ that exists in the ‘Node’ area of the UI, how is it reflected in the corresponding VIEW in real time?</p>

---

## Post #2 by @dsa934 (2023-04-25 05:01 UTC)

<pre><code class="lang-auto">SetNodes = slicer.util.getNodesByClass('vtkMRMLMarkupsFiducialNode')
    length = len(SetNodes)
    for idx in range(length):
        SetNodes[idx].SetNthControlPointLabel(0, SetNodes[idx].GetName() )
</code></pre>
<p>Aha, it works just by coding like this</p>

---

## Post #3 by @lassoan (2023-04-25 12:19 UTC)

<p>At far as I remember this issue was fixed in the current Slicer version (Slicer-5.2.2). Always use at least the latest Slicer Stable Release. If you find any problems in the latest version then you can report it here.</p>

---
