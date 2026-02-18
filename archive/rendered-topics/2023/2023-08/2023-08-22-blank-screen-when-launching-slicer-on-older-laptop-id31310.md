# Blank screen when launching Slicer on older laptop

**Topic ID**: 31310
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/blank-screen-when-launching-slicer-on-older-laptop/31310

---

## Post #1 by @Eduardo_Hernandez (2023-08-22 23:46 UTC)

<p>I have downloaded version 5.2.2, 5.5.0 and 5.4.0, it manages to download everything but when I open it I get a window with a white screen. My laptop has these features:<br>
Operating system: windows 10 pro; version : 21H2<br>
Processor : Intel(R) Core™ i3-2365M CPU @ 1.40GHz 1.40 GHz<br>
RAM : 12.00 GB (11.8 GB usable)<br>
Processor graphics : Intel(R) HD Graphics 3000<br>
Shader version : 5.0<br>
OpenGL: 4.3<br>
Open CL : 1.2<br>
Is it because of the characteristics of the machine or why is this due?</p>

---

## Post #2 by @jcfr (2023-08-23 01:52 UTC)

<blockquote>
<p>I get a window with a white screen.</p>
</blockquote>
<p>Assuming you were able to download the package and the white screen appears at startup, consider reviewing these:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-starts-up-with-a-blank-screen-then-slicerapp-real-exe-not-responding-error/21001" class="inline-onebox">Slicer starts up with a blank screen then "Slicerapp-real.exe not responding" error</a></li>
</ul>

---

## Post #3 by @lassoan (2023-08-23 08:28 UTC)

<aside class="quote no-group" data-username="Eduardo_Hernandez" data-post="1" data-topic="31310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eduardo_hernandez/48/17229_2.png" class="avatar"> Eduardo_Hernandez:</div>
<blockquote>
<p>Intel(R) Core™ i3-2365M CPU</p>
</blockquote>
</aside>
<p>This CPU was release more than 10 years ago. Current version of Slicer is compatible with hardware released in the past 5 years. You can try to dig up a very old version of Slicer that is still compatible with your computer, but that would lack many new features and fixes. Therefore, I would strongly recommend to get a more recent computer (or to rent a virtual machine from a cloud provider) that is compatible with current Slicer version.</p>

---

## Post #4 by @Eduardo_Hernandez (2023-08-23 13:07 UTC)

<p>The same thing happens to me with all the versions, I downloaded the Mesa OpenGL driver but it didn’t solve anything or possibly it didn’t work correctly</p>

---

## Post #5 by @Eduardo_Hernandez (2023-08-23 20:23 UTC)

<p>i made these instructions<br>
<strong>Setting up software renderer on Windows:</strong></p>
<ul>
<li>Download Mesa OpenGL driver from <a href="https://github.com/pal1000/mesa-dist-win/releases" class="inline-onebox" rel="noopener nofollow ugc">Releases · pal1000/mesa-dist-win · GitHub</a> (MSVC version - mesa3d-X.Y.Z-release-msvc.7z). Last tested with release <a href="https://github.com/pal1000/mesa-dist-win/releases/tag/22.2.0" class="inline-onebox" rel="noopener nofollow ugc">Release 22.2.0 · pal1000/mesa-dist-win · GitHub</a></li>
<li>Extract the archive and copy files from the x64 folder into the bin subfolder in the Slicer install tree.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6fe412299b7c3b1858d227b6e0df55d03b3272.png" data-download-href="/uploads/short-url/rjwVacjZQ2eROrfeo96m2uUkOt4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6fe412299b7c3b1858d227b6e0df55d03b3272_2_690x387.png" alt="image" data-base62-sha1="rjwVacjZQ2eROrfeo96m2uUkOt4" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6fe412299b7c3b1858d227b6e0df55d03b3272_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6fe412299b7c3b1858d227b6e0df55d03b3272_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6fe412299b7c3b1858d227b6e0df55d03b3272.png 2x" data-dominant-color="F1F5F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 86.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I found it up to here, but everything does not appear</p>

---

## Post #6 by @jcfr (2023-08-23 23:32 UTC)

<p>Thanks for the follow up.</p>
<aside class="quote no-group" data-username="Eduardo_Hernandez" data-post="4" data-topic="31310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eduardo_hernandez/48/17229_2.png" class="avatar"> Eduardo_Hernandez:</div>
<blockquote>
<p>The same thing happens to me with all the versions</p>
</blockquote>
</aside>
<p>Do you also experience the same issue using older Slicer versions ? Starting with <code>4.10.2</code>.</p>
<p>Here are links:</p>
<ul>
<li><a href="https://download.slicer.org/?version=4.10.2">https://download.slicer.org/?version=4.10.2</a></li>
<li><a href="https://download.slicer.org/?version=4.11.20200930">https://download.slicer.org/?version=4.11.20200930</a></li>
<li><a href="https://download.slicer.org/?version=4.11.20210226">https://download.slicer.org/?version=4.11.20210226</a></li>
</ul>

---

## Post #7 by @Eduardo_Hernandez (2023-08-25 11:36 UTC)

<p>install and uninstall the recommended versions, more things appear and do not appear in each installed version</p>

---
