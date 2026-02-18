# DICOM network retrieve from PACS - selected item and download crash

**Topic ID**: 21590
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/dicom-network-retrieve-from-pacs-selected-item-and-download-crash/21590

---

## Post #1 by @skyhsu (2022-01-24 04:09 UTC)

<p>Hi ,<br>
I am trying to query and retrieve Dicom data from PACS.<br>
Slicer Version:4.11.20210226<br>
Win-10 Pro 64<br>
And I have a two questions that I want to ask.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5adb789e7ee6d7dc5dfc9cdaa6c353aa7fd9d89a.jpeg" data-download-href="/uploads/short-url/cXLbBp8ul3qQlgmTR6rPSBkvoiS.jpeg?dl=1" title="slicer1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5adb789e7ee6d7dc5dfc9cdaa6c353aa7fd9d89a_2_690x469.jpeg" alt="slicer1" data-base62-sha1="cXLbBp8ul3qQlgmTR6rPSBkvoiS" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5adb789e7ee6d7dc5dfc9cdaa6c353aa7fd9d89a_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5adb789e7ee6d7dc5dfc9cdaa6c353aa7fd9d89a_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5adb789e7ee6d7dc5dfc9cdaa6c353aa7fd9d89a.jpeg 2x" data-dominant-color="596D71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer1</span><span class="informations">1236×841 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol>
<li>please see the attached, the Series Tab<br>
Is there anyway to download the selected Series lists.<br>
It seems to download all items.</li>
<li>Before this download, I have already downloaded 10 patient data , and it’s fine.<br>
But this time, the message will show ‘Got move request’, then suddenly close all windows.<br>
After restart Slicer, it’s the same situation.<br>
So I tried deleting all downloaded patient data, then the download worked fine.<br>
Are there any restrictions on the action of retrieve?</li>
</ol>
<p>Thanks<br>
Sky</p>

---

## Post #2 by @pieper (2022-01-28 13:48 UTC)

<p>There have been some improvements to the <a href="https://github.com/commontk/CTK/tree/master/Libs/DICOM">CTK DICOM code</a> since 4.11, so you could try the latest preview.  I believe <a class="mention" href="/u/rbumm">@rbumm</a> has experience doing large transfers.  in general it’s really hard to debug networking and PACS compatibility issues since few people have appropriate access.  If you have a C++ programmer with networking experience it should be possible to diagnose what’s going on and ideally provide a fix that would benefit all users.</p>

---

## Post #3 by @rbumm (2022-01-28 16:12 UTC)

<aside class="quote no-group" data-username="skyhsu" data-post="1" data-topic="21590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed655f/48.png" class="avatar"> skyhsu:</div>
<blockquote>
<p>then the download worked fine</p>
</blockquote>
</aside>
<p>Are you indicating that in the end, after deleting downloaded patient data (where did you delete them ?)  the transfer of that MRI was successful?</p>

---

## Post #4 by @rbumm (2022-01-28 16:32 UTC)

<aside class="quote no-group" data-username="skyhsu" data-post="1" data-topic="21590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed655f/48.png" class="avatar"> skyhsu:</div>
<blockquote>
<p>Is there anyway to download the selected Series lists.<br>
It seems to download all items.</p>
</blockquote>
</aside>
<p>This request should be solved in 4.13 preview. There you can select individual series.</p>
<p>DICOM retrieval in Slicer is based on the <a href="https://dicom.offis.de/dcmtk.php.en">DCMTK</a> toolkit. If you need to have full DICOM control on your client (automatic reading from your PACS, writing to your PACS) or need to debug the network before using Slicer, this is the tool of choice for you or your DICOM specialist.</p>
<p>However, it would be great if we could lock down the reason for your crash in order to improve Slicer.</p>

---

## Post #5 by @rbumm (2022-01-28 16:44 UTC)

<aside class="quote no-group" data-username="skyhsu" data-post="1" data-topic="21590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed655f/48.png" class="avatar"> skyhsu:</div>
<blockquote>
<p>I have already downloaded 10 patient data</p>
</blockquote>
</aside>
<p>You have downloaded data from 10 other patients?</p>

---

## Post #6 by @skyhsu (2022-02-07 01:55 UTC)

<p>Hi Piper,</p>
<p>Thanks<br>
I will try the latest preview version.</p>

---

## Post #7 by @skyhsu (2022-02-07 02:01 UTC)

<p>Hi rbumm,<br>
Yew , the transfer of that MRI was successful.</p>
<p>I use the Delete function to delete all patient data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9074ed03e76d405cc6c606ba53270bf096f46ad1.png" data-download-href="/uploads/short-url/kBVgCYlDGuppEBxJrjKhbd8hKPD.png?dl=1" title="delete" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9074ed03e76d405cc6c606ba53270bf096f46ad1.png" alt="delete" data-base62-sha1="kBVgCYlDGuppEBxJrjKhbd8hKPD" width="690" height="215" data-dominant-color="405E7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">delete</span><span class="informations">1109×347 19.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #8 by @skyhsu (2022-02-07 02:03 UTC)

<p>Hi rbumm,</p>
<p>I will try the 4.13 preview version</p>
<p>Thanks</p>

---

## Post #9 by @skyhsu (2022-02-07 02:05 UTC)

<p>Yes.<br>
10 different patients.</p>

---
