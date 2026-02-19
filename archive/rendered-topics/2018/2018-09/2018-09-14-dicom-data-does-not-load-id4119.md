---
topic_id: 4119
title: "Dicom Data Does Not Load"
date: 2018-09-14
url: https://discourse.slicer.org/t/4119
---

# DICOM data does not load

**Topic ID**: 4119
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/dicom-data-does-not-load/4119

---

## Post #1 by @bouliane (2018-09-14 15:04 UTC)

<p>Operating system:IOS 10.13.6<br>
Slicer version: 4.9.0<br>
Expected behavior: images open when I click “load”<br>
Actual behavior: nothing happens, no images appear</p>
<p>I can see the series in the database and they appear in the DICOM browser, but nothing happens when I try to load them.</p>

---

## Post #2 by @timeanddoctor (2018-09-14 15:13 UTC)

<p>can you load the datas with DICOM module?</p>

---

## Post #3 by @cpinter (2018-09-14 15:15 UTC)

<p>Is there a crash or just nothing happens?</p>
<p>Can you paste the log here? You can find it in the menu About / Report a problem</p>
<p>If you switch to DCMTK as DICOM loader in Edit / Application Settings then does it load?</p>

---

## Post #4 by @bouliane (2018-09-14 15:46 UTC)

<p>Yes</p>
<p>It shows up as loaded data</p>
<p>But still no images</p>
<details>
<summary>
signature</summary>
<p>Martin Bouliane MD FRCS ©</p>
<p>Assistant Clinical Professor</p>
<p>University of Alberta</p>
<p>Department of Surgery</p>
<p>Division of Orthopedics</p>
<p>The content of this email communication, including any attachments, is considered confidential, privileged or otherwise exempt from disclosure. It is intended only for the person(s) to whom it is addressed, and further distribution is strictly prohibited without the consent of the original sender. If you have received this message in error, please immediately notify the sender by return email, and delete this communication. Thank you.</p>
</details>

---

## Post #5 by @bouliane (2018-09-14 15:51 UTC)

<p>Ok</p>
<p>I will try</p>
<p>I had to go to work</p>
<p>So will have to do it  later</p>
<p>Thanks</p>
<details>
<summary>
signature</summary>
<p>Martin Bouliane MD FRCS ©</p>
<p>Assistant Clinical Professor</p>
<p>University of Alberta</p>
<p>Department of Surgery</p>
<p>Division of Orthopedics</p>
<p>The content of this email communication, including any attachments, is considered confidential, privileged or otherwise exempt from disclosure. It is intended only for the person(s) to whom it is addressed, and further distribution is strictly prohibited without the consent of the original sender. If you have received this message in error, please immediately notify the sender by return email, and delete this communication. Thank you.</p>
</details>

---

## Post #6 by @Andinet_Enquobahrie (2018-09-14 19:02 UTC)

<p>there are some good pointers at</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>

---

## Post #7 by @bouliane (2018-09-22 19:07 UTC)

<p>Hi</p>
<p>Still stuck….I think when I am loading the CT scan DICOM data there may be too much information. All the series are being loaded (ie the axial, sag, coronal, 3D RECON, scout etc)</p>
<p>Should I maybe just load the axial images?</p>
<p>The problem is I can see all the series in the DICOM browser but when I try to load them (by clicking on the axial series), nothing happens.</p>
<p>Not sure this will be something that I can solve on my own, but the power of this program is my ability to segment certain bones from one another, although it is labour intensive. (Humerus from the scapula)</p>
<p>Marty</p>

---

## Post #8 by @lassoan (2018-09-23 13:06 UTC)

<aside class="quote no-group" data-username="bouliane" data-post="7" data-topic="4119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> bouliane:</div>
<blockquote>
<p>All the series are being loaded (ie the axial, sag, coronal, 3D RECON, scout etc)</p>
<p>Should I maybe just load the axial images?</p>
</blockquote>
</aside>
<p>Yes, sure, just load what you need by selecting the series that you are interested in. If you select an entire patient or entire study then Slicer will try to load all the associated series, including those that are not usable for much or cannot be even imported (scout scans, dose reports, secondary captures, etc.).</p>
<aside class="quote no-group" data-username="bouliane" data-post="7" data-topic="4119">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/67e7ee/48.png" class="avatar"> bouliane:</div>
<blockquote>
<p>The problem is I can see all the series in the DICOM browser but when I try to load them (by clicking on the axial series), nothing happens.</p>
</blockquote>
</aside>
<p>You can click Advanced checkbox and examine metadata to make sure that is a valid series. You may also check application logs to see if any error is reported.</p>
<p>If you think that something should be possible to load but it does not work then you may send us anonymized version of the data that we can analyze.</p>

---

## Post #9 by @bouliane (2018-10-20 01:47 UTC)

<p>Hi</p>
<p>I am trying to load the DICOM data and it is really hard…</p>
<p>I can now get the data to load partly but the scans are not there in there in their entirety…. part of them are cut off…</p>
<p>I have included a screen shot of what is happening…What is the problem? You can see that a large part of the image is cropped even thought the entire series has been loaded.</p>
<p>FYI…OSIRIX loads them fine, but I am unable to segment in that application.</p>
<p>Any thoughts?</p>
<p>Marty</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e269de1fcc49ecd9145dc93ddf7a845f10d753.png" alt="image" data-base62-sha1="tNSoXJP1yRmB2vODcnNmvOI5VhV" width="640" height="439"></p>

---

## Post #10 by @lassoan (2018-10-20 17:34 UTC)

<p>You may have loaded multiple series. You can choose in Data module what is shown.</p>
<p>You may also align slice views with the volume’s acquisition planes (click “Rotate to volume plane” button in the slice view controller).</p>

---
