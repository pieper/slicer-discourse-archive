# Slicer build up fail

**Topic ID**: 44256
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/slicer-build-up-fail/44256

---

## Post #1 by @akuan1997 (2025-08-29 14:39 UTC)

<p>I was trying to build up Slicer by using source code from github.</p>
<p>I followed the instructions from here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a></p>
<p>I also checked with the Install Prerequisites</p>
<p>Cmake: cmake version 3.28.6</p>
<p>Git: git version 2.50.1.windows.1</p>
<p>Qt5: 5.12.2</p>
<p>Visual Studio: Desktop development with C++ (checked), MSVC v143 - VS 2022 C++ x64/x86 build tools (checked), Windows 11 SDK (checked)</p>
<p>–</p>
<p>I created two folders, D:\D\S and D:\D\SR</p>
<p>I am using D:\D\SR as &lt;Slicer_BUILD&gt;</p>
<p>–</p>
<p>I use CMake (cmake-gui) to configure and build Slicer. I follow every step from the website.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e4500b321c4182b7a43db4f8f771fa0d0644f8.png" data-download-href="/uploads/short-url/9GB9bx0hpDnwylsZfwc1BL8sL32.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43e4500b321c4182b7a43db4f8f771fa0d0644f8.png" alt="image" data-base62-sha1="9GB9bx0hpDnwylsZfwc1BL8sL32" width="375" height="500" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">584×777 38.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>–</p>
<p>I opened Visual Studio, switched to Release mode, right-clicked on <strong>ALL_BUILD</strong>, and selected <strong>Build</strong>. After several hours, the build failed. And the error messages are shown below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8cc58ce816aacc9314341012f94f9a058589c67.png" data-download-href="/uploads/short-url/zuYdSCH5lWFVVDbKMQIAr1xzpqv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8cc58ce816aacc9314341012f94f9a058589c67.png" alt="image" data-base62-sha1="zuYdSCH5lWFVVDbKMQIAr1xzpqv" width="690" height="69" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1531×154 8.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>–</p>
<p>I navigate to D:\D\SR\python-install\bin and type the command</p>
<pre><code class="lang-auto"> ./python.exe -m pip install --upgrade setuptools wheel
</code></pre>
<pre><code class="lang-auto">Muen@MUEN MINGW64 /d/D/SR/python-install/bin
$ ./python.exe -m pip show setuptools
Name: setuptools
Version: 80.9.0
Summary: Easily download, build, install, upgrade, and uninstall Python packages
Home-page:
Author:
Author-email: Python Packaging Authority &lt;distutils-sig@python.org&gt;
License-Expression: MIT
Location: D:\D\SR\python-install\Lib\site-packages
Requires:
Required-by:
</code></pre>
<p>I’ve checked the setuptools version is above 42 (mine is 80.9.0). I went back to Visual Studio and right clicked “SimpleSTK” and selected “Build” again.</p>
<p>But the errors remain.</p>
<p>Could someone please give me some suggestions? Thanks</p>

---

## Post #2 by @lassoan (2025-08-29 14:52 UTC)

<p>Slicer does not require or use any existing Python installations. If you installed any Python distributions from <a href="http://python.org">python.org</a> it should not cause any problems. However, Anaconda Python distributions tend to be really invasive, arbitrarily changing system-level Python settings, which can cause problems in all other Python installations, including Slicer’s.</p>
<p>You can look into the logs to see any Python installation mentioned in the logs (in <code>D:\D\SR\Testing\Temporary</code> folder) that is outside the Slicer build tree then delete (or temporarily rename its parent folder so it is not found) and restart the build. Maybe you need to restart the build from scratch.</p>

---

## Post #3 by @akuan1997 (2025-08-29 15:16 UTC)

<p>Hi Mr. Lasso, thank you for your reply. I’ve checked the folder</p>
<pre><code class="lang-auto">D:\D\SR\Testing\Temporary
</code></pre>
<p>Unfortunately, there is no file in this folder.</p>
<p>Some articles also mentioned Python might be a big problem while compiling. As a result, I’ve removed Python path from my environmental variables. Currently I am rebuilding Slicer with Slicer_USE_PYTHONQT_WITH_OPENSSL checked and unchecked (from CMake). Hope this time I can build up Slicer successfully.</p>

---

## Post #4 by @akuan1997 (2025-08-29 23:47 UTC)

<p>Like I mentioned above, I restarted the build from scratch. Unfortunately, I still got the errors.</p>
<p>The errors with Slicer_USE_PYTHONQT_WITH_OPENSSL checked, and no python path in environmental variables</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9e5b777dd9e518f75ff90f73f36e754f7231e6.jpeg" data-download-href="/uploads/short-url/4e17MIouWBJajO7vpRqM0xGxclE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9e5b777dd9e518f75ff90f73f36e754f7231e6_2_690x84.jpeg" alt="image" data-base62-sha1="4e17MIouWBJajO7vpRqM0xGxclE" width="690" height="84" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9e5b777dd9e518f75ff90f73f36e754f7231e6_2_690x84.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9e5b777dd9e518f75ff90f73f36e754f7231e6_2_1035x126.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9e5b777dd9e518f75ff90f73f36e754f7231e6.jpeg 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1320×161 73.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The errors with Slicer_USE_PYTHONQT_WITH_OPENSSL unchecked, and no python path in environmental variables</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef2257b861c13a1661c202239579c159fa052cb.jpeg" data-download-href="/uploads/short-url/8YQoLzgQWrDdyNVTvyqzpEH7p91.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef2257b861c13a1661c202239579c159fa052cb_2_690x167.jpeg" alt="image" data-base62-sha1="8YQoLzgQWrDdyNVTvyqzpEH7p91" width="690" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef2257b861c13a1661c202239579c159fa052cb_2_690x167.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ef2257b861c13a1661c202239579c159fa052cb_2_1035x250.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ef2257b861c13a1661c202239579c159fa052cb.jpeg 2x" data-dominant-color="353434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×330 76.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5bac52b2c2a721117cf23f7ab9c60f964103928.png" data-download-href="/uploads/short-url/sdcdkkc9DBiZ1LBIl7SNle3yaso.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5bac52b2c2a721117cf23f7ab9c60f964103928.png" alt="image" data-base62-sha1="sdcdkkc9DBiZ1LBIl7SNle3yaso" width="514" height="107"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">514×107 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seems Slicer_USE_PYTHONQT_WITH_OPENSSL must be checked during build up.</p>
<p>My Python was downloaded from <a href="http://python.org" rel="noopener nofollow ugc">python.org</a>, not from Anaconda. I have Anaconda in my PC, but the path is not in the environmental variables.</p>
<p>After the build, I still cannot see any log from <code>D:\D\SR\Testing\Temporary</code>.</p>
<p>In the Visual Studio console, I saw the log shows</p>
<p><code>5&gt;-- Using src=‘``https://www.python.org/ftp/python/3.12.10/Python-3.12.10.tgz’</code></p>
<p>I think during the build, Slicer is using its own Python. But I still don’t know how to solve this problem.</p>
<p>Any suggestion would be appreciated, thanks!</p>

---

## Post #5 by @lassoan (2025-09-12 00:26 UTC)

<aside class="quote no-group" data-username="akuan1997" data-post="4" data-topic="44256">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/akuan1997/48/80917_2.png" class="avatar"> akuan1997:</div>
<blockquote>
<p>My Python was downloaded from <a href="http://python.org">python.org</a>, not from Anaconda</p>
</blockquote>
</aside>
<p>If you download any Python and somehow the build process finds it then it might break the build. Do not install Python manually, but let Slicer build Python.</p>
<p>If you share the build log (either displayed in the console or in the <code>Testing</code> or <code>Slicer-build\Testing</code> folder) then we may give advice on how to fix it.</p>

---
