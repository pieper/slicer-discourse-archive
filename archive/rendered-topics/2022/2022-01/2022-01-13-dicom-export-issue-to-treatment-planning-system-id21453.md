---
topic_id: 21453
title: "Dicom Export Issue To Treatment Planning System"
date: 2022-01-13
url: https://discourse.slicer.org/t/21453
---

# DICOM Export Issue to Treatment Planning System

**Topic ID**: 21453
**Date**: 2022-01-13
**URL**: https://discourse.slicer.org/t/dicom-export-issue-to-treatment-planning-system/21453

---

## Post #1 by @sdomal (2022-01-13 20:41 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20200930<br>
Expected behavior: I am trying to export a virtual phantom as a DICOM image set as to be read in by a treatment planning system, specifically RayStation. I am exporting as “Int” output and with a Rescale Intercept of 0 and Rescale Slope of 1.</p>
<p>Actual behavior: When I try to import the DICOM series into RayStation I get the following error:   <span class="hashtag">#707</span> 2.16.840.1.114362.1.11843457.24057291391.599878543.576.8207 CT: Rescale Type (0028,1054) failed IsAnyOf validation</p>
<p><span class="hashtag">#708</span> Error while importing CT: If the Rescale Type attribute is defined it must be HU (Hounsfield unit) [CT image module]</p>
<p>at RaySearch.CorePlatform.Dicom.ImportExport.DicomInterface.DicomErrorHandler.FatalError(String format, Object[] args)</p>
<p>at RaySearch.CorePlatform.Presentation.Actions.ImportExport.DicomSeriesImportAction.Import_(IList`1 iods)</p>
<p>at RaySearch.CorePlatform.Presentation.Actions.ImportExport.DicomSeriesImportAction.DoWork_()</p>
<p>Are there export options I need to change to work around this issue?</p>

---

## Post #2 by @lassoan (2022-01-13 20:43 UTC)

<p>Thanks for reporting this. As far as I remember, this issue has been fixed a while ago. Please let us know if I there are problems with images exported by the latest Slicer Preview Release.</p>

---

## Post #3 by @sdomal (2022-01-14 00:07 UTC)

<p>Thank you for your reply, for some reason the current download for the preview version of Slicer for windows is just an empty zip file. I did however update to the newest stable version of slicer and tried again but this time I got the following error:</p>
<p><span class="hashtag">#3767</span> 1.2.826.0.1.3680043.2.1125.1.90325020486013685008757661786594524 CT: Bits Allocated (0028,0100) failed IsAnyOf validation (occurences: 2)<br>
<span class="hashtag">#3768</span> 1.2.826.0.1.3680043.2.1125.1.90325020486013685008757661786594524 CT: Bits Stored (0028,0101) failed IsAnyOf validation<br>
<span class="hashtag">#3769</span> Error while importing CT: The attribute Bits Allocated must have the value 16. [Image pixel]</p>
<p>at RaySearch.CorePlatform.Dicom.ImportExport.DicomInterface.DicomErrorHandler.FatalError(String format, Object[] args)<br>
at RaySearch.CorePlatform.Presentation.Actions.ImportExport.DicomSeriesImportAction.Import_(IList`1 iods)<br>
at RaySearch.CorePlatform.Presentation.Actions.ImportExport.DicomSeriesImportAction.DoWork_()</p>
<p>I’m a bit confused on this error but even more so about all of the export options, namely what output type I should be using, for this trial I used “Int”.</p>

---

## Post #4 by @jamesobutler (2022-01-14 03:04 UTC)

<p>Looks like last nights Preview build on Windows didn’t upload correctly. You can use the one from the day before by using the following download link</p>
<p><a href="https://slicer-packages.kitware.com/api/v1/file/hashsum/SHA512/a81c6d17414024929ea38f1cf7ce6fcff47ccd5f103c6711f9582a4a922e19c83d7a65f206b31d589e034249c1967080f0cc01e8bc2e26fbb79901566c5c8c2b/download" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/file/hashsum/SHA512/a81c6d17414024929ea38f1cf7ce6fcff47ccd5f103c6711f9582a4a922e19c83d7a65f206b31d589e034249c1967080f0cc01e8bc2e26fbb79901566c5c8c2b/download</a></p>

---
