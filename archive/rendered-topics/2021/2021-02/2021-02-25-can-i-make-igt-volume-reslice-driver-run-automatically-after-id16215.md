# Can I make IGT-Volume Reslice Driver run automatically after an event?

**Topic ID**: 16215
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/can-i-make-igt-volume-reslice-driver-run-automatically-after-an-event/16215

---

## Post #1 by @akshay_pillai (2021-02-25 16:01 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.11.20200930</p>
<p>I want to use the IGTs Volume Reslice driver to move along a transform path, I can do that manually by opening the volume reslice driver module and selecting the transform path and planes. But is there any way I can do that programmatically as soon as a transform is created? For example: I am using endoscopy module to create a transform curve and now I want the volume reslice driver to take the transform without me going into the module manually. Any help is appreciated. Thanks.</p>

---

## Post #2 by @lassoan (2021-02-25 16:33 UTC)

<p>This is implemented in <a href="https://github.com/vmtk/SlicerExtension-VMTK/tree/master/CrossSectionAnalysis">Cross section analysis module</a> in SlicerVMTK extension.</p>

---

## Post #3 by @akshay_pillai (2021-02-25 16:46 UTC)

<p>Thanks. I saw the Cross-section analysis module but it doesn’t seem to take the transform as an input. I was looking for something that takes a linear transforms node when it is created. Or maybe I don’t completely understand cross section analysis</p>

---

## Post #4 by @lassoan (2021-02-25 16:50 UTC)

<p>Cross-section analysis module shows how you can have volume reslicing functionality in a few lines of code, without relying on Volume reslice driver module. If you implement your own scripted module then it is probably simpler to reslice yourself than configure Volume reslice driver module.</p>

---
