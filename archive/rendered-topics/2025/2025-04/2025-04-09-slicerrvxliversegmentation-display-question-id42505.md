# SlicerRVXLiverSegmentation display question

**Topic ID**: 42505
**Date**: 2025-04-09
**URL**: https://discourse.slicer.org/t/slicerrvxliversegmentation-display-question/42505

---

## Post #1 by @feiyu (2025-04-09 15:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e7ddf80d7213009297d6b78ce5d79858b76c8c2.jpeg" data-download-href="/uploads/short-url/8UPhFmDcY8ptRaoQYjR78oVhJPI.jpeg?dl=1" title="3D11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e7ddf80d7213009297d6b78ce5d79858b76c8c2_2_690x371.jpeg" alt="3D11" data-base62-sha1="8UPhFmDcY8ptRaoQYjR78oVhJPI" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e7ddf80d7213009297d6b78ce5d79858b76c8c2_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e7ddf80d7213009297d6b78ce5d79858b76c8c2_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e7ddf80d7213009297d6b78ce5d79858b76c8c2_2_1380x742.jpeg 2x" data-dominant-color="595A68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D11</span><span class="informations">1851×996 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de8d496fa6b1e5d8f1e792709de8bdc467934998.jpeg" data-download-href="/uploads/short-url/vKMHEIvNLyRVNMqFdfd5bsYU3IA.jpeg?dl=1" title="3D22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8d496fa6b1e5d8f1e792709de8bdc467934998_2_690x334.jpeg" alt="3D22" data-base62-sha1="vKMHEIvNLyRVNMqFdfd5bsYU3IA" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8d496fa6b1e5d8f1e792709de8bdc467934998_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8d496fa6b1e5d8f1e792709de8bdc467934998_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de8d496fa6b1e5d8f1e792709de8bdc467934998_2_1380x668.jpeg 2x" data-dominant-color="323232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D22</span><span class="informations">1927×935 291 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’m really excited to encounter such an excellent liver segmentation module while attempting liver segmentation - it’s awesome! It achieves perfect segmentation in just 3 seconds. However, I’m facing an issue: When using the <em>SlicerRVXLiverSegmentation v1.1.0</em> extension, the 3D Viewer displays both the liver model and background skeletal structures, and I’m unsure how to remove the bone background. When using the <em>Segment Editor</em> extension, clicking the 3D Viewer shows blank images instead. Could you please guide me on how to resolve these issues?</p>

---

## Post #2 by @Thibault_Pelletier (2025-04-11 06:36 UTC)

<p>Hi <a class="mention" href="/u/feiyu">@feiyu</a>,</p>
<p>Thanks for your feedbacks!</p>
<p>In the segmentation editor, after clicking show 3D you should reset your 3D view so that it fits to the models (and other nodes) currently displayed in the view. This can be done by clicking in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#d-view" rel="noopener nofollow ugc">Center 3D view button</a> .</p>
<p>In the RVX plugin, the view is centered by default on the displayed volume and the rendering mode is set to MIP (Maximum Intensity Projection).<br>
The projection mode can be changed in the Volume Rendering module in the advanced / techniques options.<br>
Please refer to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" rel="noopener nofollow ugc">module’s documentation</a> if you need more information on this.</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @feiyu (2025-04-13 01:14 UTC)

<p>I’m really excited to encounter such an excellent liver segmentation module while attempting liver segmentation - it’s awesome! It achieves perfect segmentation in just 3 seconds. However, I’m facing an issue: When using the <em>SlicerRVXLiverSegmentation v1.1.0</em> extension, the 3D Viewer displays both the liver model and background skeletal structures, and I’m unsure how to remove the bone background. When using the <em>Segment Editor</em> extension, clicking the 3D Viewer shows blank images instead. Could you please guide me on how to resolve these issues?</p>

---

## Post #4 by @cpinter (2025-04-14 10:52 UTC)

<p>Please do not repost any question without changes. Also I recommend not giving titles like what you gave (“The extension is excellent, but there are bugs during use!”), it could not be less specific, and if I see it in an email subject I will surely pass by. I changed the title to something more meaningful. Unfortunately I cannot help with this extension, but flooding will surely not help. Thanks for understanding.</p>

---
