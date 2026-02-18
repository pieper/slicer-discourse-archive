# Isolated muscle segmentation from MRI

**Topic ID**: 14628
**Date**: 2020-11-16
**URL**: https://discourse.slicer.org/t/isolated-muscle-segmentation-from-mri/14628

---

## Post #1 by @Sz368 (2020-11-16 05:26 UTC)

<p>Hello everybody<br>
I am creating a 3D foot from a MRI for medical education.<br>
I see Materialise/Mimic say they have a ‘gradient’ application where you can trace muscle to the boundary of the most contrast tissue difference<br>
Do we have any functionality like that?<br>
I am thinking the best method will be fill between slices to segment individual foot muscles? What are your thoughts or does anyone have experience?<br>
What is difficult is there is not much contrast difference between foot muscles.<br>
Thanks a lot<br>
Susan</p>

---

## Post #2 by @pieper (2020-11-16 13:29 UTC)

<p>Are you planning to use MRI or CT?  If you have an example dataset people could try some experiments and make suggestions.</p>

---

## Post #3 by @Sz368 (2020-11-17 11:11 UTC)

<p>Hi Steve,<br>
I can’t send the images out of our hospital firewall unfortunately<br>
Thank you though<br>
Susan</p>

---

## Post #4 by @pieper (2020-11-17 13:04 UTC)

<p>That’s understandable you can’t share the data, but can you describe in in more detail? (CT? MR? resolution?)</p>

---

## Post #5 by @Sz368 (2020-11-18 13:50 UTC)

<p>thanks Steve,<br>
it’s MRI 1.5T PD or T2 images of a foot.<br>
Small structures like ligaments are difficult to segment without manual segmentation, techniques that interpolate from 2D to 3D are handy.</p>
<p>Muscle muscle interfaces for instance Abductor Hallucis next to flexor hallucis brevis are also tricky to delineate</p>
<p>reading around techniques semi-auto techniques to edges seem handy, I’m assuming that’s similar to grow from seeds techniques which are awesome for lots of things</p>
<p>that’s my experience so far</p>

---

## Post #6 by @lassoan (2020-11-18 22:07 UTC)

<aside class="quote no-group" data-username="Sz368" data-post="1" data-topic="14628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/439d5e/48.png" class="avatar"> Sz368:</div>
<blockquote>
<p>I see Materialise/Mimic say they have a ‘gradient’ application where you can trace muscle to the boundary of the most contrast tissue difference</p>
</blockquote>
</aside>
<p>Most semi-automatic segmentation methods are gradient based (segment boundaries are placed where gradient is high), such as Grow from seeds, Watershed, Fast marching, Local thresholding.</p>
<aside class="quote no-group" data-username="Sz368" data-post="1" data-topic="14628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/439d5e/48.png" class="avatar"> Sz368:</div>
<blockquote>
<p>I am thinking the best method will be fill between slices to segment individual foot muscles?</p>
</blockquote>
</aside>
<p>Fill between slices is very efficient for segmenting long structures, such as muscles. It is particularly useful when there is no visible contrast between structures, because this effect does not rely on image content, only on the segmentations that you provide.</p>
<aside class="quote no-group" data-username="Sz368" data-post="5" data-topic="14628">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/439d5e/48.png" class="avatar"> Sz368:</div>
<blockquote>
<p>Small structures like ligaments are difficult to segment without manual segmentation</p>
</blockquote>
</aside>
<p>If you want to segment structures that have cross-section of less than 5-10 voxels then you may consider using Crop volume module to resample to have smaller, isotropic voxels (also crop it to the minimum necessary size to keep the image as small as possible).</p>

---

## Post #7 by @Sz368 (2020-11-20 15:05 UTC)

<p>thank you so much for explaining the differences to me Andras and the best way to approach each of these problems. Appreciate your time replying</p>

---
