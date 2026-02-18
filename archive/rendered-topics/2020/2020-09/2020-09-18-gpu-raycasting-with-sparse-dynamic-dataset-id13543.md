# GPU raycasting with sparse dynamic dataset

**Topic ID**: 13543
**Date**: 2020-09-18
**URL**: https://discourse.slicer.org/t/gpu-raycasting-with-sparse-dynamic-dataset/13543

---

## Post #1 by @Zerfox (2020-09-18 11:49 UTC)

<p>Dear all,</p>
<p><strong>First some background information:</strong> I have implemented a so-called visitation map, which is a 3D grid of voxels where each voxel/cell stores a certain frequency. The visitation map is very sparse and the cells are continuously being updated in the background. My goal is to render the dataset at interactive rates and use some custom shaders.</p>
<p>So far I have implemented this using <code>vtkImageData</code> with an auxiliary datastructure for bookkeeping. The <code>vtkImageData</code> is pushed to the GPU, which is running shaders that were inspired by <code>vtkOpenGLGPUVolumeRayCastMapper</code>.</p>
<p>This works great, and I am really satisfied with the results I am getting.</p>
<p><strong>Now the problem:</strong> the current approach will not work in my real world use-case, as <code>vtkImageData</code> requires a priori knowledge on its dimensions. I can make a rough overestimation on these dimensions, but since the dataset is very sparse it results in very high memory consumption and unworkable frame rates.</p>
<p>Using a data structure such as an Octree would be nice, but I was not able to find any existing built-in solution for Slicer/VTK that I could immediately use on the GPU. I assumed this would exist given their popularity, however. Can anyone point me in the right direction? Or are there any Slicer extensions that I could use?</p>
<p>I have looked around and found that I might be able to ‘abuse’ <code>vtkPolyData</code> to store my sparse dataset, and then convert this to a <code>vtkImageData</code> to send of to the GPU. Although I still need to figure out how to do this, my feeling is that this will not be very efficient. The polydata would get updated numerous times per second and the generated <code>vtkImageData</code> might still be quite large to send over every time to the shader. I was wondering if there are any solutions available in Slicer or VTK that I can use.</p>
<p>If something like this is not (yet) possible and I’ll have to make it work myself that will be reassuring to know before I’ll continue. In that case I’ll probably go for implementing a visitation map based on Octrees on the GPU to work around it altogether.</p>
<p>I hope someone can give a small hint with some more material on this area. Thanks in advance!</p>
<p>Kind regards,<br>
Rutger</p>

---

## Post #2 by @lassoan (2020-09-18 14:09 UTC)

<p>VTK offers many solutions for this kind of visualization tasks and all of them can be used in Slicer. Probably the <a href="https://discourse.vtk.org/">VTK forum</a> would be a better fit for this question but I can give you a few tips here:</p>
<ul>
<li>Probably the most compact and lossless representation of your data is a point set, so try to stick to that.</li>
<li>For approximate visualization you can use point glyphs (e.g., by using the GPU-accelerated <a href="https://vtk.org/doc/nightly/html/classvtkGlyph3DMapper.html">vtkGlyph3DMapper</a>) (see for example Figure 9 in <a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Harish2016a.pdf">this paper</a> where we used 3D visitation map to show where our optical/EM tracking error inspector tool collected data).</li>
<li>For accurate opacity mapping you probably need to use volume rendering. You can generate volume from your point set anytime using splatting (<a href="https://vtk.org/doc/nightly/html/classvtkGaussianSplatter.html">Gaussian</a> or <a href="https://vtk.org/doc/nightly/html/classvtkCheckerboardSplatter.html">checkerboard</a>).</li>
<li>If you find that updates are slowing down as you have increasingly more points, you can collect new points in a separate point set. Once the point set reaches a size that updates are starting to slow down (probably after 10k-100k points) then move those points to a separate actor or merge them with the previously acquired points.</li>
</ul>

---

## Post #3 by @Zerfox (2020-09-18 16:57 UTC)

<p>Hi Andras,</p>
<p>Thank you for your quick answer! You are totally right: I should have asked this question on the VTK forum, I must have misread which forum I was asking my question on.</p>
<p>I’m looking to construct smooth isosurfaces from the visitation map and wrote my own splat function already, so I think refactoring my code to use a point set and using VTK’s built-in splatters makes the most sense.</p>
<p>I’ll have a good look and if I have further questions I will ask them on the VTK forums.</p>
<p>Have a good weekend,<br>
Rutger</p>

---
