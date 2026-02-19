---
topic_id: 40114
title: "Dicom Loading Could Not Load Unnamed Series As A Scalar Volu"
date: 2024-11-11
url: https://discourse.slicer.org/t/40114
---

# DICOM loading - Could not load: Unnamed Series as a Scalar Volume

**Topic ID**: 40114
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/dicom-loading-could-not-load-unnamed-series-as-a-scalar-volume/40114

---

## Post #1 by @mhal0018 (2024-11-11 03:50 UTC)

<p>Hi there.<br>
I’m trying to load DICOM files downloaded from the Aneurisk database, specifically patient C0051 (<a href="http://ecm2.mathcs.emory.edu/aneuriskweb/repository#" class="inline-onebox" rel="noopener nofollow ugc">AneuriskWeb</a>).<br>
I’m getting the ‘Could not load: Unnamed Series as a Scalar Volume’ error, and having a look at the metadata there’s some fields missing (I’ve tried adding in Patient Name and Patient ID and the problem still persists).</p>
<p>I’ve had a look at the DICOM documentation (<a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.10/FAQ/DICOM - Slicer Wiki</a>) but I can’t figure out what fields I’m missing. I’m using pydicom to add in any metadata I’m missing. Could someone please help me figure out what extra fields I need?</p>
<p>Thankyou!</p>

---

## Post #2 by @pieper (2024-11-11 13:55 UTC)

<p>These are pretty poorly formed files so you’ll need to dig around to figure them out.</p>
<p>Be sure to see the latest documenation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>
<p>One thing to investigate is <a href="https://dclunie.com/dicom3tools/dciodvfy.html">dciodvfy</a>.</p>
<p>It points to several issues:</p>
<pre><code class="lang-auto">~/Downloads/dicom3tools_macexe_1.00.snapshot.20241003102953/dciodvfy /tmp/C0051/dicom/IM_00769
Error - MediaStorageSOPClassUID but missing SOPClassUID and not a directory
Warning - Missing attribute or value that would be needed to build DICOMDIR - Patient ID
Warning - Missing attribute or value that would be needed to build DICOMDIR - Study Date
Warning - Missing attribute or value that would be needed to build DICOMDIR - Study Time
Warning - Missing attribute or value that would be needed to build DICOMDIR - Study ID
Warning - Missing attribute or value that would be needed to build DICOMDIR - Series Number
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x0008,0x0001) UL Length to End 
Warning - Retired attribute - (0x4008,0x0212) CS Interpretation Status ID 
Warning - Dicom dataset contains retired attributes
Error - Information Object Not found
</code></pre>
<p>Please report back if you figure this out.</p>

---
