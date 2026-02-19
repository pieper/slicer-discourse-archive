---
topic_id: 3846
title: "Vtk Fiber Bundle Import From Mrtrix And Or Good Format Descr"
date: 2018-08-20
url: https://discourse.slicer.org/t/3846
---

# Vtk fiber bundle import from mrtrix and/or good format description of the slicer polydata fiber bundle format

**Topic ID**: 3846
**Date**: 2018-08-20
**URL**: https://discourse.slicer.org/t/vtk-fiber-bundle-import-from-mrtrix-and-or-good-format-description-of-the-slicer-polydata-fiber-bundle-format/3846

---

## Post #1 by @UNSW_MRI (2018-08-20 13:23 UTC)

<p>Hi,<br>
I was wondering if there is a good description of the vtk polydata format of the slicer fiber bundles?<br>
I currently have the following problem: When I use MRtrix for fiber tracking and convert the tracts to vtk polydata, Slicer imports the data just fine BUT I cannot use FA or orientaion based coloring. I guess this is stored in some place with the polydata of the fibre bundles, but I cannot find any documantation form that. Can anybody give me a hint how I can properly import this and add this information to the fiber bundles, so I can user these color schemes? Maybe there is a conversion step I am missing?</p>
<p>Thanks</p>
<p>Andre</p>

---

## Post #2 by @ihnorton (2018-08-20 15:07 UTC)

<p>Hi Andre,</p>
<aside class="quote no-group" data-username="UNSW_MRI" data-post="1" data-topic="3846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/u/ed655f/48.png" class="avatar"> UNSW_MRI:</div>
<blockquote>
<p>BUT I cannot use FA or orientaion based coloring. I guess this is stored in some place with the polydata of the fibre bundles, but I cannot find any documantation form that.</p>
</blockquote>
</aside>
<p>There are two options available.</p>
<ul>
<li>
<p>The fiber bundle VTK files can store an ordered array of tensors in a VTK cell array, with one tensor corresponding to each point. The visualization pipeline within Slicer then calculates the property requested for display on-the-fly from the tensors.</p>
<p>Each component of the cell array is a 9-tuple (9 elements), corresponding to the upper 9 components of the symmetric matrix representing the tensor.</p>
<p>From a quick look at the thread below, I think MRtrix tools are available to sample scalars from images, not tensors, so such an export option may not be available. But, if you know how to get tensors from MRtrix and want to pursue this scheme, let me know and I’ll send more information about the format.</p>
</li>
</ul>
<aside class="onebox discoursetopic" data-onebox-src="https://community.mrtrix.org/t/along-tract-analysis-after-tract-segmentation/1007/3">
  <header class="source">
      <img src="https://community.mrtrix.org/uploads/default/optimized/2X/5/5a141e867cdef5b8247f929cbfd88191a5a6da05_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://community.mrtrix.org/t/along-tract-analysis-after-tract-segmentation/1007/3" target="_blank" rel="noopener" title="11:26AM - 05 July 2017">MRtrix3 Community – 5 Jul 17</a>
  </header>

  <article class="onebox-body">
    <img src="https://community.mrtrix.org/uploads/default/original/2X/7/75b1ba7b1622a349252608c59eb89a88db4a8c27.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://community.mrtrix.org/t/along-tract-analysis-after-tract-segmentation/1007/3" target="_blank" rel="noopener">Along tract analysis after tract segmentation</a></h3>
</div>

  <p>Just in case you want to use the MRtrix3 functionality here, the commands you’re after are tcksample and tckresample. These admittedly need to be better documented.  The process consists of first re-sampling the streamlines at equivalent locations...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<ul>
<li>The second, probably simpler/tractable option, is to store pre-computed scalars, similarly in a polydata cell array, but this time with a single scalar value per point. After using the method detailed in the post above, the output text file could be loaded and added to the VTK as a cell array with (hopefully) a few lines of Python code.</li>
</ul>

---

## Post #3 by @ljod (2018-08-20 15:08 UTC)

<p>Hi the FA can only be shown if tensors (or FA) are stored along the fibers. This data would have to come from MRtrix, but as far as I know it does not store tensors. The orientation coloring should still work, as that requires only the fibers. Did you go to Tractography Display and turn the color by orientation on?</p>

---
