# ERROR -can  not download .........as scalar volume

**Topic ID**: 16406
**Date**: 2021-03-07
**URL**: https://discourse.slicer.org/t/error-can-not-download-as-scalar-volume/16406

---

## Post #1 by @zaineb_chiha (2021-03-07 01:38 UTC)

<p>Operating system:ubuntu<br>
Slicer version:Slicer-4.11.20200930-linux-amd64<br>
Expected behavior: load  slices to visualizate it<br>
Actual behavior:ERROR -can  not download …as scalar volume</p>
<p>i can not find the DICOM patcher as extension in the latest version of slicer 3D i downloaded</p>

---

## Post #2 by @zaineb_chiha (2021-03-06 23:05 UTC)

<p>i can not find DICOM patcher in the latest version , i had the same problem to visualize MRI data, what can i do please</p>

---

## Post #3 by @zaineb_chiha (2021-03-06 23:06 UTC)

<p>i had the same problem to visualize MRI data, i can not find DICOM patcher in the latest version ,  what can i do please</p>

---

## Post #4 by @zaineb_chiha (2021-03-06 23:11 UTC)

<p>Version downloaded-Slicer-4.11.20200930-linux-amd64<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba92769b6d299ed0f534b14442d1cbea937f4207.png" data-download-href="/uploads/short-url/qCuByil4735Ro5cjhWlhtDfKXvV.png?dl=1" title="Screenshot from 2021-03-04 16-18-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba92769b6d299ed0f534b14442d1cbea937f4207_2_690x387.png" alt="Screenshot from 2021-03-04 16-18-27" data-base62-sha1="qCuByil4735Ro5cjhWlhtDfKXvV" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba92769b6d299ed0f534b14442d1cbea937f4207_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba92769b6d299ed0f534b14442d1cbea937f4207_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba92769b6d299ed0f534b14442d1cbea937f4207.png 2x" data-dominant-color="969B9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-03-04 16-18-27</span><span class="informations">1366×768 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-03-07 01:43 UTC)

<p>These all look like reprocessed frames. They are probably rejected because they don’t have geometry information (e.g., they are screenshots). Please follow troubleshooting instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#when-i-click-on-load-selection-to-slicer-i-get-an-error-message-could-not-load-as-a-scalar-volume">here</a>.</p>
<aside class="quote no-group" data-username="zaineb_chiha" data-post="3" data-topic="16406">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zaineb_chiha/48/10197_2.png" class="avatar"> zaineb_chiha:</div>
<blockquote>
<p>i can not find DICOM patcher in the latest version</p>
</blockquote>
</aside>
<p>DICOM patcher is a module that you can find by hitting Ctrl+F and then typing <code>DICOM patcher</code>.</p>

---

## Post #6 by @zaineb_chiha (2021-03-07 11:25 UTC)

<p>Thank you for the response , but i already checked it and nothing works , i dunno what to do</p>

---

## Post #7 by @lassoan (2021-03-07 13:27 UTC)

<p>Then this applies: “If none of the above helps then check the Slicer error logs and report the error on the Slicer forum. If you share the data (e.g., upload it to Dropbox and add the link to the error report) then Slicer developers can reproduce and fix the problem faster.” - share the application log, and - if possible - a sample data set.</p>

---
