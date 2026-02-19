---
topic_id: 29110
title: "Identify A Single Slice File Name In 3D Dicom Volume"
date: 2023-04-25
url: https://discourse.slicer.org/t/29110
---

# identify a single slice file name in 3D dicom volume

**Topic ID**: 29110
**Date**: 2023-04-25
**URL**: https://discourse.slicer.org/t/identify-a-single-slice-file-name-in-3d-dicom-volume/29110

---

## Post #1 by @sumsumin (2023-04-25 11:10 UTC)

<p>How can I identify a the file name of a single slice in a loaded 3D DICOM volume? I have loaded a DICOM directory with several hundred slices, but after I have identified a single slice of interest, I would like to know which file name it is.</p>

---

## Post #2 by @pieper (2023-04-25 12:58 UTC)

<p>You can use the python api like in the example linked below.  The <code>instanceUIDs</code> attribute of the volume node can be used with <code>fileForInstance()</code> to get the path.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-path-and-filename-of-a-scalar-volume-node-loaded-from-dicom" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-path-and-filename-of-a-scalar-volume-node-loaded-from-dicom</a></p>

---

## Post #3 by @sumsumin (2023-04-26 02:55 UTC)

<p>thanks for reply.</p>
<p>‘’’<br>
volumeName = “1302: Chest CE 3.0 I50f 2_1”</p>
<p>volumeNode = slicer.util.getNode(volumeName)</p>
<p>instUids = volumeNode.GetAttribute(“DICOM.instanceUIDs”).split()</p>
<p>filepath = slicer.dicomDatabase.fileForInstance(instUids[0])</p>
<p>print(“DICOM path=%s” % filepath)<br>
‘’’</p>
<p>I implemented this code , and the result of filepath was from DicomDatabase.<br>
But i want the filepath from where I import the dicom file.</p>

---

## Post #4 by @lassoan (2023-04-26 03:29 UTC)

<p>You can choose to copy the imported DICOM files into the database or just add a link to it. For example to con toggle this setting in the DICOM module by clicking the down-arrow button on the DICOM import button.</p>
<p>That said, filename is not the most robust way of referring to an image slice. Instead, the instance UID uniquely identifies the entire content of the image frame, globally, forever. If you have the UID then you can always retrieve the file from a local folder, from a DICOM server, from a local database, etc.</p>

---

## Post #5 by @sumsumin (2023-04-26 04:34 UTC)

<aside class="quote no-group" data-username="sumsumin" data-post="3" data-topic="29110">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sumsumin/48/65767_2.png" class="avatar"> sumsumin:</div>
<blockquote>
<p>‘’’<br>
volumeName = “1302: Chest CE 3.0 I50f 2_1”</p>
<p>volumeNode = slicer.util.getNode(volumeName)</p>
<p>instUids = volumeNode.GetAttribute(“DICOM.instanceUIDs”).split()</p>
<p>filepath = slicer.dicomDatabase.fileForInstance(instUids[0])</p>
<p>print(“DICOM path=%s” % filepath)<br>
‘’’</p>
</blockquote>
</aside>
<p>if i print(instUids) in this code, there are lot of UID , but i want to know only specific slice UID.<br>
How can i know the index of slice file and approach to that?</p>

---

## Post #6 by @lassoan (2023-05-02 20:03 UTC)

<p>In most cases, there is an instance UID for each slice. The slice index is the third voxel coordinate (K). You can convert RAS to IJK as shown in <a href="https://stackoverflow.com/questions/16087674/how-can-i-make-my-nsis-silent-installer-block-until-complete">this example</a>.</p>

---
