# Watershed segmentation

**Topic ID**: 15499
**Date**: 2021-01-13
**URL**: https://discourse.slicer.org/t/watershed-segmentation/15499

---

## Post #1 by @Ester_RG (2021-01-13 11:57 UTC)

<p>Hi there! I would like to know how Watershed algorithm computes on 3D images, like CT images using Segment Editor extension. Does it go through every 2D layer on the register or does it computes all the image register? Some repository where I can found the code?</p>
<p>Thank you so much!</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-01-13 12:33 UTC)

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py</a></h4>
<pre><code class="lang-py">import os
import vtk, qt, ctk, slicer
import logging
from SegmentEditorEffects import *

class SegmentEditorEffect(AbstractScriptedSegmentEditorAutoCompleteEffect):
  """This effect uses Watershed algorithm to partition the input volume"""

  def __init__(self, scriptedEffect):
    AbstractScriptedSegmentEditorAutoCompleteEffect.__init__(self, scriptedEffect)
    scriptedEffect.name = 'Watershed'
    self.minimumNumberOfSegments = 2
    self.clippedMasterImageDataRequired = True # master volume intensities are used by this effect
    self.growCutFilter = None

  def clone(self):
    import qSlicerSegmentationsEditorEffectsPythonQt as effects
    clonedEffect = effects.qSlicerSegmentEditorScriptedEffect(None)
    clonedEffect.setPythonSource(__file__.replace('\\','/'))
    return clonedEffect
</code></pre>

  This file has been truncated. <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorWatershed/SegmentEditorWatershedLib/SegmentEditorEffect.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
