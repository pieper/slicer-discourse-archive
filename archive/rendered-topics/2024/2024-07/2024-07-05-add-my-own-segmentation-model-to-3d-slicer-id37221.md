# Add my own segmentation model to 3D Slicer

**Topic ID**: 37221
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/add-my-own-segmentation-model-to-3d-slicer/37221

---

## Post #1 by @maniron (2024-07-05 17:03 UTC)

<p>Previously we were trying to add a plugin in windows and install the required packages of our plugin using PythonSlicer.exe in windows.</p>
<blockquote>
<p>PythonSlicer.exe -m pip install --trusted-host=<a href="http://pytorch.org" rel="noopener nofollow ugc">pytorch.org</a> --trusted-host=<a href="http://download.pytorch.org" rel="noopener nofollow ugc">download.pytorch.org</a> --trusted-host=<a href="http://files.pytorch.org" rel="noopener nofollow ugc">files.pytorch.org</a> -r requirements-slicer.txt</p>
</blockquote>
<p>Similarly how to do a this kind of installation of packages in ubuntu OS</p>

---

## Post #2 by @lassoan (2024-07-05 17:05 UTC)

<p>It looks good in general. However, I would not recommend to install pytorch like this. Pytorch is now used very commonly - all AI extensions use it - and we provide the PyTorch extension to install it, as the installation can go wrong in many ways. You can see an example of how it is used in MONAIAuto3DSeg and TotalSegmentator extensions.</p>
<p>I’m not sure what you mean by plugin though, as neither Slicer nor Python use plugins. Slicer has extensions that you can install via Slicer’s Extensions Manager, while Python has packages that you can install via pip.</p>

---

## Post #3 by @maniron (2024-07-08 06:02 UTC)

<p>Hi Iassoan We are trying to add a our own developed segmentation model as a part of Slicer which I referred as the plugin here, for that I want to know how can I install the packages required using the Slicer.</p>
<p>In windows OS Pythonslicer.exe is used to install the required packages, similarly what is used to install packages in ubuntu OS</p>

---

## Post #4 by @lassoan (2024-07-08 13:30 UTC)

<p>Thanks for the clarification. I would recommend to use similar extensions as example. You can use <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg">MONAIAuto3DSeg</a> as an example for implementing MONAI based model, or <a href="https://github.com/gaudot/SlicerDentalSegmentator">DentalSegmentator</a> for nn-UNet based model.</p>

---

## Post #5 by @maniron (2024-07-10 10:57 UTC)

<p>Hi Iassoan Recently I have been facing this issue</p>
<p>“[/home/ubuntu/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.”</p>

---

## Post #6 by @lassoan (2024-07-22 21:08 UTC)

<p>Since you have built Slicer in debug mode, you can get detailed information of where the problem occurred (see instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html#gdb-debug-by-attaching-to-running-process-recommended">here</a>, you can probably skip <em>Step 1</em>).</p>

---
