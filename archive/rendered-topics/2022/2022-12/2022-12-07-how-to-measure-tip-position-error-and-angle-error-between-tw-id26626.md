# How to measure tip position error and angle error between two needles in CT image?

**Topic ID**: 26626
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/how-to-measure-tip-position-error-and-angle-error-between-two-needles-in-ct-image/26626

---

## Post #1 by @Yitian_Xian (2022-12-07 12:35 UTC)

<p>Hello everyone, I am very new to 3D Slicer, and I found this software very amazing! Thank you to the development team!</p>
<p>Currently I am doing a project to compute the tip position error and angle error between two needles in the CT image. I am wondering if anyone can provide any help on this issue. Any suggestion is highly appreciated!</p>
<p>System: Windows 10<br>
Software version: 5.2.1</p>
<hr>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3cc17752b43ef1163e089953085bb59efaf8645.jpeg" data-download-href="/uploads/short-url/wvbEiY56vFR8NVmduIBYgMmVbDf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3cc17752b43ef1163e089953085bb59efaf8645_2_690x375.jpeg" alt="image" data-base62-sha1="wvbEiY56vFR8NVmduIBYgMmVbDf" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3cc17752b43ef1163e089953085bb59efaf8645_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3cc17752b43ef1163e089953085bb59efaf8645_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3cc17752b43ef1163e089953085bb59efaf8645_2_1380x750.jpeg 2x" data-dominant-color="33333A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1928×1048 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the reference data. As you can see, the needle is short and it is placed in the skull phantom.</p>
<hr>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77ff1b9431e9863ea71c065eebbe32afc6680db5.jpeg" data-download-href="/uploads/short-url/h7xnR4u5HyPF2lxJDUVLecBeqNf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ff1b9431e9863ea71c065eebbe32afc6680db5_2_690x375.jpeg" alt="image" data-base62-sha1="h7xnR4u5HyPF2lxJDUVLecBeqNf" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ff1b9431e9863ea71c065eebbe32afc6680db5_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ff1b9431e9863ea71c065eebbe32afc6680db5_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ff1b9431e9863ea71c065eebbe32afc6680db5_2_1380x750.jpeg 2x" data-dominant-color="32323A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1928×1048 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the second data (Maybe we can call it ‘test data’). As you can see, the needle is longer and it is also placed in the skull phantom.</p>
<hr>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97933041381cded7fc11e76c94d62b4b699c8acf.jpeg" data-download-href="/uploads/short-url/lCTrLRi2JkJsIRdtxdgxEdW4eKj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97933041381cded7fc11e76c94d62b4b699c8acf_2_690x375.jpeg" alt="image" data-base62-sha1="lCTrLRi2JkJsIRdtxdgxEdW4eKj" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97933041381cded7fc11e76c94d62b4b699c8acf_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97933041381cded7fc11e76c94d62b4b699c8acf_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97933041381cded7fc11e76c94d62b4b699c8acf_2_1380x750.jpeg 2x" data-dominant-color="36363B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1928×1048 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the image where I show them together. One thing I need to mention is that: the CT C-arm is fixed and just does a rotating scan, and the phantom is also fixed, therefore no registration is performed. This may make the problem simpler and more accurate, since registration error may happen. As you can see, some artifects exist because the needle is made from metal.</p>
<p>So with these images, I would like to know how I can compute the tip position error and angle error between two needles? The shorter one is regarded as the reference.</p>
<hr>
<p>Idea 1:</p>
<p>Do I need to do needle segmentation first? Then how the tip can be automatically detected and computed?</p>
<hr>
<p>Idea 2:</p>
<p>Maybe I can draw out the two line segments mannually, but this may reduce the accuracy.</p>
<hr>
<p>Does anyone have better idea? Thank you very much for your advice!</p>

---

## Post #2 by @lassoan (2022-12-08 02:57 UTC)

<aside class="quote no-group" data-username="Yitian_Xian" data-post="1" data-topic="26626">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/yitian_xian/48/15171_2.png" class="avatar"> Yitian_Xian:</div>
<blockquote>
<p>Do I need to do needle segmentation first? Then how the tip can be automatically detected and computed?</p>
</blockquote>
</aside>
<p>Manually specify a line markup that is aligned with needle takes less than one minute (one click near the tip in the 3D view, then click on the dropped point and adjust in slice views; then repeat this for another point along the needle shaft, as far as possible from the tip).</p>
<p>You could automate the process quite easily, as the needle has very high voxel value, a unique shape, and it is not connected to any other object. For example a fully automatic process could be the following: do thresholding, split islands to segments, then compute segment statistics; the needle will have relatively small volume and very elongated shape - there will be no other segments similar to it.However, since manual definition of the needle is so fast and simple, it might not worth the effort - only if you need to process thousands of cases or you use this intraoperatively and one minute is too long or you don’t have anyone in the operating room that could do the manual marking.</p>

---
