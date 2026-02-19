---
topic_id: 37057
title: "Edit Segmentation Task"
date: 2024-06-26
url: https://discourse.slicer.org/t/37057
---

# Edit Segmentation Task

**Topic ID**: 37057
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/edit-segmentation-task/37057

---

## Post #1 by @AnyGoe (2024-06-26 20:37 UTC)

<p>Dear all,</p>
<p>is there any way to extend the Segmentation task selection in the TotalSegmentator module, so that I can choose myself which anatomical regions I am actually interested in? Using propper GPU-support I wouldn’t mind going for the “total” segmentation, but being restricted to the CPU power, I would like to specify only a subset of organs (liver, spleen and kidneys) for speed-up.</p>
<p>Thx!<br>
Andy</p>

---

## Post #2 by @lassoan (2024-06-27 12:31 UTC)

<p>TotalSegmentator performs inference with 5 models (one after the other) to get all the segments. You could speed up the segmentation by using only those models that produce segments that you need. If you are lucky and all segments you need are in the same model then you could get results about 5x faster. If you need 4 out of 5 models then the speed improvement will not be significant.</p>
<p>If you want to explore this then first you need to check if TotalSegmentator allows running only certain tasks. If that’s possible then I can help with advice on how to make it available in TotalSegmentator.</p>

---

## Post #3 by @AnyGoe (2024-06-28 07:58 UTC)

<p>Thanks a lot for the suggestion. Sounds like a good approach. Using TotalSegmentator via command line, I already succeeded in tailoring the segmentation task to certain anatomical regions using the roi_subset flag. That functionality is actually what I would like to achieve in slicer. Most interesting in 99% of my use cases is kidney segmentation. That might be represented in the inference process by only one of the models, right? So, is there a way to provide a selection for this in the <em>Segmentation Task</em> selector of the TotalSegmentator module. There, I find already an extended set of selectable configurations, including <em>total</em> and a few requiring prior licence agreements. Do you think it’s possible to somehow include e. g. an additional <em>kidney</em> selection there?</p>

---
