# CUDA version for build machines

**Topic ID**: 7298
**Date**: 2019-06-24
**URL**: https://discourse.slicer.org/t/cuda-version-for-build-machines/7298

---

## Post #1 by @gregsharp.geo (2019-06-24 19:32 UTC)

<p>I have compiled some information regarding which CUDA version would be most compatible with the Slicer factory build machines.</p>
<p>Windows (overload.kitware)<br>
The web page says both VS2013 and VS2015 installed.  I assume the latter is used to build slicer.  All CUDA versions 8.0 to 10.1 support VS 2015 on Windows 7.</p>
<p>Linux (metroplex.kitware)<br>
No gcc version is given on the web site.  CUDA 8.0 recommends gcc 4.8.2, CUDA 9.0-10.1 recommend gcc 4.8.5.</p>
<p>MacOS (factory-south.kitware)<br>
No CUDA version supports the combination of OSX 10.11 and LLVM 8.0.0.  The closest match is CUDA 8.0, which supports 10.11 with LLVM 7.2 and 10.12 with LLVM 8.0.0.  Probably it will work, but can’t be certain.</p>
<p>Other considerations:</p>
<p>CUDA 8.0 is the last version which supports Fermi (compute capability 2.x), it supports Volta (7.0) and Turing (7.5) through PTX JIT only.  CUDA 9.0 adds native support for Volta (7.0), Turing (7.5) supported through PTX only.  CUDA 10.0 adds native support for Turing (7.5).</p>
<p>Refs:<br>
[1] <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Factory</a><br>
[2] <a href="https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html" rel="nofollow noopener">https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html</a><br>
[3] <a href="https://docs.nvidia.com/cuda/archive/" rel="nofollow noopener">https://docs.nvidia.com/cuda/archive/</a><br>
[4] <a href="https://docs.nvidia.com/deploy/cuda-compatibility/" rel="nofollow noopener">https://docs.nvidia.com/deploy/cuda-compatibility/</a></p>

---
