# How does the crosshair tool work on different series?

**Topic ID**: 27205
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/how-does-the-crosshair-tool-work-on-different-series/27205

---

## Post #1 by @francesca_flore (2023-01-12 12:32 UTC)

<p>Since I have 3 series, each of which has a high quality view and the other two low quality views, I display in 3D slicer the three best resolution planes chosen from the 3 series.<br>
If I crosshair and select a point in a plane, will it cause other Slice Viewers to scroll to the same position? Even if these come from 3 different series?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1c2bba21871500dac95aab55305d2b12b2c4bdb.jpeg" data-download-href="/uploads/short-url/rE5mDPCTQFgydeiQd3WGf80mhmP.jpeg?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c2bba21871500dac95aab55305d2b12b2c4bdb_2_659x500.jpeg" alt="Screenshot_3" data-base62-sha1="rE5mDPCTQFgydeiQd3WGf80mhmP" width="659" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c2bba21871500dac95aab55305d2b12b2c4bdb_2_659x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c2bba21871500dac95aab55305d2b12b2c4bdb_2_988x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c2bba21871500dac95aab55305d2b12b2c4bdb_2_1318x1000.jpeg 2x" data-dominant-color="4B4A52"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">1535×1163 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-12 23:25 UTC)

<p>Yes, the crosshair makes slice views jump to the same physical position.</p>
<p>The 3 orthogonal MRI series are usually reconstructed at the same time and they are accurately aligned in physical space, so everything should nicely line up.</p>

---

## Post #3 by @francesca_flore (2023-01-13 08:23 UTC)

<p>Even if the 3 series have a different slice thickness?</p>

---

## Post #4 by @lassoan (2023-01-13 12:24 UTC)

<p>Yes. Slicer performs all vísualization and processing in physical space, so it can work seamlessly with images with different origin, spacing, and axis directions.</p>

---

## Post #5 by @francesca_flore (2023-01-13 12:34 UTC)

<p>Thanks! I have an other question…Why ImageDimensions are not the same in Volumes module and in metadata? It seems that 3D slicer defaults to 512x512 for all the series.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7caf771c7cdd9c86cf6c74719d21c5b8cca8ad.png" data-download-href="/uploads/short-url/93DdvBDuGj2020qLLGOrOJTkFIN.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f7caf771c7cdd9c86cf6c74719d21c5b8cca8ad.png" alt="Untitled" data-base62-sha1="93DdvBDuGj2020qLLGOrOJTkFIN" width="690" height="274" data-dominant-color="EBEBEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">730×290 4.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2023-01-13 13:30 UTC)

<p>(0027,1060) and (0027,1061) are just some GE private fields. They are not needed for image reconstruction. Number of pixels in a slice are stored in standard fields (0028,0010) and (0028,0011).</p>

---

## Post #7 by @francesca_flore (2023-01-13 13:48 UTC)

<p>So if I have ImageDimension(0028,0010 and 0028,0011) of 512x512 and PixelSpacing (0028,0030) of 0.4688x0.4688, the real size of my image will be 240.0256 mm x 240.0256 mm. Correct?</p>

---

## Post #8 by @lassoan (2023-01-13 15:59 UTC)

<p>Yes, that’s correct.</p>

---
