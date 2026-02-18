# One viewer per image + segmentation

**Topic ID**: 35059
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/one-viewer-per-image-segmentation/35059

---

## Post #1 by @rkraaijveld (2024-03-25 15:49 UTC)

<p>Hi!</p>
<p>I have three separate images with corresponding segmentations and colour tables. I want to  make three viewers, viewing the image in an axial direction.</p>
<p>Until now, I’m able to get one image in each viewer, but the image+segmentation in each viewer has been unsuccessful, also in axial orientation. Can anyone help?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2024-03-25 15:51 UTC)

<p>You can look at the <a href="https://slicer.readthedocs.io/en/5.6/user_guide/modules/comparevolumes.html">CompareVolume</a> logic for ideas.  It does some of what you describe but doesn’t handle segmentations explicitly.</p>

---

## Post #3 by @rkraaijveld (2024-03-25 16:15 UTC)

<p>Hi! Thanks for such a quick response!</p>
<p>I looked into that but for some reason all my segmentations are still visibly in each viewer. I tried to do something like this but it didnt work:</p>
<pre><code>#put one of the volumes into each view, or none if it should be blank
sliceNodesByViewName = {}
layoutManager = slicer.app.layoutManager()

for index in range(len(actualViewNames)):
  viewName = actualViewNames[index]
  try:
    volumeNodeID = volumeNodes[index].GetID()
    segNodeID = label[index].GetID()
  except IndexError:
    volumeNodeID = ""

  sliceWidget = layoutManager.sliceWidget(viewName)
  compositeNode = sliceWidget.mrmlSliceCompositeNode()
  

  if label:
    compositeNode.SetBackgroundVolumeID(volumeNodeID)
    compositeNode.SetLabelVolumeID(segNodeID)
    
  else:
    compositeNode.SetBackgroundVolumeID(volumeNodeID)

  sliceNode = sliceWidget.mrmlSliceNode()
  sliceNode.SetOrientation(orientation)
  sliceNodesByViewName[viewName] = sliceNode
</code></pre>

---

## Post #4 by @rkraaijveld (2024-03-25 16:27 UTC)

<p>I wanted to start over, so this is what I have at the moment:</p>
<p>slicer.mrmlScene.Clear(0)<br>
# Reset the slice views to clear any remaining segmentations<br>
file_path = self.nifti_files[self.current_index]</p>
<pre><code>    self.volume0_node = slicer.util.loadVolume(file_path[0]["image"])
    self.volume1_node = slicer.util.loadVolume(file_path[1]["image"])
    self.volume2_node = slicer.util.loadVolume(file_path[2]["image"])

    self.label0_node = slicer.util.loadColorTable(file_path[0]["label"])
    self.label1_node = slicer.util.loadColorTable(file_path[1]["label"])
    self.label2_node = slicer.util.loadColorTable(file_path[2]["label"])

    self.segmentation0_node = slicer.util.loadSegmentation(file_path[0]["segmentation"], {'colorNodeID': self.label0_node.GetID()})
    self.segmentation1_node = slicer.util.loadSegmentation(file_path[1]["segmentation"], {'colorNodeID': self.label1_node.GetID()})
    self.segmentation2_node = slicer.util.loadSegmentation(file_path[2]["segmentation"], {'colorNodeID': self.label2_node.GetID()})

    sliceNodes = slicer.util.getNodes('vtkMRMLSliceNode*')

    layoutManager = slicer.app.layoutManager()
    sliceWidget = layoutManager.sliceWidget('Red')
    sliceNode = sliceWidget.mrmlSliceNode()
    sliceNode.SetOrientation('Axial')
    compositeNode = sliceWidget.mrmlSliceCompositeNode()
    compositeNode.SetBackgroundVolumeID(self.volume0_node.GetID())
    compositeNode.SetLabelVolumeID(self.segmentation0_node.GetID())

    layoutManager = slicer.app.layoutManager()
    sliceWidget = layoutManager.sliceWidget('Green')
    sliceNode = sliceWidget.mrmlSliceNode()
    sliceNode.SetOrientation('Axial')
    compositeNode = sliceWidget.mrmlSliceCompositeNode()
    compositeNode.SetBackgroundVolumeID(self.volume1_node)
    compositeNode.SetLabelVolumeID(self.segmentation1_node)

    layoutManager = slicer.app.layoutManager()
    sliceWidget = layoutManager.sliceWidget('Yellow')
    sliceNode = sliceWidget.mrmlSliceNode()
    sliceNode.SetOrientation('Axial')
    compositeNode = sliceWidget.mrmlSliceCompositeNode()
    compositeNode.SetBackgroundVolumeID(self.volume2_node)
    compositeNode.SetLabelVolumeID(self.segmentation2_node)

    slicer.util.resetSliceViews()
</code></pre>

---

## Post #5 by @pieper (2024-03-25 19:03 UTC)

<p>Segmentations aren’t managed by the <code>vtkMRMLSliceCompositeNode</code> so you need to manage their visibility using the list of view node ids in their display nodes, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-point-list-display-properties">something like this</a>.</p>

---
