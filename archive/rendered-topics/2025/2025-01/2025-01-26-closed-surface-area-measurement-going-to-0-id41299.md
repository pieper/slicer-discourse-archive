---
topic_id: 41299
title: "Closed Surface Area Measurement Going To 0"
date: 2025-01-26
url: https://discourse.slicer.org/t/41299
---

# Closed surface area measurement going to 0

**Topic ID**: 41299
**Date**: 2025-01-26
**URL**: https://discourse.slicer.org/t/closed-surface-area-measurement-going-to-0/41299

---

## Post #1 by @cgordon_Slicer (2025-01-26 22:03 UTC)

<p>Hello!</p>
<p>I’m trying to measure the surface areas of segmented muscle attachment sites using the Closed Curve (CC) Markups tool. However, whenever I trace too complex or too inwardly bending of a shape, its area automatically changes to zero. I show this happening in real-time in the attached video. I know it’s not too small an area, and in the video you’ll see on the right a smaller but simpler CC that has a non-zero area.</p>
<p>This issue persists regardless of which Curve Type I select for the CC and regardless of how many decimal points of precision I allow for the area.</p>
<p>Why does this happen? Is there any way to get around this issue?</p>
<p>Thank you for your help with this!</p>
<p>Best,<br>
cgordon</p>

---

## Post #2 by @lassoan (2025-01-26 22:38 UTC)

<p>Computing surface area enclosed by a closed planar curve is a well-defined, trivial task. However, if the curve is non-planar then the the task becomes very complex or impossible to solve. Slicer computes a soap-bubble-like-surface by warping a disk by a thin-plate spline. If the soap bubble surface is infeasible because to the shape of the curve is highly non-planar and not smooth then you will get 0 surface area.</p>
<p>There are many ways to define surfaces in Slicer, you just need to find the appropriate modeling tool for the task.</p>
<p>I suspect that you actually want to cut out a surface patch from a segmented structure. You can do that by exporting the segmentation to a model node and then use tools in the Dynamic Modeler module.</p>
<p>If you have trouble using the Dynamic Modeler module or you think it is not the right tool then please write a bit more details about what you need and post a couple of screenshots.</p>

---

## Post #3 by @cgordon_Slicer (2025-01-26 23:07 UTC)

<p>Hi Mr. Lasso, thank you for this quick reply!</p>
<p>If calculating a non-planar curve’s area is infeasible, I would be happy to cut out a surface patch from the segmented mesh instead.</p>
<p>Unfortunately, so far I haven’t been able to do this. When I try to “Select by points” within the Dynamic Modeler module, and click Apply, my model disappears (see screenshots attached).</p>
<p>Is there any chance you would be open to Zooming about this issue to go over how to proceed with the Dynamic Modeler option?</p>
<p>If so, I would email you a Zoom link and happily Venmo you a coffee!</p>
<p>Best,<br>
Caleb<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06635e30d9da51d27b584e099a835b830c3c2315.png" data-download-href="/uploads/short-url/UvL62MPPTHffnylDnRUUg8cDGJ.png?dl=1" title="Screenshot 2025-01-26 at 5.58.42 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06635e30d9da51d27b584e099a835b830c3c2315_2_690x470.png" alt="Screenshot 2025-01-26 at 5.58.42 PM" data-base62-sha1="UvL62MPPTHffnylDnRUUg8cDGJ" width="690" height="470" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06635e30d9da51d27b584e099a835b830c3c2315_2_690x470.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06635e30d9da51d27b584e099a835b830c3c2315_2_1035x705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06635e30d9da51d27b584e099a835b830c3c2315.png 2x" data-dominant-color="BDBED8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-26 at 5.58.42 PM</span><span class="informations">1239×845 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3245bba25725ecb3f01a3e3bcefbe6182ba59b3b.png" data-download-href="/uploads/short-url/7aJh5FREUgwzgdJ7VxKZ1hyixzd.png?dl=1" title="Screenshot 2025-01-26 at 6.03.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/3245bba25725ecb3f01a3e3bcefbe6182ba59b3b_2_690x471.png" alt="Screenshot 2025-01-26 at 6.03.31 PM" data-base62-sha1="7aJh5FREUgwzgdJ7VxKZ1hyixzd" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/3245bba25725ecb3f01a3e3bcefbe6182ba59b3b_2_690x471.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/3245bba25725ecb3f01a3e3bcefbe6182ba59b3b_2_1035x706.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/3245bba25725ecb3f01a3e3bcefbe6182ba59b3b.png 2x" data-dominant-color="BDBDDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-26 at 6.03.31 PM</span><span class="informations">1243×849 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @sajad_amiri (2025-01-29 12:46 UTC)

<aside class="quote no-group" data-username="cgordon_Slicer" data-post="1" data-topic="41299">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b9bd4f/48.png" class="avatar"> cgordon_Slicer:</div>
<blockquote>
<p>surface areas</p>
</blockquote>
</aside>
<p>you can use Pyradiomics one of the features of that is surface area of segmentation</p>

---
