---
topic_id: 3402
title: "Dce Analysis Ktrans Is Calculated Only In A Few Small Points"
date: 2018-07-06
url: https://discourse.slicer.org/t/3402
---

# DCE analysis - Ktrans is calculated only in a few small points

**Topic ID**: 3402
**Date**: 2018-07-06
**URL**: https://discourse.slicer.org/t/dce-analysis-ktrans-is-calculated-only-in-a-few-small-points/3402

---

## Post #1 by @Egor (2018-07-06 12:26 UTC)

<p>How to get Ktrans from DCE multivolume?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/431a5a51e058fa104e307bf8ddddd9b202165fd5.png" data-download-href="/uploads/short-url/9zCrYfPFKglAzX1uodbUlyIVCKx.png?dl=1" title="%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431a5a51e058fa104e307bf8ddddd9b202165fd5_2_690x369.png" alt="%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9" data-base62-sha1="9zCrYfPFKglAzX1uodbUlyIVCKx" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431a5a51e058fa104e307bf8ddddd9b202165fd5_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/431a5a51e058fa104e307bf8ddddd9b202165fd5_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/431a5a51e058fa104e307bf8ddddd9b202165fd5.png 2x" data-dominant-color="C5C0C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9</span><span class="informations">1366×732 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>At random ROI level Ktrans is calculated only in a single small points</p>

---

## Post #2 by @fedorov (2018-07-06 15:02 UTC)

<p>In general, you should not expect to fit model to an arbitrary signal, since you may not have contrast uptake, or you may have significant artifacts, or high noise. If you try to fit model to the noise, you cannot expect more than noise as the output!</p>
<p>Looking at your specific dataset, it seems that you have very few time points (just 6?), which probably is insufficient for PK analysis.</p>

---
