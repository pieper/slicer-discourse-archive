---
topic_id: 22226
title: "Join Image Series Together"
date: 2022-03-01
url: https://discourse.slicer.org/t/22226
---

# Join image series together

**Topic ID**: 22226
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/join-image-series-together/22226

---

## Post #1 by @lmboop (2022-03-01 05:48 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.2021<br>
Expected behavior: N/A<br>
Actual behavior: N/A<br>
Due to the 50+ year age of equipment, we believe our scanner has a limit of ~230 images per series. While it is not unmanageable to work with separate series, we could greatly improve our workflow if multiple series could be combined together to create a single series.<br>
Are their any tools or extensions to allow this to happen with the raw dicom images and folder structure on loading to the slicer database?<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2022-03-01 14:38 UTC)

<p>50 year old scanner?  Can you elaborate?</p>
<blockquote>
<p>Are their any tools or extensions to allow this to happen with the raw dicom images and folder structure on loading to the slicer database?</p>
</blockquote>
<p>It’s not clear exactly what you need, but if you are willing to write some python code you can pretty easily transform your dicom files.  See the DICOMPatcher for example.</p>

---

## Post #3 by @mikebind (2022-03-01 20:04 UTC)

<p>You can definitely accomplish this using Slicer through a custom python module.  I put together a module to do a portion of what you are describing you want (the stitching together of multiple series into one joined image volume).  You might find this code helpful in pursuing your own goals.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/b3d4829966c9086909b789399d3c8b6f">
  <header class="source">

      <a href="https://gist.github.com/mikebind/b3d4829966c9086909b789399d3c8b6f" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/b3d4829966c9086909b789399d3c8b6f" target="_blank" rel="noopener">https://gist.github.com/mikebind/b3d4829966c9086909b789399d3c8b6f</a></h4>

  <h5>StitchVolumes.py</h5>
  <pre><code class="Python">import os
import unittest
import logging
import vtk, qt, ctk, slicer
import numpy as np
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# StitchVolumes</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mikebind/b3d4829966c9086909b789399d3c8b6f" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, please make sure you completely understand how it works and how it might manipulate and modify your imaging data before using it. Depending on the data supplied, this stitching can lead to shifts in physical space of imaging data by up to 1/2 voxel in any direction or, in the case of varying voxel dimensions between acquisitions to be combined, linear interpolation of voxel values which could potentially degrade image quality compared to the original uncombined images. I made a series of reasonable choices based on the data I was working with which may or may not be as reasonable in other contexts.  There is no attempt to register the different volumes together based on any overlapping regions; instead each image volume is placed in scanner space based on the DICOM positioning tags. If the patient moved between scan stations, this will lead to discontinuities.</p>
<p>Unlike your described goals, the linked code does not run automatically on DICOM import or on subfolders of a given parent folder, it operates on already-loaded images, and does not generate a stitched DICOM output (though Slicer certainly has this capability).  If you do want to use elements of the linked code and have questions about it, please feel free to ask here, and I’ll get back to you.</p>

---

## Post #4 by @lmboop (2022-03-01 23:41 UTC)

<p>Thank you for this valuable guidance.<br>
We have a Toshiba Asteion Model S4 being used in a non-medical application (concrete) , and from the DICOM image metadata acquired we see two series. Series 3 has images 1 to 230 (where the machine reached some form of internal limit and errored) , then Series 5 has images 1 to 130.<br>
All images are in fact completely sequential at 2mm slice thickness, and it appears that by manually placing all images in the one sub-folder and renaming the SeriesUID parameter for Series 5 images, then renumbering those images from 231 to 360, we get the desired result.<br>
I would be very interested to hear from anyone who has specific experience with this model of scanner, as I’m sure there are plenty of things we haven’t found out yet…<br>
Kind Regards<br>
Pat</p>

---

## Post #5 by @lassoan (2022-10-20 15:09 UTC)

<p>Just in case somebody comes across this topic now: <a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for stitching multiple volumes into one. It is available in Sandbox extension.</p>

---
