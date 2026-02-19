---
topic_id: 19047
title: "Tiff Stack Loading Problem 1 View Strange"
date: 2021-08-04
url: https://discourse.slicer.org/t/19047
---

# Tiff Stack Loading Problem - 1 view strange

**Topic ID**: 19047
**Date**: 2021-08-04
**URL**: https://discourse.slicer.org/t/tiff-stack-loading-problem-1-view-strange/19047

---

## Post #1 by @ebryson (2021-08-04 00:26 UTC)

<p>Hi,<br>
I loaded a tiff stack with Image Stacks, the files were in order and I think the spacing is correct but my middle view as you can see from the photo is not the mouse skulls… any idea where I went wrong? (The far right view is also double-image, only the far left view is correct.)</p>
<p>Thanks for the help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9afff2d95f30c5e87e818ed94c5f244c31a7377.jpeg" data-download-href="/uploads/short-url/quFp0J8lmcjYFUCrYLjx5fY24o7.jpeg?dl=1" title="Screen Shot 2021-08-03 at 8.23.10 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9afff2d95f30c5e87e818ed94c5f244c31a7377_2_690x226.jpeg" alt="Screen Shot 2021-08-03 at 8.23.10 PM" data-base62-sha1="quFp0J8lmcjYFUCrYLjx5fY24o7" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9afff2d95f30c5e87e818ed94c5f244c31a7377_2_690x226.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9afff2d95f30c5e87e818ed94c5f244c31a7377_2_1035x339.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b9afff2d95f30c5e87e818ed94c5f244c31a7377_2_1380x452.jpeg 2x" data-dominant-color="7F7F7F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-08-03 at 8.23.10 PM</span><span class="informations">1920×629 60.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-08-04 00:58 UTC)

<p>These are shadow images (sinogram) you need to recostruct them into slices first for you to load them into Slicer.</p>

---

## Post #3 by @ebryson (2021-08-04 01:02 UTC)

<p>Thank you! Do you know if a tutorial exists yet on how to do that, I haven’t had shadow images before so I’m not sure how to fix it.</p>

---

## Post #4 by @muratmaga (2021-08-04 01:14 UTC)

<p>That is vendor specific. You should check with the lab that generated the images. It is uncommon to just give the shadow images to a researcher.</p>

---

## Post #5 by @ebryson (2021-08-04 01:15 UTC)

<p>Will do, thanks so much for the help.</p>

---
