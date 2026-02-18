# ROI clipping in arbitrary direction (new feature)

**Topic ID**: 1310
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/roi-clipping-in-arbitrary-direction-new-feature/1310

---

## Post #1 by @muratmaga (2017-10-27 17:12 UTC)

<p>Hi,</p>
<p>I saw in the changelog under volume rendering, there is now a support for ROI clipping in arbitrary direction. I am testing the new stable version, and the crop box is not behaving any different than I am used to (i.e., it only expands and shrinks along the bounding box axes).<br>
Is this a different feature? How do I get that functionality?<br>
Thanks,<br>
M</p>

---

## Post #2 by @pieper (2017-10-27 17:26 UTC)

<p>Hi Murat -</p>
<p>You can put the ROI in a transform:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e525eafc9fbeafc155972dde78d5ad19d2697b3.jpeg" data-download-href="/uploads/short-url/4keNE478YnS2qXw6fn5smi4eHwT.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1e525eafc9fbeafc155972dde78d5ad19d2697b3_2_690x344.jpg" alt="image" data-base62-sha1="4keNE478YnS2qXw6fn5smi4eHwT" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1e525eafc9fbeafc155972dde78d5ad19d2697b3_2_690x344.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1e525eafc9fbeafc155972dde78d5ad19d2697b3_2_1035x516.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/1e525eafc9fbeafc155972dde78d5ad19d2697b3_2_1380x688.jpg 2x" data-dominant-color="A6A6AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1820×909 403 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pieper (2017-10-27 17:29 UTC)

<p>Note you can alse enable interaction with the transform in the “Display” tab that lets you rotate/scale/translate the ROI box for the transform in the 3D view which should be really useful.</p>

---

## Post #4 by @muratmaga (2017-10-27 17:55 UTC)

<p>I did not know that. Very very cool. Though the handle bars and outline gets a bit confusing. I can’t seem to control the extents of the ROI within the DIsplay tab of the Transform module. But definitely very useful.</p>

---

## Post #5 by @stevenagl12 (2018-08-03 02:17 UTC)

<p>How do you do this in the latest nightly builds with the newest transforms module?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778598a77ad6bdeb9bc193dcb1a6934a0f1972d6.png" data-download-href="/uploads/short-url/h3l2XxGeKU7UIgjaaLZkLprnIr4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778598a77ad6bdeb9bc193dcb1a6934a0f1972d6.png" alt="image" data-base62-sha1="h3l2XxGeKU7UIgjaaLZkLprnIr4" width="558" height="500" data-dominant-color="545456"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">711×637 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-08-03 09:33 UTC)

<p>You can only apply linear transforms to an ROI node.</p>

---

## Post #7 by @stevenagl12 (2018-08-03 11:58 UTC)

<p>Yes, but how can you apply them now as before you could see the angle of rotation to be applied, but I don’t see that anymore?</p>

---

## Post #8 by @stevenagl12 (2018-08-03 14:26 UTC)

<p>I apologize, my laptop had an old version of the nightly build and wasn’t working correctly. How do you reformat the off center cropped volume so that you can display it as if it’s in the normal cube format when you cropped it at an angle?</p>

---

## Post #9 by @lassoan (2018-08-03 17:39 UTC)

<p>Click on “Rotate to volume plane” button in the slice controller widget to align slice view with image axes.</p>
<p>Also, if you use a recent nightly version then in Segment Editor module you can see a warning button next to the master volume selector in case of non-image-axis-aligned slice views - clicking the button aligns the slice views.</p>

---
