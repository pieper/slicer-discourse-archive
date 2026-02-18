# How to observe save button event

**Topic ID**: 39498
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/how-to-observe-save-button-event/39498

---

## Post #1 by @Cavers_Chen (2024-10-02 17:23 UTC)

<p>Hi!<br>
I am writing a Python script and encountered a problem recently. I want to save a specific component’s data through MRMLTextnode. However, I need to update and write them into the MRMLTextnode before users open the save dialog.</p>
<p>Is there a way to observe the Save Scene and Unsaved Data button event?</p>

---

## Post #2 by @lassoan (2024-10-02 17:28 UTC)

<p>You can override the default scene save dialog as shown in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#override-default-scene-save-dialog">example in the script repository</a>.</p>

---

## Post #3 by @Cavers_Chen (2024-10-07 16:30 UTC)

<p>Hi, I added this module to my code, but it doesn’t seem to work. When I click the save button, there is no output in the console. Should I register it?</p>
<pre><code class="lang-auto">import os

import vtk

import slicer, qt
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

class MyModuleFileDialog ():
  """This specially named class is detected by the scripted loadable
  module and is the target for optional drag and drop operations.
  See: Base/QTGUI/qSlicerScriptedFileDialog.h.

  This class is used for overriding default scene save dialog
  with simple saving the scene without asking anything.
  """

  def __init__(self,qSlicerFileDialog ):
    self.qSlicerFileDialog = qSlicerFileDialog
    qSlicerFileDialog.fileType = "NoFile"
    qSlicerFileDialog.description = "Save scene"
    qSlicerFileDialog.action = slicer.qSlicerFileDialog.Write

  def execDialog(self):
    # Implement custom scene save operation here.
    # Return True if saving completed successfully,
    # return False if saving was cancelled.
    print("hello")
    return True
  
  
#
# BCMaker
#
....
</code></pre>

---

## Post #4 by @lassoan (2024-10-23 19:22 UTC)

<p>The class must be called <code>(YourModuleName)FileDialog</code>, for example in your case something like <code>BCMakerFileDialog</code>.</p>

---
