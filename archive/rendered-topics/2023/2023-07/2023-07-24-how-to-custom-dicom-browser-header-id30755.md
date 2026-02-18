# How to custom dicom browser header?

**Topic ID**: 30755
**Date**: 2023-07-24
**URL**: https://discourse.slicer.org/t/how-to-custom-dicom-browser-header/30755

---

## Post #1 by @icedream (2023-07-24 11:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74bfd730c7926803915f91f5b105767701d3804a.png" data-download-href="/uploads/short-url/gEOoZEHr15m9y7bKWFW24UEkzN0.png?dl=1" title="a84307c54e3b2aa40790080b26b72c9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bfd730c7926803915f91f5b105767701d3804a_2_690x104.png" alt="a84307c54e3b2aa40790080b26b72c9" data-base62-sha1="gEOoZEHr15m9y7bKWFW24UEkzN0" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bfd730c7926803915f91f5b105767701d3804a_2_690x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bfd730c7926803915f91f5b105767701d3804a_2_1035x156.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74bfd730c7926803915f91f5b105767701d3804a_2_1380x208.png 2x" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a84307c54e3b2aa40790080b26b72c9</span><span class="informations">1910×288 8.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i want to remove sex header from patient table,how to do it through python or c++ or other method?<br>
I found dicom-schema.sql has config ,but when i changed the data , it’s not work</p>

---

## Post #2 by @lassoan (2023-07-24 15:56 UTC)

<p>See examples for customizing columns displayed in the DICOM browser in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-table-columns-in-dicom-browser">script repository</a>.</p>
<p>Note that the <code>Sex</code> field in you screenshot shows invalid value. The <a href="https://dicom.innolitics.com/ciods/general-ecg/patient/00100040">allowed values for this allowed in DICOM</a> are <code>M</code>, <code>F</code>, <code>O</code>. Where does this DICOM data set comes from?</p>

---

## Post #3 by @icedream (2023-07-25 01:08 UTC)

<p>thank you lassoan !!</p>

---
