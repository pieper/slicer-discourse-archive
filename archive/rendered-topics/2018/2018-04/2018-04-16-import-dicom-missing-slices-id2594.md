---
topic_id: 2594
title: "Import Dicom Missing Slices"
date: 2018-04-16
url: https://discourse.slicer.org/t/2594
---

# Import DICOM missing slices

**Topic ID**: 2594
**Date**: 2018-04-16
**URL**: https://discourse.slicer.org/t/import-dicom-missing-slices/2594

---

## Post #1 by @Joanna (2018-04-16 09:10 UTC)

<p>Hi,<br>
I have 753 DICOM files and want to import into 3DSlicer. But only 516 slices are imported successfully. And the volume information especially slice number and slice thickness of “Z” dimention is incorrect (using volume moduale). How can I import correct slice number and slice thickness? Thanks.</p>
<ol>
<li>
<p>Dialog of import confirmation show there are 753 new instances:<br>
<a href="https://www.screencast.com/t/M4SgjSkqf" rel="nofollow noopener">https://www.screencast.com/t/M4SgjSkqf</a></p>
</li>
<li>
<p>Only 516 slices in metadata:<br>
<a href="https://www.screencast.com/t/D8gvklWl" rel="nofollow noopener">https://www.screencast.com/t/D8gvklWl</a></p>
</li>
<li>
<p>Incorrect of “Z” dimention using volume moduale:<br>
<a href="https://www.screencast.com/t/iSYfSo1ML" rel="nofollow noopener">https://www.screencast.com/t/iSYfSo1ML</a></p>
</li>
<li>
<p>Error log:<br>
<a href="https://www.screencast.com/t/cwmCJi7STVJP" rel="nofollow noopener">https://www.screencast.com/t/cwmCJi7STVJP</a></p>
</li>
</ol>
<hr>
<p>Data type: CBCT<br>
3DSlicer version: Nightly Build<br>
OS: Windows 10 64bit</p>

---

## Post #2 by @lassoan (2018-04-17 03:55 UTC)

<p>You may have several series in your DICOM folder, so it may be normal that one of the series consists of 516 slices.</p>
<p>MicroCT manufacturers often implement DICOM export incorrectly and produces invalid DICOM files; and as the error log shows, your DICOM files are indeed invalid. However, there is a chance that they can still be imported.</p>
<p>You may try DICOM patcher module, which can fix some of the most common errors.</p>
<p>You could share a sample data set (upload to dropbox, onedrive, etc. and copy-paste the link) and we’ll have a look.</p>
<p>You can also complain to your scanner’s manufacturer that they produce invalid DICOM files. Maybe they have an updated version of their software that works better.</p>

---
