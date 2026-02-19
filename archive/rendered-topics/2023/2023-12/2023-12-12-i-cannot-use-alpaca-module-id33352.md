---
topic_id: 33352
title: "I Cannot Use Alpaca Module"
date: 2023-12-12
url: https://discourse.slicer.org/t/33352
---

# I cannot use ALPACA module

**Topic ID**: 33352
**Date**: 2023-12-12
**URL**: https://discourse.slicer.org/t/i-cannot-use-alpaca-module/33352

---

## Post #1 by @YOU_DDS (2023-12-12 09:58 UTC)

<p>Dear Professors, friends and all members here,</p>
<p>I need your advice on using ALPACA.</p>
<p>I have installed the SlicerMorph extension. After installation, I am trying to use ALPACA module, but when I click on this module, nothing shown in the working tab(as in the attached photo) and this is what have been show in the Python interactor.<br>
Python 3.9.10 (main, Aug 19 2023, 07:42:26) [MSC v.1935 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
Traceback (most recent call last):<br>
File “C:/Users/youis/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/SlicerMorph/lib/Slicer-5.4/qt-scripted-modules/ALPACA.py”, line 160, in setup<br>
from itk import Fpfh<br>
ImportError: cannot import name ‘Fpfh’ from ‘itk’ (C:\Users\youis\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\itk_<em>init</em>_.py)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d40ba71a414703fd97c525078c21eb12a706633.png" data-download-href="/uploads/short-url/fAuIT6XVYZKz1DGLDuaSNvhZvKb.png?dl=1" title="Screenshot 2023-12-12 185300" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d40ba71a414703fd97c525078c21eb12a706633_2_619x499.png" alt="Screenshot 2023-12-12 185300" data-base62-sha1="fAuIT6XVYZKz1DGLDuaSNvhZvKb" width="619" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d40ba71a414703fd97c525078c21eb12a706633_2_619x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d40ba71a414703fd97c525078c21eb12a706633_2_928x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d40ba71a414703fd97c525078c21eb12a706633.png 2x" data-dominant-color="DBE0E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-12-12 185300</span><span class="informations">1220×985 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-12-12 17:07 UTC)

<p>Please try with the newest stable (v5.6.1) that will be available later today, and then let us know if it doesn’t work.</p>

---
