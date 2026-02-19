---
topic_id: 39605
title: "How To Interpolate Ct Scan Slices So I Can Plot It In 3D"
date: 2024-10-09
url: https://discourse.slicer.org/t/39605
---

# How to interpolate CT scan slices so i can plot it in 3D 

**Topic ID**: 39605
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/how-to-interpolate-ct-scan-slices-so-i-can-plot-it-in-3d/39605

---

## Post #1 by @Baron_Noam (2024-10-09 12:07 UTC)

<p>Hey I’m currently working on a personal project where i try to reconstruct CT scans image and the last part of my project include visualizing my reconstructed image in 3D. But i’m currently stuck, I successfully reconstructed all the slices of a brain scan i’m working with but to plot it in 3D i have to interpolate / create images between slice so that i have the same resolution in all dimensions. But interpolating naively with regard to the intensity values produces grey, sloppy and wrong values. instead of interpolating between the images i need to find a transformation that turns one slice into the next and incrementing this transformation to the right value so i end up with a new image at the right depth between the slices. I cannot seem to find how to code the transformation and apply it so i’m here seeking help, I don’t know if its the right place to ask this question as it’s my first time here, sorry for my english. I hope you can help me, and thank you for your attention. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>PS : i work in python, then i’m gonna work in C and i’m coding every function i’m not using pré-coded function from librairies</p>

---

## Post #2 by @lassoan (2024-10-10 04:44 UTC)

<p>If your slices are very far away from each other then no matter what interpolation you use, your segmentation will be low quality.</p>
<p>You can make it smooth, though, if you think that helps. One way to do that is to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">decreasing the spacing of the segmentation</a> and then use the Smoothing effect.</p>

---
