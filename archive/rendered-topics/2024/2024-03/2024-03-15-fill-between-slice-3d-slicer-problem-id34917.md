# Fill between slice 3D slicer problem

**Topic ID**: 34917
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/fill-between-slice-3d-slicer-problem/34917

---

## Post #1 by @Simon_Molina (2024-03-15 18:16 UTC)

<p>Hello,<br>
I have a stent-graft geometry and I would like to fill its holes without modifying the rest of the geometry. I tried to use the fill between slice tool to do so but I can’t figure out how this works…<br>
In one of the photos you can see the holes for a slice in the axial plane</p>
<p>thank you for you help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac528ed81e22b38b8f41be6e8a8197eaad1b4f58.png" data-download-href="/uploads/short-url/oAr0hCFTPYFmj1CYRpb6g9xsrMY.png?dl=1" title="test 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac528ed81e22b38b8f41be6e8a8197eaad1b4f58.png" alt="test 3" data-base62-sha1="oAr0hCFTPYFmj1CYRpb6g9xsrMY" width="690" height="406" data-dominant-color="0F150F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test 3</span><span class="informations">726×428 1.63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6a4d89e4259061fe829fb0757fe5b3e40fb09b5.png" alt="test 2" data-base62-sha1="wUmZY0GMROCOC5TZT54THdyEkkd" width="215" height="207"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af287ee5bbf952e7a7f3d9f5b7f582d0aaadd1d4.png" data-download-href="/uploads/short-url/oZwjM2RBF9vDQBDaAnqVwdCLxHu.png?dl=1" title="test" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af287ee5bbf952e7a7f3d9f5b7f582d0aaadd1d4_2_150x500.png" alt="test" data-base62-sha1="oZwjM2RBF9vDQBDaAnqVwdCLxHu" width="150" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af287ee5bbf952e7a7f3d9f5b7f582d0aaadd1d4_2_150x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af287ee5bbf952e7a7f3d9f5b7f582d0aaadd1d4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af287ee5bbf952e7a7f3d9f5b7f582d0aaadd1d4.png 2x" data-dominant-color="7D9295"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test</span><span class="informations">156×518 42.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-03-17 01:00 UTC)

<p>Fill between slices requires complete segmentation within each slice. If you paint anything in a slice that is considered as a segmented slice and the effect will not change anything in that slice. To fill in holes, You can use Wrap Solidify effect instead (provided by SurfaceWrapSolidify extension).</p>

---

## Post #3 by @Simon_Molina (2024-03-18 09:58 UTC)

<p>Okay thank you for the tip !<br>
I tried to use SurfaceWrapSolidify but if fills the main hole…<br>
I also tried his “Create shell” feature but the shell stops there (in blue on the photo) and is not “closed” in the end<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/031f568298b253935c824a6855b7bee062e14dea.png" alt="test" data-base62-sha1="rCzyZ37kviEv08uPMTa7h6rxOy" width="360" height="223"></p>

---

## Post #4 by @Matteboo (2024-03-18 12:37 UTC)

<p>Maybe this is a naive proposition but have you tried to use the “closing” option in the segment editor ?<br>
If you choose your kernel size to be smaller than the central hole it will not fill it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1264b853d6812838c20f10082256ec9542fc54e4.png" data-download-href="/uploads/short-url/2CInWiUOwXJoG65M4nisa2v48rG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1264b853d6812838c20f10082256ec9542fc54e4_2_474x499.png" alt="image" data-base62-sha1="2CInWiUOwXJoG65M4nisa2v48rG" width="474" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1264b853d6812838c20f10082256ec9542fc54e4_2_474x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1264b853d6812838c20f10082256ec9542fc54e4_2_711x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1264b853d6812838c20f10082256ec9542fc54e4.png 2x" data-dominant-color="38393A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">787×829 54.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
