---
topic_id: 46587
title: "Diffusion Tensor Estimation From A Manually Segmented Brain"
date: 2026-03-26
url: https://discourse.slicer.org/t/46587
---

# Diffusion tensor estimation from a manually segmented brain mask

**Topic ID**: 46587
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/diffusion-tensor-estimation-from-a-manually-segmented-brain-mask/46587

---

## Post #1 by @Anna_98 (2026-03-26 19:02 UTC)

<p>Hey There,</p>
<p>I tried to do get an “output DTI volume” with a manually segmented brain mask, but it didn’t work.</p>
<p>My workflow (using Version 5.6.2):</p>
<p>Generated a automatic brain mask &gt; convert lablemap to segmentation node &gt; used the DWI volume as the source &gt;  edited the the brain mask via segmentation &gt; exported lablemap as binary lablemap &gt; diffusion tensor estimation to create a new output DTI volume … what I see now is a  frozen  slice of the manual brain mask</p>
<p>When I create a  DTI Volume with the automatically brain mask it is all working.</p>
<p>I would be super thankful for help <img src="https://emoji.discourse-cdn.com/twitter/folded_hands/3.png?v=15" title=":folded_hands:t3:" class="emoji" alt=":folded_hands:t3:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2026-03-26 19:20 UTC)

<aside class="quote no-group" data-username="Anna_98" data-post="1" data-topic="46587">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ec9cab/48.png" class="avatar"> Anna_98:</div>
<blockquote>
<p>what I see now is a frozen slice of the manual brain mask</p>
</blockquote>
</aside>
<p>Not sure what you mean by this one.</p>
<p>In any case, I suggest you estimate the tensors from the DWI, then calculate the FA from the tensors and then apply the mask to the FA scalar volume.</p>
<p>Also 5.6.2 is pretty old. SlicerDMRI may not have changed much since then but we generally suggest always using a recent supported version (you can have more than one version on your machine at the same time).</p>

---
