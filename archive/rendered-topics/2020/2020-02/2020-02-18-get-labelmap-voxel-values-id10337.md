---
topic_id: 10337
title: "Get Labelmap Voxel Values"
date: 2020-02-18
url: https://discourse.slicer.org/t/10337
---

# Get LabelMap voxel values

**Topic ID**: 10337
**Date**: 2020-02-18
**URL**: https://discourse.slicer.org/t/get-labelmap-voxel-values/10337

---

## Post #1 by @loubna (2020-02-18 15:20 UTC)

<p>how can we extract points from binary volume (labelMap). I confuse between the vertices of each voxel and points. So I need extract  points from labelMap.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-02-18 15:24 UTC)

<p>You can get voxel values of a labelmap volume as a numpy array by calling <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromVolume"><code>slicer.util.arrayFromVolume</code></a>.</p>

---

## Post #3 by @loubna (2020-02-18 15:28 UTC)

<p>Is there other filters to do that in vtk and C++?</p>

---

## Post #4 by @lassoan (2020-02-18 15:32 UTC)

<p>In C++ you can get access to the <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html">vtkImageData</a> by calling volumeNode-&gt;GetImageData(). To map between voxel and physical space, you can use the matrix returned by GetIJKToRAS().</p>

---

## Post #5 by @loubna (2020-02-18 15:36 UTC)

<p>I am trying to get the coordinates of 3D points from vtkImageData(); For example, given a <code>vtkImageData</code> object, called <code>image</code> , I know I can get the voxel values like this:</p>
<p>image = vtk.vtkImageData()<br>
voxels = image.GetPointData().GetScalars().</p>
<p>but what I want is a 3D point.</p>

---

## Post #6 by @lassoan (2020-02-18 15:48 UTC)

<p>You can use <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#aa89753c6bbd8af0d6c1a599e03081714">GetScalarComponentAsDouble(int x, int y, int z, int component)</a> to get value of a voxel. You can get voxel coordinates from physical coordinates using the matrix returned by <code>volumeNode-&gt;GetIJKToRAS()</code>.</p>
<p>Note that GetScalarComponentAsDouble is extremely slow - it is mainly for testing and debugging. You can sample millions of points at once using vtkProbeFilter.</p>

---

## Post #7 by @loubna (2020-02-18 15:56 UTC)

<p>Thank you so much for the response . as the voxel has 8 vertices, I guess obtain 8 points for each voxel?</p>

---

## Post #8 by @lassoan (2020-02-18 16:19 UTC)

<p>If nearest neighbor interpolation is good enough then you could use <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#aa89753c6bbd8af0d6c1a599e03081714">GetScalarComponentAsDouble</a>. For higher-order interpolation, you could use any of the <a href="https://vtk.org/doc/nightly/html/classvtkAbstractImageInterpolator.html">vtkAbstractImageInterpolator</a> child classes. However, you should use vtkProbeFilter, which is simpler and faster, as it samples all the points that you are interested in at once.</p>

---

## Post #9 by @loubna (2020-02-18 18:42 UTC)

<p>What about this;</p>
<p>image=vtk.vtkImageData();</p>
<p>for each voxel of the volume , to recover the corresponding 3 point, we can do:</p>
<p>double p[3];<br>
int coords={i,j,k}   // i, j , k are the coordinates of each vertex of the voxel<br>
image-&gt;GetPoint(image-&gt;ComputePointId(coords), p);</p>

---

## Post #10 by @lassoan (2020-02-18 19:15 UTC)

<p>image-&gt;GetPoints(image-&gt;ComputePointId(…)) is just a more complicated version of image-&gt;GetScalarComponentAsDouble or image-&gt;GetScalarPointer and it is suitable if nearest neighbor interpolation is acceptable.</p>
<p>IJK coordinates are voxel coordinates, vertex coordinates are in physical coordinates, so the coordinate values you use are incorrect. I already wrote above 2x that you need to convert using IJK to RAS matrix.</p>

---

## Post #11 by @loubna (2020-02-18 19:20 UTC)

<p>Thank you very much for your help , and i know that I must convert the IJK  To RAS coordinates. I developped a non-optimized marching cubes algorithm as vtk Filter. I did all computations in ijk coordinates and once the algorithm generates the list of triangles and points , I converted the output from IJK To RAS.</p>

---

## Post #12 by @loubna (2020-02-19 12:05 UTC)

<p>Hi Mr</p>
<p>I have just another question. A have Applied IJKTORAS transformation to get the IJK voxel coordinates in word space, but what about normal vectors which I have computed from volume data. Normals vectors need to be transformed into word space or not. If right, what must I use?</p>
<p>Thank’s in advance for your response</p>

---

## Post #13 by @lassoan (2020-02-20 03:55 UTC)

<p>Yes, you need to transform vectors by multiplying with the same homogeneous transformation matrix. Note that point positions must be represented as (x, y, z, 1) while vector directions as (x, y, z, 0).</p>

---
