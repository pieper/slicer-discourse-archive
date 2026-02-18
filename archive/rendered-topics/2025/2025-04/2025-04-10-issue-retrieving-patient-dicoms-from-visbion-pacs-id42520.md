# Issue Retrieving Patient DICOMS from Visbion PACS

**Topic ID**: 42520
**Date**: 2025-04-10
**URL**: https://discourse.slicer.org/t/issue-retrieving-patient-dicoms-from-visbion-pacs/42520

---

## Post #1 by @sandigeeup (2025-04-10 13:04 UTC)

<p>Hi I am using the Dicom Networking, Query and Retrieve option to access a Visbion PACS system. I am able to retrieve the DICOM using the ID and it says Retrieve Process finished, however it then does not appear in my show dicom database, nor does it appear in the destination database location. Can anyone help with this, I have checked my firewall and re-downloaded Slicer. A colleague has no issues on her system which is set up the same. Many thanks Sandie</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7ec3d6ff7320c3d35d4d9eef8ea1aa21ddd2025.png" data-download-href="/uploads/short-url/qf3waMWa25mxB9H76QK15TszOMR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7ec3d6ff7320c3d35d4d9eef8ea1aa21ddd2025_2_614x500.png" alt="image" data-base62-sha1="qf3waMWa25mxB9H76QK15TszOMR" width="614" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7ec3d6ff7320c3d35d4d9eef8ea1aa21ddd2025_2_614x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7ec3d6ff7320c3d35d4d9eef8ea1aa21ddd2025_2_921x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7ec3d6ff7320c3d35d4d9eef8ea1aa21ddd2025_2_1228x1000.png 2x" data-dominant-color="C7CED6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1815×1476 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2025-04-10 18:59 UTC)

<aside class="quote no-group" data-username="sandigeeup" data-post="1" data-topic="42520">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sandigeeup/48/13722_2.png" class="avatar"> sandigeeup:</div>
<blockquote>
<p>A colleague has no issues on her system which is set up the same</p>
</blockquote>
</aside>
<p>Thanks for the report. Can you also confirm that the same version of Slicer is used in both cases ?</p>

---

## Post #3 by @sandigeeup (2025-04-10 19:31 UTC)

<p>Hi Jean Christophe, my colleague downloaded the latest 5.8.1 release on her Mac, and it worked fine. I’m using Windows 11 and it initially worked with version 5.6.2. to which I initially managed to download one DICOM from the PACS system using DICOM networking, but all subsequent attempts with DICOM IDs reached the point shown in the screenshot and then failed to appear in the DICOM database. I also tried version 5.8.1, but the same issue persists. This is urgent for my PhD project as the PACS system will be replaced by Petcloud next week. I’ve been desperately trying to download all the DICOMs I need before then, but it keeps failing. I’m with Cambridge University.</p>

---

## Post #4 by @jcfr (2025-04-10 20:01 UTC)

<blockquote>
<p>my colleague downloaded the latest 5.8.1 release on her Mac, and it worked fine […]  This is urgent for my PhD project as the PACS system will be replaced by Petcloud next week</p>
</blockquote>
<p>Waiting this is sorted out, you may consider copying the local database directory already available on your colleague workstation onto your own workstation and locally importing the DICOM series from it.</p>
<p>In the interim, would that be a workable solution ?</p>

---

## Post #5 by @sandigeeup (2025-04-11 15:46 UTC)

<p>My colleague is in a different part of the country and the dicoms are currently being transferred to the new cloud platform, however, I think I may have resolved the issue, although it takes along time to download and quite often crashes, before reaching to the dicom database. I will keep trying. Are there any others with issues, do you have a any debugging methods. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @pieper (2025-04-11 16:59 UTC)

<p>Note that DICOM DIMSE, the standard way of communicating with PACS is meant to be a local area network protocol, so using it to access a remote cloud server can lead to slow performance or timeouts.  If possible you should try to use the newer DICOMweb standard, which is designed for this use case.</p>
<p>Note that under the hood Slicer uses DCMTK, which offers some useful command line options that can probably set longer timeouts that could improve the robustness of the transfer.</p>

---

## Post #7 by @lassoan (2025-04-11 17:31 UTC)

<p>The new DICOM browser (that you can actuvate using the dropdown menu of the “Show DICOM database” button has much more advanced and more robust DICOM query/retrieve implementation.</p>
<p>Is your computer and the PACS on the same local network? What protocol does the server support for retrieve: C-GET or C-MOVE? Is your computer registered as known host in the PACS?</p>

---
