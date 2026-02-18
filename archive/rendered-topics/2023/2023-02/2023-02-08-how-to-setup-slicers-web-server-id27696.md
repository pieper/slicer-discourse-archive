# How to setup slicer's web server?

**Topic ID**: 27696
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/how-to-setup-slicers-web-server/27696

---

## Post #1 by @dsa934 (2023-02-08 05:34 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>HI , slicer users</p>
<p>I need to create a communication module that works on slicer. I have never done network coding before.</p>
<p>So I’m trying to do a toy project that turns on the slicer web server and sends and receives data, but there is no way to turn on the slicer server even if I refer to the documentation. What should I do?</p>

---

## Post #2 by @lassoan (2023-02-08 13:26 UTC)

<p>I would recommend to have a look at <a href="https://pypi.org/project/slicerio/">slicerio</a> Python package. It can start Slicer with the web server interface enabled and send commands from Python. You can use slicerio as is, or copy-paste useful code snippets from its <a href="https://github.com/lassoan/slicerio/blob/main/slicerio/server.py">source code</a> into your project.</p>

---

## Post #3 by @dsa934 (2023-02-09 02:41 UTC)

<p>Hi, <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8044462bc6c60b7b111a6870e9d04655bf18780.png" alt="image" data-base62-sha1="uOYh6zIapj8TwBd8YFILJJwd3nG" width="245" height="89"></p>
<p>I am using slicer in window environment, is it correct to install slicerio package in python console in slicer ?</p>
<p>Or do I need to set up and connect to a slicer-only virtual environment in Anaconda?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f186dd5884b0e12c6a201b7bb530e3283489745a.png" alt="image" data-base62-sha1="ysE11v49kV4dRniP86QJiNQWNCi" width="656" height="153"></p>
<p>edit :</p>
<p>Is the slicerio library a function related to communication within 3d slicer in an external python module, not utilized in the slicer’s python console?</p>

---

## Post #4 by @dsa934 (2023-02-09 03:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaac27d0efc8c6e49c95c709155704114b016795.png" data-download-href="/uploads/short-url/xu0zjAfZHx5sKG6krkZgXdv69HD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaac27d0efc8c6e49c95c709155704114b016795.png" alt="image" data-base62-sha1="xu0zjAfZHx5sKG6krkZgXdv69HD" width="690" height="79" data-dominant-color="F7F8F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×108 4.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is it correct to use the location where the Python executable file is installed in the form of server (location)?</p>

---

## Post #5 by @lassoan (2023-02-09 04:19 UTC)

<p>If you run Python script in Slicer’s Python environment you don’t need <em>slicerio</em>. The <em>slicerio</em> Python package is useful if you want to use Slicer features (e.g., use Slicer as an viewer or editor for images or segmentations) in Python scripts running in any environment.</p>
<p>Set slicer_exexutable to the full path of Slicer.exe (you can get the folder from the menu: Help /Report a bug)</p>

---

## Post #6 by @dsa934 (2023-02-09 05:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Sorry for frequently asking questions.<br>
Can I send and receive files from the slicer’s python console to a private(personal) server other than the 3d slicer’s server?</p>
<p>files : Result of working with slicer</p>

---
