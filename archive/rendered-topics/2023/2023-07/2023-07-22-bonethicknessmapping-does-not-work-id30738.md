---
topic_id: 30738
title: "Bonethicknessmapping Does Not Work"
date: 2023-07-22
url: https://discourse.slicer.org/t/30738
---

# BoneThicknessMapping does not work

**Topic ID**: 30738
**Date**: 2023-07-22
**URL**: https://discourse.slicer.org/t/bonethicknessmapping-does-not-work/30738

---

## Post #1 by @Yanglab (2023-07-22 03:03 UTC)

<p>Hi guys, I’m try to use bone thickness mapping on my own data and demo data (Predentalsurgery).<br>
But none of them worked.<br>
The status kept showing Initializing execution, and the process was permanantly 0%.<br>
When I checked the python console, it feeded back:</p>
<p>Initializing execution…<br>
Traceback (most recent call last):<br>
File “C:/Users/Administrator/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 521, in click_execute<br>
BoneThicknessMappingLogic.set_scalar_colour_bar_state(0)<br>
File “C:/Users/Administrator/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 936, in set_scalar_colour_bar_state<br>
ctkBar = slicer.util.findChildren(colorWidget, name=‘VTKScalarBar’)[0]<br>
IndexError: list index out of range<br>
[Qt] This function is deprecated. Use lookFromAxis(const ctkAxesWidget::Axis&amp; axis) instead.</p>
<p>Do anyone have any cues what it means? Thanks for you nice guys’ help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa9ac5155dc2809c461cc3bbc21942e2e9b2dae7.png" data-download-href="/uploads/short-url/zKWXyayX2ZdRh2f5szV4HRYbFUH.png?dl=1" title="problem1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9ac5155dc2809c461cc3bbc21942e2e9b2dae7_2_690x388.png" alt="problem1" data-base62-sha1="zKWXyayX2ZdRh2f5szV4HRYbFUH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9ac5155dc2809c461cc3bbc21942e2e9b2dae7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9ac5155dc2809c461cc3bbc21942e2e9b2dae7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa9ac5155dc2809c461cc3bbc21942e2e9b2dae7_2_1380x776.png 2x" data-dominant-color="E3DEE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem1</span><span class="informations">1920×1080 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @JulianEG (2026-01-29 19:15 UTC)

<p>With this fix it should work in 3D slicer version 5.10. <a href="https://discourse.slicer.org/t/color-scalar-bar-reworked-and-upgraded-now-it-s-called-color-legend/21567/12" class="inline-onebox">"Color Scalar Bar" reworked and upgraded, now it’s called "Color Legend" - #12 by Mik</a> .</p>

---
