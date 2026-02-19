---
topic_id: 13712
title: "Tensorflow V 2 3 0 Tf Config List Physical Devices Gpu Shows"
date: 2020-09-26
url: https://discourse.slicer.org/t/13712
---

# [Tensorflow v 2.3.0] tf.config.list_physical_devices('GPU') shows empty list in PythonSlicer.exe

**Topic ID**: 13712
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/tensorflow-v-2-3-0-tf-config-list-physical-devices-gpu-shows-empty-list-in-pythonslicer-exe/13712

---

## Post #1 by @strider_hunter (2020-09-26 14:42 UTC)

<p>Hi,<br>
I am attempting to check if tensorflow installed in 3DSlicer is <em>able to access the GPU</em> for its computation. I get the following outputs in “PythonSlicer.exe”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d0b9b077caf2a9e9743e6951c2d928ddb61ff9a.png" data-download-href="/uploads/short-url/dh7gIkUelqxa7rYZbrQrzAkOIPw.png?dl=1" title="GPU_Tensorflow_Issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d0b9b077caf2a9e9743e6951c2d928ddb61ff9a.png" alt="GPU_Tensorflow_Issue" data-base62-sha1="dh7gIkUelqxa7rYZbrQrzAkOIPw" width="690" height="379" data-dominant-color="626262"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GPU_Tensorflow_Issue</span><span class="informations">1354×744 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anybody know what is missing here? Tensorflow was able to detect the GPU as well as CUDA runtime (<em>cudart64_101.dll</em>). Is it necessary to install cuDNN?</p>
<br>
---
---
&gt; **System Info**
&gt; 1. Windows 10
&gt; 2. 3D Slicer (*4.11.0-2020-09-05 r29359 / 5513baa*)
&gt; - PythonSlicer: C:\Users\\AppData\Local\NA-MIC\Slicer 4.11.0-2020-09-05\bin\PythonSlilcer.exe
&gt; 3. Tensorflow - 2.3.0
&gt;  - slicer.util.pip_install('tensorflow')
&gt; 4. CUDA Toolkit - 10.1
&gt; 5. GPU - Nvidia GTX 2080Ti (Driver Version = 451.48)

---

## Post #2 by @strider_hunter (2020-09-26 14:53 UTC)

<p><strong>Solution</strong><br>
So it turns out that installing cuDNN is required.</p>
<p>For any people referring to this in the future, you can use <a href="https://www.tensorflow.org/install/source#tested_build_configurations" rel="noopener nofollow ugc">this link on tensorflows website</a> to determine the CUDA and cuDNN version to use corresponding to a tensorflow version.</p>
<p>Latest tensorflow version (2.3.0) uses CUDA 10.1 with cuDNN (7.6.5)</p>

---

## Post #3 by @lassoan (2020-09-26 16:44 UTC)

<p>Thanks a lot for sharing the solution.</p>

---
