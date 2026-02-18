# Are there automatic segmentation models for musculoskeletal anatomy?

**Topic ID**: 37254
**Date**: 2024-07-04
**URL**: https://discourse.slicer.org/t/are-there-automatic-segmentation-models-for-musculoskeletal-anatomy/37254

---

## Post #1 by @Roshawnbrown (2024-07-04 12:28 UTC)

<p>Hello all,</p>
<p>Thank you introducing this. Are there any segmentations available for musculoskeletal anatomy? Specifically, I am looking for joints, tendons, ligaments, bursae, and cartilage.If not, are there any resources out there on how to create such segmentations?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2024-07-04 15:20 UTC)

<p>I’m not aware of any publicly available free models for segmenting joints, tendons, ligaments, bursae, or cartilage in 3D CT or MRI images. If you can segment these structures manually or semi-automatically on a few dozens to few hundreds of patients (the number depends on the difficulty of the segmentation task) then you can train your own AI model, for example by following <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg?tab=readme-ov-file#training-models">these instructions</a>.</p>

---

## Post #3 by @diazandr3s (2024-07-05 10:17 UTC)

<p>Hi <a class="mention" href="/u/roshawnbrown">@Roshawnbrown</a>,</p>
<p>I’m not aware of such dataset/model either <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"><br>
Can I ask which task or body region are you interested?</p>

---

## Post #4 by @Roshawnbrown (2024-07-05 13:13 UTC)

<p>I am looking specifically for knee anatomy. Accurate visual representations of the LCL, MCL,ACL etc… and the meniscus as well</p>

---

## Post #5 by @Roshawnbrown (2024-07-05 13:14 UTC)

<p>Much appreciated. Thank you for the directions</p>

---
