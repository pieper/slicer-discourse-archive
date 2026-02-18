# How to add custom plugin to the cpack package

**Topic ID**: 25322
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/how-to-add-custom-plugin-to-the-cpack-package/25322

---

## Post #1 by @jay1987 (2022-09-19 03:45 UTC)

<p>i have wrote one custom plugin , and i want the PACKAGE project can package the plugin<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a37c29ad22681b082f364cdf6ef9cb90e0d406b.png" alt="image" data-base62-sha1="aAyNvbSuEs8jzGtIH7TTYL35C0H" width="176" height="30"><br>
i try to write the cmake in cmake_install.cmake like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab4ab2343c98e24442206625dbab283d8ddf023.png" data-download-href="/uploads/short-url/jN2Ye6Qnu8Rm6iYfpzaDita1U9t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab4ab2343c98e24442206625dbab283d8ddf023.png" alt="image" data-base62-sha1="jN2Ye6Qnu8Rm6iYfpzaDita1U9t" width="690" height="37" data-dominant-color="272826"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">765×42 2.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
it does true to package the custom plugin into the slicer project tree and running without error,but it can’t package into a exe file with the error below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba2402a1bea6fc60e446f60e28ececbd59836c3f.png" data-download-href="/uploads/short-url/qyFXAKC5ODL75nuZRlCRQBKB2eX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba2402a1bea6fc60e446f60e28ececbd59836c3f.png" alt="image" data-base62-sha1="qyFXAKC5ODL75nuZRlCRQBKB2eX" width="690" height="25" data-dominant-color="F2F3F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1365×50 2.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i guess i wrote a wrong way , it should not wirte into the cmake_install.cmake file,but i don’t known which file should do the work.</p>

---
