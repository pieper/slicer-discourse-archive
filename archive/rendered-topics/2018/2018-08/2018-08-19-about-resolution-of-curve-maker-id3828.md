# About resolution of curve maker

**Topic ID**: 3828
**Date**: 2018-08-19
**URL**: https://discourse.slicer.org/t/about-resolution-of-curve-maker/3828

---

## Post #1 by @timeanddoctor (2018-08-19 06:21 UTC)

<p>What I am doing is to get a higher resolution of curve maker, and I changed the code in python just like the picture showing. But there is nothing happen in slicer.<br>
Thanks.<br>
Li zhenzhu.<br>
Binzhou Medical University Hospital.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e69d61a43dea3332043466d213bb93fd5905afe.jpeg" data-download-href="/uploads/short-url/fKLh3k6VN1JUGMqC3PsU40xzXNY.jpeg?dl=1" title="2018-08-19_141001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e69d61a43dea3332043466d213bb93fd5905afe_2_690x123.jpeg" alt="2018-08-19_141001" data-base62-sha1="fKLh3k6VN1JUGMqC3PsU40xzXNY" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6e69d61a43dea3332043466d213bb93fd5905afe_2_690x123.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e69d61a43dea3332043466d213bb93fd5905afe.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e69d61a43dea3332043466d213bb93fd5905afe.jpeg 2x" data-dominant-color="F3EDED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2018-08-19_141001</span><span class="informations">1003×179 80.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> ![2018-08-19_141839|690x248]</p>

---

## Post #2 by @lassoan (2018-08-19 10:18 UTC)

<p>I would recommend to use MarkupsToModel extension instead. It offers the same features (actually, much more) and implemented in a way, that closely follows Slicer conventions. In contrast to CurveMaker, with MarkupsToModel, you can configure all options in MRML nodes, you can save the scene and reload without loss of information, you can have any number of curves, etc.</p>

---
