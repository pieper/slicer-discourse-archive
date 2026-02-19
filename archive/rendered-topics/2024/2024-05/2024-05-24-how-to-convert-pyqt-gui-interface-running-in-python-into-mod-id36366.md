---
topic_id: 36366
title: "How To Convert Pyqt Gui Interface Running In Python Into Mod"
date: 2024-05-24
url: https://discourse.slicer.org/t/36366
---

# How to convert PyQt Gui interface running in python into module in 3D slicer

**Topic ID**: 36366
**Date**: 2024-05-24
**URL**: https://discourse.slicer.org/t/how-to-convert-pyqt-gui-interface-running-in-python-into-module-in-3d-slicer/36366

---

## Post #1 by @Cathy123 (2024-05-24 08:08 UTC)

<p>I have a GUI interface that can be runned in Python. Now I hope to intergrate the GUI into 3Dslicer. How to do it. My gui was based on PyQt5 and vtk package and 3D slicer doesn’t support PyQt5, so how to do it.My file is attached.<br>
Another question is how to load an obj file as segmentation directly into 3D slicer with programming.<br>
Thank you.<a href="https://drive.google.com/file/d/1o7Zn9G18oXvwpbvFiBw1wL5YhX0mfUm4/view?usp=sharing" rel="noopener nofollow ugc">PyQt5 code file.</a></p>

---

## Post #2 by @pieper (2024-05-24 14:00 UTC)

<p>From a quick look it seems your code doesn’t use much Qt, so that part of the porting may be easy.  On the other hand you are doing lower-level VTK event processing and that may be harder to integrate in Slicer’s regular 3D views since events need to be managed carefully.  On the other hand if you just wanted to pop up an independent 3d view window you could basically use the code you already have.</p>
<p>I didn’t look in detail, but it seems you are working with shortest paths on surfaces, so maybe Slicer’s curve markups can already do some of what you need.  What’s the purpose of your program?</p>

---

## Post #3 by @Akiragi (2024-06-14 07:03 UTC)

<aside class="quote no-group" data-username="Cathy123" data-post="1" data-topic="36366">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e8c25b/48.png" class="avatar"> Cathy123:</div>
<blockquote>
<p>I have a GUI interface that can be runned in Python. Now I hope to intergrate the GUI into 3Dslicer. How to do it. My gui was based on PyQt5 and vtk package and 3D slicer doesn’t support PyQt5, so how to do it.My file is attached.<br>
Another question is how to load an obj file as segmentation directly into 3D slicer with programming.</p>
</blockquote>
</aside>
<p>According to me Integrating a PyQt5  grounded GUI into 3D Slicer can be  grueling  since 3D Slicer does not support PyQt5 directly. I have a ans for your first question. You can follow this   Since 3D Slicer uses Qt, you might need to rewrite your GUI to use the Qt classes that 3D Slicer supports. This will allow  flawless integration;   You can integrate your VTK  grounded visualizations into 3D Slicer by creating custom modules. relate to the 3D Slicer attestation for guidance on creating scripted modules using Python.</p>

---
