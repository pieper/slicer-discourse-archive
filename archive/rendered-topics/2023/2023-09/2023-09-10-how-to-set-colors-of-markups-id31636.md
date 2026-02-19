---
topic_id: 31636
title: "How To Set Colors Of Markups"
date: 2023-09-10
url: https://discourse.slicer.org/t/31636
---

# How to set colors of markups?

**Topic ID**: 31636
**Date**: 2023-09-10
**URL**: https://discourse.slicer.org/t/how-to-set-colors-of-markups/31636

---

## Post #1 by @esomjai (2023-09-10 10:07 UTC)

<p>Hi there, just  a quick question about the customisation of pre-populating linear and angle measurements this way.<br>
Would I be able to include the colour of the angle/line in the code? I tried to use L.SetColor() but never succeeded.<br>
My current code looks like this:</p>
<pre><code class="lang-auto">G=getNode('hard tissue')
L=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
firstPoint = G.GetNthControlPointPositionVector(4)
L.AddControlPoint(firstPoint)
L.SetName('mastoid height R')
</code></pre>
<p>and for the angle: (2 prepopulated points, one by hand)</p>
<pre><code class="lang-auto">F=getNode('soft tissue')
H=getNode('EA R intersection')
A=slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsAngleNode')
firstPoint = F.GetNthControlPointPositionVector(5)
A.AddControlPoint(firstPoint)
secondPoint = H.GetNthControlPointPositionVector(0)
A.AddControlPoint(secondPoint)
A.SetName('ear angle R')
</code></pre>
<p>Thank you again for your help!</p>

---

## Post #2 by @lassoan (2023-09-10 12:42 UTC)

<p>Display properties are specified in the “display” node associated with the markup node. This separation is useful for many purposes, for example it allows displaying the same markup differently in different views.</p>
<p>To change the color, you can do this:</p>
<pre><code class="lang-python">L.GetDisplayNode().SetColor(1, 0, 1)
</code></pre>

---
