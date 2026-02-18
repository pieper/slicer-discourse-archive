# Brain Strip mask

**Topic ID**: 38560
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/brain-strip-mask/38560

---

## Post #1 by @BDhoth (2024-09-26 14:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2e481076ebd5ec88d981cac84249d1e1b4543d9.jpeg" data-download-href="/uploads/short-url/yEJ79NFmBXlqn1UrNejfpaSdpFf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e481076ebd5ec88d981cac84249d1e1b4543d9_2_461x500.jpeg" alt="image" data-base62-sha1="yEJ79NFmBXlqn1UrNejfpaSdpFf" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e481076ebd5ec88d981cac84249d1e1b4543d9_2_461x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2e481076ebd5ec88d981cac84249d1e1b4543d9_2_691x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2e481076ebd5ec88d981cac84249d1e1b4543d9.jpeg 2x" data-dominant-color="595955"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×843 88.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Brain strip mask still overlaying scan. Can I get this off to clearly visualize the scan better?</p>

---

## Post #2 by @lassoan (2024-09-27 12:19 UTC)

<p>Yes, sure. For example, you can go to <code>Segmentations</code> module and choose to show only the contours. If you are only interested in the brain then you can use <code>Mask volume</code> effect in <code>Segment Editor</code> module to blank out everything else (and then hide the segmentation).</p>

---

## Post #3 by @BDhoth (2024-10-03 16:55 UTC)

<p>I’m not really sure I follow your instructions. I am trying to view the vessels more clearly, but the mask from the HD brain extraction still overlays my image even though I have the source at top of the entire scan, not the stripped volume. Does that make sense?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d24bd59fd38705618faa5a11747039093471644.png" data-download-href="/uploads/short-url/dhZ7nOrwMwy4M0YXfjykbPfvM8Y.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d24bd59fd38705618faa5a11747039093471644_2_562x408.png" data-base62-sha1="dhZ7nOrwMwy4M0YXfjykbPfvM8Y" alt="image.png" width="562" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d24bd59fd38705618faa5a11747039093471644_2_562x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d24bd59fd38705618faa5a11747039093471644_2_843x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5d24bd59fd38705618faa5a11747039093471644_2_1124x816.png 2x" data-dominant-color="7E807E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">1256×912 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
