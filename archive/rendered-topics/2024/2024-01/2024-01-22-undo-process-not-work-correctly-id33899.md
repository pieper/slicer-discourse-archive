# Undo process not work correctly

**Topic ID**: 33899
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/undo-process-not-work-correctly/33899

---

## Post #1 by @park (2024-01-22 07:37 UTC)

<p>Hi all</p>
<p>I am currently testing undo/redo process using “SetUndoEnabled”</p>
<p>I checked that the function works well when there is only one markups ground, but it malfunctions when there are two or more groups, as shown in the video below.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/133ae4e6e1b4e7d6aea723fd2699858d25d89e5c.mp4">
  </div><p></p>
<p>Also, the undo function does not work in “vtkMRMLModelNode”. Do I need to add “SaveStateForUndo” to the Slicer Model source code and rebuild to address this issue?</p>
<p>My codes in “.slicerry.py” looks like below.</p>
<pre><code class="lang-auto"> slicer.mrmlScene.SetUndoOn()

undoEnabledNodeClassNames = [
  "vtkMRMLMarkupsFiducialNode",
  "vtkMRMLMarkupsLineNode",
  "vtkMRMLMarkupsAngleNode",
  "vtkMRMLMarkupsCurveNode",
  "vtkMRMLMarkupsClosedCurveNode",
  "vtkMRMLMarkupsPlaneNode",
  "vtkMRMLMarkupsROINode",
  "vtkMRMLModelNode",
  "vtkMRMLScalarVolumeNode",
  "vtkMRMLLinearTransformNode",
  ]
for className in undoEnabledNodeClassNames:
  node = slicer.mrmlScene.CreateNodeByClass(className)
  node.SetUndoEnabled(True)
  slicer.mrmlScene.AddDefaultNode(node)

def onRedo():
  slicer.mrmlScene.Redo()

def onUndo():
  slicer.mrmlScene.Undo()

redoShortcuts = []
redoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Redo)
for redoBinding in redoKeyBindings:
  redoShortcut = qt.QShortcut(slicer.util.mainWindow())
  redoShortcut.setKey(redoBinding)
  redoShortcut.connect("activated()", onRedo)
  redoShortcuts.append(redoShortcut)

undoShortcuts = []
undoKeyBindings = qt.QKeySequence.keyBindings(qt.QKeySequence.Undo)
for undoBinding in undoKeyBindings:
  undoShortcut = qt.QShortcut(slicer.util.mainWindow())
  undoShortcut.setKey(undoBinding)
  undoShortcut.connect("activated()", onUndo)
  undoShortcuts.append(undoShortcut)

toolBar = qt.QToolBar("Undo/Redo")
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerUndo.png"), "Undo", onUndo)
toolBar.addAction(qt.QIcon(":/Icons/Medium/SlicerRedo.png"), "Redo", onRedo)
slicer.util.mainWindow().addToolBar(toolBar)
</code></pre>

---

## Post #2 by @pieper (2024-01-22 20:59 UTC)

<p>Yes, that looks like the kind of situation that led us to disable it by default.  Probably there is a sequence of events triggered by other events that doesn’t unroll correctly, Some of the GUI/Logic code tracks changes in order to avoid completely re-syncing with the scene at every change and those efficiency heuristics can get disrupted by undo/redo.</p>
<p>What would help would be to try replicating the issue using a SelfTest, or better a set of SelfTests that are representative of how undo/redo should be working and seeing how things hold up.  That would form a basis for investigating the underlying issues (e.g. running the same tests with and without the GUI connected).</p>

---
