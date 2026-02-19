---
topic_id: 45635
title: "Segment Editor Crashes During Logical Operators In Segment E"
date: 2025-12-30
url: https://discourse.slicer.org/t/45635
---

# Segment Editor crashes during Logical Operators in segment editor (Intersect) - Windows 10 - Lenovo LOQ 5.10.0

**Topic ID**: 45635
**Date**: 2025-12-30
**URL**: https://discourse.slicer.org/t/segment-editor-crashes-during-logical-operators-in-segment-editor-intersect-windows-10-lenovo-loq-5-10-0/45635

---

## Post #1 by @zahra_Tabasi (2025-12-30 04:30 UTC)

<p><strong>Title:</strong> Segment Editor crashes during Logical Operators (Intersect) - Windows 10 - Lenovo LOQ</p>
<p><strong>Slicer version:</strong> 5.10.0 (stable) + preview versions tested<br>
<strong>OS:</strong> Windows 10<br>
<strong>Hardware:</strong> Lenovo LOQ 15IRH8 (i7-13th gen, 32GB RAM, NVIDIA RTX)<br>
<strong>Data:</strong> CT chest + RTSTRUCT (3.5GB total 22 patients, but crash with single patient)</p>
<p><strong>Steps to reproduce:</strong></p>
<ol>
<li>Load DICOM CT + RTSTRUCT (single patient)</li>
<li>Segment Editor → Logical Operators → Intersect (Heart + Field)</li>
<li>Click Apply → Immediate crash</li>
</ol>
<p><strong>Error logs:</strong><br>
[Log Name:      Application<br>
Source:        Application Error<br>
Date:          08/10/1404 02:40:14 ب.ظ<br>
Event ID:      1000<br>
Task Category: (100)<br>
Level:         Error<br>
Keywords:      Classic<br>
User:          N/A<br>
Computer:      DESKTOP-F92USHO<br>
Description:<br>
Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x6911bf2c<br>
Faulting module name: qSlicerBaseQTApp.dll, version: 0.0.0.0, time stamp: 0x6911bf23<br>
Exception code: 0xc0000005<br>
Fault offset: 0x0000000000005763<br>
Faulting process id: 0xac<br>
Faulting application start time: 0x01dc7913153620dd<br>
Faulting application path: E:\3D Slicer 5.10.0\bin\SlicerApp-real.exe<br>
Faulting module path: E:\3D Slicer 5.10.0\bin\qSlicerBaseQTApp.dll<br>
Report Id: 9b2d9262-e59a-4fae-a7da-c18098b0a6e5<br>
Faulting package full name:<br>
Faulting package-relative application ID:<br>
Event Xml:</p>
<p>1000<br>
0<br>
2<br>
100<br>
0<br>
0x80000000000000</p>
<p>3864</p>
<p>Application<br>
DESKTOP-F92USHO</p>
<p>SlicerApp-real.exe<br>
0.0.0.0<br>
6911bf2c<br>
qSlicerBaseQTApp.dll<br>
0.0.0.0<br>
6911bf23<br>
c0000005<br>
0000000000005763<br>
ac<br>
01dc7913153620dd<br>
E:\3D Slicer 5.10.0\bin\SlicerApp-real.exe<br>
E:\3D Slicer 5.10.0\bin\qSlicerBaseQTApp.dll<br>
9b2d9262-e59a-4fae-a7da-c18098b0a6e5</p>
<p>]<br>
[[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20251229_144023<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.10.0 (revision 34045 / a2b6d08) win-amd64 - installed release<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19045, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16108 MB physical, 37612 MB virtual<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - DCMTK configuration …: version 3.6.8, no SSL<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: E:/3D Slicer 5.10.0/bin<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۳ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/cli-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34045/SlicerRT/lib/Slicer-5.10/qt-scripted-modules</a><br>
[INFO][Stream] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۴ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[DEBUG][Python] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۵ [Python] (E:\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۵ [Python] (E:\3D Slicer 5.10.0\lib\Slicer-5.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] ۲۹.۱۲.۲۰۲۵ ۱۴:۴۰:۲۵ <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
]<br>
[Console output if available]</p>
<p><strong>Tried:</strong></p>
<ul>
<li>Show 3D off</li>
<li>Single patient only</li>
<li>Oversampling=1</li>
<li>Multiple Slicer versions</li>
<li>Close other apps</li>
</ul>

---

## Post #2 by @muratmaga (2025-12-30 05:59 UTC)

<p>Windows 10 is not supported at this point. Any chance you can try this on a computer with windows 11 (to rule out that this is not a windows 10 specific problem)?</p>

---

## Post #3 by @lassoan (2025-12-30 15:28 UTC)

<p>I could not reproduce the problem. Could you share the scene file (saved as .mrb) that you have problem with? Make sure the data is anonymized or use one of the images from Sample Data module.</p>

---

## Post #4 by @zahra_Tabasi (2025-12-30 22:41 UTC)

<p><strong>UPDATE: CRITICAL - Cannot even SAVE scene file (.mrb)</strong></p>
<p><strong>Original Issue:</strong> Segment Editor → Logical Operators → Intersect → CRASH on Apply<br>
<strong>NEW Issue:</strong> Even File → Save fails BEFORE Apply!</p>
<p><strong>Error Screenshot:</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b30a5f9c3ac6bc571d64163e42155940c3f4e54a.png" data-download-href="/uploads/short-url/pxRGV8AplTGNfRyb4WrXmMl4YFY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b30a5f9c3ac6bc571d64163e42155940c3f4e54a.png" alt="image" data-base62-sha1="pxRGV8AplTGNfRyb4WrXmMl4YFY" width="501" height="390"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">501×390 12 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Error Details:</strong> Slicer has caught an application error, please save your work and restart. The application has run out of memory. Exception thrown in event: bad_alloc</p>
<p><strong>Steps to reproduce:</strong></p>
<ol>
<li>Load single patient CT + RTSTRUCT (Heart + Field segments)</li>
<li>Segment Editor → Logical Operators → Intersect (Heart ∩ Field)</li>
<li><strong>File → Save (.mrb)</strong> → <strong>CRASH before saving</strong></li>
<li>No Apply clicked yet!</li>
</ol>
<p><strong>System:</strong></p>
<ul>
<li>Windows 10 (32GB RAM Lenovo LOQ i7)</li>
<li>Slicer 5.10 stable</li>
<li>Single patient only (~500MB CT)</li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>Previously could save outputs manually</li>
<li>Now crashes even on Save scene</li>
<li>Tried: Close 3D view, single slice viewer</li>
</ul>
<p><strong>Windows 11 VM testing tomorrow.</strong></p>
<p><strong>Request:</strong> This <code>bad_alloc</code> on Save is blocking .mrb sharing.</p>

---

## Post #5 by @lassoan (2025-12-30 22:54 UTC)

<p>This is very useful information. Your computer has simply run out of memory. If you are not working with a particularly large image then most likely there is a problem in your processing workflow that leads to unreasonably large memory need.</p>
<p>For example, you may have some structures that are very far out, which makes the segmentation extents extremely large. You can find the offending segment by inspecting content of the segmentation node in Data module; or delete segments and see which one you need to remove to resolve the issue. You can also force the segmentation to be stay within the reference image geometry (typically the geometry of the segmented image) by setting <code>Crop to reference image geometry</code> conversion parameter to 1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5218e929ae3ae230e1be64805bdb8dc3bb3ffa0.png" data-download-href="/uploads/short-url/uprAZgS730uFkfDU1UzqdgZUHQc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5218e929ae3ae230e1be64805bdb8dc3bb3ffa0_2_505x500.png" alt="image" data-base62-sha1="uprAZgS730uFkfDU1UzqdgZUHQc" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5218e929ae3ae230e1be64805bdb8dc3bb3ffa0_2_505x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5218e929ae3ae230e1be64805bdb8dc3bb3ffa0_2_757x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5218e929ae3ae230e1be64805bdb8dc3bb3ffa0_2_1010x1000.png 2x" data-dominant-color="E3E6E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1689×1672 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
