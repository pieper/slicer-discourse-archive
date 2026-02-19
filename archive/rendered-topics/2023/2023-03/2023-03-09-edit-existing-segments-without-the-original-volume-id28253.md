---
topic_id: 28253
title: "Edit Existing Segments Without The Original Volume"
date: 2023-03-09
url: https://discourse.slicer.org/t/28253
---

# Edit existing segments without the original volume

**Topic ID**: 28253
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/edit-existing-segments-without-the-original-volume/28253

---

## Post #1 by @Melanie (2023-03-09 08:13 UTC)

<p>Hi Have few segmented bones which are not correctly segmented. The outline has holes. I would like to correct them by solidifying them, correcting the outline. However I do not have the original 3D CT volume for these. Is there a way I could do this please</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4900a50636be450ef82c8bbd83b3c38466994df.jpeg" data-download-href="/uploads/short-url/ntMUqem70VOgLRXitS4vIFzudxd.jpeg?dl=1" title="Screen Shot 2023-03-09 at 6.42.43 pm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4900a50636be450ef82c8bbd83b3c38466994df_2_690x195.jpeg" alt="Screen Shot 2023-03-09 at 6.42.43 pm" data-base62-sha1="ntMUqem70VOgLRXitS4vIFzudxd" width="690" height="195" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4900a50636be450ef82c8bbd83b3c38466994df_2_690x195.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4900a50636be450ef82c8bbd83b3c38466994df_2_1035x292.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4900a50636be450ef82c8bbd83b3c38466994df_2_1380x390.jpeg 2x" data-dominant-color="5F6065"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-09 at 6.42.43 pm</span><span class="informations">1920×545 45.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @tsehrhardt (2023-03-13 17:59 UTC)

<p>If you are familiar with Meshlab, that might be the fastest option. You can use:</p>
<ul>
<li>
<p>Filters–&gt;</p>
</li>
<li>
<p>Remeshing, Simplification, and Reconstruction–&gt;</p>
</li>
<li>
<p>Surface Reconstruction: Screened Poisson</p>
</li>
<li>
<p>Try different Reconstruction depths: 8, 9, or 10.</p>
</li>
</ul>
<p>In Slicer, you can try the Fill Holes tool in the Surface Toolbox. You’re missing quite a bit though.</p>

---

## Post #3 by @Melanie (2023-03-17 10:08 UTC)

<p>Thanks for your reply,</p>
<p>Yes I think its quite challenging to fill without the original volume.</p>

---
