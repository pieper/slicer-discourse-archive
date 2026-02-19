---
topic_id: 9155
title: "4Dv File Error Message"
date: 2019-11-15
url: https://discourse.slicer.org/t/9155
---

# 4dv file, error message

**Topic ID**: 9155
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/4dv-file-error-message/9155

---

## Post #1 by @floppy (2019-11-15 13:59 UTC)

<p>hello, i’m really a newbie. i installed slicer and just wanted to open a .4dv file which my doctor gave me.<br>
i get this error massage, any suggestions what i can do?<br>
“bool __cdecl qSlicerScalarOverlayReader::load(const class QMap&lt;class QString,class QVariant&gt; &amp;)  failed: missing fileName or modelNodeId property”<br>
kind regards,<br>
floppy <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2019-11-15 14:04 UTC)

<p>Not all GE 3D ultrasound files can be loaded, but try these instructions and let us know if it works: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#loading-ge-kretz-ultrasound-images">https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#loading-ge-kretz-ultrasound-images</a></p>

---

## Post #3 by @floppy (2019-11-15 14:57 UTC)

<p>Hello Andras Lasso, it says:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62e0f095af85d19f2c8e1a3cb951c85511a5289d.png" data-download-href="/uploads/short-url/e6IIQCZVKUyah3osCMOJihH4gwJ.png?dl=1" title="Anmerkung%202019-11-15%20155038" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62e0f095af85d19f2c8e1a3cb951c85511a5289d_2_640x500.png" alt="Anmerkung%202019-11-15%20155038" data-base62-sha1="e6IIQCZVKUyah3osCMOJihH4gwJ" width="640" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62e0f095af85d19f2c8e1a3cb951c85511a5289d_2_640x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62e0f095af85d19f2c8e1a3cb951c85511a5289d_2_960x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62e0f095af85d19f2c8e1a3cb951c85511a5289d_2_1280x1000.png 2x" data-dominant-color="FBFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Anmerkung%202019-11-15%20155038</span><span class="informations">1522×1189 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any ideas?<br>
Thanks for helping</p>

---

## Post #4 by @RISH (2019-11-15 16:50 UTC)

<p>hi,<br>
Mr. Lasson, I sent you a message with a link, with those 4dv files, I could check them, I can’t open them either.</p>

---

## Post #5 by @lassoan (2019-11-18 21:11 UTC)

<p>The files you have were DICOM files that contained screenshots of 3D volumes (just color pictures, the same as the .jpg files that were in the folder, too) and a short time sequence of a static slice. They do not contain any 3D volumes.</p>

---

## Post #6 by @floppy (2019-11-19 00:04 UTC)

<p>hello, can you tell us, how you opened the file and got the screenshots so i can extract them as well. thank you</p>

---

## Post #7 by @floppy (2019-11-19 00:36 UTC)

<p>“EXTRACT” was the right word!<br>
Just thought, it can’t be that easy and renamed the .3DV file into .ZIP file <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"><br>
Now I could extract the folder and had all the .DCM and .VOL files.<br>
The .DCM files I could open and save as .JPG with Photohop.</p>
<p>If somone has the same problem, here you go!</p>

---

## Post #8 by @lassoan (2019-11-19 17:19 UTC)

<p>I’ve checked that the .dcm files do not contain more information than the .jpg files by using the new <a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">RawImageGuess</a> extension.</p>
<p>You may be able to load the .vol files using <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/README.md#loading-ge-kretz-ultrasound-images">SlicerHeart extension</a>.</p>

---

## Post #9 by @floppy (2019-11-19 19:32 UTC)

<p>My .dcm files had larger .jpgs because the others in the folder were just thumbnails…<br>
To open and check the .vol files as well was a good hint. Beautiful!<br>
Thanks</p>

---
