---
topic_id: 42672
title: "Gesture Of Libs Path And Dlls While Developing"
date: 2025-04-24
url: https://discourse.slicer.org/t/42672
---

# Gesture of libs, path and DLLs while developing

**Topic ID**: 42672
**Date**: 2025-04-24
**URL**: https://discourse.slicer.org/t/gesture-of-libs-path-and-dlls-while-developing/42672

---

## Post #1 by @Theophanis_Eleftheri (2025-04-24 03:29 UTC)

<p>Hello,<br>
I’m trying to develop an extension for 3D Slicer using torch and many other libs. Those libs are currently installed in a conda environment (I have a plenty depending on the project). I’d like to develop my extension but if I do execute it in slicer, even after adding the site package of my env in my sys.path, torch isn’t imported because slicer doesn’t know where are the DLLs that torch uses. And if I try to do it in my IDE I have the same problem with Slicer’s and VTK’s DLLS. Is there a clean way to organize my libraries or to give access to my conda env to slicer?</p>
<p>Thanks for your ideas and answers!</p>

---

## Post #2 by @lassoan (2025-04-24 03:41 UTC)

<p>Conda is gnerally not playing nice with other sofware. On Windows, it pretty much takes over your computer and modifies how your computer uses Python by overwriting, overriding, injecting various system settings. This may work fine on a developer’s computer, but not for end-user deployments. I would recommend to use stock Python instead of conda.</p>
<p>Slicer provides a virtual Python environment, where you can pip-install any Python packages (including pytorch). So, usually the easiest is to just use this environment.</p>

---
