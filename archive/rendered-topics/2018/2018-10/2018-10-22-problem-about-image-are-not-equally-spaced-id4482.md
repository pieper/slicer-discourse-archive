---
topic_id: 4482
title: "Problem About Image Are Not Equally Spaced"
date: 2018-10-22
url: https://discourse.slicer.org/t/4482
---

# Problem about image are not equally spaced

**Topic ID**: 4482
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/problem-about-image-are-not-equally-spaced/4482

---

## Post #1 by @TingtingYu (2018-10-22 02:23 UTC)

<p>Hi,</p>
<p>I was trying to import patient images, however, I got the warning after I clicked “examine”. Before I loaded the images, I enabled the “DICOMScalarVolumePlugin” as the warning suggested, but the image still appeared distorted not only in sagittal, coronal direction, but also seems to be disconnected in axial direction. Could you please help me solve this problem?</p>
<p>Many thanks,<br>
Tingting!</p>
<p><a href="/uploads/short-url/qtbrvkzJhQ9JZr3SeLU8Dxqz0cM.png">DICOMiMPORT|690x81</a></p>

---

## Post #2 by @lassoan (2018-10-22 03:41 UTC)

<p>Please follow suggestions described in <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected">DICOM faq</a> and let us know what you’ve found.</p>

---

## Post #3 by @TingtingYu (2018-10-23 08:22 UTC)

<p>Hi Andras,</p>
<p>Thank you. Based on the warnings that I receive when I was using the DICOM module and the DICOM faq you recommended, I modified the application setting, change the acquisition geometry regularization to “apply regularization transform”, I also tried different reader approach. However, I still got the distorted images. Below are the images and the error logs.</p>
<p>Regards,<br>
Tingting<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6345bc62a608b7d7089c48d41b8694d2d64b2c54.png" data-download-href="/uploads/short-url/eacG2guutED98pArOjofOq9bX5W.png?dl=1" title="DICOMiMPORT_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6345bc62a608b7d7089c48d41b8694d2d64b2c54_2_690x84.png" alt="DICOMiMPORT_2" data-base62-sha1="eacG2guutED98pArOjofOq9bX5W" width="690" height="84" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6345bc62a608b7d7089c48d41b8694d2d64b2c54_2_690x84.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6345bc62a608b7d7089c48d41b8694d2d64b2c54_2_1035x126.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/6345bc62a608b7d7089c48d41b8694d2d64b2c54_2_1380x168.png 2x" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOMiMPORT_2</span><span class="informations">1900×232 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51fdf6bc08b410951b4e0aa977aa7d2f5bdc0f92.jpeg" data-download-href="/uploads/short-url/bHkMYXGFtqgAKYKrxnG6K5PhrzA.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51fdf6bc08b410951b4e0aa977aa7d2f5bdc0f92_2_690x450.jpeg" alt="PNG" data-base62-sha1="bHkMYXGFtqgAKYKrxnG6K5PhrzA" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51fdf6bc08b410951b4e0aa977aa7d2f5bdc0f92_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51fdf6bc08b410951b4e0aa977aa7d2f5bdc0f92_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51fdf6bc08b410951b4e0aa977aa7d2f5bdc0f92_2_1380x900.jpeg 2x" data-dominant-color="4C4C58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1391×908 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db51a5c969c34d3d3eb58a23c9eb08cf58df2f6.png" data-download-href="/uploads/short-url/1XgdxIXRXWGMBLWWPCejQsNbgB8.png?dl=1" title="ErrorLog1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0db51a5c969c34d3d3eb58a23c9eb08cf58df2f6.png" alt="ErrorLog1" data-base62-sha1="1XgdxIXRXWGMBLWWPCejQsNbgB8" width="665" height="500" data-dominant-color="ECEEF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorLog1</span><span class="informations">1285×966 44.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9449263885c5574ee7aac7b61a0c0fcb855dc81.png" data-download-href="/uploads/short-url/qqXfhyNlUuXXgfb1dyN7HUpAwX7.png?dl=1" title="ErrorLog2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9449263885c5574ee7aac7b61a0c0fcb855dc81.png" alt="ErrorLog2" data-base62-sha1="qqXfhyNlUuXXgfb1dyN7HUpAwX7" width="665" height="500" data-dominant-color="E7EAF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ErrorLog2</span><span class="informations">1285×966 59.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-10-23 11:31 UTC)

<p>It looks quite good. It seems you are either missing some slices (or there are extra slices of the same region that interfere with the reconstruction). To diagnose the issue, please send us all the image slice positions occurring in your data set by follow these steps:</p>
<ul>
<li>Open DICOM browser</li>
<li>Click on the patient</li>
<li>Check <code>Advanced</code> checkbox</li>
<li>Click `Metadata button</li>
<li>Enter <code>Image</code> in the search box</li>
<li>Click <code>Copy all files metadata</code> button to copy image position information on the clipboard</li>
<li>Paste it to an empty Excel sheet</li>
<li>Upload the Excel sheet to OneDrive, Dropbox, or any other file sharing service, and paste the link in your response (taking a screenshot of the sheet and attaching it is not enough, as only a small fraction of the data would be visible)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71cba9670a1fc9af08c728e0bd6ca2fd08fe897.png" data-download-href="/uploads/short-url/zg3ua5ta5g8XPRyp72TXCvtaRFR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f71cba9670a1fc9af08c728e0bd6ca2fd08fe897.png" alt="image" data-base62-sha1="zg3ua5ta5g8XPRyp72TXCvtaRFR" width="690" height="332" data-dominant-color="F7F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">846×408 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @TingtingYu (2018-10-24 05:39 UTC)

<p>Hi Andras,</p>
<p>Thank you for your quick reply. Below is the link to the excel file containing image position information. There are two work sheets. One is about CT image, another is about StructSets.</p>
<p><a href="https://polyuit-my.sharepoint.com/:x:/g/personal/tt3yu_polyu_edu_hk/EZb_VmuwjLJGvn4O7GuhNZwBTzYz_IihN-AsWn4DrEiQUQ?e=lPbMsj" class="onebox" target="_blank" rel="nofollow noopener">https://polyuit-my.sharepoint.com/:x:/g/personal/tt3yu_polyu_edu_hk/EZb_VmuwjLJGvn4O7GuhNZwBTzYz_IihN-AsWn4DrEiQUQ?e=lPbMsj</a></p>
<p>Regards,<br>
Tingting</p>

---

## Post #6 by @lassoan (2018-10-24 12:34 UTC)

<p>Thank you the table was very useful. It showed that the problem is that you don’t have any slices between coordinates I 66.25 and I 101.25. Slice spacing is 5mm and slices are missing from the end of the list (after 060.DCM), which means that most likely you haven’t received (or did not import into Slicer) files 061.DCM to 067.DCM.</p>

---

## Post #7 by @TingtingYu (2018-10-25 05:46 UTC)

<p>Hi Andras,</p>
<p>Thank you. Thank you for helping me figure out the problem. We did miss some files.</p>
<p>Regards,<br>
Tingting</p>

---
