# Nvidia AI-assisted annotation of liver CT

**Topic ID**: 21661
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/nvidia-ai-assisted-annotation-of-liver-ct/21661

---

## Post #1 by @muzahem (2022-01-27 16:21 UTC)

<p>Hello,</p>
<p>I wanted to try the liver segmentation with AIAA. I downloaded the extension and runned a sample data from 3d slicer. In “Segment from boundary points” the function “annotation ct liver” is not showing.<br>
Was the function deleted ?</p>

---

## Post #2 by @lassoan (2022-01-28 23:02 UTC)

<p>Nvidia dropped many models when they changed their backend from Tensorflow to Pytorch/MONAI. Therefore, the Slicer NvidiaAIAA demo server (which uses the latest server version) cannot offer these models anymore. Most of Nvidia development effort is now focused on MONAILabel, so you either need to train your own models or you need to switch to use MONAILabel.</p>

---
