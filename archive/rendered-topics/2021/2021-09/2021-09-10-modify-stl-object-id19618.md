# Modify stl object

**Topic ID**: 19618
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/modify-stl-object/19618

---

## Post #1 by @Vinny (2021-09-10 21:14 UTC)

<p>Hello,</p>
<p>I am using Slicer version 4.11.20200930 on Ubuntu 20.04 OS.  I have imported electrode leads as STL objects from a Matlab-based toolbox and noticed that the black/white colour coding for contacts and inter-contact gaps were missing.  However, when I had changed the opacity, it seems that markings highlighting the boundaries for the contacts and gaps are present.<br>
Is there a way to replicate the electrode lead black/white colour coding scheme for the Slicer scene?  I’ve attached a few pics to illustrate.</p>
<p>Thanks,</p>
<p>Vinny<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1170f1b8fabb03ba993145b66b2ccd20bef2991.jpeg" data-download-href="/uploads/short-url/tPHc5I62BM1NfODv3apxfRZBCMh.jpeg?dl=1" title="test1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1170f1b8fabb03ba993145b66b2ccd20bef2991_2_690x359.jpeg" alt="test1" data-base62-sha1="tPHc5I62BM1NfODv3apxfRZBCMh" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1170f1b8fabb03ba993145b66b2ccd20bef2991_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1170f1b8fabb03ba993145b66b2ccd20bef2991_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d1170f1b8fabb03ba993145b66b2ccd20bef2991_2_1380x718.jpeg 2x" data-dominant-color="7E7E7E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test1</span><span class="informations">1847×961 66.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff26e3ddeb4a1f98fe88b8c25bd9945f32be9acc.jpeg" data-download-href="/uploads/short-url/Apb4Kz6sNpgNTH276kSsx1fcf3C.jpeg?dl=1" title="test2-3dSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff26e3ddeb4a1f98fe88b8c25bd9945f32be9acc_2_690x451.jpeg" alt="test2-3dSlicer" data-base62-sha1="Apb4Kz6sNpgNTH276kSsx1fcf3C" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff26e3ddeb4a1f98fe88b8c25bd9945f32be9acc_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff26e3ddeb4a1f98fe88b8c25bd9945f32be9acc_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff26e3ddeb4a1f98fe88b8c25bd9945f32be9acc_2_1380x902.jpeg 2x" data-dominant-color="AFAFB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test2-3dSlicer</span><span class="informations">1409×922 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05d9d19ec87cef52a8e1de75c9827d15e18b80f4.jpeg" data-download-href="/uploads/short-url/PL3QuaU9ETmtSRWoJ7zYZ11Dms.jpeg?dl=1" title="test3-3dSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9d19ec87cef52a8e1de75c9827d15e18b80f4_2_690x451.jpeg" alt="test3-3dSlicer" data-base62-sha1="PL3QuaU9ETmtSRWoJ7zYZ11Dms" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9d19ec87cef52a8e1de75c9827d15e18b80f4_2_690x451.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9d19ec87cef52a8e1de75c9827d15e18b80f4_2_1035x676.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/05d9d19ec87cef52a8e1de75c9827d15e18b80f4_2_1380x902.jpeg 2x" data-dominant-color="AFAFB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test3-3dSlicer</span><span class="informations">1409×922 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-09-10 21:18 UTC)

<p>STL is a simple format that doesn’t support surface coloring.  It looks like there are internal polygons in the model you see when you change the transparency.  Maybe the easiest is to find a way would be to export a .vtk in polydata format with surface scalars and enable them in Slicer’s Models module.</p>

---

## Post #3 by @Vinny (2021-09-10 21:35 UTC)

<p>Thanks for your suggestion.  The only other format option for export is PLY.  However, the result is the same when viewed in the Slicer scene.</p>

---

## Post #4 by @pieper (2021-09-10 21:42 UTC)

<p>Did you try enabling scalars for the ply file?  They might be there.</p>
<p>Otherwise you’ll need to come up with another workaround, like adding additional models in the right place and putting them all in the same transform.</p>

---

## Post #5 by @Vinny (2021-09-10 21:47 UTC)

<p>Thank you very much, this worked perfectly!</p>
<p>Regards,</p>
<p>Vinny<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/204e79acf9396b0e3957e293e7875a241fa9b691.jpeg" data-download-href="/uploads/short-url/4BNpwbL50JHdAjFqFb6ns8T7enf.jpeg?dl=1" title="test4-3dSlicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/204e79acf9396b0e3957e293e7875a241fa9b691_2_690x467.jpeg" alt="test4-3dSlicer" data-base62-sha1="4BNpwbL50JHdAjFqFb6ns8T7enf" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/204e79acf9396b0e3957e293e7875a241fa9b691_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/204e79acf9396b0e3957e293e7875a241fa9b691_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/204e79acf9396b0e3957e293e7875a241fa9b691.jpeg 2x" data-dominant-color="B6B6B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test4-3dSlicer</span><span class="informations">1360×921 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
