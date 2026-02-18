# Model-to-Model Distance - How to see the Inside

**Topic ID**: 17233
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/model-to-model-distance-how-to-see-the-inside/17233

---

## Post #1 by @seanchoi0519 (2021-04-21 17:42 UTC)

<p>I have two tooth models I am comparing. One of them has been drilled (YELLOW), while the other is in pristine condition (RED). I have aligned them using ALPACA and then used model-to-model distance extension to calculate the difference between the two models (GREEN/BLUE).</p>
<p>Expected: When reduced opacity, I should be able to see the difference inside the tooth.<br>
Actual: Only the difference of the outside surface area can be seen via the colour map.</p>
<p>How can I adjust so that I can see not only the outside surface, but also the hollow inside difference?<br>
Thanks in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f167eb141fb671c38176633fc9b03b5cbcd914d9.jpeg" data-download-href="/uploads/short-url/yrzIhBwn4hkRQcoIy2hWAopsfAR.jpeg?dl=1" title="Screen Shot 2021-04-22 at 2.26.14 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f167eb141fb671c38176633fc9b03b5cbcd914d9_2_417x499.jpeg" alt="Screen Shot 2021-04-22 at 2.26.14 AM" data-base62-sha1="yrzIhBwn4hkRQcoIy2hWAopsfAR" width="417" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f167eb141fb671c38176633fc9b03b5cbcd914d9_2_417x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f167eb141fb671c38176633fc9b03b5cbcd914d9_2_625x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f167eb141fb671c38176633fc9b03b5cbcd914d9_2_834x998.jpeg 2x" data-dominant-color="A04965"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 2.26.14 AM</span><span class="informations">1192×1428 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2021-04-21 18:54 UTC)

<p>For the model of interest, in the “Display” section of the Models module, in the “3D Display” section, make sure that “Visible Sides” is set to “All”.  If it is set to “Front” then only the outer surface is rendered and inner surfaces are invisible.</p>
<p>Once you do that, you might also try using the “Clipping Planes” section to get cut-away views.</p>

---

## Post #3 by @smrolfe (2021-04-21 19:29 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="1" data-topic="17233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Expected: When reduced opacity, I should be able to see the difference inside the tooth.</p>
</blockquote>
</aside>
<p>The model to model surface will calculate the difference for each point on the source model. It looks like the tooth without drilling is the source model here? If this model has no interior structure, there will be no values on the interior. In this case, you might consider reversing the mapping and using the drilled tooth as the source model.</p>

---

## Post #5 by @seanchoi0519 (2021-04-22 08:32 UTC)

<p>Thank you for your advice, however it is already set to all visible sides.</p>

---

## Post #6 by @seanchoi0519 (2021-04-22 08:32 UTC)

<aside class="quote no-group" data-username="smrolfe" data-post="3" data-topic="17233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>The model to model surface will calculate the difference for each point on the source model. It looks like the tooth without drilling is the source model here? If this model has no interior structure, there will be no values on the interior. In this case, you might consider reversing the mapping and using the drilled tooth as the source model.</p>
</blockquote>
</aside>
<p>Thank you. I’ve swapped the two and I am getting a better result. However, I am still confused as in theory, the inside of the tooth should show red, not green as shown in the pic attached. The only difference between the two teeth is the hollow inside cavity.</p>
<p>Would you have any idea what’s going on here?<br>
Sincerely</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98709062405445ad293ca222604cd88ebaef47ba.jpeg" data-download-href="/uploads/short-url/lKxK3bwAuTy09CyyybawfSwqr8K.jpeg?dl=1" title="Screen Shot 2021-04-22 at 6.24.55 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98709062405445ad293ca222604cd88ebaef47ba_2_347x500.jpeg" alt="Screen Shot 2021-04-22 at 6.24.55 PM" data-base62-sha1="lKxK3bwAuTy09CyyybawfSwqr8K" width="347" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98709062405445ad293ca222604cd88ebaef47ba_2_347x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98709062405445ad293ca222604cd88ebaef47ba_2_520x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98709062405445ad293ca222604cd88ebaef47ba_2_694x1000.jpeg 2x" data-dominant-color="6382A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 6.24.55 PM</span><span class="informations">1014×1460 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @smrolfe (2021-04-22 17:28 UTC)

<p>If this is the output from the ModelToModelDistance module, the colors will correspond to the signed or unsigned Hausdorff distance between the source and the target points (if you are using the signed or absolute closest point options in the module).</p>
<p>The colors that each distance value is mapped to is determined by the color table, which you can adjust in the Models module, under the ‘Scalers’ menu.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae568cf1098596ddc6004a6b9f6a8b8a0d564da4.png" data-download-href="/uploads/short-url/oSgvQ8lmXZfxVwQhv0td9UpggYc.png?dl=1" title="Screen Shot 2021-04-22 at 10.27.09 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae568cf1098596ddc6004a6b9f6a8b8a0d564da4_2_526x500.png" alt="Screen Shot 2021-04-22 at 10.27.09 AM" data-base62-sha1="oSgvQ8lmXZfxVwQhv0td9UpggYc" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae568cf1098596ddc6004a6b9f6a8b8a0d564da4_2_526x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae568cf1098596ddc6004a6b9f6a8b8a0d564da4_2_789x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae568cf1098596ddc6004a6b9f6a8b8a0d564da4_2_1052x1000.png 2x" data-dominant-color="3E3C3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-04-22 at 10.27.09 AM</span><span class="informations">1600×1520 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
