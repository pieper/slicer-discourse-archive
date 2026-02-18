# Changing names in database

**Topic ID**: 13061
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/changing-names-in-database/13061

---

## Post #1 by @avrilev (2020-08-18 00:09 UTC)

<p>Hi guys,<br>
In the DICOM db, I get some ??? instead of the patient name. Is there a way to amend this?<br>
TIA<br>
Dr. Avri Lev</p>

---

## Post #2 by @lassoan (2020-08-18 00:11 UTC)

<p>Support for international characters was limited in Slicer-4.10. Slicer-4.11 (Slicer Preview Release) has full unicode support, so special characters should show up correctly.</p>

---

## Post #3 by @avrilev (2020-08-18 03:45 UTC)

<p>Well, the only issue, that it doesn’t…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91fa230c62ebb6700d3635a28c76d69c1bd15b9f.png" data-download-href="/uploads/short-url/kPn9f1a4twZ58BtHV9eQI7EisJV.png?dl=1" title="Screenshot 2020-08-18 064450.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91fa230c62ebb6700d3635a28c76d69c1bd15b9f_2_585x500.png" alt="Screenshot 2020-08-18 064450.png" data-base62-sha1="kPn9f1a4twZ58BtHV9eQI7EisJV" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91fa230c62ebb6700d3635a28c76d69c1bd15b9f_2_585x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91fa230c62ebb6700d3635a28c76d69c1bd15b9f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91fa230c62ebb6700d3635a28c76d69c1bd15b9f.png 2x" data-dominant-color="40413F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-08-18 064450.png</span><span class="informations">699×597 38.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-08-18 04:37 UTC)

<p>Could you send the content of “Operating system” line in application log (menu: Help / Report a bug)?</p>
<p>It should be something like this:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 18.08.2020 00:32:49 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 18363, Code Page 65001) - 64-bit
</code></pre>
<p>How the data set was created?</p>
<p>Can you share a sample data set of a phantom (not a patient), with similar characters in the patient name?</p>

---

## Post #5 by @avrilev (2020-08-18 07:49 UTC)

<p>I guess this is what you want:</p>
<p>[DEBUG][Qt] 18.08.2020 10:47:37 [] (unknown:0) - Operating system …: Windows / Professional / (Build 19041, Code Page 65001) - 64-bit</p>

---

## Post #6 by @lassoan (2020-08-18 13:08 UTC)

<p>Thank you, this looks good.</p>
<p>How the data set was created?</p>
<p>Can you share a sample data set of a phantom (not a patient’s), with similar characters in the patient name?</p>

---

## Post #7 by @avrilev (2020-08-19 04:41 UTC)

<p>Hi, I wouldn’t know how to do what you’ve asked from me…</p>
<p>Sorry.</p>
<p>Best,</p>
<p>Dr. Avri Lev</p>

---

## Post #8 by @lassoan (2020-08-19 04:44 UTC)

<p>How the data set was created? Acquired on a clinical scanner? Was it anonymized?</p>
<p>Can you acquire a data set of a phantom (e.g., calibration object, but if the scanner can acquire an empty image then that’s fine, too, you don’t need to put anything in the bore), enter patient name that has similar characters that you have problem with displaying, and share that data set, so that we can investigate if the created image is valid and if it is, why Slicer does not display the characters properly?</p>

---

## Post #9 by @avrilev (2020-08-19 07:08 UTC)

<p>The data are taken from a CT scan. I have the dicoms in a library on my PC.</p>
<p>Where can I get a phantom data?</p>
<p>Best,</p>
<p>Dr. Avri Lev</p>

---

## Post #10 by @lassoan (2020-08-19 12:51 UTC)

<p>A “phantom” is just any object that you out into the scanner. Do you still have access to the scanner so that you can acquire image of any object (or just the empty bore) with the same protocol and similar patient names that are used in your existing images? We could use these test images to investigate why some characters in the name do not appear correctly. Normally we could use anonymized patient images for such investigation but anonymization would remove the patient name, so it is not a good solution in this case.</p>
<p>Note that you don’t have to see the patient name if you import them one by one and save as nrrd image with the appropriate name. You can write a script that automates this, if doing manually would be too tedious.</p>

---

## Post #11 by @avrilev (2020-08-22 14:02 UTC)

<p>Hi Andras Lasso,</p>
<p>I did some digging on the subject.</p>
<p>It seams that the metadata associated with each DICOM file is to blame For the phenomena.</p>
<p>The issue resides in the field “Patient Name” and only there, since this is the field where you put the patient name by the receptionist who’s responsible for checking in the patient. The app cannot read other fonts besides Latin ones, hence it’s not adhering to the UTF-8 protocol.</p>
<p>i.e. the examination date is written in a number format, so Windows can read it and format it accordingly in my language. (see photos attached).</p>
<p>Now, the only thing to do here, is to let us, users, the possibility to be able to edit that field (Patient Name), directly in 3D Slicer, because it is impossible to make these changes for every single DICOM file (hundreds of them…) .</p>
<p>I know that 3D Slicer is open source and I think also that the app can be manipulate through coding - hence developers can change the behavior of the app.</p>
<p>Best,</p>
<p>Dr. Avri Lev</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d803119364a1263c1948696002c46568422f66.png" data-download-href="/uploads/short-url/5oMt8vf652No31cAeuYhGzdbe8C.png?dl=1" title="DICOM metadata.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25d803119364a1263c1948696002c46568422f66.png" alt="DICOM metadata.png" data-base62-sha1="5oMt8vf652No31cAeuYhGzdbe8C" width="564" height="500" data-dominant-color="4A4948"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DICOM metadata.png</span><span class="informations">584×517 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59723e81ae832388cb8d59cb91ceeea1dba17772.png" data-download-href="/uploads/short-url/cLhgeCknGXlOXcNH9HO0AFBszPY.png?dl=1" title="DB 3D Slicer.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59723e81ae832388cb8d59cb91ceeea1dba17772.png" alt="DB 3D Slicer.png" data-base62-sha1="cLhgeCknGXlOXcNH9HO0AFBszPY" width="690" height="248" data-dominant-color="3C3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DB 3D Slicer.png</span><span class="informations">748×269 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @pieper (2020-08-22 17:17 UTC)

<p>Did you try the dicom patcher module?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html" class="onebox" target="_blank">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicompatcher.html</a></p>
<p>Extending it with extra name editing fearures would very feasible, and a good project that any python programmer could take on.</p>

---

## Post #13 by @lassoan (2020-08-22 18:37 UTC)

<p>Slicer can read patient name with various encodings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e81372640b3b8ebdf77f7cc18e8683ecf44bbb8.png" data-download-href="/uploads/short-url/8UWrEd1vUWgdY66VSsIw4bljInu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e81372640b3b8ebdf77f7cc18e8683ecf44bbb8_2_673x500.png" alt="image" data-base62-sha1="8UWrEd1vUWgdY66VSsIw4bljInu" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e81372640b3b8ebdf77f7cc18e8683ecf44bbb8_2_673x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e81372640b3b8ebdf77f7cc18e8683ecf44bbb8_2_1009x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e81372640b3b8ebdf77f7cc18e8683ecf44bbb8_2_1346x1000.png 2x" data-dominant-color="3D4246"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1537×1141 77.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There is a good chance that there is something wrong with the DICOM file encoding, but of course it is possible that the DICOM file is valid and DCMTK toolkit does not interpret it correctly. We need an example file to verify. You can create an example data set by creating a patient in the dental imaging software (with non-Latin characters in the patient name) and acquire an image of anything.</p>

---

## Post #14 by @avrilev (2020-08-22 19:23 UTC)

<p>I can’t find that module on 3d slicer…</p>
<p>Can you guide me through, please?</p>
<p>Avri</p>

---

## Post #15 by @avrilev (2020-08-22 19:30 UTC)

<p>I really don’t understand what you guys referring to by “. We need an example file to verify. You can create an example data set by creating a patient in the dental imaging software (with non-Latin characters in the patient name) and acquire an image of anything.”</p>
<p>What kind of file? I’m really confused now.</p>
<p>Also I cannot fine the DICOM Patcher module within 3D Slicer ( in the Slicer extension section)…</p>
<p>Thanks,</p>
<p>Dr. Avri Lev</p>

---

## Post #16 by @avrilev (2020-08-22 19:53 UTC)

<p>I found the module. Thank you guys, everything back to normal. <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #17 by @lassoan (2020-08-22 19:53 UTC)

<p>We can only fix those problems that we can reproduce on our own computers. With DICOM images that we have, we don’t have any patient name encoding issues. Therefore, if you want us to investigate this issue then you need to send us a DICOM image file that you have problem with. We don’t want to handle files that have patient health information in it, so send us a DICOM image file that does not belong to a real patient (but it contains a fake patient name with non-latin characters in it).</p>

---
