# OpenDose3D module is not loaded

**Topic ID**: 36045
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/opendose3d-module-is-not-loaded/36045

---

## Post #1 by @Huihui (2024-05-10 05:14 UTC)

<p>Hi there,</p>
<p>I’m trying to install OpedDose3D extension, but the module can not be loaded. Could anyone please help me? Thanks!</p>
<p>Operating system: Windows<br>
Slicer version: 5.6.0<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dc3437bf0d0883572a25850c28bc78187a7b476.png" data-download-href="/uploads/short-url/1XKyyUSxRETEkOUvoEDQdxbzORw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc3437bf0d0883572a25850c28bc78187a7b476_2_690x394.png" alt="image" data-base62-sha1="1XKyyUSxRETEkOUvoEDQdxbzORw" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc3437bf0d0883572a25850c28bc78187a7b476_2_690x394.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc3437bf0d0883572a25850c28bc78187a7b476_2_1035x591.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0dc3437bf0d0883572a25850c28bc78187a7b476_2_1380x788.png 2x" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1635×934 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/683021ce646b8836947030b717ba9ee13f123c74.png" data-download-href="/uploads/short-url/eRGMjW6qmkHbTcDthEpOkE7H1CA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/683021ce646b8836947030b717ba9ee13f123c74_2_690x304.png" alt="image" data-base62-sha1="eRGMjW6qmkHbTcDthEpOkE7H1CA" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/683021ce646b8836947030b717ba9ee13f123c74_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/683021ce646b8836947030b717ba9ee13f123c74_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/683021ce646b8836947030b717ba9ee13f123c74_2_1380x608.png 2x" data-dominant-color="EDEDF7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×848 72.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pkenned (2024-06-11 15:20 UTC)

<p>I am also having the same issue. I wonder were you able to find a solution? Thanks.</p>

---

## Post #3 by @pcom12345 (2025-01-23 12:33 UTC)

<p>Hi, I have recently downloaded Slicer 3D and I am trying to use the OpenDose3D module with the same issue that you have detailed above. The error message I am getting is:<br>
loadSourceAsModule - Failed to load file “C:/Users/PCOMISKE/Desktop/Slicer 5.6.2/slicer.org/Extensions-32448/OpenDose3D/lib/Slicer-5.6/qt-scripted-modules/OpenDose3D.py”  as module “OpenDose3D” !<br>
Fail to instantiate module  “OpenDose3D”<br>
The following modules failed to be instantiated:<br>
Calibration<br>
OpenDose3D<br>
Gamma</p>
<p>Do you have any advice for overcoming this issue? Thanks</p>

---

## Post #4 by @Alex_Vergara (2025-01-31 13:21 UTC)

<p>Hello, for all questions you can use our mail <a href="mailto:opendose3d@gmail.com">opendose3d@gmail.com</a></p>
<p>For reporting issues you can use <a href="https://gitlab.com/opendose/opendose3d/-/issues" rel="noopener nofollow ugc">Issues · OpenDose / SlicerOpenDose3D · GitLab</a></p>
<p>We are happy to help: for the moment there is a slicer 5.8 upgrade that makes opendose3d not compatible, we are working in this regard WIP. We have also detected issues with the last version of elastix.</p>

---

## Post #5 by @pcom12345 (2025-01-31 17:18 UTC)

<p>I am currently using version 5.6.2 of slicer - I think this is same version used in the OpenDose3D videos that were recently added to youtube so I assumed it was not an issue with the version.</p>

---

## Post #6 by @Alex_Vergara (2025-02-01 11:20 UTC)

<p>Your issue is being treated here <a href="https://gitlab.com/opendose/opendose3d/-/issues/92" class="inline-onebox" rel="noopener nofollow ugc">OpenDose3D failed to be instantiated/loaded (#92) · Issues · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---
