---
topic_id: 14800
title: "Extension Manager Consistenly Doesnt Load On First Try"
date: 2020-11-28
url: https://discourse.slicer.org/t/14800
---

# Extension manager consistenly doesn't load on first try

**Topic ID**: 14800
**Date**: 2020-11-28
**URL**: https://discourse.slicer.org/t/extension-manager-consistenly-doesnt-load-on-first-try/14800

---

## Post #1 by @jsalas424 (2020-11-28 16:41 UTC)

<p>After a fresh boot of slicer, my extension manager opens to a blank page. I need to close the extension manager and then re-open it to get it to work. This is consistently reproducible. Logs and screenshot of fresh boot attached.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71e7b9b21220b3c455747d744a5d7857265bf30c.png" data-download-href="/uploads/short-url/gfEqfRZdHwXysMEc5yjTrWFNZgM.png?dl=1" title="Screen Shot 2020-11-28 at 7.53.39 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71e7b9b21220b3c455747d744a5d7857265bf30c_2_690x431.png" alt="Screen Shot 2020-11-28 at 7.53.39 AM" data-base62-sha1="gfEqfRZdHwXysMEc5yjTrWFNZgM" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71e7b9b21220b3c455747d744a5d7857265bf30c_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71e7b9b21220b3c455747d744a5d7857265bf30c_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71e7b9b21220b3c455747d744a5d7857265bf30c_2_1380x862.png 2x" data-dominant-color="303134"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-28 at 7.53.39 AM</span><span class="informations">2880×1800 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">Session start time .......: 2020-11-28 07:53:23
Slicer version ...........: 4.11.20200930 (revision 29402 / 002be18) macosx-amd64 - installed release
Operating system .........: Mac OS X / 10.15.7 / 19H2 - 64-bit
Memory ...................: 8192 MB physical, 1024 MB virtual
CPU ......................: GenuineIntel Intel(R) Core(TM) i7-8557U CPU @ 1.70GHz, 4 cores, 8 logical processors
VTK configuration ........: OpenGL2 rendering, Sequential threading
Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
Developer mode enabled ...: no
Prefer executable CLI ....: yes
Application path .........: /Applications/Slicer.app/Contents/MacOS
Additional module paths ..: /Applications/Slicer.app/Contents/Extensions-29402/SlicerHeart/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerHeart/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerHeart/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/Sandbox/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/RawImageGuess/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerDcm2nii/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/Auto3dgm/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29402/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules, /Applications/Slicer.app/Contents/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-29402/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules
Reversing DICOM dictionary so can look up tag from a keyword...
libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
libpng warning: iCCP: known incorrect sRGB profile
Scripted subject hierarchy plugin registered: Annotations
Scripted subject hierarchy plugin registered: SegmentEditor
Scripted subject hierarchy plugin registered: SegmentStatistics
Scripted subject hierarchy plugin registered: ExportAs
Switch to module:  "Welcome"
QPixmap::scaled: Pixmap is a null pixmap
libpng warning: iCCP: known incorrect sRGB profile
QPixmap::scaled: Pixmap is a null pixmap
QPixmap::scaled: Pixmap is a null pixmap
QPixmap::scaled: Pixmap is a null pixmap
QPixmap::scaled: Pixmap is a null pixmap
QPixmap::scaled: Pixmap is a null pixmap
QPixmap::scaled: Pixmap is a null pixmap
[936:102147:1128/075337.297499:ERROR:gl_context_cgl.cc(118)] Error creating context.
</code></pre>

---

## Post #2 by @lassoan (2020-11-28 16:48 UTC)

<p>The extension manager can take up to a minute to start. In current stable (Slicer-4.11.20200930) version you can click on the extension manager button again, which makes the incompletely initialized window appear immediately, leading various issues later. In latest Slicer preview release we fixed this issue, but in the latest stable version you need to restrain yourself and <em>click only once</em> and wait until the extension manager appears. <strong>Do not click again while you are waiting for the window to show up.</strong></p>
<p>We will replace the extension manager server soon and then we will try to optimize the extension manager startup time then, but for now you need to wait for those few ten seconds.</p>

---

## Post #3 by @jsalas424 (2020-11-28 16:57 UTC)

<p>Thank you for the clarification! I feel like your point that re-initializing the window leads to issues later is rather important, is this documented elsewhere?</p>

---

## Post #4 by @lassoan (2020-11-28 18:33 UTC)

<p>The issue is mostly that you don’t get notifications about extension installation completion and the first extension manager window popping up when you close the application. None of these are not serious issues, the extension manager still works, just behaves inconsistently. I’m not sure if it is worth documenting. Have you tried to read the documentation when you encountered the problem? What pages did you visit?</p>

---

## Post #5 by @jsalas424 (2020-11-28 18:57 UTC)

<p>Good to know it’s not too serious then. I have not run into follow up issues with the extension manager, just thought I’d report an odd behavior.</p>

---

## Post #6 by @lassoan (2020-11-28 19:01 UTC)

<p>Thanks for reporting (and please keep reporting if you find any issues). The fix did not make it into the current stable release, but will be included in the next one.</p>

---
