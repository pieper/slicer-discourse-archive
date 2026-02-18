# Draw tube for vessel segmentation: does not show

**Topic ID**: 35889
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/draw-tube-for-vessel-segmentation-does-not-show/35889

---

## Post #1 by @ILB (2024-05-03 11:34 UTC)

<p>Hi there!</p>
<p>I’ve been trying to work with Draw tube tool for a while. I’m currently working on vessel segmentation, and my goal is to draw a tube in those areas where there is a blood vessel, but the segmentation on the 3D model is incomplete.</p>
<p>However, when I add the fiducials and click apply, it does not show on the model. I noticed that this only happens when I add the fiducial on my model. If I place fiducials in a space not occupied by the model, the tube appears just fine.</p>
<p>How can I solve this?</p>
<p>Thank you in advance!</p>
<p>Here you have some images before and after clicking Apply</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0146e40f1db8d6d26738752e384248e830c9826.jpeg" data-download-href="/uploads/short-url/p7FO3mledr9ceHBC3XRWvpYjRDo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0146e40f1db8d6d26738752e384248e830c9826_2_690x257.jpeg" alt="image" data-base62-sha1="p7FO3mledr9ceHBC3XRWvpYjRDo" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0146e40f1db8d6d26738752e384248e830c9826_2_690x257.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0146e40f1db8d6d26738752e384248e830c9826_2_1035x385.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0146e40f1db8d6d26738752e384248e830c9826_2_1380x514.jpeg 2x" data-dominant-color="B6ADBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1837×685 83.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7b03290c03494d07a8175d1960e4dd0c0b9189.jpeg" data-download-href="/uploads/short-url/fLm4CjreetFPsh3K0DqWrc4OhCx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b03290c03494d07a8175d1960e4dd0c0b9189_2_690x260.jpeg" alt="image" data-base62-sha1="fLm4CjreetFPsh3K0DqWrc4OhCx" width="690" height="260" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b03290c03494d07a8175d1960e4dd0c0b9189_2_690x260.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b03290c03494d07a8175d1960e4dd0c0b9189_2_1035x390.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7b03290c03494d07a8175d1960e4dd0c0b9189_2_1380x520.jpeg 2x" data-dominant-color="B7AFC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×725 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-05-03 12:46 UTC)

<p>I suggest you read this small part of the documentation:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options</a></p>
<p>You’ll see that when you draw something within another segment using the current options, it will overwrite the existing segment. And since you use the same color, you can’t see it at all. Depending on your use case, either use a different color, or allow overlaps.</p>

---
