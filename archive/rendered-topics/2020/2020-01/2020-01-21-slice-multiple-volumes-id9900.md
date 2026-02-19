---
topic_id: 9900
title: "Slice Multiple Volumes"
date: 2020-01-21
url: https://discourse.slicer.org/t/9900
---

# Slice multiple volumes

**Topic ID**: 9900
**Date**: 2020-01-21
**URL**: https://discourse.slicer.org/t/slice-multiple-volumes/9900

---

## Post #1 by @fbordignon (2020-01-21 20:48 UTC)

<p>Hi, is there a way to display multiple volumes on a slice window?<br>
For example, I have 2 volumes that has no overlap, can I slice both of them via the yellow slice window?<br>
Or any other special slice window?</p>

---

## Post #2 by @Juicy (2020-01-22 06:54 UTC)

<p>You can visualise two volumes in one window by putting one in the foreground and one in the background.</p>
<p>Click the pin icon in the yellow slice window then click the arrow button to expand the menu. There is a drop down menu for the background and foreground of the slice window. You can select a volume in each of these drop down menus. Drag the slider up and down to fade between the two volumes.</p>
<p>Is that what you meant?</p>

---

## Post #3 by @lassoan (2020-01-22 13:18 UTC)

<p>Background volume extents are used as mask, so if the volumes don’t overlap then you don’t see the foreground volume. This is often useful but I see that it can be inconvenient. We may revisit this decision later but until then you can expand the background volume using Crop Volume module.</p>

---

## Post #4 by @fbordignon (2020-01-22 16:00 UTC)

<p>I meant to slice various volumes at the same slice window. I don’t want to compare them, I just want to see the slice from all the volumes that my slice window intercept Ex. I have 3 volumes in 3D and want to slice all of them at the same time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/014cc84d018f2a8038edc69751ca9fb658e5424c.png" data-download-href="/uploads/short-url/buYWS5Tbng6G1ky1Rd3tc3lBko.png?dl=1" title="3D to 2D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cc84d018f2a8038edc69751ca9fb658e5424c_2_616x500.png" alt="3D to 2D" data-base62-sha1="buYWS5Tbng6G1ky1Rd3tc3lBko" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cc84d018f2a8038edc69751ca9fb658e5424c_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/014cc84d018f2a8038edc69751ca9fb658e5424c_2_924x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/014cc84d018f2a8038edc69751ca9fb658e5424c.png 2x" data-dominant-color="F0E8E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D to 2D</span><span class="informations">1002×812 23.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-01-22 16:26 UTC)

<p>In one slice view, you can display 2 scalar volumes, 1 labelmap volume, and any number of segmentations, model intersections, markups, etc.</p>
<p>If you want to display more than 2 volumes then you can either show one volume in each slice view (there are layouts with many slice views) and display each of the in a single 3D view.</p>
<p>There are many other options, depending on what exactly you would like to achieve.</p>

---

## Post #6 by @fbordignon (2020-01-22 16:37 UTC)

<p>I see. What I wanted was for the slice window to slice through my entire scene, showing all the volumes that the plane defining the slice window intercepts.</p>

---

## Post #7 by @lassoan (2020-01-22 16:39 UTC)

<p>Can you write a bit about your use case? What volumes you display and why? What is the clinical application?</p>

---

## Post #8 by @fbordignon (2020-01-22 17:12 UTC)

<p>We are using slicer for rock sample CT scans interpretation.<br>
We have well cores of 90cm in length (depth) with 13.3cm in diameter.<br>
We need to interpret depth intervals ranging from 20 to 100 meters, looking at 20 to 100 volumes for each interpretation. These cores are continuous in place, but the trip from the subsurface to the CT scanner is though, they most likely lost their azimuth alignment relative to each other. We need to keep them separate inside slicer.</p>
<p>So it would be great to have multiple volumes displayed at the slice window at the same time, where I would only pan the window to view another volume, or work at the boundary of two volumes. Trying to align them rotating around the IS axis.</p>

---

## Post #9 by @lassoan (2020-01-23 00:39 UTC)

<p>Thank you, this clarifies things a bit. Would you like to stitch the cores into one long continuous volume?</p>
<p>If you need to align the cores then probably the simplest would be to write a short script that finds the centerline position and orientation of each core and they are transformed to a normalized position (e.g., center in (0,0,0) position, centerline axis in (0,0,1) direction). From there, it would be trivial to further align them manually (with sliders in Transforms module) and a fully automatic alignment should not be difficult either (average a few ten slices at the matching ends of two cores and automatically register them using intensity-based registration - since rotation is just a single value, you don’t need any sophisticated optimization scheme to find the optimum).</p>

---

## Post #10 by @fbordignon (2020-01-24 14:47 UTC)

<p>Thanks for your suggestions, Andras.<br>
The alignment algorithm is not the problem. We’ve managed to do that. Stitching the cores together is not ideal, because the interpreter would like to rotate them manually according to some interpretation in his mind, after the automatic alignment and IS rotation, he/she could segment them individually, split cores if a fracture occurs (to IS rotate two segments separately). Ex. this is a slice of a core that broke apart and have two pieces that needs to be rotated separately:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb806286fd93d88959ab89dae6def710bbbae6a6.png" alt="image" data-base62-sha1="qKIlIwVZ69G4mtFTam2XgHM4qWO" width="60" height="333"><br>
Note the angle of the structures in the top portion is different from the bottom, they should be the same.  And many other examples where the user would like to interpret and compare the multiple cores, manipulating them individually.</p>
<p>Showing them in 3D is an option, but it would require the manipulation of the ROI for each of the volumes to slice them in 3D. In my opinion, a 2D slice window that can show multiple independent volumes would be a great tool for this kind of interpretation. Do you have any idea of how to do that, how to start implementing such window? We could try to do that over here. Do you think it is a bad idea?</p>
<p>Ps. low res image intentional for it is a not so public dataset.</p>

---

## Post #11 by @lassoan (2020-01-24 15:29 UTC)

<p>Easy-to-implement options (that do not require any Slicer core change):</p>
<ul>
<li>dynamically compute the merged image slice from your volumes</li>
<li>visualize in 3D viewer (you can disable certain interactions, such as rotation to make it more behave like a slice view) and create a scripted module that sets up slice views automatically in the background</li>
</ul>
<p>Alternatively, you can change slice view to make it able to display any number of scalar volumes. You would not need to expose this on the default Slicer GUI, but it would probably still be considerable implementation effort. We haven’t implemented this because usually you cannot see much when you overlap more than 2 volumes, but your case is special because the volumes actually don’t overlap they are just close to each other.</p>

---
