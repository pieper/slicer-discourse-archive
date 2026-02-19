---
topic_id: 11203
title: "Question About Patient Id"
date: 2020-04-20
url: https://discourse.slicer.org/t/11203
---

# Question about patient ID

**Topic ID**: 11203
**Date**: 2020-04-20
**URL**: https://discourse.slicer.org/t/question-about-patient-id/11203

---

## Post #1 by @codecrazer (2020-04-20 13:53 UTC)

<p>When I try to convert from DICOM to NRRD, I have to rename both image and segmentation, and this is an error-prone process. Is it possible for me to check the patient ID in the NRRD file, thanks for your help!</p>

---

## Post #2 by @lassoan (2020-04-20 14:28 UTC)

<p>You can write a few-line Python script that imports images and segmentations from a folder and before saving them to file, renames the nodes to have and sets the node names the way you like. YOu can find all the necessary code snippets in the script repository:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder">import DICOM</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:">retrieve DICOM field values</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Save_a_node_to_file">save node to file</a></li>
</ul>

---

## Post #3 by @codecrazer (2020-04-21 11:49 UTC)

<p>If I load the DICOM image manually, how could I check the name of current DICOM image. I ask this question because when I load two or more patients, the previous series will exist in the segmentation module, and this is really misleaded! Thansk for your help!!</p>

---

## Post #4 by @cpinter (2020-04-21 12:35 UTC)

<p>In the Data module you can see the DICOM images in a patient/study/series tree. When you create a segmentation in Segment Editor, then the segmentation is added ot the same study as the image, so you can check the correspondence there.</p>
<p>Then, when you change segmentation in Segment Editor, the master volume (i.e. the corresponding DICOM image) is selected automatically.</p>

---

## Post #5 by @AGR (2020-08-04 16:23 UTC)

<p>It’s a bit late of a response, but you could check the Left Top annotation in the DataProbe module. It’ll show patient name, ID and/or sequence in the visor depending on the Annotation Level (1,2,3). Not sure if this is what you’re looking for.<br>
Edit: sorry, I misunderstood. Like it was said above, you could make a script and write not only the name, but a new field in the nrrd header like DICOM.PatientID, and it’ll appear in the nrrd when opened in any text editor.</p>

---
