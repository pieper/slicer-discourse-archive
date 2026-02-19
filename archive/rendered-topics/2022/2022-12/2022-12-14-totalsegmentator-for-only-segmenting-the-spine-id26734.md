---
topic_id: 26734
title: "Totalsegmentator For Only Segmenting The Spine"
date: 2022-12-14
url: https://discourse.slicer.org/t/26734
---

# TotalSegmentator for only segmenting the spine

**Topic ID**: 26734
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/totalsegmentator-for-only-segmenting-the-spine/26734

---

## Post #1 by @drvarunagarwal (2022-12-14 16:33 UTC)

<p>hi,</p>
<p>can we use this just to segment spine in isolation?</p>
<p>Please advise</p>

---

## Post #2 by @lassoan (2022-12-14 16:47 UTC)

<p>Yes, it already segments each vertebra separately. You can show on vertebra or all vertebra, and hide everything else.</p>

---

## Post #3 by @drvarunagarwal (2022-12-14 16:50 UTC)

<p>Thanks for the prompt reply</p>
<p>What I meant was</p>
<p>So if we can adapt this to just segment spine then it will take less processing power and time rather than segment everything and hide rest</p>
<p>Is that possible?</p>
<p>Best Regards,<br>
Dr. Varun Agarwal</p>

---

## Post #4 by @lassoan (2022-12-14 17:00 UTC)

<p>You cannot easily gain time by ignoring all the other structures, other than deleting segments before show 3D.</p>
<p>If you want to speed up the segmentation by segmenting less structures then you would need to modify the model. There are a few examples in TotalSegmentator for a two-stage approach: first perform a fast overall segmentation to get a region of interest and then run a refined model for that region. But the aim there is to improve the segmentation quality.</p>
<p>Is the few-minute computation time a problem or you have been just wondering if it could be easily reduced?</p>

---

## Post #5 by @rbumm (2022-12-14 19:41 UTC)

<p>As Andras said, you would need to segment all structures, as the selective programs are only implemented for a few use cases.</p>
<p>But you could use the “Filter” function in “Segmentations” as <a href="https://youtu.be/osvMB5SKcVQ?t=90">shown here</a> to just display the vertebrae.</p>

---

## Post #6 by @lassoan (2022-12-20 05:05 UTC)

<p>I’ve realized that you can actually complete the full-resolution segmentation faster if you only need the spine, because the model is trained in 5 groups (organs, vertebrae, cardiac, muscles, ribs) and you could modify the implementation to only compute the vertebrae group.</p>

---

## Post #7 by @drvarunagarwal (2023-01-25 15:58 UTC)

<p>how about marking ROI first manually<br>
cropping it out<br>
and then running total segmentator</p>

---

## Post #8 by @lassoan (2023-01-25 19:31 UTC)

<p>No need to mark the ROI manually first, as the vertebrae are segmented using a single model. If you crop the image then processing might be a little bit faster because some preprocessing steps may take longer for a larger image. However, you can expect much bigger speed improvement (processing may be 5x faster) by l running only the task necessary for spine segmentation. You can experiment with simply changing a <a href="https://github.com/wasserth/TotalSegmentator/blob/master/bin/TotalSegmentator#L113">single line in the TotalSegmentator executable script</a> in your Slicer installation (<code>...\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator</code>).</p>

---

## Post #9 by @wesselk (2023-11-06 22:59 UTC)

<p>This is now possible in Total Segmentator 2. From their <a href="https://github.com/wasserth/TotalSegmentator#advanced-settings" rel="noopener nofollow ugc">documentation</a>:</p>
<blockquote>
<p><code>--roi_subset</code> : Takes a space-separated list of class names (e.g. <code>spleen colon brain</code> ) and only predicts those classes.</p>
</blockquote>

---

## Post #10 by @rbumm (2023-11-07 09:59 UTC)

<p>Yes, we will implement it in the next version of the extension which will be out when 3D Slicer 5.5.0 becomes stable version.</p>

---

## Post #11 by @drvarunagarwal (2023-12-17 17:49 UTC)

<p>hello all</p>
<p>I tried totalsegmentator<br>
Needless to say that it is a brilliant extension</p>
<p>I tried to segement partially<br>
When I select “vertebral body” as segmentation task only the body is segmented and not the pedicles or spinous processes</p>
<p>however when I select “total” as segmentation task then whole vertebrae are segmented - in addition to rest of the stuff</p>
<p>how to segement whole of vertebrae only without other things or only bones?</p>
<p>Please advise<br>
thanks</p>

---

## Post #12 by @lassoan (2023-12-17 20:34 UTC)

<p>Vertebral body segmentation model only segments the vertebral body, not the processes.</p>
<p>In our projects we merge and remove the segments/details that we don’t need.</p>
<p>It could be possible to slightly reduce the execution time if you only run the bone segmentation subtask, but that would require some development in the extension and maybe slight changes in TotalSegmentator as well. We don’t plan to work on this right now, so you would need to find someone to work on it (but we can help with advice).</p>

---
