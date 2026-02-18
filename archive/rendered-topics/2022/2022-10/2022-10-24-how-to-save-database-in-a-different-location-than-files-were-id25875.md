# How to save database in a different location than files were uploaded from?

**Topic ID**: 25875
**Date**: 2022-10-24
**URL**: https://discourse.slicer.org/t/how-to-save-database-in-a-different-location-than-files-were-uploaded-from/25875

---

## Post #1 by @millicentroach (2022-10-24 20:52 UTC)

<p>Hello!</p>
<p>I need to upload dicom images from a different location than I want to save the database.</p>
<p>Do any of you know how to do that? Your help would be greatly appreciated.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2022-10-24 20:54 UTC)

<p>You can import the DICOM images from any location and you can export DICOM files to anywhere in the file system.</p>
<p>Can you describe what you did, what you expected to happen, and what happened instead?</p>

---

## Post #3 by @millicentroach (2022-10-25 21:16 UTC)

<p>Hello Andras,</p>
<p>Thank you so much for responding.</p>
<p>I selected, ‘Import DICOM files’, selected the folder I wanted to import from. It began importing the folder (it ended up not responding though because the number of files was large).</p>
<p>I see that the location of the database in the lower left corner says it is in: Documents/SlicerDICOMDatabase</p>
<p>Instead I need the location of the slicer database to be in another folder.</p>
<p>I am going to re-start this process, but want to do it in the right way. Do you know how I would save the location of where I want the database to be stored before I begin the upload?</p>
<p>I appreciate your help.</p>
<p>Please see the attached.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02c45fdfc56749099a2531c6d0e48b57d93fa00.jpeg" data-download-href="/uploads/short-url/mQXfxkZw11DpvaxtjcvanID8aL6.jpeg?dl=1" title="Screen Shot 2022-10-25 at 3.42.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02c45fdfc56749099a2531c6d0e48b57d93fa00_2_690x171.jpeg" alt="Screen Shot 2022-10-25 at 3.42.15 PM" data-base62-sha1="mQXfxkZw11DpvaxtjcvanID8aL6" width="690" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02c45fdfc56749099a2531c6d0e48b57d93fa00_2_690x171.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02c45fdfc56749099a2531c6d0e48b57d93fa00_2_1035x256.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a02c45fdfc56749099a2531c6d0e48b57d93fa00_2_1380x342.jpeg 2x" data-dominant-color="E9EAEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-25 at 3.42.15 PM</span><span class="informations">2042×508 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you,<br>
Millicent</p>

---

## Post #4 by @muratmaga (2022-10-25 22:23 UTC)

<p>That button is clickable, click and navigate to the folder where you want the DICOM DB to be stored. From now on, that will be the location of DICOM DB files. This setting will be saved in the Slicer.ini file.</p>
<p>However, you will loose access to everything you import in the previous DB (though sounds like you didn’t import anything anyways)…</p>

---

## Post #5 by @lassoan (2022-10-25 23:33 UTC)

<p>From the screenshot it looks like you are not using the current Slicer version. We have improved speed and robustness of DICOM import in recent Slicer versions, so I would strongly recommend to upgrade.</p>

---

## Post #6 by @millicentroach (2022-10-27 18:20 UTC)

<p>Ok thank you! I will download that. What version is it you suggest I download?</p>

---

## Post #7 by @millicentroach (2022-10-27 18:21 UTC)

<p>Thank you so much. I will try that out.</p>

---
