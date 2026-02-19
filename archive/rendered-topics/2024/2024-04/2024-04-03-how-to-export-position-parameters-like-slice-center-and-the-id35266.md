---
topic_id: 35266
title: "How To Export Position Parameters Like Slice Center And The"
date: 2024-04-03
url: https://discourse.slicer.org/t/35266
---

# How to export position parameters like slice center and the normal vector for the slice plane?

**Topic ID**: 35266
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/how-to-export-position-parameters-like-slice-center-and-the-normal-vector-for-the-slice-plane/35266

---

## Post #1 by @Arjun (2024-04-03 22:26 UTC)

<p>Hi!</p>
<p>I wanted to know how can we export position parameters like slice center and the normal vector for the slice plane we are viewing such that I can visualize that slice of the 3D data in lets say python? Thanks for the help</p>

---

## Post #2 by @rfenioux (2024-04-04 07:52 UTC)

<p>You can get the slice transformation matrix using the slice Id (here for the default red slice). This returns the 4x4 transform matrix, from which you can retrieve the slice origin and the normal vector.</p>
<pre><code class="lang-auto">sliceNode = slicer.util.getNode('vtkMRMLSliceNodeRed')
sliceToRas = sliceNode..GetSliceToRAS()
origin = np.array([sliceToRas.GetElement(i, 3) for i in range(3)])
normal = np.array([sliceToRas.GetElement(0, 2), sliceToRas.GetElement(1, 2), sliceToRas.GetElement(2, 2)])
</code></pre>

---

## Post #3 by @Arjun (2024-04-17 00:23 UTC)

<p>Hi! Thank you so much! I tried this but it does seem to be updating the slice we are seeing on the Red, Green and Yellow panels. The 4x4 transform matrix remains the same, is there something else I need to do for getting the transform matrix for the slice I see on the screen after interacting with it?</p>

---

## Post #4 by @mikebind (2024-04-17 01:29 UTC)

<p><code>sliceNode.GetSliceToRAS()</code> will give you the updated 4x4 matrix after interaction. The <code>sliceToRas</code> matrix in the code above is just a stored copy of that information at the point when that code is run, and will not be dynamically updated as the slice location is changed.</p>

---
