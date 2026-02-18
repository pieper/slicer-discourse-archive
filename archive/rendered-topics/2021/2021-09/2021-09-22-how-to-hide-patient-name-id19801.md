# How to hide patient name

**Topic ID**: 19801
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/how-to-hide-patient-name/19801

---

## Post #1 by @akmal871026 (2021-09-22 02:22 UTC)

<p>Does anyone know how to hide the patient name in all views?</p>

---

## Post #2 by @chir.set (2021-09-22 07:00 UTC)

<p>Have a look at DataProbe module.</p>

---

## Post #3 by @akmal871026 (2021-09-22 07:07 UTC)

<p>I mean on this side<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53a3bc77804bc56673d9e19989daea13b3b6edb2.jpeg" data-download-href="/uploads/short-url/bVUqRlVfMq9BnR8Kp9BSb2wBUXM.jpeg?dl=1" title="IMG-20210922-WA0010" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53a3bc77804bc56673d9e19989daea13b3b6edb2.jpeg" alt="IMG-20210922-WA0010" data-base62-sha1="bVUqRlVfMq9BnR8Kp9BSb2wBUXM" width="690" height="387" data-dominant-color="9594A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG-20210922-WA0010</span><span class="informations">1080×607 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Name in red circle</p>

---

## Post #4 by @Alex_Vergara (2021-09-22 08:34 UTC)

<p>Anonymize before uploading to Slicer OR rename patient name in the Data module (double click on name)</p>

---

## Post #5 by @akmal871026 (2021-09-22 09:27 UTC)

<p>how to Anonymize sir?</p>

---

## Post #6 by @chir.set (2021-09-22 09:35 UTC)

<p>Check ‘Create a DICOM series’ module.</p>

---

## Post #7 by @Alex_Vergara (2021-09-22 10:44 UTC)

<p>If you have your DICOM folder, before importing into Slicer you can use my <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/OpenDose3D/Logic/CLIScripts/anonymise.py" rel="noopener nofollow ugc">anonymization script</a> if you like.</p>

---

## Post #8 by @rbumm (2021-09-22 11:29 UTC)

<p>Alternatively, you could save your non-anonymized CT dataset as ct.nrrd file, then close scene and reopen ct.nrrd .</p>

---

## Post #9 by @akmal871026 (2021-09-27 14:55 UTC)

<p>How to save in nrrd file?</p>

---

## Post #10 by @rbumm (2021-09-27 18:57 UTC)

<p>Import the DICOM series to Slicer and just “Save” the series, there is a *.nrrd option.</p>

---
