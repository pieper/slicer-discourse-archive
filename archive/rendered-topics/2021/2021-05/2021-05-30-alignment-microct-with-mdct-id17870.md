# Alignment microCT with MDCT

**Topic ID**: 17870
**Date**: 2021-05-30
**URL**: https://discourse.slicer.org/t/alignment-microct-with-mdct/17870

---

## Post #1 by @sfglio (2021-05-30 21:30 UTC)

<p>I have a microCT scan of an implant which I would like to align as good as possible to the same implant in a MDCT scan.</p>
<p>My way: manual alignment (using transform) and then segmentation of each implant, export as labelmap and rigid registration using (fix/mov mask).</p>
<p>Is there any other way to register these modalities in a more convenient way as from my point of view the manual registration (green implant) in this context works better!</p>
<p>The attached Figure demonstrates that the additional rigid registration after manual alignment has no benefit and instead makes it worse again.<br>
Is there a way to be more accurate?</p>
<p>kind regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33fb37e8823c809b4bc1dc5ae28e887b581815a3.jpeg" data-download-href="/uploads/short-url/7pQAczaOs5PlvBL6ucuENnUnCg3.jpeg?dl=1" title="segmentierung" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33fb37e8823c809b4bc1dc5ae28e887b581815a3_2_690x476.jpeg" alt="segmentierung" data-base62-sha1="7pQAczaOs5PlvBL6ucuENnUnCg3" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33fb37e8823c809b4bc1dc5ae28e887b581815a3_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33fb37e8823c809b4bc1dc5ae28e887b581815a3_2_1035x714.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/33fb37e8823c809b4bc1dc5ae28e887b581815a3_2_1380x952.jpeg 2x" data-dominant-color="B3AEA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentierung</span><span class="informations">2120×1465 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-01 05:09 UTC)

<p>All the methods described <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here</a> could work.</p>
<p>Probably the image-based segmentation methods struggle because only the sample points taken very near to the implant surface will contribute to the accuracy. Therefore you would need to crop the moving volume tightly around the implant and use many training points (20-50% sampling rate).</p>
<p>Alternatively, you can run model registration on the implant segmented from both images.</p>
<p>If you don’t care about rotation around the long axis, then you can use Segment Statistics to get very accurate orientation of the implant’s long axis and the position along the axis.</p>

---
