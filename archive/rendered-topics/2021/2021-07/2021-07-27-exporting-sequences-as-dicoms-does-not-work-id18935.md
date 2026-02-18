# Exporting Sequences as Dicoms does not work

**Topic ID**: 18935
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/exporting-sequences-as-dicoms-does-not-work/18935

---

## Post #1 by @shehab (2021-07-27 02:19 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13.0-2021-07-22<br>
Expected behavior:<br>
Generation of 768 dicoms after I export the sequence with the VolumeSequence option selected<br>
Actual behavior:<br>
Either a message stating “Error occured in exporter” pops up, or after a bit of gimmicking it says export successful and it exports nothing.<br>
Background:<br>
I am using the sequence registration extension to register 2D+t perfusion studies (generic rigid transformation). The registration process goes quite smoothly and rapidly, however, whenever I try to export it always ends up failing. The sequence replay of the registration checks out and the result registered, so its not an issue with registration or the sequence; its just the exporting. I would like to avoid exporting every frame of the sequence as separate volume.</p>

---

## Post #2 by @lassoan (2021-07-27 18:20 UTC)

<p>We don’t have a DICOM exporter for volume sequences, but you can easily write a simple Python script for this. All you need to do is to iterate through the sequence and export each volume as it is done in the <a href="https://github.com/Slicer/Slicer/blob/2d1e1d819a8cf410b025e8f4c523280860b5c736/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L98-L163">scalar volume exporter</a>.</p>
<p>If you share your final script with us then we can turn it into a DICOM exporter plugin that can be used via GUI.</p>

---

## Post #3 by @shehab (2021-08-01 04:42 UTC)

<p>I tried to take on coding the DicomVolumeSequence script like you told me in your answer to my question, but first I tried debugging the existing DicomVolumeSequencePlugin in here: <a href="https://github.com/SlicerRt/Sequences/blob/master/DicomVolumeSequencePlugin/DicomVolumeSequencePlugin.py" rel="noopener nofollow ugc">Sequences/DicomVolumeSequencePlugin.py at master · SlicerRt/Sequences · GitHub</a>.</p>
<p>I found the source of the errors: DICOMExportScalarVolume.py expects the tags dictionary to contain Patient Birth Date and Patient Sex, which weren’t provided by the DicomVolumeSequence tag dictionary. I just wrote 2 lines of code to get those parameters into the DicomVolumeSequence tag dictionary.</p>
<p>The second error was with the datetimefromDicom method, which always seemed to raise the Oserror unless I formatted my inputs perfectly so I commented the else raises out. I don’t think this is a correct solution but it worked for my case so I didn’t really care too much.</p>
<p>In total I commented lines 121,122,146 and 147 out, and added lines 195 and 196 as:<br>
tags[‘Patient Birth Date’] = exportable.tag(slicer.vtkMRMLSubjectHierarchyConstants.GetDICOMPatientBirthDateTagName())<br>
tags[‘Patient Sex’] = exportable.tag(slicer.vtkMRMLSubjectHierarchyConstants.GetDICOMPatientSexTagName())</p>

---

## Post #4 by @lassoan (2021-09-14 19:46 UTC)

<p>Thank you <a class="mention" href="/u/shehab">@shehab</a>.<br>
<a class="mention" href="/u/cjohnson">@CJohnson</a> submitted these suggested changes in a <a href="https://github.com/Slicer/Slicer/pull/5853">pull request</a> that has now been merged into Slicer master.</p>

---
