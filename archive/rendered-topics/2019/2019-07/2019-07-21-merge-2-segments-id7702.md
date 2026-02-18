# Merge 2 segments

**Topic ID**: 7702
**Date**: 2019-07-21
**URL**: https://discourse.slicer.org/t/merge-2-segments/7702

---

## Post #1 by @Jmarcs (2019-07-21 15:46 UTC)

<p>I msorry about my ridiculous request but how can I merge 2 segments in ONE segment<br>
best regards<br>
jean-marc<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caf527f1a72fbf5e68a7f24508f2a6145fbbe6a6.jpeg" data-download-href="/uploads/short-url/sXrGZrNPXO634L9th1u7AZSa3Yy.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/caf527f1a72fbf5e68a7f24508f2a6145fbbe6a6_2_690x281.jpeg" alt="PNG" data-base62-sha1="sXrGZrNPXO634L9th1u7AZSa3Yy" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/caf527f1a72fbf5e68a7f24508f2a6145fbbe6a6_2_690x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/caf527f1a72fbf5e68a7f24508f2a6145fbbe6a6_2_1035x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/caf527f1a72fbf5e68a7f24508f2a6145fbbe6a6_2_1380x562.jpeg 2x" data-dominant-color="8F8686"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1801×735 463 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2019-07-21 19:30 UTC)

<p>You can use the Logical operators effect in Segment Editor. Let me know if you have further questions!</p>

---

## Post #3 by @muratmaga (2019-07-21 19:40 UTC)

<p>You can use logical effects and the choose the add segments option.</p>

---

## Post #4 by @soukup.la (2023-01-18 09:43 UTC)

<p>Hello,<br>
is it possible using Python interactor please? Or, is it possible to merge two models using Python interactor please?</p>
<p>thank you very much!</p>

---

## Post #5 by @rbumm (2023-01-19 12:11 UTC)

<p>Yes, you can add the segments in Python by calling functions of the SegmentEditorWidget, see an <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/eca5aa39b7bd519954f3f1869de4d9210d582a69/LungCTSegmenter/LungCTSegmenter.py#L1535">example here</a>.</p>

---
