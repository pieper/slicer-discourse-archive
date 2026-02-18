# Animating Spheres (or markups) Using Sequencer

**Topic ID**: 41494
**Date**: 2025-02-04
**URL**: https://discourse.slicer.org/t/animating-spheres-or-markups-using-sequencer/41494

---

## Post #1 by @mrsh0r3s (2025-02-04 16:29 UTC)

<p>Hello,</p>
<p>I am trying to animate some markers in slicer. Basically, I want a bunch of spheres that change sizes and colors as time progresses. I did some digging and reached the conclusion that the parameters of markup control points cannot be changed individually (you seem to have to change the entire list) so I thought I could work around that by making a bunch of sphere models with the vtkSphereSource node and place them at each markup point and animating that.</p>
<p>I have 128 independent control points for which I have already calculated the relative position (in Python) and absolute position in 3D space (in Slicer) to yield 2 separate point lists as markup nodes. I also have the RGB values I want each point to have at each frame (in Python) and the relative size I want each point to have at each frame (also in Python). I also can make a sphere model in code for the most part.</p>
<p>I just cannot for the life of me understand the sequencer. I’m starting to think it wants each frame of each point imported as a separate object? With 128 points over many frames, that will get unwieldy fast. I am missing how I can click the play button in the sequencer and play through my colors/ sizes of points. If I need to limit myself to loading just a small subset of frames, that is also fine since I have over a hundred points and many thousand potential frames. I don’t even mind just reading the data from Python - I just don’t understand how I can make a timeline of indices, access them in code, and update either markups or vtkspheres when I click play. The timeline and play/stop functionality is what I care about the most here.</p>
<p>Any insight you all have would be helpful.</p>

---

## Post #2 by @pieper (2025-02-10 23:18 UTC)

<p>You could just make a VTK pipeline to create the spheres and colors you want at each frame. You may want to look at the Animator module in SlicerMorph for ideas this approach integrates with Sequences.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py" target="_blank" rel="noopener">Animator/Animator.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py" rel="noopener"><code>master</code></a>
</div>


      <pre><code class="lang-py">import json
import logging
import math
import os
import unittest
import uuid
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging

#
# action classes
#
class AnimatorAction:
  """Superclass for actions to be animated."""
  def __init__(self):
    self.uuid = uuid.uuid4()

  def cleanup(self, action):
    """Called when the action is deleted"""
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/Animator/Animator.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
