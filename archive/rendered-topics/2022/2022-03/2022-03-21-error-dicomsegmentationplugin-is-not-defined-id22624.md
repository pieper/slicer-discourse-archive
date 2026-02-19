---
topic_id: 22624
title: "Error Dicomsegmentationplugin Is Not Defined"
date: 2022-03-21
url: https://discourse.slicer.org/t/22624
---

# Error: DICOMSegmentationPlugin is not defined

**Topic ID**: 22624
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/error-dicomsegmentationplugin-is-not-defined/22624

---

## Post #1 by @Liu_Lance (2022-03-21 17:31 UTC)

<p>Hi<br>
I try with the segmentation export to file function. It does not work for the line  “import DICOMScalarVolumePlugin”,</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
in the python console in 3d slicer, the error is like<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘DICOMSegmentationPlugin’ is not defined</p>
<p>Does this package still work. How can I install this ?<br>
the code snippet is as follow:</p>
<h3><a name="p-75783-export-a-volume-to-dicom-file-formathttpsslicerreadthedocsioenlatestdeveloper_guidescript_repositoryhtmlexport-a-volume-to-dicom-file-format-1" class="anchor" href="#p-75783-export-a-volume-to-dicom-file-formathttpsslicerreadthedocsioenlatestdeveloper_guidescript_repositoryhtmlexport-a-volume-to-dicom-file-format-1" aria-label="Heading link"></a>Export a volume to DICOM file format<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" rel="noopener nofollow ugc">¶</a></h3>
<p>volumeNode = getNode(“CTChest”) outputFolder = “c:/tmp/dicom-output” # Create patient and study and put the volume under the study shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene) # set IDs. Note: these IDs are not specifying DICOM tags, but only the names that appear in the hierarchy tree patientItemID = shNode.CreateSubjectItem(shNode.GetSceneItemID(), “test patient”) studyItemID = shNode.CreateStudyItem(patientItemID, “test study”) volumeShItemID = shNode.GetItemByDataNode(volumeNode) shNode.SetItemParent(volumeShItemID, studyItemID) import DICOMScalarVolumePlugin exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass() exportables = exporter.examineForExport(volumeShItemID) for exp in exportables: # set output folder exp.directory = outputFolder # here we set DICOM PatientID and StudyID tags exp.setTag(‘PatientID’, “test patient”) exp.setTag(‘StudyID’, “test study”) exporter.export(exportables)</p>

---

## Post #2 by @jamesobutler (2022-03-21 20:19 UTC)

<p>Yes for that example to work you have to have a Slicer extension installed. See the following thread about this:</p>
<aside class="quote quote-modified" data-post="6" data-topic="22289">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-dicomsegmentationplugin-does-not-work-in-preview-release/22289/6">Import DICOMSegmentationPlugin does not work in preview release</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Are you trying to replicate this example? 
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-segmentation-to-dicom-segmentation-object" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-segmentation-to-dicom-segmentation-object</a> 
According to this statement in Slicer core, the “DICOMSegmentationPlugin” comes from a Slicer extension. You would need to install Quantitative Reporting before being able to import DICOMSegmentationPlugin. 
[image] 
<a class="mention" href="/u/pieper">@pieper</a> This probably brings up a point that the Script Repository needs to make mentions of any dependent ex…
  </blockquote>
</aside>


---

## Post #3 by @Liu_Lance (2022-03-22 01:16 UTC)

<aside class="quote no-group" data-username="Liu_Lance" data-post="1" data-topic="22624">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/liu_lance/48/14386_2.png" class="avatar"> Liu_Lance:</div>
<blockquote>
<p>DICOMSegmentationPlugin</p>
</blockquote>
</aside>
<p>Thanks so much,<br>
It looks like the problem is solved. the icon of the dicomQR doesn’t work anyway<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f2b557b3f71206184b983fa6cd3ab9dbfaba39b.png" alt="image" data-base62-sha1="fRrQbu9SpnWT9oJpFjSwZyzR0RZ" width="262" height="363"></p>

---
