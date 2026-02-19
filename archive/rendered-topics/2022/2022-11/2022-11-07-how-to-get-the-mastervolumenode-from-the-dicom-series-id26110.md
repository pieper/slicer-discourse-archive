---
topic_id: 26110
title: "How To Get The Mastervolumenode From The Dicom Series"
date: 2022-11-07
url: https://discourse.slicer.org/t/26110
---

# How to get the masterVolumeNode from the dicom series

**Topic ID**: 26110
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/how-to-get-the-mastervolumenode-from-the-dicom-series/26110

---

## Post #1 by @user_ghost (2022-11-07 13:39 UTC)

<p>hello every teachers:<br>
I used python code to load the ct dicom files, then i want to get the masterVolumeNode  from the dicom file ,<br>
the load dicom files as followes:</p>
<pre><code class="lang-python">def loadCtData():
    dicomDataDir = "D:/xgx/newdicom"  
    ###"D:\301\15\443250"  "D:/301/15/443250"
    loadedNodeIDs = []  

    from DICOMLib import DICOMUtils
    with DICOMUtils.TemporaryDICOMDatabase() as db:
        DICOMUtils.importDicom(dicomDataDir, db)
        patientUIDs = db.patients()
        for patientUID in patientUIDs:
            loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
        print(type(db))
</code></pre>

---

## Post #2 by @lassoan (2022-11-07 19:18 UTC)

<p>You can get the referenced volume node from the segmentation via the <code>referenceImageGeometryRef</code> node reference. For example:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
volumeNode = segmentationNode.GetNodeReference('referenceImageGeometryRef')
</code></pre>

---

## Post #3 by @user_ghost (2022-11-17 05:23 UTC)

<p>ok, i wlii try, thanks</p>

---
