# 3d morphometry in Version 5.1

**Topic ID**: 25674
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/3d-morphometry-in-version-5-1/25674

---

## Post #1 by @juliangallaun (2022-10-13 11:22 UTC)

<p>Hi everyone,</p>
<p>I have a rather general question, what version of 3DSlicer (4 or 5) would be preferable for 3d morphological analysis using landmarks? I saw that version 4 had an extension called SlicerMorph which is missing in version 5, if I am not mistaken.</p>
<p>I would in general appreciate extension-recommendations, for analyses using DICOM files from CT scans of oral an pharyngeal fish jaws.</p>

---

## Post #2 by @pieper (2022-10-13 14:28 UTC)

<p>You should work with the current stable release 5.0.3.  SlicerMorph is available and is the right tool for what you describe.</p>

---

## Post #3 by @muratmaga (2022-10-13 16:56 UTC)

<p>You can see installation procedures and how to run SlicerMorph here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/#installation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/#installation" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/63ed5c0c75fca34abcf250ec9515d5006b8ea408defea374d0c264850197acb8/SlicerMorph/SlicerMorph" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/#installation" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph: Extensions to conduct 3D morphometrics in...</a></h3>

  <p>Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let us know if you have questions.</p>

---

## Post #4 by @Carlos_Felipe_Lobo (2023-07-14 13:37 UTC)

<p>Hello everyone,<br>
I was looking for VolumetoModel in Utility Modules as described by Rolfe et al., 2020. I don’t know if it’s still available, it’s not mentioned in the 2021 article.<br>
Thanks for SlicerMorph <img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji" alt=":clap:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><br>
I am using Slicer 5.2.2</p>

---

## Post #5 by @muratmaga (2023-07-14 14:55 UTC)

<p>We disabled that module since it had a very fairly specific use case (segment a number of volumes with identical threshold settings and save them as models) and not generally applicable. But the source code is still available, if it is any of use to you.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/VolumeToModel/VolumeToModel.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/VolumeToModel/VolumeToModel.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/VolumeToModel/VolumeToModel.py" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/master/VolumeToModel/VolumeToModel.py</a></h4>


      <pre><code class="lang-py">import os
import unittest
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import logging
import fnmatch
import  numpy as np
import random
import math

#
# VolumeToModel
#

class VolumeToModel(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
    """

  def __init__(self, parent):
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/VolumeToModel/VolumeToModel.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Normally you would use the segment editor and then export the segmentation as a model. Or write your custom script to do the same.</p>

---

## Post #6 by @Carlos_Felipe_Lobo (2023-07-14 16:47 UTC)

<p>Thanks! Nice, I will try it out!</p>

---
