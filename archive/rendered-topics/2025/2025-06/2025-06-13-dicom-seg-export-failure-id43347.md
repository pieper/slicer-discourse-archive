---
topic_id: 43347
title: "Dicom Seg Export Failure"
date: 2025-06-13
url: https://discourse.slicer.org/t/43347
---

# Dicom-seg Export Failure

**Topic ID**: 43347
**Date**: 2025-06-13
**URL**: https://discourse.slicer.org/t/dicom-seg-export-failure/43347

---

## Post #1 by @GaryPlayer (2025-06-13 20:38 UTC)

<p>I am trying to create an example dicom-seg from export.  I have my original dicom loaded as a volume and my segmentation (nrrd file) also loaded.  Following the tutorial I get the following pop up:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/764b81acbbadc542752da14e1ebf04358c942b11.png" data-download-href="/uploads/short-url/gSu72q6ahW7qdl5G70BrV7uArND.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/764b81acbbadc542752da14e1ebf04358c942b11.png" alt="image" data-base62-sha1="gSu72q6ahW7qdl5G70BrV7uArND" width="509" height="151"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">509×151 9.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I try and drop the segmentation under the dicom:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a767d37a9d40d9a6ebc1f3a9b0bcfde3e0e174c.png" data-download-href="/uploads/short-url/fbOtmKenrKQJiJkDSsZ56WqzLu4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a767d37a9d40d9a6ebc1f3a9b0bcfde3e0e174c.png" alt="image" data-base62-sha1="fbOtmKenrKQJiJkDSsZ56WqzLu4" width="517" height="103"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">517×103 6.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So then I try to use the export dialog to arrange everything per my understanding:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f66e2a8f0659dc5919810834afef4ac141549111.png" data-download-href="/uploads/short-url/za1ufbxuSaOvr5HjWJzeMbEIArT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f66e2a8f0659dc5919810834afef4ac141549111.png" alt="image" data-base62-sha1="za1ufbxuSaOvr5HjWJzeMbEIArT" width="533" height="500" data-dominant-color="F3F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">659×618 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is my error log.  No matter how hard I try to organize the dicom and segmentation I keep getting reference volume not found errors.  There is obviously something simple I am missing.</p>
<p>My google search has yielded me little and I am very stuck.</p>
<pre><code class="lang-auto">

[Qt] void __cdecl qSlicerSubjectHierarchyDICOMPlugin::openDICOMExportDialog(void) : DICOM export cannot be performed without a parent patient and study. Manual interaction has been selected.
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] bool __cdecl qMRMLSubjectHierarchyModel::reparent(__int64,__int64) : Failed to reparent virtual item  Test2_002087_10 YR_SD-OCT_R(OD)_OPT.dcm  under parent  EZ_63
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] class QString __cdecl qSlicerDICOMTagEditorWidget::setExportables(class QList&lt;class qSlicerDICOMExportable *&gt;) :  "No patient found"
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
[Qt] class QString __cdecl qSlicerDICOMTagEditorWidget::setExportables(class QList&lt;class qSlicerDICOMExportable *&gt;) :  "No patient found"
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
Traceback (most recent call last):
  File "&lt;string&gt;", line 3, in &lt;module&gt;
  File "C:/Users/rdslater/AppData/Local/slicer.org/Slicer 5.8.1/bin/../lib/Slicer-5.8/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py", line 235, in export
    exporter.export()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMExportScene.py", line 65, in export
    success = self.createDICOMFileForScene()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMExportScene.py", line 170, in createDICOMFileForScene
    DICOMLib.DICOMCommand("img2dcm", args).start()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMProcesses.py", line 167, in start
    raise UserWarning(f"Could not run {self.executable} with {self.args}")
UserWarning: Could not run C:/Users/rdslater/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin/img2dcm.exe with ['-k', 'SeriesDescription=Slicer Data Bundle', '--no-latin1', '-k', 'SeriesNumber=100', '--dataset-from', 'C:/Users/rdslater/Desktop\\template.dcm', 'C:/Users/rdslater/Desktop/scene.jpg', 'C:/Users/rdslater/Desktop\\SlicerDataBundle.dcm']
[Python] Failed to export using plugin DICOMSlicerDataBundlePluginClass
[VTK] Warning: In vtkMRMLSegmentationStorageNode.cxx, line 702
[VTK] vtkMRMLSegmentationStorageNode (000001C1A92CEB20): vtkMRMLSegmentationStorageNode::ReadBinaryLabelmapRepresentation: Segmentation is a floating point scalar type and will be cast to an integer type by truncation (rounding towards 0).
[Qt] void __cdecl qSlicerIOManager::showLoadNodesResultDialog(bool,class vtkMRMLMessageCollection *) Errors occurred while loading nodes: "Warning: Loading C:/Users/rdslater/Downloads/EZ_63.seg.nrrd - Segmentation is a floating point scalar type and will be cast to an integer type by truncation (rounding towards 0).\n"
[Qt] void __cdecl qSlicerSubjectHierarchyDICOMPlugin::openDICOMExportDialog(void) : DICOM export cannot be performed without a parent patient and study. Manual interaction has been selected.
[Qt] void __cdecl qSlicerDICOMExportDialog::examineSelectedItem(void) : Can only export data node or study item
Traceback (most recent call last):
  File "&lt;string&gt;", line 3, in &lt;module&gt;
  File "C:/Users/rdslater/AppData/Local/slicer.org/Slicer 5.8.1/bin/../lib/Slicer-5.8/qt-scripted-modules/DICOMSlicerDataBundlePlugin.py", line 235, in export
    exporter.export()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMExportScene.py", line 65, in export
    success = self.createDICOMFileForScene()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMExportScene.py", line 170, in createDICOMFileForScene
    DICOMLib.DICOMCommand("img2dcm", args).start()
  File "C:\Users\rdslater\AppData\Local\slicer.org\Slicer 5.8.1\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMProcesses.py", line 167, in start
    raise UserWarning(f"Could not run {self.executable} with {self.args}")
UserWarning: Could not run C:/Users/rdslater/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin/img2dcm.exe with ['-k', 'SeriesDescription=Slicer Data Bundle', '--no-latin1', '-k', 'PatientName=Anonymous', '-k', 'PatientID=VIQMDW', '-k', 'StudyDate=20250613', '-k', 'StudyTime=153022', '-k', 'StudyDescription=No study description', '-k', 'StudyInstanceUID=1.2.276.0.7230010.3.1.2.3587915286.48156.1749846622.23', '--dataset-from', 'C:/Users/rdslater/Desktop\\template.dcm', 'C:/Users/rdslater/Desktop/scene.jpg', 'C:/Users/rdslater/Desktop\\SlicerDataBundle.dcm']
[Python] Failed to export using plugin DICOMSlicerDataBundlePluginClass
</code></pre>

---
