---
topic_id: 27658
title: "How To Display A Transformed Single Image In 3D View"
date: 2023-02-06
url: https://discourse.slicer.org/t/27658
---

# How to display a transformed single image in 3D view?

**Topic ID**: 27658
**Date**: 2023-02-06
**URL**: https://discourse.slicer.org/t/how-to-display-a-transformed-single-image-in-3d-view/27658

---

## Post #1 by @wrc (2023-02-06 13:40 UTC)

<p>Hi, I want to display one single 2D image in 3D view. I input the image as a volume node and apply a transform to it. However, if I try to make rotation / translation, the image in 3D view will become incomplete or disappeared. I think it is because the image in 3D view is only a slice with a fixed section and a limited area. How to display it under any transform? Thank you.</p>

---

## Post #2 by @RafaelPalomar (2023-02-08 06:08 UTC)

<p>Displaying objects in the 3D view may require re-centering the view.</p>
<p>There is a button in the 3D view widget for re-centering the view:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d11786b8dfbd99e99452de4e5d4333e6cb53354.png" alt="2b41629bf071c9b19a13136e63d509f1557e62e5" data-base62-sha1="1RBDvC0A6fPhZOnlqVLLGHXMDAM" width="223" height="91"><br>
<em>(extracted from <a href="https://discourse.slicer.org/t/how-from-python-scritps-to-trigger-the-click-function-of-center-of-the-3d-view-on-the-scene/8181/8" class="inline-onebox">How, from python-scritps, to trigger the click-function of "center of the 3D view on the scene"? - #8 by aiden.zhu</a>)</em></p>
<p>You can use the following python snippet if you prefer to do that programmatically (<em>from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#center-the-3d-view-on-the-scene" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></em>):</p>
<pre><code class="lang-python">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.resetFocalPoint()
</code></pre>

---

## Post #3 by @wrc (2023-02-08 12:31 UTC)

<p>Thank you. I tried the "center view: button. Only when both the image and its rotation are on the plane of the slice, it works. In other cases, the image will also become incomplete or disappeared. I am looking for a method which can reformat the slice according to a given transform.</p>

---

## Post #4 by @pieper (2023-02-08 12:53 UTC)

<p>The Slice views represent planes in patient space (RAS).  Your 2D image is also a plane in patient space, so if you move it with a transform it will no longer be the same as the slice view.  You can reset a slice view to match the displayed volume with the Rotate to volume plane button.  If you need to do this in python you can research the underlying logic API.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc27f7c495abb7e972ba367b29dba13abb405141.png" alt="image" data-base62-sha1="qQvouYfO9B1ec7Ba8l5EeDoHXzj" width="278" height="172"></p>

---
