---
topic_id: 10852
title: "Opening Nightly Saved Segmentation Files On Stable Version"
date: 2020-03-26
url: https://discourse.slicer.org/t/10852
---

# Opening nightly saved segmentation files on stable version

**Topic ID**: 10852
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/opening-nightly-saved-segmentation-files-on-stable-version/10852

---

## Post #1 by @Aep93 (2020-03-26 16:46 UTC)

<p>Hello all,<br>
I used the slicer nightly version and generated several seg.nrrd files. However, for some reason, I should use the stable version for now. The problem is that the stable version does not completely read the segmentation files I generated in the nightly version. Is there any solution for this?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-03-26 19:06 UTC)

<p>Slicer preserves backward compatibility (you can load old scenes on a new Slicer version). “Future compatibility” is not feasible because we don’t know what features will be implemented in the future and how.</p>
<p>We do not explicitly disable opening a scene created by a newer version of Slicer, but in general it should not expected to work (for example, not all data can be loaded).</p>

---

## Post #3 by @Aep93 (2020-03-26 19:53 UTC)

<p>Thank you very much for your response.</p>

---

## Post #4 by @brhoom (2020-06-14 14:56 UTC)

<p>I had a similar problem. I solved it by loading .seg file as volume then converted it to segmentation.</p>

---
