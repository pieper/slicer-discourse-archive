# Release build of Slicer fails with error on sphinx-build

**Topic ID**: 30544
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/release-build-of-slicer-fails-with-error-on-sphinx-build/30544

---

## Post #1 by @drdH (2023-07-12 11:04 UTC)

<p>Hello Team,</p>
<p>Kindly wanted to know how to fix the error based on below message:</p>
<blockquote>
<p>CUSTOMBUILD : warning : sphinx-build not found: Python documentation will not be created</p>
</blockquote>
<p>I am trying to build in release mode.  The issue occurs when ALL_BUILD is performed from visual studio.</p>
<p>Regards,<br>
Darshan</p>

---

## Post #2 by @pieper (2023-07-12 13:53 UTC)

<p>I believe this is just a warning you can ignore.  Or maybe you can just install the package and it will build the documentation.</p>

---

## Post #3 by @drdH (2023-07-13 10:24 UTC)

<p>Hello Steve Sir,</p>
<p>Thank you.  Kindly wanted to know if there is a way to turn off this build in the CMake file or some place so that it does not try and build this ?</p>
<p>Regards,<br>
Darshan</p>

---

## Post #4 by @pieper (2023-07-13 12:45 UTC)

<p>You’d need to look in the source code for a way to turn this off, but you shouldn’t need to.  You should just ignore this if you don’t need to build the documentation.</p>

---

## Post #5 by @drdH (2023-07-13 14:53 UTC)

<p>Hello Steve Sir,</p>
<p>Thank you, but the build does not proceed to create the slicer exe. It simply fails at this step and gives below error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f.png" data-download-href="/uploads/short-url/2igjSYhhHXOil8ACLacCuGY4k4n.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_690x21.png" alt="grafik" data-base62-sha1="2igjSYhhHXOil8ACLacCuGY4k4n" width="690" height="21" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_690x21.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_1035x31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_1380x42.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1840×58 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Darshan</p>

---

## Post #6 by @pieper (2023-07-13 15:13 UTC)

<p>Probably there is something else going wrong with the build.  Look higher up in the logs to see what is going on.  Maybe someone who routinely builds on Windows can offer suggestions.</p>

---
