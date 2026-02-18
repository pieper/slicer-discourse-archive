# Is the dicom database can manager file like .nrrd or .nii?

**Topic ID**: 32148
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/is-the-dicom-database-can-manager-file-like-nrrd-or-nii/32148

---

## Post #1 by @icedream (2023-10-11 01:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/891a660d016f2bae02d7a1cecd438a81a4ac55d7.png" data-download-href="/uploads/short-url/jyRYhoJxXTwuGxBkl39QodaHO5N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/891a660d016f2bae02d7a1cecd438a81a4ac55d7.png" alt="image" data-base62-sha1="jyRYhoJxXTwuGxBkl39QodaHO5N" width="690" height="447" data-dominant-color="212121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1427×925 6.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>i can use dicom database to manager my dicom data , is it possible to use dicom database to manager single file like nrrd or nii file?</p>

---

## Post #2 by @pieper (2023-10-11 17:09 UTC)

<p>The dicom database extracts metadata that only exists for dicom files.  For other formats people typically use filenames and folders of the regular OS for organization and drop the files on Slicer to load.</p>

---

## Post #3 by @muratmaga (2023-10-11 18:38 UTC)

<aside class="quote no-group" data-username="icedream" data-post="1" data-topic="32148">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/48db29/48.png" class="avatar"> icedream:</div>
<blockquote>
<p>i can use dicom database to manager my dicom data , is it possible to use dicom database to manager single file like nrrd or nii file?</p>
</blockquote>
</aside>
<p>If you need a DB manager for your datasets in nii.gz, nrrd (as well as dicoms), you may want to look into XNAT. There used to be a Slicer extension as well. Though I haven’t look into it recently.</p>

---
