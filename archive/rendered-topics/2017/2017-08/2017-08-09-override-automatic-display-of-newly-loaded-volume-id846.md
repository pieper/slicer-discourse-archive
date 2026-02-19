---
topic_id: 846
title: "Override Automatic Display Of Newly Loaded Volume"
date: 2017-08-09
url: https://discourse.slicer.org/t/846
---

# Override automatic display of newly-loaded volume?

**Topic ID**: 846
**Date**: 2017-08-09
**URL**: https://discourse.slicer.org/t/override-automatic-display-of-newly-loaded-volume/846

---

## Post #1 by @mschumaker (2017-08-09 14:00 UTC)

<p>Writing my first module.<br>
When I use the DICOM widget to load an image set, and use a qMRMLNodeComboBox, the newly-loaded node is automatically displayed in the Red, Yellow, and Green MRML slice views. I’m hoping to override this action, so that the newly-loaded volume is only displayed in either (but only one of) the Red or Yellow view. How would I do that? Thanks.<br>
Code is below:</p>
<pre><code>def setup(self):
    ScriptedLoadableModuleWidget.setup(self)

    #Link to image database for SSFP
    self.LoadSSFPButton = qt.QPushButton("Load SSFP Image Series")
    self.LoadSSFPButton.toolTip = "Select the SSFP image series from the image database"
    self.LoadSSFPButton.enabled = True
    self.layout.addWidget(self.LoadSSFPButton)

    # SSFP volume selector
    self.SSFPSelector = slicer.qMRMLNodeComboBox()
    self.SSFPSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
    self.SSFPSelector.selectNodeUponCreation = True
    self.SSFPSelector.addEnabled = False
    self.SSFPSelector.removeEnabled = False
    self.SSFPSelector.noneEnabled = False
    self.SSFPSelector.showHidden = False
    self.SSFPSelector.showChildNodeTypes = False
    self.SSFPSelector.setMRMLScene( slicer.mrmlScene )
    self.addRow("SSFP Image Volume: ", self.SSFPSelector)

    #Connections
    self.LoadSSFPButton.connect('clicked()', self.loadImageSeriesClicked)
    self.SSFPSelector.connect("currentNodeChanged(bool)", self.onSSFPSelect)

def loadImageSeriesClicked(self):
    slicer.modules.dicom.widgetRepresentation()
    slicer.modules.DICOMWidget.enter()</code></pre>

---

## Post #2 by @cpinter (2017-08-09 14:26 UTC)

<p>This a really good question. After taking a quick look, I think the DoPropagateVolumeSelection member in vtkMRMLSliceCompositeNode is just to do this. A code snippet about how to access the node and set the flag. Of course you will want to do it differently, not iterating over all 2D views.</p>
<pre><code>  layoutManager = slicer.app.layoutManager()
  sliceWidgetNames = ['Red', 'Green', 'Yellow']
  for sliceWidgetName in sliceWidgetNames:
    slice = layoutManager.sliceWidget(sliceWidgetName)
    if slice is None:
      continue
    sliceLogic = slice.sliceLogic()
    compositeNode = sliceLogic.GetSliceCompositeNode()
    compositeNode.SetDoPropagateVolumeSelection(False)</code></pre>

---

## Post #3 by @mschumaker (2017-08-09 20:52 UTC)

<p>Excellent, thank you! That worked well.</p>

---
