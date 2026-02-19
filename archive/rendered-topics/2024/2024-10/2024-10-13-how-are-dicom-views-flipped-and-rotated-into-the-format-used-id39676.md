---
topic_id: 39676
title: "How Are Dicom Views Flipped And Rotated Into The Format Used"
date: 2024-10-13
url: https://discourse.slicer.org/t/39676
---

# How are dicom views flipped and rotated into the format used in 3d slicer?

**Topic ID**: 39676
**Date**: 2024-10-13
**URL**: https://discourse.slicer.org/t/how-are-dicom-views-flipped-and-rotated-into-the-format-used-in-3d-slicer/39676

---

## Post #1 by @dj_96 (2024-10-13 16:24 UTC)

<p>In my own code when I load a dicom series with pydicom the slices are not necessarily in correct order and the 3 views are often flipped or rotated in a strange way. 3d Slicer seems to always correct it to a standard format where axial is anterior up, sagittal and coronal are superior up, inferior down etc…</p>
<p>Is this specific to slicer or do itk/vtk have some functionality for fixing the orientation of the views to a standard format. The other thing I’m doing is when adding a marker to a ct view it displays it on the 3d model in the RCS coordinate and vice versa. This seems to work perfectly in slicer when adding a point.</p>
<p>I wanted to know if there’s some scripts or samples from slicer or one of the libraries that handles this so I can use it in a small ct/3d model viewer that loads ct views in a standard format and correlates a point placed on either ct or 3d model to each other like in slicer.</p>

---

## Post #2 by @pieper (2024-10-13 18:03 UTC)

<p>DICOM management in general is a complex task.  You are free to look through the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/DICOM">Slicer source code</a> to see how it’s handled and also to read the documentation.  For example <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">here</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">here</a>.</p>
<p>Creating your own “simple” viewer seems nice in concept, but debugging and ongoing maintenance may be more trouble than it’s worth.  We typically suggest instead that such time and effort goes into <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html">Slicer extensions</a> or <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">custom Slicer applications</a> so that you take advantage of existing code that already works and ongoing community efforts.</p>

---

## Post #3 by @dj_96 (2024-10-13 18:16 UTC)

<p>Thanks, in my case it’s already embedded into a larger codebase so I don’t really have the option of extending slicer anymore so I was wondering more if I could pull some code from slicer just to fix this since the viewer is already made I’m just having issues handling the dicom orientations and conversion to 3d model coordinates. If I just run a dicom sample through slicer first before loading into my app everything works pretty well since Slicer must already do some correction so that views are in a consistent orientation.</p>
<p>I’m currently just reading with pydicom and displaying ct with pyqt and the model with vtk. Does ITK have some useful functionality for this instead or is most of it within Slicer exclusively because maybe that’s actually more practical?</p>

---

## Post #4 by @pieper (2024-10-13 18:47 UTC)

<p>You can have a look at this code that uses ITK-based methods plus some custom logic to handle complex cases.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py</a></h4>


      <pre><code class="lang-py">import logging
from functools import cmp_to_key

import ctk
import numpy
import qt
import vtk
import vtkITK
from slicer.i18n import tr as _

import slicer

from DICOMLib import DICOMPlugin
from DICOMLib import DICOMLoadable
from DICOMLib import DICOMUtils
from DICOMLib import DICOMExportScalarVolume


#
# This is the plugin to handle translation of scalar volumes
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We’ve requested funding to factor this code out into python packages that would be easier to reuse, but for now they are part of the application.</p>

---
