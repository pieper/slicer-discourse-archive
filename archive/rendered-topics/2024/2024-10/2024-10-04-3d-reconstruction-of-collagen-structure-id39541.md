---
topic_id: 39541
title: "3D Reconstruction Of Collagen Structure"
date: 2024-10-04
url: https://discourse.slicer.org/t/39541
---

# 3D reconstruction of collagen structure

**Topic ID**: 39541
**Date**: 2024-10-04
**URL**: https://discourse.slicer.org/t/3d-reconstruction-of-collagen-structure/39541

---

## Post #1 by @papagalos21 (2024-10-04 12:30 UTC)

<p>Hello, I want to ask help for my project.</p>
<p>So i have a stack of images from the collagen structure in the abnominal aorta. The stack consists 81 images with 1μm between them. The size of each image is 500μm X 500μm.</p>
<p>I want to create the 3D structure of the collagen but when i insert the stack in the 3D Slicer the program set the step to 1mm and when i change this (“Volume Module” → " Volume information" → “Image spacing”) 3D slicer bugs and can’t process the info.</p>
<p>What can i do to solve this problem?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2024-10-04 13:22 UTC)

<p>Try the <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">ImageStacks</a> module in SlicerMorph.</p>

---

## Post #3 by @papagalos21 (2024-10-08 09:53 UTC)

<p>Thank you for your reply.</p>
<p>I follow the instructions for the SlicerMorph and i install it in my 3D slicer programm.</p>
<p>Now when i set the values for the spacing i get this error message:<br>
“Loading failed: could not broadcast input array from shape (20,256,1024,3) into shape (20,256)”</p>
<p>Do you know how can i solve this error??</p>
<p>Thank you</p>

---

## Post #4 by @pieper (2024-10-08 16:57 UTC)

<p>I’m not sure why you get that message.  Try the tutorial with sample data and confirm that works, then see what’s different with your data.  If you can’t figure it out then post example data that fails with step by step of what you tried, full error log, and any other info that might help debug (see the <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html">documentation</a> on how to get this info).</p>

---
