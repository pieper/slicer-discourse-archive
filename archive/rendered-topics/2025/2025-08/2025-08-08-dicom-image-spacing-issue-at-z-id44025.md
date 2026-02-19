---
topic_id: 44025
title: "Dicom Image Spacing Issue At Z"
date: 2025-08-08
url: https://discourse.slicer.org/t/44025
---

# DICOM Image Spacing Issue at Z

**Topic ID**: 44025
**Date**: 2025-08-08
**URL**: https://discourse.slicer.org/t/dicom-image-spacing-issue-at-z/44025

---

## Post #1 by @txuh (2025-08-08 15:11 UTC)

<p>I am writing a single DICOM with multiple frames.</p>
<p>After loading the dcm file via 3D Slicer (volume), the x/y image spacing is correct which I set the value (0.0195) at tag “0028,0030” (Pixel Spacing).</p>
<p>However, the image spacing at Z is always 1mm at 3D Slicer. I had tested tag “0018,0088” (Spacing Between Slices) and “0018,0050” (Slice Thickness) respectively or set both to value (0.05). This does not work. Can anyone advise?</p>

---

## Post #2 by @fedorov (2025-08-08 15:20 UTC)

<p>I don’t know what is happening, but two things to keep in mind:</p>
<ol>
<li>Slicer should be calculating distance between slices based on <code>ImagePositionPatient</code> for the individual frames. Changing <code>SliceThickness</code> is not expected to have any effect in your test. <code>SpacingBetweenSlices</code> is probably also not taken into account - it is important only in those situations where volume is not sampled regularly (such as with sparse segmentations). If you could could identify two samples that have very different, and not 1, distance between adjacent slices based on <code>ImagePositionPatients</code>, and both would load with z spacing of 1, that would confirm the bug. Ideally, using publicly available data.</li>
<li>Multiframe DICOM remains uncommon, and it might well be that its support has bugs.</li>
</ol>

---

## Post #3 by @pieper (2025-08-08 16:30 UTC)

<p>Building on what <a class="mention" href="/u/fedorov">@fedorov</a> said, you will want to specify the ImagePositionPatient for the frames in the PerFrameFunctionalGroupsSequence.  In case it helps, <a href="https://github.com/dcmjs-org/dcmjs/blob/2ca6bb1e86daf528a10c28585a02fe37bbbf1025/src/normalizers.js#L135">here’s some code</a> for creating multiframes from single frame dicom.</p>

---

## Post #4 by @txuh (2025-08-08 18:35 UTC)

<p>Thanks both replies. I add this to PerFrameFunctionalGroupsSequence. This time I use 0.04167 as spacing and it seems the DICOM tags are right after loading by 3D Slicer (DICOM). But the Z-spacing is still 1mm (volume).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e146913604d5dd6b1db4097232d744986b4a9c.png" data-download-href="/uploads/short-url/87bo86KtTHkiHpXgWVwGBIA8eDO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38e146913604d5dd6b1db4097232d744986b4a9c.png" alt="image" data-base62-sha1="87bo86KtTHkiHpXgWVwGBIA8eDO" width="674" height="281"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">674×281 7.34 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc5f32ee59721a85b8256e228110de13497b2cae.png" alt="image" data-base62-sha1="A0AhGVFnZvOPm6EaBUaaQ4rFe6q" width="467" height="49"></p>

---

## Post #5 by @pieper (2025-08-08 18:57 UTC)

<p>You could try dropping it on <a href="https://viewer.ohif.org/local" class="inline-onebox">OHIF Viewer</a> to see what it does.  You should also compare your file’s structure to a file that is known to work.</p>
<p>Are you writing code that you are planning to share publicly?  If you are doing something public it would be easier for us to help you debug.</p>

---

## Post #6 by @lassoan (2025-08-09 21:30 UTC)

<p>Maybe 3D position information is ignored because the imaging modality does not indicate that it is a 3D volume. Is this a secondary capture (screenshot)?</p>
<p>You can try installing <code>SlicerDcm2nii</code> extension and use the “Advanced” mode in the DICOM module to load the series using <code>dcm2niix</code> reader.</p>

---

## Post #7 by @txuh (2025-08-11 14:02 UTC)

<p>Thanks for all your kind replies. I finally decide not include PerFrameFunctionalGroupsSequence in the DICOM, and manually adjust Z spacing in 3D slicer. That’s because my DICOM might be huge and include a large number of frames (e.g. &gt; 10,000 frames) and this tab could be very long. Thanks for all your kind helps.</p>

---
