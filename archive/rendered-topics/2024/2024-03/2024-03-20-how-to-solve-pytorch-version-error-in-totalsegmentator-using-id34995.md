# How to solve Pytorch version error in TotalSegmentator using CPU

**Topic ID**: 34995
**Date**: 2024-03-20
**URL**: https://discourse.slicer.org/t/how-to-solve-pytorch-version-error-in-totalsegmentator-using-cpu/34995

---

## Post #1 by @Cchloe_G (2024-03-20 19:45 UTC)

<p>My GPU is small, so I decided to use CPU to run totalsegmentator. I have uninstalled GPU version Pytorch in PyTorch Utils and downloaded cpu version Pytorch 1.8.1  successfully. However when I apply total segmentator, It shows this error:<br>
PyTorch version 1.8.1+cpu is not compatible with this module. Minimum required version is 1.12. You can use “PyTorch Util” module to install PyTorch with version requirement set to: &gt;=1.12</p>
<p>Please help me!</p>

---

## Post #2 by @muratmaga (2024-03-20 21:28 UTC)

<aside class="quote no-group" data-username="Cchloe_G" data-post="1" data-topic="34995">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cchloe_g/48/69702_2.png" class="avatar"> Cchloe_G:</div>
<blockquote>
<p>PyTorch Utils and downloaded cpu version Pytorch 1.8.1</p>
</blockquote>
</aside>
<p>Pyutil should display a number of different versions compatible with your system. You chose 1.8.1 because 1.12 (or higher) wasn’t available?</p>

---

## Post #3 by @muratmaga (2024-03-20 21:40 UTC)

<p>Himm this is interesting. I just tried on my Mac, and while it started downloading v 2.2.1, it ended up installing 1.8. Not sure why. <a class="mention" href="/u/lassoan">@lassoan</a></p>
<pre><code class="lang-auto">Install PyTorch using light-the-torch with arguments: ['install', 'torch', 'torchvision', '--pytorch-computation-backend=cpu']
Collecting torch
  Downloading https://download.pytorch.org/whl/cpu/torch-2.2.1-cp39-none-macosx_10_9_x86_64.whl (151.0 MB)

Collecting torchvision
  Using cached https://download.pytorch.org/whl/torchvision-0.9.1-cp39-cp39-macosx_10_9_x86_64.whl (13.1 MB)
Requirement already satisfied: filelock in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (3.13.1)
Requirement already satisfied: typing-extensions&gt;=4.8.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (4.8.0)
Requirement already satisfied: sympy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (1.12)
Requirement already satisfied: networkx in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (3.2.1)
Requirement already satisfied: jinja2 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (3.1.3)
Requirement already satisfied: fsspec in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torch) (2024.2.0)
Requirement already satisfied: numpy in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (1.26.1)
Collecting torch
  Using cached https://download.pytorch.org/whl/cpu/torch-1.8.1-cp39-none-macosx_10_9_x86_64.whl (119.6 MB)
Requirement already satisfied: pillow&gt;=4.1.1 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from torchvision) (10.1.0)
Requirement already satisfied: MarkupSafe&gt;=2.0 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from jinja2-&gt;torch) (2.1.5)
Requirement already satisfied: mpmath&gt;=0.19 in /Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages (from sympy-&gt;torch) (1.3.0)
Installing collected packages: torch, torchvision
  WARNING: The scripts convert-caffe2-to-onnx and convert-onnx-to-caffe2 are installed in '/Applications/Slicer.app/Contents/lib/Python/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed torch-1.8.1 torchvision-0.9.1
</code></pre>

---

## Post #4 by @lassoan (2024-03-22 22:42 UTC)

<p>Maybe PyTorch-1.8.1 files were in use and could not be updated. Try uninstalling pytorch, restart Slicer, and then install it. Maybe check if the <code>lib\Python\Lib\site-packages\torch</code> folder in the Slicer install tree is empty.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> FYI, a <a href="https://github.com/KitwareMedical/SlicerNNUnet">new Slicer extension</a> is in the works that all extensions that use nnunet could use to install nnunet and all its dependencies (and it should include all the tricks we learned from TotalSegmentator). You may consider using it for MEMOS.</p>

---

## Post #5 by @So-lets-code (2025-02-10 23:12 UTC)

<p>I also have a Mac which installed v1.8.1 again and again. It eventually worked, you just need to <strong>restart 3D slicer</strong> after you uninstall 1.8.1. Once you reopen slicer and set Torch version to &gt;=1.12, it will automatically download v2.2.1</p>

---

## Post #7 by @Sundeep_Kisku (2025-03-04 12:55 UTC)

<p>Yes, doing this worked for my Mac too</p>

---
