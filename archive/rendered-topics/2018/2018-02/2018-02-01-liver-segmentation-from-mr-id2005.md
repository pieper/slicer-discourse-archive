# Liver Segmentation from MR

**Topic ID**: 2005
**Date**: 2018-02-01
**URL**: https://discourse.slicer.org/t/liver-segmentation-from-mr/2005

---

## Post #1 by @Giovanny.Casadiego (2018-02-01 21:47 UTC)

<p>Hi everyone, I have been trying to segment this liver tumor with the vasculature but so far no success.<br>
Any ideas?</p>
<p>Thanks,<br>
G</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c21857d30ebecc246b069a14071ed82aebb75c7.jpeg" data-download-href="/uploads/short-url/6ioPl3a6u7FOQCMgrYbRPW8IN3F.jpg?dl=1" title="LiverMR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c21857d30ebecc246b069a14071ed82aebb75c7_2_690x414.jpg" alt="LiverMR" data-base62-sha1="6ioPl3a6u7FOQCMgrYbRPW8IN3F" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c21857d30ebecc246b069a14071ed82aebb75c7_2_690x414.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c21857d30ebecc246b069a14071ed82aebb75c7_2_1035x621.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c21857d30ebecc246b069a14071ed82aebb75c7_2_1380x828.jpg 2x" data-dominant-color="9B99A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LiverMR</span><span class="informations">1680×1008 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-02-02 05:28 UTC)

<p>Try Segment editor module in latest stable version (Slicer-4.8.1). Probably Grow from seeds effect will work well. You can learn how to use it from this tutorial:</p>
<div class="lazyYT" data-youtube-id="BJoIexIvtGo" data-youtube-title="Whole heart segmentation from cardiac CT in 10 minutes" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>There are some more segmentation tutorials here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---
