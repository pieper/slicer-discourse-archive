# Is there a way to look all metadata information of a Dicom file like itk-snap did

**Topic ID**: 37304
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-look-all-metadata-information-of-a-dicom-file-like-itk-snap-did/37304

---

## Post #1 by @lucarqi (2024-07-10 14:21 UTC)

<p>I’m new to 3D Slicer. ITK-snap can easily read “Image Metadata” like follow(anonymous) :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19819ec6f56de6751fa0a32bfa41533b78c212e6.png" data-download-href="/uploads/short-url/3DDE6kHftsxE3vI6QqZXoWvP9xI.png?dl=1" title="2dd9d714d6d196d8e12303065a060b8b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19819ec6f56de6751fa0a32bfa41533b78c212e6.png" alt="2dd9d714d6d196d8e12303065a060b8b" data-base62-sha1="3DDE6kHftsxE3vI6QqZXoWvP9xI" width="566" height="500" data-dominant-color="DFE3E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2dd9d714d6d196d8e12303065a060b8b</span><span class="informations">644×568 17.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can find basic information , when I load a Dicom file in follows(anonymous):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51bb2ae0e87892c8f28307e44bc9a11d5e84f56b.png" data-download-href="/uploads/short-url/bF1G8qWbWjO4h5r5eqSIYOOyjdF.png?dl=1" title="ba888c68793f6e2c4c5d40984da35a43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51bb2ae0e87892c8f28307e44bc9a11d5e84f56b.png" alt="ba888c68793f6e2c4c5d40984da35a43" data-base62-sha1="bF1G8qWbWjO4h5r5eqSIYOOyjdF" width="690" height="422" data-dominant-color="E8F0F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ba888c68793f6e2c4c5d40984da35a43</span><span class="informations">768×470 5.27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, there still miss a lot of information compared to ITK-snap.<br>
So, there is a simple way to look all information like ITK-snap did?</p>

---

## Post #2 by @jamesobutler (2024-07-10 14:29 UTC)

<p>There is a section in the DICOM module documentation regarding how to view the metadata. See linked section below:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#view-dicom-metadata" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#view-dicom-metadata</a></p>

---

## Post #3 by @lucarqi (2024-07-11 06:55 UTC)

<p>Thanks. I get metadata in “DICOM database” page, just right click the patient , select “view DICOM metadata”</p>

---
