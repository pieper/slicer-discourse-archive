---
topic_id: 17654
title: "Combine Two Ct Volumes And Generate A New Dicom Set"
date: 2021-05-17
url: https://discourse.slicer.org/t/17654
---

# Combine two CT volumes and generate a new dicom set

**Topic ID**: 17654
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/combine-two-ct-volumes-and-generate-a-new-dicom-set/17654

---

## Post #1 by @wjd582 (2021-05-17 16:09 UTC)

<p>Operating system: window 7<br>
Slicer version:4.11.0-2020-08-19</p>
<p>Hello.<br>
Now I am trying to combine two dicom set to a singe dicom set.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ed0e6fd978e0f25763feb7aaf8e0e44d86937fc.jpeg" data-download-href="/uploads/short-url/dwMs6GbI5zQMB3FDZcjYzXKiete.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ed0e6fd978e0f25763feb7aaf8e0e44d86937fc_2_690x373.jpeg" alt="image" data-base62-sha1="dwMs6GbI5zQMB3FDZcjYzXKiete" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ed0e6fd978e0f25763feb7aaf8e0e44d86937fc_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ed0e6fd978e0f25763feb7aaf8e0e44d86937fc_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ed0e6fd978e0f25763feb7aaf8e0e44d86937fc_2_1380x746.jpeg 2x" data-dominant-color="6A6C74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1038 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you can I above image, I have two volumes that are Lower and Upper body.<br>
What I want to do is to merging these two volumes and generate Full body CT set.</p>
<p>I tried to use the registration function but it was just registration.</p>
<p>Is there any function or method regarding this?</p>
<p>Thank you for your help in advance.</p>

---

## Post #2 by @pieper (2021-05-17 17:26 UTC)

<p>There are some instructions here: <a href="https://discourse.slicer.org/t/combine-two-volumes-from-two-scans-into-a-complete-volume/10704" class="inline-onebox">Combine Two Volumes From Two Scans Into A Complete Volume</a>.</p>
<p>Once you have merged them you can export the result as DICOM.</p>

---

## Post #3 by @wjd582 (2021-05-17 18:05 UTC)

<p>Thank you for your comment.</p>
<p>But, how can I align two volumes? I can only see the one volume when I use a trasform. Do I need to preprocess before alignment?</p>
<p>Thanks,</p>

---

## Post #4 by @pieper (2021-05-17 20:47 UTC)

<p>You can put <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">one volume in the foreground and one in the background and enable cross-fade between them</a> to see both.  Then you can use the Transform controls to match them up manually.  If that’s not good enough and there is overlap between the two volumes you can use Crop Volumes to make two volumes that each just contain the overlap and then get them close manually can <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">calculate a better registration</a> using the automated methods.</p>

---

## Post #5 by @Young_Wang (2022-01-27 21:18 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I’m working on a similar project where I have two portions of CT data of the human middle ear. I wonder if there is a better visualization method to merge the co-registered images.<br>
The top is merged and the bottom is the original one<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef4be02ab7dea2caf81437277f90284860d1514a.jpeg" data-download-href="/uploads/short-url/y8UG3h7zA6I7113xiimBYqfMCNA.jpeg?dl=1" title="Screen Shot 2022-01-27 at 5.12.52 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4be02ab7dea2caf81437277f90284860d1514a_2_690x409.jpeg" alt="Screen Shot 2022-01-27 at 5.12.52 PM" data-base62-sha1="y8UG3h7zA6I7113xiimBYqfMCNA" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4be02ab7dea2caf81437277f90284860d1514a_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4be02ab7dea2caf81437277f90284860d1514a_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4be02ab7dea2caf81437277f90284860d1514a_2_1380x818.jpeg 2x" data-dominant-color="A2A3A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-27 at 5.12.52 PM</span><span class="informations">3584×2126 787 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @mikebind (2022-01-27 21:26 UTC)

<p>I found this discussion very helpful: <a href="https://discourse.slicer.org/t/checkerboard-for-registered-mri-and-ct-of-hip-bone/18768/5" class="inline-onebox">Checkerboard for registered MRI and CT of hip bone - #5 by lassoan</a>  (not suggesting checkerboard, but the description for either segmentation outline alignment or edge filtering and overlaying). Perhaps it will be helpful for you as well.</p>

---

## Post #7 by @jtwlam717 (2023-06-30 11:40 UTC)

<p>Hi,</p>
<p>I am very new with using Slicer. I am trying to merge 2 CT volumes (one of the skull and the other of the neck).  I am able to load the two volumes, but I don’t know how to put one in the foreground and one in the background and have them stack without overlapping. Can someone please share an easy to understand tutorial! Thank you so much.</p>

---

## Post #8 by @mikebind (2023-07-18 18:50 UTC)

<p>You can set the foreground and background volumes using the selectors in the slice view, see the documentation here:  <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="inline-onebox" rel="noopener nofollow ugc">User Interface — 3D Slicer documentation</a></p>
<p>If you want to merge them into one combined image volume, you may find the Stitch Volumes module helpful.  You would first need to install the SlicerSandbox extension, restart Slicer, and then open the Stitch Volumes module.  It is not very polished, but you can find some documentation about how to use it here: <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" class="inline-onebox" rel="noopener nofollow ugc">GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished implementations but can be useful to users</a>.</p>

---
