# "Show 3D" only meshing outside of ROI

**Topic ID**: 15826
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/show-3d-only-meshing-outside-of-roi/15826

---

## Post #1 by @d_roscoe_j (2021-02-04 02:49 UTC)

<p>After uploading a .vol file of an sonogram, I create a volume rendering of the file and crop the ROI to be the section I want isolated (roughly) then change the “gradient anisotropic diffusion” of the roi, creating a new output volume.</p>
<p>Then, in the segment editor module, I add a new segment, setting the output volume as the “master volume”.<br>
After adjusting the threshold to almost any level/combination and clicking apply, after attempting to “Show 3D”, the only 3d mesh that appears is outside of the selected ROI box and seems to both begin and end right at the ROI faces.</p>
<p>Does it seem like I’m doing something wrong with cropping, diffusing, adding the segment, defining the threshold… or something in between?</p>
<p>Been at it for hours and running out of ideas.<br>
Thanks in advance for any ideas!</p>
<p>Operating system: Win10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: “show 3d” is supposed to make a mesh inside the selected segment, not outside<br>
Actual behavior: “Show 3d” is meshing only sections that have already been cropped out-outside the ROI<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f255e91adc686650fef67a01b70ccd42596ca4.jpeg" data-download-href="/uploads/short-url/5yxlq1ADTgwOjbSmZpoLyhIOmWM.jpeg?dl=1" title="Screenshot 2021-02-03 20.03.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f255e91adc686650fef67a01b70ccd42596ca4_2_690x388.jpeg" alt="Screenshot 2021-02-03 20.03.06" data-base62-sha1="5yxlq1ADTgwOjbSmZpoLyhIOmWM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f255e91adc686650fef67a01b70ccd42596ca4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/26f255e91adc686650fef67a01b70ccd42596ca4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f255e91adc686650fef67a01b70ccd42596ca4.jpeg 2x" data-dominant-color="A4A7B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-03 20.03.06</span><span class="informations">1368×770 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21fa169a8d05cdf9f7ab623d77420c74081dd098.jpeg" data-download-href="/uploads/short-url/4QzzegublYldNbrl64ehhZOmeMM.jpeg?dl=1" title="Screenshot 2021-02-03 20.03.19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fa169a8d05cdf9f7ab623d77420c74081dd098_2_690x391.jpeg" alt="Screenshot 2021-02-03 20.03.19" data-base62-sha1="4QzzegublYldNbrl64ehhZOmeMM" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fa169a8d05cdf9f7ab623d77420c74081dd098_2_690x391.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21fa169a8d05cdf9f7ab623d77420c74081dd098_2_1035x586.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21fa169a8d05cdf9f7ab623d77420c74081dd098.jpeg 2x" data-dominant-color="A3A0A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-03 20.03.19</span><span class="informations">1365×774 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/930ef6e996c77b73c7b31ef8b7b5c8cbecfa2bc9.jpeg" data-download-href="/uploads/short-url/kYWfsTGATpkl99WgIqF9q6y2pW9.jpeg?dl=1" title="Screenshot 2021-02-03 20.03.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/930ef6e996c77b73c7b31ef8b7b5c8cbecfa2bc9_2_690x386.jpeg" alt="Screenshot 2021-02-03 20.03.49" data-base62-sha1="kYWfsTGATpkl99WgIqF9q6y2pW9" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/930ef6e996c77b73c7b31ef8b7b5c8cbecfa2bc9_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/930ef6e996c77b73c7b31ef8b7b5c8cbecfa2bc9_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/930ef6e996c77b73c7b31ef8b7b5c8cbecfa2bc9.jpeg 2x" data-dominant-color="A7A2AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-03 20.03.49</span><span class="informations">1373×770 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce143853d3cd8168d4c91477a6a81d128a4809e1.jpeg" data-download-href="/uploads/short-url/tp3GaoQtGnZAsG5mWsE6a4LjaCJ.jpeg?dl=1" title="Screenshot 2021-02-03 20.27.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce143853d3cd8168d4c91477a6a81d128a4809e1_2_690x390.jpeg" alt="Screenshot 2021-02-03 20.27.24" data-base62-sha1="tp3GaoQtGnZAsG5mWsE6a4LjaCJ" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce143853d3cd8168d4c91477a6a81d128a4809e1_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce143853d3cd8168d4c91477a6a81d128a4809e1_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce143853d3cd8168d4c91477a6a81d128a4809e1.jpeg 2x" data-dominant-color="A5AEAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-02-03 20.27.24</span><span class="informations">1365×772 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-04 03:20 UTC)

<aside class="quote no-group" data-username="d_roscoe_j" data-post="1" data-topic="15826">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ad7895/48.png" class="avatar"> d_roscoe_j:</div>
<blockquote>
<p>After adjusting the threshold to almost any level/combination and clicking apply, after attempting to “Show 3D”, the only 3d mesh that appears is outside of the selected ROI box and seems to both begin and end right at the ROI faces.</p>
</blockquote>
</aside>
<p>The ROI that you define to crop volume rendering display has no effect anywhere else.</p>
<p>If you want, you can use that ROI in Crop volume module, but you can just as easily crop away parts of segments using Segment Editor (such as Scissors).</p>

---

## Post #3 by @d_roscoe_j (2021-02-04 03:51 UTC)

<p>When I attempt to crop using scissors, I see something similar to <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa354314d5e85a7c04bc03ec8e15c91feb3ecedb.jpeg" data-download-href="/uploads/short-url/zHrtOXF30Dr1ceDGurdefGXZuS7.jpeg?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa354314d5e85a7c04bc03ec8e15c91feb3ecedb_2_690x387.jpeg" alt="5" data-base62-sha1="zHrtOXF30Dr1ceDGurdefGXZuS7" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa354314d5e85a7c04bc03ec8e15c91feb3ecedb_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa354314d5e85a7c04bc03ec8e15c91feb3ecedb_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa354314d5e85a7c04bc03ec8e15c91feb3ecedb.jpeg 2x" data-dominant-color="A2A0A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1365×766 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So the fluid cloud is still visible after attempting to crop it all away. Am I missing a step or function on cropping the entire object away?</p>
<p>This is the first project I’ve ever tried to use this software for, so I greatly appreciate your patience and help!</p>

---

## Post #4 by @lassoan (2021-02-05 04:18 UTC)

<p>If the goal is 3D printing then just hide the volume rendering. It will not be useful for creating a printable model.</p>
<p>If you want to create nice 3D renderings then use Mask volume effect to blank out region outside the segment:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---
