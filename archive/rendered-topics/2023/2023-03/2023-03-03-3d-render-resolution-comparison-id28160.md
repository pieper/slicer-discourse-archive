# 3D render resolution comparison

**Topic ID**: 28160
**Date**: 2023-03-03
**URL**: https://discourse.slicer.org/t/3d-render-resolution-comparison/28160

---

## Post #1 by @Cervantes (2023-03-03 17:17 UTC)

<p>Hi Everyone,<br>
I understand this may be less of a 3D slicer specific question, and more of a general resolution question.<br>
I’m working on something that includes using both 3D renders from DICOM images, and models created from a 3D scanner. I’m trying to find a way to compare the resolution of the rendering of both in Slicer.<br>
So far I’ve used the Volume module and looked at the information, and for the DICOM I get 512x512x427, but with my imported .obj model (of a different individual) I get measurements in mm^2 for the surface and mm^3 for the volume… but I need to know what the actual resolution of what I am seeing in the 3D render window, and the resolution of the screen grabs that I take from them so they can be compared.<br>
Thanks in advance for any help or input!</p>

---

## Post #2 by @RafaelPalomar (2023-03-06 06:14 UTC)

<p><a class="mention" href="/u/cervantes">@Cervantes</a>, 3D surface models, like the ones stored in <code>.obj</code> files do not have resolution in the same terms as medical images. While medical images are typically formed by a 3D matrix of voxels, 3D surface models are sets of 3D connected points.</p>
<p>If you want to know the resolution of the final rendering of the screen for either images or 3D surface models, you could use the 3D Slicer capture functionality (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html</a>). This, though, does not have to do that much with the underlying data, but with the rendering parameters like screen resolution, window size, etc., (i.e., you could render very poor images or models in very high screen resolution and vice-versa).</p>

---

## Post #3 by @tsehrhardt (2023-03-13 18:07 UTC)

<p>Meshlab lets you view models side by side–you can even link them so they move together if they are aligned. There are several filters that let you generate all kinds of mesh statistics: surface area, volume, triangle size, etc. Feel free to DM me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29eb242db3aa052e09ac5246a328adbf7fcddd15.jpeg" data-download-href="/uploads/short-url/5YPmAawsIStVn20Pesys962nL5X.jpeg?dl=1" title="2023-03-13_14-05-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29eb242db3aa052e09ac5246a328adbf7fcddd15_2_690x397.jpeg" alt="2023-03-13_14-05-30" data-base62-sha1="5YPmAawsIStVn20Pesys962nL5X" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29eb242db3aa052e09ac5246a328adbf7fcddd15_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29eb242db3aa052e09ac5246a328adbf7fcddd15_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29eb242db3aa052e09ac5246a328adbf7fcddd15_2_1380x794.jpeg 2x" data-dominant-color="6E6D95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-03-13_14-05-30</span><span class="informations">3376×1947 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
