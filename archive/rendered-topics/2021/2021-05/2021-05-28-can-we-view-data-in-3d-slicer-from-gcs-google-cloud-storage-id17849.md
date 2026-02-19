---
topic_id: 17849
title: "Can We View Data In 3D Slicer From Gcs Google Cloud Storage"
date: 2021-05-28
url: https://discourse.slicer.org/t/17849
---

# Can we view Data in 3D slicer from GCS (Google Cloud Storage) Bucket? Is there any workaround that can be followed in order to achieve this?

**Topic ID**: 17849
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/can-we-view-data-in-3d-slicer-from-gcs-google-cloud-storage-bucket-is-there-any-workaround-that-can-be-followed-in-order-to-achieve-this/17849

---

## Post #1 by @Coder (2021-05-28 20:46 UTC)

<p>Operating system: Using DockerSlicer Image to host 3d slicer<br>
Slicer version: 4.10</p>

---

## Post #2 by @Coder (2021-06-04 17:06 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Is there any plugin or extension which can connect slicer to GCS bucket?</p>

---

## Post #3 by @lassoan (2021-06-04 20:58 UTC)

<p>It should be no problem.</p>
<p>For example, I know that it works with the DICOMwebBrowser extension (you can browse a DICOMweb database, filter, download, locally cache, and display any DICOM data set).</p>
<p>For generic file access, you can use standard Python packages. Maybe <a class="mention" href="/u/pieper">@pieper</a> can give advice about authentication and other best practices in Slicer’s Python environment.</p>
<p>What is your end goal?</p>

---

## Post #4 by @Coder (2021-06-04 21:04 UTC)

<p>Assuming the data user  wants to view is on cloud GCS(Google storage bucket) and not locally so want to directly connect this bucket to slicer.</p>

---

## Post #5 by @lassoan (2021-06-05 00:23 UTC)

<p>What kind of data sets do you need to access and how do you find what data set you want to load? If you use DICOM then a good option is to set up <a href="https://cloud.google.com/healthcare/docs/how-tos/dicomweb">DICOMweb access</a> because then you can access the data using a standard interface from a wide variety of applications (e.g., 3D Slicer, web viewers such as OHIF).</p>

---

## Post #6 by @pieper (2021-06-07 20:39 UTC)

<p>If you can assume the user installs the <a href="https://cloud.google.com/sdk/docs/install">Google Cloud SDK</a> utilities (gcloud and gsutil) then you can use them from Slicer like <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py#L1083-L1102">we do here</a>.  Depending on what you want to do it might be more efficient to use <a href="https://cloud.google.com/python/docs/reference">the python libraries</a> to access APIs directly.</p>

---
