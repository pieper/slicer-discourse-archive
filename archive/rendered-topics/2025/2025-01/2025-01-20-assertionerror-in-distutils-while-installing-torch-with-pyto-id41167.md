---
topic_id: 41167
title: "Assertionerror In Distutils While Installing Torch With Pyto"
date: 2025-01-20
url: https://discourse.slicer.org/t/41167
---

# AssertionError in distutils while installing Torch with PytorchUtils for Segment Anything Model-based extension

**Topic ID**: 41167
**Date**: 2025-01-20
**URL**: https://discourse.slicer.org/t/assertionerror-in-distutils-while-installing-torch-with-pytorchutils-for-segment-anything-model-based-extension/41167

---

## Post #1 by @oothomas (2025-01-20 16:02 UTC)

<p>I’m developing an extension called <strong>SlicerPhotogrammetry</strong> that uses Meta’s <a href="https://github.com/facebookresearch/segment-anything" rel="noopener nofollow ugc">Segment Anything</a> model. Because Segment Anything requires PyTorch (and thus Torch + TorchVision), I’m programmatically installing PyTorch inside the Slicer environment if it isn’t already installed.</p>
<p>Here is the relevant installation snippet in my <code>SlicerPhotogrammetry.py</code> (using the PyTorchUtils extension):</p>
<p>python</p>
<p>Copy</p>
<pre><code class="lang-auto">try:
    import PyTorchUtils
except ModuleNotFoundError:
    slicer.util.messageBox("SlicerPhotogrammetry requires the PyTorch extension. Please install it from the "
                           "Extensions Manager.")

torchLogic = PyTorchUtils.PyTorchUtilsLogic()
if not torchLogic.torchInstalled():
    logging.debug('SlicerPhotogrammetry requires the PyTorch Python package. Installing... '
                  'this may take several minutes')
    torch = torchLogic.installTorch(askConfirmation=True, forceComputationBackend='cu118')
    if torch is None:
        slicer.util.messageBox('PyTorch extension needs to be installed manually to use this module.')

try:
    from PIL import Image, ExifTags
except ImportError:
    slicer.util.pip_install("Pillow")
    from PIL import Image, ExifTags

try:
    import cv2
    if not hasattr(cv2, 'xfeatures2d'):
        raise ImportError("opencv-contrib-python is not properly installed")
except ImportError:
    slicer.util.pip_install("opencv-python")
    slicer.util.pip_install("opencv-contrib-python")
    import cv2

try:
    import segment_anything
except ImportError:
    slicer.util.pip_install("git+https://github.com/facebookresearch/segment-anything.git")
    import segment_anything
</code></pre>
<p>However, after the PyTorch installation completes, the module fails to load with an <code>AssertionError</code> pointing to:</p>
<p>bash</p>
<p>Copy</p>
<pre><code class="lang-auto">AssertionError: /home/username/Slicer-5.7.0-2025-01-11-linux-amd64/lib/Python/lib/python3.9/distutils/core.py
</code></pre>
<p>Below is part of the console log:</p>
<p>vbnet</p>
<p>Copy</p>
<pre><code class="lang-auto">Collecting torch
  Using cached https://download.pytorch.org/whl/cu118/torch-2.5.1%2Bcu118-cp39-cp39-linux_x86_64.whl (838.4 MB)
...
AssertionError: /home/username/Slicer-5.7.0-2025-01-11-linux-amd64/lib/Python/lib/python3.9/distutils/core.py
[Qt] loadSourceAsModule - Failed to load file "...SlicerPhotogrammetry.py" as module "SlicerPhotogrammetry" !
[Qt] Fail to instantiate module  "SlicerPhotogrammetry"
[Python] The module factory manager reported an error.
</code></pre>
<p><strong>Steps to Reproduce:</strong></p>
<ol>
<li>Clone the <a href="https://github.com/SlicerMorph/SlicerPhotogrammetry" rel="noopener nofollow ugc">SlicerPhotogrammetry repository</a>.</li>
<li>Use Slicer’s <strong>Extension Wizard</strong> to “Select Extension” and build/install this extension from the cloned local folder. An error will occur</li>
<li>If you restart Slicer and attempt to load or use the <code>SlicerPhotogrammetry</code> module, an error should occur.</li>
<li>Observe that PyTorch is downloaded and installed, but an <code>AssertionError</code> related to <code>distutils</code> occurs afterward, causing the module to fail to load.</li>
</ol>
<p><strong>Environment Details:</strong></p>
<ul>
<li>Operating System: Linux (Ubuntu 22.04)</li>
<li>Slicer Version: 5.7.0-2025-01-11 (Preview Release)</li>
<li>PyTorch installed via <code>torchLogic.installTorch(askConfirmation=True, forceComputationBackend='cu118')</code>.</li>
</ul>
<p><strong>Question:</strong></p>
<ul>
<li>How can I resolve the <code>AssertionError</code> due to distutils being replaced by setuptools?</li>
<li>Is there a recommended or more robust approach to install Torch/TorchVision (and dependencies like <code>segment_anything</code>) within Slicer so that Segment Anything can run without environment conflicts?</li>
</ul>
<p>Any guidance or best practices for seamlessly installing PyTorch inside a Slicer extension would be greatly appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/037065d7756af75398fbfdc6068856857496631e.png" data-download-href="/uploads/short-url/uqf6viQbfqxWJDYhGjhBNypub4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/037065d7756af75398fbfdc6068856857496631e.png" alt="image" data-base62-sha1="uqf6viQbfqxWJDYhGjhBNypub4" width="598" height="230"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">598×230 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfe4469569b291f0304d5def5f98b5a69f7b728.png" data-download-href="/uploads/short-url/zXeBPhCwmQHt8isoujkeM3Mm7cQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbfe4469569b291f0304d5def5f98b5a69f7b728.png" alt="image" data-base62-sha1="zXeBPhCwmQHt8isoujkeM3Mm7cQ" width="554" height="186"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">554×186 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @oothomas (2025-01-20 16:38 UTC)

<p>RESOLVED! I was checking for dependencies and installing in the constructor of the widget class due to another error with cv2 import. That has been resolved and now the dedicated load_dependencies method works as expected.</p>

---
