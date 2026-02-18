# Problem with measuring tool

**Topic ID**: 41594
**Date**: 2025-02-09
**URL**: https://discourse.slicer.org/t/problem-with-measuring-tool/41594

---

## Post #1 by @Bernard_Victor (2025-02-09 22:46 UTC)

<p>Operating system: MacOS 15.3<br>
Slicer version: 5.8.0</p>
<p>Hello again,</p>
<p>The measuring tool gives me 192 mm when it should be 10 mm (on the right of my screen shot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8c100d8af83403bcd3131c63226944020b070a4.png" data-download-href="/uploads/short-url/sDX06N20Zcv3ccdIMs0eu5CiUgQ.png?dl=1" title="Capture d’écran 2025-02-09 à 22.39.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c100d8af83403bcd3131c63226944020b070a4_2_690x443.png" alt="Capture d’écran 2025-02-09 à 22.39.08" data-base62-sha1="sDX06N20Zcv3ccdIMs0eu5CiUgQ" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c100d8af83403bcd3131c63226944020b070a4_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c100d8af83403bcd3131c63226944020b070a4_2_1035x664.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8c100d8af83403bcd3131c63226944020b070a4.png 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2025-02-09 à 22.39.08</span><span class="informations">1052×676 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For the record, Horos gives me the same 192 size in pixels, but the correct dimension (10 mm)</p>
<p>I suspect it is because I cannot charge it as a DICOM file. I have to charge it as a non-DICOM volume file, otherwise Slicer makes flat annotations that do not stick to particular frame (I can browe the US sequence in the upder slider but I cannot use the slider where my sequence is displayed as if there were only one frame).</p>
<p>Even though my files look like this in my file browser:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/770775ab70afdc1c10f3424e08ddd943e7136e3e.png" data-download-href="/uploads/short-url/gYYNFPjYjfk81cDaxWlYzqBOiQu.png?dl=1" title="Capture d’écran 2025-02-09 à 22.53.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/770775ab70afdc1c10f3424e08ddd943e7136e3e.png" alt="Capture d’écran 2025-02-09 à 22.53.45" data-base62-sha1="gYYNFPjYjfk81cDaxWlYzqBOiQu" width="408" height="218"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2025-02-09 à 22.53.45</span><span class="informations">408×218 43.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The file browser says it is ‘executable Unix file’</p>
<p>The images were exported from a GE Logic e10.</p>
<p>Is there a way to get back proper measurment, or should I find a way to extract the date another way?</p>
<p>Thank you very much</p>
<p>Bernard</p>

---

## Post #2 by @lassoan (2025-02-09 23:08 UTC)

<p>Ultrasound images are often saved as secondary capture (screenshot). Readers may ignore the physical spacing in such images. This has not been an issue for decades, because most analysis in ultrasound images were done in the ultrasound cart or using the vendor’s software. Now that people want to use these images for AI training, there are a number of issues to solve. Image spacing is just one of them. You’ll also have to deal with having several frame sets under one series, some information present only in the first frameset of thr series, annotations (patient information, measurements, etc) burnt into the image.</p>
<p>The Ultrasound extension of Slicer has a module for dealinf with most of these issues. I would recommend to use that for preparing your images for AI training.</p>

---

## Post #3 by @Bernard_Victor (2025-02-11 11:55 UTC)

<p>Thanky you so much Andras for your kind help. I’ve installed it but I have have trouble using it even after reading the complete readme about the ‘timeseries’ extension ( <a href="https://github.com/SlicerUltrasound/SlicerUltrasound/tree/main/TimeSeriesAnnotation" rel="noopener nofollow ugc">https://github.com/SlicerUltrasound/SlicerUltrasound/tree/main/TimeSeriesAnnotation</a> ).<br>
In this doc, it is said that the first step is to set up segmentation and segmentation browser nodes. Does that refer to something outisde the ‘times series analysis’ modules? I suspect I need further basic training in 3dSlicer.<br>
For further assistance for this specific question, if I may, should I ask here or ask on of the developper of the module, or maybe look for commercial help?</p>
<p>Thank you very much for your kind help</p>
<p>Bernard</p>

---
