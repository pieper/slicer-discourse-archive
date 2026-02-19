---
topic_id: 21382
title: "How Cna I Save My Segmentation Seperately"
date: 2022-01-10
url: https://discourse.slicer.org/t/21382
---

# How cna I save my segmentation seperately?

**Topic ID**: 21382
**Date**: 2022-01-10
**URL**: https://discourse.slicer.org/t/how-cna-i-save-my-segmentation-seperately/21382

---

## Post #1 by @LIE_CAI (2022-01-10 09:37 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91678a2db2befa9ab57fec9a8520caac50786fe.png" data-download-href="/uploads/short-url/xfZouqMWBp2mqRFyxhBvllgHTXg.png?dl=1" title="1641807198(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e91678a2db2befa9ab57fec9a8520caac50786fe_2_517x500.png" alt="1641807198(1)" data-base62-sha1="xfZouqMWBp2mqRFyxhBvllgHTXg" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e91678a2db2befa9ab57fec9a8520caac50786fe_2_517x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e91678a2db2befa9ab57fec9a8520caac50786fe_2_775x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91678a2db2befa9ab57fec9a8520caac50786fe.png 2x" data-dominant-color="F2F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1641807198(1)</span><span class="informations">787×760 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
For example, now I have two segmentation documents.<br>
But when I click the save button I only get one document.<br>
How can I save them seperately?<br>
Thanks a lot!</p>

---

## Post #2 by @Fluvio_Lobo (2022-01-10 14:51 UTC)

<p>The <code>Segmentation.seg.nrrd</code> extension saves the segmentation node, including both segments <code>(Segment_1, Segment_2)</code>, and a reference to the master volume used for the segmentation <code>(6 1st ax dyn)</code></p>

---

## Post #3 by @LIE_CAI (2022-01-10 14:54 UTC)

<p>Thanks, is it possible to save them separately?<br>
Because I want to do an analysis of these two segmentation independently and jointly.</p>
<p>Fluvio Lobo via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; 于2022年1月10日周一 15:51写道：</p>

---

## Post #4 by @Fluvio_Lobo (2022-01-10 16:19 UTC)

<p><a class="mention" href="/u/lie_cai">@LIE_CAI</a>,</p>
<p>Quick and dirty: Clone the segmentation node and erase the segments you don’t need on each respective copy. You will end-up with multiple segmentations nodes with only one segment, in your case.</p>
<p>Keep in mind that any relevant analysis is tied to the <code>master volume</code>. So ensure that each “cloned” node has the right <code>master volume</code> assigned.</p>

---

## Post #5 by @LIE_CAI (2022-01-11 18:06 UTC)

<p>Got that. But how to clone the segmentation node?<br>
Just repeating the segment process would be waste of time…</p>
<p>Fluvio Lobo via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; 于2022年1月10日周一 17:19写道：</p>

---

## Post #6 by @Fluvio_Lobo (2022-01-11 18:10 UTC)

<p>Right click, clone node!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f40031f8b8f88447daf322f07ff1aa1d5185fd6c.png" data-download-href="/uploads/short-url/yOwV6lHiB9PcrerHaNMtkoWPh6I.png?dl=1" title="clone_node" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f40031f8b8f88447daf322f07ff1aa1d5185fd6c.png" alt="clone_node" data-base62-sha1="yOwV6lHiB9PcrerHaNMtkoWPh6I" width="690" height="131" data-dominant-color="354A51"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clone_node</span><span class="informations">706×135 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @LIE_CAI (2022-01-11 18:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f42f6bed4e9419c15dd5adcf8555ebe2e464db8c.png" data-download-href="/uploads/short-url/yQa6oe9oDsOkIAIvTV7WYKzFcpC.png?dl=1" title="1641926280(1).png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f42f6bed4e9419c15dd5adcf8555ebe2e464db8c_2_472x59.png" alt="1641926280(1).png" data-base62-sha1="yQa6oe9oDsOkIAIvTV7WYKzFcpC" width="472" height="59" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f42f6bed4e9419c15dd5adcf8555ebe2e464db8c_2_472x59.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f42f6bed4e9419c15dd5adcf8555ebe2e464db8c_2_708x88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f42f6bed4e9419c15dd5adcf8555ebe2e464db8c.png 2x" data-dominant-color="CEDDEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1641926280(1).png</span><span class="informations">925×115 6.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hmmm, I still have not found the clone node button.<br>
But I found a way to achieve it.<br>
First, click “Segmentations…”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6f2947d8b00b90d2f723e3df9f9a70cd26759e4.png" data-download-href="/uploads/short-url/uFvU32neBRvXxVv2lO82Crsrkaw.png?dl=1" title="1641926307(1).png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f2947d8b00b90d2f723e3df9f9a70cd26759e4_2_472x290.png" alt="1641926307(1).png" data-base62-sha1="uFvU32neBRvXxVv2lO82Crsrkaw" width="472" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f2947d8b00b90d2f723e3df9f9a70cd26759e4_2_472x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f2947d8b00b90d2f723e3df9f9a70cd26759e4_2_708x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6f2947d8b00b90d2f723e3df9f9a70cd26759e4.png 2x" data-dominant-color="E8EFF4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1641926307(1).png</span><span class="informations">939×576 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then click “Copy/move segments”,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce300984335bfc4d5f962f9b0ea6240b8eb4d11e.png" alt="1641926452(1).png" data-base62-sha1="tq1heWJcGbL2QPSLYagJMGemnCu" width="472" height="154"></p>
<p>Then choose “Create new Segmentation”.<br>
In this way, I can get two “segmentation. nrrd” documents and save them separately.<img src="https://emoji.discourse-cdn.com/twitter/yum.png?v=12" title=":yum:" class="emoji" alt=":yum:" loading="lazy" width="20" height="20"></p>
<p>Fluvio Lobo via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; 于2022年1月11日周二 19:10写道：</p>

---
