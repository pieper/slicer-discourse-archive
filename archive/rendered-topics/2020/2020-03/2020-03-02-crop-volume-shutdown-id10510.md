# Crop Volume Shutdown

**Topic ID**: 10510
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/crop-volume-shutdown/10510

---

## Post #1 by @manjula (2020-03-02 22:51 UTC)

<p>I am encountering rather strange behavior of 3D Slicer when it comes to cropping the volumes of .nii files.   Most of the files that i am working are 3 GB +.  I have recorded a clip of this rather strange behaviour.</p>
<ol>
<li>Load the volume</li>
<li>Select ROI and save the scene</li>
<li>cropping volume ( interpolator linear or windowed sinc behave the same way)</li>
<li>3D slicer shutdown in the middle but in the temporary folder can see the cropped volume (nrrd) file saved. (But 3D Slicer must be working in the background as the file is written after it is shutdown)</li>
<li>restart it and load the scene and do the same thing it works fine.</li>
</ol>
<p>I was thinking this was happening due to running out of memory in my machine but is this something else ?</p>
<div class="lazyYT" data-youtube-id="lQc9oFk71pg" data-youtube-title="out 4" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #2 by @lassoan (2020-03-03 01:24 UTC)

<p>You need much more memory to keep the original volume in the scene and load the cropped volume as well, than just load the cropped volume in an empty scene. However, there should be no problem if you have enough virtual memory/swap space (10x more than the size of the data set - about 30GB).</p>

---

## Post #3 by @manjula (2020-03-03 07:28 UTC)

<p>Thank you for the explanation but how does it do it the second time around always with the same settings ?</p>

---

## Post #4 by @manjula (2020-03-03 17:28 UTC)

<p>I think this is something to do with Linux Mint version i am using rather than swap space. I installed Elementary OS and with default swap of 1 gb this works. So guess it is something more to do with the OS.</p>

---
