---
topic_id: 44633
title: "Batch Dental Segmentator No Valid Volume File Found In The F"
date: 2025-09-30
url: https://discourse.slicer.org/t/44633
---

# Batch dental segmentator: No valid volume file found in the folder

**Topic ID**: 44633
**Date**: 2025-09-30
**URL**: https://discourse.slicer.org/t/batch-dental-segmentator-no-valid-volume-file-found-in-the-folder/44633

---

## Post #1 by @Chanrury_s (2025-09-30 12:01 UTC)

<p>Hello!<br>
I’m having problems with the “AutomatedDentalTools” extension.<br>
AutomatedDentalTools contains the “BatchDentalSegmentator” module.<br>
When I select a date folder, an error appears (No valid volume file found in the folder) when I click apply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a62dfd869c38f16a91afe7ac5066cf415f40a22.png" data-download-href="/uploads/short-url/cTAOcHHX3j1ZfUKnrHedmGua8jo.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a62dfd869c38f16a91afe7ac5066cf415f40a22.png" alt="image" data-base62-sha1="cTAOcHHX3j1ZfUKnrHedmGua8jo" width="407" height="500" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">603×739 31.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What could be causing this problem?<br>
Please tell me which file extensions this module can work with?<br>
Maybe I should change the file extension to something else?<br>
It seems very strange to me that the module, for some reason, can’t read regular .dcm files.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0d30f1bcc15c3aa4071ba7e03f63c2e3f168b31.png" data-download-href="/uploads/short-url/w4T90iZa9ErRazcN9W4LCULP4nT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0d30f1bcc15c3aa4071ba7e03f63c2e3f168b31.png" alt="image" data-base62-sha1="w4T90iZa9ErRazcN9W4LCULP4nT" width="230" height="229"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">230×229 1.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think I should clarify. There’s a neural network called NNUnet. This neural network powers the DentalSegmentator. In Slicer3D, DentalSegmentator is available in two extensions: “DentalSegmentator” itself and DentalSegmentator as part of “AutomatedDentalTools”.</p>
<p>When working with another extension “DentalSegmentator” such problems do not arise. In this extension, data is loaded via “add DICOM data.” I can process the same DICOM files without any problems in this extension. This gives me reason to believe my DICOM files are fine. I have worked with them for a long time without any problems.</p>
<p>I wanted to test whether the same “dentalsegmentator,” but as part of “BatchDentalSeg” from the “AutomatedDentalTools” extension, could perform individual segmentation of each tooth. Here, you need to specify a folder to load the data, but the program apparently doesn’t see DICOM files in the folder.</p>

---

## Post #2 by @mau_igna_06 (2025-10-01 18:42 UTC)

<p>Maybe try putting your DICOM files in a folder path that does not contain special characters such as those “russian” letters between <code>OneDrive</code> and <code>endodontics</code></p>

---

## Post #3 by @Chanrury_s (2025-10-01 20:28 UTC)

<pre><code class="lang-auto">
</code></pre>
<p>I already thought about this and tried changing the file locations. Now there are no Cyrillic characters, but the error still appears.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d19fded8023139572bc818d05163fa7951c0fe.png" data-download-href="/uploads/short-url/17asyVNKWBjxVUczQYtENqfJwwS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07d19fded8023139572bc818d05163fa7951c0fe.png" alt="image" data-base62-sha1="17asyVNKWBjxVUczQYtENqfJwwS" width="406" height="500" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">602×740 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mau_igna_06 (2025-10-01 20:32 UTC)

<p>Maybe you need to convert all your dicom studies to usual (<code>volume</code>) 3D image formats such as <code>.nrrd</code>, <code>.nii</code> or <code>.nii.gz</code> and not <code>.dcm</code> files</p>

---

## Post #5 by @Chanrury_s (2025-10-01 20:47 UTC)

<p>Yes, it finally worked! Thank you very much! I ran the neural network calculation and I still have to wait for it to give me the results. I hope everything works out.</p>
<p>Thanks for telling me to try nii.gz - at least I was able to run the neural network. It looks like it really doesn’t accept the .dcm format.</p>

---
