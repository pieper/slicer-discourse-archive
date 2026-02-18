# Specifying coordinate system in surface mesh file

**Topic ID**: 724
**Date**: 2017-07-20
**URL**: https://discourse.slicer.org/t/specifying-coordinate-system-in-surface-mesh-file/724

---

## Post #1 by @chribaue (2017-07-20 13:35 UTC)

<p>Hi,</p>
<p>I have a related question regarding file formats and coordinate systems.</p>
<p>We’re having 3d images and models (meshes) that are generated with ITK. We promised to publish the data such that it’s compatible with ITK and currently store the images as .mha files and the meshes as .vtk files.</p>
<p>However, when others want to view the data with Slicer one has to transform either the mesh or the volume so that they align.</p>
<p>Is there a way to store image volumes and corresponding meshes so that they align in ITK and Slicer?</p>
<p>Best,<br>
Christian</p>

---

## Post #2 by @pieper (2017-07-20 14:42 UTC)

<p>I would say the best would be to provide an ITK code example that applies the transform after the reader step.  As <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/fedorov">@fedorov</a> mentioned, there’s no accepted standard to represent the coordinate system of polydata formats except in dicom (to our knowledge).</p>
<p>On the other hand, a basic dicom surface segmentation format is relatively simple, so it could be easiest to add support for that.  Surface segmentations are not widely used they are standard and perhaps we should encourage the use of it.</p>
<p>I did a prototype of a surface segmentation reader for Slicer but didn’t have any public sample data so I never finished it.  I did work for the data I had.  I think it would be feasible to do something similar for ITK and also create a basic exporter for both system.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py</a></h4>
<pre><code class="lang-py">import glob, os, json
from datetime import datetime
import string
import vtk, qt, ctk, slicer
from DICOMLib import DICOMPlugin
from DICOMLib import DICOMLoadable
import logging

#
# This is the plugin to handle translation of DICOM Surface SEG objects
#

class DICOMSurfaceSegmentationPluginClass(DICOMPlugin):

  def __init__(self,epsilon=0.01):
    super(DICOMSurfaceSegmentationPluginClass,self).__init__()
    self.loadType = "DICOMSurfaceSegmentation"

    self.surfaceSegmentationSOPClassUID = "1.2.840.10008.5.1.4.1.1.66.5"

</code></pre>

  This file has been truncated. <a href="https://github.com/pieper/QuantitativeReporting/blob/add-surface-seg/Py/DICOMSurfaceSegmentationPlugin.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2017-07-20 14:43 UTC)

<p>It would be great to finally solve this annoying issue.</p>
<p>I would try to add a custom tag in the header of the mesh file that follows how anatomical orientation is already specified in a well-established file format. For example, we could use <a href="http://teem.sourceforge.net/nrrd/format.html#space">NRRD format’s <code>space</code> attribute</a>: <code>space: left-posterior-superior</code>.</p>
<p>Using some DICOM definition would be nice, too, but I think <a href="https://www.dabsoft.ch/dicom/3/C.7.6.2.1.1/">in DICOM the space is LPS by definition</a>, so I’m not sure if there is a way to specify other anatomical orientations.</p>
<p>It would depend on each file format how this metadata could be stored. For example, in STL there is a comment line and there are <a href="https://en.wikipedia.org/wiki/STL_%28file_format%29#Color_in_binary_STL">examples how to store additional metadata</a>.</p>
<p>While we are at it, it might be useful to also add a unit field. As in medical imaging everybody uses mm, but if you export from CAD software, blender, etc. then sometimes the unit is m, inch, 1/10 inch, etc.</p>

---

## Post #4 by @lassoan (2017-07-20 14:47 UTC)

<p>I agree, it would be great to add the ability to save/load DICOM surface segmentation objects. For the next 10-20 years we also need to offer robust saving/loading of other commonly formats (STL, PLY, …).</p>

---

## Post #5 by @chribaue (2017-07-20 15:01 UTC)

<p>Thanks for the answers.</p>
<p>Our plan was also to explain the issue to users of the data and provide examples how to deal with it.</p>
<p>I was just hoping that there might be an off the shelf solution that doesn’t need extra explanation. It seems to be such a trivial task.</p>

---

## Post #6 by @Lorensen (2017-07-20 15:02 UTC)

<p>For vtk formats you can store anything you want in field data for the dataset. For example, I have saved color, origin and spacing.</p>

---

## Post #7 by @pieper (2017-07-20 15:03 UTC)

<p>Yes, for now adding a custom flag in the vtk metadata and some example itk import code is probably the best.</p>

---

## Post #8 by @lassoan (2017-08-04 13:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="724" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, for now adding a custom flag in the vtk metadata and some example itk import code is probably the best.</p>
</blockquote>
</aside>
<p>Added a ticket to track this task: <a href="https://issues.slicer.org/view.php?id=4408" class="inline-onebox">Save coordinate system in surface mesh file · Issue #4408 · Slicer/Slicer · GitHub</a></p>

---
