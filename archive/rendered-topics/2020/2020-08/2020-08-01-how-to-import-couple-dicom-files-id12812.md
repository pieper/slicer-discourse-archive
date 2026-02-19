---
topic_id: 12812
title: "How To Import Couple Dicom Files"
date: 2020-08-01
url: https://discourse.slicer.org/t/12812
---

# How to import couple dicom files

**Topic ID**: 12812
**Date**: 2020-08-01
**URL**: https://discourse.slicer.org/t/how-to-import-couple-dicom-files/12812

---

## Post #1 by @Vitalii_Shmadiuk (2020-08-01 04:23 UTC)

<p>Hi, can you help mi please. How to import couple around 30 small dicom files? That files it is a segmentation of one hall Dicom file.</p>

---

## Post #2 by @lassoan (2020-08-01 04:25 UTC)

<p>What kind of segmentation? RT structure set or Segmentation object? You need to install SlicerRT extension to be able to import the former, and QuantitativeReporting extension to import the latter. If you run into any issues, follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser">these instructions</a>.</p>

---
