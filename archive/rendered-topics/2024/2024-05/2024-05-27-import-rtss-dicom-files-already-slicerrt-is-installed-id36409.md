---
topic_id: 36409
title: "Import Rtss Dicom Files Already Slicerrt Is Installed"
date: 2024-05-27
url: https://discourse.slicer.org/t/36409
---

# Import RTSS-DICOM files (Already SlicerRT is Installed)

**Topic ID**: 36409
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/import-rtss-dicom-files-already-slicerrt-is-installed/36409

---

## Post #1 by @youngchanseo (2024-05-27 08:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f850a50b6e6b0e172bf1ea09c2aa70dc844f1be7.png" data-download-href="/uploads/short-url/zqHbYuAf2SmOAOsMfsy1NNP30xN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f850a50b6e6b0e172bf1ea09c2aa70dc844f1be7_2_690x421.png" alt="image" data-base62-sha1="zqHbYuAf2SmOAOsMfsy1NNP30xN" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f850a50b6e6b0e172bf1ea09c2aa70dc844f1be7_2_690x421.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f850a50b6e6b0e172bf1ea09c2aa70dc844f1be7_2_1035x631.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f850a50b6e6b0e172bf1ea09c2aa70dc844f1be7.png 2x" data-dominant-color="2F3136"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1379×843 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to import  DICOM-RTSS  files, and then want to convert to DICOM seg format.</p>
<p>But there is something error that i can see in the python script,<br>
"Python 3.9.10 (main, May 19 2024, 23:18:48) [MSC v.1939 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Python] Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects<br>
[Python] Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects"</p>
<p>However, I already downloaded the “SLicer RT” extension as you can see in the picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afaec8779cdb034685819e213357c80358cc011f.png" data-download-href="/uploads/short-url/p4a1KWdY7dRDmDxUgblt4CPmuTl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afaec8779cdb034685819e213357c80358cc011f_2_690x273.png" alt="image" data-base62-sha1="p4a1KWdY7dRDmDxUgblt4CPmuTl" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afaec8779cdb034685819e213357c80358cc011f_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afaec8779cdb034685819e213357c80358cc011f_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afaec8779cdb034685819e213357c80358cc011f_2_1380x546.png 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2210×877 91.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I solve this problem?<br>
I guess there is something wrong with the extension settings…</p>

---

## Post #2 by @cpinter (2024-05-27 08:54 UTC)

<p>The error in the Python message in the screenshot suggests that you did not load the file using the DICOM browser, but as a regular file. Sorry if this is basic but after selecting the study (and with that all the series) did you click the Load button on the bottom (as visible in the first screenshot)?</p>
<p>Update: After installing an extension you need to restart Slicer, this may be another source of problem.</p>

---

## Post #3 by @youngchanseo (2024-05-28 04:45 UTC)

<p>(This is Rt structure DICOM (DICOM-RTSS) file’s metadata )<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/463c22cf658ccfb0242396d2eb0a4162beddd21e.png" data-download-href="/uploads/short-url/a1kglxw4KERmPzrOgQx44zScst8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463c22cf658ccfb0242396d2eb0a4162beddd21e_2_690x486.png" alt="image" data-base62-sha1="a1kglxw4KERmPzrOgQx44zScst8" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463c22cf658ccfb0242396d2eb0a4162beddd21e_2_690x486.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/463c22cf658ccfb0242396d2eb0a4162beddd21e_2_1035x729.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/463c22cf658ccfb0242396d2eb0a4162beddd21e.png 2x" data-dominant-color="3E3F42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1263×891 82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did click the DICOM-RTSS file and clicked the load button on the bottom.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c6a5d5988c02a8c64af6ad720afa5bfa9d8cfd6.png" data-download-href="/uploads/short-url/dbxOncvsiZMfa5x2csqlvbRoyk6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c6a5d5988c02a8c64af6ad720afa5bfa9d8cfd6_2_689x194.png" alt="image" data-base62-sha1="dbxOncvsiZMfa5x2csqlvbRoyk6" width="689" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c6a5d5988c02a8c64af6ad720afa5bfa9d8cfd6_2_689x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c6a5d5988c02a8c64af6ad720afa5bfa9d8cfd6_2_1033x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c6a5d5988c02a8c64af6ad720afa5bfa9d8cfd6.png 2x" data-dominant-color="282A2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1231×347 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But i can still see the python script as "  Please install SlicerRT extension to enable loading of DICOM RT Structure Set objects "<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902b8edfdef21c491e6bb815dd8dc245f7799e27.png" data-download-href="/uploads/short-url/kzo4RWU6rj51sIsL5Yk5GWqaTht.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902b8edfdef21c491e6bb815dd8dc245f7799e27_2_690x494.png" alt="image" data-base62-sha1="kzo4RWU6rj51sIsL5Yk5GWqaTht" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902b8edfdef21c491e6bb815dd8dc245f7799e27_2_690x494.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/902b8edfdef21c491e6bb815dd8dc245f7799e27_2_1035x741.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/902b8edfdef21c491e6bb815dd8dc245f7799e27.png 2x" data-dominant-color="39383B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1255×899 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I just import normal MR images, it shows normally.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0f444d6404269975d2af454f684e39df200d135.png" data-download-href="/uploads/short-url/ynzW4i04kFCK2o66KiGw8R2T6q9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0f444d6404269975d2af454f684e39df200d135.png" alt="image" data-base62-sha1="ynzW4i04kFCK2o66KiGw8R2T6q9" width="690" height="368" data-dominant-color="2D3035"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1139×609 28.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e1802427b6f220d7efa03265594e5faa227b3ff.jpeg" data-download-href="/uploads/short-url/8Rj2AQccPQWdkIB6bxgGMOb0xBl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e1802427b6f220d7efa03265594e5faa227b3ff_2_410x500.jpeg" alt="image" data-base62-sha1="8Rj2AQccPQWdkIB6bxgGMOb0xBl" width="410" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e1802427b6f220d7efa03265594e5faa227b3ff_2_410x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e1802427b6f220d7efa03265594e5faa227b3ff_2_615x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e1802427b6f220d7efa03265594e5faa227b3ff.jpeg 2x" data-dominant-color="423E40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">727×886 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @youngchanseo (2024-05-28 05:02 UTC)

<p>The problem has been solved.<br>
When I installed extension, I didn’t run the program as an administrator option.</p>
<p>After I deleted the extension, I ran the program with the administrator option, then reinstalled the extension and ran the program again (with the administrator option).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbb1c5f4247c15fcc255c98c66851310c9aa5c8b.jpeg" data-download-href="/uploads/short-url/zUAINoJhvzdpo7Klp34N2uFbvDB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb1c5f4247c15fcc255c98c66851310c9aa5c8b_2_590x500.jpeg" alt="image" data-base62-sha1="zUAINoJhvzdpo7Klp34N2uFbvDB" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb1c5f4247c15fcc255c98c66851310c9aa5c8b_2_590x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb1c5f4247c15fcc255c98c66851310c9aa5c8b_2_885x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbb1c5f4247c15fcc255c98c66851310c9aa5c8b_2_1180x1000.jpeg 2x" data-dominant-color="373655"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1286×1089 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>

---

## Post #5 by @cpinter (2024-05-28 11:12 UTC)

<p>Great! Special thanks for sharing the solution!</p>

---
