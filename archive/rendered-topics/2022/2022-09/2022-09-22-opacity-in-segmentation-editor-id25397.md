---
topic_id: 25397
title: "Opacity In Segmentation Editor"
date: 2022-09-22
url: https://discourse.slicer.org/t/25397
---

# opacity in segmentation editor

**Topic ID**: 25397
**Date**: 2022-09-22
**URL**: https://discourse.slicer.org/t/opacity-in-segmentation-editor/25397

---

## Post #1 by @davidP (2022-09-22 13:51 UTC)

<p>IN the (very helpful) documentation they describe a setting for OPACITY as well as a variety of functions for REPRESENTATIONS and other things…but I do not see any of that on my screen.  Am I missing something? Wrong version? (I have the latest one  available…)</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2022-09-22 19:55 UTC)

<p>If you want to set the opacity different for each segment differently, switch to the Segmentations module which gives you full control about display settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/931afa2c24da2f21d8761d959de0f43e4ea99fef.png" data-download-href="/uploads/short-url/kZlZayDsvu3r7IFykE3mhLujArJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/931afa2c24da2f21d8761d959de0f43e4ea99fef_2_481x500.png" alt="image" data-base62-sha1="kZlZayDsvu3r7IFykE3mhLujArJ" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/931afa2c24da2f21d8761d959de0f43e4ea99fef_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/931afa2c24da2f21d8761d959de0f43e4ea99fef_2_721x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/931afa2c24da2f21d8761d959de0f43e4ea99fef.png 2x" data-dominant-color="E4EBF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">798×828 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @davidP (2022-09-22 22:10 UTC)

<p>Awesome!!  Thank you so much<br>
IS there a way to save a segment with a specific opacity when it is exported?  We bring them in to XR and would like to be able to have certain segments "semi-transparent’ in the actual XR view so structures inside can be seen (like a tumor inside the liver)</p>
<p>Thank you!!</p>

---

## Post #4 by @lassoan (2022-09-22 22:34 UTC)

<p>Opacity (and all display properties other than color) is stored in the display node in the .mrml file. However, you can export to .gltf or .OBJ format using SlicerOpenAnatomy extension and these files store color and opacity (.gltf also saves segment names and hierarchy).</p>

---

## Post #5 by @davidP (2022-09-23 19:44 UTC)

<p>I really appreciate your help so much…<br>
So, I loaded the SlicerOpenAnatomy extension and used it to export the files.<br>
When I exported it in .obj it did not show opacity,  but it did create an .mtl file for color<br>
When I exported it as .gtlf it is a single file, with color, but without the opacity.</p>
<p>Am I doing something wrong?</p>
<p>Thank you so much!!</p>

---
