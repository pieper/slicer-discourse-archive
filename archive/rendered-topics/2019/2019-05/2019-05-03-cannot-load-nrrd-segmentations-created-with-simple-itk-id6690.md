---
topic_id: 6690
title: "Cannot Load Nrrd Segmentations Created With Simple Itk"
date: 2019-05-03
url: https://discourse.slicer.org/t/6690
---

# Cannot load nrrd segmentations created with Simple ITK

**Topic ID**: 6690
**Date**: 2019-05-03
**URL**: https://discourse.slicer.org/t/cannot-load-nrrd-segmentations-created-with-simple-itk/6690

---

## Post #1 by @dominicwhite (2019-05-03 21:50 UTC)

<p>I’m trying to create a segmentation (externally) in Python and then import it into Slicer through the data module, but Slicer keeps crashing. As far as I can tell, this seems to be related to how SimpleITK converts NumPy array to Images, but I don’t know what to do differently to make it work with Slicer.</p>
<p>For example, given a segmentation NRRD saved from Slicer, <code>Segmentation.seg.nrrd</code>, the following code works:</p>
<pre><code class="lang-python">import SimpleITK as sitk
seg_vol = sitk.ReadImage(DATA_DIR + 'Segmentation.seg.nrrd')
writer = sitk.ImageFileWriter()
writer.Execute(seg_vol, DATA_DIR + 'Segmentation_v2.seg.nrrd', True)
</code></pre>
<p>… and I import <code>Segmentation_v2.seg.nrrd</code> into Slicer without problems.</p>
<p>However, if I convert the sitk image to a Numpy array and back again…</p>
<pre><code class="lang-python">seg_vol = sitk.ReadImage(DATA_DIR + 'Segmentation.seg.nrrd')

# there and back again:
seg_nda = sitk.GetArrayFromImage(seg_vol)
seg_reverse = sitk.GetImageFromArray(seg_nda)
seg_reverse.CopyInformation(seg_vol)

writer = sitk.ImageFileWriter()
writer.Execute(seg_vol, DATA_DIR + 'Segmentation_v3.seg.nrrd', True)
</code></pre>
<p>… then Slicer crashes when I try to import the segmentation, and I get a bunch of nasty error messages in my terminal:</p>
<pre><code class="lang-bash">Warning: In /Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx, line 586
vtkMRMLSegmentationStorageNode (0x7faecf985ed0): ReferenceImageExtentOffset attribute was not found in NRRD segmentation file. Assume no offset.

Warning: In /Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx, line 663
vtkMRMLSegmentationStorageNode (0x7faecf985ed0): Segment ID is missing for segment 0 adding segment with ID: SegmentAuto

Warning: In /Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx, line 674
vtkMRMLSegmentationStorageNode (0x7faecf985ed0): Segment name is missing for segment 0

Warning: In /Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.cxx, line 724
vtkMRMLSegmentationStorageNode (0x7faecf985ed0): Segment extent is missing for segment 0

Segmentation fault: 11
</code></pre>
<p>Am I missing something obvious? Any solutions/suggestions welcome.</p>

---

## Post #2 by @lassoan (2019-05-04 11:44 UTC)

<p>Segmentation is stored as a 4D volume (to allow overlap between segments) and contain additional metadata (segment names, colors, etc).</p>
<p>If you have a labelmap in a 3D volume, with each segment represented by a different label value, then probably the easiest is to load that the file a labelmap volume and import it into segmentation:</p>
<pre><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
[success, labelmapVolumeNode] = slicer.util.loadLabelVolume('c:/Users/abc/Documents/SomeLabelmap.nrrd', returnNode=True)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segmentationNode)
slicer.mrmlScene.RemoveNode(labelmapVolumeNode)</code></pre>

---

## Post #3 by @bashkanov (2020-11-24 10:15 UTC)

<p>I have exactly the same issue with my segmentations.<br>
If I save it like this (without <code>.seg</code> exstention):</p>
<pre><code class="lang-auto">writer = sitk.ImageFileWriter()
writer.Execute(seg_vol, 'Segmentation.nrrd', True)
</code></pre>
<p>then if I load it manually in Slicer, first, I need to load it as “Volume” and import it further as “Segmentation” in Segmentations module. However, if I use CaseIterator Module then it is done automatically.</p>
<p>Is there any way to embed the code snipped from above into my SimpleITK pipeline and use it outside Slicer software?<br>
Or, to put it differently, is it possible to install the following packages in my python environment and then use it simply like that: <code>import vtk, qt, ctk, slicer</code>?<br>
Am I missing something?</p>

---

## Post #4 by @lassoan (2020-11-24 19:15 UTC)

<p>If you use a recent Slicer version, then all you need to do is save the segmentation using .seg.nrrd extension. Slicer will automatically load it as a segmentation. If you want to specify segment names and colors then you can add that information as custom fields in the header.</p>
<p>All the custom fields are specified <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">here</a>. You can find an example of <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header">reading segmentation custom fields from plain Python</a> (using pynrrd, without any Slicer dependency).You could implement writing of custom fields similarly.</p>
<aside class="quote no-group" data-username="bashkanov" data-post="3" data-topic="6690">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/e79b87/48.png" class="avatar"> bashkanov:</div>
<blockquote>
<p>is it possible to install the following packages in my python environment and then use it simply like that: <code>import vtk, qt, ctk, slicer</code> ?</p>
</blockquote>
</aside>
<p>Slicer modules rely on having an application that provides a lot of features that the plain Python executable does not. Some libraries could be Python-wrapped and used without a Slicer application (in any Python interpreter). We might offer this in the future, but it is not high priority for us since you can install any Python packages in Slicer’s Python environment (<code>pip_install('...')</code>) and use it from there, along with everything else that Slicer provides. You can use Slicer’s Python environment using Slicer GUI, console, or <a href="https://github.com/Slicer/SlicerJupyter">Jupyter notebooks</a>.</p>

---
