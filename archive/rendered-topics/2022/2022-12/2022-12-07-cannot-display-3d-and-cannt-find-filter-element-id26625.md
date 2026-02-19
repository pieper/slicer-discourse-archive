---
topic_id: 26625
title: "Cannot Display 3D And Cannt Find Filter Element"
date: 2022-12-07
url: https://discourse.slicer.org/t/26625
---

# Cannot Display 3d and Cann't find filter element

**Topic ID**: 26625
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/cannot-display-3d-and-cannt-find-filter-element/26625

---

## Post #1 by @yd_l (2022-12-07 12:29 UTC)

<p>Problem report for Slicer 5.2.1 win-amd64: [please describe expected and actual behavior]<br>
Log File Content reports a bug:</p>
<pre><code class="lang-auto">[DEBUG][Python] 07.12.2022 17:44:25 [Python] (C:\Users\new\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor

[DEBUG][Python] 07.12.2022 17:44:25 [Python] (C:\Users\new\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Slicer-5.2\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics

[DEBUG][Qt] 07.12.2022 17:44:25 [] (unknown:0) - Switch to module: "Welcome"

**[CRITICAL][FD] 07.12.2022 17:44:28 [] (unknown:0) - Can't find filter element**

**[CRITICAL][FD] 07.12.2022 17:44:28 [] (unknown:0) - Can't find filter element**
</code></pre>
<p>And the 3dslicer cannot display 3d:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6a4ea6ad83454a1232421f7c97393c1b2968f6.png" data-download-href="/uploads/short-url/xrJuoCEoofvuW1yYfAoxT6NeCCa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6a4ea6ad83454a1232421f7c97393c1b2968f6_2_690x284.png" alt="image" data-base62-sha1="xrJuoCEoofvuW1yYfAoxT6NeCCa" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6a4ea6ad83454a1232421f7c97393c1b2968f6_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6a4ea6ad83454a1232421f7c97393c1b2968f6_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6a4ea6ad83454a1232421f7c97393c1b2968f6_2_1380x568.png 2x" data-dominant-color="BFBFBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2825×1164 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I solve the problem?</p>

---

## Post #2 by @lassoan (2022-12-07 12:34 UTC)

<p>You (or one of the modules you used) switched to a layout that shows 3 slice views and a plot view. If you want to see 3 slice views and a 3D view then you can use the toolbar to switch to the “Four up” layout.</p>
<p>I’m not sure what is the origin of the error messages, but they are probably unrelated.</p>

---

## Post #3 by @yd_l (2022-12-08 06:53 UTC)

<p>Thank you very much, exactly what I needed</p>

---
