---
topic_id: 28726
title: "Run A 3D Slicer Module Multiple Times On Different Scans"
date: 2023-04-03
url: https://discourse.slicer.org/t/28726
---

# Run a 3D Slicer module multiple times on different scans

**Topic ID**: 28726
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/run-a-3d-slicer-module-multiple-times-on-different-scans/28726

---

## Post #1 by @rahulhere (2023-04-03 11:29 UTC)

<p>Hi Team,</p>
<p>I need to use the N4ITK MRI Bias correction module of 3D slicer. I have multiple scans on which I want to use the Module. Is there a way to automate running the module on multiple scans (looping basically) and also saving the results back to the system ?</p>
<p>Thanks a lot in Advance.</p>

---

## Post #2 by @rbumm (2023-04-03 12:12 UTC)

<p>Absolutely, but there is a Python script required to establish this. It needs to be run from the 3D Slicer  Python Console.<br>
See <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/66dfec4b810f38a2b4fd1a6e6af53815b398d874/LungCTAnalyzer/LungCTAnalyzer.py#L735">how we did</a> it for the Lung CT Analyzer extension.  You recursively scan your input directory for input files, process them, and save results to the output folder.</p>

---

## Post #3 by @marwanabb (2023-04-11 14:38 UTC)

<p>This link might be useful also : <a href="https://discourse.slicer.org/t/how-to-segment-multiple-volumes-at-once/10280" class="inline-onebox">How to segment multiple volumes at once?</a></p>

---
