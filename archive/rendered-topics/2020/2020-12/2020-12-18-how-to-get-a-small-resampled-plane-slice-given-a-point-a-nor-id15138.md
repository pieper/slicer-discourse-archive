---
topic_id: 15138
title: "How To Get A Small Resampled Plane Slice Given A Point A Nor"
date: 2020-12-18
url: https://discourse.slicer.org/t/15138
---

# How to get a small resampled plane slice given a point, a normal, and slice dimensions?

**Topic ID**: 15138
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/how-to-get-a-small-resampled-plane-slice-given-a-point-a-normal-and-slice-dimensions/15138

---

## Post #1 by @mikebind (2020-12-18 23:09 UTC)

<p>I would like to be able to get a resampled image slice as a numpy array by supplying a slice center (in RAS coord), slice dimensions and resolution (e.g. 50x50 pixels which are 1 mm x 1 mm), a slice normal vector, and a slice view-up vector.  From looking at the Curved Planar Reformat module code, I was able to put together a function which will produce a reformatted volume where the slices of the straightened volume are almost what I want, except that it requires a curve as input (rather than just a point and vectors), does not allow control of the viewUp vector (I assume because it is calculated automatically from the curve?), and outputs a volume rather than a single image array.</p>
<p>What I want to be able to do is obviously exactly what is happening in slice viewers when in reformat mode, but I have not been able to find the code which actually does the resampling work based on the inputs, probably because I have trouble following C++ code around in the Slicer GitHub repository.  I see things like vtkSlicerReformatLogic::SetSliceNormal() which seems related, but it’s more modifying the state of a continuously existing object (a slice node I think) than linking a specific set of inputs to a specific resampled image output slice, which is what I am trying to do.</p>
<p>Both of these examples (the Reformat and CurvedPlanarReformat modules) make it seem like what I want is probably already doable within Slicer without me trying to write code from scratch to do the resampling I want, but I could use some help figuring out how to use or modify the existing tools.  Thanks for any help you can provide!</p>

---

## Post #2 by @lassoan (2020-12-18 23:46 UTC)

<p>You can use <code>SetSliceToRASByNTP</code> as a convenient way to set slice position by specifying normal and x axis direction and slice position. See example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_a_normal_vector_and_position">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Set_slice_position_and_orientation_from_a_normal_vector_and_position</a></p>
<p>If you don’t want to use the slice viewer for this then you can create a single-slice volume with the desired dimensions, zero-centered, axis-aligned, then transform it to the desired position and orientation, and use it as a reference volume in an image resample module.</p>

---

## Post #3 by @mikebind (2020-12-18 23:52 UTC)

<p>Thanks, I think this will work fine for my purposes.  I’ll take over the Red slice node, temporarily set the background volume to the volume I want to resample, use SetSliceToRASByNTP to orient the slice, and then grab the image array from the slice (which I see there is also code for in the script repository).  Is there a way to control the pixel size of the extracted slice?  It’s great if there is, but if not, I can just resample the 2D image to the desired resolution.</p>

---

## Post #4 by @pieper (2020-12-19 00:01 UTC)

<p>I had an example lying around that extracts randomly oriented samples from a volume.  It shows how to set the dimensions and orientation.  It’s no in the script repository.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Extract_randomly_oriented_slabs_of_given_shape_from_a_volume" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Extract_randomly_oriented_slabs_of_given_shape_from_a_volume" target="_blank" rel="noopener">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
