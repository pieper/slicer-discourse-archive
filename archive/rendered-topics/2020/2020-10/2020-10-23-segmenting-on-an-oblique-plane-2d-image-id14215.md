---
topic_id: 14215
title: "Segmenting On An Oblique Plane 2D Image"
date: 2020-10-23
url: https://discourse.slicer.org/t/14215
---

# Segmenting on an oblique plane 2D image

**Topic ID**: 14215
**Date**: 2020-10-23
**URL**: https://discourse.slicer.org/t/segmenting-on-an-oblique-plane-2d-image/14215

---

## Post #1 by @mk.kassai (2020-10-23 15:59 UTC)

<p>I would like to do segmentation of a single slice of MRI, that has been acquired in an oblique angle.<br>
If I load it into 3D slicer, I only get some lines in different directions, since it shows the X Y and Z plane cross sections. I can manually copy the rotation information from the MRI metadata, but it’s a huge effort, since I will eventually have to work with around 1000 images.<br>
Is there any way, I can automatically get the plane to be displayed as in a dicom viewer, like Osirix?</p>

---

## Post #2 by @cpinter (2020-10-23 16:01 UTC)

<p>I believe this button will do the trick<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/1422919ab4495e0e6992188cfe0c987ac01b2f03.png" alt="image" data-base62-sha1="2S7BZ1JRCFT5lmGYbX2hlu5woq7" width="493" height="194"></p>

---

## Post #3 by @Hapietsch (2021-01-30 17:40 UTC)

<p>Hi Mr. Pinter.<br>
I’m having a similar issue, I think, based on the description. But the button suggested causes my screen just to revert back to the original slice, not the oblique slice I need.</p>
<p>I have a CT scan, and need to measure the area of the end plate on a vertebral body. The spine is not always in line with the orientation of the slice, so I used an oblique slice to view the end plate and take a measurement like so:</p>
<ol>
<li>Reformat module - select red slice, then adjust A-P and L-R until the red slice is aligned as best I can</li>
<li>Markups module - draw a closed loop around the area of interest. Then use the code from Mr. Lasso in another question to calculate the area within the loop. <a href="https://discourse.slicer.org/t/how-can-i-calculate-an-area-on-a-ct-image-i-can-calculate-volumes-mm-3-but-not-areas-mm-2/1549/4" class="inline-onebox">How can I calculate an area on a CT image. I can calculate volumes (mm^3) but not areas (mm^2) - #4 by lassoan</a>
</li>
</ol>
<p>I would prefer to make a more consistent calculation based on threshold of the bone, vs my eye drawing a loop. I repeated the process a few times, and I get slightly different values. I have about 90 of these measurements to take, so I don’t want to introduce variation from my own ability to draw on the screen. And it’s quite a lot of measures to do multiple times and take an average.<br>
I was hoping to use the segment function for a single oblique slice. I have tried to take a segment on the oblique plane, but 3D slicer always shows the segment across all of the original slices when I try this. I get a short volume, rather than the 2D segment on the oblique plane.</p>
<p>I was hoping your solution to this question would work for me, but when I click the button you highlighted, it just reverts the view back to an axial slice, rather than the oblique one. For me, it acts as a “undo reformat” button.</p>
<p>Is there another way?</p>
<p>Below is an image of the oblique plane. I’m using a sample data set from Slicer rather than my actual data but it is the same part of the body.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df93036dd639001c4ab9c4cb44036e796905279.jpeg" data-download-href="/uploads/short-url/dpkhSepOILDnnZXQVP1ZXw7ARxn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5df93036dd639001c4ab9c4cb44036e796905279_2_690x376.jpeg" alt="image" data-base62-sha1="dpkhSepOILDnnZXQVP1ZXw7ARxn" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5df93036dd639001c4ab9c4cb44036e796905279_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5df93036dd639001c4ab9c4cb44036e796905279_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5df93036dd639001c4ab9c4cb44036e796905279_2_1380x752.jpeg 2x" data-dominant-color="7D7D82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3838×2096 657 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-01-30 19:14 UTC)

<aside class="quote no-group" data-username="Hapietsch" data-post="3" data-topic="14215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> Hapietsch:</div>
<blockquote>
<p>I click the button you highlighted, it just reverts the view back to an axial slice, rather than the oblique one. For me, it acts as a “undo reformat” button.</p>
</blockquote>
</aside>
<p>There are multiple approaches that you can use, see detailed description of basic techniques on oblique image segmentation: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>
<p>If you need to quantify many end plates on a single image then I would recommend to define a spine curve by placing 10-20 markups open curve control points on axial slices, then use this curve to reformat (straighten) the entire volume at once using Curved Planar Reformat module (in Sandbox extension):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WJQexDTiRRc" data-video-title="Transform markups between original and straightened vessel" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WJQexDTiRRc/maxresdefault.jpg" title="Transform markups between original and straightened vessel" width="" height="">
  </a>
</div>

<p>Each axial slice of the reformatted volume is cut out from the original image with a plane, so there is no distortion of any kind, you can make measurements with full accuracy.</p>
<p>You can choose to segment the straightened volume or measure cross section area directly using markups.</p>
<aside class="quote no-group" data-username="Hapietsch" data-post="3" data-topic="14215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> Hapietsch:</div>
<blockquote>
<p>I have a CT scan, and need to measure the area of the end plate on a vertebral body.</p>
</blockquote>
</aside>
<p>Probably measuring cross-sectional area using closed markups curve is as accurate as it gets. You could of course do the measurement based on segmentation, but that relies on visual assessment, too (what threshold do you choose, how do you deal with intensity variations, etc.).</p>
<p>If one person performs all the measurements then it is not hard to achieve consistent measurements, so the real challenge is inter-operator variability. You can do little experiment with 4-5 operators to see if you get reduced variability with segmentation based methods.</p>

---

## Post #5 by @lassoan (2021-01-31 13:52 UTC)

<aside class="quote no-group" data-username="Hapietsch" data-post="3" data-topic="14215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/977dab/48.png" class="avatar"> Hapietsch:</div>
<blockquote>
<p>draw a closed loop around the area of interest. Then use the code from Mr. Lasso in another question to calculate the area within the loop</p>
</blockquote>
</aside>
<p>FYI, in latest Slicer Preview Release area of markups closed contour can be computed without scripting, just by enabling “area” in Markups module “Measurements” section.</p>

---

## Post #6 by @Hapietsch (2021-01-31 18:03 UTC)

<p>Mr. Lasso,<br>
Thank you, I will try your suggested methods to find what will work best for my issue.</p>
<p>Prior to your replies, I may have also stumbled upon a method using Transform to rotate the image to the standard slice, rather than rotating the slice angle. This seems to allow segmentation that does not take a volume, but the single slice.</p>
<p>Glad there seem to be a few options.</p>
<p>Thank you!</p>

---
