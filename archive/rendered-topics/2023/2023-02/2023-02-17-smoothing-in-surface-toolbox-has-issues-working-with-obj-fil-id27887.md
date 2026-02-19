---
topic_id: 27887
title: "Smoothing In Surface Toolbox Has Issues Working With Obj Fil"
date: 2023-02-17
url: https://discourse.slicer.org/t/27887
---

# Smoothing in Surface toolbox has issues working with OBJ file with texture coordinates

**Topic ID**: 27887
**Date**: 2023-02-17
**URL**: https://discourse.slicer.org/t/smoothing-in-surface-toolbox-has-issues-working-with-obj-file-with-texture-coordinates/27887

---

## Post #1 by @chz31 (2023-02-17 19:35 UTC)

<p>Hi all,</p>
<p>It appears that the Taubin &amp; Laplace smoothing in Surface Toolbox does not work well with OBJ format. For example, decimation does not work. Furthermore, when I altered the parameters between the higher and lower ends in Taubin smoothing, there is essentially no difference between the outcomes. It appears that smoothing does not work at all.</p>
<p>original model<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5ea8324cebcdf11749aa1f41e073c09b1f389d.jpeg" data-download-href="/uploads/short-url/kjsBm7pyTSiyqROeo6yNMyhrXOt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5ea8324cebcdf11749aa1f41e073c09b1f389d_2_517x207.jpeg" alt="image" data-base62-sha1="kjsBm7pyTSiyqROeo6yNMyhrXOt" width="517" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5ea8324cebcdf11749aa1f41e073c09b1f389d_2_517x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5ea8324cebcdf11749aa1f41e073c09b1f389d_2_775x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5ea8324cebcdf11749aa1f41e073c09b1f389d_2_1034x414.jpeg 2x" data-dominant-color="41AD56"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×772 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Lower pass band &amp; iteration in Taubin smoothing<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bb27ae2333b846c3885fbf628e2542d0a932fb0.jpeg" data-download-href="/uploads/short-url/8w6yRX9gUwt7BOA9wrYZaW0sWc0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb27ae2333b846c3885fbf628e2542d0a932fb0_2_517x291.jpeg" alt="image" data-base62-sha1="8w6yRX9gUwt7BOA9wrYZaW0sWc0" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb27ae2333b846c3885fbf628e2542d0a932fb0_2_517x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb27ae2333b846c3885fbf628e2542d0a932fb0_2_775x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bb27ae2333b846c3885fbf628e2542d0a932fb0_2_1034x582.jpeg 2x" data-dominant-color="A8A872"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1524×859 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Higher pass band &amp; iterations in Taubin smoothing<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fa18d9d5ab2c8995e050a7b16378ca16c817a64.jpeg" data-download-href="/uploads/short-url/2ehhRF2rJXmu9Sx3S3lzGNHrutK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa18d9d5ab2c8995e050a7b16378ca16c817a64_2_517x272.jpeg" alt="image" data-base62-sha1="2ehhRF2rJXmu9Sx3S3lzGNHrutK" width="517" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa18d9d5ab2c8995e050a7b16378ca16c817a64_2_517x272.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa18d9d5ab2c8995e050a7b16378ca16c817a64_2_775x408.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fa18d9d5ab2c8995e050a7b16378ca16c817a64_2_1034x544.jpeg 2x" data-dominant-color="A06C75"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1674×882 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Taubin smoothing works well with the OBJ model in MeshLab. It could be due to the texture coordinates in the OBJ file that disrupts Surface Toolbox functions. When I save the OBJ file in PLY format, the smoothing function in Surface Toolbox works well.</p>
<p>Here is the link to the OBJ file I am using: <a href="https://drive.google.com/file/d/1ZxJcx2nM-fgywA8KMm6JO0t7QJIcQR7O/view?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">test_beaver-textured_model.zip - Google Drive</a></p>

---

## Post #2 by @chz31 (2023-02-17 19:49 UTC)

<aside class="quote no-group" data-username="chz31" data-post="1" data-topic="27887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>BJ model in MeshLab. It could be due to the texture coordinates in the OBJ file that disrupts Surface Toolbox functions. When I save the OBJ file in PLY format, the smoothing function in Surface Toolbox works well.</p>
</blockquote>
</aside>
<p>Just a follow up, decimation in Surface Toolbox appears to also have issues. For the same OBJ model, when I decimate it to 50%, it becomes like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/438a8f7e6df048618c99035b4ec2ce2f97dda905.jpeg" data-download-href="/uploads/short-url/9DuR0TqN3eEFcsZijAuU72JrKMR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/438a8f7e6df048618c99035b4ec2ce2f97dda905_2_517x254.jpeg" alt="image" data-base62-sha1="9DuR0TqN3eEFcsZijAuU72JrKMR" width="517" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/438a8f7e6df048618c99035b4ec2ce2f97dda905_2_517x254.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/438a8f7e6df048618c99035b4ec2ce2f97dda905.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/438a8f7e6df048618c99035b4ec2ce2f97dda905.jpeg 2x" data-dominant-color="A1A0A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">720×354 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Again, in MeshLab, I tried decimation in Meshlab, such as the quadric edge collapse and did not encounter this issue. Is it more due to the nature of the OBJ file I have or the functions in the Surface Toolbox may not work well with OBJ format with texture coordiantes? Thanks!</p>

---

## Post #3 by @pieper (2023-02-17 19:58 UTC)

<p>That model has a lot of geometry issues - if I enable the Clean step first then the decimation and smoothing filters appear to be working well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5a821e368f4baf2e71902d9f0f5057eb9077141.png" data-download-href="/uploads/short-url/nDt0hBh9s2QkGS6NSFCx3md9HY5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5a821e368f4baf2e71902d9f0f5057eb9077141_2_690x300.png" alt="image" data-base62-sha1="nDt0hBh9s2QkGS6NSFCx3md9HY5" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5a821e368f4baf2e71902d9f0f5057eb9077141_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5a821e368f4baf2e71902d9f0f5057eb9077141_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5a821e368f4baf2e71902d9f0f5057eb9077141_2_1380x600.png 2x" data-dominant-color="B9BAA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1581×688 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @chz31 (2023-02-17 20:20 UTC)

<p>I got the same result. Thanks, Steve!</p>

---

## Post #5 by @tsehrhardt (2023-02-18 12:57 UTC)

<p>This model consists of 2033 components and 77819 unreferenced vertices (from Meshlab). If it were “remeshed” into a single mesh, I think you would have fewer issues. The Poisson surface reconstruction filter in Meshlab can do this. It’s still a bit messy though, so it might help to resample the points before remeshing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffcd52c206dc4355682f9585ba7282ab983211a7.jpeg" data-download-href="/uploads/short-url/AuVENxlqWbDSLL8Fr4xsvLGOMRx.jpeg?dl=1" title="2023-02-18_7-56-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffcd52c206dc4355682f9585ba7282ab983211a7_2_690x390.jpeg" alt="2023-02-18_7-56-19" data-base62-sha1="AuVENxlqWbDSLL8Fr4xsvLGOMRx" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffcd52c206dc4355682f9585ba7282ab983211a7_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffcd52c206dc4355682f9585ba7282ab983211a7_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffcd52c206dc4355682f9585ba7282ab983211a7_2_1380x780.jpeg 2x" data-dominant-color="515084"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-02-18_7-56-19</span><span class="informations">3436×1947 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
