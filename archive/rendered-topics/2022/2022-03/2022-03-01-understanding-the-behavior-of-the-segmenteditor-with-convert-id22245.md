# Understanding the Behavior of the SegmentEditor with converted models

**Topic ID**: 22245
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/understanding-the-behavior-of-the-segmenteditor-with-converted-models/22245

---

## Post #1 by @Fluvio_Lobo (2022-03-01 19:05 UTC)

<p>Hello,</p>
<p>When applying a <strong>segmentation effect</strong> on <strong>surface models</strong> (converted into segments), the effect needs to be applied twice to get the desired result. For instance, below I try to apply a Gaussian filter to a tube model generated using markups-to-model module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c4c44bb9bca3c7ff627e0768a91ee80dea7d135.jpeg" data-download-href="/uploads/short-url/hJABRYM4M21yrAsCp5q7zWtqRi5.jpeg?dl=1" title="step1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c4c44bb9bca3c7ff627e0768a91ee80dea7d135_2_690x373.jpeg" alt="step1" data-base62-sha1="hJABRYM4M21yrAsCp5q7zWtqRi5" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c4c44bb9bca3c7ff627e0768a91ee80dea7d135_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c4c44bb9bca3c7ff627e0768a91ee80dea7d135_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c4c44bb9bca3c7ff627e0768a91ee80dea7d135_2_1380x746.jpeg 2x" data-dominant-color="74788A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step1</span><span class="informations">1920×1040 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I hit apply on the filter, then the tube becomes voxelated but not smooth.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef9bc37ebbb350011f5ef00f894dc7fa83a9f8bb.jpeg" data-download-href="/uploads/short-url/ybFPVrmXutubpVTilxW9GXYEba3.jpeg?dl=1" title="step2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef9bc37ebbb350011f5ef00f894dc7fa83a9f8bb_2_690x373.jpeg" alt="step2" data-base62-sha1="ybFPVrmXutubpVTilxW9GXYEba3" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef9bc37ebbb350011f5ef00f894dc7fa83a9f8bb_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef9bc37ebbb350011f5ef00f894dc7fa83a9f8bb_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef9bc37ebbb350011f5ef00f894dc7fa83a9f8bb_2_1380x746.jpeg 2x" data-dominant-color="74788A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step2</span><span class="informations">1920×1040 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I apply the filter again however, the filter seems to be applied correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8619606aa86120da62180928f3cd709f31ff24c4.jpeg" data-download-href="/uploads/short-url/j8ilIdKptN3PoQ3quICWe9DyBH6.jpeg?dl=1" title="step3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8619606aa86120da62180928f3cd709f31ff24c4_2_690x373.jpeg" alt="step3" data-base62-sha1="j8ilIdKptN3PoQ3quICWe9DyBH6" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8619606aa86120da62180928f3cd709f31ff24c4_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8619606aa86120da62180928f3cd709f31ff24c4_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8619606aa86120da62180928f3cd709f31ff24c4_2_1380x746.jpeg 2x" data-dominant-color="74788A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step3</span><span class="informations">1920×1040 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In code, I do this;</p>
<pre><code class="lang-auto">splintSegmentID = inputSegmentIDs.GetValue(0)
segmentEditorWidget.setCurrentSegmentID(splintSegmentID)
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "GAUSSIAN")
effect.setParameter("KernelSizeMm", 1)
#effect.setParameter("ApplyToAllVisibleSegments", str(1))
effect.self().onApply()

segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "GAUSSIAN")
effect.setParameter("KernelSizeMm", 1)
#effect.setParameter("ApplyToAllVisibleSegments", str(1))
effect.self().onApply()
</code></pre>
<p>What am I doing wrong and what is the appropriate way of applying effects on these models?</p>

---
