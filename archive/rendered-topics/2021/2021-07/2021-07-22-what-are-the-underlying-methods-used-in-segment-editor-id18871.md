---
topic_id: 18871
title: "What Are The Underlying Methods Used In Segment Editor"
date: 2021-07-22
url: https://discourse.slicer.org/t/18871
---

# What are the underlying methods used in Segment Editor?

**Topic ID**: 18871
**Date**: 2021-07-22
**URL**: https://discourse.slicer.org/t/what-are-the-underlying-methods-used-in-segment-editor/18871

---

## Post #1 by @Saima (2021-07-22 05:53 UTC)

<p>Hi Andras,<br>
I need to know what method is used to convert a volume to labelmap using createlabelvolumefromvolume. What is the method behind it. Does it use thresholding? can I get more details on this how this function convet a volume to label map.</p>
<p>Also where can I find details of methods for the split island module and then the segmentation statistics module. I need to know about the underlying methods behind all these modules.</p>
<p>Thank you so much</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2021-07-22 11:50 UTC)

<p>You can find full source code of Segmentations and Segment Editor modules <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations">here</a>. Segmentation data management and conversions are implemented in the <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore">segmentation core library</a> (a somewhat older version also made available as a standalone library, PolySeg).</p>

---

## Post #3 by @Saima (2021-08-02 06:34 UTC)

<p>Hi andras,<br>
How can i cite the split island filter. or what is the method behind the splitting? can I get any reference for it. Similarly if I am using createlabelvolumefromvolume or segment statistics what methods I should mention and what are the references. sorry I couldnt find references or methods behind these tasks.</p>
<p>Example, there is thresholding method, growcut method and watershed.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @muratmaga (2021-08-02 17:10 UTC)

<p>Most of these methods will not have a citable paper. You can cite the SegmentEditor as a tool and refer to its github page and then you can cite the Slicer as a general biomedical analysis platform. These two are the common ones people use:</p>
<p>Fedorov, A., Beichel, R., Kalpathy-Cramer, J., Finet, J., Fillion-Robin, J.-C., Pujol, S., Bauer, C., Jennings, D., Fennessy, F., Sonka, M., Buatti, J., Aylward, S., Miller, J. V., Pieper, S., &amp; Kikinis, R. (2012). 3D Slicer as an image computing platform for the Quantitative Imaging Network. <em>Magnetic Resonance Imaging</em> , <em>30</em> (9), 1323–1341. <a href="https://doi.org/10.1016/j.mri.2012.05.001" class="inline-onebox" rel="noopener nofollow ugc">Redirecting</a></p>
<p>Kikinis, R., Pieper, S. D., &amp; Vosburgh, K. G. (2014). 3D Slicer: A Platform for Subject-Specific Image Analysis, Visualization, and Clinical Support. In <em>Intraoperative Imaging and Image-Guided Therapy</em> (pp. 277–289). Springer, New York, NY. <a href="https://doi.org/10.1007/978-1-4614-7657-3_19" class="inline-onebox" rel="noopener nofollow ugc">3D Slicer: A Platform for Subject-Specific Image Analysis, Visualization, and Clinical Support | SpringerLink</a></p>

---

## Post #5 by @lassoan (2021-08-02 17:29 UTC)

<p>Yes, citing 3D Slicer platform paper (as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#how-to-cite">here</a>) and indicating the Slicer version number and module/tool names should be sufficient to specify what algorithms you used exactly.</p>
<p>If you want to reward developers of selected features that you have found particularly useful then you can look up more specific papers. For example, the overall framework of Segment Editor is described in <a href="https://doi.org/10.1016/j.cmpb.2019.02.011">this paper</a>. Reference paper for algorithms used in non-trivial Segment Editor effects (such as Grow from seeds and Fill between slices) are described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor documentation</a>.</p>

---

## Post #6 by @muratmaga (2021-08-02 17:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="18871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, the overall framework of Segment Editor is described in <a href="https://doi.org/10.1016/j.cmpb.2019.02.011">this paper </a>.</p>
</blockquote>
</aside>
<p>I wasn’t aware of that paper. I think you should also have a How to Cite section under the Segment Editor since it is a very heavily used module. Documentation page doesn’t seem to point out to that paper.</p>

---

## Post #7 by @lassoan (2021-08-03 12:41 UTC)

<p>FYI, I’ve added a “How to cite” section to Segment Editor documentation - <a href="https://github.com/Slicer/Slicer/blob/master/Docs/user_guide/modules/segmenteditor.md#how-to-cite" class="inline-onebox">Slicer/segmenteditor.md at master · Slicer/Slicer · GitHub</a></p>

---
