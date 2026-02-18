# Autosave option

**Topic ID**: 17025
**Date**: 2021-04-11
**URL**: https://discourse.slicer.org/t/autosave-option/17025

---

## Post #1 by @aldoSanchez (2021-04-11 02:46 UTC)

<p>hi guys I’m wondering if slicer haves autosave?<br>
its anyone that can guide me pleas or maybe use some python code for autosave</p>

---

## Post #2 by @pieper (2021-04-11 14:31 UTC)

<p>I’ve added autosave before to custom versions of Slicer and it’s not hard, just using QTimer to periodically call <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_the_scene_into_a_new_directory">code to save the scene</a>.  The drawback is that scene saving can be an expensive operation and thus can interrupt the user.  Also for some use cases large intermediate data is created would be wasteful to save in terms of time and disk space.  So for now most people just manually save periodically when they reach a good spot in their work.</p>

---

## Post #3 by @cpinter (2021-04-12 09:47 UTC)

<p>I guess people would need autosave most for segmentations and markup operations. Fast auto-save would be easy to implement on a per-node basis if we had global undo/redo working, which we do not. We do, however, have such history for segmentations. So I could imagine that after we initially save a scene (not MRB) manually, we could save the edited segmentation after each (nth) operation. The problem is that this would be a quite specific operation requiring a manual initialization step (saving the initial scene in a certain way).</p>
<p><a class="mention" href="/u/aldosanchez">@aldoSanchez</a> What type of objects do you want autosave for? If segmentations, then you could consider implementing the above with a dozen or so lines of python code.</p>

---

## Post #4 by @aldoSanchez (2021-04-20 23:06 UTC)

<p>I want to save a label map of the files that I want to save are   .mgz</p>

---

## Post #5 by @pieper (2021-04-21 00:11 UTC)

<p>There’s an AutoSave module in the Sandbox extension but I’ve never used it.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py</a></h4>
<pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
from slicer.util import VTKObservationMixin, NodeModify
import math
import time

#
# AutoSave
#

class AutoSave(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
    ScriptedLoadableModule.__init__(self, parent)
</code></pre>

  This file has been truncated. <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/AutoSave/AutoSave.py" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @aldoSanchez (2021-04-27 01:25 UTC)

<p>thanks, I’m going to try it.</p>

---
