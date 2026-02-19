---
topic_id: 19889
title: "Extracting The Centerline Of A Tunnel Point Cloud"
date: 2021-09-27
url: https://discourse.slicer.org/t/19889
---

# Extracting the centerline of a tunnel point cloud 

**Topic ID**: 19889
**Date**: 2021-09-27
**URL**: https://discourse.slicer.org/t/extracting-the-centerline-of-a-tunnel-point-cloud/19889

---

## Post #1 by @Ahmad1 (2021-09-27 20:33 UTC)

<p>Hello, I am a new user of 3d slicer. Currently I am working on extracting the centerline of a tunnel. I have the tunnel as point cloud data and I have managed to use Pyvista to create the mesh. My question is can I load the point cloud data directly to 3d slicer and compute the centerline or should I do some modification?<br>
Any tips or procedures to convert my data into the specified formats are appreciated.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-09-27 20:39 UTC)

<p>You can get a centerline curve from a model or segmentation using <a href="https://github.com/vmtk/SlicerExtension-VMTK/#the-vmtk-extension-for-3d-slicer">VMTK extension’s</a> Extract centerline module.</p>
<p>By “point cloud” do you mean you have a labelmap volume where certain points are labeled as tunnel points; or you have a list of points in a vtkPolyData in completely random positions? If it is the former then you don’t need any processing using pyvista but you can load the volume directly into Slicer.</p>

---

## Post #3 by @Ahmad1 (2021-09-27 21:49 UTC)

<p>Hello, thanks for the reply. The data I have are raw 3d data collected by a terrestrial laser scanner, thus each point is defined by an x,y,z coordinate.<br>
If you mean by lablemap volume a voxel grid, I think I can transform the point cloud into a voxel grid in Open3d, but I dont know if there should be further modifications since the tunnel is open on entry and exit and has some branches on the sides. Plus does it need to be a solid object and not hollow on the inside?<br>
Again much appreciated for the help.</p>

---

## Post #4 by @lassoan (2021-09-28 00:09 UTC)

<p>If you use a laser scanner then probably reconstructing a surface is better representation than a labelmap volume.</p>
<p>If you often load such scans and you want to make it very convenient for users then you can add a module with a GUI that performs the surface reconstruction, centerline extraction, and any further analysis or processing that you may need.</p>

---

## Post #5 by @Ahmad1 (2021-09-28 07:13 UTC)

<p>I will try to construct the surface and see what I can obtain. Again thank you for your fast support and accurate descriptions. Much appreciated.</p>

---
