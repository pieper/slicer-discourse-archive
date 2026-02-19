---
topic_id: 738
title: "Loading A Dicom And Changing It To Nrrd In The Background"
date: 2017-07-21
url: https://discourse.slicer.org/t/738
---

# Loading a DICOM and changing it to nrrd in the background

**Topic ID**: 738
**Date**: 2017-07-21
**URL**: https://discourse.slicer.org/t/loading-a-dicom-and-changing-it-to-nrrd-in-the-background/738

---

## Post #1 by @benwilk (2017-07-21 14:38 UTC)

<p>These functions allow you to load multivolume DICOM images and have slicer change them into .nrrd file format without any further user input. Certain modules will now be able to use the data directly. Currently it is set to specifically change vtkMRMLMultiVolumeNode1, so that may need to be modified.</p>
<pre><code>def loadDICOMButtonClicked(self):
    self.dicomDialog = DICOMLib.DICOMDetailsPopup()
    self.dicomDialog.loadButton.connect("clicked(bool)", self.onDicomLoaded)
    self.dicomDialog.open()

  def onDicomLoaded(self):
    self.dicomDialog.loadButton.disconnect('clicked(bool)', self.onDicomLoaded)
    node = slicer.mrmlScene.GetNodeByID('vtkMRMLMultiVolumeNode1')
    result = False
    tempName = next(tempfile._get_candidate_names())
    result = slicer.util.saveNode(node, tempfile.gettempdir() + '\\' + node.GetName() + '.nrrd')
    slicer.mrmlScene.RemoveNode(node.GetStorageNode())
    slicer.mrmlScene.RemoveNode(node.GetDisplayNode())
    slicer.mrmlScene.RemoveNode(node)
    props = {}
    props['fileName'] = tempfile.gettempdir() + '\\' + node.GetName() + '.nrrd'
    loadedNodes = vtk.vtkCollection()
    slicer.app.coreIOManager().loadNodes('Volume Sequence', props, loadedNodes)
    newNode = loadedNodes.GetItemAsObject(0)
</code></pre>
<p><a class="mention" href="/u/arankin">@arankin</a> got this working for me, so credit goes to him <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @adamrankin (2017-07-23 13:45 UTC)

<p>So after exploring the code for the DICOM widget, I found this:<br>
slicer.app.ioManager().emitNewFileLoaded(loadedFileParameters)</p>
<p>this means that you can catch the loaded nodes in the same way that I did the data catch here:<br>
<a href="https://github.com/adamrankin/SlicerTAVI/blob/master/ValvePlanning/ValvePlanning.py#L702" rel="nofollow noopener">https://github.com/adamrankin/SlicerTAVI/blob/master/ValvePlanning/ValvePlanning.py#L702</a></p>
<p>Only downside is that it only catches volumes, but this should be ok until someone needs another data type.</p>

---

## Post #3 by @lassoan (2017-07-23 14:00 UTC)

<p>Option A. I think the cleanest option would be to create a new DICOM reader plugin (that could use multi-volume logic to avoid code duplication). However, the disadvantage would be that the heuristic that iterates through the data in various ways is somewhat costly, so it may add a bit to the DICOM examination time.</p>
<p>Option B. Another good option that would avoid re-examining the data would be to improve the multi-volume DICOM plugin to offer loading volumes as Sequence nodes as well. There are still some features in multi-volume that are not available in Sequences, so for backward compatibility it may be better to load into multi-volumes by default. However, if we keep Sequences in a separate extension, then we could change the behavior so that if somebody installed Sequences extension then we would load volume sequence as Sequence node.</p>
<p>A bit of background info on how DICOM loading works.</p>
<ol>
<li>
<p>DICOM plugins are registered by Slicer core and extensions.</p>
</li>
<li>
<p>When a user opens DICOM browser and clicks on a patient/study/series and click Examine then DICOM plugins receive list of files to “examine”. Each plugin returns a list of “loadables” with some associated confidence value (determines how confident a plugin is that that loadable is the most appropriate for that specific data).</p>
</li>
<li>
<p>Loadables are displayed for the user. The loadable with the highest confidence is selected by default but the user can change it. Even multiple loadables can be selected.</p>
</li>
<li>
<p>When the user click Load, selected loadables are loaded into the scene.</p>
</li>
</ol>
<p>If “Advanced” mode is disabled on the GUI then clicking “Load” button runs Examine and the highest-confidence loadable will be loaded automatically.</p>
<p>I would tend to prefer option B, as it does not add any overhead to DICOM “examine” step, but if we find that examine step is very fast enough then Option A is acceptable, too.</p>

---

## Post #4 by @adamrankin (2017-07-23 14:28 UTC)

<p>Option A could also be a good option if Sequences remains an extension (not included in downloaded package).</p>
<p>However, I think I’d prefer to have it as part of the download. I will examine option B</p>
<p>Thanks for the key information!</p>

---

## Post #5 by @adamrankin (2017-07-23 15:17 UTC)

<p>When you have time, would you enumerate the features that multivolume has that sequences doesn’t?</p>
<p>I will throw it on my “when I have time” list at the top.</p>

---
