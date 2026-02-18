# From DICOM scalar volume to retrieve header attributes/tags

**Topic ID**: 11740
**Date**: 2020-05-27
**URL**: https://discourse.slicer.org/t/from-dicom-scalar-volume-to-retrieve-header-attributes-tags/11740

---

## Post #1 by @szhang (2020-05-27 23:16 UTC)

<p>Hello<br>
Probably a very basic question, after loading the DICOM stack as a scalar volume, how in the code can I obtain one of the header tag information (e.g. Patient Position, or Reconstruction Kernel)? If there are some sample code to look up to, that will be great.</p>
<p>Thank you!</p>

---

## Post #2 by @szhang (2020-05-28 13:43 UTC)

<p>To continue on this thread, this is what I have tried on Python interactor window:<br>
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)<br>
volumeNode = slicer.mrmlScene.GetNodeByID(‘vtkMRMLScalarVolumeNode1’)<br>
shNode.GetAttributeFromItemAncestor(shNode.GetItemByDataNode(volumeNode),‘DICOM.PatientName’)</p>
<p>It can return something, but if I substitute DICOM.PatientName with some other attributes, such as DICOM.modality or DICOM.ConvolutionKernel, there is nothing returned, but I clearly see the value of these attributes, what am I missing?</p>
<p>Thanks a lot in advance!</p>

---

## Post #3 by @pieper (2020-05-28 14:26 UTC)

<p>Hi -</p>
<p>Only some high level tags are stored in the node.  To get the rest of the dicom header info you use the instance uid and you can either access via the database or use pydicom to look at the instances directly.</p>
<p>This code will help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:</a></p>

---

## Post #4 by @szhang (2020-05-28 15:53 UTC)

<p>Got it, thank you, Steve!</p>

---

## Post #5 by @szhang (2020-05-28 22:23 UTC)

<p>The next step I wanted is to save this attribute value together with the output volume for DICOMs, this piece is somewhat useful:<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_a_volume_to_DICOM_file_format</a><br>
but I do not see how to set certain attribute values,<br>
I tried DICOMExportScalarVolume but the tags do not get saved in DICOM output attributes. Any advice?</p>
<p>Thank you again!</p>

---

## Post #6 by @pieper (2020-05-28 23:52 UTC)

<p>Hmm, for that kind of manipulation probably the easiest is to iterate through the exported files and modify attributes with pydicom like <a href="https://github.com/lassoan/SlicerDicomPatcher/blob/master/DicomPatcher.py">is done in the DicomPatcher</a>.</p>

---

## Post #7 by @szhang (2020-05-29 00:42 UTC)

<p>I see, thank you! However, I do not find “pydicom” used anywhere in DicomPatcher.py…</p>

---

## Post #8 by @lassoan (2020-05-29 00:42 UTC)

<aside class="quote no-group" data-username="szhang" data-post="5" data-topic="11740">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>the tags do not get saved in DICOM output attributes</p>
</blockquote>
</aside>
<p>What tags would you like to save? We can add some more of the commonly used standard tags, if that helps.</p>
<p>For adding arbitrary custom tags using pydicom as <a class="mention" href="/u/pieper">@pieper</a> suggested should work well. You can integrate the this additional update step nicely in the DICOM export GUI by implementing a custom DICOM export plugin. It should be just a few ten lines of extra code. See an example of a <a href="https://github.com/SlicerRt/SlicerRT/blob/7f56d8ee6c54ab98a80113075beaac7d2c7ed921/DicomRtImportExport/DicomRtImportExportPlugin.py#L67-L127">custom DICOM import/export plugin in SlicerRT</a>.</p>

---
