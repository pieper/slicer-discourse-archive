# saveNode returns False

**Topic ID**: 20207
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/savenode-returns-false/20207

---

## Post #1 by @S_Arbabi (2021-10-18 16:13 UTC)

<p>Hi,</p>
<p>I’m saving a node as nrrd file, it returns False.<br>
All shown in here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f7deda3c7948a808747f45c682603d7b70a32b.png" data-download-href="/uploads/short-url/z6uxltT6GD5fGuUKHiAfSpBgiD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f7deda3c7948a808747f45c682603d7b70a32b_2_690x447.png" alt="image" data-base62-sha1="z6uxltT6GD5fGuUKHiAfSpBgiD" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f7deda3c7948a808747f45c682603d7b70a32b_2_690x447.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f7deda3c7948a808747f45c682603d7b70a32b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f7deda3c7948a808747f45c682603d7b70a32b.png 2x" data-dominant-color="CCCCCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×599 42.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any ideas?</p>
<p>Best</p>

---

## Post #2 by @S_Arbabi (2021-10-18 20:28 UTC)

<p>Update: I figured the solution, I just needed to create a labelmap segmentation node from the segmentation above and then save that labelmap to disk.</p>

---
