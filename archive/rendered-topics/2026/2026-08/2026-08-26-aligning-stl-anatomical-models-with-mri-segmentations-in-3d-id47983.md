---
topic_id: 47983
title: "Aligning STL anatomical models with MRI segmentations in 3D Slicer"
date: 2026-08-26
url: https://discourse.slicer.org/t/47983
last_bumped: 2026-08-27T14:11:01.725Z
---

# Aligning STL anatomical models with MRI segmentations in 3D Slicer

**Topic ID**: 47983
**Date**: 2026-08-26
**URL**: https://discourse.slicer.org/t/aligning-stl-anatomical-models-with-mri-segmentations-in-3d-slicer/47983

---

## Post #1 by @Toumia_Bessedik (2026-08-26 12:45 UTC)

<p>Hi,</p>
<p>I am working with an MRI of the head and I have existing STL models for several anatomical domains, including the <strong>skull, brain, soft tissue (ST), etc.</strong></p>
<p>I would like to use these STL models as references and align them with the corresponding anatomy in my MRI/segmentation in 3D Slicer.</p>
<p>The problem is that when I import the STL models, there is a <strong>spatial shift between the STL models and the MRI anatomy</strong>. I have tried using a <strong>rigid transform</strong> to align them, but I have not been able to get a correct alignment.</p>
<p>For example, I managed to get the <strong>brain</strong> relatively well aligned using a rigid transform, but when I try to apply the same transform to the other STL domains (skull, ST, etc.), they are still shifted and do not match the MRI.</p>
<p>I am not sure if I am doing something wrong with the transform, the coordinate systems, or the way the STL models are imported.</p>
<p>What would be the correct way to align these STL models with the MRI/segmentations in 3D Slicer?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @ebrahim (2026-08-26 12:50 UTC)

<p>Are the STL models derived from a segmentation of the very same MRI?</p>
<p>That is, should we expect the <em>same</em> transform that mapped the brain model into MRI space to also map the other models into MRI space?</p>
<p>If not – if the STL models are in different spaces from one another – then each would have to be transformed into place individually somehow. (There could be some more automated workflows for this depending on what you have and what you are doing.)</p>

---

## Post #3 by @Toumia_Bessedik (2026-08-26 13:50 UTC)

<p>Hi,</p>
<p>Thank you for your response.</p>
<p>Yes, all of the STL models come from the same MRI examination and were segmented in the same Mimics project. The models include the skull, soft tissue (ST), cartilage, etc., so they should all be in the same Mimics coordinate space.</p>
<p>I also discovered something that may be relevant regarding the coordinate system. The original STL files exported from Mimics do not contain <code>SPACE=RAS</code> or <code>SPACE=LPS</code> in their header. When I import them into 3D Slicer, Slicer therefore assumes LPS. I tested adding <code>SPACE=RAS</code> to one of the STL headers, but this resulted in a 180° rotation / flipped orientation, so RAS does not seem to be the correct interpretation for these Mimics STL files. With the original STL, the anatomical orientation is correct, but there is a spatial shift relative to the MRI.</p>
<p>For the rigid transform I previously calculated, I used a Brain segmentation obtained directly from the MRI in Slicer using an AI segmentation extension (<code>Brain_IRM</code>) as the reference. I then aligned the Brain STL to this MRI-derived brain segmentation.</p>
<p>The Brain could be aligned reasonably well, but when I apply the same transform to the other Mimics STL models (skull, ST, cartilage, etc.), they do not align correctly with the MRI.</p>
<p>Since all the original STL models come from the same Mimics project and the same MRI, I would expect them to share the same coordinate space.</p>
<p>In your opinion, what would be the correct way to align these Mimics STL models with my MRI in 3D Slicer? Should I be looking for a way to correctly convert the Mimics coordinate system into Slicer’s physical/world coordinate system first, rather than using a rigid registration based on the Brain?</p>
<p>Any advice on the appropriate workflow would be greatly appreciated.</p>
<p>Thank you!</p>

---

## Post #4 by @ebrahim (2026-08-27 13:36 UTC)

<aside class="quote no-group" data-username="Toumia_Bessedik" data-post="3" data-topic="47983">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/toumia_bessedik/48/82753_2.png" class="avatar"> Toumia_Bessedik:</div>
<blockquote>
<p>Should I be looking for a way to correctly convert the Mimics coordinate system into Slicer’s physical/world coordinate system first, rather than using a rigid registration based on the Brain?</p>
</blockquote>
</aside>
<p>That would be the ideal solution I think, and should be possible</p>
<p>Maybe someone more familiar with Mimics than I am can comment</p>
<p>Brains have left-right symmetry so it could be that the transform that rigidly aligned your STL-imported brain to the in-Slicer MRI segmentation is off by a left-right flip, then other things could be off by that flip. WHen you see the other STL models not aligning correctly with the MRI after applying the transform, in what way are they misaligned? Flipped around? Translated? Do they all appear to differ from correctness by potentially the same transform?</p>
<p>I think slicer shoudl assume <code>SPACE=RAS</code> if you don’t have anything like that in the STL header. If you put <code>SPACE=LPS</code> it will flip.</p>
<p>You can experiment with flips also inside slicer by creating a new linear transform and then setting some of the diagonal matrix entries to -1. For example if you set the first two entries along the diagonal to -1, that is an RAS-LPS flip. Transforms can be composed on top of each other, by applying a transform node to another transform node.</p>

---

## Post #5 by @Toumia_Bessedik (2026-08-27 14:11 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="4" data-topic="47983">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>That would be the ideal solution I think, and should be possible</p>
<p>Maybe someone more familiar with Mimics than I am can comment</p>
<p>Brains have left-right symmetry so it could be that the transform that rigidly aligned your STL-imported brain to the in-Slicer MRI segmentation is off by a left-right flip, then other things could be off by that flip. WHen you see the other STL models not aligning correctly with the MRI after applying the transform, in what way are they misaligned? Flipped around? Translated? Do they all appear to differ from correctness by potentially the same transform?</p>
<p>I think slicer shoudl assume <code>SPACE=RAS</code> if you don’t have anything like that in the STL header. If you put <code>SPACE=LPS</code> it will flip.</p>
<p>You can experiment with flips also inside slicer by creating a new linear transform and then setting some of the diagonal matrix entries to -1. For example if you set the first two entries along the diagonal to -1, that is an RAS-LPS flip. Transforms can be composed on top of each other, by applying a transform node to another transform node.</p>
</blockquote>
</aside>
<p>I observed the same type of misalignment across the different structures. They all seemed to have a similar spatial displacement, which looked more like a translation than a left-right flip.</p>
<p>However, I was finally able to resolve the issue using the FastModelAlign tool from SlicerMorph, which allowed me to correctly align the STL models with the MRI.</p>
<p>Thank you very much for your time and for your suggestions. They were really helpful in troubleshooting the issue.</p>

---
