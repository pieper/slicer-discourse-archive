---
topic_id: 12272
title: "Implementing Python Code Into 3D Slicer"
date: 2020-06-29
url: https://discourse.slicer.org/t/12272
---

# Implementing Python Code Into 3D Slicer

**Topic ID**: 12272
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/implementing-python-code-into-3d-slicer/12272

---

## Post #1 by @vertebra (2020-06-29 14:18 UTC)

<p>I am having a lot of trouble with this 3D Slicer software. I have created a module that links to my python file. The goal of my code is to get the user to select a markup fiducial node on the lumbar vertebra. Then using the flood fill through a vtk class, we basically encompass the singular lumbar the user specified. Every time I have tried the code from the repository, there is no location for a fiducial node. What else do I need to add to the code in the repository? Basically, do you have any GitHub resources or anything helping with the code? I’m very unfamiliar with Python unfortunately.</p>

---

## Post #2 by @lassoan (2020-07-01 01:43 UTC)

<p>Probably you have figured this out already, but for future reference, Slicer programming tutorials are available here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers">https://www.slicer.org/wiki/Documentation/Nightly/Training#Tutorials_for_software_developers</a></p>
<p>It is recommended to complete a few basic Python tutorials before and it helps a lot if you are somewhat familiar with VTK and Qt toolkits.</p>

---
