---
topic_id: 11347
title: "Help For Perklabs Programming Example"
date: 2020-04-29
url: https://discourse.slicer.org/t/11347
---

# Help for PerkLab's programming example

**Topic ID**: 11347
**Date**: 2020-04-29
**URL**: https://discourse.slicer.org/t/help-for-perklabs-programming-example/11347

---

## Post #1 by @mau_igna_06 (2020-04-29 13:17 UTC)

<p>Hi, I have followed this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true" rel="nofollow noopener">tutorial</a> . I have finished the code for the proposed exercise: “getting a sphere between two fiducial points”. The problem is know how to write the code to get the sphere between the two fiducials but I don’t know in which class or position of the class to append my code. (I wrote “Added by me” everywhere I made a change to the original example-code to make it more searchable)</p>
<p>import os<br>
import unittest<br>
import vtk, qt, ctk, slicer<br>
from slicer.ScriptedLoadableModule import *<br>
import logging</p>
<h1></h1>
<h1>ModuleOne</h1>
<h1></h1>
<p>class ModuleOne(ScriptedLoadableModule):<br>
“”“Uses ScriptedLoadableModule base class, available at:<br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</a><br>
“””</p>
<p>def <strong>init</strong>(self, parent):<br>
ScriptedLoadableModule.<strong>init</strong>(self, parent)<br>
self.parent.title = “ModuleOne” # TODO make this more human readable by adding spaces<br>
self.parent.categories = [“Examples”]<br>
self.parent.dependencies = []<br>
self.parent.contributors = [“John Doe (AnyWare Corp.)”] # replace with “Firstname Lastname (Organization)”<br>
self.parent.helpText = “”"<br>
This is an example of scripted loadable module bundled in an extension.<br>
It performs a simple thresholding on the input volume and optionally captures a screenshot.<br>
“”"<br>
self.parent.helpText += self.getDefaultModuleDocumentationLink()<br>
self.parent.acknowledgementText = “”"<br>
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc.<br>
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.<br>
“”" # replace with organization, grant and thanks.</p>
<h1></h1>
<h1>ModuleOneWidget</h1>
<h1></h1>
<p>class ModuleOneWidget(ScriptedLoadableModuleWidget):<br>
“”“Uses ScriptedLoadableModuleWidget base class, available at:<br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</a><br>
“””</p>
<p>def setup(self):<br>
ScriptedLoadableModuleWidget.setup(self)</p>
<pre><code># Load widget from .ui file (created by Qt Designer)
uiWidget = slicer.util.loadUI(self.resourcePath('UI/ModuleOne.ui'))
self.layout.addWidget(uiWidget)
self.ui = slicer.util.childWidgetVariables(uiWidget)

self.ui.inputSelector.setMRMLScene(slicer.mrmlScene)
self.ui.outputSelector.setMRMLScene(slicer.mrmlScene)

# connections
self.ui.applyButton.connect('clicked(bool)', self.onApplyButton)
self.ui.inputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
self.ui.outputSelector.connect("currentNodeChanged(vtkMRMLNode*)", self.onSelect)
#Added by me
self.observedMarkupNode = None
self.markupsObserverTag = None
self.ui.enableScreenshotsFlagCheckBox.connect("toggled(bool)", self.onEnableAutoUpdate)

# Add vertical spacer
self.layout.addStretch(1)

# Refresh Apply button state
self.onSelect()

#Added by me
self.a = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode","sphere")
self.m = vtk.vtkSphereSource()
self.m.Update()
self.a.SetAndObservePolyData(self.m.GetOutput())
</code></pre>
<p>def cleanup(self):<br>
pass</p>
<p>def onSelect(self):<br>
self.ui.applyButton.enabled = self.ui.inputSelector.currentNode()</p>
<p>def onEnableAutoUpdate(self, autoUpdate):<br>
if self.markupsObserverTag:<br>
self.observedMarkupNode.RemoveObserver(self.markupsObserverTag)<br>
self.observedMarkupNode = None<br>
self.markupsObserverTag = None<br>
if autoUpdate and self.ui.inputSelector.currentNode:<br>
self.observedMarkupNode = self.ui.inputSelector.currentNode()<br>
self.markupsObserverTag = self.observedMarkupNode.AddObserver(<br>
vtk.vtkCommand.ModifiedEvent, self.onMarkupsUpdated)</p>
<p>def onMarkupsUpdated(self, caller=None, event=None):<br>
self.onApplyButton()</p>
<p>def onApplyButton(self):<br>
logic = ModuleOneLogic()<br>
enableScreenshotsFlag = self.ui.enableScreenshotsFlagCheckBox.checked<br>
imageThreshold = self.ui.imageThresholdSliderWidget.value<br>
logic.run(self.ui.inputSelector.currentNode(), self.ui.outputSelector.currentNode(), imageThreshold, enableScreenshotsFlag)<br>
<span class="hashtag">#Added</span> by me<br>
self.m.Update()</p>
<h1></h1>
<h1>ModuleOneLogic</h1>
<h1></h1>
<p>class ModuleOneLogic(ScriptedLoadableModuleLogic):<br>
“”“This class should implement all the actual<br>
computation done by your module.  The interface<br>
should be such that other python code can import<br>
this class and make use of the functionality without<br>
requiring an instance of the Widget.<br>
Uses ScriptedLoadableModuleLogic base class, available at:<br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</a><br>
“””</p>
<p>def hasImageData(self,volumeNode):<br>
“”“This is an example logic method that<br>
returns true if the passed in volume<br>
node has valid image data<br>
“””<br>
if not volumeNode:<br>
logging.debug(‘hasImageData failed: no volume node’)<br>
return False<br>
if volumeNode.GetImageData() is None:<br>
logging.debug(‘hasImageData failed: no image data in volume node’)<br>
return False<br>
return True</p>
<p>def isValidInputOutputData(self, inputVolumeNode, outputVolumeNode):<br>
“”“Validates if the output is not the same as input<br>
“””<br>
if not inputVolumeNode:<br>
logging.debug(‘isValidInputOutputData failed: no input volume node defined’)<br>
return False<br>
if not outputVolumeNode:<br>
logging.debug(‘isValidInputOutputData failed: no output volume node defined’)<br>
return False<br>
if inputVolumeNode.GetID()==outputVolumeNode.GetID():<br>
logging.debug(‘isValidInputOutputData failed: input and output volume is the same. Create a new volume for output to avoid this error.’)<br>
return False<br>
return True</p>
<p><span class="hashtag">#Added</span> by me<br>
def setSphereRadiusAndCenter(r,c):<br>
self.m = vtk.vtkSphereSource()<br>
self.m.SetRadius®<br>
self.m.SetCenter(c[0],c[1],c[2])<br>
self.m.Update()<br>
return</p>
<p>def setSphereTouchingFiducials(self):<br>
import numpy<br>
f = slicer.util.getNode(‘F’)<br>
pos0 = [0,0,0]<br>
pos1 = [0,0,0]<br>
if f.GetNumberOfMarkups() == 2:<br>
f.GetNthFiducialPosition(0,pos0)<br>
f.GetNthFiducialPosition(1,pos1)<br>
p0 = numpy.array(pos0)<br>
p1 = numpy.array(pos1)<br>
radius = numpy.linalg.norm(p0-p1)/2.0<br>
center = (p0+p1)/2.0<br>
self.setSphereRadiusAndCenter(radius,center)<br>
else:<br>
logging.info(‘Error: Incorrect number of fiducial points’)</p>
<p>def run(self, inputVolume, outputVolume, imageThreshold, enableScreenshots=0):<br>
“”"<br>
Run the actual algorithm<br>
“”"<br>
self.setSphereTouchingFiducials()</p>
<pre><code>return True
</code></pre>
<p>class ModuleOneTest(ScriptedLoadableModuleTest):<br>
“”"<br>
This is the test case for your scripted module.<br>
Uses ScriptedLoadableModuleTest base class, available at:<br>
<a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</a><br>
“”"</p>
<p>def setUp(self):<br>
“”" Do whatever is needed to reset the state - typically a scene clear will be enough.<br>
“”"<br>
slicer.mrmlScene.Clear(0)</p>
<p>def runTest(self):<br>
“”“Run as few or as many tests as needed here.<br>
“””<br>
self.setUp()<br>
self.test_ModuleOne1()</p>
<p>def test_ModuleOne1(self):<br>
“”" Ideally you should have several levels of tests.  At the lowest level<br>
tests should exercise the functionality of the logic with different inputs<br>
(both valid and invalid).  At higher levels your tests should emulate the<br>
way the user would interact with your code and confirm that it still works<br>
the way you intended.<br>
One of the most important features of the tests is that it should alert other<br>
developers when their changes will have an impact on the behavior of your<br>
module.  For example, if a developer removes a feature that you depend on,<br>
your test should break so they know that the feature is needed.<br>
“”"</p>
<pre><code>self.delayDisplay("Starting the test")
#
# first, get some data
#
import SampleData
SampleData.downloadFromURL(
  nodeNames='FA',
  fileNames='FA.nrrd',
  uris='http://slicer.kitware.com/midas3/download?items=5767')
self.delayDisplay('Finished with download and loading')

volumeNode = slicer.util.getNode(pattern="FA")
logic = ModuleOneLogic()
self.assertIsNotNone( logic.hasImageData(volumeNode) )
self.delayDisplay('Test passed!')</code></pre>

---

## Post #2 by @mau_igna_06 (2020-04-29 17:03 UTC)

<p>Maybe someone can post the code of the solution to the exercise if reading the code above is too much work</p>

---

## Post #3 by @lassoan (2020-04-29 20:53 UTC)

<p>The solution is posted in the same repository.</p>

---

## Post #4 by @mau_igna_06 (2020-04-30 16:50 UTC)

<p>Hi Andras. The task is given on page 47 of <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx" rel="nofollow noopener">the tutorial</a> and there is no solution there. I also searched <a href="https://github.com/PerkLab/PerkLabBootcamp/tree/master/Doc" rel="nofollow noopener">here</a> with no results. Could you post the link to the solution?</p>

---

## Post #5 by @lassoan (2020-04-30 17:11 UTC)

<p>All information that is needed to create the module is in the slides and students develop their module on their own, and I have just discovered that we stopped providing a “solution” 3 years ago. You can download that old solution (using old templates, does not leverage recent Slicer features, etc.) <a href="https://1drv.ms/u/s!Arm_AFxB9yqHr7clmSSvwLxVByo6EQ?e=lLqJdr">here</a>.</p>

---
