# How can I open a 3DVolume on 3DSlicer?

**Topic ID**: 35963
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/how-can-i-open-a-3dvolume-on-3dslicer/35963

---

## Post #1 by @vieimar (2024-05-07 13:06 UTC)

<p>Hello everyone,</p>
<p>I’m trying to open a Volume3D file on 3DSlicer in order to create a 3D file and then import it into STL. I’m still new to using 3DSlicer, is there a particular method to import it?</p>
<p>I have images in DICOM format, I went to the DICOM importer module and then tried to open the file and selected Volume, but it gives me errors, I don’t understand why. I have version 5.6.2 of 3DSlicer. In the same way, I tried using the “FreeSurfer Model” module but it seems that the internal network is blocking access to certain libraries, in fact the error says that I can’t install “NiBabel” or “pip” even though I have reinstalled the latest version of Python and checked and made sure pip is checked.</p>
<p>Additionally, I went to check in Application Settings and the file where Python is located is properly applied. Have you ever encountered similar errors?<br>
Thank you for your help, if you have any tutorials I’m interested. Have a good day.</p>

---

## Post #2 by @muratmaga (2024-05-08 02:59 UTC)

<aside class="quote no-group" data-username="vieimar" data-post="1" data-topic="35963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ee7513/48.png" class="avatar"> vieimar:</div>
<blockquote>
<p>elected Volume, but it gives me errors,</p>
</blockquote>
</aside>
<p>please copy and paste the actual error. There are many non-compliant dicom files out there. Often running them through the DICOM Patcher module will correct the issue and then you can import the corrected version via the DICOM module.</p>

---

## Post #4 by @vieimar (2024-05-13 11:56 UTC)

<p>Hello sir, thank you for your response. I found a way to import it since las t week. I think I have a problem with Python…</p>

---
