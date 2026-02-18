# Compile the latest fails

**Topic ID**: 23829
**Date**: 2022-06-11
**URL**: https://discourse.slicer.org/t/compile-the-latest-fails/23829

---

## Post #1 by @SteveLiu (2022-06-11 12:30 UTC)

<p>Operating system: windows10<br>
Slicer version: latest version (5.0)<br>
Expected behavior: compile the “buildall” project<br>
Actual behavior:*<br>
all the configuration according to " <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>"<br>
git version 2.36.0., cmake version 3.23.1, VS2022 V143</p>
<p><strong>when compile with ““C:\Program Files\CMake\bin\cmake.exe” --build . --config Debug”</strong> it had the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd5c201c31ef805cb8524bb4f670b7abb7365b79.png" data-download-href="/uploads/short-url/A9kb1E3nECu9jDQF4Gu5nr43Njj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd5c201c31ef805cb8524bb4f670b7abb7365b79.png" alt="image" data-base62-sha1="A9kb1E3nECu9jDQF4Gu5nr43Njj" width="690" height="343" data-dominant-color="080908"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1442×718 46.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
*<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c73fcdbbb3338a470cfde6968ce94bd906a2859.png" data-download-href="/uploads/short-url/ftq4iEE3oZYpvRNKgwdKquGF9gZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c73fcdbbb3338a470cfde6968ce94bd906a2859.png" alt="image" data-base62-sha1="ftq4iEE3oZYpvRNKgwdKquGF9gZ" width="690" height="345" data-dominant-color="110505"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×720 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-06-12 01:22 UTC)

<p>It seems that your computer had problems accessing github. Check your network (firewall, proxy, vpn, …) settings and try again. We build Slicer on Windows, Linux, and macOS and <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">there have been no build errors recently</a>.</p>

---

## Post #3 by @SteveLiu (2022-06-12 04:55 UTC)

<p>thanks Lassoan.<br>
I shut the proxy and the auto-detect opened<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802e36e984cd6ee53b3ff45f829d21d86f6410f8.png" data-download-href="/uploads/short-url/ihW84YXjSN1VMXsuqd966kV9yBO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/802e36e984cd6ee53b3ff45f829d21d86f6410f8_2_678x500.png" alt="image" data-base62-sha1="ihW84YXjSN1VMXsuqd966kV9yBO" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/802e36e984cd6ee53b3ff45f829d21d86f6410f8_2_678x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/802e36e984cd6ee53b3ff45f829d21d86f6410f8_2_1017x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/802e36e984cd6ee53b3ff45f829d21d86f6410f8_2_1356x1000.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2080×1532 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>btw, I tried the git by cmd git clone <a href="https://github.com/commontk/DCMTK.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - commontk/DCMTK: WARNING: This is NOT the official upstream DCMTK git repository.</a> it works well but by ““C:\Program Files\CMake\bin\cmake.exe” --build . --config Debug” fail<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce91cd3ceb506bad377d57db2301fc7840e3ad8e.png" data-download-href="/uploads/short-url/ttoJJtBukAUVK2icq78UaeVOePY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce91cd3ceb506bad377d57db2301fc7840e3ad8e_2_690x345.png" alt="image" data-base62-sha1="ttoJJtBukAUVK2icq78UaeVOePY" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce91cd3ceb506bad377d57db2301fc7840e3ad8e_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce91cd3ceb506bad377d57db2301fc7840e3ad8e_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce91cd3ceb506bad377d57db2301fc7840e3ad8e_2_1380x690.png 2x" data-dominant-color="0A0909"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×720 49.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @SteveLiu (2022-06-12 07:02 UTC)

<p>I modified git protocol:<br>
git config –global url.”https://”.insteadOf git://<br>
and<br>
OpenSSL connecting proxy setting:<br>
git config --global http.proxy 127.0.0.1:1234<br>
git config --global https.proxy 127.0.0.1:1234<br>
they seem to be the solution of connection with github repository.</p>
<p>but i still have the “Project Completion Failure” in VS2022<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49a26d610fef8c1eb3f1c56940597a0bdb1d509.png" data-download-href="/uploads/short-url/s3dQROLKzU8ktvYVd5mjeW679oJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49a26d610fef8c1eb3f1c56940597a0bdb1d509.png" alt="image" data-base62-sha1="s3dQROLKzU8ktvYVd5mjeW679oJ" width="690" height="255" data-dominant-color="DEE0E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1680×621 33.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
it seems no solution/download link for this project</p>

---

## Post #5 by @lassoan (2022-06-12 12:38 UTC)

<p>Are you connecting to the internet via a proxy server?</p>
<p>You then need to specify it for every Neutrogena access operations. It seems that you figured it out how to do it for git. You also need to specify the proxy server for Python"s pip. Setting the -<code>HTTP_PROXY=&lt;proxyserver_name&gt;:&lt;port#&gt;</code> environment variable may be sufficient.</p>

---

## Post #6 by @SteveLiu (2022-06-13 06:09 UTC)

<p>Thanks, I am trying to do with your instruction as below hope it is right…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f817bdf7308a42689b439c272dadaf3e7fc2307f.png" alt="image" data-base62-sha1="zoJhluHWjGFsEYdF7W9WvsBDjk3" width="655" height="305"></p>
<p>but still the python has project failed in building （but i find the executable(.exe) application of Slicer in the folder）. So I am thinking do the python- affixed projects need to be built? As I saw when building :  <code>No download step for 'python-wheel' No update step for 'python-wheel' </code></p>
<pre data-code-wrap="------"><code class="lang-------">Creating directories for 'python-setuptools'
Building Custom Rule C:/D/S/CMakeLists.txt
No download step for 'python-setuptools'
No update step for 'python-setuptools'
Generate version-python-setuptools.txt and license-python-setuptools.txt
fatal: not a git repository (or any of the parent directories): .git
CMake Warning (dev) at C:/D/D4R/CMakeFiles/python-setuptools-generate-project-description.cmake:69 (message):
  python-setuptools: Could not find a license file
This warning is for project developers.  Use -Wno-dev to suppress it.

No patch step for 'python-setuptools'
No configure step for 'python-setuptools'
No build step for 'python-setuptools'
Performing install step for 'python-setuptools'
CMake Error at C:/D/D4R/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-Release.cmake:49 (message):
  Command failed: 1

   'C:/D/D4R/python-install/bin/PythonSlicer.exe' '-m' 'pip' 'install' '--require-hashes' '-r' 'C:/D/D4R/python-setuptools-requirements.txt'

  See also

    C:/D/D4R/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-*.log


C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(245,5): error MSB8066: Custom build for 'C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-mkdir.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-download.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-update.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-patch.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-configure.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-build.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-generate_project_description.rule;C:\D\D4R\CMakeFiles\48d8ac0d9c1890032347ba8b3181d423\python-setuptools-install.rule;C:\D\D4R\CMakeFiles\ee0ff0a71f8955ced5249e2ec794c4aa\python-setuptools-complete.rule;C:\D\D4R\CMakeFiles\a478b26e6350678435a4bc11611aaba7\python-setuptools.rule;C:\D\S\CMakeLists.txt' exited with code 1.
Done building project "python-setuptools.vcxproj" -- FAILED.```</code></pre>

---

## Post #7 by @lassoan (2022-06-13 12:45 UTC)

<p>Python’s package manager and pip tool is not related to CMake. You need to set HTTP_PROXY/HTTPS_PROXY as environment variable in your operating system.</p>

---

## Post #8 by @SteveLiu (2022-06-14 01:30 UTC)

<p>Thanks Lassoan,<br>
There is still a little error (MSB8066) about <code>python-setuptools</code> project;<br>
Locate in the file: <code> &lt;CustomBuild Condition ="'@(_CustomBuild)' != ''"</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d833929f858f4817519d736570c3fa70085f7b20.png" data-download-href="/uploads/short-url/uQBCUWxsifPCsCVnZGTAEco3ct2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d833929f858f4817519d736570c3fa70085f7b20_2_585x500.png" alt="image" data-base62-sha1="uQBCUWxsifPCsCVnZGTAEco3ct2" width="585" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d833929f858f4817519d736570c3fa70085f7b20_2_585x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d833929f858f4817519d736570c3fa70085f7b20_2_877x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d833929f858f4817519d736570c3fa70085f7b20.png 2x" data-dominant-color="29292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">956×817 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @SteveLiu (2022-06-14 10:45 UTC)

<p>I tried to build specific error project, this is the error with <code>python</code>project<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09948d1d159e3fc4122bf0734c003d7e12feea89.png" data-download-href="/uploads/short-url/1mKz8EaGCnM0W1k26No6KbN0ooF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09948d1d159e3fc4122bf0734c003d7e12feea89_2_690x226.png" alt="image" data-base62-sha1="1mKz8EaGCnM0W1k26No6KbN0ooF" width="690" height="226" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09948d1d159e3fc4122bf0734c003d7e12feea89_2_690x226.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09948d1d159e3fc4122bf0734c003d7e12feea89_2_1035x339.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09948d1d159e3fc4122bf0734c003d7e12feea89_2_1380x452.png 2x" data-dominant-color="E6E7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1690×555 38.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I locate to the folder <code>C:\D\S4R\CMakeFiles\b971bae278932486b6f223c6e29c96a3</code><br>
and I find the XXX.rule file writes <code># generated from CMake</code> but nothing.</p>

---

## Post #10 by @mau_igna_06 (2022-06-14 19:35 UTC)

<p>I sometimes solve this errors by rebuilding the whole project again from zero</p>

---

## Post #11 by @lassoan (2022-06-17 19:41 UTC)

<p>Check out the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#errors-related-to-python">“Common errors” section of the build instructions</a> to see how to solve Python related build errors.</p>

---

## Post #12 by @SteveLiu (2022-06-19 09:19 UTC)

<p>Thanks for the replies. I will try.</p>

---
