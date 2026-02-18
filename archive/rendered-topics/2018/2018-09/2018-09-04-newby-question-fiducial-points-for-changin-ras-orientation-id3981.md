# Newby question, Fiducial points for changin RAS orientation

**Topic ID**: 3981
**Date**: 2018-09-04
**URL**: https://discourse.slicer.org/t/newby-question-fiducial-points-for-changin-ras-orientation/3981

---

## Post #1 by @SebastianE93 (2018-09-04 03:25 UTC)

<p>Operating system: win 10 - 64<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I would like to know how to use 3 fiducial points to get a plane that could be my anterior plane in RAS orientation. I tried to create a matrix that would represent this plane and use it for changing the base of the matrix but I don’t know how to code the transformation.</p>
<p>Basically I want to use a plane that I choose with 3 fiducial markers and therefore, change the RAS orientation. It is possible?</p>
<p>I’m using Python<br>
Thanks,</p>

---

## Post #2 by @steffen-o (2018-09-04 14:34 UTC)

<p>Have a look at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials" rel="nofollow noopener">Documentation/Nightly/ScriptRepository</a><br>
there you find what you are looking for --&gt; <strong>Fit slice plane to markup fiducials</strong></p>

---

## Post #3 by @SebastianE93 (2018-09-05 00:36 UTC)

<p>Thanks you, but I would like to fit the RAS orientation to the plane I create. The solution presented in <strong>Fit slice plane to markup fiducials</strong> is for the ‘red’ plane. Maybe it’s just changing the name but I have trouble with the coding.</p>

---

## Post #4 by @ihnorton (2018-09-05 00:58 UTC)

<p>If you are using a <a href="https://www.vtk.org/doc/nightly/html/classvtkPlane.html">vtkPlane</a> then you can calculate the normal with the formula in the linked solution, and use vtkPlane::SetNormal and vtkPlane::SetOrigin to set the orientation.</p>

---

## Post #5 by @SebastianE93 (2018-09-05 01:28 UTC)

<p>Thanks, it’s perfect!</p>

---
