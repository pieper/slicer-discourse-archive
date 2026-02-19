---
topic_id: 1492
title: "Calling In A Mat Object Into 3D Slicer"
date: 2017-11-20
url: https://discourse.slicer.org/t/1492
---

# Calling in a .mat object into 3D Slicer

**Topic ID**: 1492
**Date**: 2017-11-20
**URL**: https://discourse.slicer.org/t/calling-in-a-mat-object-into-3d-slicer/1492

---

## Post #1 by @stevenagl12 (2017-11-20 13:58 UTC)

<p>I was wondering if Slicer has any functionality for calling in a .mat object into the program. I know that there is a MATLAB bridge, does this have the capability of calling in these objects?</p>

---

## Post #2 by @lassoan (2017-11-20 15:00 UTC)

<p>The only .mat file reading option I can think about is through the MatlabBridge. You can define a simple module that takes a .mat file as input and returns output whatever data you would like to retrieve from the .mat file.</p>
<p>In general, I would strongly recommend using common standard open file formats for data storage instead of .mat files (.mha or .nrrd for images, .stl or .ply for surface meshes, .xml or .json for various parameter files, etc.).</p>

---

## Post #3 by @ihnorton (2017-11-20 15:26 UTC)

<p>You can use <a href="https://docs.scipy.org/doc/scipy/reference/tutorial/io.html"><code>scipy.io.loadmat</code></a> and then push the buffers into VTK objects with the examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting">Python scripting</a> section.</p>

---
