---
topic_id: 46908
title: "Pencil Tool Not Visible On Some Slices But Works In 3D View"
date: 2026-05-03
url: https://discourse.slicer.org/t/46908
---

# Pencil tool not visible on some slices, but works in 3D view

**Topic ID**: 46908
**Date**: 2026-05-03
**URL**: https://discourse.slicer.org/t/pencil-tool-not-visible-on-some-slices-but-works-in-3d-view/46908

---

## Post #1 by @Alexander_Schirkow (2026-05-03 14:35 UTC)

<p>Hello,</p>
<p>I encountered an issue when using the Pencil tool in Segment Editor. On some slices and with certain datasets, the pencil strokes are not visible in the 2D views (axial/sagittal/coronal). However, in the 3D view it is clear that the segmentation is actually being created.</p>
<p>Steps to reproduce:</p>
<p>1. Load a volume (.mhd in my case)</p>
<p>2. Open Segment Editor</p>
<p>3. Use the Pencil tool on different slices</p>
<p>Expected behavior:</p>
<p>The drawn segmentation should be visible in 2D slice views while drawing.</p>
<p>Actual behavior:</p>
<p>On some slices/files, the pencil is not visible in 2D views, although it appears correctly in 3D.</p>
<p>Version: Slicer 5.10.0 (rev 34045)</p>
<p>Any ideas what might be causing this?</p>
<p>Thanks.</p>
<p>[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Session start time …: 20260503_095834<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) macosx-amd64 - installed release<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Operating system …: macOS / 26.4.1 / 25E253 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Memory …: 8192 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - CPU …:  Apple M2, 8 cores, 8 logical processors<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Qt configuration …: version 5.15.18, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 03.05.2026 09:58:34 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Additional module paths ..: (none)<br>
[INFO][Stream] 03.05.2026 09:58:35 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) -<br>
[DEBUG][Python] 03.05.2026 09:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 03.05.2026 09:58:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-5.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 03.05.2026 09:58:38 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 03.05.2026 09:58:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_007/vibe963_q_dixon_tra_p4_bh_DL_FF_Series0103.mhd” “[0.12s]”<br>
[DEBUG][Qt] 03.05.2026 09:58:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_007/vibe963_q_dixon_tra_p4_bh_DL_R2s_Eff_Series0105.mhd” “[0.04s]”<br>
[DEBUG][Qt] 03.05.2026 09:58:59 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_007/vibe963_q_dixon_tra_p4_bh_DL_W_Series0101.mhd” “[0.03s]”<br>
[DEBUG][Qt] 03.05.2026 09:59:11 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 03.05.2026 09:59:18 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[INFO][Stream] 03.05.2026 10:10:52 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - self.extentGrowthRatio = 0.1<br>
[INFO][Stream] 03.05.2026 10:10:52 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - masterImageExtent = (0, 319, 0, 279, 0, 71)<br>
[INFO][Stream] 03.05.2026 10:10:52 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - labelsEffectiveExtent = (68, 217, 91, 203, 4, 63)<br>
[INFO][Stream] 03.05.2026 10:10:52 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - labelsExpandedExtent = [54, 231, 80, 214, 0, 68]<br>
[DEBUG][Qt] 03.05.2026 10:16:43 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 03.05.2026 10:16:47 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[INFO][Stream] 03.05.2026 10:27:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - self.extentGrowthRatio = 0.1<br>
[INFO][Stream] 03.05.2026 10:27:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - masterImageExtent = (0, 319, 0, 279, 0, 71)<br>
[INFO][Stream] 03.05.2026 10:27:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - labelsEffectiveExtent = (68, 263, 90, 203, 4, 63)<br>
[INFO][Stream] 03.05.2026 10:27:58 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - labelsExpandedExtent = [49, 282, 79, 214, 0, 68]<br>
[DEBUG][Qt] 03.05.2026 10:30:04 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Markups”<br>
[DEBUG][Qt] 03.05.2026 10:32:19 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 03.05.2026 10:33:08 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 03.05.2026 12:12:24 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_008/vibe963_q_dixon_tra_p4_bh_DL_FF_Series0103.mhd” “[0.15s]”<br>
[DEBUG][Qt] 03.05.2026 12:12:24 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_008/vibe963_q_dixon_tra_p4_bh_DL_R2s_Eff_Series0105.mhd” “[0.04s]”<br>
[DEBUG][Qt] 03.05.2026 12:12:24 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/alexanderschirkow/Downloads/SITE_006_PAT_008/vibe963_q_dixon_tra_p4_bh_DL_W_Series0101.mhd” “[0.03s]”<br>
[DEBUG][Qt] 03.05.2026 12:12:37 <span class="chcklst-box fa fa-square-o"></span> (unknown:0) - Switch to module:  “SegmentEditor”</p>

---
