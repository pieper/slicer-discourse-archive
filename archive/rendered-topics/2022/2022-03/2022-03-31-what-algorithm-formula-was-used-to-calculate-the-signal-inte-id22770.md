---
topic_id: 22770
title: "What Algorithm Formula Was Used To Calculate The Signal Inte"
date: 2022-03-31
url: https://discourse.slicer.org/t/22770
---

# What algorithm/formula was used to calculate the signal intensity mean and SD in the module segment statistics?

**Topic ID**: 22770
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/what-algorithm-formula-was-used-to-calculate-the-signal-intensity-mean-and-sd-in-the-module-segment-statistics/22770

---

## Post #1 by @Jue (2022-03-31 01:17 UTC)

<p>I used 3d slicer software to segment an adipose tissue from the MRI dicom image, and the module Segment Statistics automatically calculated and displayed the signal intensity mean and SD of this segmentation.<br>
How the signal intensity mean and SD of this segmentation was calculated and what algorithm/formula was used.</p>
<p>I find a code<br>
<code> self.scalarSelector.setToolTip( "Select the scalar volume for intensity statistics calculations")</code><br>
but I couldn’t understand what kind of the algorithm/formula was used.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2022-03-31 13:33 UTC)

<p>If you have any doubts then you can always look up the implementation. <a href="https://github.com/Slicer/Slicer/blob/942a83bbe72646afb788fd6059596a1ca658b9d0/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ScalarVolumeSegmentStatisticsPlugin.py#L32-L60">Segment Statistics module uses vtkImageAccumulate</a> and that class internally uses <a href="https://github.com/Kitware/VTK/blob/master/Imaging/Statistics/vtkImageAccumulate.cxx#L225-L247">this formula</a>, which is the <em>corrected sample standard deviation</em>.</p>

---

## Post #3 by @dszimatore (2023-01-14 18:33 UTC)

<p>Hello! Which command did you use to obtain the signal intensity in the “Segment staistics” module? I can obtain only informarmation about volume.<br>
Thank you!</p>

---

## Post #4 by @rbumm (2023-01-14 19:33 UTC)

<p>You can enable Scalar Volume Statistics but need to select the reference volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b193d0cf24536a8cee02225760809702e29233.png" data-download-href="/uploads/short-url/cECtsNMMJFbRjyzI73Jipk5Tbfd.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b193d0cf24536a8cee02225760809702e29233_2_690x468.png" alt="image" data-base62-sha1="cECtsNMMJFbRjyzI73Jipk5Tbfd" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b193d0cf24536a8cee02225760809702e29233_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58b193d0cf24536a8cee02225760809702e29233_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b193d0cf24536a8cee02225760809702e29233.png 2x" data-dominant-color="DBDAD4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1074×729 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @dszimatore (2023-01-15 11:38 UTC)

<p>I didn’t catch that “mean” was referred to signal intensity!<br>
Thank you very much!</p>

---
