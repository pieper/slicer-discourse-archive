# Problem importing RTSTRUCT

**Topic ID**: 13829
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/problem-importing-rtstruct/13829

---

## Post #1 by @RhysJenks89 (2020-10-02 20:12 UTC)

<p>Operating system: Windows 7 64-bit<br>
Slicer version: 4.10.2 with SlicerRT plugin.<br>
Expected behavior: To import RTSTRUCT file with the rest of the DICOM CT images and be able to see the contoured structures within the RTSTRUCT file.<br>
Actual behavior: DICOM CT images load fine (Series 2). the RTSTRUCT file brings up two error messages when trying to import. I can’t figure this out as I am sure I have done this before, and the files come from the same treatment planning system as before too.</p>
<ol>
<li>
</li></ol>
<p>Warning: Plugin failed: DicomSroImportPlugin<br>
See python console for error message</p>
<ol start="2">
<li>Could not load 1: Unnamed Series as a Scalar Volume.</li>
</ol>
<p>In the python console, the only thing different is:<br>
Reference image in series does not contain geometry information. Please use caution.</p>
<p>Loading with imageIOName: GDCM:<br>
FileFormatError<br>
Loading with imageIOName: DCMTK<br>
FileFormatError</p>
<p>This is probably something simple. I am only exporting the RTSTRUCT and CT DICOM images from the treatment planning system - should I have the plan/dose attached? Can anyone shed any light? Thanks.</p>

---

## Post #2 by @fedorov (2020-10-02 20:17 UTC)

<p>It looks like you are trying to load RTSTRUCT using the ScalarVolume plugin. Can you toggle “Advanced” checkbox in the DICOM Browser and confirm RTSTRUCT loadable is selected in the list?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee0dcf532a1dd6304f247be5a198371c0163854e.png" data-download-href="/uploads/short-url/xXVdYFKuEqXKBkAcHfGbl0yJxq6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee0dcf532a1dd6304f247be5a198371c0163854e_2_690x193.png" alt="image" data-base62-sha1="xXVdYFKuEqXKBkAcHfGbl0yJxq6" width="690" height="193" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee0dcf532a1dd6304f247be5a198371c0163854e_2_690x193.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee0dcf532a1dd6304f247be5a198371c0163854e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee0dcf532a1dd6304f247be5a198371c0163854e.png 2x" data-dominant-color="2B3141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">811×227 9.88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2020-10-03 03:02 UTC)

<p>Please try with latest Slicer stable version (currently, revision 29402). We have made huge improvements in DICOM support since Slicer-4.10.2.</p>

---

## Post #4 by @RhysJenks89 (2020-10-06 14:17 UTC)

<p>I will when I can. The computer is off network (NHS) and any updates etc. have to be done by our in-house IT department and the computer virus-scanned before it can join our local network again. This shouldn’t be the issue, though, as someone helping us locally has opened the RTSTRUCT file on his laptop with no issues.</p>

---

## Post #5 by @RhysJenks89 (2020-10-06 14:49 UTC)

<p>I click the ‘Advanced’ tickbox and this comes up. Nothing appears in the ‘Reader’ column for the RTSTRUCT file, and I get the same errors or it crashes when various tickboxes are unticked and I try to load. (apologies for the poor quality picture).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fa91cd1f2eb537d58c793278d5e2aa2f49b56cf.jpeg" data-download-href="/uploads/short-url/mMqeRUc9OVmhE94CLF7WbvoiN55.jpeg?dl=1" title="pic (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fa91cd1f2eb537d58c793278d5e2aa2f49b56cf_2_690x322.jpeg" alt="pic (2)" data-base62-sha1="mMqeRUc9OVmhE94CLF7WbvoiN55" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fa91cd1f2eb537d58c793278d5e2aa2f49b56cf_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fa91cd1f2eb537d58c793278d5e2aa2f49b56cf_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9fa91cd1f2eb537d58c793278d5e2aa2f49b56cf_2_1380x644.jpeg 2x" data-dominant-color="B4B8B1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic (2)</span><span class="informations">1958×916 724 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @cpinter (2020-10-06 15:16 UTC)

<p>Your screenshot shows that some modules are not loaded successfully. Do you have SlicerRT installed? If so, if you open the module list what is in the Radiotherapy category?</p>

---

## Post #7 by @lassoan (2020-10-06 15:42 UTC)

<p>SlicerRT is installed because “DicomRtImprotExportPlugin” is listed, but there is a DLL load failed.</p>
<p>We have released a new stable version (version 4.11.20200930, revision 29402), please try with that and let us know what you find.</p>

---
