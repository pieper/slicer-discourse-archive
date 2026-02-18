# Contouring the outer surface of a CT image

**Topic ID**: 13940
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/contouring-the-outer-surface-of-a-ct-image/13940

---

## Post #1 by @aseman (2020-10-08 18:47 UTC)

<p>Slicer version: 4.10.1<br>
Hi 3D Slicer Experts and all<br>
I have a CT image and I only want to contour its outside surface (like Figure A). I used Draw and Paint in the Segment Editor module. But it includes the inside area, too (Figure B). Also, when I use the Eraser, the outer line isn’t uniform. Is  it possible not to do this contouring manually? and can I obtain this outer line?<br>
Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f7c380a962aff1a1344e69130eff303d67b0b99.png" data-download-href="/uploads/short-url/ibMM90EiAtaDkU5MADfDBMtSN3X.png?dl=1" title="p2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7c380a962aff1a1344e69130eff303d67b0b99_2_517x183.png" alt="p2" data-base62-sha1="ibMM90EiAtaDkU5MADfDBMtSN3X" width="517" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7c380a962aff1a1344e69130eff303d67b0b99_2_517x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f7c380a962aff1a1344e69130eff303d67b0b99_2_775x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f7c380a962aff1a1344e69130eff303d67b0b99.png 2x" data-dominant-color="AFAFB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">p2</span><span class="informations">859×306 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/105b802ac29ec16734c621b61dd8ab254f2cf7af.png" alt="p1" data-base62-sha1="2kHG5c81FJhlDmx1q5uLIvoDxdt" width="237" height="158"></p>

---

## Post #2 by @lassoan (2020-10-09 03:06 UTC)

<p>You can use <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify</a> extension to fill internal cavities in a segment.</p>

---

## Post #3 by @manjula (2020-10-09 06:55 UTC)

<p>I use the hollow effect to get what you describing and it gives very good results.You can use the hollow effect first to get the inner or outer surfaces and as Prof Lasso said then use the warpsolodify to fill inside if you want again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/179bc977d0a995583493b59186b7b57f4a9df93a.jpeg" data-download-href="/uploads/short-url/3mQKJYlq4ahK2WgU6KvnMwD8kdk.jpeg?dl=1" title="Screenshot from 2020-10-09 08-58-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/179bc977d0a995583493b59186b7b57f4a9df93a_2_690x322.jpeg" alt="Screenshot from 2020-10-09 08-58-21" data-base62-sha1="3mQKJYlq4ahK2WgU6KvnMwD8kdk" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/179bc977d0a995583493b59186b7b57f4a9df93a_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/179bc977d0a995583493b59186b7b57f4a9df93a_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/179bc977d0a995583493b59186b7b57f4a9df93a_2_1380x644.jpeg 2x" data-dominant-color="787774"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-09 08-58-21</span><span class="informations">1851×864 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @aseman (2020-10-15 19:44 UTC)

<p>Hi<br>
Thank you very much for your helpful reply. now I have another question. I want to shift the red contour d cm to the Anterior( like the figure) . How can I do this?<br>
If the value of d in each slice be different (di), can I shift the red contour in each slice separately di cm?<br>
Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/437dc1ecb98b70f272ff1fda908b06cdb149795a.png" data-download-href="/uploads/short-url/9D3qkMlqO6Uxw4Hidi4FVNyJAD0.png?dl=1" title="pic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/437dc1ecb98b70f272ff1fda908b06cdb149795a_2_483x375.png" alt="pic" data-base62-sha1="9D3qkMlqO6Uxw4Hidi4FVNyJAD0" width="483" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/437dc1ecb98b70f272ff1fda908b06cdb149795a_2_483x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/437dc1ecb98b70f272ff1fda908b06cdb149795a_2_724x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/437dc1ecb98b70f272ff1fda908b06cdb149795a.png 2x" data-dominant-color="101111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic</span><span class="informations">728×565 75.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-10-15 20:38 UTC)

<p>What do you mean by “shifting” the contour? What would you like to achieve?</p>
<p>What is the clinical application? (maybe we can point to readily available solutions)</p>

---

## Post #6 by @aseman (2020-10-22 16:52 UTC)

<p>Hi<br>
I’m sorry for the delay in reply. I want to design a bolus for a mastectomy patient. In figure C, the following steps seem to have been performed :</p>
<p>First, internal (B) and external (A) contours are defined. Then, the inner contour is shifted to the Anterior. Finally, the difference between the two contours (B-A) is obtained, which its result is  Figure D. I want to do exactly the same steps. But I don’t know how to shift the inner contour d cm.<br>
Also, the value of d in each slice is variable (di). Is it possible to shift the internal contour di cm in each slice?<br>
Thanks a lot</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a75e1c386b17e26248403aca5fb25021a3d8317.png" alt="BOLUS" data-base62-sha1="jKSs0maNQJKIYbrakfOJbz0EaX5" width="432" height="193"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa9d2129e0723ba0631e18ac474cdabcee73a013.png" alt="BOLUS2" data-base62-sha1="oljOKdmPvC7zZVfOUZZJgul8exd" width="356" height="235"></p>

---

## Post #7 by @lassoan (2020-10-22 21:14 UTC)

<p>You can shift contours using Margin effect. To create a thick shell over a surface, use Hollow effect (us current segment as inner surface) and remove what is not needed using Scissors effect (and you can remove the side that you don’t need using Islands effect). Once you figure out all the steps you need, you can automate everything using Python scripting.</p>

---
