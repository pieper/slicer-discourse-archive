# Error installing PyRadiomics

**Topic ID**: 35105
**Date**: 2024-03-26
**URL**: https://discourse.slicer.org/t/error-installing-pyradiomics/35105

---

## Post #1 by @UnknownIta (2024-03-26 15:20 UTC)

<p>I’m trying to download Radiomics but I ran into this error. Can anyone explain to me how I can solve this?<br>
Thank you in advance</p>
<p>Install target: install<br>
C:\Users\AppData\Local\Temp\pip-install-2mkjrouf\simpleitk af1blhdc40184a66b1fx672x72ecf1f</p>
<p>Source directory:<br>
C:\Users\AppData\Local\Temp\pip-install-Zakjrouf\simpleitk_af1b@dc4818a4a68b1faa672a72ecf1f_skbuil Please check the install target is valid and see CMake e’s output for more information.</p>
<p>Working directory:<br>
C:\Users\AppData\Local\Temp\pip-install-Zakjrouf\simpleitk_af1b@dc4818a4a68b1faa672a72ecf1f_skbuil</p>
<p>Please check the install target is valid and see CMake e’s output for more information.</p>
<p>[end of output]</p>
<p>Note: this error originates from a subprocess, and is likely not a problem with pip.</p>
<p>ERROR: Failed building wheel for SimpleITK<br>
Failed to build SimpleITK<br>
ERROR: Could not build wheels for SimpleITK, which is required to install pyproject.toml-based projects</p>

---

## Post #2 by @rbumm (2024-03-26 18:08 UTC)

<p>I can not explain your error messages, however you could just install the SlicerRadiomics extension and run it on your segmentations:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff2da373690d75bd8dfc909d950ec1ac194c5995.png" data-download-href="/uploads/short-url/Appxan6sCAIAF2FgFwkkkJNYjUF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2da373690d75bd8dfc909d950ec1ac194c5995_2_690x254.png" alt="image" data-base62-sha1="Appxan6sCAIAF2FgFwkkkJNYjUF" width="690" height="254" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2da373690d75bd8dfc909d950ec1ac194c5995_2_690x254.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2da373690d75bd8dfc909d950ec1ac194c5995_2_1035x381.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2da373690d75bd8dfc909d950ec1ac194c5995_2_1380x508.png 2x" data-dominant-color="ABA9A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×705 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @UnknownIta (2024-03-27 14:09 UTC)

<p>so are you advising me to install 3D slicer first and then pyradiomics?  But won’t it give me the same problem? I downloaded visual 2022, is it correct or superfluous?</p>

---

## Post #4 by @UnknownIta (2024-03-27 17:12 UTC)

<p>I downloaded 3D Slicer and I downloaded the Pyradiomics extension.<br>
But I’d still like to understand why he didn’t let me download it via pip. Also why shouldn’t the wheels be installed automatically by python?</p>

---
