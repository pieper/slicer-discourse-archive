---
topic_id: 20697
title: "Use Markups To Model Outside Of 3D Slicer"
date: 2021-11-19
url: https://discourse.slicer.org/t/20697
---

# Use Markups to Model outside of 3D Slicer

**Topic ID**: 20697
**Date**: 2021-11-19
**URL**: https://discourse.slicer.org/t/use-markups-to-model-outside-of-3d-slicer/20697

---

## Post #1 by @helenawill95 (2021-11-19 11:49 UTC)

<p>I found a similar feed but it wasn’t clear if the module was a public fn yet outside of the 3d slicer gui.</p>
<p>I am looking to use markups to model features, of translating several surface points, into a 3D mesh and then a binary 3D segmentation for CNN training.</p>
<p>I want to use the same functions as 3D Slicer’s module but in a python script run on my command line, as I will be training a network to identify some hyperparameters. Is this possible?<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2021-11-19 14:59 UTC)

<p>Most Slicer modules rely on many libraries that come bundled in Slicer and in general it would be hard to split out modules to run in other environments.  Instead it’s often easier to use Slicer’s python environment, either as a command line program (even with a hidden gui (e.g. with docker or xvfb) if gui-related features are needed) or by pip_installing machine learning libraries into Slicer’s python.  PyTorch and Tensorflow both work fine in Slicer, even with GPU drivers.</p>

---
