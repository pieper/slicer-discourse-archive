# Export RTStruct referencing original volume

**Topic ID**: 9771
**Date**: 2020-01-10
**URL**: https://discourse.slicer.org/t/export-rtstruct-referencing-original-volume/9771

---

## Post #1 by @rmd (2020-01-10 04:39 UTC)

<p>Hi Everyone,</p>
<p>I’m trying to use the DicomRtImportExportPlugin python module to export RTStructs associated with a CT volume (call it the original volume). When I use the exporter it creates a new CT volume (same pixel values but different SOPInstanceUIDs) and the RTStruct references the new volume. Is there any way to export a RTStruct that references the original volume? The rest of my colleagues are using the original image volumes so it would be nice to have the RTStructs reference those.</p>
<p>Happy to provide code snippets if/when it would be useful.</p>
<p>Thanks</p>
<p>Operating system: Windows<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @cpinter (2020-01-11 09:04 UTC)

<p>This is a very fair request. Unfortunately right now we can only export with the duplicate CT, creating all new UIDs. Export is done by Plastimatch (<a href="https://gitlab.com/plastimatch/plastimatch/blob/master/src/plastimatch/base/rt_study.h#L65-68">here</a>) and it was designed to export an all-new study.</p>
<p>We already have ha many discussions about exporting DICOM series to existing study, see for example here: <a href="https://issues.slicer.org/view.php?id=3937">https://issues.slicer.org/view.php?id=3937</a><br>
So far, however, none of the developers have had enough time and push to make it happen. Contributions are very welcome.</p>
<p>As an alternative, you can manually change DICOM tags such as study ID and referenced CT instance UID. But I know that if you need to do it as part of a regular workflow it is not feasible.</p>

---

## Post #3 by @gcsharp (2020-01-11 19:42 UTC)

<p>If you are willing use plastimatch, you can do this:</p>
<p>plastimatch convert --input RTSTRUCT.dicom --referenced-ct dicom-ct-directory/ --output-dicom output/</p>

---

## Post #4 by @cpinter (2020-01-13 09:42 UTC)

<p>Good to know! Is it also possible not to re-export the CT and reference the existing one to begin with?</p>

---

## Post #5 by @rmd (2020-01-31 01:01 UTC)

<p>Hi Greg and Csaba,</p>
<p>Thanks for your suggestions. Plastimatch worked well.</p>
<p>I also tried the other solution of writing a python script that would go through the slicer-generated RTStruct (referencing a Slicer-generated volume) and map all the SOPInstanceUIDs and SeriesInstanceUID back to the original volume. I verified that the RTStructs could be opened by Slicer and MiM.</p>
<p>In case it’s useful to the community, I’ve posted the relevant code in it’s own <a href="https://github.com/ryanmdavis/mapRTStructToVolume/blob/master/map_rtstruct_to_volume.py" rel="nofollow noopener">github repo</a>.</p>
<p>Ryan</p>

---

## Post #6 by @cpinter (2020-01-31 11:01 UTC)

<p>Excellent, thanks for reporting back! Special thanks for sharing your script <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
