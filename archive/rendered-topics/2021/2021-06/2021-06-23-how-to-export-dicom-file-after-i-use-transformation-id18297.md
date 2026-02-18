# How to export dicom file after I use transformation?

**Topic ID**: 18297
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/how-to-export-dicom-file-after-i-use-transformation/18297

---

## Post #1 by @yllgl (2021-06-23 12:33 UTC)

<p>I import my local dicom dataset. There are two study of one patient : one about CT, the other about MR. Then I use registration between them, and automatically generate a linear transformation and apply on CT. Now I want to export the series after applying the tranformation.<br>
I have three questions:</p>
<ol>
<li>Why are there no “export to dicom” option when I right-click on patient node? Only study node and series node have “export to dicom” option. And Must I export dicom one study by one study? Can’t I select multiple patients at once and export them all at once?</li>
<li>When I export dicom, the directory was named ScalarVolume_xxx , (xxx is some digits) I don’t know what the name mean so I can’t correspond them to the information in the software. Can I change the name to some meaningful string?<br>
3、After I export dicom, I found no difference between my original dicom file and output file after registration. The transformation only contains translation, so I think the output file should modified the dicom tag (0020,0032) which is image position. But nothing was modified. How could I export dicom file after transformation?</li>
</ol>

---

## Post #2 by @lassoan (2021-06-25 18:40 UTC)

<aside class="quote no-group" data-username="yllgl" data-post="1" data-topic="18297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/8e7dd6/48.png" class="avatar"> yllgl:</div>
<blockquote>
<p>Why are there no “export to dicom” option when I right-click on patient node? Only study node and series node have “export to dicom” option. And Must I export dicom one study by one study? Can’t I select multiple patients at once and export them all at once?</p>
</blockquote>
</aside>
<p>Yes, the GUI only allows you to export one study at a time. If it is too tedious for your workflow then you can implement fully automatic export of everything that you need with a short Python script.</p>
<aside class="quote no-group" data-username="yllgl" data-post="1" data-topic="18297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/8e7dd6/48.png" class="avatar"> yllgl:</div>
<blockquote>
<p>When I export dicom, the directory was named ScalarVolume_xxx , (xxx is some digits) I don’t know what the name mean so I can’t correspond them to the information in the software. Can I change the name to some meaningful string?</p>
</blockquote>
</aside>
<p>DICOM does not know anything about filenames. All file content is described in DICOM tags in the files. During DICOM export, you can specify values for many DICOM tags, which you can use to identify data sets.</p>
<aside class="quote no-group" data-username="yllgl" data-post="1" data-topic="18297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/8e7dd6/48.png" class="avatar"> yllgl:</div>
<blockquote>
<p>After I export dicom, I found no difference between my original dicom file and output file after registration. The transformation only contains translation, so I think the output file should modified the dicom tag (0020,0032) which is image position. But nothing was modified. How could I export dicom file after transformation?</p>
</blockquote>
</aside>
<p>You need to harden the transform on the data images if you want to export a modified image. Alternatively, you can export the transform as a DICOM Spatial Registration Object if you install SlicerRT extension.</p>

---

## Post #4 by @yllgl (2021-06-26 12:34 UTC)

<p>How to get original dicom tag from volumeNode? I just use the code:</p>
<pre><code class="lang-python">volumeNode = slicer.util.getNode(pattern='8002: 3D_Default_2_9', index=0, scene=None)
plugin = slicer.modules.dicomPlugins['DICOMScalarVolumePlugin']()
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
subjectHierarchyItemID = shNode.GetItemByDataNode(volumeNode)
exportables = plugin.examineForExport(subjectHierarchyItemID)
for exportable in exportables :
...
</code></pre>
<p>But <code>exportable</code> 's tag is different from original one, which modality is CT but original one is MR, how could I get original tag so I could save it ?</p>

---

## Post #5 by @yllgl (2021-06-27 02:47 UTC)

<p>Why can’t I get original study ID? I use the following code:</p>
<pre><code class="lang-python">subjectHierarchyItemID = shNode.GetItemByDataNode(volumeNode)
studyItemID = shNode.GetItemParent(subjectHierarchyItemID)
print(shNode.GetItemAttribute(studyItemID,'DICOM.StudyID'))# this line return empty string
</code></pre>

---

## Post #6 by @lassoan (2021-06-27 02:54 UTC)

<p>The attribute name is <code>StudyID</code> (not <code>DICOM.StudyID</code>). You can get the list of all attribute names available for the item by calling <code>shNode.GetItemAttributeNames(studyItemID)</code>.</p>

---

## Post #7 by @yllgl (2021-06-27 05:02 UTC)

<p>it’s very strange, if I change DICOM.StudyID to StudyID, it will fail to save. I don’t know why. Maybe it’s a bug?</p>
<pre><code class="lang-python">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
for name,volumeNode in slicer.util.getNodes(pattern='*3D*[!m]', scene=None, useLists=False).items():
    subjectHierarchyItemID = shNode.GetItemByDataNode(volumeNode)
    if volumeNode is None or not volumeNode.IsA('vtkMRMLScalarVolumeNode'):
        error = "Series '" + shNode.GetItemName(subjectHierarchyItemID) + "' cannot be exported"
        print(error)
        continue
    studyItemID = shNode.GetItemParent(subjectHierarchyItemID)
    if not studyItemID:
        error = "Unable to get study for series '" + volumeNode.GetName() + "'"
        print(error)
        continue
    patientItemID = shNode.GetItemParent(studyItemID)
    if not patientItemID:
        error = "Unable to get patient for series '" + volumeNode.GetName() + "'"
        print(error)
        continue
    tags = {}
    tags['Patient Name'] = shNode.GetItemAttribute(patientItemID,'DICOM.PatientName')
    tags['Patient ID'] = shNode.GetItemAttribute(patientItemID,'DICOM.PatientID')
    tags['Patient Birth Date'] = shNode.GetItemAttribute(patientItemID,'DICOM.PatientBirthDate')
    tags['Patient Sex'] = shNode.GetItemAttribute(patientItemID,'DICOM.PatientSex')
    tags['Patient Comments'] = shNode.GetItemAttribute(patientItemID,'DICOM.PatientComments')
    tags['Study ID'] = shNode.GetItemAttribute(studyItemID,'DICOM.StudyID')#if change DICOM.StudyID to StudyID, it will fail to save.
    tags['Study Date'] = shNode.GetItemAttribute(studyItemID,'DICOM.StudyDate')
    tags['Study Time'] = shNode.GetItemAttribute(studyItemID,'DICOM.StudyTime')
    tags['Study Description'] = shNode.GetItemAttribute(studyItemID,'DICOM.StudyDescription')
    tags['Modality'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.Modality')
    tags['Manufacturer'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.Manufacturer')
    tags['Model'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.Model')
    tags['Series Description'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.SeriesDescription')
    tags['Series Number'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.SeriesNumber')
    tags['Series Date'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.SeriesDate')
    tags['Series Time'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.SeriesTime')
    tags['Content Date'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.ContentDate')
    tags['Content Time'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.ContentTime')
    tags['Study Instance UID'] = shNode.GetItemAttribute(studyItemID,'StudyInstanceUID')
    tags['Series Instance UID'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.SeriesInstanceUID')
    tags['Frame of Reference Instance UID'] = shNode.GetItemAttribute(subjectHierarchyItemID,'DICOM.ReferencedInstanceUIDs')
    if tags['Modality'] == "":
        error = "Empty modality for series '" + volumeNode.GetName() + "'"
        print(error)
        continue
    directoryName = str(tags['Series Number'])
    directoryDir = qt.QDir(f"D:/data/{str(tags['Patient Name'])}/{str(tags['Modality'])}")
    directoryDir.mkpath(directoryName)
    directoryDir.cd(directoryName)
    directory = directoryDir.absolutePath()
    exporter = DICOMExportScalarVolume(tags['Study ID'], volumeNode, tags, directory)
    if not exporter.export():
        print("Creating DICOM files from scalar volume failed")
        continue
</code></pre>

---

## Post #8 by @lassoan (2021-06-27 13:44 UTC)

<aside class="quote no-group" data-username="yllgl" data-post="7" data-topic="18297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/8e7dd6/48.png" class="avatar"> yllgl:</div>
<blockquote>
<p>if I change DICOM.StudyID to StudyID, it will fail to save</p>
</blockquote>
</aside>
<p>If you use DICOM.StudyID then you pass an empty string for StudyID, so a new one is generated for you.</p>
<p>It seems that you have problem when you pass the actual existing StudyID to the exporter. It should work, too. What is the error message that you get?</p>

---

## Post #9 by @yllgl (2021-06-27 13:48 UTC)

<p>just output :</p>
<pre><code class="lang-auto">True
True
Creating DICOM files from scalar volume failed
</code></pre>
<p>I don’t know why.</p>

---

## Post #10 by @lassoan (2021-06-27 13:54 UTC)

<p>Do you see errors in the application log (menu: Help / Report a bug)?</p>

---
