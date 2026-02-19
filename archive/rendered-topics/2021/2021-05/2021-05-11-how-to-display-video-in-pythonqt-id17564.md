---
topic_id: 17564
title: "How To Display Video In Pythonqt"
date: 2021-05-11
url: https://discourse.slicer.org/t/17564
---

# How to display video in PythonQt?

**Topic ID**: 17564
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/how-to-display-video-in-pythonqt/17564

---

## Post #1 by @Chintha_Siva_Prasad (2021-05-11 07:48 UTC)

<p>How can I display a video in Slicer through PythonQt?</p>

---

## Post #2 by @lassoan (2021-05-13 13:09 UTC)

<p>You can display animated gifs, and some videos using QVideo:</p>
<pre><code class="lang-python">movie = qt.QMovie("c:/path/to/myvideo.gif")
label = qt.QLabel()
label.setMovie(movie)
label.show()
movie.start()
</code></pre>
<p>You can load and replay mkv videos (compressed with VP9 or AV1) as volume sequences in slice views using SlicerIGSIO extension.</p>
<p>You can probably display videos using <code>slicer.qSlicerWebWidget()</code>. It is a Chromium web browser window, so it has all the infrastructure to replay videos, but I’m not sure what codecs are installed.</p>

---

## Post #4 by @lhefeng662 (2025-05-29 09:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db9a41a217cecb418278761cac7f038d711e75f.png" data-download-href="/uploads/short-url/b5AuXffTuv8wF3UwnIbfI4ZT3C7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db9a41a217cecb418278761cac7f038d711e75f_2_689x397.png" alt="image" data-base62-sha1="b5AuXffTuv8wF3UwnIbfI4ZT3C7" width="689" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db9a41a217cecb418278761cac7f038d711e75f_2_689x397.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db9a41a217cecb418278761cac7f038d711e75f_2_1033x595.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4db9a41a217cecb418278761cac7f038d711e75f_2_1378x794.png 2x" data-dominant-color="8E8C90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2388×1376 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am using  sequence(or videoUtil) to load mkv videos, but the videos can only be displayed as volumes and cannot be fully watched. What should I do</p>

---
