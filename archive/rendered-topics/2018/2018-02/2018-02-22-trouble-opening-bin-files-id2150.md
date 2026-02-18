# Trouble opening .bin files

**Topic ID**: 2150
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/trouble-opening-bin-files/2150

---

## Post #1 by @aturner (2018-02-22 17:31 UTC)

<p>Hi,</p>
<p>I have a number of bin files from a micro ct scan which i am having trouble opening in 3d slicer, does anyone know how i can open them, as following the procedure for dicom files is not working?</p>
<p>thanks<br>
alex</p>

---

## Post #2 by @pieper (2018-02-22 18:34 UTC)

<p>“.bin” is a pretty generic sounding extension - you might be able to write a converter if you have documentation of know the internal format.</p>
<p>But if the dicom are even close to standard they should work.  Please try the steps in the DICOM faq:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>maybe post the error log and some sample files.</p>

---

## Post #3 by @aturner (2018-02-23 11:08 UTC)

<p>Thanks Steve. So, i have 991 .bin files and a .txt file with all of the scan info in, so i imagine converting the files is a possibility? When i try and open the folder containing all of that, 3dslicer crashes on this loading screen<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6461cc67ba4eab24ba09e63082b9481fdaf9b2a.png" data-download-href="/uploads/short-url/uzyopNu1lW3ybd6pmC5qAXqYcDE.png?dl=1" title="07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6461cc67ba4eab24ba09e63082b9481fdaf9b2a_2_690x252.png" alt="07" data-base62-sha1="uzyopNu1lW3ybd6pmC5qAXqYcDE" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6461cc67ba4eab24ba09e63082b9481fdaf9b2a_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6461cc67ba4eab24ba09e63082b9481fdaf9b2a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6461cc67ba4eab24ba09e63082b9481fdaf9b2a.png 2x" data-dominant-color="E4E5E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">07</span><span class="informations">969×354 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2018-02-23 12:58 UTC)

<p>It looks like you are trying to import the bin files into the dicom database and that won’t work.  It probably crashes because the micro ct files are so big.</p>
<p>You need to figure out what the bin files are and map them into something Slicer can read.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SupportedDataFormat</a></p>
<p>If you know the scan info the most direct method can be to try making a .nhdr file by hand that points to the binary files (assuming you know or can figure out how the data is arranged).</p>
<p><a href="http://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank">http://teem.sourceforge.net/nrrd/format.html</a></p>
<p>Or export a different format from the scanner.</p>

---
