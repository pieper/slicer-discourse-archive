# Breach warning, Open Sound Control, test with Pure Data errors

**Topic ID**: 5045
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/breach-warning-open-sound-control-test-with-pure-data-errors/5045

---

## Post #1 by @jadam1995 (2018-12-11 16:53 UTC)

<p>Operating system: Windows (6.1.7601)<br>
Slicer version: 4.10.0</p>
<p>I am trying to run the Breach Warning and Sound Navigation modules in 3d Slicer. I have followed all of the appropriate steps to install the IGT, Sound Control modules etc. and am trying to load the OscSimpleTest.pd file in the Open Sound Control module as specified in your instructions: <a href="https://github.com/SlicerIGT/SlicerSoundControl" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerSoundControl: 3D Slicer extension to generate sound for feedback during navigation</a></p>
<p>When I load this file and try to start the server, I get the follow error log:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0012fc453c7d1ae8ce1825947add950e2a60ba.png" data-download-href="/uploads/short-url/vFU9KMjkc8yJhjihEUf2QQxcMnU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de0012fc453c7d1ae8ce1825947add950e2a60ba.png" alt="image" data-base62-sha1="vFU9KMjkc8yJhjihEUf2QQxcMnU" width="690" height="126" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">864×159 6.31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can get the Pure data file to open in the purr-data application and I can manipulate the volume and orientation.translations to get varying sounds, however, this error still persists when I try to load the .pd file and start the Open Sound Control server.</p>
<p>Any recommendations on dealing with this error would be greatly appreciated.</p>

---

## Post #2 by @lRaulMN7 (2019-06-23 13:55 UTC)

<p>I got that error when I forgot to set the pd.exe executable in the advanced label. My Open Sound Control looks like this: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c7d89795a3b8056d83772fa364f18fd864d889.png" data-download-href="/uploads/short-url/hnjWpAfv9pYleBegtaZ440FYqCZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c7d89795a3b8056d83772fa364f18fd864d889.png" alt="image" data-base62-sha1="hnjWpAfv9pYleBegtaZ440FYqCZ" width="690" height="333" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">847×409 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
