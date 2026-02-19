---
topic_id: 13764
title: "Is It Possible To Merge Multiple Labels Into One Label In A"
date: 2020-09-30
url: https://discourse.slicer.org/t/13764
---

# Is it possible to merge multiple labels into one label in a segmentation image?

**Topic ID**: 13764
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/is-it-possible-to-merge-multiple-labels-into-one-label-in-a-segmentation-image/13764

---

## Post #1 by @kevin.x (2020-09-30 01:56 UTC)

<p>Hi all,</p>
<p>I have an image with multiple labels and I want to merge them and label it as a single label. Is it possible for me to do it in 3D Slicer or ITK-SNAP?</p>
<p>Here is the image displaying in  3D Slicer and ITK-SNAP:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c019ac3643b5deb75b3deaddf170fc454f4522a.png" data-download-href="/uploads/short-url/aQnIYIGzwfF8LHdIh1LVUJT6UK6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c019ac3643b5deb75b3deaddf170fc454f4522a_2_690x447.png" alt="image" data-base62-sha1="aQnIYIGzwfF8LHdIh1LVUJT6UK6" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c019ac3643b5deb75b3deaddf170fc454f4522a_2_690x447.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c019ac3643b5deb75b3deaddf170fc454f4522a_2_1035x670.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c019ac3643b5deb75b3deaddf170fc454f4522a_2_1380x894.png 2x" data-dominant-color="5F5F6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2024×1314 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6a82c19500a17aaab18a070e18c1b05f3417ccf.jpeg" data-download-href="/uploads/short-url/nMjzbtK4r2hve3iGWa9eHcJdm7t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6a82c19500a17aaab18a070e18c1b05f3417ccf_2_690x474.jpeg" alt="image" data-base62-sha1="nMjzbtK4r2hve3iGWa9eHcJdm7t" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6a82c19500a17aaab18a070e18c1b05f3417ccf_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6a82c19500a17aaab18a070e18c1b05f3417ccf_2_1035x711.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a6a82c19500a17aaab18a070e18c1b05f3417ccf_2_1380x948.jpeg 2x" data-dominant-color="686867"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2102×1446 379 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It seems a silly question but I am stuck in it and I didn’t find a solution after searching online for a long time. Much appreciated for your help!</p>

---

## Post #2 by @timeanddoctor (2020-09-30 09:18 UTC)

<p>Yes, you can do it in slicer simply.<br>
If you just want get a model, you can merger them into one model in surfacetool.<br>
And if you tend to get a label you can convert them as a segment and then have a booloperation to get a one segment and convert back to a label.<br>
Good luck!</p>

---
