# OpenCad 3D Slicer - Breast DCE MRI

**Topic ID**: 5172
**Date**: 2018-12-22
**URL**: https://discourse.slicer.org/t/opencad-3d-slicer-breast-dce-mri/5172

---

## Post #1 by @fitouss (2018-12-22 19:48 UTC)

<p>Hello,</p>
<p>I’m new with 3D slicer.</p>
<p>I have a problem on SegmentCad on 3d Slicer with the last step of the tutorial <a href="https://www.slicer.org/w/images/d/d2/SegmentCADTutorial.pptx" rel="noopener nofollow ugc">https://www.slicer.org/w/images/d/d2/SegmentCADTutorial.pptx</a> (page 20)</p>
<p>When i try to generate the “SegmentCADLabelMap”, nothing happens.<br>
This appears in Log messages :</p>
<blockquote>
<p>" Traceback (most recent call last):<br>
File "/Applications/Slicer.app/Contents/Extensions-27618/OpenCAD/lib/Slicer-4.11/qt-scripted-modules/SegmentCAD.py", line 619, in onSegmentCADButtonClicked<br>
self.logic.renderLabelMap()<br>
File "/Applications/Slicer.app/Contents/Extensions-27618/OpenCAD/lib/Slicer-4.11/qt-scripted-modules/SegmentCADLogic/SegmentCADLogic.py", line 112, in renderLabelMap<br>
SegmentCADLabelMapImageData.SetScalarTypeToShort()<br>
AttributeError: ‘vtkCommonDataModelPython.vtkImageData’ object has no attribute ‘SetScalarTypeToShort’ "</p>
</blockquote>
<p>I don’t understand the problem and i didn’t find any explanation.</p>
<p>I’m on Mac Os 10.11.6 and Slicer 4.11.0-2018-12-08 r27618.</p>
<p>Thanks for your returns.</p>
<p>Alex</p>

---

## Post #2 by @pieper (2018-12-22 20:13 UTC)

<p><a class="mention" href="/u/jayender">@jayender</a> may be able to help -  it looks like this module hasn’t been ported to the latest VTK.</p>

---

## Post #3 by @lassoan (2018-12-23 04:37 UTC)

<p>I’ve submitted a pull request with the fix.</p>
<p>Until the fix gets integrated (it may take a couple of days), you can replace your SegmentCADLogic.py file by this updated version: <a href="https://github.com/lassoan/Slicer-OpenCAD/blob/master/SegmentCAD/SegmentCADLogic/SegmentCADLogic.py" rel="nofollow noopener">https://github.com/lassoan/Slicer-OpenCAD/blob/master/SegmentCAD/SegmentCADLogic/SegmentCADLogic.py</a></p>

---

## Post #4 by @fitouss (2018-12-23 07:41 UTC)

<p>Thanks for your fast answer,  it’s working <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #5 by @lassoan (2018-12-23 13:01 UTC)

<p>Let us know if you find the module useful.</p>
<p>To make it nicer and more easily usable with current Slicer, it should be updated to use new plot infrastructure (instead of legacy charts), segmentations (in addition to simple labelmap), and sequences (in addition to multi-volume). However, we would only do this if there is strong enough user need.</p>

---

## Post #6 by @fitouss (2018-12-23 14:18 UTC)

<p>The module is useful, and important for practice i think (MRI Breast ++).<br>
Something similar is used where i’m working currently.<br>
I’m going to compare and see if it can be used in routine.</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @malcolmlim (2022-03-15 05:48 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>, i’m sorry for reviving this old post but i’m having similar issues.</p>
<p>I downloaded OpenCad extension and am at the final steps of  “Tumor Segmentation from DCE-MRI with the SegmentCAD module training” when this log message came up:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/uqmlim3/AppData/Roaming/NA-MIC/Extensions-28257/OpenCAD/lib/Slicer-4.10/qt-scripted-modules/SegmentCAD.py”, line 619, in onSegmentCADButtonClicked<br>
self.logic.renderLabelMap()<br>
File “C:\Users\uqmlim3\AppData\Roaming\NA-MIC\Extensions-28257\OpenCAD\lib\Slicer-4.10\qt-scripted-modules\SegmentCADLogic\SegmentCADLogic.py”, line 112, in renderLabelMap<br>
SegmentCADLabelMapImageData.SetScalarTypeToShort()<br>
AttributeError: ‘vtkCommonDataModelPython.vtkImageData’ object has no attribute ‘SetScalarTypeToShort’</p>
<p>I tried to follow your remedy, but I am not sure how to replace the ‘SegmentCADLogic.py’ with your fixed version. I tried searching for ‘SegmentCADlogic’ in Slicer 4.10.2 Folder but nothing comes up. I see other .py files but no SegmentCADlogic, as such am at the limit of my abilites. Can you enlighten on how do i go about getting this fix please?</p>

---
