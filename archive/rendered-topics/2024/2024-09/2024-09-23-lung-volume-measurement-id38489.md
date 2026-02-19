---
topic_id: 38489
title: "Lung Volume Measurement"
date: 2024-09-23
url: https://discourse.slicer.org/t/38489
---

# Lung volume measurement

**Topic ID**: 38489
**Date**: 2024-09-23
**URL**: https://discourse.slicer.org/t/lung-volume-measurement/38489

---

## Post #1 by @Arash1 (2024-09-23 01:09 UTC)

<p>Hello<br>
I wanted to use the LungCTAnalyzer for lung volume measurement.<br>
I followed the instructions provided on Github, but when I reviewed the results, the lung volume, and a few other values seemed wrong.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/007f46b15fa308d02e08650f76962581fccac350.png" data-download-href="/uploads/short-url/4oGEdhs8Nm8zsUgbHnzWDIVX1e.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/007f46b15fa308d02e08650f76962581fccac350_2_690x182.png" alt="image" data-base62-sha1="4oGEdhs8Nm8zsUgbHnzWDIVX1e" width="690" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/007f46b15fa308d02e08650f76962581fccac350_2_690x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/007f46b15fa308d02e08650f76962581fccac350.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/007f46b15fa308d02e08650f76962581fccac350.png 2x" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×260 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the Log:</p>
<ol>
<li>[WARNING][VTK] 22.09.2024 16:24:48 [vtkMRMLMarkupsFiducialNode (000002329D09EFB0)] (vtkMRMLMarkupsFiducialNode.h:119) - vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead</li>
<li>Generic Warning: In vtkSlicerMarkupsToModelClosedSurfaceGeneration.cxx, line 311<br>
Extent ranges not provided in order largest to smallest. Unexpected results may occur.</li>
<li>[WARNING][VTK] 22.09.2024 16:21:20 [vtkOpenGLVolumeOpacityTable (0000023335C918B0)] (vtkOpenGLVolumeLookupTable.cxx:88) - This OpenGL implementation does not support the required texture size of 65536, falling back to maximum allowed, 16384.This may cause an incorrect lookup table mapping.</li>
</ol>
<p>The problem, I guess, is similar to what one of the other researchers had before <a href="https://discourse.slicer.org/t/lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006/30" class="inline-onebox">LungCTAnalyzer extension for lung CT segmentation and analysis for COVID-19 assessment - #30 by mahmoud</a>.</p>
<p>On the demo model, everything works perfectly. Is this potentially because of the resampling?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2024-09-23 01:27 UTC)

<p>All these warnings are harmless. Are you suspicious of the results because the lung volume seems too small? Have you loaded the image from DICOM or some 2D file format such as tiff or png?</p>

---

## Post #3 by @Arash1 (2024-09-23 01:29 UTC)

<p>Hello<br>
Thank you very much for your reply.<br>
It is a DICOM.</p>

---

## Post #4 by @lassoan (2024-09-23 01:36 UTC)

<p>If it is from a clinical DICOM scanner then the image geometry (most importantly, the image spacing) is correct, too, and therefore the volume measurment is accurate, too.</p>
<p>The automatic segmentation is very robust, too, but you always need to verify visually. Does the segmentation looks correct? The full lung is segmented, there are no missing parts or holes?</p>
<p>You may also post a few screenshots, they may help explaining why you get different results than what you expect.</p>

---

## Post #5 by @Arash1 (2024-09-25 20:32 UTC)

<p>I will use the sample data to demonstrate the steps to begin the process.</p>
<p>CTChest<br>
1.1 Scene: CTChest</p>
<ol start="2">
<li>
<p>Lung Segmentation: Chest Imaging Platform (CIP)<br>
2.1. Lung CT Segmenter<br>
2.1.1. Parameters:<br>
2.1.1.1. High Detail, Airway Segmentation Checked, NO AI<br>
2.1.2. Seed Placement<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d801901afc206fdf8fe95d8002cf9ff958d84716.jpeg" data-download-href="/uploads/short-url/uOStTlsuNbGNJo7Zkd1SQfTHnv0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d801901afc206fdf8fe95d8002cf9ff958d84716_2_344x249.jpeg" alt="image" data-base62-sha1="uOStTlsuNbGNJo7Zkd1SQfTHnv0" width="344" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d801901afc206fdf8fe95d8002cf9ff958d84716_2_344x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d801901afc206fdf8fe95d8002cf9ff958d84716_2_516x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d801901afc206fdf8fe95d8002cf9ff958d84716_2_688x498.jpeg 2x" data-dominant-color="4A4B47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×807 74.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2.1.3. Segment Validation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0b0a8ad60bdd8728979168c155597daf5e261d8.jpeg" data-download-href="/uploads/short-url/tM9NPM1tIJnN9THlJuGnEqZ1H0A.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0b0a8ad60bdd8728979168c155597daf5e261d8_2_344x249.jpeg" alt="image" data-base62-sha1="tM9NPM1tIJnN9THlJuGnEqZ1H0A" width="344" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0b0a8ad60bdd8728979168c155597daf5e261d8_2_344x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0b0a8ad60bdd8728979168c155597daf5e261d8_2_516x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0b0a8ad60bdd8728979168c155597daf5e261d8_2_688x498.jpeg 2x" data-dominant-color="83847D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×807 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2.1.4. 3D Preview<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df649f71bbe3d13c22b8873321e183db02ef3272.jpeg" data-download-href="/uploads/short-url/vSe3G3nWdEspUr0X2ieuAKHoQTw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df649f71bbe3d13c22b8873321e183db02ef3272_2_344x249.jpeg" alt="image" data-base62-sha1="vSe3G3nWdEspUr0X2ieuAKHoQTw" width="344" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df649f71bbe3d13c22b8873321e183db02ef3272_2_344x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df649f71bbe3d13c22b8873321e183db02ef3272_2_516x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df649f71bbe3d13c22b8873321e183db02ef3272_2_688x498.jpeg 2x" data-dominant-color="CFD4C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×807 67.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
2.1.5. Finalising<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da39df22e6db460e3c9edb8abbe60f31b207c742.jpeg" data-download-href="/uploads/short-url/v8w4PCzPgqmIhtPXPO2qDI9uzZg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da39df22e6db460e3c9edb8abbe60f31b207c742_2_344x249.jpeg" alt="image" data-base62-sha1="v8w4PCzPgqmIhtPXPO2qDI9uzZg" width="344" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da39df22e6db460e3c9edb8abbe60f31b207c742_2_344x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da39df22e6db460e3c9edb8abbe60f31b207c742_2_516x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da39df22e6db460e3c9edb8abbe60f31b207c742_2_688x498.jpeg 2x" data-dominant-color="DCDFD5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×807 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>CIP, Lung CT Analyzer<br>
3.1. Parameters: Density Statistics Checked<br>
3.2. Compute Results<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf4a408bf88548f26c1b08f6cc97996493b35f52.jpeg" data-download-href="/uploads/short-url/riehrp98UtBoAQaHa8BtqpDEN22.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf4a408bf88548f26c1b08f6cc97996493b35f52_2_516x374.jpeg" alt="image" data-base62-sha1="riehrp98UtBoAQaHa8BtqpDEN22" width="516" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf4a408bf88548f26c1b08f6cc97996493b35f52_2_516x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf4a408bf88548f26c1b08f6cc97996493b35f52_2_774x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf4a408bf88548f26c1b08f6cc97996493b35f52_2_1032x748.jpeg 2x" data-dominant-color="3F4751"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×807 48.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
3.3. Results<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0afba8bfac426aaa8b91a21dbbb4ad7d9407f50d.png" data-download-href="/uploads/short-url/1z9X1uaeaVq0TgZZxfHX3gXv3oV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0afba8bfac426aaa8b91a21dbbb4ad7d9407f50d_2_535x500.png" alt="image" data-base62-sha1="1z9X1uaeaVq0TgZZxfHX3gXv3oV" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0afba8bfac426aaa8b91a21dbbb4ad7d9407f50d_2_535x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0afba8bfac426aaa8b91a21dbbb4ad7d9407f50d_2_802x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0afba8bfac426aaa8b91a21dbbb4ad7d9407f50d.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">890×831 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8beb8133e304cd20c45221e8d8bc7b640011b0e7.png" data-download-href="/uploads/short-url/jXMVXGgSyaPdG0zhzV6bpT3FKXt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8beb8133e304cd20c45221e8d8bc7b640011b0e7_2_650x500.png" alt="image" data-base62-sha1="jXMVXGgSyaPdG0zhzV6bpT3FKXt" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8beb8133e304cd20c45221e8d8bc7b640011b0e7_2_650x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8beb8133e304cd20c45221e8d8bc7b640011b0e7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8beb8133e304cd20c45221e8d8bc7b640011b0e7.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×677 76.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2e47264b4925d0f558763fe9530a46954fb6ae.png" data-download-href="/uploads/short-url/dijyotJTg0L5OhWagQS0ccGXpVQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2e47264b4925d0f558763fe9530a46954fb6ae.png" alt="image" data-base62-sha1="dijyotJTg0L5OhWagQS0ccGXpVQ" width="690" height="280" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">893×363 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>
<p>Compare with Segment Statistics (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html#segment-statistics" class="inline-onebox" rel="noopener nofollow ugc">Segment statistics — 3D Slicer documentation</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3c1636820429c07065720358bfff76a6043997.png" data-download-href="/uploads/short-url/fruiJl8I1XnowPVCkjhc54W9t8r.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3c1636820429c07065720358bfff76a6043997.png" alt="image" data-base62-sha1="fruiJl8I1XnowPVCkjhc54W9t8r" width="690" height="63" data-dominant-color="EBEBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1384×127 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Also, as a user suggestion, it would have been beneficial to add an export option for this module (CSV, PDF, etc.)</p>
</li>
<li>
<p>Repeating the Step With Research Data<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b572eab18ca1a7d5f17728a26316a3af73e65514.jpeg" data-download-href="/uploads/short-url/pTaD4u5X9cJHDaHzHGLlVOj85iQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b572eab18ca1a7d5f17728a26316a3af73e65514_2_345x204.jpeg" alt="image" data-base62-sha1="pTaD4u5X9cJHDaHzHGLlVOj85iQ" width="345" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b572eab18ca1a7d5f17728a26316a3af73e65514_2_345x204.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b572eab18ca1a7d5f17728a26316a3af73e65514_2_517x306.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b572eab18ca1a7d5f17728a26316a3af73e65514_2_690x408.jpeg 2x" data-dominant-color="B3B4AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×807 45.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
5.1. Additional Step: Local Threshold (IF Required)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83dc856527a0aa0acca86af20e5b0e52e770d84.jpeg" alt="image" data-base62-sha1="x8v8MDerYQTQChmu18Pq9V3Irha" width="339" height="193"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d29c0553608c4448621a757493004b0bcd71323.png" data-download-href="/uploads/short-url/1SrEQFJWPdghFP3IT5d3VRVx41J.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d29c0553608c4448621a757493004b0bcd71323_2_690x224.png" alt="image" data-base62-sha1="1SrEQFJWPdghFP3IT5d3VRVx41J" width="690" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d29c0553608c4448621a757493004b0bcd71323_2_690x224.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d29c0553608c4448621a757493004b0bcd71323_2_1035x336.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d29c0553608c4448621a757493004b0bcd71323_2_1380x448.png 2x" data-dominant-color="EEECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1474×480 54.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d2be0d19c2486544bbcf8b1b021943ef7623946.png" data-download-href="/uploads/short-url/1SwdneFG4NK6wbb6RaTqsRAQoom.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d2be0d19c2486544bbcf8b1b021943ef7623946.png" alt="image" data-base62-sha1="1SwdneFG4NK6wbb6RaTqsRAQoom" width="690" height="54" data-dominant-color="EEEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1256×100 7.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>

---

## Post #6 by @lassoan (2024-09-25 22:41 UTC)

<p>CTChest: right and left lungs are about 3223 and 3116 cm3. All the numbers in your post above (3223≈3228≈3238 cm3 and 3116≈3122≈3131 cm3) are consistent with this.</p>
<p>Your “research data”: the numbers look consistent, too (1589≈1596 cm3, 1276≈1283 cm3).</p>
<p>Are concerned about the 5-15cm3 volume difference? That is due to small differences in how much of the airways and vessels are included. Since this corresponds to &lt;1% of the volume, this should be negligible.</p>
<p>In summary, everything looks good.</p>

---

## Post #7 by @Arash1 (2024-09-25 22:48 UTC)

<p>The problem is the volume. With my research data, the lung volume is not correct.</p>

---
