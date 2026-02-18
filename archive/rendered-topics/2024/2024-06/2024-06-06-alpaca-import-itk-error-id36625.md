# ALPACA "import itk" error

**Topic ID**: 36625
**Date**: 2024-06-06
**URL**: https://discourse.slicer.org/t/alpaca-import-itk-error/36625

---

## Post #1 by @EllaNicklin (2024-06-06 17:12 UTC)

<p>Hello 3D Slicer community,</p>
<p>I have just tried to use ALPACA module for the first time on a new lab laptop (Windows 11) running 3D Slicer 5.7.0 (preview release). Slicer ran into an issue loading in the python script then spat out the following “import itk” error in the python console.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c8e7475c2be29c8f574a02c15d640943164369.png" data-download-href="/uploads/short-url/9f6ZucxV7zYOz0cT0aOxOkaaBFn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c8e7475c2be29c8f574a02c15d640943164369_2_530x499.png" alt="image" data-base62-sha1="9f6ZucxV7zYOz0cT0aOxOkaaBFn" width="530" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c8e7475c2be29c8f574a02c15d640943164369_2_530x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40c8e7475c2be29c8f574a02c15d640943164369_2_795x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40c8e7475c2be29c8f574a02c15d640943164369.png 2x" data-dominant-color="F8F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">924×871 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have since closed and reopened Slicer, but this “issue with the python script”+ error in the console happens every time I go to use ALPACA.</p>
<p>It seems like there is a permission issue but I don’t know why. Please could I get some help on this subject/guidance on how I might be able to resolve this issue!</p>

---

## Post #2 by @muratmaga (2024-06-06 17:41 UTC)

<p>I can replicate a similar issue on latest preview on Mac as well. ALPACA fails with</p>
<p><code>Traceback (most recent call last):   File "/Users/amaga/SlicerMorph/ALPACA/ALPACA.py", line 105, in setup     from itk import Fpfh ImportError: cannot import name 'Fpfh' from 'itk' (/Users/amaga/Desktop/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/itk/__init__.py)</code></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is this related to the recent ITK version change in preview builds?</p>
<p><a class="mention" href="/u/ellanicklin">@EllaNicklin</a> Meanwhile, you can use ALPACA with the latest stable build (5.6.2)</p>

---

## Post #3 by @jamesobutler (2024-06-06 18:01 UTC)

<p><a class="mention" href="/u/ellanicklin">@EllaNicklin</a> appears to be using Slicer Preview version 5.7.0-2024-05-21 which was prior to the ITK 5.4.0 update which was integrated on June 3rd. Ella’s error looks to be from installing Slicer in the Program Files system location instead of the default AppData users location. It is installing the <code>itk</code> python package in the extensions directory located in the install location which in this case is a system location which requires higher permissions to modify. Installing this Slicer version (5.7.0-2024-05-21) in the user space instead of Program Files would likely resolve this issue for the user.</p>

---

## Post #4 by @muratmaga (2024-06-06 18:06 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> nice catch.</p>
<p><a class="mention" href="/u/ellanicklin">@EllaNicklin</a> please reinstall (or move if you have the rights) Slicer to a folder where you can have write permission. This can be something like C:/Users/YOURUSER/AppData or even your desktop, and retry.</p>
<p>But my mac problem with the latest preview seems something to do with the new ITK version.</p>

---
