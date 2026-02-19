---
topic_id: 24363
title: "How To Run A Python File On 3D Slicer And Generate Output"
date: 2022-07-18
url: https://discourse.slicer.org/t/24363
---

# How to run a python file on 3D slicer and generate output

**Topic ID**: 24363
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/how-to-run-a-python-file-on-3d-slicer-and-generate-output/24363

---

## Post #1 by @ashuashu (2022-07-18 09:53 UTC)

<p>Operating system: macOS M1<br>
Slicer version: 5.0.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I am completely new to the 3D slicer.</p>
<p>I have my deep learning model coded in python and my dataset ready. I want to deploy it in 3D Slicer and generate outputs.</p>
<p>What is the process or commands? Any links to follow the procedure are appreciated.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2022-07-18 18:31 UTC)

<p>You can start by watching this recent webinar and reading up on the topics discussed.  You can follow up with specific questions here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="wtiEe_jiUzg" data-video-title="MONAI Label Workshop - Project Week 37" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=wtiEe_jiUzg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/wtiEe_jiUzg/maxresdefault.jpg" title="MONAI Label Workshop - Project Week 37" width="" height="">
  </a>
</div>


---

## Post #3 by @lassoan (2022-07-18 23:00 UTC)

<p>If you don’t use MONAI then you can find a complete example that brings a Pytorch-based model into Slicer:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/lassoan/SlicerHDBrainExtraction/blob/main/HDBrainExtractionTool/HDBrainExtractionTool.py">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerHDBrainExtraction/blob/main/HDBrainExtractionTool/HDBrainExtractionTool.py" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerHDBrainExtraction/blob/main/HDBrainExtractionTool/HDBrainExtractionTool.py" target="_blank" rel="noopener">lassoan/SlicerHDBrainExtraction/blob/main/HDBrainExtractionTool/HDBrainExtractionTool.py</a></h4>


      <pre><code class="lang-py">import logging
import os

import vtk

import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin


#
# HDBrainExtractionTool
#

class HDBrainExtractionTool(ScriptedLoadableModule):
  """Uses ScriptedLoadableModule base class, available at:
  https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py
  """

  def __init__(self, parent):
</code></pre>



  This file has been truncated. <a href="https://github.com/lassoan/SlicerHDBrainExtraction/blob/main/HDBrainExtractionTool/HDBrainExtractionTool.py" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The module installs pytorch, installs the deep learning based segmentation tool, downloads the model, and displays GUI for specifying inputs and outputs for the model.</p>

---
