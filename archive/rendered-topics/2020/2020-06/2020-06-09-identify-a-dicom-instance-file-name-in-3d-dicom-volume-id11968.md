---
topic_id: 11968
title: "Identify A Dicom Instance File Name In 3D Dicom Volume"
date: 2020-06-09
url: https://discourse.slicer.org/t/11968
---

# Identify a DICOM Instance file name in 3D DICOM volume

**Topic ID**: 11968
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/identify-a-dicom-instance-file-name-in-3d-dicom-volume/11968

---

## Post #1 by @Vincent_C (2020-06-09 19:27 UTC)

<p>Hi all,</p>
<p>How can I identify a the file name of a single slice in a loaded 3D DICOM volume? I have loaded a DICOM directory with several hundred slices, but after I have identified a single slice of interest, I would like to know which file name it is.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-06-09 20:31 UTC)

<p>You can get the <code>k</code> (slice) index in the dataprobe and then look up the instanceUID in the attributes, which allows you to look up the filename in the database.  (Use <code>k</code> instead of <code>0</code> in this example and <code>filename</code> will the the one you are looking for.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_a_volume_loaded_from_DICOM.3F_For_example.2C_get_the_patient_position_stored_in_a_volume:</a></p>

---

## Post #3 by @Vincent_C (2020-06-12 01:53 UTC)

<p>Hi Steve,</p>
<p>This is the exact answer I was looking for! Thank you</p>
<p>Vince</p>

---
