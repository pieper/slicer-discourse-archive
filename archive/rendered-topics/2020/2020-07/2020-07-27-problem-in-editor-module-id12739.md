# Problem in Editor module

**Topic ID**: 12739
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/problem-in-editor-module/12739

---

## Post #1 by @fpsiddiqui91 (2020-07-27 08:46 UTC)

<p>I am trying to build Slicer again in my windows machine. I have some problem in loading the editor module.  When I am switching to the Editor module, I am getting this error:</p>
<pre><code>Traceback (most recent call last):
  File "C:/D/S4R/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/Editor.py", line 247, in setup
    self.createEditBox()
  File "C:/D/S4R/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/Editor.py", line 287, in createEditBox
    self.toolsBox = EditorLib.EditBox(self.editBoxFrame, optionsFrame=self.effectOptionsFrame)
  File "C:\D\S4R\Slicer-build\lib\Slicer-4.11\qt-scripted-modules\EditorLib\EditBox.py", line 37, in __init__
    self.effectActionGroup.exclusive = True
AttributeError: 'exclusive' does not exist on QActionGroup and creating new attributes on C++ objects is not allowed
Traceback (most recent call last):
  File "C:/D/S4R/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/Editor.py", line 129, in enter
    self.installShortcutKeys()
  File "C:/D/S4R/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/Editor.py", line 98, in installShortcutKeys
    ('z', self.toolsBox.undoRedo.undo),
AttributeError: 'NoneType' object has no attribute 'undoRedo'
</code></pre>
<p>I think it is a small bug and fixable.<br>
Thank you</p>

---

## Post #2 by @pieper (2020-07-27 14:31 UTC)

<p>We’re not maintaining the legacy Editor module anymore, so hopefully you can switch your workflow to the Segment Editor.  Of course you may be correct that this is a small bug and if you find a fix it could make sense to merge it.</p>

---

## Post #3 by @lassoan (2020-07-27 15:45 UTC)

<p>Yes, in fact we are just working on removing the last few usages of Editor module in various extensions and if that happens (within a few days or worst case weeks) then the Editor module will not be available in Slicer-4.11 anymore. We are happy to help with porting any code that you have, optimizing your workflow or GUI for Segment Editor, just let us know what you need.</p>

---

## Post #4 by @fpsiddiqui91 (2020-07-27 15:59 UTC)

<p>Well I already have updated my code to use Segmentation module. However, DMRI extension still needs label map for running tractography seeding. Can we generate label map directly from segmentation?</p>

---

## Post #5 by @lassoan (2020-07-27 16:05 UTC)

<p>DMRI extension should be updated to also accept segmentation node as input. Which module is this?</p>
<p>As a workaround you can export segmentation to labelmap by right-clicking on it in Data module.</p>

---

## Post #6 by @fpsiddiqui91 (2020-07-28 08:35 UTC)

<p>In DMRI extension, its tractography seeding which accepts only label map.<br>
Yes, I already have converted it into label map but just for other users it would be better if they can directly use segmentation input in tractography module.</p>
<p>Thanks</p>

---

## Post #7 by @lassoan (2020-07-28 22:41 UTC)

<p>Which module do you use? “Tractography Interactive Seeding” or “Tractography ROI Seeding”?</p>
<p>How would you select multiple segments for seeds? Would using all visible segments work? Or would you like to display a segment list table where you can select multiple segments (similar to the one in Segmentations module)?</p>
<p>Probably the best would be to add an issue to <a href="https://github.com/SlicerDMRI/SlicerDMRI/issues">https://github.com/SlicerDMRI/SlicerDMRI/issues</a> and discuss it further there.</p>

---
