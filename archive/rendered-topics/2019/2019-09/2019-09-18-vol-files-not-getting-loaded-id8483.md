---
topic_id: 8483
title: "Vol Files Not Getting Loaded"
date: 2019-09-18
url: https://discourse.slicer.org/t/8483
---

# .vol files not getting loaded

**Topic ID**: 8483
**Date**: 2019-09-18
**URL**: https://discourse.slicer.org/t/vol-files-not-getting-loaded/8483

---

## Post #1 by @deepz (2019-09-18 16:21 UTC)

<p>Hello Guys,<br>
I wanted to load .vol files in slicer 3d. I kept the mode as Volume only. But when I drag n drop it, all the planes are dark . I have attached a picture too. Kindly share your thoughts on it . Thanks in advance.<br>
<a href="/404" data-orig-href="upload://ssh7vW1C2y3zVSIaV2xklGGrz1e.png">Capture|690x413</a></p>

---

## Post #2 by @lassoan (2019-09-18 18:24 UTC)

<p>There are many file types that use .vol extension. What data you are trying to load?</p>
<p>If it is GE 3D ultrasound data then follow instructions on this page: <a href="https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer" rel="nofollow noopener">https://github.com/SlicerHeart/SlicerHeart#slicerheart-extension-for-3d-slicer</a></p>

---

## Post #3 by @deepz (2019-09-26 07:31 UTC)

<p>Thank you so much. I was able to load the .vol files. Appreciate your help!</p>

---

## Post #4 by @J_Deng (2020-09-11 01:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac9987655746ff0e9dafaf0af438b3bf538154e0.png" data-download-href="/uploads/short-url/oCT3EYBEWRcz8iw3wm5NeKNIhDW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9987655746ff0e9dafaf0af438b3bf538154e0_2_690x360.png" alt="image" data-base62-sha1="oCT3EYBEWRcz8iw3wm5NeKNIhDW" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9987655746ff0e9dafaf0af438b3bf538154e0_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9987655746ff0e9dafaf0af438b3bf538154e0_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac9987655746ff0e9dafaf0af438b3bf538154e0_2_1380x720.png 2x" data-dominant-color="DCE2E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1002 414 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I searched Extensions above using SlicerHeart, cardiac, heart, but it did not return a result. Is SlicerHeart no longer in the list, or did I go to a wrong site [automatically linked from 3D Slicer’s extensions?</p>
<p>I am quite a layman in terms of tech. If the extension could find elsewhere, could I simply download it as we usually download a file and paste it into a corresponding folder [then which one?] in 3DSlicer?<br>
Many thanks,</p>

---

## Post #5 by @muratmaga (2020-09-11 01:56 UTC)

<p>Looks like SlicerHeart built successfully for the latest preview (from yesterday). Which version of Slicer (Help-&gt;About) are you using? Can you try with the latest one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f90c16acdfaa0be7a9a4462a02ea8c49e88d4fd.jpeg" data-download-href="/uploads/short-url/icuM792fOroD6oH1JGGVzBRnp1z.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f90c16acdfaa0be7a9a4462a02ea8c49e88d4fd_2_690x371.jpeg" alt="image" data-base62-sha1="icuM792fOroD6oH1JGGVzBRnp1z" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f90c16acdfaa0be7a9a4462a02ea8c49e88d4fd_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f90c16acdfaa0be7a9a4462a02ea8c49e88d4fd_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f90c16acdfaa0be7a9a4462a02ea8c49e88d4fd_2_1380x742.jpeg 2x" data-dominant-color="E2E7EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1716×923 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @J_Deng (2020-09-11 01:59 UTC)

<p>4.11.0-2020-08-29 r29335 / 0311336 using which I can see SLICERCIP extension but not SLICERHEART. I am downloading the newer version now. Many thanks.</p>

---

## Post #7 by @J_Deng (2020-09-11 02:18 UTC)

<p>Yes, it becomes visible after updating 3D slicer. Thanks again.</p>

---

## Post #8 by @muratmaga (2020-09-11 02:23 UTC)

<p>Glad to hear it. Sometimes extension(s) is/are not built for a particular preview version for various reasons. Whatever the issue was, it is usually fixed in the next preview version (following day)…</p>

---

## Post #9 by @J_Deng (2020-09-11 02:39 UTC)

<p>Got you. If I uninstall an older version having installed the newer version, would it affect segmentations and data that I have already worked on? It should not, but just to be on a safe side.</p>
<p>Also, this extension is to use together with Image3dAPI, which requires to run regsvr32 Image3dLoaderGe.dll . Where could I obtain the dll file? Search 3D slicer and internet did not return such a file for downloading.</p>

---

## Post #10 by @muratmaga (2020-09-11 02:49 UTC)

<p>Installing a new version will not affect the segmentation that you generated with the previous version, particularly between 4.11 series.</p>
<p>As for your second question, unfortunately I am not familiar with SlicerHeart extension. Perhaps others on the forum can help.</p>

---

## Post #11 by @J_Deng (2020-09-11 02:50 UTC)

<p>Thanks for assurance. BW</p>

---

## Post #12 by @lassoan (2020-09-11 03:07 UTC)

<aside class="quote no-group" data-username="J_Deng" data-post="9" data-topic="8483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/j_deng/48/8020_2.png" class="avatar"> J_Deng:</div>
<blockquote>
<p>Also, this extension is to use together with Image3dAPI, which requires to run regsvr32 Image3dLoaderGe.dll . Where could I obtain the dll file? Search 3D slicer and internet did not return such a file for downloading</p>
</blockquote>
</aside>
<p>You can get access by filling in a web form - I’ve added more details here: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#loading-various-3d4d-ultrasound-images-using-image3dapi" class="inline-onebox">SlicerHeart/README.md at master · SlicerHeart/SlicerHeart · GitHub</a></p>

---

## Post #13 by @J_Deng (2020-09-11 04:07 UTC)

<p>Thank you for the helpful change. Registered and waiting for reply.</p>
<p>Is there a downloadable user manual [such as in PDF] available? This will allow me to search key words, find info, and have a go myself before repeated bothering you helpful guys. The online documentation is helpful, but if a topic or key word is not on the page you are browsing, such as automatically make a VIDEO CLIP [rather than manual building from serial PNG captures], use MESH, I could not find their respective starting points.</p>

---

## Post #14 by @muratmaga (2020-09-11 04:19 UTC)

<p>To search documentation, particularly for ones hosted on github, you can use the github’s own search tool and restrict it to “in this repository”, this will search everything in that particular repo. It will probably return more than what you wanted (as it will search for source code too), but it may also be helpful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d7cecfc6bcb516c6bbe5353e615057d2c161481.png" data-download-href="/uploads/short-url/hU7kPm9XU4b7At9pyAbPfFeYLf3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7cecfc6bcb516c6bbe5353e615057d2c161481_2_675x500.png" alt="image" data-base62-sha1="hU7kPm9XU4b7At9pyAbPfFeYLf3" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7cecfc6bcb516c6bbe5353e615057d2c161481_2_675x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7cecfc6bcb516c6bbe5353e615057d2c161481_2_1012x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d7cecfc6bcb516c6bbe5353e615057d2c161481_2_1350x1000.png 2x" data-dominant-color="DADEE2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2083×1542 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @J_Deng (2020-09-11 04:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9275b08b33c4ce3554e3460e20f8c16997737be1.png" data-download-href="/uploads/short-url/kTDRi4YrSGI9se9qMFQTLT3vXGN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9275b08b33c4ce3554e3460e20f8c16997737be1_2_690x468.png" alt="image" data-base62-sha1="kTDRi4YrSGI9se9qMFQTLT3vXGN" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9275b08b33c4ce3554e3460e20f8c16997737be1_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9275b08b33c4ce3554e3460e20f8c16997737be1_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9275b08b33c4ce3554e3460e20f8c16997737be1.png 2x" data-dominant-color="E2E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×777 51.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Many thanks for the info.<br>
A bit unlucky when restricting my MESH search to “in this repository” - 3D Slicer, which seems not on public repositories.</p>

---

## Post #16 by @lassoan (2020-09-11 05:09 UTC)

<p>“Topic” is a very specific term in github. It refers to special keywords attached to repositories. You can search in the 3D Slicer repository instead (<a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a>), as you can see in <a class="mention" href="/u/muratmaga">@muratmaga</a>’s example above.</p>
<p>There are lots of sources of information (this forum, github, tutorials, old and new manuals, old mailing list, etc.) and all these are indexed by google. So, instead of off-line search in a PDF, you can google search. For example, if you google for these, you get very relevant results on the first page:</p>
<ul>
<li>3d slicer load 3d ultrasound image</li>
<li>3d slicer capture video</li>
</ul>

---

## Post #17 by @muratmaga (2020-09-11 05:27 UTC)

<p>and also keyword to search should be “3d slicer” not 3d-slicer</p>

---

## Post #18 by @J_Deng (2020-09-11 12:28 UTC)

<p>Thanks. It appears to me that 3d-slicer with a hyphen was/is an automatic directory on GitHub</p>

---

## Post #19 by @EwertonFreitas (2021-02-23 23:32 UTC)

<p>Hello, Mr. Andras Lasso! I intend to do 3D printing from echocardiogram exams by GE Vivid E 95.<br>
I’ve found out the Extension SlicerHeart and i started to use it. It’s really good!<br>
During my web search i also found a topic written by you. You taught about the use of <code>regsvr32 Image3dLoaderGe.dll</code> to load some of these files as DICOM Module. However, two days ago I filled out the Edison Developer Program’s form, but i didn’t receive a reply yet! Is there any change to receive it?</p>
<p>Thanks!</p>

---

## Post #20 by @lassoan (2021-02-23 23:36 UTC)

<p>Give them some more time.</p>

---
