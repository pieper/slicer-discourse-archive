---
topic_id: 6436
title: "Importing A Segmentation"
date: 2019-04-08
url: https://discourse.slicer.org/t/6436
---

# Importing a segmentation

**Topic ID**: 6436
**Date**: 2019-04-08
**URL**: https://discourse.slicer.org/t/importing-a-segmentation/6436

---

## Post #1 by @LizzyMedinaGtz (2019-04-08 17:00 UTC)

<p>My partner and I are working on the same DICOM file, I’d like to know if I can import my segmentation into the file that my partner its working on.<br>
I already tried with the data icon and it loads my .obj file but I cannot fit it to the CT my partner is working on 3d slicer, It loads in an 180º angle than I wish it to be.</p>
<p>We would like to work quicker because right now we can only work on it 1 person at the time</p>

---

## Post #2 by @lassoan (2019-04-08 18:18 UTC)

<aside class="quote no-group" data-username="LizzyMedinaGtz" data-post="1" data-topic="6436">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lizzymedinagtz/48/3398_2.png" class="avatar"> LizzyMedinaGtz:</div>
<blockquote>
<p>if I can import my segmentation into the file that my partner its working on.</p>
</blockquote>
</aside>
<p>Yes, you can. Instead of exporting to surface mesh file (which is a lossy operation), save the scene. In menu: choose File/Save, and click Save. If you only want to save the segmentation, then check the checkbox only in the row of the segmentation .seg.nrrd file (uncheck all the other rows).</p>
<aside class="quote no-group" data-username="LizzyMedinaGtz" data-post="1" data-topic="6436">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lizzymedinagtz/48/3398_2.png" class="avatar"> LizzyMedinaGtz:</div>
<blockquote>
<p>I already tried with the data icon and it loads my .obj file but I cannot fit it to the CT my partner is working on 3d slicer, It loads in an 180º angle than I wish it to be.</p>
</blockquote>
</aside>
<p>The 180deg rotation is because exporting to model is done in LPS coordinate system by default and when you import a mode then Slicer assumes RAS. You could rotate the imported model or export as RAS to avoid this, but as I wrote above, you should use scene save instead.</p>

---

## Post #3 by @lassoan (2019-05-23 03:32 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-edit-an-imported-segmentation/6890">How to edit an imported segmentation?</a></p>

---
