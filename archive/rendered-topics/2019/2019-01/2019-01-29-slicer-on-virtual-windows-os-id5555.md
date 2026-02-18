# Slicer on Virtual Windows OS

**Topic ID**: 5555
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/slicer-on-virtual-windows-os/5555

---

## Post #1 by @anandmulay3 (2019-01-29 07:57 UTC)

<p>I’ve installed Slicer on my remote virtual windows 10 OS, i’m using a batch script to call scriptablemodule  and its working fine. In this i’m creating a 3d model from a dicom series.<br>
The problem is the output model which is created on that remote virtual OS is different and causing large Holes in the output model, and the same thing if i runs on my laptop its working fine and gives right output model.<br>
what should i do to fix this issue, my virtual OS has 32+GB ram and also allocated GPU.</p>

---

## Post #2 by @lassoan (2019-01-30 01:46 UTC)

<p>This should not happen, since model generation is all implemented in the CPU and your virtual machine seems to be capable to deal with this task. If you shared a screenshot of the correct and incorrect result then it might give a hint of what could go wrong.</p>

---

## Post #3 by @anandmulay3 (2019-01-30 07:18 UTC)

<p>The Skull model output on my laptop.:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d96eac6bcfd7a120ff4ed001acc9a3ce255d4aa.png" alt="image" data-base62-sha1="6viP7AyfaLjKKc2nb8ODf8ug0VY" width="487" height="367"><br>
The Skull model output on the virtual machine.:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f6c8dbb4e0ab06791c0a28cf94dd351feb74a54.jpeg" data-download-href="/uploads/short-url/6Lx10jsjzT1Iea8Hjf2eSNhVvG4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f6c8dbb4e0ab06791c0a28cf94dd351feb74a54_2_607x500.jpeg" alt="image" data-base62-sha1="6Lx10jsjzT1Iea8Hjf2eSNhVvG4" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f6c8dbb4e0ab06791c0a28cf94dd351feb74a54_2_607x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f6c8dbb4e0ab06791c0a28cf94dd351feb74a54.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f6c8dbb4e0ab06791c0a28cf94dd351feb74a54.jpeg 2x" data-dominant-color="2D2D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">632×520 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Input for both, is same.</p>

---

## Post #4 by @lassoan (2019-01-30 10:11 UTC)

<p>The image below looks smoother, so probably either the smoothing factor during surface generation is larger or voxel size segmentation labelmap voxel size is larger. Or maybe the threshold value is higher for some reason.</p>

---

## Post #5 by @anandmulay3 (2019-01-30 10:21 UTC)

<p>the threshold parameters and smoothing parameters are same for both.<br>
Today i also noticed that if i manually runs my batch file on virtual machine it gives expected output.<br>
But if i invoke it from my remote program it gives me the second image output <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=6" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #6 by @lassoan (2019-01-31 00:22 UTC)

<p>What do you mean by running manually and invoking it? Do you run exactly the same command-line?<br>
Can you post the code that you use for batch conversion?</p>

---

## Post #7 by @anandmulay3 (2019-01-31 07:50 UTC)

<p>DICOMInputPath ="   "<br>
volumeOutputPath = "  "<br>
slicer.modules.PythonInterfacerInstance.logic.Run(DICOMInputPath, volumeOutputPath)</p>
<p>this is the code in my batch file.<br>
if i run this batch file it runs perfectly, But if i invoke / call this batch file form my program/C# script . it gives me the second output.</p>

---

## Post #8 by @lassoan (2019-01-31 10:57 UTC)

<p>In this small piece of code there is nothing suspicious. Probably the problem is inside PythonInterfacerInstance.logic.</p>

---
