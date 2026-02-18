# SlicerExtension-VMTK - VesselnessFiltering - Code

**Topic ID**: 9306
**Date**: 2019-11-26
**URL**: https://discourse.slicer.org/t/slicerextension-vmtk-vesselnessfiltering-code/9306

---

## Post #1 by @marie (2019-11-26 20:26 UTC)

<p>Hey there!</p>
<p>I would like to understand how VesselnessFiltering is working in general. So, I’m looking at:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py" target="_blank" rel="nofollow noopener">vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py</a></h4>
<pre><code class="lang-py"># slicer imports
import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# Vesselness Filtering using VMTK based Tools
#

class VesselnessFiltering(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
    self.parent.title = "Vesselness Filtering"
    self.parent.categories = ["Vascular Modeling Toolkit"]
</code></pre>

  This file has been truncated. <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I see how the internal parameters are generated from the inputInformation and the inputImage, but I still don’t know that much about the vtkvmtkSegmentationPython module. I found this page: <a href="http://www.vmtk.org/doc/html/classvtkvmtkVesselnessMeasureImageFilter.html#details" rel="nofollow noopener">http://www.vmtk.org/doc/html/classvtkvmtkVesselnessMeasureImageFilter.html#details</a> and I have been looking for a more detailed vtk manual…</p>
<p>anyway, I still don’t understand what kind of parameters all those vtk-methods expect (apart from type) and what they are needed for. I would like to understand why the internal parameters (diameter, alpha, beta,…) are calculated like that. Is there something like a detailed example or an user documentation?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2019-11-26 20:39 UTC)

<p>Yes, this exactly the main problem with VMTK: there is nearly zero API documentation. You can ask about the parameters on the VMTK mailing list then write what you learn to documentation of the corresponding class in VMTK (they accept pull requests).</p>

---

## Post #3 by @marie (2019-11-26 20:47 UTC)

<p>Okay, thanks! I will try… let’s see what I can figure out <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
