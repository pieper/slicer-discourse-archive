---
topic_id: 19218
title: "Registering Only One Branch Of A Segment"
date: 2021-08-16
url: https://discourse.slicer.org/t/19218
---

# Registering only one branch of a segment

**Topic ID**: 19218
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/registering-only-one-branch-of-a-segment/19218

---

## Post #1 by @parvaneh.a (2021-08-16 22:59 UTC)

<p>Operating system:ubuntu<br>
Slicer version:<br>
Expected behavior:Registering only one branch of a segment<br>
Actual behavior:</p>
<p>Hi, I have a segment like the figure below. As you see there are four branches connected to the main body. I would like to do the registration of each branch individually in a way that the ostia plate where the point F1 is located be still connected to the main body and only the purposed branch (for example the upper left) moves in registration.<br>
If I do the fiducial point regsitration with this two points on the template and moving image,  the whole body and the other branches also moves while I want them to be fixed. Is there any way that I be able to do so?<br>
the registration method can be fiducial point-based, affine or non-rigid. I would be thankful if you could let me know if you have any idea.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52e5d276931199ee2d56f95128de75b9c1a92439.jpeg" alt="Screenshot from 2021-08-16 18-49-25" data-base62-sha1="bPlxJUy7vrSR6ZhxtOEkBSofBFL" width="631" height="490"></p>

---

## Post #2 by @lassoan (2021-08-16 23:23 UTC)

<p>You can place many fiducials all over the segmentation, clone the fiducial list (by right-clicking on it in Data module), choose one fiducial list as To, the other as From, and lock the From list (so that you don’t accidentally move points in it). Then you can move points in the To list to prescribe displacements.</p>

---

## Post #3 by @parvaneh.a (2021-08-17 00:23 UTC)

<p>Thanks for your reply . Unfortunately, I did not understand the explanation very well so, I highly appreciate it if you could clarify more. what I exactly want to do is register F1 and F2 in image 1 (moving image) to f1 and f2 in image 2 (template image) while all the body and the other branches are fixed in image 1 and only the branch between f1 and f2 can change in registration to be registered to the same branch in image 2. so, I think ‘from’ points should be f1 and f2 in image 1 and ‘To’ points should be f1 and f2 in image 2. Right?<br>
In this situation, I have added many points around the place where I want to be fixed on image 1 (fig3) and  cloned it as you said but I don’t know how and where I should use it since ‘To’ and ‘from’ are already filled as I explained before. I appreciate any help in that problem.</p>
<p>fig1:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97adb7dbc8c761bbf5500a6a0d5d27c8d78c5b32.png" alt="Screenshot from 2021-08-16 18-49-25" data-base62-sha1="lDOhPnpmhJjNLWG9CpoesHBjItA" width="631" height="490"></p>
<p>fig2:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c910fa51e55eaa2b5f48254a68dcffc83fd284f.png" alt="Screenshot from 2021-08-16 20-22-24" data-base62-sha1="fuqmfgxuXL91CXPzgI31qexoQJ9" width="588" height="345"></p>
<p>Fig. 3.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531c87b95a4747b3a4c09a491492748e9ead7ef9.png" data-download-href="/uploads/short-url/bReKQKFD9vgBp2ybGhoi1xFHYb7.png?dl=1" title="Screenshot from 2021-08-16 20-18-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531c87b95a4747b3a4c09a491492748e9ead7ef9_2_592x500.png" alt="Screenshot from 2021-08-16 20-18-30" data-base62-sha1="bReKQKFD9vgBp2ybGhoi1xFHYb7" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531c87b95a4747b3a4c09a491492748e9ead7ef9_2_592x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531c87b95a4747b3a4c09a491492748e9ead7ef9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531c87b95a4747b3a4c09a491492748e9ead7ef9.png 2x" data-dominant-color="A1829F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-08-16 20-18-30</span><span class="informations">664×560 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>also , is there anyway easier than putting each point in fig3 one by one?</p>

---

## Post #4 by @lassoan (2021-08-17 03:44 UTC)

<p>If there are large parts of the volume that should not be changed at all then put those into a separate segment. For example, you can put the left atrium in a separate segment (will not be modified) from the pulmonary vein segment (that will be warped). You can only apply a transform to an entire segmentation, so you will need to temporarily move the segment to another segmentation, warp it (by applying and hardening a transform), then move it back to the original segmentation.</p>
<p>It is enough to anchor the end of the vein that is closer to the left atrium by placing a 2-3 points, and warp the other end of the vein by a few points.</p>
<p>There are many other ways to do this. For example extracting centerline using VMTK then edit it as a curve.</p>
<p>What would you like to achieve overall? What is the clinical problem that you are trying to solve?</p>

---
