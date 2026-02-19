---
topic_id: 24974
title: "Question Regarding Converting A Model Back To A Segmentation"
date: 2022-08-29
url: https://discourse.slicer.org/t/24974
---

# Question regarding converting a model back to a segmentation node

**Topic ID**: 24974
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/question-regarding-converting-a-model-back-to-a-segmentation-node/24974

---

## Post #1 by @jegberink (2022-08-29 09:38 UTC)

<p>Hello,</p>
<p>My question pertains to the conversion of a model back to a segmentation.</p>
<p>Currently i want to overlay 2 CT scans to calculate the dice score between 2 femoral segmentations (preoperative and postoperative).<br>
These CT’s are not in the same orientation and do not overlap.</p>
<p>I first segment both, convert them to a model and use SlicerIGT’s model registration to overlap these models. Then convert them back to a segmentation node and us slicerRT segment comparison to compute the dice score and hausdorff distances.</p>
<p>If i return both models back to a segmentation node, will there be a loss in quality or will the original segmentation stay intact?</p>
<p>Any suggestion to my way of approaching this would also be quite welcome.</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2022-08-29 17:55 UTC)

<p>You wouldn’t need to convert the models back to segmentations.  You can just apply the transform to the segmentations and calculate your metrics in binary labelmap space.</p>

---

## Post #3 by @jegberink (2022-08-29 18:52 UTC)

<p>Truly overcomplicated it. Thank you, such a simple solution.</p>

---
