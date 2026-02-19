---
topic_id: 21558
title: "Suggestion For An Extension To Measure Parameters Like Angle"
date: 2022-01-21
url: https://discourse.slicer.org/t/21558
---

# Suggestion for an extension to measure parameters (Like angle in 2d plane, drawing straight and curved line) or is there any other DICOM viewer like slicer with these features available for windows

**Topic ID**: 21558
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/suggestion-for-an-extension-to-measure-parameters-like-angle-in-2d-plane-drawing-straight-and-curved-line-or-is-there-any-other-dicom-viewer-like-slicer-with-these-features-available-for-windows/21558

---

## Post #1 by @akil.prabhakar (2022-01-21 13:32 UTC)

<p>Im trying to measure a 3D CT based parameters. Most of the simple task I am able to do with MarkUps. But, some task like drawing a perfect circle is not possible. I have already asked for help. But because of my poor knowledge in coding I am not able to do.</p>

---

## Post #2 by @mikebind (2022-01-21 20:27 UTC)

<p>Angle in a 2D plane is possible using Markups as well, using angle tool. You place three control points in a row via mouse clicks and it reports the angle formed at the second point.</p>
<p>Drawing a closed perfect circle is a very simple task and would be quick to implement in a short python script.  I understand that you don’t feel you have the skill to implement this yourself, but if you can tell me what simple task you want to accomplish I would be happy to try to help.</p>
<p>What do you want to measure using this tool? The radius or diameter of the circle?  The area enclosed?  The mean voxel value enclosed (this is slightly more work to gather)?  The simplest way to control the circle positioning would be to have a small number of points placed.  The two placement schemes which come to mind are</p>
<ul>
<li>one point at the center and one on the circumference</li>
<li>three points on the circumference</li>
</ul>
<p>Does one of those sound easier for your task?</p>

---
