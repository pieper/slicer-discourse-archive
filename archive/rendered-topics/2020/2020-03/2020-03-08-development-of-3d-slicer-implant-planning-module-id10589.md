---
topic_id: 10589
title: "Development Of 3D Slicer Implant Planning Module"
date: 2020-03-08
url: https://discourse.slicer.org/t/10589
---

# Development of 3D Slicer Implant planning Module

**Topic ID**: 10589
**Date**: 2020-03-08
**URL**: https://discourse.slicer.org/t/development-of-3d-slicer-implant-planning-module/10589

---

## Post #1 by @manjula (2020-03-08 12:05 UTC)

<p>We have started developing a module based on Pedicle Screw Simulator for dental implant planning, simulation and navigation <a class="mention" href="/u/chamath">@chamath</a> , <a class="mention" href="/u/anuradha">@anuradha</a> and <a class="mention" href="/u/anuradha_rajapaksha">@Anuradha_Rajapaksha</a>  .</p>
<p>We would hope for support in this project and keep this thread running for development of this.</p>
<p>The first problem we have is, in the screw insertion <a href="https://github.com/cmfsx/SlicerImplant/blob/master/PedicleScrewSimulatorWizard/ScrewStep.py" rel="nofollow noopener">step</a>, since we plan to let the user to import the dental implant they want and we assume every company will have their screw oriented differently because there is no standard for this. However we want to automatically orient the screw tip to the fiducial placed by the user.</p>
<p>therefore,</p>
<p>transformScrewTemp = slicer.vtkMRMLLinearTransformNode()<br>
slicer.mrmlScene.AddNode(transformScrewTemp)<br>
transformScrewTemp.ApplyTransformMatrix(matrix)</p>
<p>Currently ‘matrix’ was calculated using following static matrix.<br>
matrix.DeepCopy((1, 0, 0, self.coords[0],<br>
0, 0, 1, self.coords[1],<br>
0, 1, 0, self.coords[2],<br>
0, 0, 0, 1))</p>
<p>We’d like to make it dynamic with the axis specified by a given orientation. Can you point us to a reference where we can read about how the matrix coefficients are calculated for a given orientation.</p>

---

## Post #2 by @lassoan (2020-03-08 21:17 UTC)

<p>I would recommend to store all models in a standard coordinate system, for example, origin is along the centerline at the bone line; z axis is the center of rotation of the implant, pointing towards the crown; x and y axes are orthogonal to z axis (they can be arbitrary, or aligned to some specific direction), unit is mm.</p>
<p>If any of the models that you receive does not follow the standard coordinate system, you can fix that using Transforms module, and when the alignment is correct, harden the transform, and save the resulting model.</p>
<p>For future reference, if you need to compute transformation matrix then you can use <code>vtkTransform</code> class: call <code>Rotate...</code>, <code>Translate...</code>, etc. then get the resulting matrix using <code>GetMatrix</code>.</p>

---
