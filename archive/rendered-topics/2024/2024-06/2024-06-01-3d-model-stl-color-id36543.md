# 3D model STL color

**Topic ID**: 36543
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/3d-model-stl-color/36543

---

## Post #1 by @Assaad (2024-06-01 22:00 UTC)

<p>Hi,<br>
I have a question about the 3D model export into STL file<br>
I have no problem with exporting the 3D model<br>
However, when I include it into a powerpoint presentation, the 3D model is all time in gray color and I can not conserve the color used in the segmentation.<br>
Please can You help me !</p>

---

## Post #2 by @lassoan (2024-06-01 22:10 UTC)

<p>STL file can only store the surface geometry and nothing else (no colors, no material properties, no lighting, …). If you cannot find a way to set these in powerpoint then you can try to export as obj or glTF format (using OpenAnatomy extension), which preserve color.</p>

---

## Post #3 by @Assaad (2024-06-02 06:40 UTC)

<p>Thank you so much it works with an obj file but I did not find the extension OpenAnatomy in the extension list. How can I get it?</p>

---

## Post #4 by @lassoan (2024-06-02 12:59 UTC)

<p>You can use the search box:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56546107a5493573d98d7a1fc0ba33942be195c8.png" data-download-href="/uploads/short-url/cjHQj6UFSvhwqjuCHQMB2vDqDH2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56546107a5493573d98d7a1fc0ba33942be195c8_2_641x500.png" alt="image" data-base62-sha1="cjHQj6UFSvhwqjuCHQMB2vDqDH2" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56546107a5493573d98d7a1fc0ba33942be195c8_2_641x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56546107a5493573d98d7a1fc0ba33942be195c8_2_961x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56546107a5493573d98d7a1fc0ba33942be195c8_2_1282x1000.png 2x" data-dominant-color="252728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2509×1955 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Assaad (2024-06-03 16:28 UTC)

<p>I finally downloaded the extension. Please if you have any tutorial or youtube video link for how to use this extension please share it with me.</p>

---

## Post #6 by @lassoan (2024-06-04 16:05 UTC)

<p>You can find all information in the <a href="https://github.com/PerkLab/SlicerOpenAnatomy?tab=readme-ov-file#slicer-open-anatomy-extension">extension documentation</a>. If anything is not clear then you can ask here.</p>

---
