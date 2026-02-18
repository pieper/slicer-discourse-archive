# Build slicer stable release from the source on ArchLinux

**Topic ID**: 14236
**Date**: 2020-10-25
**URL**: https://discourse.slicer.org/t/build-slicer-stable-release-from-the-source-on-archlinux/14236

---

## Post #1 by @ButuiHu (2020-10-25 08:37 UTC)

<p>Following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#archlinux" rel="noopener nofollow ugc">build instruction</a>, I could now build 3dslicer 4.11.20200930 from the source in ArchLinux. The <code>PKGBUILD</code> file used to create an ArchLinux package is available <a href="https://github.com/archlinuxcn/repo/blob/master/archlinuxcn/3dslicer/PKGBUILD" rel="noopener nofollow ugc">here</a>. Here are some tips if you would like to build it from the source.</p>
<ol>
<li>DO NOT <code>strip</code>, I mean add <code>options=(!strip)</code> to your <code>PKGBUILD</code> file.</li>
<li>use <code>clang</code> as the compiler, I failed to build with gcc. Currently, the latest clang is 10.0.1, and latest gcc 10.2.0 in ArchLinux. Though gcc8 and gcc9 are available in ArchLinux’s official repo too, they will be removed once there are no pkgs depends on them.</li>
<li>I try to system’s libs instead of superbuild, but I have to do dirty hack to help cmake find sqlite, see also this <a href="https://github.com/Slicer/Slicer/issues/5264" rel="noopener nofollow ugc">issue</a>.</li>
<li>If I set <code>Slicer_USE_SYSTEM_VTK=ON</code>, then <code>Slicer_USE_SYSTEM_CTKAPPLAUNCHER=ON</code> is set, which is not supported, and lead to cmake configuration error. I can’t figure out why this happen yet. If we could use system’s vtk, then I could save more time building the package.</li>
</ol>

---

## Post #2 by @ButuiHu (2020-10-25 10:51 UTC)

<p>I failed to build 3dslicer with gcc 10, because I failed to build itk with gcc 10. itk is required by simpleitk, simpleitk is required by 3dslicer. See also related <a href="https://discourse.itk.org/t/fail-to-build-itk-5-1-1-with-gcc-10-on-archlinux/3571" rel="noopener nofollow ugc">post</a> on itk discourse.</p>

---

## Post #3 by @ButuiHu (2020-10-29 04:27 UTC)

<p>I found that the drop-down menu in Segment Editor (the red rectangle in the snapshot) is not working, but the drop-down menu to switch module (the green rectangle in the snapshot) works.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9dbaab23cad40523e3a44b3a64b1fd9661f5c0.png" data-download-href="/uploads/short-url/6mGWoEfT9dzjkh1CtVHqArk81O0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c9dbaab23cad40523e3a44b3a64b1fd9661f5c0_2_690x465.png" alt="image" data-base62-sha1="6mGWoEfT9dzjkh1CtVHqArk81O0" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c9dbaab23cad40523e3a44b3a64b1fd9661f5c0_2_690x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9dbaab23cad40523e3a44b3a64b1fd9661f5c0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c9dbaab23cad40523e3a44b3a64b1fd9661f5c0.png 2x" data-dominant-color="E7E5E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">716×483 40.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-10-30 04:46 UTC)

<p>Do node selectors work in other modules (volumes, Models, Transforms, …)? Do all the other buttons and widgets work? Do you see any errors in the log?</p>

---

## Post #5 by @ButuiHu (2020-10-30 07:30 UTC)

<p>No, the node selectors do not work in other modules either.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Session start time .......: 2020-10-30 15:26:04
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Slicer version ...........: 4.11.20200930-2020-09-30 (revision 29402 / 002be18) linux-amd64 - installed release
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Operating system .........: Linux / 5.4.72-1-lts / #1 SMP Sat, 17 Oct 2020 13:30:57 +0000 - 64-bit
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Memory ...................: 15791 MB physical, 0 MB virtual
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz, 8 cores, 8 logical processors
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Application path .........: /opt/3dslicer/bin
[DEBUG][Qt] 30.10.2020 15:26:04 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 30.10.2020 15:26:05 [Python] (/opt/3dslicer/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[WARNING][Qt] 30.10.2020 15:26:05 [] (unknown:0) - QXcbConnection: XCB error: 5 (BadAtom), sequence: 594, resource id: 0, major code: 20 (GetProperty), minor code: 0
[DEBUG][Python] 30.10.2020 15:26:06 [Python] (/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 30.10.2020 15:26:07 [Python] (/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 30.10.2020 15:26:07 [Python] (/opt/3dslicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 30.10.2020 15:26:07 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 30.10.2020 15:26:08 [] (unknown:0) - QVTKWidgetPlugin instantiated
[DEBUG][Qt] 30.10.2020 15:26:08 [] (unknown:0) - QVTKWidgetPlugin::name
[DEBUG][Qt] 30.10.2020 15:26:13 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 30.10.2020 15:26:13 [] (unknown:0) - QVTKWidgetPlugin::name
[INFO][Python] 30.10.2020 15:26:15 [Python] (/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:383) - Loading with imageIOName: GDCM
[INFO][Python] 30.10.2020 15:26:16 [Python] (/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:457) - Window/level found in DICOM tags (center=1009.0, width=2018.0) has been applied to volume 7: 3D Ax T1 BRAVO+C
[WARNING][Python] 30.10.2020 15:26:16 [Python] (/opt/3dslicer/bin/../lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py:787) - Irregular volume geometry detected (maximum error of 0.00204849 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.
[INFO][Stream] 30.10.2020 15:26:15 [] (unknown:0) - Loading with imageIOName: GDCM
[WARNING][ITK] 30.10.2020 15:26:16 [ImageSeriesReader (0x55b02c8efc40)] (/build/3dslicer/src/build/ITK/Modules/IO/ImageBase/include/itkImageSeriesReader.hxx:480) - Non uniform sampling or missing slices detected,  maximum nonuniformity:7.87061e-05
[INFO][Stream] 30.10.2020 15:26:16 [] (unknown:0) - Window/level found in DICOM tags (center=1009.0, width=2018.0) has been applied to volume 7: 3D Ax T1 BRAVO+C
[CRITICAL][Stream] 30.10.2020 15:26:16 [] (unknown:0) - Irregular volume geometry detected (maximum error of 0.00204849 mm is above tolerance threshold of 0.001 mm).  Regularization transform is not added, as the option is disabled.
[DEBUG][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Switch to module:  "Volumes"
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;columnWidth(j) == newWidth` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - ctkDoubleRangeSlider::setSingleStep( 100 ) is outside of valid bounds.
[WARNING][Qt] 30.10.2020 15:26:33 [] (unknown:0) - ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds
[WARNING][Qt] 30.10.2020 15:26:38 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:38 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[WARNING][Qt] 30.10.2020 15:26:38 [] (unknown:0) - Assertion `this-&gt;Table-&gt;rowHeight(i) == newHeight` failed in  /build/3dslicer/src/build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253
[DEBUG][Qt] 30.10.2020 15:26:59 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 30.10.2020 15:27:03 [] (unknown:0) - Switch to module:  "Models"
</code></pre>

---

## Post #6 by @lassoan (2020-10-30 13:50 UTC)

<p>Do all the other buttons and widgets work?</p>

---

## Post #7 by @ButuiHu (2020-10-31 03:21 UTC)

<p>what buttons and widgets do you mean? I only notice the node selectors in Segment Editor do not work at first. And those in volumes, models, transforms module do not work either.</p>

---
