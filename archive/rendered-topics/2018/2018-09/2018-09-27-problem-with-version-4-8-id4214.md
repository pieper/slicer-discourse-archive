---
topic_id: 4214
title: "Problem With Version 4 8"
date: 2018-09-27
url: https://discourse.slicer.org/t/4214
---

# Problem with version 4.8

**Topic ID**: 4214
**Date**: 2018-09-27
**URL**: https://discourse.slicer.org/t/problem-with-version-4-8/4214

---

## Post #1 by @Ash_Alarfaj (2018-09-27 21:42 UTC)

<p>when I’ve finished the segmentation and need to do the segment statistic. the apply icon didn’t active and I need to save my segmentation then close the programme and reopen it to activate the segment statistic. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896134a4365fac9ac94b82f9d3dbffb6649116b6.png" data-download-href="/uploads/short-url/jBjFSPC9R9DP1EQ66mkcaelLYG2.png?dl=1" title="24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/896134a4365fac9ac94b82f9d3dbffb6649116b6_2_690x344.png" alt="24" data-base62-sha1="jBjFSPC9R9DP1EQ66mkcaelLYG2" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/896134a4365fac9ac94b82f9d3dbffb6649116b6_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/896134a4365fac9ac94b82f9d3dbffb6649116b6_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/896134a4365fac9ac94b82f9d3dbffb6649116b6.png 2x" data-dominant-color="8C8B91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">24</span><span class="informations">1362×680 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>please consider this problem as I need to work with so much data. however, this version is work very nice better than version 4.9</p>
<p>best regards</p>

---

## Post #2 by @lassoan (2018-09-27 22:31 UTC)

<p>If you experience problems with Slicer-4.8 that are fixed in recent Slicer-4.9.x version then I would recommend to use Slicer-4.9 - it works well and will be soon released as the new stable version.</p>
<p>If you have any problems with Slicer-4.9.x then let us know.</p>

---

## Post #3 by @Ash_Alarfaj (2018-09-27 22:33 UTC)

<p>Yes I am using Mac and I can’t upload data in version 4.9. it totally didn’t work.</p>
<p>THANKS</p>

---

## Post #4 by @stephan (2018-09-27 23:19 UTC)

<p>I had the same problem in 4.8.1 before, but it is easy to solve:<br>
For some reason, the drop down menu “Parameter Set” seem to reset itself to “Select a ScriptedModule” when opening the SegmentStatistics module several times.<br>
Simply make sure the only ScripteModule available in the drop down menu, called “SegmentStatistics”, is selected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8040a8379a3dfe7f5c5a70f57b886db14c65833.jpeg" data-download-href="/uploads/short-url/nYkS7KN7hocRqkE2IfnH9IWSxiz.jpeg?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8040a8379a3dfe7f5c5a70f57b886db14c65833_2_690x344.jpeg" alt="screenshot" data-base62-sha1="nYkS7KN7hocRqkE2IfnH9IWSxiz" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8040a8379a3dfe7f5c5a70f57b886db14c65833_2_690x344.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/8/a8040a8379a3dfe7f5c5a70f57b886db14c65833_2_1035x516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8040a8379a3dfe7f5c5a70f57b886db14c65833.jpeg 2x" data-dominant-color="A7A5AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1362×680 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2018-09-27 23:19 UTC)

<p>Please describe what you did exactly, what you expected to happen, and what happened instead.</p>

---

## Post #6 by @Ash_Alarfaj (2018-09-28 08:57 UTC)

<p>Thanks for replay I will give a try.</p>

---

## Post #7 by @Ash_Alarfaj (2018-09-28 10:43 UTC)

<p>HI<br>
I’ve done your option but still, the problem exist? do you think if I redownload the programme, the problem will resolve? this programme is promising but there is few things need to fix. I will use it for 3 publications with large data so I hope the developer fix this problem.</p>

---

## Post #8 by @dzenanz (2018-09-28 12:46 UTC)

<p>Andras is one of the developers, and in order to fix it he first needs to know what exactly the problem is, and how to reproduce it. What steps to do to trigger the problem?</p>

---

## Post #9 by @lassoan (2018-09-28 13:07 UTC)

<p>Exactly. We need description of every click that you make. You may also record a screen capture video and share that.</p>
<p>Do you use Model Maker module? Currently, <a href="https://issues.slicer.org/view.php?id=4570">running Model Maker module has the side effect</a> that it de-selects nodes in all node selectors. Workaround is that you need to re-select the modules.</p>

---

## Post #10 by @Ash_Alarfaj (2018-09-28 13:32 UTC)

<p>Hi<br>
you need me to explain the problem in version 4.8 or the nighty one 4.9 mac?</p>
<p>I am working on my DICOM MRI DATA from my university.</p>
<p>thanks</p>

---

## Post #11 by @stephan (2018-09-28 14:28 UTC)

<p>I think we have two issues here:</p>
<ol>
<li>The greyed out Apply button in the Segment Statistics module in 4.8. and</li>
<li>something not working for you in 4.9.</li>
</ol>
<p><a class="mention" href="/u/lassoan">@lassoan</a>: How to reproduce 1:<br>
When opening the Segment statistics module, the Parameter set “SegmentStatistics” is pre-selected. This behaviour is expected. However, after closing the scene and re-loading the data (with the Segment Statistics module open), the SegmentStatistics Parameter set disappears (I realized, as opposed to my post above, it’s even no longer in the drop down menu) and the drop down menu shows “Select a Scripted Module”.<br>
And without a Parameter set selected, the Apply button is inactive.<br>
This is reproducible in 4.8.1 and still in 4.9. (r27399)</p>
<p><a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a>: When the drop down menu (the one I circled in the screenshot) shows “Select a Scripted Module”, select the item “Create new Scripted Module” to re-create the missing parameter set. When all the other parameters have been filled in as well (Segmentation, Scalar Volume, Output Table), you should be good to go.</p>
<p>I hope that make sense?</p>

---
