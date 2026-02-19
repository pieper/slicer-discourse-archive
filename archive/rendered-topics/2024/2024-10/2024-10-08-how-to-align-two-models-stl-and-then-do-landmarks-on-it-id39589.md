---
topic_id: 39589
title: "How To Align Two Models Stl And Then Do Landmarks On It"
date: 2024-10-08
url: https://discourse.slicer.org/t/39589
---

# How to align two models (stl) and then do landmarks on it? 

**Topic ID**: 39589
**Date**: 2024-10-08
**URL**: https://discourse.slicer.org/t/how-to-align-two-models-stl-and-then-do-landmarks-on-it/39589

---

## Post #1 by @Puja_Ghosh (2024-10-08 20:27 UTC)

<p>I have two models(stl) of torso (pregnant) and I am trying to align them one after another (superimpose) and then I want to do landmarks on the specific points where there are electrodes placed (checking position of electrodes from both the files) ?</p>

---

## Post #2 by @muratmaga (2024-10-08 20:49 UTC)

<p>You don’t really need to align the models if you just want to landmark them.</p>
<p>But if you do, you can use the <code>FastModelAlign</code> to rigidly register one model to the other, and then you can do the landmarks on the rigidly registered model.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/FastModelAlign" target="_blank" rel="noopener nofollow ugc">Tutorials/FastModelAlign at main · SlicerMorph/Tutorials</a></h3>


  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Puja_Ghosh (2024-10-08 21:03 UTC)

<p>Thank you so much Professor Maga</p>

---

## Post #4 by @Sofia_Gonzalez (2024-10-09 08:29 UTC)

<p>Someone knows how to align two models but with a code in python?</p>

---

## Post #5 by @pblascof (2025-01-17 21:57 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a>, I am super interested in aligning a batch of stl files to a target. I cannot use batch ALPACA or MALPACA directly since I do not have any reference landmarks and the PseudoLMGenerator does not do the job nicely. Is there a way to implement the FastAlignModel module in a smooth way in Python so I do not have to align all of them one by one? I would like to skip this manual work since afterwards I intend to compute a loss to decide which is the optimal source mesh to do the alignment to. I will use that one for later generating an average shape model based on the registered ones, so I need to find the optimal registration based on the optimal source and those many comparisons would be feasible only if automating the process.</p>

---

## Post #6 by @muratmaga (2025-01-17 22:02 UTC)

<p>We really don’t have bandwidth to implement the batch mode in FastModelAlign. The source code is available and perhaps you can do and contribute back using the ALPACA as an example.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/FastModelAlign/FastModelAlign.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/FastModelAlign/FastModelAlign.py" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/FastModelAlign/FastModelAlign.py" target="_blank" rel="noopener nofollow ugc">FastModelAlign/FastModelAlign.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/FastModelAlign/FastModelAlign.py" rel="noopener nofollow ugc"><code>master</code></a>
</div>


      <pre><code class="lang-py">import logging
import os

import vtk

import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin


#
# FastModelAlign
#

class FastModelAlign(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/FastModelAlign/FastModelAlign.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py" target="_blank" rel="noopener nofollow ugc">ALPACA/ALPACA.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py" rel="noopener nofollow ugc"><code>master</code></a>
</div>


      <pre><code class="lang-py">##BASE PYTHON
import os
import unittest
import logging
import copy
import json
import subprocess
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
import glob
import vtk.util.numpy_support as vtk_np
import numpy as np
from datetime import datetime
import time
import sys
import os
import platform
import math

#
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ALPACA/ALPACA.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
