# DSCMRIAnalysis extension issue

**Topic ID**: 5519
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/dscmrianalysis-extension-issue/5519

---

## Post #1 by @Shudaizi (2019-01-25 18:28 UTC)

<p>Hello everyone,<br>
I’m new to Slicer and already having such a problem:</p>
<blockquote>
<p>Description: itk::ERROR: itk::ERROR: Unrecognized frame identifying DICOM tag name ContentTime Image C:/…/AppData/Local/Temp/Slicer/IIE_vtkMRMLMultiVolumeNodeC.nrrd does not contain sufficient attributes to support algorithms.</p>
</blockquote>
<p>So it is impossible to use. What can I do with these “insufficient attributes”?</p>
<p>(Slicer 4.11.0-2019-01-21 win-amd64)</p>

---

## Post #2 by @fedorov (2019-01-27 11:25 UTC)

<p>Anna, this means the DSC series was not parsed from DICOM in such a way that contains information needed for modeling. Unfortunately, it is difficult to debug this kind of issues without the dataset. If you can share anonymized dataset, this may be possible to resolve.</p>

---

## Post #3 by @Shudaizi (2019-01-29 06:43 UTC)

<p>Thank you for your response dear Dr. Fedorov!<br>
I supposed that our DICOM might not contain such time related tags which are needed for this extension; i guessed that it needs TriggerTime, AcquisitionTime, SeriesTime and Time, and checked our ones. Our DICOM does contain AcquisitionTime, ContentTime, SeriesTime, InstanceCreationTime, and group of PerformedProcedureStep tags but i didnt found TriggerTime and Time among them. Here are our data: <a href="https://drive.google.com/file/d/1YjEG_4CiSGTGTcVlbgqwJcz8v6WBIl2R/view?usp=sharing" rel="nofollow noopener">https://drive.google.com/file/d/1YjEG_4CiSGTGTcVlbgqwJcz8v6WBIl2R/view?usp=sharing</a></p>

---
