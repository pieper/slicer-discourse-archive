---
topic_id: 34915
title: "Long Loading Time For Dicom Folder"
date: 2024-03-15
url: https://discourse.slicer.org/t/34915
---

# Long loading time for DICOM folder. 

**Topic ID**: 34915
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/long-loading-time-for-dicom-folder/34915

---

## Post #1 by @Frederik (2024-03-15 15:48 UTC)

<p>Dear 3D Slicer Team.</p>
<p>We are a small team who are currently segmenting and annotating data from a larger dataset containing CT Thorax DICOM containing Lung Nodules.</p>
<p>First of all, we would like to express our gratitude. We are extremely thankfull for your services and are very satisfied in general.</p>
<p>Our problem:</p>
<p>To save time, we have dissected the filepaths pre-3Dslicer so only relevant scan files are imported.</p>
<p>When importing DICOM folders, we experience 2 problems:</p>
<ol>
<li>
<p>The loadbar tend to stall at 94%. This can go on for several minutes.<br>
we have performed stress tests on our computers and tried it on multiple computers as well, but the issue remains.</p>
</li>
<li>
<p>When choosing a scan file in uploaded DICOM, the process stalls at<br>
DICOMEnhancedUSVolumeplugin and DICOMGeAbusPlugin, but espicially at DICOMScalarVolumePlugin and MultiVolumeImporterPlugin.</p>
</li>
</ol>
<p>Do you have any recommendations for optimizing? Do you know, if previos releases are without these Volume-Plugins?</p>
<p>Thank you for your services.</p>
<p>Best regards</p>
<p>Frederik A and Team.</p>

---

## Post #2 by @pieper (2024-03-15 18:52 UTC)

<p>Glad things are working for you generally.  Regarding your questions:</p>
<ol>
<li>
<p>The import process is pretty optimized.  If you can demonstrate with public data a case where you think things are slower than they should be perhaps we can investigate.  If you can’t share something reproducible you may need to test yourself.  One thing is to be sure the database directory is on a local disk.  Maybe also try small batches of data and see if the performance is linear or if there’s some slowdown for bigger chunks.</p>
</li>
<li>
<p>Here you can improve performance by turning off some plugins you don’t need (see the options in the lower left of the dicom module panel).  In fact, if you turn these off before importing they might speed things up too - let us know if you see that.</p>
</li>
</ol>

---
