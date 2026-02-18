# Loading dynamic sequence

**Topic ID**: 1652
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/loading-dynamic-sequence/1652

---

## Post #1 by @Bing (2017-12-12 19:08 UTC)

<p>Hi,<br>
When I upload a new subject .dicom file, the new 4.8 version was not able to identify the dynamic sequence as a sequence but as 20+ separate slice. Is there any setting should debug before loading?</p>
<p>Thanks and have a great day!</p>
<p>Bing</p>

---

## Post #2 by @lassoan (2017-12-12 19:52 UTC)

<p>There have been related fixes since 4.8. Could you please try the latest nightly?</p>

---

## Post #3 by @Bing (2017-12-12 19:53 UTC)

<p>Great to know this~ Thanks a lot~</p>

---

## Post #4 by @Bing (2017-12-12 20:06 UTC)

<p>Just install the most recently released version, but the plugin could not open at all… Could you please help me about that or should I go back to the 4.8.0 again? Thanks~</p>

---

## Post #5 by @lassoan (2017-12-12 22:41 UTC)

<aside class="quote no-group" data-username="Bing" data-post="4" data-topic="1652">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/839c29/48.png" class="avatar"> Bing:</div>
<blockquote>
<p>plugin could not open at all</p>
</blockquote>
</aside>
<p>What do you mean? What happens exactly?</p>

---

## Post #6 by @Bing (2017-12-13 15:36 UTC)

<p>I reboot my computer, and it work now~ Thanks~~<br>
Could you please help me find a way that how to measure a curvature in the two dimensional images? The annotations module doesn’t have the curvature ruler, and I tried the fiducials and use the curve maker plugin. Is there any other easier way to do it? Appreciate your help~</p>

---

## Post #7 by @Frederic (2017-12-13 15:48 UTC)

<p>Hi,<br>
As far I am concerned, I advice you, if your image is in 2D, to use ImageJ and the module “<a href="https://imagej.net/Compute_Curvatures" rel="nofollow noopener">Compute curvature</a>”.<br>
If you image is in 3D, 3dslicer is the good place and I could give you a little script that I have done in 3Dslicer.<br>
Best.</p>

---

## Post #8 by @Bing (2017-12-13 15:57 UTC)

<p>Thanks, great to know this~<br>
Yes,as you mentioned, ImageJ absolutely works for two dimensional measurements. But, we are planning measure the curvature length based on the tipped plane, that‘s the reason why we are looking the ideal module for measuring. It will save a lot of time if it is feasible in Slicer rather than capture the screen, export images, reset the scale in ImageJ.</p>
<p>Thanks and best.</p>

---

## Post #9 by @lassoan (2017-12-13 19:09 UTC)

<p>We’ve been working on improving measurement features in Slicer in the coming weeks. What would you like to measure exactly?</p>

---

## Post #10 by @Bing (2017-12-13 22:06 UTC)

<p>It’s exciting!!<br>
Here are the measurements we are planning to measure:</p>
<ol>
<li>We are measuring the curvature length of the uterosacral ligaments in the tipped coronal slide.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2a70e203418bba3a34c61213329b9da7865b744.jpeg" data-download-href="/uploads/short-url/ncTgnTZSp024rXk2V60nMVqrO5u.jpeg?dl=1" title="WechatIMG17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a70e203418bba3a34c61213329b9da7865b744_2_690x390.jpeg" alt="WechatIMG17" data-base62-sha1="ncTgnTZSp024rXk2V60nMVqrO5u" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a70e203418bba3a34c61213329b9da7865b744_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a70e203418bba3a34c61213329b9da7865b744_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2a70e203418bba3a34c61213329b9da7865b744_2_1380x780.jpeg 2x" data-dominant-color="95949F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG17</span><span class="informations">3360×1902 720 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
<li>The cross-sectional area of the muscle in the tipped coronal slide(or let’s say the area of the ROI).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8cedda4f768d6b17e2662a5b044ac2dab784697.jpeg" data-download-href="/uploads/short-url/xdvYPferjHPSwSBR0VuLocpCrnV.jpeg?dl=1" title="WechatIMG18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8cedda4f768d6b17e2662a5b044ac2dab784697_2_690x390.jpeg" alt="WechatIMG18" data-base62-sha1="xdvYPferjHPSwSBR0VuLocpCrnV" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8cedda4f768d6b17e2662a5b044ac2dab784697_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8cedda4f768d6b17e2662a5b044ac2dab784697_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8cedda4f768d6b17e2662a5b044ac2dab784697_2_1380x780.jpeg 2x" data-dominant-color="9595A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WechatIMG18</span><span class="informations">3360×1902 794 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p>If those measurements could be done in Slicer, that will be tremendous~</p>
<p>Thanks and Best.</p>

---
