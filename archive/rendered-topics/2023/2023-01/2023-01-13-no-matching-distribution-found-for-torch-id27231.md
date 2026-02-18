# No matching distribution found for torch

**Topic ID**: 27231
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/no-matching-distribution-found-for-torch/27231

---

## Post #1 by @arobinson (2023-01-13 16:27 UTC)

<p>When I try to install pytorch through the PyTorch Utils module, I get an error saying no matching distribution found for torch. I have CUDA11.7 and have the newest version of the pytorch module for slicer installed. I’m able to use pytorch outside of slicer just fine, so not sure what the issue is here.</p>

---

## Post #2 by @ebrahim (2023-01-13 16:53 UTC)

<p>SlicerPyTorch <a href="https://github.com/fepegar/SlicerPyTorch/blob/12ed0b2777a436bff4c22b7a5e9e8238db7e242f/PyTorchUtils/PyTorchUtils.py#L187" rel="noopener nofollow ugc">uses</a> the tool <a href="https://github.com/pmeier/light-the-torch" rel="noopener nofollow ugc">light-the-torch</a> to choose a matching distribution. You could try using it yourself in Slicer’s python console and see if there’s a more informative error.</p>
<p>Or skip light-the-torch and copy the desried pip install command from <a href="https://pytorch.org/get-started/locally/" rel="noopener nofollow ugc">here</a> based on the cuda version, etc. that you want. Then in Slicer’s python console do</p>
<pre data-code-wrap="py"><code class="lang-plaintext">slicer.util.pip_install("&lt;your pip install command&gt;")
</code></pre>
<p>just omitting the initial “pip install” from the command string.</p>

---

## Post #3 by @arobinson (2023-01-17 18:40 UTC)

<p>This worked thanks!! However, it’s running with the CPU. Do you have any tips on getting it running with CUDA? It seems to not be finding my CUDA installation.</p>

---

## Post #4 by @lassoan (2023-01-17 19:06 UTC)

<p>Light-the-torch works very robustly. If it cannot find your graphics driver/CUDA then something is wrong/unusual about your system configuration.</p>
<p>What operating system do you use?</p>
<p>What GPU model do you have?</p>
<p>Do you have multiple graphics card in your computer (e.g., NVIDIA discrete GPU + integrated Intel Graphics)? Have you set in your NVIDIA settings to use the high-performance GPU for 3D Slicer (SlicerApp-real.exe)?</p>
<p>What pytorch and NVIDIA driver is reported in PyTorch Utils module?</p>
<p>What do you see if you type <code>import torch; torch.has_cuda</code> into the Python console in Slicer?</p>

---

## Post #5 by @arobinson (2023-01-17 21:42 UTC)

<p>I’m sure it’s something with my system’s configuration. I’ve had issues with all sorts of things using python.</p>
<p>I’m on Windows 10 with a NVIDIA Quadro P4000. I don’t believe I have multiple graphics cards and haven’t touched the NVIDIA settings (not sure where those are). The PyTorch Utils module is still telling me to install PyTorch, but when I click on that button it says “Pytorch 1.13.1+cpu already installed correctly”. Torch.has_cuda returns false.</p>

---
