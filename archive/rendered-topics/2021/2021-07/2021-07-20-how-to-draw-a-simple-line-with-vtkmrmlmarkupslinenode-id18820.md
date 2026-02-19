---
topic_id: 18820
title: "How To Draw A Simple Line With Vtkmrmlmarkupslinenode"
date: 2021-07-20
url: https://discourse.slicer.org/t/18820
---

# How to draw a simple line with vtkMRMLMarkupsLineNode?

**Topic ID**: 18820
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/how-to-draw-a-simple-line-with-vtkmrmlmarkupslinenode/18820

---

## Post #1 by @Guillaume (2021-07-20 13:04 UTC)

<p>Hello,<br>
I have not found how to make a simple line going from point P1 to point P2. with vtkMRMLMarkupsLineNode … I’m still on Slicer 4.11.<br>
Could you help me?<br>
Thank you !!</p>

---

## Post #2 by @Mik (2021-07-20 14:23 UTC)

<p>Something like</p>
<pre><code class="lang-auto"># Create line node
line = slicer.mrmlScene.AddNewNodeByClass( 'vtkMRMLMarkupsLineNode', 'TestLine')
# First point
pBegin = vtk.vtkVector3d( 0, 0, 0)
# Second point
pEnd = vtk.vtkVector3d( 100, 100, 100)
# Add points
line.AddControlPointWorld(pBegin)
line.AddControlPointWorld(pEnd)
</code></pre>

---

## Post #3 by @Guillaume (2021-07-20 14:45 UTC)

<p>Thank you for your help.<br>
But, it doesn’t work … The row doesn’t even append in the data.</p>

---

## Post #4 by @Mik (2021-07-20 14:58 UTC)

<p>I have tested with version <a href="https://download.slicer.org/" rel="noopener nofollow ugc">4.11</a> from site page and it works without problems, and node is shown in subject hierarchy correctly.</p>

---

## Post #5 by @Mik (2021-07-20 15:10 UTC)

<p>Make sure that every line of code is executed correctly.</p>

---

## Post #6 by @Guillaume (2021-07-20 15:19 UTC)

<p>yesss… <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=9" title=":sob:" class="emoji" alt=":sob:"> I find the problème… I totally forgot to call the function… Sorry <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=9" title=":sob:" class="emoji" alt=":sob:"> And thank you !</p>

---
