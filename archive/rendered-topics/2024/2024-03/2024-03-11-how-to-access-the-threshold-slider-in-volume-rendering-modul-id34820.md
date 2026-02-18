# How to access the threshold slider in volume rendering module through python?

**Topic ID**: 34820
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/how-to-access-the-threshold-slider-in-volume-rendering-module-through-python/34820

---

## Post #1 by @ebin1234 (2024-03-11 12:30 UTC)

<p>Hello, I would like to know how to access the threshold  slider in volume rendering module through python. By changing the threshold values in the code will change the upper and lower limits of the slider. The scalar opacity mapping should shows step function in the graph.</p>

---

## Post #2 by @pieper (2024-03-11 12:37 UTC)

<p>The general guidelines are here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>

---

## Post #3 by @lassoan (2024-03-12 04:09 UTC)

<p>Shifting the transfer functions like the Shift slider does it in Volume Rendering module is a very finicky, unstable operation. The Volume Rendering module must be very general-purpose, so we don’t have much options. However, in your own module I would recommend to directly set the transfer function you want (similarly how it is done for example in <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ColorizeVolume/ColorizeVolume.py#L491-L544">Colorize volume module</a>).</p>

---
