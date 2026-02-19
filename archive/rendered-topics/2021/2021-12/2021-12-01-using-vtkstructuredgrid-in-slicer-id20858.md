---
topic_id: 20858
title: "Using Vtkstructuredgrid In Slicer"
date: 2021-12-01
url: https://discourse.slicer.org/t/20858
---

# Using `vtkStructuredGrid` in Slicer

**Topic ID**: 20858
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/using-vtkstructuredgrid-in-slicer/20858

---

## Post #1 by @keri (2021-12-01 03:00 UTC)

<p>Hi,</p>
<p>Just wondering does Slicer support <code>vtkStructuredGrid</code>? I can’t find any information on that</p>

---

## Post #2 by @lassoan (2021-12-01 15:04 UTC)

<p>Working directly with structured grids could be hard because I think most VTK filters and mappers do not support it.</p>
<p>Would you like to manage images with varying spacing? Slicer supports that via storing an image with uniform spacing and applying a non-linear transform that moves each slice to the correct physical location.</p>
<p>You can also convert your structured grid to an unstructured grid (volumetric mesh) with scalar value associated with each point. Cross-sections can be displayed in slice views and outer surface (some internal surfaces as well, if clipping planes are used) can be displayed in 3D views.</p>

---

## Post #3 by @keri (2021-12-01 15:55 UTC)

<p>Thank you for response,</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would you like to manage images with varying spacing?</p>
</blockquote>
</aside>
<p>I’m still struggling with volumetric <a href="https://discourse.vtk.org/t/writing-custom-class-based-on-vtkdataset/6950" rel="noopener nofollow ugc">data that is arbitrary spaced in the XY plane but has uniform Z spacings</a><br>
Even <code>vtkStructuredGrid</code> is not a good choice for me.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer supports that via storing an image with uniform spacing and applying a non-linear transform that moves each slice to the correct physical location.</p>
</blockquote>
</aside>
<p>Didn’t think about that, probably I need to investigate nonlinear transformations.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also convert your structured grid to an unstructured grid (volumetric mesh) with scalar value associated with each point.</p>
</blockquote>
</aside>
<p>Unstructured grid is a possible solution but has a drawback that it consumes RAM. I think I will implement that for visualizing relatively small datasets (I also like <code>vtkExplicitStructuredGrid</code> but that is not a nearest task).</p>
<p>But for general case when the data is pretty big I created custom dataset <a href="https://github.com/tierra-colada/Colada/tree/master/Applications/Libs/vtkEigen" rel="noopener nofollow ugc">vtkRaisedGrid</a> that stores only XY points (triangulated with <code>vtkDelaunay2D</code>) and Z spacings vector. I guess it is partly implicit grid. To display the data in Slicer I interpolate point scalars on <code>vtkImageData</code> via <code>vtkProbeFilter</code>. It takes some time to do that but I hope when working in release mode with TBB enabled the perfomance will be few times higher.</p>
<p>The problem has arised when I started testing it on real data and I’ve got some bugs when probing my custom dataset on <code>vtkImageData</code>:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9dbb4f383213e91cdd720b35b0bc39c7c52200de.jpeg" alt="image" data-base62-sha1="mvmgPGbjMNoxLYcKTYPQpCVgpwG" width="626" height="380"></p>
<p>I’ve looked to the source code of <code>vtkProbeFilter</code> and it seems that when probing on <code>vtkImageData</code> it works very efficiently: for each cell of source data it probes all cells (or points I don’t remember) of image data that are within that source cell. Most likely the problem is in my implementation of my dataset or the way <code>vtkDelaunay2D</code> works.</p>

---

## Post #4 by @lassoan (2021-12-01 19:08 UTC)

<p>If the topology of your data set is the same as an image volume (you can index points using IJK coordinates) and just geometry is different (the physical coordinate of each point is arbitrary) then using an image data with a warping transform should work well. You can specify physical location of each point using a vtkOrientedGridTransform.</p>

---

## Post #5 by @keri (2021-12-02 17:42 UTC)

<p>Thank you for the help,</p>
<p>Unfortunately in general case I can’t use IJK indexing. I will keep in mind <code>vtkOrientedGridTransform</code></p>
<p>But I have found bug in my custom vtk dataset: the method <code>MyDataset::GetCell()</code> that is supposed to be thread safe was not that. So I fixed that and now vtk probing from my dataset on <code>vtkImageData</code> works pretty fast with TBB enabled.</p>
<p>Also I implemented loading my data using <code>vtkUnstructuredGrid</code>.<br>
If the actual size of my data (scalar values) is 20 Mb, then Clipping Planes (from Models module) is very slow (probably 30-40 sec to clip) in DEBUG mode. Though that is not the primary task for now, I mostly rely on <code>vtkImageData</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b052b164f02081dd00284488faa017e42283b15.jpeg" data-download-href="/uploads/short-url/3R1XOvKCJfWCIFSzyym3iPqb20B.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b052b164f02081dd00284488faa017e42283b15_2_690x259.jpeg" alt="image" data-base62-sha1="3R1XOvKCJfWCIFSzyym3iPqb20B" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1b052b164f02081dd00284488faa017e42283b15_2_690x259.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b052b164f02081dd00284488faa017e42283b15.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b052b164f02081dd00284488faa017e42283b15.jpeg 2x" data-dominant-color="819698"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">810×305 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-12-02 18:31 UTC)

<aside class="quote no-group" data-username="keri" data-post="5" data-topic="20858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Also I implemented loading my data using <code>vtkUnstructuredGrid</code> .<br>
If the actual size of my data (scalar values) is 20 Mb, then Clipping Planes (from Models module) is very slow (probably 30-40 sec to clip) in DEBUG mode. Though that is not the primary task for now, I mostly rely on <code>vtkImageData</code></p>
</blockquote>
</aside>
<p>Performance in debug mode can be 10-100x slower, so don’t make any judgement based on debug-mode tests. Nevertheless, if you have dense data then resampling on a regular grid (resulting in a vtkImageData) makes a lot of sense, as it can make processing and visualization magnitudes faster.</p>

---
