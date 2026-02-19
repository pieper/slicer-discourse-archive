---
topic_id: 13978
title: "Using One Segmentation To Subtract Out From Another During T"
date: 2020-10-10
url: https://discourse.slicer.org/t/13978
---

# Using one segmentation to subtract out from another during thresholding

**Topic ID**: 13978
**Date**: 2020-10-10
**URL**: https://discourse.slicer.org/t/using-one-segmentation-to-subtract-out-from-another-during-thresholding/13978

---

## Post #1 by @Stone18jo (2020-10-10 18:28 UTC)

<p>Hello all!</p>
<p>I am trying to create 2 separate models for teeth that are biting together (occluding).  It takes a while to isolate the lower teeth.  Because they are touching, I then have to repeat the process.  Instead I would like to use the lower jaw segmentation to subtract out that area on the upper jaw, to make it a faster process.  On the attached photos, I want to use the cyan color to subtract out the green color.  I appreciate the help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0cf12cb832e450ee26d53e4db56ee0b81de8f90.png" data-download-href="/uploads/short-url/w4KBzYhxPzfYJXnmzwGs0mZAhP2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0cf12cb832e450ee26d53e4db56ee0b81de8f90_2_614x500.png" alt="image" data-base62-sha1="w4KBzYhxPzfYJXnmzwGs0mZAhP2" width="614" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0cf12cb832e450ee26d53e4db56ee0b81de8f90_2_614x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0cf12cb832e450ee26d53e4db56ee0b81de8f90.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0cf12cb832e450ee26d53e4db56ee0b81de8f90.png 2x" data-dominant-color="889DC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">619×504 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d34504d31caae93982d427e27312299bd82e9e0.jpeg" data-download-href="/uploads/short-url/mqH2KFoNtXqKKH9AowWi5UGeRri.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d34504d31caae93982d427e27312299bd82e9e0_2_496x500.jpeg" alt="image" data-base62-sha1="mqH2KFoNtXqKKH9AowWi5UGeRri" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d34504d31caae93982d427e27312299bd82e9e0_2_496x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d34504d31caae93982d427e27312299bd82e9e0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d34504d31caae93982d427e27312299bd82e9e0.jpeg 2x" data-dominant-color="4B4F4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">713×718 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf38749672d20dbf9ace184356351249c9c0004.jpeg" data-download-href="/uploads/short-url/dghGrDpGR4BRHk6iqZGQr54lvwg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cf38749672d20dbf9ace184356351249c9c0004_2_456x500.jpeg" alt="image" data-base62-sha1="dghGrDpGR4BRHk6iqZGQr54lvwg" width="456" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cf38749672d20dbf9ace184356351249c9c0004_2_456x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cf38749672d20dbf9ace184356351249c9c0004_2_684x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf38749672d20dbf9ace184356351249c9c0004.jpeg 2x" data-dominant-color="3A463E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">748×820 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-10 18:59 UTC)

<p>You can use “Logical operators” effect to subtract one segment from another.</p>

---

## Post #3 by @Stone18jo (2020-10-11 15:27 UTC)

<p>Thanks!  This worked perfectly.  Saves quite a bit of time.  Take care.</p>

---
