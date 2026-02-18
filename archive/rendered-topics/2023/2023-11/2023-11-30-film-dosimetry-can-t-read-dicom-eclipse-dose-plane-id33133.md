# film dosimetry . Can´t read dicom eclipse dose plane 

**Topic ID**: 33133
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/film-dosimetry-can-t-read-dicom-eclipse-dose-plane/33133

---

## Post #1 by @Carlos_Lujan (2023-11-30 04:47 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.8<br>
Expected behavior:film dosimetry Load dicom data<br>
Actual behavior:Eclipse dicom dose plane load freezes at 40%<br>
When I want to load the dicom dose plane extracted from eclipse, in the FILM Dosimetry Analysis application, the file loading freezes at 40%. Eclipse is version 15.6.<br>
I greatly appreciate the help!<br>
Carlos</p>

---

## Post #2 by @cpinter (2023-11-30 09:36 UTC)

<p>Hi Carlos,</p>
<p>Unfortunately said extension is not maintained anymore for several years, and I have to say it was never in a satisfactory condition regarding versatility etc.</p>
<p>If you have the capacity to try to fix the issue yourself, I’m happy to provide you guidance.</p>
<p>Normally we’d say that instead of using such an old version of Slicer update to the latest one, however, I’m fairly sure that more work would be needed in the latest Slicer.<br>
Still, using the latest Slicer that is known to work well with the extension would be a good idea. So for starters, I suggest that you use the version that the latest tutorial (linked from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/FilmDosimetry">this page</a>) was created with, which is 4.11. Since that version cannot be downloaded anymore I dug around in my files and found this one, which is pretty close<br>
<a href="https://1drv.ms/u/s!Ao_a-dPPX98Zhu4Qc0coDFB7dpiMcA?e=D2CzuS">Slicer-4.11.0-2020-07-20-win-amd64.exe</a></p>
<p>Can I ask you to install and try this Slicer?</p>

---
