# Saved linearly transformed images change orientation

**Topic ID**: 43250
**Date**: 2025-06-06
**URL**: https://discourse.slicer.org/t/saved-linearly-transformed-images-change-orientation/43250

---

## Post #1 by @NinaO (2025-06-06 17:47 UTC)

<p>Dear 3D Slicer Community</p>
<p>I tried searching through previous topics, but did not find an answer to my problem.</p>
<p>I had a few images I needed to manually rotate so they have approximately the same orientation. For this I first centered the volume of the image, created a Lineartransform, moved the image file under the lineartransform whereby I hardened the centered volume transform. I then manually transformed the image to how I wanted it to be. When done, I hardened the image and saved both the scene, the lineartransform, the center transform and the now transformed image (nii.gz).<br>
However, afterwards if I open only the transformed image in a new slicer window, the transformation seems to have been improperly saved and has slightly rotated… If I open the scene in another slicer window, the image looks fine.<br>
I drew a little schematic example of what I mean.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ebd15d0d4427c43a764131149747a245dc901f.jpeg" data-download-href="/uploads/short-url/rFvo7VtL3ONw3xJzA68Uo47Yp2L.jpeg?dl=1" title="transform slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ebd15d0d4427c43a764131149747a245dc901f_2_690x268.jpeg" alt="transform slicer" data-base62-sha1="rFvo7VtL3ONw3xJzA68Uo47Yp2L" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ebd15d0d4427c43a764131149747a245dc901f_2_690x268.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ebd15d0d4427c43a764131149747a245dc901f_2_1035x402.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1ebd15d0d4427c43a764131149747a245dc901f_2_1380x536.jpeg 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">transform slicer</span><span class="informations">2604×1015 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How to solve this, and make sure that my transformed image gets saved properly?</p>
<p>Thank you for the help!</p>

---

## Post #2 by @lassoan (2025-06-06 17:53 UTC)

<p>When you display an image, slice views are automatically aligned with the volume axes by default. You can either disable this “Reset view orientation on show” feature or you can resample the image (for example, using Crop volume module). See more details in this discussion: <a href="https://discourse.slicer.org/t/how-to-make-the-image-load-with-the-new-default-axis-position/20818" class="inline-onebox">How to make the image load with the new default axis position</a></p>

---

## Post #3 by @NinaO (2025-06-10 13:25 UTC)

<p>Thank you very much for the reply. Disabling “reset view orientation on show” works when working in the scene, but does not influence the save file or opening of the save file. Is there a setting to disable reset view orientation on show before opening them?<br>
(Resampling was so far not successful for me, and I would like to avoid cropping if possible.)</p>

---
