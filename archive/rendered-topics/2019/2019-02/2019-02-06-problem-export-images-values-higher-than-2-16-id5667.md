# Problem export images, values higher than 2^16

**Topic ID**: 5667
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/problem-export-images-values-higher-than-2-16/5667

---

## Post #1 by @nbarbosap (2019-02-06 20:53 UTC)

<p>Slicer version: 4.8.1</p>
<p>I’m registering a few SPECT/CT images using the common registration. Everything works relly well and the images seems to be as good as I expect !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70deeb891ec66d606bf1ba9f5e454e0394591ecf.png" data-download-href="/uploads/short-url/g6v50hrWtYa31ZCIOX5Eg931Kt9.png?dl=1" title="image%20(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_690x388.png" alt="image%20(1)" data-base62-sha1="g6v50hrWtYa31ZCIOX5Eg931Kt9" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70deeb891ec66d606bf1ba9f5e454e0394591ecf_2_1380x776.png 2x" data-dominant-color="949497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(1)</span><span class="informations">1920×1080 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My problem is when I try to “export” the DICOM file. My image  values are higher than 2^16, so, when I export the images, all the values higher than 2^16, appears with no value (an horrible black hole).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d282815440c96ddac7edc1d7a2e61b0723e2964.jpeg" data-download-href="/uploads/short-url/49VSFhu3tY9WHqnk2dCfeDMSsHq.jpeg?dl=1" title="image%20(2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_690x388.jpeg" alt="image%20(2)" data-base62-sha1="49VSFhu3tY9WHqnk2dCfeDMSsHq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d282815440c96ddac7edc1d7a2e61b0723e2964_2_1380x776.jpeg 2x" data-dominant-color="909093"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(2)</span><span class="informations">1920×1080 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I “export” the images without affect the maximum values??.. I need to use this images on another software to quantify the retained activity into the patient, so, It´is not viable rescale the pixel values to be lower than 2^16. I need the pixels values as they are.</p>

---

## Post #4 by @cpinter (2019-02-06 21:24 UTC)

<p>A post was merged into an existing topic: <a href="/t/export-dicom-spect-values-higher-than-2-16/5666">Export DICOM SPECT, values higher than 2^16</a></p>

---

## Post #5 by @cpinter (2019-02-06 21:24 UTC)



---
