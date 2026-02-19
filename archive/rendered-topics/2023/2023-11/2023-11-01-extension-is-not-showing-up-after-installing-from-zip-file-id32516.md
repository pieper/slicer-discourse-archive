---
topic_id: 32516
title: "Extension Is Not Showing Up After Installing From Zip File"
date: 2023-11-01
url: https://discourse.slicer.org/t/32516
---

# Extension is not showing up after installing from zip file

**Topic ID**: 32516
**Date**: 2023-11-01
**URL**: https://discourse.slicer.org/t/extension-is-not-showing-up-after-installing-from-zip-file/32516

---

## Post #1 by @haphantran (2023-11-01 00:07 UTC)

<p>Hi guys,<br>
I followed the extension build process here <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" rel="noopener nofollow ugc">Extensions — 3D Slicer documentation</a><br>
and got the zip file to work on 5.3 preview before.<br>
Now we have 5.4 stable, I installed it, pull the new source code and rebuilt the application from source, then package the extension again.<br>
When I install the extension from zip file, it was successful (only concern is that the version is NA but I’m not sure how to fix that)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b5a6cfe7e5e8e7cf978d9525bf3c173eb7682cc.png" data-download-href="/uploads/short-url/d29bxnTMVRp9cEwB24JyqRjpzFa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a6cfe7e5e8e7cf978d9525bf3c173eb7682cc_2_690x73.png" alt="image" data-base62-sha1="d29bxnTMVRp9cEwB24JyqRjpzFa" width="690" height="73" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a6cfe7e5e8e7cf978d9525bf3c173eb7682cc_2_690x73.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a6cfe7e5e8e7cf978d9525bf3c173eb7682cc_2_1035x109.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b5a6cfe7e5e8e7cf978d9525bf3c173eb7682cc_2_1380x146.png 2x" data-dominant-color="F2F7FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×205 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After restart, the extension doesn’t show up as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58213a4375e14fc4a4ef35a2c2e4f88fe2bf564a.png" data-download-href="/uploads/short-url/czDcQqpeF6olimDd9oywXY4P0CK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58213a4375e14fc4a4ef35a2c2e4f88fe2bf564a_2_690x365.png" alt="image" data-base62-sha1="czDcQqpeF6olimDd9oywXY4P0CK" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58213a4375e14fc4a4ef35a2c2e4f88fe2bf564a_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58213a4375e14fc4a4ef35a2c2e4f88fe2bf564a_2_1035x547.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58213a4375e14fc4a4ef35a2c2e4f88fe2bf564a.png 2x" data-dominant-color="B9B8BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1368×724 55.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
How should I troubleshoot it?</p>

---

## Post #2 by @lassoan (2023-11-01 13:57 UTC)

<p>Slicer and extension versions are encoded in folder names in the extension .zip files. Check if they contain the correct versions.</p>
<p>Having NA as extension version may be due to not having the source code of Slicer or the extension under revision control (you must build from a git tree, not from an extacted zip file that you downloaded from github).</p>

---

## Post #3 by @haphantran (2023-11-03 03:25 UTC)

<p>Hi Andras,<br>
Thank you for the answer.<br>
I did build 3D Slicer from the git repo. Here is the git log result<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4115f75d89fabbf8d7ab87e3db844f28743d042.png" alt="image" data-base62-sha1="ug2rAwgKXhhQlAHmhIHmIoHhKP8" width="593" height="331"></p>
<p>This is the git log in our extension repo:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10aefaa4234ca6da85901934290121a06010fb8e.png" alt="image" data-base62-sha1="2nAwT2VQpz3oFdHNj1xyT7KcBYi" width="579" height="293"></p>
<p>Here is the zip file I got after I built the extension<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b30a7a4884c569f4fa41998b2bea3c6ed98e205.png" alt="image" data-base62-sha1="1AZuFHwhnfot32bBVO8WZfzqmgd" width="681" height="43"><br>
The file name of the zip file has the hash of the last commit and the date-time as well.<br>
Any other ideas that might be an issue for us?<br>
Thank you very much!</p>

---

## Post #4 by @jamesobutler (2023-11-03 03:44 UTC)

<p>Does the python console indicate any errors loading the module? Maybe the new Slicer version is incompatible with your extension now which is why it worked for you previously, but now no longer.</p>
<p>Does your generated ZIP contain all of the module files that you expect? If not, make sure your CMakeLists files are appropriately including all files to include in the install package. Maybe you changed the organization of files since the previous time when it was working for you with an older Slicer version?</p>

---
