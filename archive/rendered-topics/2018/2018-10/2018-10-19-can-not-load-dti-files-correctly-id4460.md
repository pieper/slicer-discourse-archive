---
topic_id: 4460
title: "Can Not Load Dti Files Correctly"
date: 2018-10-19
url: https://discourse.slicer.org/t/4460
---

# Can not load DTI files correctly

**Topic ID**: 4460
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/can-not-load-dti-files-correctly/4460

---

## Post #1 by @wpgao (2018-10-19 09:05 UTC)

<p>Operating system: win10<br>
Slicer version: 4.9<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi Guys,</p>
<p>I had encounter a problem when loading the dicom files of DTI obtained from Philips Achieva 3.0T. The file can be read but can not be shown correctly. There are some warnings<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00c1470cf847e838c4f55222b85ddfda20faeca1.png" alt="warning" data-base62-sha1="6G5U2m6DFBvQtGbIwQWaA9Jidb" width="595" height="377">  and the DTI data was not shown correctly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edfc072ad8fceac1481203d6358fe6d0a20862b.png" data-download-href="/uploads/short-url/27A4mZZgnQPEvXDm135A16WoSwP.png?dl=1" title="show" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0edfc072ad8fceac1481203d6358fe6d0a20862b_2_626x500.png" alt="show" data-base62-sha1="27A4mZZgnQPEvXDm135A16WoSwP" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0edfc072ad8fceac1481203d6358fe6d0a20862b_2_626x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edfc072ad8fceac1481203d6358fe6d0a20862b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0edfc072ad8fceac1481203d6358fe6d0a20862b.png 2x" data-dominant-color="34343F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">show</span><span class="informations">706×563 37.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I also modified the setting according to the warning, but the DTI data was still not shown correctly. Any advice about this problem is appreciate!</p>

---

## Post #2 by @pieper (2018-10-19 12:00 UTC)

<p>Hi <a class="mention" href="/u/wpgao">@wpgao</a> -</p>
<p>For diffusion MRI, install the SlicerDMRI extension: <a href="http://dmri.slicer.org/">http://dmri.slicer.org/</a> and try again.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @wpgao (2018-10-22 02:36 UTC)

<p>Hi Steve,</p>
<p>Thanks. It’s done!<br>
In fact, the module “DWIConvert” could convert the diffusion weighted dicom into nrrd file.</p>
<p>Best,<br>
Wenpeng</p>

---
