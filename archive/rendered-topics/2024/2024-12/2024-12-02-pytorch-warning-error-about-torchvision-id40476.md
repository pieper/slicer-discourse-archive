# pyTorch warning/error about torchvision

**Topic ID**: 40476
**Date**: 2024-12-02
**URL**: https://discourse.slicer.org/t/pytorch-warning-error-about-torchvision/40476

---

## Post #1 by @muratmaga (2024-12-02 16:03 UTC)

<p>Not sure whether this breaks anything, but there is this error/warning message about setup tools replacing distools:</p>
<pre><code class="lang-auto">Installing collected packages: mpmath, sympy, nvidia-nvtx-cu11, nvidia-nccl-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cufft-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda-nvrtc-cu11, nvidia-cuda-cupti-cu11, nvidia-cublas-cu11, networkx, MarkupSafe, fsspec, filelock, triton, nvidia-cusolver-cu11, nvidia-cudnn-cu11, jinja2, torch, torchvision
Successfully installed MarkupSafe-3.0.2 filelock-3.16.1 fsspec-2024.10.0 jinja2-3.1.4 mpmath-1.3.0 networkx-3.2.1 nvidia-cublas-cu11-11.11.3.6 nvidia-cuda-cupti-cu11-11.8.87 nvidia-cuda-nvrtc-cu11-11.8.89 nvidia-cuda-runtime-cu11-11.8.89 nvidia-cudnn-cu11-9.1.0.70 nvidia-cufft-cu11-10.9.0.58 nvidia-curand-cu11-10.3.0.86 nvidia-cusolver-cu11-11.4.1.48 nvidia-cusparse-cu11-11.7.5.86 nvidia-nccl-cu11-2.21.5 nvidia-nvtx-cu11-11.8.86 sympy-1.13.1 torch-2.5.1+cu118 torchvision-0.20.1+cu118 triton-3.1.0
PyTorch 2.5.1+cu118 installed successfully.
Importing torch...
PyTorch 2.5.1+cu118 imported successfully
/media/volume/MyData/Slicer/lib/Python/lib/python3.9/site-packages/torch/cuda/__init__.py:129: UserWarning: CUDA initialization: CUDA driver initialization failed, you might not have a CUDA gpu. (Triggered internally at ../c10/cuda/CUDAFunctions.cpp:108.)
  return torch._C._cuda_getDeviceCount() &gt; 0
CUDA available: False
PyTorch 2.5.1+cu118 installed successfully using cpu.
/media/volume/MyData/Slicer/lib/Python/lib/python3.9/site-packages/_distutils_hack/__init__.py:11: UserWarning: Distutils was imported before Setuptools, but importing Setuptools also replaces the `distutils` module in `sys.modules`. This may lead to undesirable behaviors or errors. To avoid these issues, avoid using distutils directly, ensure that setuptools is installed in the traditional way (e.g. not an editable install), and/or make sure that setuptools is always imported before distutils.
  warnings.warn(
/media/volume/MyData/Slicer/lib/Python/lib/python3.9/site-packages/_distutils_hack/__init__.py:26: UserWarning: Setuptools is replacing distutils.
  warnings.warn("Setuptools is replacing distutils.")
/media/volume/MyData/Slicer/lib/Python/lib/python3.9/distutils/core.py
</code></pre>

---

## Post #2 by @lassoan (2024-12-02 16:14 UTC)

<p><code>distutils</code> is going away (<a href="https://stackoverflow.com/questions/69858963/how-can-one-fully-replace-distutils-which-is-deprecated-in-3-10">deprecated in Python-3.10, removed in Python-3.12)</a>. This warning means that some Python package that was installed still used <code>distutils</code>. This can be safely ignored for Python-3.9 (distutils will remain available for this Python version). <a href="https://github.com/Slicer/Slicer/issues/7060">Slicer will switch to Python 3.10 or 3.11 after releasing Slicer-5.8</a> and Python packages built for this version will most likely not depend on <code>distutils</code> anymore.</p>
<p>In short, I don’t think we need to do anything with this.</p>

---

## Post #3 by @pieper (2024-12-02 16:17 UTC)

<p>I’m not sure if it’s related, but I wasn’t able to get torch to recognize cuda on a a jetstream2 A100 today using various torch install methods (SlicerPyTorch, pip install command from the pytorch site).  Slicer was running with gpu accelerated graphics, but the torch cuda driver never worked.  The pytorch site offered cuda 12.1 and 12.4, but nvida-smi on the instance reports 12.2.</p>

---

## Post #4 by @muratmaga (2024-12-02 16:20 UTC)

<p>Yeah, I am getting the same issue as well. I sent a message to JS2 admins to check if it is a hypervisor or a driver issue.</p>
<p>I am going to start a workshop in an hour, so I won’t have time, but can you try installing torch outside of Slicer. We need to know whether that’s a Slicer issue is a more general driver issue.</p>

---

## Post #5 by @pieper (2024-12-02 16:28 UTC)

<p>Okay, I can try.  I used <code>PythonSlicer</code> which is basically a raw python so I don’t think it’ll be any different from any other python.  We’ll see.</p>

---

## Post #6 by @pieper (2024-12-02 17:11 UTC)

<p>On a fresh jetstream2 gpu machine with ubuntu 24.04 I can install and access cuda from torch,   My other machine where I couldn’t get torch to use cuda is a 22.04 machine where I had set up gpu accelerated X, so either of those could be the difference.</p>

---

## Post #7 by @muratmaga (2024-12-03 04:26 UTC)

<p>From JS2 admins:</p>
<p><code>So, a little bit of context. The nvidia driver we build into our featured images is the nvidia-linux-grid-535  a special, proprietary GRID driver needed to communicate properly with the hypervisor since all GPU instances used to use vGPU. We recently reconfigured resources so that g3.xl instances no longer use vGPU, and instance have their PCI device directly passed through from the hypervisor to your instance (no middleman). This has a number of benefits, including unified memory support and being able to use whatever driver you want, but comes with the drawback that the flavor is semantically different from the rest. Unfortunately there seems to be some incompatibility using the grid driver on a non vGPU instance, most notably the extremely slow response times from the GPU which caused things like pytorch to timeout and give errors. You may want to install nvidia-driver-550-server-open as part of your setup script for g3.xl instances instead. In my experience, this driver has been a lot more reliable for this flavor. You won't be able to resize down to a smaller flavor after doing this, though I believe you don't use resizing in your workflow, correct?</code></p>

---

## Post #8 by @pieper (2024-12-03 15:05 UTC)

<p>This makes sense with what I saw.  The vm that works is a g3.small and the one that doesn’t is a g3.xl.</p>
<p>When I get a chance I’ll try installing the nvidia-driver-550-server-open and see what happens.</p>

---

## Post #9 by @pieper (2024-12-03 15:37 UTC)

<p>I used the <code>ubuntu-drivers install</code> to install the recommended drivers and now my <code>g3.xl</code> instance and now I can run Slicer with gpu accelerated rendering and access cuda from torch in Slicer python.</p>

---

## Post #10 by @muratmaga (2024-12-03 15:49 UTC)

<p>weird, I am still having the GPU hang problem with vanilla 22.04 from JS2 and 550 drivers and torch installation hangs in Slicer…</p>
<p>I will open a ticket with them.</p>

---
