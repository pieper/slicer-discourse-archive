# The program '[12808] SlicerApp-real.exe' has exited with code -1073741515 (0xc0000135) 'A dependent dll was not found'.

**Topic ID**: 2537
**Date**: 2018-04-09
**URL**: https://discourse.slicer.org/t/the-program-12808-slicerapp-real-exe-has-exited-with-code-1073741515-0xc0000135-a-dependent-dll-was-not-found/2537

---

## Post #1 by @1115 (2018-04-09 06:53 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.9<br>
Expected behavior:debug<br>
Actual behavior:</p>
<p>I compiled and run Slicer, but after restarting the computer, I get the following error:<br>
System lost CTKWidgets.dll ,QtCored4.dll, QtGuid4.dll…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6412708dd05993250a49e172c53d7b4c663f5f4.png" data-download-href="/uploads/short-url/wQVpdwTTzc6Ze5NI9Zfl3eQn3N2.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180409144816" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6412708dd05993250a49e172c53d7b4c663f5f4_2_690x376.png" alt="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180409144816" data-base62-sha1="wQVpdwTTzc6Ze5NI9Zfl3eQn3N2" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6412708dd05993250a49e172c53d7b4c663f5f4_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6412708dd05993250a49e172c53d7b4c663f5f4_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6412708dd05993250a49e172c53d7b4c663f5f4_2_1380x752.png 2x" data-dominant-color="343233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180409144816</span><span class="informations">1920×1048 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @timeanddoctor (2018-04-11 13:34 UTC)

<p>The anti-virus software killed and deleted essensial files. I think you can donwload the latest version of 3d slicer and then re-install after closing this safe-manager such as 360/qq in Chinese.</p>

---

## Post #3 by @ihnorton (2018-04-11 14:53 UTC)

<p>In order to launch Slicer in Visual Studio, the environment (PATH) needs to be set up correctly. Please see:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio</a></p>

---
