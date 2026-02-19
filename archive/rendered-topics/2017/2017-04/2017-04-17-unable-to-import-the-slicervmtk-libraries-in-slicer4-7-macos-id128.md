---
topic_id: 128
title: "Unable To Import The Slicervmtk Libraries In Slicer4 7 Macos"
date: 2017-04-17
url: https://discourse.slicer.org/t/128
---

# Unable to import the SlicerVmtk libraries` in	Slicer4.7, macOS

**Topic ID**: 128
**Date**: 2017-04-17
**URL**: https://discourse.slicer.org/t/unable-to-import-the-slicervmtk-libraries-in-slicer4-7-macos/128

---

## Post #1 by @lassoan (2017-04-17 13:28 UTC)

<p>I am using vmtk as an extension in 3D Slicer4.7. It works fine on Windows,<br>
but fails to import dynamic libraries in macOS by reporting <code>Unable to import the SlicerVmtk libraries</code>.</p>
<p><code>qt-scripted-modules</code> can be accessed, but <code>qt-loadable-modules</code> can not be<br>
found. It seems that rpath is incorrect. Anybody knows how to solve it?</p>
<p>Errors in Python interactor:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; [VMTK 04/17/2017 12:53:06] DEBUG: Starting Level Set Segmentation..
Unable to import the SlicerVmtk libraries
Traceback (most recent call last):
  File
"/Applications/Slicer.app/Contents/Extensions-25933/SlicerExtension-VMTK/lib/Slicer-4.7/qt-scripted-modules/LevelSetSegmentation.py",
line 342, in onRefreshButtonClicked
    self.start( True )
  File
"/Applications/Slicer.app/Contents/Extensions-25933/SlicerExtension-VMTK/lib/Slicer-4.7/qt-scripted-modules/LevelSetSegmentation.py",
line 622, in start
    'collidingfronts' ) )
  File
"/Applications/Slicer.app/Contents/Extensions-25933/SlicerExtension-VMTK/lib/Slicer-4.7/qt-scripted-modules/SlicerVmtkCommonLib/LevelSetSegmentationLogic.py",
line 64, in performInitialization
    collidingFronts =
vtkvmtkSegmentation.vtkvmtkCollidingFrontsImageFilter()
</code></pre>

---

## Post #2 by @lassoan (2017-04-17 13:30 UTC)

<p>Please try the latest nightly version.</p>

---
