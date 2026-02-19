---
topic_id: 5223
title: "Problem With Loading Files"
date: 2018-12-29
url: https://discourse.slicer.org/t/5223
---

# Problem with loading files

**Topic ID**: 5223
**Date**: 2018-12-29
**URL**: https://discourse.slicer.org/t/problem-with-loading-files/5223

---

## Post #1 by @kartezjush (2018-12-29 22:01 UTC)

<p>Hello, I have problem with loading files like on screenshot. There is log too. Do I have wrong type of files? If yes, what I have to do to create a SLT file. I have only that files: <a href="https://www.zeta-uploader.com/pl/1094621942" rel="noopener nofollow ugc">https://www.zeta-uploader.com/pl/1094621942</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd09d505907c9dc7829f8c596427cfb5c2913ab6.png" data-download-href="/uploads/short-url/qYjj2ARAMMlRu7irQkuAAcrwj54.png?dl=1" title="48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd09d505907c9dc7829f8c596427cfb5c2913ab6_2_690x388.png" alt="48" data-base62-sha1="qYjj2ARAMMlRu7irQkuAAcrwj54" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd09d505907c9dc7829f8c596427cfb5c2913ab6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd09d505907c9dc7829f8c596427cfb5c2913ab6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bd09d505907c9dc7829f8c596427cfb5c2913ab6_2_1380x776.png 2x" data-dominant-color="C3C4C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">48</span><span class="informations">1920×1080 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Log file: <a href="https://megawrzuta.pl/download/b1a7414d5d7e81c62a66e9803f1c9616.html" class="inline-onebox" rel="noopener nofollow ugc">Darmowy hosting plików - wrzucaj i dziel się plikami za darmo |</a></p>

---

## Post #2 by @lassoan (2018-12-30 03:12 UTC)

<p>See the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser">DICOM FAQ</a>:</p>
<blockquote>
<p>Try moving the data and the database directory to a path that includes only US English characters (ASCII) to avoid possible parsing errors. No special, international characters are allowed.</p>
</blockquote>
<p>You’ve tried to load the data set from the folder name C:/Users/P???czek typu gniazdko/Desktop/… folder, which contained a special character. Instead, move your DICOM data to c:\temp and import it from there.</p>

---

## Post #3 by @kartezjush (2018-12-30 11:14 UTC)

<p>Yes, that was Very helpful. Thank you. Problem has been solved.</p>

---
