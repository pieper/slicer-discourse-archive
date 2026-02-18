# 3D coordinate of input 3D matrix

**Topic ID**: 34937
**Date**: 2024-03-17
**URL**: https://discourse.slicer.org/t/3d-coordinate-of-input-3d-matrix/34937

---

## Post #1 by @Cathy123 (2024-03-17 20:47 UTC)

<p>Hi, I have some problems of 3D coordinates and segmentation.</p>
<ol>
<li>what’s the coordinate relationship between 3D slicer and my volume coordinate? When I load my 3D matrix( 512<em>512</em>512 object) in the software, how can i set the coordinate with my volume coordinate?</li>
<li>for the 3D volume(512<em>512</em>512), it is a binary volume. The values on the object that can be seen are 1, and i want to ask how to do segment? can it be segment automatically or semi-automatically? after segmentation, how can i set the coordinate at the center of intersection betweent to the two segment parts?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d174c4dffce9809abb5db4f017f9ebfd90adf372.jpeg" data-download-href="/uploads/short-url/tSVY0onl1If474xKBdDOsyw0P3I.jpeg?dl=1" title="volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d174c4dffce9809abb5db4f017f9ebfd90adf372_2_533x500.jpeg" alt="volume" data-base62-sha1="tSVY0onl1If474xKBdDOsyw0P3I" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d174c4dffce9809abb5db4f017f9ebfd90adf372_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d174c4dffce9809abb5db4f017f9ebfd90adf372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d174c4dffce9809abb5db4f017f9ebfd90adf372.jpeg 2x" data-dominant-color="AEA3C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume</span><span class="informations">559×524 42.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---

## Post #2 by @muratmaga (2024-03-17 21:17 UTC)

<p>Please read<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>

---

## Post #3 by @Cathy123 (2024-03-18 14:13 UTC)

<aside class="quote no-group" data-username="Cathy123" data-post="1" data-topic="34937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e8c25b/48.png" class="avatar"> Cathy123:</div>
<blockquote>
<p>for the 3D volume(512<em>512</em>512), it is a binary volume. The values on the object that can be seen are 1, and i want to ask how to do segment? can it be segment automatically or semi-automatically?</p>
</blockquote>
</aside>
<p>Thank you so much. What about the second question?" for the 3D volume(512<em>512</em> 512), it is a binary volume. The values on the object that can be seen are 1, and i want to ask how to do segment? can it be segment automatically or semi-automatically?"</p>

---

## Post #4 by @muratmaga (2024-03-18 15:35 UTC)

<p>In short, you can segment a binary image if you like with the segment editor.</p>
<p>Segmentation is to define specific regions in intensity images with continuous grayscale as binary images. I am not sure what you want to do by segmenting it (because the screenshot above already shows something segmented).</p>
<p>You will find most tools not working very well for an image that consists only 0 and 1.  But if your goal is to use something like scissors, or some morphological operations, you can do those.</p>

---

## Post #5 by @Cathy123 (2024-03-18 18:56 UTC)

<p>Thank you so much. It is a segmented image shown above. I want to go on conducting with aneurysm segmentation, so I need to segmented based on it.</p>

---

## Post #6 by @muratmaga (2024-03-18 19:09 UTC)

<p>If you want to split that whole thing into two segments as shown in schematic, you can easily achieve that using the scissors tool.</p>

---
