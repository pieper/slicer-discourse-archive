# Error when running sample Slicer Jupyter Notebooks from local linux machine

**Topic ID**: 11975
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/error-when-running-sample-slicer-jupyter-notebooks-from-local-linux-machine/11975

---

## Post #1 by @Andrius (2020-06-10 07:29 UTC)

<p>Dear Slicers,</p>
<p>I am just getting started with Python and slicer. My goal is to use slicer to combine ITK, VTK and VMTK capabilities for vascular segmentation and geometric data extraction. I love the idea that all this can be combined with the rest of python packages.</p>
<p>I installed into my vmtk python environment as per instructions here:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" target="_blank" rel="nofollow noopener">Slicer/SlicerJupyter/blob/master/README.md#setup</a></h4>
<pre><code class="lang-md"># SlicerJupyter
Extension for 3D Slicer that allows the application to be used from Jupyter notebook

Demo video: https://youtu.be/oZ3_cRXX2QM

[![](https://img.youtube.com/vi/oZ3_cRXX2QM/0.jpg)](https://www.youtube.com/watch?v=oZ3_cRXX2QM "Slicer Jupyter kernel demo")

# Usage

## Option 1. Run using Binder

You can use this option for a quick start. No installation or setup is needed, just click the link below and start using Slicer via Jupyter notebook in your web browser.

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master)

When you click on the link, Binder launches 3D Slicer with SlicerJupyter extension on their cloud servers. Binder is a free service and server resources are quite limited. Also, there is no interactive access to the graphical user interface. Therefore, this option is only recommended for testing, demos, or simple computations or visualizations.

## Option 2. Run Slicer and Jupyter on your own computer

### Setup
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>For the most part all the sample notebooks are running well from my local linux.<br>
However, this particular bit of code gives me an error. The manual segmentation part:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerNotebooks/blob/master/04_Segmentation.ipynb" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerNotebooks/blob/master/04_Segmentation.ipynb" target="_blank" rel="nofollow noopener">Slicer/SlicerNotebooks/blob/master/04_Segmentation.ipynb</a></h4>
<pre><code class="lang-ipynb">{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Segmentation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import JupyterNotebooksLib as slicernb\n",
    "\n",
    "# Set image viewer size to 50% (fill half of a cell)\n",
    "slicernb.AppWindow.setWindowSize(scale=0.5)\n",
    "# Hide patient information from slice view\n",
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/SlicerNotebooks/blob/master/04_Segmentation.ipynb" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<h2>The error I get:</h2>
<p>TypeError                                 Traceback (most recent call last)<br>
In  [8]:<br>
Line 4:</p>
<h2>TypeError: ‘MRMLCorePython.vtkMRMLScalarVolumeNode’ object is not subscriptable</h2>
<p>Hope somebody can help to troubleshoot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Cheers,<br>
Andrius</p>

---
