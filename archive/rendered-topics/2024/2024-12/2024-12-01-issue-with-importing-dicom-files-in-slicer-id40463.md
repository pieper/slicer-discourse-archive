# Issue with Importing DICOM Files in Slicer

**Topic ID**: 40463
**Date**: 2024-12-01
**URL**: https://discourse.slicer.org/t/issue-with-importing-dicom-files-in-slicer/40463

---

## Post #1 by @rcabeza (2024-12-01 17:43 UTC)

<p>Hello everyone,</p>
<p>I am encountering an issue when importing DICOM files. I am working with version 5.6.4 of Slicer.</p>
<p>The details are as follows:</p>
<ol>
<li>I have around 300 MRI studies, each including series for examining the patient’s thigh. These series consist of a locator scan, performed in the coronal plane, and an axial series for quantifying the mid-thigh region. The same acquisition protocol was essentially used for all these studies.</li>
<li>After importing the DICOM files into Slicer, I noticed that some studies have the quantification series displayed in an inverted orientation (upside down) and with incorrect voxel spacing (default value of 1 mm). The locator scan is always correctly oriented and has the correct voxel size.</li>
<li>During the DICOM file import process, several warnings are displayed, but they are exactly the same for the series that are read incorrectly as for those imported correctly.</li>
<li>We tested the files with other viewers (Weasis, Radiant, Syngo), and all of them correctly read all the series.</li>
<li>If the “Interoperability” option is enabled when exporting studies from the MRI workstation, Slicer correctly imports the DICOM data and displays the volumes properly. When this option is enabled, each slice is saved in a separate individual DICOM file, whereas initially, there is one DICOM file per entire series.</li>
</ol>
<p>I am unable to determine which parameter in the DICOM header causes Slicer to interpret some studies correctly and others incorrectly. I can share two studies of each type to help debug the import process.</p>
<p>Best regards, and many thanks in advance.</p>

---

## Post #2 by @lassoan (2024-12-01 17:44 UTC)

<p>Thanks for reporting. Please test with the latest Slicer Preview Release and if the problem is still there then it would be great if you could share sample data sets.</p>

---

## Post #3 by @rcabeza (2024-12-01 21:54 UTC)

<p>Good morning again,<br>
I’m very grateful for your quick response.<br>
I have tested with version 5.7.0 revision 33134, and the result is identical.<br>
I should mention, in case it sheds some light, that with the <strong>ImageSeriesReader()</strong> function from SimpleITK in Python, I get the same behavior as with Slicer.<br>
I’m sharing the link to the ZIP file containing the volumes with you, Andras, via private message.</p>
<p>Best regards, and many thanks again,<br>
Rafa</p>

---

## Post #4 by @rcabeza (2024-12-04 22:55 UTC)

<p>Hello everyone<br>
I share the four volumes: two imported properly and two imported with wrong orientation.<br>
<a href="https://unavarra-my.sharepoint.com/:u:/g/personal/rcabeza_unavarra_es/EbQjfHXJ-39MgD0sXIAdSrgBf2OqFM8byT7ZZqa_tsurRw?e=FKbLEJ" rel="noopener nofollow ugc">2share_dicom_files</a><br>
Best regards and thank you very much in advance<br>
Rafael Cabeza</p>

---

## Post #5 by @pieper (2024-12-05 15:58 UTC)

<p>Thanks for sharing these.  The dicom files are multiframe, of a format that is fairly new and not seen a lot, which is why you get the warning messages when loading and you see the inconsistent behavior.</p>
<p>The good news is that there appears to be plenty of metadata in the header, including all the parameters (orientation and position of the frames) to reconstruct volumes and perform analysis.  On the other hand, many of the acquisition parameters are in private tags, and they may or may not be interpretable to fully process the scan.</p>
<p>In any case with a bit of python scripting it should be possible to robustly interpret these scans.  It would be great to see a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-plugins">DICOMPlugin</a> that detects and properly interprets this kind of data.</p>

---
