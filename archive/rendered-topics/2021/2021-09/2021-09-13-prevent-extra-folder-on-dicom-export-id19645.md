---
topic_id: 19645
title: "Prevent Extra Folder On Dicom Export"
date: 2021-09-13
url: https://discourse.slicer.org/t/19645
---

# Prevent extra folder on dicom export

**Topic ID**: 19645
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/prevent-extra-folder-on-dicom-export/19645

---

## Post #1 by @stephan13 (2021-09-13 13:10 UTC)

<p>Hi there</p>
<p>Exporting a volume to DICOM from the Data module does not place all DICOM files inside of the selected folder, but creates an extra one on the same level.<br>
Is there an option to prevent the extra folder?</p>

---

## Post #2 by @lassoan (2021-09-13 14:05 UTC)

<p>Exporting data to a clean folder ensures that there is no interference between DICOM exporters that are writing their outputs (potentially in parallel), the maximum number of files per folder is not exceeded (it can be a problem on file systems used for some removable media) and it also offers an easy way to determine which files are resulted from the same DICOM export operation.</p>
<aside class="quote no-group" data-username="stephan13" data-post="1" data-topic="19645">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/7ea924/48.png" class="avatar"> stephan13:</div>
<blockquote>
<p>Is there an option to prevent the extra folder?</p>
</blockquote>
</aside>
<p>It is certainly possible, but it would require developing alternative solutions for the issues mentioned above. If there are strong use cases / needed by many users then we could allocate Slicer core developers time to change the current design. What is your use case? Is the problem that you have each DICOM export result in a separate folder or that you don’t know how to get that folder?</p>

---

## Post #3 by @stephan13 (2021-09-13 15:57 UTC)

<p>I understand, thank you for your quick reply. In my case the exported DICOMs are read by a Python routine after the volume is processed with 3D Slicer. I create different folders for different volumes beforehand. Of course I could just select the deepest available folder in my routine, but I prefer a direct output to get a clean folder structure.</p>

---

## Post #4 by @lassoan (2021-09-13 16:06 UTC)

<p>If you only need to export scalar volumes then you can use the CreateDICOMSeries CLI module as it is done here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L108-L163">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L108-L163" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L108-L163" target="_blank" rel="noopener">Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L108-L163</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="108" style="counter-reset: li-counter 107 ;">
          <li>cliparameters = {}</li>
          <li># Patient</li>
          <li>cliparameters['patientName'] = self.tags['Patient Name']</li>
          <li>cliparameters['patientID'] = self.tags['Patient ID']</li>
          <li>cliparameters['patientBirthDate'] = self.tags['Patient Birth Date']</li>
          <li>cliparameters['patientSex'] = self.tags['Patient Sex'] if self.tags['Patient Sex'] else "[unknown]"</li>
          <li>cliparameters['patientComments'] = self.tags['Patient Comments']</li>
          <li># Study</li>
          <li>cliparameters['studyID'] = self.tags['Study ID']</li>
          <li>cliparameters['studyDate'] = self.tags['Study Date']</li>
          <li>cliparameters['studyTime'] = self.tags['Study Time']</li>
          <li>cliparameters['studyDescription'] = self.tags['Study Description']</li>
          <li>cliparameters['modality'] = self.tags['Modality']</li>
          <li>cliparameters['manufacturer'] = self.tags['Manufacturer']</li>
          <li>cliparameters['model'] = self.tags['Model']</li>
          <li># Series</li>
          <li>cliparameters['seriesDescription'] = self.tags['Series Description']</li>
          <li>cliparameters['seriesNumber'] = self.tags['Series Number']</li>
          <li>cliparameters['seriesDate'] = self.tags['Series Date']</li>
          <li>cliparameters['seriesTime'] = self.tags['Series Time']</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L108-L163" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Alternatively, you could add an option to CreateDICOMSeries module to take a file prefix. The scalar volume DICOM plugin then could create all the files in the base folder with a randomly generated prefix to make sure there is no name clash:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L581-L588">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L581-L588" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L581-L588" target="_blank" rel="noopener">Slicer/Slicer/blob/8eaa925245a96cf46d6c2baab72bc7c07b6e3aa3/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L581-L588</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="581" style="counter-reset: li-counter 580 ;">
          <li># Get output directory and create a subdirectory. This is necessary</li>
          <li># to avoid overwriting the files in case of multiple exportables, as</li>
          <li># naming of the DICOM files is static</li>
          <li>directoryName = 'ScalarVolume_' + str(exportable.subjectHierarchyItemID)</li>
          <li>directoryDir = qt.QDir(exportable.directory)</li>
          <li>directoryDir.mkpath(directoryName)</li>
          <li>directoryDir.cd(directoryName)</li>
          <li>directory = directoryDir.absolutePath()</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @stephan13 (2023-05-03 13:59 UTC)

<p>Late follow-up. In the end, I moved the exported files from the subdirectory created by 3DSlicer to the parent directory and removed the empty subdirectory.</p>
<pre><code class="lang-auto">import os
import shutil

import DICOMScalarVolumePlugin

def export_volume_to_DICOM(slicer: object, vol_name: str, dir_out: str):
    if len(vol_name) == 0:
        raise ValueError("invalid volume name")
    if len(dir_out) == 0:
        raise ValueError("invalid output directory")
    if not (len(os.listdir(dir_out)) == 0):
        raise ValueError(f'Directory not empty {dir_out}')

    # get patient and study name
    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    volumeNode = slicer.util.getNode(vol_name)
    seriesItem = shNode.GetItemByDataNode(volumeNode)
    studyItem = shNode.GetItemParent(seriesItem)
    patientItem = shNode.GetItemParent(studyItem)
    dcm_patient_id = shNode.GetItemAttribute(patientItem, 'DICOM.PatientID')
    dcm_study_name = shNode.GetItemName(studyItem)
    # export to file
    exporter = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
    exportables = exporter.examineForExport(seriesItem)
    for exp in exportables:
        # set output folder
        exp.directory = dir_out
        # here we set DICOM PatientID and StudyID tags
        exp.setTag('PatientID', dcm_patient_id)
        exp.setTag('StudyID', dcm_study_name)

    exporter.export(exportables)

def move_files(source, dest):
    files = os.listdir(source)
    for file in files:
        file_name = os.path.join(source, file)
        shutil.move(file_name, dest)
    print(f"Moved files from {source} to {dest}")


def get_immediate_subdirectories(a_dir):
    ret = [name for name in os.listdir(a_dir)
           if os.path.isdir(os.path.join(a_dir, name))]
    return ret


def get_immediate_subdirectory(a_dir):
    ret = get_immediate_subdirectories(a_dir)
    if len(ret) != 1:
        raise ValueError(f'Must contain exactly one subdirectory {ret}')
    ret = ret[0]
    return ret


def move_files_from_immediate_subdir_to_parent(parent_dir):
    dir_sub = get_immediate_subdirectory(parent_dir)
    dir_sub = os.path.join(parent_dir, dir_sub)
    move_files(dir_sub, parent_dir)


def remove_immediate_subdir(parent_dir):
    dir_sub = get_immediate_subdirectory(parent_dir)
    dir_sub = os.path.join(parent_dir, dir_sub)
    os.removedirs(dir_sub)
    print(f'removed dir {dir_sub}')

# example from Jupyter managed 3DSlicer: clean up temporary directory right after file export
export_volume_to_DICOM(slicer, 'my_volume', dir_out)
move_files_from_immediate_subdir_to_parent(dir_out)
remove_immediate_subdir(dir_out)
</code></pre>

---
