# Cannot load dicom file segmentation

**Topic ID**: 32210
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/cannot-load-dicom-file-segmentation/32210

---

## Post #1 by @helene_c (2023-10-13 13:51 UTC)

<p>Hello,</p>
<p>I am trying to open Dicom images that I directly downloaded from the image viewer of the hospital. The software is called Sectra. The images should contain a segmentation made with Sectra.<br>
When I am loading the images with Slicer (or any other Dicom viewer I could find), the images are correctly opened, but not the segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05c616e9d4deb9ace92f4dc69b9dc9dac9c591c4.png" data-download-href="/uploads/short-url/P4N740sebrDSc9kNHhwMEFrEyM.png?dl=1" title="Screenshot from 2023-10-13 09-58-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05c616e9d4deb9ace92f4dc69b9dc9dac9c591c4_2_690x174.png" alt="Screenshot from 2023-10-13 09-58-42" data-base62-sha1="P4N740sebrDSc9kNHhwMEFrEyM" width="690" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05c616e9d4deb9ace92f4dc69b9dc9dac9c591c4_2_690x174.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05c616e9d4deb9ace92f4dc69b9dc9dac9c591c4_2_1035x261.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05c616e9d4deb9ace92f4dc69b9dc9dac9c591c4_2_1380x348.png 2x" data-dominant-color="E9F2F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-10-13 09-58-42</span><span class="informations">2025×513 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It looks like this is empty. However, if I load the Dicom file back in Sectra, the segmentation is correctly shown.<br>
I suspect it is a weird Dicom file from Sectra, not meant to be opened with anything else.<br>
On top of that, my image file contains 40 slices, and the segmentation only 15, which corresponds to the number of slices the segmentation is present.<br>
I also cannot open it with pydicom.</p>
<p>Have a nice day!</p>

---

## Post #2 by @pieper (2023-10-13 13:55 UTC)

<p>Yes, that’s probably some proprietary format wrapped in dicom just so it can be stored in the pacs.  With some examples and some effort someone might be able to reverse engineer it.</p>

---

## Post #3 by @lassoan (2023-10-13 14:25 UTC)

<p>DICOM standard compliant software can use “SEG” or “RTSTRUCT” modality for storing a segmentation. Probably Sectra decided to store segmentation in private fields of a “PR” (presentation state) object because:</p>
<ol>
<li>It was simpler for them to store the data in their own internal format instead of spending time with understanding and implementing DICOM compliant saving.</li>
<li>Vendor lock-in. If you switch to a different software vendor then you may lose access to these segmentations that only Sectra software can interpret. This is very good for the software vendor.</li>
</ol>
<p>Since it is so favorable for vendors to use private DICOM fields, it is the responsibility of users to speak up and ask vendors to use standard DICOM information objects instead. If the vendor does not listen then users should switch to a different vendor (it is better for everyone if they listen).</p>

---

## Post #4 by @helene_c (2023-10-13 14:35 UTC)

<p>So I should directly address Sectra?</p>
<p>Thanks for your time!</p>

---

## Post #5 by @pieper (2023-10-13 14:45 UTC)

<aside class="quote no-group" data-username="helene_c" data-post="4" data-topic="32210">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/helene_c/48/67854_2.png" class="avatar"> helene_c:</div>
<blockquote>
<p>So I should directly address Sectra?</p>
</blockquote>
</aside>
<p>Yes, ask them to provide you with data in standard DICOM.</p>

---

## Post #6 by @helene_c (2023-10-20 12:27 UTC)

<p>Hello,</p>
<p>In case someone ever has similar issues, Sectra gave me more details about those segmentations:</p>
<ul>
<li>It is not meant to be a real segmentation, that is why it is not saved as segmentation and thus, they cannot be loaded outside sectra</li>
<li>There is a possibility to create segmentation as volume, that can be saved as meshes with an obj format</li>
</ul>

---
