# Segmentation (.seg.nrrd) merges labels instead of one-layer-per-label representation

**Topic ID**: 30792
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/segmentation-seg-nrrd-merges-labels-instead-of-one-layer-per-label-representation/30792

---

## Post #1 by @mangotee (2023-07-25 22:49 UTC)

<p>Hi,<br>
I have noticed that the array in the saved segmentation file (.seg.nrrd) is not really one-layer-per-label. Instead, non-overlapping labels are merged into one layer, while overlapping layers are kept separately.<br>
I find this quite clever, but for convenient echange with deep learning (specifically MONAI Label), I would like to store it as a one-layer-per-label representation with exactly the same voxel grid size as the source image volume. The latter seems to be the default behaviour in the latest Slicer versions, but I couldn’t find a discussion on “one-layer-per-label” (perhaps I don’t know the right search term).<br>
Btw, I know that MONAI Label allows overlapping labels in principle… but I am playing around with a 2D radiology app right now, and I need to manually change the storage behaviour of .seg.nrrd files. Would be great if there was a global flag (e.g. in Application Settings) that could switch that on.<br>
I also contacted the authors of the MONAILabelReviewer module, who contributed overlapping-labels support in MONAI Label, but they also didn’t know how to avoid the layer-collapsing behaviour in .seg.nrrd.<br>
Thanks for your advice in advance!</p>

---

## Post #2 by @pieper (2023-07-27 16:25 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="1" data-topic="30792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>The latter seems to be the default behaviour in the latest Slicer versions</p>
</blockquote>
</aside>
<p>Maybe you can just standardize on the newer version?  There will be a new 5.4 release before too long that will be essentially the current preview version with a few tweaks.</p>

---
