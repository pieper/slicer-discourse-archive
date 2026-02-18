# How do access the source filepath(s) of a DICOM image given a `vtkMRMLScalarVolumeNode`

**Topic ID**: 20619
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/how-do-access-the-source-filepath-s-of-a-dicom-image-given-a-vtkmrmlscalarvolumenode/20619

---

## Post #1 by @aarashy (2021-11-15 02:34 UTC)

<p>Hello!<br>
I’m making my first Slicer plugin, and my goal is to use the <code>pydicom</code> package to read a DICOM file, i.e. <code>pydicom.read_file(&lt; Path to the .dcm file, whether it was copied or linked during import &gt;)</code></p>
<p>I am having trouble getting the filepath.</p>
<p>I was following the tutorial in this youtube video: <code>https://www.youtube.com/watch?v=njoTEisxAJ4</code></p>
<p>I’m using <code>slicer.util.getNode(&lt;name&gt;)</code> to get a <code>vtkMRMLScalarVolumeNode</code>, but to my surprise, when I call <code>_.GetStorageNode()</code>, my storage node is None. It seems the storage node object has a <code>_.GetFileName()</code> property, but I can’t reach it.</p>
<p>I tried to look around for information on why my StorageNode might be None, what I can do to make it initialize properly, or if there’s another way to get the DICOM file path.</p>
<p>Any advice? Thank you!</p>

---

## Post #2 by @pieper (2021-11-15 20:56 UTC)

<p>If the volume was loaded from dicom then the file path can be accessed with this code:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-volume-loaded-from-dicom-for-example-get-the-patient-position-stored-in-a-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-volume-loaded-from-dicom-for-example-get-the-patient-position-stored-in-a-volume</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-path-and-filename-of-a-loaded-dicom-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-path-and-filename-of-a-loaded-dicom-volume</a></p>

---

## Post #3 by @aarashy (2021-11-16 03:58 UTC)

<p>Worked like a charm!! Thanks. I hadn’t seen the script repository somehow.</p>

---
