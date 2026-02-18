# Question about the visualization of displacement vector fields

**Topic ID**: 25090
**Date**: 2022-09-05
**URL**: https://discourse.slicer.org/t/question-about-the-visualization-of-displacement-vector-fields/25090

---

## Post #1 by @zhangzhehao (2022-09-05 03:53 UTC)

<p>Hi all,</p>
<p>I am doing image registration between two 3D CTs and have already got the dispalcement vector fields in MHA format with shape (224, 224, 96, 3), where first three dimensions represents the 3D image size.</p>
<p>Once I load my displacement field into Slicer, I can see a 3D color image and the vaule for each voxel is a 3-length vector representing the space shift along three directions, which also make sense. However, when I try to turn on the color legend for this image, it only gives me the grey color legend.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6db041c6b9c5b5fe9c069b7c6751f83c44976bbe.png" data-download-href="/uploads/short-url/fElFJ7t0W9Oedm6fT2ey0fxe4km.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6db041c6b9c5b5fe9c069b7c6751f83c44976bbe.png" alt="image" data-base62-sha1="fElFJ7t0W9Oedm6fT2ey0fxe4km" width="690" height="412" data-dominant-color="587762"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×414 78.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to change the lookup table for my displacement field but it seems the lookup table doesn’t work for this vector image. No matter which table I’m using, the real visualization result would not change. I know I can use the ‘Vector to Scalar Volume’ module to covert my vector image to some scalar image, but I’m just curious how the 3D Slicer deal with the visualization of a vector image by default or how does Slicer choose a specific color for a vector with multiple scalar values.</p>
<p>Appreciate for any help. Thank you.</p>
<p>Best,<br>
Zhehao</p>

---

## Post #2 by @pieper (2022-09-05 18:02 UTC)

<p>There’s no infrastructure to display scale bars for color (vector) volumes.  You can explore loading the data as a Transform and use the various visualization options which are quite powerful for this application.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes</a></p>

---

## Post #3 by @zhangzhehao (2022-09-05 19:35 UTC)

<p>Thank you for your quick reply. Loading the data as a ‘Transform’ rather than ‘Volume’ makes things reasonable!</p>
<p>Since it seems like Slicer can still handle the vector volume (like the wrong case I was using, loading displacement as Volume), do you have any idea about how Slicer visualize such vector image please? Using the magnitude of vector or something else?</p>
<p>Thanks again!</p>

---

## Post #4 by @pieper (2022-09-05 21:12 UTC)

<p>You’re welcome <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="zhangzhehao" data-post="3" data-topic="25090">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangzhehao/48/16515_2.png" class="avatar"> zhangzhehao:</div>
<blockquote>
<p>do you have any idea about how Slicer visualize such vector image please? Using the magnitude of vector or something else?</p>
</blockquote>
</aside>
<p>Probably the transform visualization is what you want.  But if you want a volume of vector magnitudes you can use the Vector To Scalar module as you mentioned earlier.</p>

---

## Post #5 by @zhangzhehao (2022-09-05 21:17 UTC)

<p>Got it. Thank you again!</p>

---
