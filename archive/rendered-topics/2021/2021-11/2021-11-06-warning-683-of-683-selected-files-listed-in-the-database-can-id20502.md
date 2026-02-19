---
topic_id: 20502
title: "Warning 683 Of 683 Selected Files Listed In The Database Can"
date: 2021-11-06
url: https://discourse.slicer.org/t/20502
---

# Warning: 683 of 683 selected files listed in the database cannot be found on disk. see python console for error message Is there anything I can do?

**Topic ID**: 20502
**Date**: 2021-11-06
**URL**: https://discourse.slicer.org/t/warning-683-of-683-selected-files-listed-in-the-database-cannot-be-found-on-disk-see-python-console-for-error-message-is-there-anything-i-can-do/20502

---

## Post #1 by @CP_HO (2021-11-06 04:49 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11202<br>
Expected behavior: views in 3 dimension<br>
Actual behavior: only one window</p>
<p>I had been using 3D slicer for some time with no problem.</p>
<p>Recently I ran into some problem.  After I have uploaded the files from disk and then loaded them under 3D slicer, I could not get the 3 D image.  Below is the screen shot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/308d23283e03f45796db0339a992a93d125bed4b.png" data-download-href="/uploads/short-url/6VviQheNBF6HPuqDJDir1qRIUZR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/308d23283e03f45796db0339a992a93d125bed4b_2_690x379.png" alt="image" data-base62-sha1="6VviQheNBF6HPuqDJDir1qRIUZR" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/308d23283e03f45796db0339a992a93d125bed4b_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/308d23283e03f45796db0339a992a93d125bed4b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/308d23283e03f45796db0339a992a93d125bed4b.png 2x" data-dominant-color="97969B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">711×391 73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried that on another computer with another patient and the result was the same. There was an error message</p>
<p>warning:  683 of 683 selected files listed in the database cannot be found on disk. see python console for error message</p>
<p>Is there anything I can do?<br>
cp</p>

---

## Post #2 by @pieper (2021-11-06 13:03 UTC)

<p>First I guess, where you able to look in the python console and were there any messages?</p>
<p>The message means that when you imported the data into the dicom database the files were readable on disk.  But then when you went to load them they were not available.  Maybe they were on a removable disk or got deleted from the system somehow.  Sometimes network or cloud disks can cause trouble.</p>

---
