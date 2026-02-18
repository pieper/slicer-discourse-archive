# Slow loading dicom CT slices (~300)

**Topic ID**: 36209
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/slow-loading-dicom-ct-slices-300/36209

---

## Post #1 by @tenzin_kunkyab (2024-05-16 17:14 UTC)

<p>Hi,</p>
<p>I wanted to ask if its normal to take couple of minutes to load CT volume of about 300 slices?</p>
<p>I used to drag + drop, which took long, so importing dicom files was quick. But then loading the actual CT volume to view/segment takes couple of minutes. Although I used an older version of slicer (5.4). Is that the reason?</p>

---

## Post #2 by @pieper (2024-05-16 20:38 UTC)

<p>No, it shouldn’t take that long.  Is there something special about your data compared to sample data?</p>

---

## Post #3 by @tenzin_kunkyab (2024-05-17 18:09 UTC)

<p>Hi,</p>
<p>nothing special, it’s a high-resolution diagnostic CT with about 300 slices. Previously, I drag+dropped the data. The import time was shortened after I correctly loaded the dicom from a file. However, actual loading of the data still takes a bit of time.</p>
<p>Thanks, let me know if there is anything else I should try.</p>

---

## Post #4 by @pieper (2024-05-17 19:00 UTC)

<p>I think the main thing would be to know if there’s something odd going on either with your data or maybe something with your setup.</p>
<p>A 300 slice CT should not take minutes to load.  I just tested a 344 slice 512x512 CT and it loaded in just a couple seconds.</p>
<p>Maybe you can try other datasets or other computers to triangulate on what’s going on.</p>

---

## Post #5 by @tenzin_kunkyab (2024-05-17 19:05 UTC)

<p>The other thing I can think of is that the data is in a shared drive and not on the computer hard drive itself. could that be an issue of the slow loading?</p>
<p>May be I can copy one of the data and try loading from the hard drive.</p>

---

## Post #6 by @pieper (2024-05-17 19:18 UTC)

<p>Yes, that would explain it.  There have been issues reported recently about OneDrive and Dropbox causing problems.</p>
<aside class="quote quote-modified" data-post="1" data-topic="36153">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/windows-unable-to-import-dicom-files-that-are-in-a-onedrive-backed-up-folder/36153">Windows: Unable to import DICOM files that are in a OneDrive-backed up folder</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    TL;DR: on Windows, do not use folders that are backed up by Microsoft OneDrive for DICOM images that you want to import into Slicer DICOMBrowser! 
<a class="mention" href="/u/vkt1414">@vkt1414</a> and I have been debugging an issue that we thought is a problem with our extension, but upon further investigation it turned out the issue was not in the extension. Logs showed that DCMTK failed to open the DICOM files our extension was downloading. Initially, I thought this is due to the presence of dots in the folder hierarchy, but <a class="mention" href="/u/pieper">@pieper</a> …
  </blockquote>
</aside>


---

## Post #7 by @tenzin_kunkyab (2024-05-17 19:37 UTC)

<p>thanks. I made a local copy of the data on the desktop and the loading takes 2-3 minutes. I am not sure if that was the case for you or if it was instantaneous.</p>
<p>Might have something to do with the computer too. I probably need to investigate this further. We are doing a large number of segmentation, so every minute matters…</p>
<p>I am just using a remote desktop for now, may be that also could be a problem.</p>

---

## Post #8 by @pieper (2024-05-17 19:42 UTC)

<p>I don’t use windows myself, but I’ve been told sometimes the “Desktop” folder is hijacked by OneDrive in unexpected ways.</p>
<p>Loading 300 CT slices really shouldn’t take more than a few seconds.</p>

---

## Post #9 by @tenzin_kunkyab (2024-05-17 20:34 UTC)

<p>Thanks I put it into the same file as the Appdata for the slicer and it loaded much faster.</p>
<p>Thank you,</p>

---
