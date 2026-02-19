---
topic_id: 5113
title: "How To Obtain X Y Z Points From Fiducial Points And Insert T"
date: 2018-12-17
url: https://discourse.slicer.org/t/5113
---

# How to obtain x,y,z points from fiducial points and insert them into vtkPoints

**Topic ID**: 5113
**Date**: 2018-12-17
**URL**: https://discourse.slicer.org/t/how-to-obtain-x-y-z-points-from-fiducial-points-and-insert-them-into-vtkpoints/5113

---

## Post #1 by @chaddy1004 (2018-12-17 17:16 UTC)

<p>Hello</p>
<p>I am trying to get the point values of fiducial points and put them into a vtkPoints.</p>
<p>The end goal is to create a tps transformation using these fiducial points.</p>
<pre><code>tps = vtk.vtkThinPlateSplineTransform()
tps.SetSourceLandmarks()
tps.SetTargetLandmarks()
</code></pre>
<p>I was using this function and it requires me to input a vtkPoints.</p>
<p>I would appreciate it if you can help me.</p>
<p>Thank you</p>

---

## Post #2 by @adamrankin (2018-12-17 18:08 UTC)

<pre><code class="lang-python">n = slicer.util.getNode('F')

points = vtk.vtkPoints()

for i in range(0, n.GetNumberOfFiducials()):
  point = [0,0,0]
  n.GetMarkupPoint(i,0,point)
  points.InsertNextPoint(point[0], point[1], point[2])

print('Yay!')
</code></pre>

---

## Post #3 by @chaddy1004 (2018-12-17 18:13 UTC)

<p>Thank you! That is exactly what I needed!</p>

---

## Post #4 by @lassoan (2018-12-17 18:15 UTC)

<aside class="quote no-group" data-username="chaddy1004" data-post="1" data-topic="5113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chaddy1004:</div>
<blockquote>
<p>The end goal is to create a tps transformation using these fiducial points.</p>
</blockquote>
</aside>
<p>SlicerIGT extension’s Fiducial Registration wizard module does exactly this and much more. It offers a nice GUI, allows preview of results, real-time updates, helps collection of landmarks, can automatically match landmarks (even if their order is mixed up or the number of source and landmarks is not the same), compute residual error, etc.</p>

---

## Post #5 by @chaddy1004 (2018-12-17 18:46 UTC)

<p>Hi Andras</p>
<p>Thank you, I tried it out and it gives me the result I need. Is there a place where I can find more information on how to use the functions in a script?</p>
<p>Thank you</p>
<p>Chad Paik</p>

---

## Post #6 by @lassoan (2018-12-17 19:59 UTC)

<p>See documentation in header files:</p>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h" rel="nofollow noopener">https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/Logic/vtkSlicerFiducialRegistrationWizardLogic.h</a></li>
<li><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/MRML/vtkMRMLFiducialRegistrationWizardNode.h" rel="nofollow noopener">https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/MRML/vtkMRMLFiducialRegistrationWizardNode.h</a></li>
</ul>
<p>See examples of manipulating MRML nodes and using various module logics from Python in script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>
<p>Let us know if you have any specific questions.</p>

---

## Post #7 by @chaddy1004 (2018-12-21 18:22 UTC)

<p>Hi Andras</p>
<p>Is there any code that used the Fiducial Registration Wizard in their script? I could not find one in the repository.</p>
<p>I am just having trouble getting started in how to use the module. I want to to go through multiple fiducial mark up sets and find warping transform from one to another. How would I get started?</p>
<p>Thank you</p>
<p>Chad Paik</p>

---

## Post #8 by @lassoan (2018-12-21 22:25 UTC)

<p>All you need to do is to add a <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/FiducialRegistrationWizard/MRML/vtkMRMLFiducialRegistrationWizardNode.h" rel="nofollow noopener">fiducial registration wizard node</a> to the scene and set its input markup nodes and output transform nodes, registration mode, etc. Output is automatically updated if yiy enable autó-update or call the module logic’s Update Calibration method.</p>

---
