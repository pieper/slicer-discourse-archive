# Direct DICOM image download from ultrasound system

**Topic ID**: 9098
**Date**: 2019-11-10
**URL**: https://discourse.slicer.org/t/direct-dicom-image-download-from-ultrasound-system/9098

---

## Post #1 by @jimmyt8408 (2019-11-10 12:48 UTC)

<p>I just logged on and need information before downloading 3DSlicer. I have 4 very old Siemens Acuson Sequoia systems in our research lab that have issues with DVD’s and our hospital does not want us to use their PACS system for storage of animal/human research studies. My question is, can I directly send studies from the US system via the ethernet connection into 3DSlicer? At this moment, I cannot take studies off the hard drive until I can find a compatible DVD drive (operating systems of Windows XT and earlier) so I must find a way to download them onto some sort of PACS system to complete analysis. Thanks for any help!</p>
<p>Jim</p>

---

## Post #2 by @lassoan (2019-11-10 13:07 UTC)

<p>Yes, you can send images directly to Slicer using DICOM push (C-store SCP) or Slicer can download the images using Query/Retrieve.</p>
<p>DICOM push is simpler: you start a listening server and you select and send images using the ultrasound system. Slicer’s default port is 11112 and any AETITLE can be used. I would recommend to use Slicer Preview Release (it has a more user-friendly interface and faster import):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86860b4f571f1263eefaf8711e8bc101a6c63547.png" data-download-href="/uploads/short-url/jc3av3CcvMY681EK1Gq3gqlIund.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86860b4f571f1263eefaf8711e8bc101a6c63547_2_355x500.png" alt="image" data-base62-sha1="jc3av3CcvMY681EK1Gq3gqlIund" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86860b4f571f1263eefaf8711e8bc101a6c63547_2_355x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86860b4f571f1263eefaf8711e8bc101a6c63547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86860b4f571f1263eefaf8711e8bc101a6c63547.png 2x" data-dominant-color="F6F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">486×683 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you need to download lots of data in bulk (without starting Slicer or immediately importing data into Slicer’s DICOM database) then you can run the SCP server from the command line, something like this:</p>
<blockquote>
<p>C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.11.0-2019-11-03\storescp.exe 11112 --accept-all --output-directory C:/tmp/incoming</p>
</blockquote>

---

## Post #3 by @jimmyt8408 (2019-11-16 14:33 UTC)

<p>Thank you for this valuable information.</p>
<p>Jim</p>

---
