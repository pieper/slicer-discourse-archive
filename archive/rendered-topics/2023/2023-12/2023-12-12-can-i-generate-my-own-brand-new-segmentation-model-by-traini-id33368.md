# Can I generate my own brand new segmentation model by training without loading the pre trained model?

**Topic ID**: 33368
**Date**: 2023-12-12
**URL**: https://discourse.slicer.org/t/can-i-generate-my-own-brand-new-segmentation-model-by-training-without-loading-the-pre-trained-model/33368

---

## Post #1 by @xiang_yao (2023-12-12 19:04 UTC)

<p>I would like to use MonAILabel to create a new model for segmenting the bone gray matter of vertebrae L1, L2, and L3. May I ask if I have modified the self labels in segmention.py{<br>
“Background”: 0,<br>
“SegmentionL1”: 1,<br>
“SegmentionL2”: 2,<br>
“SegmentionL3”: 3,<br>
}And if strtobool<br>
(self. conf. get (“use_pretrained_model”, “false”):,<br>
How to train without loading pre trained models and generate your own brand new segmentation model? In fact, after trying it out, I found that it did not work</p>

---
