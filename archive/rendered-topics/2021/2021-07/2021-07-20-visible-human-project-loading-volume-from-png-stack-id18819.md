# Visible human project - loading volume from PNG stack

**Topic ID**: 18819
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/visible-human-project-loading-volume-from-png-stack/18819

---

## Post #1 by @CP_HO (2021-07-20 12:58 UTC)

<p>Operating system: windows 10 professional<br>
Slicer version:4.11<br>
Expected behavior: open header<br>
Actual behavior: cannot open header</p>
<p>Dear all:  I wish to use the data in the Visual Human Anatomy project to do 3D rendering.  I downloaded the data set.  Some of them are in RGB format and some in rar format.  I unzipped them with winrar but on opening them with infranview, it says they cannot find the header.  Is there anyway I can correct that?  thanks for your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31093547ca1fb161eb816b89212769c057f96821.png" data-download-href="/uploads/short-url/6ZN7I5qxpDjLvSaiaEmZYSxf5rH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31093547ca1fb161eb816b89212769c057f96821.png" alt="image" data-base62-sha1="6ZN7I5qxpDjLvSaiaEmZYSxf5rH" width="690" height="346" data-dominant-color="2A2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×575 4.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-08-10 00:20 UTC)

<p>You can load visible human color PNG images as a 3D volume using ImageStacks module in SlicerMorph extension. You need to use the very latest Slicer Preview Release and disable the “grayscale” option.</p>

---

## Post #3 by @CP_HO (2021-08-10 02:03 UTC)

<p>Thank you very much<br>
Will try</p>

---

## Post #4 by @CP_HO (2021-08-15 18:56 UTC)

<p>Dear Andras</p>
<p>thank you very much for your advice.</p>
<p>yes, we can do it with the PNG images with no problem. We had problems when we open the other photos, (non-PNG ones) that we had problems with the headers. Usually after we decompress the photos.</p>
<p>thanks again</p>
<p>cpho</p>

---

## Post #5 by @lassoan (2021-08-15 19:55 UTC)

<p>Which images exactly you have problem with? Please send link to the folder.</p>

---
