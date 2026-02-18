# Automate thresholding w. unknown values - Max Entropy (Python)

**Topic ID**: 39443
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/automate-thresholding-w-unknown-values-max-entropy-python/39443

---

## Post #1 by @mhal0018 (2024-09-30 02:52 UTC)

<p>Hey there. I’m currently building a script to segment aneurysms and surrounding blood vessels from CT scans. I have successfully created a modular python script that completes the entire process from importing PNGs, applying filters, create segmentation editor and volume nodes, global thresholding, island effects, smoothing, saving of STL etc. However, I’m currently hard coding threshold min/max values in - see the function I created below.</p>
<pre><code class="lang-auto">def globalThresholding(segmentEditorWidget, minThresh, maxThresh):

  # Apply thresholding
  print("Applying Global Thresholding...")
  segmentEditorWidget.setActiveEffectByName("Threshold")   
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("MinimumThreshold", f"{minThresh}")
  effect.setParameter("MaximumThreshold", f"{maxThresh}")
  effect.self().onApply()
  print("Thresholding Complete")
  
  return 
</code></pre>
<p>I’ve found, that using the automatic thresholding method <strong>Maximum Entropy</strong> is sufficient for my needs. I’ve found a couple forum posts about how to implement this and have followed. However regardless of the method I use (yen/max entropy etc), it just doesn’t work and returns a solid cube as the segemented volume. This is the function I created.</p>
<pre><code class="lang-auto">
def globalThresholdingMaxEntropy(segmentEditorWidget):
  # Apply thresholding
  print(“Applying Global Thresholding…”)
  segmentEditorWidget.setActiveEffectByName(“Threshold”)
  effect = segmentEditorWidget.activeEffect()
  
  # if effect is not None:
  # Set the thresholding method to Yen's method
  effect.setParameter("AutomaticThresholdMethod", "MaximumEntropy")
  effect.setParameter("ThresholdType", "Above")
  effect.self().onApply()
  print("Thresholding Complete using MaximumEntropy's method")
  
  return 
</code></pre>
<p>Could someone please help me figure out why this is the case and how I can fix this? Is it a bug?</p>
<p>Or, could someone suggest another method where the threshold values are unknown. I have considered using histograms of the pixel intensities but there doesn’t seem to be a sufficient pattern. Ideally, when I segment manually, I use local thresholding.</p>

---

## Post #2 by @cpinter (2024-09-30 14:05 UTC)

<p>One issue that I see is that the name of the parameter is incorrect. It should be <code>AutoThresholdMode</code>.</p>
<p>I suggest looking at the code of the Threshold effect to find out more about the parameters it uses</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py</a></h4>


      <pre><code class="lang-py">import logging
import os

import ctk
import vtk
import qt

import slicer
from SegmentEditorEffects import *

from slicer.i18n import tr as _


class SegmentEditorThresholdEffect(AbstractScriptedSegmentEditorEffect):
    """ThresholdEffect is an Effect implementing the global threshold
    operation in the segment editor

    This is also an example for scripted effects, and some methods have no
    function. The methods that are not needed (i.e. the default implementation in
    qSlicerSegmentEditorAbstractEffect is satisfactory) can simply be omitted.
</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
