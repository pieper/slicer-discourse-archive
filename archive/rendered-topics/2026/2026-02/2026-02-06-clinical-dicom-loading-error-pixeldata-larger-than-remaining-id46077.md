---
topic_id: 46077
title: "Clinical Dicom Loading Error Pixeldata Larger Than Remaining"
date: 2026-02-06
url: https://discourse.slicer.org/t/46077
---

# Clinical DICOM loading error, PixelData larger than remaining bytes in file, but images look OK

**Topic ID**: 46077
**Date**: 2026-02-06
**URL**: https://discourse.slicer.org/t/clinical-dicom-loading-error-pixeldata-larger-than-remaining-bytes-in-file-but-images-look-ok/46077

---

## Post #1 by @mikebind (2026-02-06 17:55 UTC)

<p>When I download an image series directly from our clinical PACS and import it into Slicer, I get the following error message repeated for each .dcm file:</p>
<p>“E: DcmElement: PixelData (7fe0,0010) larger (4294967295) than remaining bytes (0) in file, premature end of stream”</p>
<p>If I load the series into the scene from the database, it appears to load fine, and the image data seems correct, so I don’t think the problem is actually missing data. However, the error does break interactions in the DICOM database, like reviewing metadata in the “DICOM File Metadata” window.  The search/filter on DICOM tags doesn’t do anything because of the encountered error, and reports:</p>
<p>“E: DcmElement: PixelData (7fe0,0010) larger (4294967295) than remaining bytes (0) in file, premature end of stream</p>
<p>E: can’t change to unencapsulated representation for pixel data</p>
<p>E: can’t determine ‘PhotometricInterpretation’ of decompressed image</p>
<p>E: mandatory attribute ‘PhotometricInterpretation’ is missing or can’t be determined</p>
<p>W: Rendering of DICOM image failed for thumbnail failed: Missing attribute”</p>
<p>I tried to investigate the possible issues with pydicom, and encountered this warning:</p>
<p>“UserWarning: The (0028,0101) ‘Bits Stored’ value (12-bit) doesn’t match the JPEG 2000 data (16-bit). It’s recommended that you change the ‘Bits Stored’ value”</p>
<p>My guess is that this is the root of the problem: only 12 bits of data represent stored clinical data, but the lossless compression is in 16-bit chunks.  I think the intended procedure would be to uncompress to 16-bit chunks and then ignore 4 of the bits per pixel when reconstructing the image arrays, but something in the Slicer machinery doesn’t like that mismatch between 12 and 16.  Somehow, the actual reconstruction of the image arrays seems to be working fine, so some piece of the import code is interpreting everything correctly. I’m not enough of a DICOM expert to tell whether the PACS is storing invalid DICOM, or whether Slicer’s DICOM import machinery is incorrectly complaining. Because it is clinical data, I can’t share the files themselves, but I am happy to run any investigative tests that might be helpful in sorting this out. I also can’t modify the images stored in our PACS, but If our scanners are actually spitting out invalid DICOM images, we can alert the scanner manufacturer if that’s where the problem lies.</p>

---

## Post #2 by @mikebind (2026-02-06 18:01 UTC)

<p>I forgot to mention, the problem that the DICOM File Metadata window search/filter stops working is new in 5.10; in 5.8.1 the window functions keep working (though I get the same error messages as on 5.10).<br>
I’m on Windows 11, newly transitioning to 5.10.</p>
<p>Other possibly helpful factoids:</p>
<ul>
<li>
<p>4294967295 = (2^32)-1, the largest 32-bit unsigned integer, which is kind of suspicious</p>
</li>
<li>
<p>Despite some of the error messages suggesting a missing PhotometricInterpretation field, it is present in the metadata and has value “MONOCHROME2”</p>
</li>
<li>
<p>I am not using the “Experimental visual DICOM browser”, that box is unchecked</p>
</li>
<li>
<p>The “Examine” and “Load” steps from the DICOM browser don’t report any errors, it is only in import and when using the DICOM metadata browser that errors are reported.</p>
</li>
</ul>

---

## Post #3 by @lassoan (2026-02-08 04:14 UTC)

<p>The main issue is that the image is compressed with <code>JPEG 2000</code> algorithm. DCMTK has a paid module for this, but <a href="https://github.com/commontk/CTK/issues/1332">we have an alternative solution</a>. This is the reason why you don’t see the image in the metadata browser and you see those error messages.</p>
<p>The image is loaded with ITK’s DICOM reader, which uses GDCM, which supports JPEG 2000, that’s why you can load the image.</p>
<p>The metadata filter/search is broken in Slicer 5.10 due to a regression that was introduced when preparing CTK for Qt6. It was <a href="https://github.com/commontk/CTK/commit/64f2e07ae3ff07390ce5f95f9cfc8459be1c84e2">fixed in December</a> - after releasing Slicer-5.10. Therefor the fix is only available in Slicer Preview Releases.</p>

---

## Post #4 by @mikebind (2026-02-08 22:44 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> , that clears up the main issues very well.  Much appreciated!</p>

---
