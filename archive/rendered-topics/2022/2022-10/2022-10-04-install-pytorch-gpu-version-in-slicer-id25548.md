# Install pytorch GPU version in Slicer

**Topic ID**: 25548
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/install-pytorch-gpu-version-in-slicer/25548

---

## Post #1 by @l2022 (2022-10-04 19:43 UTC)

<p>Hi,<br>
I am trying to install pytorch GPU version in Slicer but I can only install the CPU version. I can successfully install pytorch GPU in a external python but running the same pip commands in the Slicer’s python I only get the CPU one.<br>
Do you know how to solve it?</p>
<p>Thank you</p>

---

## Post #2 by @muratmaga (2022-10-04 20:18 UTC)

<p>remove all packages you installed, and follow the instructions in here. <a href="https://pytorch.org/" rel="noopener nofollow ugc">https://pytorch.org/</a><br>
Choosing correct versions of OS, package manager and cuda versions installed on your system.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://pytorch.org/">
  <header class="source">
      <img src="https://pytorch.org/favicon.ico?" class="site-icon" width="32" height="32">

      <a href="https://pytorch.org/" target="_blank" rel="noopener nofollow ugc">pytorch.org</a>
  </header>

  <article class="onebox-body">
    <img src="https://pytorch.org/assets/images/pytorch-logo.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://pytorch.org/" target="_blank" rel="noopener nofollow ugc">PyTorch</a></h3>

  <p>An open source machine learning framework that accelerates the path from research prototyping to production deployment.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>then instead of installing with pip (if you are on Linux), just download the appropriate wheels for your system. (i.e., ignore the first part, and follow the second part that goes <a href="https://download.pytorch.org/whl/cu116" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu116</a>)</p>
<p>for example if you are on linux and you have cuda 11.6 installed this would be the one of the appropriate package (since Slicer uses python 3.9) if your goal is to use torch 1.12</p>
<p><code>https://download.pytorch.org/whl/cu116/torch-1.12.0%2Bcu116-cp39-cp39-linux_x86_64.whl</code></p>
<p>once those are downloaded, open Slicer go to python interactor and install via<br>
<code>pip_install('path-to-your-downloaded-wheels')</code></p>

---

## Post #3 by @ebrahim (2022-10-05 00:55 UTC)

<p>Additionally there is the <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">SlicerPyTorch extension</a> (should be in the extension manager). It uses light-the-torch under the hood, so you could also just go ahead use light-the-torch yourself to help fetch and install the correct wheel for your hardware</p>

---

## Post #4 by @muratmaga (2022-10-05 01:46 UTC)

<p>I wasn’t aware of this. This look really cool. will give it a try.</p>

---
