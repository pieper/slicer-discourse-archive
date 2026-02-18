# 3D Slicer not responding on cuts with scissor tool and quantification

**Topic ID**: 20096
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/3d-slicer-not-responding-on-cuts-with-scissor-tool-and-quantification/20096

---

## Post #1 by @ErikW (2021-10-11 06:24 UTC)

<p>Hello, new user here. As the title states, the program becomes unresponsive when these features are used. Hardware is not the issue as I have a rather capable computer</p>

---

## Post #2 by @lassoan (2021-10-11 14:19 UTC)

<p>By “not responding” do you mean the action has no effect or that the application hangs?</p>
<p>What operating system and Slicer version do you use?</p>
<p>What is the size of the segmented image? How much RAM does your computer have?</p>

---

## Post #3 by @ErikW (2021-10-11 15:55 UTC)

<p>By not responding I mean the application hangs and it says not responding at the top of the window.  I use windows 10, slicer 4.11.20210226 and have 16 gigabytes of ram. The segmented image is just over 2.5 gigabytes.  Thank you for your response!</p>

---

## Post #4 by @lassoan (2021-10-11 19:55 UTC)

<p>If you want to make sure that you don’t run out of memory then you need to have about 10x more memory space than your image size. For example, if you use the Segment Editor then you need to have source for saving undo states, multiple layers for overlapping segments, etc. Therefore, 16GB RAM may not be sufficient for  a 2.5GB image.</p>
<p>Adding 16GB more RAM or configure that much extra virtual memory/swap space should fix the issue.</p>
<p>Alternatively, you can use Crop volume to crop and/or resample the volume to reduce its size.</p>

---
