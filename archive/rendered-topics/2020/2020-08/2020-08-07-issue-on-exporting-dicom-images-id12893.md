---
topic_id: 12893
title: "Issue On Exporting Dicom Images"
date: 2020-08-07
url: https://discourse.slicer.org/t/12893
---

# Issue on exporting DICOM images

**Topic ID**: 12893
**Date**: 2020-08-07
**URL**: https://discourse.slicer.org/t/issue-on-exporting-dicom-images/12893

---

## Post #1 by @schumi00 (2020-08-07 15:45 UTC)

<p>Hi,</p>
<p>I am trying to load images in nifti format in to Slicer and then export them into DICOM format.  I could export images with DICOM module.  However, after reloading the exported images back to Slicer, it seems that some bright regions in the original images are now displayed as dark (see below).  How could this be fixed?  Thanks!</p>
<p>These are original nifiti images and the display info shown in the volume module:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8ed4bf129b89d9362bf4960604adbc0f7788f14.png" alt="image Nifti" data-base62-sha1="sFtTMT2pBYfCqrdYfeqFTln0KX2" width="589" height="390"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af23337a43e1c1120dff183aa3a1d03201ffb4c3.png" alt="hist Nifti" data-base62-sha1="oZkYt4fToDTxpdhys0l7g9vLMpt" width="457" height="385"></p>
<p>These are the exported dicom images (reloaded back to Slicer) and the display info shown in the volume module:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5220cf26d80780dcd0459ce0fa1f04433b39fa5f.png" alt="image dicom" data-base62-sha1="bIxrEaHQ4LrcHTU3GO9fKg7RJEP" width="449" height="359"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9f0766e66b5f0eed5faa0d01cbebb18df9eac11.png" alt="hist dicom" data-base62-sha1="sOr9WonUBxVWG6CwVnLJJ94QypX" width="514" height="389"></p>

---

## Post #2 by @schumi00 (2020-08-12 15:21 UTC)

<p>It could be that during the conversion (load NIFTI images and export with DICOM module), the UNSIGNED 16-bit pixels in NIFTI were interpreted as SIGNED 16-bit pixels in DICOM output.</p>
<p>Is there a way in 3D Slicer this property can be specified during exporting with DICOM module?</p>

---

## Post #3 by @lassoan (2020-08-12 16:12 UTC)

<p>Probably the image export fails because the range is larger than 32767. Probably up to 65535 could be supported, but since scalar value range in medical images is usually a couple of thousand and not tens of thousands, this has not come up before. How this nifti image was generated? Probably you can just rescale its intensity range to a more sensible value, but if you have time then it would be nice if you could track down where the 32767 limit comes from.</p>

---

## Post #4 by @schumi00 (2020-08-13 15:01 UTC)

<p>Thanks, Andras, for the comments.</p>
<p>The images were from the Dixon sequence of a MRI scan for research purposes.  As you hinted, I scaled the intensity range from the original Single 32-bit (but the actual intensity is in the range of about 0~65535) to Un-signed Integer 8-bit in Matlab, which seems to solve the problem (see below). However, the exported DICOM images are still in Signed 16-bit, which may have caused the issue I posted.</p>
<p>Is there a way to rescale the intensity range in Slicer?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea341e0aa1277706288a17727da532e90231deb5.png" alt="image dicom uint8" data-base62-sha1="xpRo7hDRtEXIj8wKJbQMeEAkgyp" width="458" height="365"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c2e8266a563212542d90115fae89db9e99f6f0b.png" alt="hist dicom uint8" data-base62-sha1="hIyQPVUzmUKTPDarGTZhtnOlX3d" width="642" height="413"></p>

---

## Post #5 by @lassoan (2020-08-13 15:49 UTC)

<p>You can use Simple Filters module’s <em>RescaleIntensityImageFilter</em> or <em>IntensityWindowingImageFilter</em> to rescale intensity range of an image.</p>

---
