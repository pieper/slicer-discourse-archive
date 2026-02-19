---
topic_id: 9447
title: "How To Set Select Fudicial Points One By One"
date: 2019-12-09
url: https://discourse.slicer.org/t/9447
---

# How to set/select Fudicial Points one by one

**Topic ID**: 9447
**Date**: 2019-12-09
**URL**: https://discourse.slicer.org/t/how-to-set-select-fudicial-points-one-by-one/9447

---

## Post #1 by @Aping (2019-12-09 15:12 UTC)

<p>Hi slicer experts,</p>
<p>There are 100 coordinates in a file named 1,2,3,…100. I want to make one point’s color is different from others. For example, point 1st to 5th is red, and the 6th is yellow, the left (7th-100th) is invisible.<br>
I load the coordinates into Slicer, firstly.</p>
<pre><code class="lang-auto">slicer.util.loadMarkupsFiducialList('fiducial_coords.fcsv')
mDisplayNode = getNode('vtkMRMLMarkupsFiducialNode1').GetDisplayNode()
</code></pre>
<p>Now, I want to change the point color one by one, but it will change the color of all points by using:</p>
<pre><code class="lang-auto">mDisplayNode.SetSelectedColor(0,1,0)
</code></pre>
<p>Does anyone know how to select one point and set the corresponding property?</p>
<p>Thanks is advance.</p>

---

## Post #2 by @pieper (2019-12-09 15:31 UTC)

<p>Within the markup list you can set each fiducial selected or not and that will change between two colors: <code>f.SetNthFiducialSelected(0, False)</code></p>

---

## Post #3 by @Aping (2019-12-09 15:39 UTC)

<p>Thanks Pieper. Yes , it works.<br>
Thanks again.</p>

---

## Post #4 by @Aping (2019-12-09 16:33 UTC)

<p>Hello, Pieper,<br>
Do you know how to change the size of the selected fiducial?<br>
I use the following function, but it will change all fiducial points in the list. I want to adjust size of the selected point only.</p>
<pre><code class="lang-auto">fiducialDisplayNode.SetGlyphScale(2.5)
</code></pre>
<p>Thanks in advance.</p>

---

## Post #5 by @muratmaga (2019-12-09 16:35 UTC)

<p>Currently it is not possible to set different scale or color options for fiducials in a single fiducial list. If you need to do that, you will have to break apart your list. (i.e., clone your existing one, or create a new  empty list, and copy/paste from the original).</p>

---

## Post #6 by @lassoan (2019-12-09 17:12 UTC)

<p>You can also create a model node with arbitrarily scaled and colored spheres, using <a href="https://vtk.org/doc/nightly/html/classvtkGlyph3D.html">vtkGlyph3D</a> filter. It probably takes just a couple of lines of Python code to create a model from a point list.</p>
<p>If you have a script that does what you need, you can create a small Python-scripted module from it by following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">developer tutorials</a>.</p>

---

## Post #7 by @Aping (2019-12-09 22:24 UTC)

<p>Thanks for all your suggestions and help. It is very useful.<br>
Best wishes,</p>

---
