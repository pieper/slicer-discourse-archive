# Volumes display Image Spacing and Image Origin wrong?

**Topic ID**: 43587
**Date**: 2025-07-03
**URL**: https://discourse.slicer.org/t/volumes-display-image-spacing-and-image-origin-wrong/43587

---

## Post #1 by @StephenLeePeng (2025-07-03 09:46 UTC)

<p>When I load a CT Lung series (axial) into Slicer 4.13, and switch to the “Volumes” Module, and the “Image Spacing” and “Image Origin” display: [1mm, 1mm, 1mm] and [0, 0, 0] as picture below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6ceb979a18393accef68b7d879a2ca7d349164c.png" data-download-href="/uploads/short-url/uEh5cvUxcBJZaU4sEmPjnso8hVW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6ceb979a18393accef68b7d879a2ca7d349164c_2_690x322.png" alt="image" data-base62-sha1="uEh5cvUxcBJZaU4sEmPjnso8hVW" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6ceb979a18393accef68b7d879a2ca7d349164c_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6ceb979a18393accef68b7d879a2ca7d349164c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6ceb979a18393accef68b7d879a2ca7d349164c.png 2x" data-dominant-color="363333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×326 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I dcmdump the random dcm file, the relative DICOM tag values are:</p>
<p>(0020,0032) DS [-173.100 \ -180.000 \ -272.500]              #  26, 3 ImagePositionPatient,</p>
<p>(0020,0037) DS [1.000000\0.000000\0.000000\0.000000\1.000000\0.000000] #  54, 6 ImageOrientationPatient</p>
<p>(0028,0030) DS [0.703125\0.703125]                      #  18, 2 PixelSpacing.</p>
<p>(0018,0050) DS [1.250000]                               #   8, 1 SliceThickness</p>
<p>And the dicom MPR image is as follow:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7dcd0fcae82f8a74c01452f63b6535e13a98f0.jpeg" data-download-href="/uploads/short-url/p2t5fSpA4EwzKmKm3YIlJltOa9W.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7dcd0fcae82f8a74c01452f63b6535e13a98f0_2_690x495.jpeg" alt="image" data-base62-sha1="p2t5fSpA4EwzKmKm3YIlJltOa9W" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7dcd0fcae82f8a74c01452f63b6535e13a98f0_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7dcd0fcae82f8a74c01452f63b6535e13a98f0_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7dcd0fcae82f8a74c01452f63b6535e13a98f0.jpeg 2x" data-dominant-color="888895"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1197×859 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So, why Image Spacing of Volumes Module is: [1, 1, 1], not: [0.703125, 0.703125, 1.25].<br>
And the x, y of ImageOrigin is [0, 0], not: [-173.100, -180.00].</p>

---

## Post #2 by @pieper (2025-07-03 12:03 UTC)

<p>There’s probably more going on - check the logs to see if there are any error messages or other warnings.  We try very hard to make sure DICOM files are properly interpreted in 3D, but weird things can happen, possibly due to inconsistencies in the data.  If you can share a public example that replicates the issue for sure we’ll look into it.</p>

---

## Post #3 by @StephenLeePeng (2025-07-04 08:06 UTC)

<p>Thank you for your reply.</p>
<p>I have uploaded the sampleData to Google Driver, pop the sensitive dicom tags.  Please download the data by link to look into why ImageOrigin and ImageSpacing is not displayed as expected.</p>
<p>link is: <a href="https://drive.google.com/file/d/1RnD_xzYptdIY5nfiPeQsDSlC4airhcx2/view?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1RnD_xzYptdIY5nfiPeQsDSlC4airhcx2/view?usp=drive_link</a></p>
<p>Thank you very much.</p>

---

## Post #4 by @issakomi (2025-07-06 09:42 UTC)

<p>The link to Google Drive is not public.<br>
What is the value of the <em>SOP Class UID</em> <code>(0x0008,0x0016)</code>?<br>
Most likely the series is stored in <em>Secondary Capture IOD</em>.</p>
<p>Adding spatial information to the <em>Secondary Capture IOD</em> is a fairly common practice, even if it was <strong>not</strong> part of the IOD until 2024, s. <a href="https://dicom.nema.org/medical/dicom/Final/cp2330_ft_AddImagePlaneModuleToSC.pdf" rel="noopener nofollow ugc">CP-2330</a>. Probably the recent version of Slicer will work with this series (you are using the old version 4.13).</p>

---

## Post #5 by @StephenLeePeng (2025-07-07 01:19 UTC)

<p>I’m so sorry the google drive link is private, I’m new to Google driver.</p>
<p>This is the new data link: <a href="https://drive.google.com/file/d/1RnD_xzYptdIY5nfiPeQsDSlC4airhcx2/view" rel="noopener nofollow ugc">https://drive.google.com/file/d/1RnD_xzYptdIY5nfiPeQsDSlC4airhcx2/view</a><br>
anyone can download and view the data.</p>
<p>I have try this data with the Slicer 5.6.2-linux-amd64, and this problem always exist.</p>
<p>And I test this data with the most new stable Release: 5.8.1, and this problem have been solved. And I want to know why?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2495315cdfb7c3a2d0a6e6e06cbbae8594537b0a.png" data-download-href="/uploads/short-url/5dCPEnKaIFz2aZaT09l1LstXWyK.png?dl=1" title="5.8.1-pro" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2495315cdfb7c3a2d0a6e6e06cbbae8594537b0a.png" alt="5.8.1-pro" data-base62-sha1="5dCPEnKaIFz2aZaT09l1LstXWyK" width="577" height="404"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5.8.1-pro</span><span class="informations">577×404 37.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/issakomi">@issakomi</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #6 by @issakomi (2025-07-07 01:27 UTC)

<blockquote>
<p>anyone can download and view the data.</p>
</blockquote>
<p>I have looked, yes, it is Secondary Capture IOD.</p>
<blockquote>
<p>And I want to know why?</p>
</blockquote>
<p>S. the post above.</p>

---
