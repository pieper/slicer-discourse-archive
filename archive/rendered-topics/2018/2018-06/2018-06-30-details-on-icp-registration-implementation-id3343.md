---
topic_id: 3343
title: "Details On Icp Registration Implementation"
date: 2018-06-30
url: https://discourse.slicer.org/t/3343
---

# Details on ICP registration implementation

**Topic ID**: 3343
**Date**: 2018-06-30
**URL**: https://discourse.slicer.org/t/details-on-icp-registration-implementation/3343

---

## Post #1 by @odiseo123 (2018-06-30 10:40 UTC)

<p>Operating system: Windows 7 64bits<br>
Slicer version: 4.8.1<br>
Expected behavior: N/A<br>
Actual behavior: N/A</p>
<p>I am using the surface registration module with “Surface Registration” as “Type of Registration”. I just wanted some extra information about it:<br>
*Is the registration algorithm a pure ICP method, i.e. it aligns points WITHOUT considering normals or curvature?<br>
*Is the “Number Of Landmarks” the number of points sampled from the mesh surface? Is the sampling done randomly?</p>
<p>Thanks a lot for your help.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-07-01 13:48 UTC)

<p>Hi,</p>
<p>The Surface Registration module which is part of the CMFreg extension uses vtkIterativeClosestPointTransform. You can look into the details in the following links.</p>
<p>Surface registration python script<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py" target="_blank" rel="nofollow noopener">DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py</a></h4>
<pre><code class="lang-py">import os
from __main__ import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import time
import numpy
import json

#
# SurfaceRegistration
#

class SurfaceRegistration(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Surface Registration"
</code></pre>

  This file has been truncated. <a href="https://github.com/DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>vtkIterativeClosestPointTransform<br>
<a href="https://www.vtk.org/doc/nightly/html/classvtkIterativeClosestPointTransform.html#details" class="onebox" target="_blank" rel="nofollow noopener">https://www.vtk.org/doc/nightly/html/classvtkIterativeClosestPointTransform.html#details</a></p>
<p>HTH,<br>
Andinet</p>

---
