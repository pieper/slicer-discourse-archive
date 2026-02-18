# load DICOM import

**Topic ID**: 2839
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/load-dicom-import/2839

---

## Post #1 by @HwangJeongUk (2018-05-17 11:46 UTC)

<p>Operating system: windows7<br>
Slicer version: 4.9.0<br>
Expected behavior: DICOM load<br>
Actual behavior:</p>
<p>There is no change after loading the DICOM file.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28abef20af040c325687722baf5ac575c160a664.png" alt="1" data-base62-sha1="5NNsSXUOMHZYRSQPzhrN5k4DQ9u" width="229" height="171"><br>
If you drag the DICOM folder to the Slicer window and click “Load directory into dicom database”, nothing happens.<br>
When I import to DICOM Browser, there is no dicom data information.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d89b97e0a1721f65d0dd502eace1b8e9775236a.png" data-download-href="/uploads/short-url/b3VQ0fCebwaFov4RlYLEHc7RGYO.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d89b97e0a1721f65d0dd502eace1b8e9775236a.png" alt="2" data-base62-sha1="b3VQ0fCebwaFov4RlYLEHc7RGYO" width="690" height="362" data-dominant-color="DEE7ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1029×541 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The DICOM file I use is probably not a problem.<br>
It is being used in other programs.<br>
I have tried to input and import to try the DICOM Patcher module, but nothing is active in the viewer.<br>
I am also a Korean student. So I can not use English programs well.<br>
So it is difficult to do self-study.<br>
Please help me.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-05-17 12:42 UTC)

<p>please take a look at</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser</a></p>

---

## Post #3 by @pieper (2018-05-17 13:03 UTC)

<p>Also be sure that all the directories have English characters only (sometimes characters from other languages can confuse the parsing).</p>

---
