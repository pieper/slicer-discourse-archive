# How to update from Python 2.7 to 3.7?

**Topic ID**: 11443
**Date**: 2020-05-07
**URL**: https://discourse.slicer.org/t/how-to-update-from-python-2-7-to-3-7/11443

---

## Post #1 by @katjx (2020-05-07 13:07 UTC)

<p>Hi!<br>
I 'm very new with DICOM images processing and with Python<br>
I have <strong>3DSlicer version 4.10.2</strong> installed and the Python version I see in Python Interactor is:</p>
<blockquote>
<p>Python 2.7.13 (default, May 16 2019, 14:27:45) [MSC v.1900 64 bit (AMD64)] on win32</p>
</blockquote>
<p>Is there a way to upgrade to Python 3.7?</p>
<p>The original reason for wanting to do this is because when trying to load DICOM files I get the following error:</p>
<blockquote>
<p>DICOM Plugin failed: ‘module’ object has no attribute ‘TemporaryDirectory’</p>
</blockquote>
<p>and from what I 've read, an upgrade to python 3.7 may solve the problem</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2020-05-07 13:41 UTC)

<p>Slicer-4.11 uses Python 3. It also has a greatly improved DICOM browser. See examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> to see how you can manage DICOM files.</p>

---

## Post #3 by @katjx (2020-05-07 18:15 UTC)

<p>I have downloaded and installed Slicer-4.11, but still getting errors like the following and couldn’t load any DICOM file yet.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec0c822de63bd968efbc4fb51fbb3e39467cd7d.png" data-download-href="/uploads/short-url/i5jc32BlXHvsvEGfylgIhep9sGp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec0c822de63bd968efbc4fb51fbb3e39467cd7d.png" alt="image" data-base62-sha1="i5jc32BlXHvsvEGfylgIhep9sGp" width="690" height="87" data-dominant-color="FCF4F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×127 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks anyway!</p>

---

## Post #4 by @lassoan (2020-05-07 18:26 UTC)

<p>That means that your DICOM files are corrupted. What software created them?</p>

---

## Post #5 by @katjx (2020-05-07 19:48 UTC)

<p>I only have the information from the file’s metadata, so I can see the following:<br>
Source Application Entity Title: ECHOPAC<br>
Manufacturer: GE Vingmed Ultrasound<br>
Manufacturer’s Model Name: EchoPAC PC SW-Only</p>

---

## Post #6 by @lassoan (2020-05-07 21:58 UTC)

<p>You may try running the image through DICOM patcher module to see if that can fix the format error.</p>
<p>Could you provide a sample image file (must not contain patient information; preferably an original scan of any object, not a patient)?</p>

---

## Post #7 by @katjx (2020-05-08 07:15 UTC)

<p>I run the DICOM patcher on the data and then, when I tried to import, I got the following errors and couldn’t import the data:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de75f679b0492556f6a3779280134c411d96477f.png" data-download-href="/uploads/short-url/vJYJpXMmSUG1xlhUQ7RjGCYq0KH.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de75f679b0492556f6a3779280134c411d96477f.png" alt="Untitled" data-base62-sha1="vJYJpXMmSUG1xlhUQ7RjGCYq0KH" width="690" height="117" data-dominant-color="FCF2F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">871×148 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unfortunately I’m not allowed to publish the files, even anonymized, and I don’t have access to the machine to get a new scan of an object.</p>

---

## Post #8 by @pieper (2020-05-08 12:09 UTC)

<p>It looks like your files are pretty badly formatted or maybe corrupted by some processing step.  Since you can’t share them, a good path would be for you would be to study up on dicom.  There are tons of books and web pages.  Also try the <a href="https://dicom.innolitics.com">analyze tab on the innolitics site</a> to better understand what’s going on inside.</p>

---

## Post #9 by @katjx (2020-05-08 13:16 UTC)

<p>I will. Thank you for your answers!</p>

---
