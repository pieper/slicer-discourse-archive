# Define the user-defined item in the Stereo viewing icon of 3D view 

**Topic ID**: 28297
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/define-the-user-defined-item-in-the-stereo-viewing-icon-of-3d-view/28297

---

## Post #1 by @TerryHuang (2023-03-10 20:19 UTC)

<p>Hi. In the user interface, the 3D view of the scene has a panel for configuring the 3D View. In the Stereo viewing icon of the panel, there are some models like Red/blue and anaglyph modes, also user defined 1, 2, and 3. Does anyone know how to program the user-defined item? I have a special stereo display device, which needs to use four views to render the display image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fe75dd71d6dc06706d8357714224822a1eb6a9b.jpeg" data-download-href="/uploads/short-url/iful2mhTLd24RHTHJ1j6iWy5Ymv.jpeg?dl=1" title="Snipaste_2023-03-09_22-02-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fe75dd71d6dc06706d8357714224822a1eb6a9b_2_690x390.jpeg" alt="Snipaste_2023-03-09_22-02-49" data-base62-sha1="iful2mhTLd24RHTHJ1j6iWy5Ymv" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fe75dd71d6dc06706d8357714224822a1eb6a9b_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fe75dd71d6dc06706d8357714224822a1eb6a9b_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7fe75dd71d6dc06706d8357714224822a1eb6a9b_2_1380x780.jpeg 2x" data-dominant-color="A09FC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snipaste_2023-03-09_22-02-49</span><span class="informations">1920×1087 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-11 07:06 UTC)

<p>This API was added in early stages of experimenting with virtual reality (it might have been for <a href="https://github.com/franklinwk/SlicerVirtualRealityViewer">this</a>). Nowadays we use OpenVR, OpenXR, LookingGlass, etc. renderwindow classes instead.</p>

---

## Post #3 by @TerryHuang (2023-03-11 09:29 UTC)

<p>Thank you very much to your nice reply. I try the LookingGlass extension, it seem what i need. But to get a right 3d perception,  the LookingGlass extension need a LookingGlass device, which i donot have.  What i can get now is a multiple view window. I wonder if there is a way to modify the looking glass API to achieve the 3D effect I need, without the need for looking glass hardware devices?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0b23ac3f2a2a1df75e4266479edc5ad60a93661.jpeg" data-download-href="/uploads/short-url/w3KO7CPwMKmAubM8fzOBiWnahlD.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b23ac3f2a2a1df75e4266479edc5ad60a93661_2_690x361.jpeg" alt="1" data-base62-sha1="w3KO7CPwMKmAubM8fzOBiWnahlD" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b23ac3f2a2a1df75e4266479edc5ad60a93661_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b23ac3f2a2a1df75e4266479edc5ad60a93661_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0b23ac3f2a2a1df75e4266479edc5ad60a93661_2_1380x722.jpeg 2x" data-dominant-color="8F90A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1007 86.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-03-11 16:40 UTC)

<p>Yes, sure, all software (Slicer, VTK, LookingGlass remote module) are free, unrestricted open-source software, so you can modify anything locally as you see fit.</p>

---
