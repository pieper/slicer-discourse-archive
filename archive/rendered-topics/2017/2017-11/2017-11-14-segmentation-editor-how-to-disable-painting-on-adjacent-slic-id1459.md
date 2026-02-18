# Segmentation Editor - How to disable painting on adjacent slices?

**Topic ID**: 1459
**Date**: 2017-11-14
**URL**: https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459

---

## Post #1 by @matt-berseth (2017-11-14 22:00 UTC)

<p>I am working on a project where we are segmenting lesions from an MRI using the paint tool from the Segment Editor module. We are using a large brush size along with a threshold so only pixels within a certain range are included in the segmentation.</p>
<p>My problem is that I want the segmentation to be only in 2d (i.e. just affecting the pixels on the current slice of the volume). For example, if I do a threshold paint on slice 10 of the MRI, I don’t want it to paint any of the pixels on slice 9 or 11.</p>
<p>I figured there would be a way to disable this, but I can’t seem to find the option.</p>
<p>I am using the following version of slicer: 4.9.0-2017-11-10 r26630</p>

---

## Post #2 by @lassoan (2017-11-14 23:08 UTC)

<p>By default, paint effect only paints on the current slice. Have you enabled “sphere” brush option?</p>

---

## Post #3 by @matt-berseth (2017-11-14 23:27 UTC)

<p>Thanks for the reply. I was thinking that option might be related.</p>
<p>I tried enabling and disabling that brush option, but the adjacent slices are still painted. I tried using both the stable and nightly builds. I am not sure if it would matter or not, but I am running linux - I did not try on windows.</p>
<p>Either way, thanks for the tip. I will close out of the application and start fresh and retest to make sure it was not user error.</p>
<p>Lead Data Scientist<br>
NLP Logix, LLC<br>
4215 Southpoint Boulevard|Suite 160<br>
Jacksonville, FL 32216<br>
<a href="http://www.nlplogix.com" rel="nofollow noopener">www.nlplogix.com</a><a href="http://www.nlplogix.com" rel="nofollow noopener">http://www.nlplogix.com</a><br>
<a href="https://www.nvidia.com/en-us/gtc-dc/" rel="nofollow noopener">https://www.nvidia.com/en-us/gtc-dc/</a></p>

---

## Post #4 by @pieper (2017-11-14 23:31 UTC)

<p>If the acquisition was tilted you may need to rotate to volume plane (click the “pushpin” icon in the top-left corner of the slice view, then click the double-arrow button on the left, then the “Rotate to volume plane” icon appears):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/575732a3e977d253c956c444120242955ce37a37.jpeg" alt="image" data-base62-sha1="csEmljnHREr3yUBcsTeEFOhsTOf" width="179" height="107"></p>
<p>Here’s an example drawing on the original slice (patient space)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee6244f649d4f68c2cd1a14c4e489972a0a5755e.jpeg" data-download-href="/uploads/short-url/y0Qb6Ef1694zMHYIT45Xx6cE0bQ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ee6244f649d4f68c2cd1a14c4e489972a0a5755e_2_550x500.jpg" alt="image" data-base62-sha1="y0Qb6Ef1694zMHYIT45Xx6cE0bQ" width="550" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ee6244f649d4f68c2cd1a14c4e489972a0a5755e_2_550x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/ee6244f649d4f68c2cd1a14c4e489972a0a5755e_2_825x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee6244f649d4f68c2cd1a14c4e489972a0a5755e.jpeg 2x" data-dominant-color="4C4A57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">880×799 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And here the paint stroke on the right is after rotating the red slice into the acquisition plane and only one plane is painted in the other views.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e575499b56b012ea2cc088c24f38cb43202281.jpeg" data-download-href="/uploads/short-url/5GWesknjInRIylPfDboX3rTkF8Z.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/27e575499b56b012ea2cc088c24f38cb43202281_2_547x499.jpg" alt="image" data-base62-sha1="5GWesknjInRIylPfDboX3rTkF8Z" width="547" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/27e575499b56b012ea2cc088c24f38cb43202281_2_547x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/27e575499b56b012ea2cc088c24f38cb43202281_2_820x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e575499b56b012ea2cc088c24f38cb43202281.jpeg 2x" data-dominant-color="555360"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">882×805 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @matt-berseth (2017-11-16 14:30 UTC)

<p>That was it. Thanks for the answer (with pictures). I would not have figured this out otherwise.</p>

---

## Post #6 by @lassoan (2018-12-09 23:57 UTC)

<p>Recent versions of Slicer now show a warning button (with an exclamation mark) if any of the slice viewers are not aligned with the current segmentation axes. Click that button to snap each slice view to nearest segmentation axis.</p>

---

## Post #7 by @Zuzana_Holubova (2023-11-27 15:46 UTC)

<p>Hi. I have the same exact problem with paint/eraser segmentation tool. I tried everything I found out here on the forum but the problem remains. Even if I have brush size of 1 mm, it paints on two adjacent slices. I used the sphere brush for rough segmentation then worked with some logical operators. After that (my impression) the problem occured- when I wanted to edit the segment more precisely with paint brush (or eraser). I also tried to reload the segmentations and put the slicer view to default.<br>
Thanks for any thoughts.</p>

---

## Post #8 by @cpinter (2023-11-28 13:52 UTC)

<p>Can you please create a new post with detailed steps and screenshots? Also can you please try to reproduce the problem with an image available in the Sample Data module?</p>

---
