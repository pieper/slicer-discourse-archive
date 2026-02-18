# Older versions of 3D Slicer

**Topic ID**: 23378
**Date**: 2022-05-11
**URL**: https://discourse.slicer.org/t/older-versions-of-3d-slicer/23378

---

## Post #1 by @naninano1 (2022-05-11 22:57 UTC)

<p>Hi,</p>
<p>Since my laptop does not support the Open GL, I receive this error:<br>
See more information and help at:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Slicer_does_not_start" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Slicer_does_not_start</a><br>
Graphics capabilities of this computer:<br>
Renderer does not support required OpenGL capabilities.</p>
<p>I am using Ver 4.11.<br>
To override this error I thought I may use older versions like v4.5. But I couldn’t find the older versions for download.</p>
<p>I was wondering how it is possible to download older windows versions?</p>

---

## Post #2 by @pieper (2022-05-11 23:44 UTC)

<p>Hi -</p>
<p>There’s a link on the download page:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6add1880f2adeba206463f8ee1741b086be94f9.png" alt="image" data-base62-sha1="zcdRrXhzamYGp2e1BufobnrfWB3" width="430" height="248"></p>
<p>From there you can get to this page:</p>
<p><a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482" class="onebox" target="_blank" rel="noopener">https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482</a></p>

---

## Post #3 by @lassoan (2022-05-12 02:16 UTC)

<p>You can also switch to a software renderer by downloading and copying a few files into your Slicer folder as described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#troubleshooting" class="inline-onebox">Get Help — 3D Slicer documentation</a></p>
<p>Software renderers are slower, but the performance degradation is only significant if you use volume rendering or display a complex model.</p>

---

## Post #4 by @naninano1 (2022-05-12 05:10 UTC)

<p>Thank you for your help.<br>
I did all of the procedures step by step. However, I couldn’t run the app.</p>

---

## Post #5 by @naninano1 (2022-05-12 05:13 UTC)

<p>I also downloaded the latest version, 4.8.1 . I could run the app successfully. However, the extensions can’t be downloaded. It seems the extension link is outdated:<br>
<a href="http://slicer.kitware.com/midas3/slicerappstore" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/slicerappstore</a></p>

---

## Post #6 by @pieper (2022-05-12 14:06 UTC)

<p>I’m not sure what hardware you are using, but there’s a good chance that installing linux (e.g. ubuntu) on your hardware will enable a newer version of Slicer.  If you are able to consider new hardware, Chromebooks can be a very cost-effective option and many run Slicer well.</p>

---

## Post #7 by @lassoan (2022-05-14 23:29 UTC)

<p>There are also cloud services that allow you to run Slicer for free, such as <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">Binder</a>.</p>
<p>You can also rent quite capable computers from Microsoft, Amazon, or Google for a few ten cents per hour that you can access via your web browser.</p>

---
