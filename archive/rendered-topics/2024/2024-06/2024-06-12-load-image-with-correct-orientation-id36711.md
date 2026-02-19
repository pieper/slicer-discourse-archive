---
topic_id: 36711
title: "Load Image With Correct Orientation"
date: 2024-06-12
url: https://discourse.slicer.org/t/36711
---

# Load image with correct orientation

**Topic ID**: 36711
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/load-image-with-correct-orientation/36711

---

## Post #1 by @haphantran (2024-06-12 02:44 UTC)

<p>Hi team,<br>
Thank you for the help in advance.<br>
I’m trying to load 2 images into 3D Slicer. If I load it manually (Import data), 3D Slicer display them in the correct orientation as below.<br>
Image 0 (Green view)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9368d3e5db3e5af324489ccf4daad8131d9311c.jpeg" data-download-href="/uploads/short-url/uZyuetl1rB0cM8GmdFuU0zX1I8Q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9368d3e5db3e5af324489ccf4daad8131d9311c_2_690x332.jpeg" alt="image" data-base62-sha1="uZyuetl1rB0cM8GmdFuU0zX1I8Q" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9368d3e5db3e5af324489ccf4daad8131d9311c_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9368d3e5db3e5af324489ccf4daad8131d9311c_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9368d3e5db3e5af324489ccf4daad8131d9311c_2_1380x664.jpeg 2x" data-dominant-color="3D3C40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1603×772 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Image 1 (Yellow View)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df8de61137c4b38f94997d8b47f9984bab5696af.jpeg" data-download-href="/uploads/short-url/vTEux4akK0OMWo7Pq0u5BmPpNv1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df8de61137c4b38f94997d8b47f9984bab5696af_2_690x322.jpeg" alt="image" data-base62-sha1="vTEux4akK0OMWo7Pq0u5BmPpNv1" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df8de61137c4b38f94997d8b47f9984bab5696af_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df8de61137c4b38f94997d8b47f9984bab5696af_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df8de61137c4b38f94997d8b47f9984bab5696af_2_1380x644.jpeg 2x" data-dominant-color="36363A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1605×750 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But I tried to write code and can’t distinguish between these 2 images. As can be seen from the screenshots, the JIK to RAS direction Matrix are the same, Scan Order are the same too.<br>
Which field should I use to display the image in the correct orientation?</p>

---

## Post #2 by @haphantran (2024-06-24 14:07 UTC)

<p>Hi guys,<br>
Do anyone have any info on this?<br>
Thank you,<br>
Ha Phan.</p>

---

## Post #3 by @haphantran (2024-08-01 02:17 UTC)

<p>Bump this up. Please let me know if you have some information regarding this.</p>

---

## Post #4 by @pieper (2024-08-01 12:45 UTC)

<p>Based on the the volume information you can see that these are single slices in different axes of the volume - the first has a single ‘J’ slice, while the second has a single ‘I’ slice even though both are “axial IS”.  So if you  need to distinguish them programmatically you’ll need to look at the shape of the corresponding array.</p>

---
