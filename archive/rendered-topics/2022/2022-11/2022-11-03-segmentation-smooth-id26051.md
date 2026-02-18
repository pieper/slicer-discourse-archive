# Segmentation smooth

**Topic ID**: 26051
**Date**: 2022-11-03
**URL**: https://discourse.slicer.org/t/segmentation-smooth/26051

---

## Post #1 by @qod_rec (2022-11-03 12:37 UTC)

<p>Hello! I have a dataset of chest CTs. Here is what I see when I open them with 3d slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7259b85322707606ee57e196f3d1b9bdf72f23.jpeg" data-download-href="/uploads/short-url/dCmlYtva6qzqk81sGatj9Wvjigz.jpeg?dl=1" title="ask1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f7259b85322707606ee57e196f3d1b9bdf72f23_2_690x488.jpeg" alt="ask1.PNG" data-base62-sha1="dCmlYtva6qzqk81sGatj9Wvjigz" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f7259b85322707606ee57e196f3d1b9bdf72f23_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f7259b85322707606ee57e196f3d1b9bdf72f23_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f7259b85322707606ee57e196f3d1b9bdf72f23.jpeg 2x" data-dominant-color="59595E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ask1.PNG</span><span class="informations">1310×927 83.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This segmentation has some sawtoothes both in the label map and the mesh.<br>
I want to get smooth contour and I saw some videos use the ‘Gaussian smooth’ in ‘Segment Editor’.<br>
Is this a nice way to maintain the segmentations’ information? Since they are made by radiologists.<br>
Also the ‘Gaussian smooth’ has the ‘standard deviation’ option. How should I set this in a reasonable way? How many milimeter should I choose?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e79291925d8f82f8fe062d9f54cf941aa4d96c53.png" alt="ask2" data-base62-sha1="x2AjGBGidsLmsJGYUhVgQKLUqqL" width="513" height="183"></p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-12-01 08:00 UTC)

<p>The segmentation’s resolution looks very coarse. I don’t think you can get a very accurate segmentation out of this, but if you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">increase the resolution of the segmentation</a> before applying smoothing then you might get better results.</p>
<p>However, I’m not sure if this is worth it, as you can get much higher quality segmentations using <a href="https://github.com/rbumm/SlicerLungCTAnalyzer">LungCTAnalyzer extension</a> or <a href="https://github.com/lassoan/SlicerTotalSegmentator">TotalSegmentator extension</a> - fully automatically, in a few minutes, including splitting the lung to lobes (and also segmenting 100 other structures).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e49b51e9ed2f5075d5083cef185983aa5ee6a47.jpeg" data-download-href="/uploads/short-url/6BtSDrgGV4dLj4goZNDIep8yHwb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e49b51e9ed2f5075d5083cef185983aa5ee6a47_2_690x378.jpeg" alt="image" data-base62-sha1="6BtSDrgGV4dLj4goZNDIep8yHwb" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e49b51e9ed2f5075d5083cef185983aa5ee6a47_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e49b51e9ed2f5075d5083cef185983aa5ee6a47_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e49b51e9ed2f5075d5083cef185983aa5ee6a47_2_1380x756.jpeg 2x" data-dominant-color="A4A49F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1054 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
