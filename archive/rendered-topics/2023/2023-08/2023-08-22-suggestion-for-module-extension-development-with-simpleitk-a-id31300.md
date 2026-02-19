---
topic_id: 31300
title: "Suggestion For Module Extension Development With Simpleitk A"
date: 2023-08-22
url: https://discourse.slicer.org/t/31300
---

# Suggestion for Module Extension Development with SimpleITK and ITK-elastix

**Topic ID**: 31300
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/suggestion-for-module-extension-development-with-simpleitk-and-itk-elastix/31300

---

## Post #1 by @calici (2023-08-22 19:53 UTC)

<p>Hi,</p>
<p>I would like to develop a module extension in 3D slicer for projecting planned needle trajectories to current image by registering pre-operative CT to intra-operative CT.</p>
<p>I have already object-oriented python scripts with many classes and functions for registration, image processing and visualization. For image processing I am using SimpleITK functions and for registration I am using itk-elastix.</p>
<p>I would like to incorporate all these functionalities in this module. However I am having a bit hard time to constuct general pipeline.</p>
<p>My first idea was to install SimpleITK and itk-elastix packages and write everything in the Logic class but I could not install itk-elastix. Since there is already Elastix module in Slicer, I guess I can use that module in my custom module.</p>
<p>What would be your suggestions for creating such an extension?</p>
<p>How can I bundle my module with external python packages for example itk-elastix?</p>
<p>Thank you!</p>

---
