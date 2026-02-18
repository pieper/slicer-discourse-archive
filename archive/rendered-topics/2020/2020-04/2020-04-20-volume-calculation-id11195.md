# Volume calculation

**Topic ID**: 11195
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/volume-calculation/11195

---

## Post #1 by @siaeleni (2020-04-20 02:43 UTC)

<p>Hi all,<br>
Here you can see that I have uploaded two different models and I want to calculate the Volumes.<br>
I am expecting that the green to have a larger volume, but I get significantly larger;<br>
green = 1147349mm^3<br>
blue   = 127196mm^3<br>
I am trying to understand what exactly is calculated at the blue case?<br>
The “Inside Blue” Volume or the “Between Blue” volume?<br>
(please see the image attached)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc015e7326d60c6267e2298b336b8f17acc392ea.png" data-download-href="/uploads/short-url/zXlfQ9BUh7bDICcFdYU5kK9EK0y.png?dl=1" title="pic1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc015e7326d60c6267e2298b336b8f17acc392ea_2_690x355.png" alt="pic1" data-base62-sha1="zXlfQ9BUh7bDICcFdYU5kK9EK0y" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc015e7326d60c6267e2298b336b8f17acc392ea_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc015e7326d60c6267e2298b336b8f17acc392ea_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc015e7326d60c6267e2298b336b8f17acc392ea_2_1380x710.png 2x" data-dominant-color="636363"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic1</span><span class="informations">1918×988 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-20 04:45 UTC)

<p>Blue is a shell (it is hollow), while green is an open surface, which gets closed in some way by the volume computation algorithm. Since green is not hollow, it has much larger volume.</p>
<p>Note that volume is undefined for open surfaces and for example, result may heavily depend on orientation of the mesh, it is advisable to close the surface first. The simplest is to convert it to segmentation node (by right-clicking on it in Data module) - you will see how exactly the surface gets closed - and use Segment Statistics to get the volume.</p>
<p>If you want to compare volumes then you need to solidify the hollow model. For this, you can use the excellent Wrap Solidify effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>).</p>

---

## Post #3 by @siaeleni (2020-04-20 23:40 UTC)

<p>Thanks, Andras, I converted them to hollow and now seems that are comparable.<br>
This is what I get (image attached).<br>
I was wondering how can I get the whole inside blue volume as well? Is there any way to measure that as well?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6300285499009976bece7bf93ac86c9002a6457.jpeg" data-download-href="/uploads/short-url/z7SjJK8VPrr46qnKkbV2WQlOB4b.jpeg?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6300285499009976bece7bf93ac86c9002a6457_2_690x357.jpeg" alt="pic2" data-base62-sha1="z7SjJK8VPrr46qnKkbV2WQlOB4b" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6300285499009976bece7bf93ac86c9002a6457_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6300285499009976bece7bf93ac86c9002a6457_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6300285499009976bece7bf93ac86c9002a6457_2_1380x714.jpeg 2x" data-dominant-color="323431"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">1917×994 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-04-21 00:19 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="3" data-topic="11195">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>I was wondering how can I get the whole inside blue volume as well? Is there any way to measure that as well?</p>
</blockquote>
</aside>
<p>You can solidify a shell using WrapSolidify effect (provided by SurfaceWrapSolidify extension).</p>

---

## Post #5 by @siaeleni (2020-04-21 01:26 UTC)

<p>Oh I see what it does, thanks a lot again.</p>

---
