---
topic_id: 31835
title: "Failed To Save A Scene To External Exfat Usb Volume On Macos"
date: 2023-09-21
url: https://discourse.slicer.org/t/31835
---

# Failed to save a scene to external ExFAT usb volume on MacOS

**Topic ID**: 31835
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/failed-to-save-a-scene-to-external-exfat-usb-volume-on-macos/31835

---

## Post #1 by @DennisEx81 (2023-09-21 20:19 UTC)

<p>Hello,</p>
<p>Version 5.4.0, I was not able to save a scene successfully to an external usb volume on MacOS (works on windows though). Error message below,</p>
<pre><code class="lang-auto">vtkMRMLVolumeArchetypeStorageNode::WriteDataInternal: Error renaming file to /Volumes/USB1/test1/._t1.nii.gz, renameReturn = -1
</code></pre>
<pre><code class="lang-auto">bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const qSlicerIO::IOProperties &amp;, vtkMRMLMessageCollection *, vtkMRMLScene *) error: Saving failed with all writers found for file "/Volumes/USB1/test1/t1.nii.gz" of type "VolumeFile"
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection *, bool) Data save error: "- Error: Error renaming file to /Volumes/USB1/test1/._t1.nii.gz, renameReturn = -1\n- Error: Cannot write data file: /Volumes/USB1/test1/t1.nii.gz.\n"
</code></pre>
<p>Anyone knows why?</p>
<p>Thank you!<br>
Dennis</p>

---

## Post #2 by @lassoan (2023-09-21 20:21 UTC)

<p>By default, node names are used as file names. It seems that your node name has some special characters or starts or ends with a space, etc. that is not a valid filename on the file system you are trying to save. I would recommend to rename the node.</p>

---

## Post #3 by @DennisEx81 (2023-09-21 20:33 UTC)

<p>I simply named the node as t1 but the error message shows it somehow tried to rename/save the file to ._t1 or going through this process. It only happened in macos but worked fine in windows.</p>

---

## Post #4 by @lassoan (2023-09-21 20:55 UTC)

<p>Make sure the node name does not start or end with a space. It may be hard to see that when the node name is displayed, but more visible when you are editing the node name.</p>

---
