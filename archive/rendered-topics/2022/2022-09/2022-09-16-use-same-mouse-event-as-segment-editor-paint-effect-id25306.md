# Use same mouse event as segment editor paint effect

**Topic ID**: 25306
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/use-same-mouse-event-as-segment-editor-paint-effect/25306

---

## Post #1 by @SCY (2022-09-16 13:44 UTC)

<p>Hello everyone,</p>
<p>I used vtkcommand mouse events with the interactor style of three render windows (Red, Green, and Yellow). These mouse events triggered my custom callback functions. Everything worked until I add the segment editor widget and active paint effect. In the code, I added observers to the vtkInteractorStyle object after I activated the paint effect.</p>
<p>Expect to see: Both the paint effect and my callback functions work simultaneously.<br>
Actually see: Only the paint effect and the callback function connected with leftbuttonrelease were called when I double-clicked on the render window.</p>
<p>Some thought:<br>
In the paint effect, it uses the same mouse events as well. This might cause a problem.</p>
<p>Already tried:</p>
<ol>
<li>Set the priority of my observers to 2.0</li>
<li>Add observers before activating the paint effect</li>
<li>Move my observers and callback functions to another thread</li>
</ol>
<p>Thank you for any help and insight into the reasons behind this.</p>

---

## Post #2 by @lassoan (2022-09-16 21:00 UTC)

<p>If you want to hijack events from the Segment Editor then you need to specify an observer with high priority and return with 0 from your event callback function (which means that the event is not aborted but other observers get a chance to process it).</p>

---

## Post #3 by @SCY (2022-09-19 07:56 UTC)

<p>In qMRMLSegmentEditorWidget.cxx, it sets the priority of the observers to 1.0 in setupViewObservations(). I set mine to any number larger than 1.0 but it still couldn’t hijack the events from the Segment Editor.</p>

---

## Post #4 by @lassoan (2022-09-19 13:52 UTC)

<p>Could you send a link to the source code of your module or send a standalone Python code snippet that reproduces the behavior?</p>

---

## Post #6 by @lassoan (2022-09-19 20:50 UTC)

<p>Please provide code that I can copy-paste into the Python console in Slicer and you would expect to work.</p>

---

## Post #7 by @SCY (2022-09-19 22:17 UTC)

<pre><code class="lang-auto">import logging
import slicer
import vtk
import SampleData

def onPress(arg1, arg2):
    logging.info("Press")

def onRelease(arg1, arg2):
    logging.info("Release")

lm = slicer.app.layoutManager()
rw = lm.sliceWidget("Red").sliceView().renderWindow()
style = rw.GetInteractor().GetInteractorStyle()

style.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, onPress, 10.0)
style.AddObserver(vtk.vtkCommand.LeftButtonReleaseEvent, onRelease, 10.0)

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Run segmentation
segmentEditorWidget.setActiveEffectByName("Paint")
</code></pre>
<p>After activating the paint effect, onPress isn’t called when left button is pressed, and onRelease is called when left button is double clicked.</p>
<p>Thank you for your help!</p>

---

## Post #8 by @SCY (2022-09-25 09:15 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, do you have any idea about this? Any thoughts would be helpful. Thank you!</p>

---

## Post #9 by @lassoan (2022-09-28 04:05 UTC)

<p>Thank you, the script was very helpful. It was almost perfect, the only mistake was that the observer was added to the interactor style, while it should have been added to the interactor (because the interactor style only invokes event if the event is not processed):</p>
<pre><code class="lang-python">import logging
import slicer
import vtk
import SampleData

def onPress(arg1, arg2):
    logging.info("Press")

def onRelease(arg1, arg2):
    logging.info("Release")

lm = slicer.app.layoutManager()

interactor = lm.sliceWidget("Red").sliceView().interactorStyle().GetInteractor()
interactor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent, onPress, 10.0)
interactor.AddObserver(vtk.vtkCommand.LeftButtonReleaseEvent, onRelease, 10.0)

# Load master volume
sampleDataLogic = SampleData.SampleDataLogic()
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()

# Create segmentation
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Run segmentation
segmentEditorWidget.setActiveEffectByName("Paint")
</code></pre>

---

## Post #10 by @SCY (2022-09-29 12:36 UTC)

<p>It works. Thank you for the solution!</p>

---
