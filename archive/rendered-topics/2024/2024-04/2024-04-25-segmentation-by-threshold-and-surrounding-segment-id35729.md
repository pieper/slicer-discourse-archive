# Segmentation by threshold and surrounding segment

**Topic ID**: 35729
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/segmentation-by-threshold-and-surrounding-segment/35729

---

## Post #1 by @FraP (2024-04-25 10:20 UTC)

<p>I would like to close the lumen of vessels of which I am able to select (partially or completely) the wall, having a solid cylinder and not hollow tube. However, the colour of the lumen is similar to that surrounding the vessels and therefore only threshold cannot be used.<br>
I have already tried the close method of smoothing and with wrap solidify, but they merge the elements into a single large block, merging neighboring vessels. This is also probably because I’m working with microscopic images.</p>
<p>Is it possible in 3D Slicer to generate a segment based on its colour (threshold) and whether or not it is surrounded for a certain percentage by another segment/colour?<br>
I could use this segment to change the volume with Mask Volume and reperform the segmentation of the solid cylinders.</p>

---

## Post #2 by @muratmaga (2024-04-25 19:25 UTC)

<aside class="quote no-group" data-username="FraP" data-post="1" data-topic="35729">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e68b1a/48.png" class="avatar"> FraP:</div>
<blockquote>
<p>a segment based on its colour (threshold) and whether or not it is</p>
</blockquote>
</aside>
<p>Thats exactly what the threshold effect does. However, intensities are usually continuous with neighboring structures, making it difficult to solely dependent on a single value to separate the regions.</p>
<p>After the threshold, and before closing. Just run a median filter with small kernel (maybe 3x3x3) voxels, that should remove most of the noise, and then you can try the closing filter to fill inside.</p>

---

## Post #3 by @FraP (2024-04-29 07:44 UTC)

<p>Thank you for your answerer <a class="mention" href="/u/muratmaga">@muratmaga</a><br>
I have already used the threshold tool and it worked very well. What I am asking in this post is whether there is a possibility to segment not only based on colour but also on surrounding segments/colours.<br>
I cannot share the original files I am working on but I have tried to schematise the situation in this image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e94f63d12556ea401b9924a71a0b8d8ee50ab296.png" data-download-href="/uploads/short-url/xhXlfnYMDqqx3C3Upi9f2upS6yy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94f63d12556ea401b9924a71a0b8d8ee50ab296_2_344x375.png" alt="image" data-base62-sha1="xhXlfnYMDqqx3C3Upi9f2upS6yy" width="344" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94f63d12556ea401b9924a71a0b8d8ee50ab296_2_344x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94f63d12556ea401b9924a71a0b8d8ee50ab296_2_516x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e94f63d12556ea401b9924a71a0b8d8ee50ab296_2_688x750.png 2x" data-dominant-color="838383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×865 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can easily segment the differently coloured parts with the threshold tool. However, I would like to segment the white parts contained in the black circles/semicircles into a different segment than those outside these rings.<br>
Is this possible in your opinion?</p>

---

## Post #4 by @muratmaga (2024-04-29 15:35 UTC)

<p>If the inner white areas are not touching each other (in 3D context, not 2D), after thresholding, you can use the Island tool to convert them into separate segments.</p>

---

## Post #5 by @FraP (2024-04-29 16:01 UTC)

<p>Unfortunately, the segmentation is not so precise as to prevent the inner white parts from touching the outer ones.</p>

---

## Post #6 by @muratmaga (2024-04-29 16:06 UTC)

<p>You can also try grow from the seeds.</p>
<p>assign three different seeds (per each group you want to segmetnt), inside white, black area, and outside white and with a combination of masking options, you might be able to get further with this approach.</p>

---

## Post #7 by @mikebind (2024-04-29 20:01 UTC)

<p>How about segmenting the vessel walls via threshold, run close holes with a kernel large enough to fill lumens but not bridge between different vessels.  Then threshold to the higher value, but use masking settings to limit changes to inside existing segments.  If vessels are almost always spaced further than one vessel diameter apart, then this should work pretty well, if not, then it will fail where vessels are too close together.</p>

---
