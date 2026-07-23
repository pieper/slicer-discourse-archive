---
topic_id: 47710
title: "Pytorch extension causes crash (Slicer 5.12.2 on Ubuntu 22.04)"
date: 2026-07-22
url: https://discourse.slicer.org/t/47710
last_bumped: 2026-07-22T15:04:42.252Z
---

# Pytorch extension causes crash (Slicer 5.12.2 on Ubuntu 22.04)

**Topic ID**: 47710
**Date**: 2026-07-22
**URL**: https://discourse.slicer.org/t/pytorch-extension-causes-crash-slicer-5-12-2-on-ubuntu-22-04/47710

---

## Post #1 by @shai-ikko (2026-07-22 09:45 UTC)

<p>Hi,</p>
<p>I’m having trouble with the PyTorch extension. On a fresh Slicer 5.12.2 installation, I install the extension, open it, and tell it to install pytorch using the default (automatic) backend. The installation supposedly succeeds, and the application (the whole Slicer) crashes.</p>
<p>After this, if I open this Slicer, and navigate to the pytorch extension, the app crashes.</p>
<p>I put a log file from the app at <a href="https://gist.github.com/shai-ikko/e833d8219b20e14c5c2108176cda17c0" class="inline-onebox" rel="noopener nofollow ugc">Slicer log file · GitHub</a> , after I set the Python console logging level to “Debug” before doing all of this. In this run, I also clicked “uninstall pytorch” first, although it was a fresh installation, in hope to clean up any leftovers from previous installations that might live outside the app folder.</p>
<p>I will be happy to provide further input, and will be happy to take any help in debugging it.</p>

---

## Post #2 by @pieper (2026-07-22 14:10 UTC)

<p>It would be good to have this in the extension repo issues: <a href="https://github.com/fepegar/SlicerPyTorch">https://github.com/fepegar/SlicerPyTorch</a></p>
<p>We have troubles from time to time with PyTorch, but I don’t think anyone has a magic formula to keep up with all the changes.</p>
<p>Can you try the pytorch local install instructions with Slicer’s python? (<code>PythonSlicer -m pip</code>)</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pytorch.org/get-started/locally/">
  <header class="source">
      <img src="https://pytorch.org/wp-content/uploads/2024/10/cropped-favicon-32x32.webp" class="site-icon" alt="" width="32" height="32">

      <a href="https://pytorch.org/get-started/locally/" target="_blank" rel="noopener">PyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/387;"><img src="https://pytorch.org/wp-content/uploads/2025/01/pytorch_seo.png" class="thumbnail" alt="" width="690" height="388"></div>

<h3><a href="https://pytorch.org/get-started/locally/" target="_blank" rel="noopener">Get Started</a></h3>

  <p>Set up PyTorch easily with local installation or supported cloud platforms.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2026-07-22 15:04 UTC)

<p><a class="mention" href="/u/shai-ikko">@shai-ikko</a> it looks like it is bringing cuda 13.0.</p>
<ol>
<li>Does your Nvidia driver support cuda 13.0 (this shouldn’t be the case)</li>
<li>Does it help if you try to install 12.8? (uninstall 13.0 and then manually choose cu128 fromt he availablity list).</li>
</ol>
<p>That’s as far as I can suggest. Otherwise as <a class="mention" href="/u/pieper">@pieper</a> said it is a game of whack a mole until you find a combination that works…</p>

---
