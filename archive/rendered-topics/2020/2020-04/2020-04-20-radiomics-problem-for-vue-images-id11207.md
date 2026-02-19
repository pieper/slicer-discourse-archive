---
topic_id: 11207
title: "Radiomics Problem For Vue Images"
date: 2020-04-20
url: https://discourse.slicer.org/t/11207
---

# Radiomics problem for VUE images

**Topic ID**: 11207
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/radiomics-problem-for-vue-images/11207

---

## Post #1 by @aileeno (2020-04-20 15:15 UTC)

<p>Operating system: macOS Catalina<br>
Slicer version: 4.10.2<br>
Expected behavior: extract radiomics features from a label map created from a virtual unenhanced CT (dual energy)<br>
Actual behavior: No features extracted, following errors returned</p>
<p>Python 2.7.13 (default, May 16 2019, 14:32:14)<br>
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Loading with imageIOName: GDCM<br>
Generating customization file<br>
Feature extraction started<br>
Initializing output table<br>
Feature calculation failed.<br>
Feature calculation failed.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 407, in onApplyButton<br>
self.onFinished)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 743, in runCLI<br>
self.runCLIWithParameterFile(imageNode, maskNode, tableNode, parameterFile, callback)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 782, in runCLIWithParameterFile<br>
self._startCLI(firstRun=True)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 537, in _startCLI<br>
labelName, labelNode, label_idx, imageNode = next(self._labelGenerators)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 494, in _getLabelGeneratorFromLabelMap<br>
combinedLabelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(labelNode.GetName()))<br>
File “/Applications/Slicer.app/Contents/bin/Python/sitkUtils.py”, line 44, in GetSlicerITKReadWriteAddress<br>
myNode = nodeObjectOrName if isinstance(nodeObjectOrName, slicer.vtkMRMLNode) else slicer.util.getNode(nodeObjectOrName)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 710, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (type(pattern) == str) else “”))<br>
MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘304: VNC [HU*] , VNC, Spectral (3)-label’</p>

---

## Post #2 by @lassoan (2020-04-20 15:16 UTC)

<p>Can you try if removing the <code>*</code> character from the node name fixes the issue?</p>

---

## Post #3 by @aileeno (2020-04-20 16:26 UTC)

<p>I have removed the * in the hierarchy details, however I still get these error messages</p>
<p>Python 2.7.13 (default, May 16 2019, 14:32:14)<br>
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>Loading with imageIOName: GDCM<br>
Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 1.2207e-05 mm, tolerance threshold is 0.001 mm).<br>
Generating customization file<br>
Feature extraction started<br>
Initializing output table<br>
Feature calculation failed.<br>
Feature calculation failed.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 407, in onApplyButton<br>
self.onFinished)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 743, in runCLI<br>
self.runCLIWithParameterFile(imageNode, maskNode, tableNode, parameterFile, callback)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 782, in runCLIWithParameterFile<br>
self._startCLI(firstRun=True)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 537, in _startCLI<br>
labelName, labelNode, label_idx, imageNode = next(self._labelGenerators)<br>
File “/Applications/Slicer.app/Contents/Extensions-28257/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 494, in _getLabelGeneratorFromLabelMap<br>
combinedLabelImage = sitk.ReadImage(sitkUtils.GetSlicerITKReadWriteAddress(labelNode.GetName()))<br>
File “/Applications/Slicer.app/Contents/bin/Python/sitkUtils.py”, line 44, in GetSlicerITKReadWriteAddress<br>
myNode = nodeObjectOrName if isinstance(nodeObjectOrName, slicer.vtkMRMLNode) else slicer.util.getNode(nodeObjectOrName)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 710, in getNode<br>
raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (type(pattern) == str) else “”))<br>
MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘304: VNC [HU] , VNC, Spectral (3)-label’</p>

---

## Post #4 by @pieper (2020-04-20 17:01 UTC)

<p>The square brackets around HU are also a problem for that method.  Try taking those out too and let us know.</p>
<p>Thanks for reporting this - it looks like <a href="https://github.com/Radiomics/SlicerRadiomics/pull/60">one small change</a> should fix the problem.</p>

---

## Post #5 by @aileeno (2020-04-20 18:28 UTC)

<p>works perfectly now, thanks so much <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---
