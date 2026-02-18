# Can 2D dicom images be histogram matched in 3D slicer?

**Topic ID**: 23333
**Date**: 2022-05-08
**URL**: https://discourse.slicer.org/t/can-2d-dicom-images-be-histogram-matched-in-3d-slicer/23333

---

## Post #1 by @LIE_CAI (2022-05-08 20:33 UTC)

<p>Hello,</p>
<p>For example, when I use histogram matching method on 3D images, there are options to let me select the input, output and reference volumes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88ca06accafe66b28b55920900730bfb1fc7a655.png" data-download-href="/uploads/short-url/jw5M2w7B8VAYyEIMBnnmCLkPJyt.png?dl=1" title="scrs1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88ca06accafe66b28b55920900730bfb1fc7a655.png" alt="scrs1" data-base62-sha1="jw5M2w7B8VAYyEIMBnnmCLkPJyt" width="690" height="92" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scrs1</span><span class="informations">724×97 6.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I open a single DICOM image, for example, an ultrasound image, there are no such options:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54853271f78dbe2680f614e65223088f732c1544.png" data-download-href="/uploads/short-url/c3HtOwdT2ilk2c6rvRAy8PlzbGk.png?dl=1" title="scrs2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54853271f78dbe2680f614e65223088f732c1544_2_690x91.png" alt="scrs2" data-base62-sha1="c3HtOwdT2ilk2c6rvRAy8PlzbGk" width="690" height="91" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54853271f78dbe2680f614e65223088f732c1544_2_690x91.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54853271f78dbe2680f614e65223088f732c1544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54853271f78dbe2680f614e65223088f732c1544.png 2x" data-dominant-color="DDE6EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scrs2</span><span class="informations">722×96 8.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So my question is, can 2D dicom images be histogram matched in 3D slicer? Or does 3D slicer has better methods about preprocessing ultrasound images?</p>
<p>Thanks a lot !</p>

---

## Post #2 by @lassoan (2022-05-10 04:31 UTC)

<p>If you see a volume in the slice viewer but you don’t see it in a scalar volume selector then the most likely reason is that the image was saved as a color image (for example, because a screenshot was taken of the original image and saved as a tiff file).</p>
<p>I would recommend not to use such image because its quality may have been significantly and irreversibly degraded (may have been converted to 8 bits, compressed, etc.) and physical spacing information may have been altered. Instead, try to get the original image and use that.</p>
<p>If you want to use this potentially degraded image anyway then you can convert it to a scalar volume using <code>Vector to scalar volume</code> module.</p>

---
