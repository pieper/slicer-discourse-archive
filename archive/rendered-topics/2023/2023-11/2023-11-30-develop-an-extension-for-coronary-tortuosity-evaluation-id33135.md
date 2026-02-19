---
topic_id: 33135
title: "Develop An Extension For Coronary Tortuosity Evaluation"
date: 2023-11-30
url: https://discourse.slicer.org/t/33135
---

# Develop an extension for coronary tortuosity evaluation

**Topic ID**: 33135
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/develop-an-extension-for-coronary-tortuosity-evaluation/33135

---

## Post #1 by @michelaf (2023-11-30 04:48 UTC)

<p>Hi everyone,</p>
<p>I am a first year PhD student in biomedical engineering. For my MSc thesis I worked with 3D Slicer to create an extension for an ongoing project at the local hospital.</p>
<p>The aim of the project is to develop a pipeline for the analysis of CCTA images to extract geometric features of the course of coronary vessels for generating coronary artery tortuosity indices and metrics. To achieve this goal, I created an extension (using Extension Wizard) consisting of two scripted modules:</p>
<p>The first module uses the logic of some SlicerVMTK modules (Vesselness Filtering, LevelSetSegmentation) to perform filtering and segmentation operations on a single vessel at a time. In some cases, I imported the logic of the different modules without modifications, while in other cases, I modified the code to be able to use features that couldn’t be accessed by only importing the logic (e.g., using the Curves method for model evolution).</p>
<p>The second module performs centerline’s extraction (and smoothing) and calculates a series of tortuosity indices. Then, it generates a table with all the calculated values and some plots (we are also trying to create a pdf report).</p>
<p>I worked by myself on this extension, and it was the first time I worked as a developer. Our research group’s goal is to make this pipeline public (we are also writing a paper) and then use it to apply tortuosity indices in various studies. However, this is an initial version and it’s based on some existing modules, so I don’t know how to proceed to make it public (maybe just the second module since the segmentation is already implemented in the vmtk extension?).</p>
<p>Thank you in advance for your help!</p>

---

## Post #2 by @pieper (2023-11-30 22:44 UTC)

<p>This sounds great, thanks for letting everyone know.  Based on what you have said, it would be great if you could invest time in adding this set of features to SlicerVMTK so that that extension becomes a full featured suite of vessel-related functionality.</p>
<p>If you aren’t ready to make that level of integration and your code is just python scripts you can easily distribute them via a github repository with instructions for how users can set module paths and test locally.</p>

---

## Post #3 by @michelaf (2023-12-01 09:12 UTC)

<p>Thank you for your reply!</p>
<p>I think we will start distributing the scripts via github following the second option you proposed. In the meantime, I’ll try to study the best way to improve the code and integrate the features into SlicerVMTK (maybe posting here if I need help).</p>

---

## Post #4 by @michelaf (2024-08-27 10:11 UTC)

<p>Hi everyone,</p>
<p>I just wanted to update the conversation with the link of the github repository. You can find the code of the extension <a href="https://github.com/mife-git/SlicerCATE" rel="noopener nofollow ugc">here</a>.</p>
<p>As already mentioned, this is currently a series of Python scripts. My goal is to improve my skills so that I can eventually integrate this into the SlicerVMTK extension. In the meantime, I hope you find this tool helpful!</p>

---
