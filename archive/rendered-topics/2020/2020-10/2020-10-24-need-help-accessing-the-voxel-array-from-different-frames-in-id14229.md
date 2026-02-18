# Need help accessing the voxel array from different frames in an imported multivolume (Python)

**Topic ID**: 14229
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/need-help-accessing-the-voxel-array-from-different-frames-in-an-imported-multivolume-python/14229

---

## Post #1 by @cold-pac (2020-10-24 22:27 UTC)

<p>Hi everyone,</p>
<p>I have CT Perfusion data that I can import as a ‘multivolume’ (frames separated by acquisition time).<br>
I can get the MRML node with slicer.util.getNodes(‘vtkMRML<em>VolumeNode</em>’) or slicer.util.getNodes(‘vtkMRML<em>MultiVolumeNode</em>’)</p>
<p>this gives me an instance of this class: ‘vtkSlicerMultiVolumeExplorerModuleMRMLPython.vtkMRMLMultiVolumeNode’</p>
<p>Then I can get an array of voxels with slicer.util.arrayFromVolume(node) - but the array is only from 1 frame of the multivolume (i.e. the CT scan at time 0 and not any other time).</p>
<p>If I print out the “vtkMRMLMultiVolumeNode”, I can see that it has all of the dicom files from the whole study as “Attributes”, “MultiVolume.FrameLabels” for each frame, a “LabelArray” - again with each frame time, and “Number of Components” as the number of frames (14)</p>
<p>How do you jump between frames (and get voxel arrays from different ‘acquisition times’)? Do you have to import and use the MultiVolumeExplorer module? - I couldn’t find any documentation on how to use this in Python</p>
<p>Thanks very much</p>

---

## Post #2 by @lassoan (2020-10-25 00:12 UTC)

<p>MultiVolume modules can only replay two 4D volume nodes. It is superseded by the more generic Sequences module, which allows replaying, recording, and editing sequences of any nodes - volumes, transforms, segmentations, markups, models, etc. Therefore, I would recommend to use Sequences instead of MultiVolume modules.</p>
<p>If you have a 4D nrrd file then you can load it as a volume sequence (choose “Sequence” in Description column in Add data dialog) and access voxels as a numpy array as shown in these examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Sequences">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Sequences</a></p>
<p>If you save your 4D nrrd file using <code>.seq.nrrd</code> file extension then Slicer will automatically load it as volume sequence (no need to manually select “Sequence” in “Add data” window).</p>

---

## Post #3 by @cold-pac (2020-10-25 03:02 UTC)

<p>thank you this really helps!<br>
is there any way to get the separating value for each frame/node of the Volume Sequence (e.g. Acquisition Time for each frame) using Python? I can see it in the metadata in the DICOM viewer, also I know you can get the .ImageData().GetMTime() of the node but it’s not the same.</p>

---

## Post #4 by @lassoan (2020-10-25 03:25 UTC)

<p>You can get the index name, value, and unit from the sequence node:</p>
<pre><code class="lang-python">print("Index value of {0}th item: {1} = {2} {3}".format(
  itemIndex,
  sequenceNode.GetIndexName(),
  sequenceNode.GetNthIndexValue(itemIndex),
  sequenceNode.GetIndexUnit()))
</code></pre>

---

## Post #5 by @cold-pac (2020-10-25 08:04 UTC)

<p>thank you very much!</p>

---
