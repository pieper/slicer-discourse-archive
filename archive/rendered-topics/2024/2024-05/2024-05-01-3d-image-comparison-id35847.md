# 3D image comparison

**Topic ID**: 35847
**Date**: 2024-05-01
**URL**: https://discourse.slicer.org/t/3d-image-comparison/35847

---

## Post #1 by @Miri_Trope (2024-05-01 08:48 UTC)

<p>Hi, sorry if this question has been asked frequently, but I’ve been unable to find a satisfactory answer. Here’s my question: I have two 3D MRI images from different years for the same patient, and I want to assess whether there has been any improvement in the patient’s condition over time. I prefer comparing the axial views of both images. This means I want to display two axial (red) windows side by side, one from year A and the other from year B. I’d like to manually adjust the slices in each image for comparison without having the slices’ locations automatically adjusted. How can I accomplish this?</p>

---

## Post #2 by @muratmaga (2024-05-01 15:27 UTC)

<p>Well you can choose axial view in the <strong>yellow</strong> viewer for your other dataset, and you should be set.</p>
<p>You can actually do better than that. Given that there is probably some slight positional difference between two scans, having them side by side may not be enough for comparison. You can use Elastix (or Brains) registration and rigidly register one scan to the other to put them in exactly the same space.</p>
<p>You can then link the views between your two viewer, or even load both volumes in the same axial view as foreground and background volume and use the alpha (opacity) channel to go between them.</p>

---

## Post #3 by @Miri_Trope (2024-05-01 18:19 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="35847">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Well you can choose axial view in the <strong>yellow</strong> viewer for your other dataset, and you should be set.</p>
</blockquote>
</aside>
<p>Thanks! Your first recommendation works.</p>

---
