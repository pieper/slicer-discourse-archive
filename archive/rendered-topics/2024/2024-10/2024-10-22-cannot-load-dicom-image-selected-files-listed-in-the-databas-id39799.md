# Cannot load DICOM image: "...selected files listed in the database cannot be found on disk"

**Topic ID**: 39799
**Date**: 2024-10-22
**URL**: https://discourse.slicer.org/t/cannot-load-dicom-image-selected-files-listed-in-the-database-cannot-be-found-on-disk/39799

---

## Post #1 by @Kajper (2024-10-22 16:19 UTC)

<p>Hello,</p>
<p>I have been working mostly on TIFFs. However, I received new scan in DCM files. For some reason my Slicer can’t see the files.<br>
Do you have an idea how to fix this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9392920dda944c6bbe3989b3370b1564714745f1.png" alt="image" data-base62-sha1="l3udgPlf7tZy8yXVuhob3osHUTn" width="184" height="58"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c5c43ac17d45d7952892aa00b0bb58994555811.png" data-download-href="/uploads/short-url/42T2Lw31WAmEkdMc353EY8dyGjf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c5c43ac17d45d7952892aa00b0bb58994555811_2_690x174.png" alt="image" data-base62-sha1="42T2Lw31WAmEkdMc353EY8dyGjf" width="690" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c5c43ac17d45d7952892aa00b0bb58994555811_2_690x174.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c5c43ac17d45d7952892aa00b0bb58994555811_2_1035x261.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c5c43ac17d45d7952892aa00b0bb58994555811_2_1380x348.png 2x" data-dominant-color="282827"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×483 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-10-22 20:26 UTC)

<p>Did you check the python console log as requested int he error messages?</p>
<p>Is this by any chance on a cloud mapped folder (dropbox, onedrive etc…)</p>

---

## Post #3 by @lassoan (2024-10-23 05:51 UTC)

<p>Please follow the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">DICOM troubleshooting instructions</a> in the documentation.</p>
<p>Specifically: Try moving the data and the database directory to a path that includes only US English characters (ASCII) to avoid possible parsing errors. No special, international characters are allowed.</p>

---

## Post #4 by @Kajper (2024-10-26 10:49 UTC)

<p>Thanks for the feedback!<br>
This is how my python console looks like<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc03cdea8fda70c8e7f541a1ea67ee8930377dd.png" data-download-href="/uploads/short-url/aWY9CU6FhbKdYl4eXXGVasZNG5T.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cc03cdea8fda70c8e7f541a1ea67ee8930377dd.png" alt="image" data-base62-sha1="aWY9CU6FhbKdYl4eXXGVasZNG5T" width="689" height="112" data-dominant-color="332323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1290×210 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-10-26 13:48 UTC)

<p>The files were incorrectly created (or too agressive anonymization made them unusable). Please go back to where you got the images from and ask for files that contain all required DICOM fields. In this case, the issue seems to be that required patient name, patient ID, or study instance UID field was missing.</p>

---

## Post #6 by @Kajper (2024-10-26 15:37 UTC)

<p>Thank you for the diagnosis!</p>

---
