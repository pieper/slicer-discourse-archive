---
topic_id: 29796
title: "Mask Volume With Another Preset"
date: 2023-06-02
url: https://discourse.slicer.org/t/29796
---

# Mask volume with another preset

**Topic ID**: 29796
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/mask-volume-with-another-preset/29796

---

## Post #1 by @dbtruong (2023-06-02 10:29 UTC)

<p>Hello All, I am trying to use mask volume with CT-Muscle preset. Why is the result below?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e541e04e469e5b6b7e175f07db3b7c46057ee09.jpeg" data-download-href="/uploads/short-url/dst6musqfwIVgB555SEq1iKzkox.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e541e04e469e5b6b7e175f07db3b7c46057ee09_2_690x400.jpeg" alt="image" data-base62-sha1="dst6musqfwIVgB555SEq1iKzkox" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e541e04e469e5b6b7e175f07db3b7c46057ee09_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e541e04e469e5b6b7e175f07db3b7c46057ee09_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e541e04e469e5b6b7e175f07db3b7c46057ee09.jpeg 2x" data-dominant-color="CBC7D2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1125×653 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks.</p>

---

## Post #2 by @lassoan (2023-06-02 14:45 UTC)

<p>It seems that you filled the volume with value = 0. In clinical CT images the voxel values are in HU, therefore you filled the image with water/soft tissue. You may want to use -1000 to fill with air instead.</p>
<p>Choosing the same volume for input and output is risky, as you cannot undo your changes. I would recommend to load the input volume again (so that you restore the masked parts) and create a new output volume and use volume rendering on the masked volume.</p>
<p>You can follow the steps of this tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---

## Post #3 by @dbtruong (2023-06-02 15:15 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Thanks a lot for your explanation and advice</p>

---
