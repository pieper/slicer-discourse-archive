# Build failure windows

**Topic ID**: 7322
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/build-failure-windows/7322

---

## Post #1 by @gregsharp.geo (2019-06-26 18:36 UTC)

<p>Hi,  I get VTK build failure on VS 2017.</p>
<pre><code>Error	LNK1181	cannot open input file 'C:\S\tbb-install\lib\intel64\tbb.lib' [C:\S\VTK-build\vtkCommon.vcxproj]	VTK	C:\S\LINK	1	
Error	LNK1181	cannot open input file 'C:\S\VTK-build\lib\Release\vtkOpenGL-8.2.lib' [C:\S\SlicerExecutionModel-build\ModuleDescriptionParser\ModuleDescriptionParser.vcxproj]	SlicerExecutionModel	C:\S\LINK	1	
Error	LNK1181	cannot open input file 'C:\S\VTK-build\lib\Release\vtkChartsCore-8.2.lib' [C:\S\CTK-build\CTK-build\Libs\Visualization\VTK\Core\CTKVisualizationVTKCore.vcxproj] [C:\S\CTK-build\CTK.vcxproj]	CTK	C:\S\LINK	1	
</code></pre>
<p>Indeed, the tbb is located in a subfolder:</p>
<pre><code>$ dir
12/06/2017  08:54 AM    &lt;DIR&gt;          vc12
12/06/2017  08:54 AM    &lt;DIR&gt;          vc12_ui
12/06/2017  08:54 AM    &lt;DIR&gt;          vc14
12/06/2017  08:54 AM    &lt;DIR&gt;          vc14_uwp
</code></pre>
<p>Any idea what is going on?</p>

---

## Post #2 by @lassoan (2019-06-27 04:56 UTC)

<p>The compiler is looking for the file in incorrect location. It is at <code>c:\S\tbb-install\lib\intel64\vc14</code>. If you use VS2017 then make sure to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions/Configure#Windows" rel="nofollow noopener">use VS2015 toolset</a>.</p>

---

## Post #3 by @jcfr (2019-06-27 05:16 UTC)

<p>Reading more about Tbb, it seems that we could link the against the same version when using VS2017.<br>
See <a href="https://github.com/intel/tbb/issues/65#issuecomment-403066264" rel="nofollow noopener">https://github.com/intel/tbb/issues/65#issuecomment-403066264</a> and <a href="https://github.com/intel/tbb/blob/2019_U8/doc/Release_Notes.txt" rel="nofollow noopener">https://github.com/intel/tbb/blob/2019_U8/doc/Release_Notes.txt</a></p>

---

## Post #4 by @lassoan (2019-06-27 05:25 UTC)

<p>VS2015 toolset is probably needed anyway: last time I tried a couple of weeks ago ITK or some other libraries failed to build with VS2017 and maybe it is needed for compatibility with Python binaries, too.</p>

---

## Post #5 by @gcsharp (2019-06-27 14:29 UTC)

<p>By copying the files from the vc14 subfolder into C:\S\tbb-install\lib\intel64, the VTK compile could succeed.  But yes, python could be a problem.  I will update status on Friday.</p>

---

## Post #6 by @gcsharp (2019-06-27 14:38 UTC)

<p>Current Qt installer does not provide 5.10.X (it is not shown in either LTS or archive).  Presumably 5.9.8 would therefore be recommended?</p>

---

## Post #7 by @lassoan (2019-06-27 17:55 UTC)

<p>You need to click “Refresh” after enabling “Archive”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09ddca58eecd7aed287f8892e370eef08f07f322.png" data-download-href="/uploads/short-url/1phtP1EDIVfFQq1qSr6YuRdC1LY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ddca58eecd7aed287f8892e370eef08f07f322_2_677x500.png" alt="image" data-base62-sha1="1phtP1EDIVfFQq1qSr6YuRdC1LY" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ddca58eecd7aed287f8892e370eef08f07f322_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ddca58eecd7aed287f8892e370eef08f07f322_2_1015x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09ddca58eecd7aed287f8892e370eef08f07f322_2_1354x1000.png 2x" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1722×1270 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @gcsharp (2019-06-27 18:14 UTC)

<p>That is interesting.  I don’t get the extra one at the bottom.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd317a8f44dde63c006ee4526151db9cc6bb38e6.png" alt="Capture" data-base62-sha1="vyLwMjPANmM5ZSk00lm1ubiNp5k" width="554" height="468"></p>

---

## Post #9 by @cpinter (2019-06-27 18:23 UTC)

<p>Andras may get it because it’s already installed. I added the 5.10.0 download link to the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Common_Prerequisites_2" rel="nofollow noopener">Build instructions page</a>. This is the download <a href="https://download.qt.io/archive/qt/5.10/5.10.0" rel="nofollow noopener">link</a> itself.</p>

---

## Post #10 by @jamesobutler (2019-06-28 10:15 UTC)

<p>I also noticed recently that they removed this archived version of Qt from the maintenance tool as well. Evidently it is intentional <a href="https://bugreports.qt.io/browse/QTBUG-76323" rel="nofollow noopener">https://bugreports.qt.io/browse/QTBUG-76323</a></p>

---

## Post #11 by @gregsharp.geo (2019-06-29 15:37 UTC)

<p>Back to the original topic, the VS2017 build (with VS2017 toolset) seems to work fine.  I only had to copy the tbb.lib (for build) and tbb.dll (for launching).</p>
<p>Everything, including python, seems to work fine.</p>

---

## Post #12 by @lassoan (2019-06-30 00:59 UTC)

<p>Thank you, it’s good to know. Have you tried to install and use Python packages that contain binaries?</p>

---

## Post #13 by @gcsharp (2019-06-30 16:33 UTC)

<p>You mean like pip install?  Or can you give an example?</p>

---

## Post #14 by @jcfr (2019-06-30 17:14 UTC)

<blockquote>
<p>can you give an example?</p>
</blockquote>
<pre><code class="lang-auto">pip install pandas
pip install scipy
</code></pre>
<p>Then you could run the corresponding tests.</p>
<blockquote>
<p>I only had to copy the tbb.lib (for build) and tbb.dll (for launching).</p>
</blockquote>
<p>Makes sense. I will update the build system so that building with VS2017 works as expected.</p>
<blockquote>
<p>Python packages that contain binaries […] VS2017 + toolset v141</p>
</blockquote>
<p>Since v140 and v141 are suppose to be binary compatible, I guess we could update the build instructions.</p>
<p>See <a href="https://stackoverflow.com/a/44314010/1539918" class="inline-onebox">abi - Binary compatibility between VS2017 and VS2015 - Stack Overflow</a> and <a href="https://bugs.python.org/issue31340#msg301253" class="inline-onebox">Issue 31340: Use VS 2017 compiler for build - Python tracker</a></p>

---

## Post #15 by @lassoan (2019-06-30 17:22 UTC)

<p>If we can build Slicer with VS2017 without losing Python binary compatibility then we should switch to VS2017 because then we could upgrade to latest Qt (which contains a couple of useful improvements and fixes).</p>

---

## Post #16 by @jcfr (2019-06-30 18:34 UTC)

<p>This PR should allow to build using VS2017. See <a href="https://github.com/Slicer/Slicer/pull/1163" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1163</a></p>
<p>Could someone test this is effectively the case ?</p>
<p>After confirming it builds, we may also have to revisit which runtime libraries are packages. Indeed, the package will then have dependency on both VS2015 and VS2017 runtime libraries.</p>
<p>See <a href="https://github.com/Slicer/Slicer/blob/7f08682494af41c7941b62cbcd37a91feffe148b/CMake/SlicerCPack.cmake#L158-L159" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/7f08682494af41c7941b62cbcd37a91feffe148b/CMake/SlicerCPack.cmake#L158-L159</a> and <a href="https://cmake.org/cmake/help/latest/module/InstallRequiredSystemLibraries.html" rel="nofollow noopener">InstallRequiredSystemLibraries</a></p>

---

## Post #17 by @jamesobutler (2019-06-30 19:22 UTC)

<p>Could Slicer build with VS2019 as well?</p>
<p>The v142 toolset is binary compatible with v141 and v140. <a href="https://devblogs.microsoft.com/cppblog/cpp-binary-compatibility-and-pain-free-upgrades-to-visual-studio-2019/" rel="nofollow noopener">https://devblogs.microsoft.com/cppblog/cpp-binary-compatibility-and-pain-free-upgrades-to-visual-studio-2019/</a></p>

---

## Post #18 by @gregsharp.geo (2019-06-30 22:22 UTC)

<p>Well, my first test was a bust.  I am not a regular python user, so that is surely why.</p>
<p>I tried “pip install pandas” from the command line:</p>
<pre><code>&gt;&gt;&gt; pip install pandas
  File "&lt;console&gt;", line 1
    pip install pandas
              ^
SyntaxError: invalid syntax
</code></pre>
<p>After some web search, I understood the following is the way to install using pip:</p>
<pre><code>c:\S\python-install\bin&gt;PythonSlicer -m pip install pandas
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting pandas
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/pandas/
  Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/pandas/
  Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/pandas/
  Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/pandas/
  Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/pandas/
  Could not fetch URL https://pypi.org/simple/pandas/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pandas/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)) - skipping
  Could not find a version that satisfies the requirement pandas (from versions: )
No matching distribution found for pandas
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)) - skipping
</code></pre>
<p>Clearly I misunderstood the procedure, and I will keep looking.  If it’s obvious to y’all, any hints are welcome!</p>

---

## Post #19 by @gregsharp.geo (2019-06-30 22:28 UTC)

<p>Do you think it is because I set <code>Slicer_USE_PYTHONQT_WITH_OPENSSL</code> as unchecked?</p>

---

## Post #20 by @jamesobutler (2019-06-30 22:39 UTC)

<p>Yes, configuring python without OpenSSL is why the https url did not work.</p>
<p>From the console you can do <code>slicer.util.pip_install("pandas")</code>.</p>
<aside class="quote quote-modified" data-post="1" data-topic="7162">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162">Use full power of Python in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Until recently, Slicer used a custom Python build that was not binary compatible with third-party Python packages. Now, in latest Slicer Preview release, any Python packages can be installed and used in Slicer (except those that in direct conflict with version of libraries that are bundled with Slicer). 
Example: do curve fitting using scipy 

Install scipy by typing in Slicer’s Python console:

pip_install('scipy') 

Try a simple curve fitting example:

import numpy as np
from scipy.optimize im…
  </blockquote>
</aside>


---

## Post #21 by @jcfr (2019-07-01 17:58 UTC)

<blockquote>
<p>This PR should allow to build using VS2017. See <a href="https://github.com/Slicer/Slicer/pull/1163" class="inline-onebox">Problems with SUVComputation · Issue #1163 · Slicer/Slicer · GitHub</a></p>
</blockquote>
<p>Following <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28352">r28352</a> , PR 1163 has been integrated.</p>
<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="17" data-topic="7322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>The v142 toolset is binary compatible with v141 and v140. <a href="https://devblogs.microsoft.com/cppblog/cpp-binary-compatibility-and-pain-free-upgrades-to-visual-studio-2019/" class="inline-onebox">C++ Binary Compatibility and Pain-Free Upgrades to Visual Studio 2019 - C++ Team Blog</a></p>
</blockquote>
</aside>
<p>This is great.</p>
<p>This PRs should allow to build with VS2017 and VS2019. See <a href="https://github.com/Slicer/Slicer/pull/1164" class="inline-onebox">Runtime Error! Crashes when using Editor · Issue #1164 · Slicer/Slicer · GitHub</a> and <a href="https://github.com/Slicer/Slicer/pull/1165" class="inline-onebox">Transform Function not working · Issue #1165 · Slicer/Slicer · GitHub</a></p>
<p>After locally integrating these changes, could  you check that the build works well for you ?</p>

---

## Post #22 by @jamesobutler (2019-07-02 02:53 UTC)

<p>Yes I will check this upcoming week <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> . Currently on vacation for the Fourth of July this week.</p>

---

## Post #23 by @lassoan (2019-07-02 14:09 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="21" data-topic="7322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>After locally integrating these changes, could you check that the build works well for you ?</p>
</blockquote>
</aside>
<p>I’ve tested latest Slicer master branch build using VS2017 and VS2019:</p>
<ul>
<li>Slicer build and self-tests were successful (the same tests fail as in the nightly with VS2015)</li>
<li>Installation of scipy, matplotlib, and wxPython was successful (pip_install script did , and everything seemed to work fine (tested the plotting features with scripts <a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162/5">here</a>).</li>
<li>Packaging succeeded.</li>
</ul>
<p>There is just one set of warnings on VS2017 that might cause issues on systems that don’t have VS2017 runtime libraries installed: “<em>CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message): system runtime library file does not exist: ‘MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.CRT/msvcp140.dll’</em>” - but this seems to be a CMake issue and we can address it if we switch to VS2017 or VS2019 for the official builds.</p>

---

## Post #24 by @gcsharp (2019-07-02 18:10 UTC)

<p>This is excellent.  Thanks!!</p>

---

## Post #25 by @jcfr (2019-07-02 21:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="7322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve tested latest Slicer master branch build using VS2017 and VS2019:</p>
</blockquote>
</aside>
<p>This is great. Thanks for taking the time to do so.</p>
<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="7322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is just one set of warnings on VS2017 that might cause issues on systems that don’t have VS2017 runtime libraries installed: “ <em>CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message): system runtime library file does not exist: ‘MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.CRT/msvcp140.dll’</em> ” - but this seems to be a CMake issue and we can address it if we switch to VS2017 or VS2019 for the official builds.</p>
</blockquote>
</aside>
<p>While which version of CMake does this happen ? Which option did you select for the generator and toolset ? And is the warning report during configuration or during package creation ?</p>

---

## Post #26 by @lassoan (2019-07-02 22:55 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="25" data-topic="7322">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>While which version of CMake does this happen ? Which option did you select for the generator and toolset ? And is the warning report during configuration or during package creation ?</p>
</blockquote>
</aside>
<p>I’ve used CMake-3.14.3.</p>
<p>CMake generator options for VS2017: -G “Visual Studio 16 2019” -A x64 -T v141<br>
CMake generator options for VS2019: -G “Visual Studio 16 2019” -A x64 -T v142</p>
<p>The error occurred during configuration. There was no warning or error during package generation.</p>

---

## Post #27 by @jcfr (2019-07-03 18:35 UTC)

<p>When installing VS2019, did you install the following components:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ce2766e225e2b24b5eb9c6620a8a74da899778.png" alt="image" data-base62-sha1="zmbCjiyieQGhhVyb6AJwALIGgf6" width="643" height="95"></p>

---

## Post #28 by @lassoan (2019-07-03 19:12 UTC)

<p>Yes, I installed these - without that CMake did not find the compiler and could not even start configuring the project.</p>

---

## Post #29 by @jamesobutler (2019-07-03 19:39 UTC)

<p>It appears that another developer has had a similar issue. See this thread on visual studio’s forum:<br>
<a href="https://developercommunity.visualstudio.com/content/problem/618084/cmake-installrequiredsystemlibraries-broken-in-lat.html" class="onebox" target="_blank" rel="nofollow noopener">https://developercommunity.visualstudio.com/content/problem/618084/cmake-installrequiredsystemlibraries-broken-in-lat.html</a></p>
<p>Also a potential cmake related change, not sure which 3.14.X version this was included in:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://gitlab.kitware.com/assets/favicon-7901bd695fb93edb07975966062049829afb56cf11511236e61bcf425070e36e.png" class="site-icon" width="16" height="16">
      <a href="https://gitlab.kitware.com/cmake/cmake/merge_requests/3233" target="_blank" rel="nofollow noopener">GitLab</a>
  </header>
  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/541/cmakelogo-centered.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://gitlab.kitware.com/cmake/cmake/merge_requests/3233" target="_blank" rel="nofollow noopener">IRSL: Update redist directory for VS 2019 update 1 (!3233) · Merge Requests ·...</a></h3>

<p>VS 2019 Update 1 will fix its redist directories to be named `VC142` instead of `VC141`. It will also use cl `19.21` instead of `19.20` so we can use that...</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #30 by @jcfr (2019-07-03 19:46 UTC)

<blockquote>
<p>It appears that another developer has had a similar issue. See this thread on visual studio’s forum<br>
<a href="https://developercommunity.visualstudio.com/content/problem/618084/cmake-installrequiredsystemlibraries-broken-in-lat.html" class="inline-onebox">Developer Community</a></p>
</blockquote>
<p>This is great as it will allow to easily reproduce and move forward. Stay tuned for an update.</p>
<blockquote>
<p>Also a potential cmake related change, not sure which 3.14.X version this was included in:</p>
</blockquote>
<p>Thanks for pointing this out but it is already part of the CMake 3.14.3 release.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d92d85eb0edb4c75e2b4360a2fa3ef1964388848.png" alt="image" data-base62-sha1="uZf8VdEkjYEkiGlj1lv1QzKC25W" width="575" height="183"></p>

---

## Post #31 by @jcfr (2019-07-03 22:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Are you using the version of CMake provided by Visual Studio or one you installed yourself ?</p>
<p>Using this <a href="https://developercommunity.visualstudio.com/content/problem/618084/cmake-installrequiredsystemlibraries-broken-in-lat.html" rel="nofollow noopener">example</a>, I was not able to reproduce the problem using CMake 3.14.3 installed from <a href="https://cmake.org/download/" rel="nofollow noopener">https://cmake.org/download/</a></p>

---

## Post #32 by @lassoan (2019-07-03 22:47 UTC)

<p>I installed it myself. I’ll start a clean build and see if it comes up again.</p>

---

## Post #33 by @lassoan (2019-07-04 13:24 UTC)

<p>I did a new build from scratch using VS2017 toolset (with VS2019 IDE) and the CMake warnings are the same.</p>
<details>
<summary>
Warnings</summary>
<pre><code>  CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message):
    system runtime library file does not exist:
    'MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.CRT/msvcp140.dll'
  Call Stack (most recent call first):
    CMake/SlicerCPack.cmake:159 (include)
    CMake/LastConfigureStep/CMakeLists.txt:44 (include)
  
  CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message):
    system runtime library file does not exist:
    'MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.CRT/vcruntime140.dll'
  Call Stack (most recent call first):
    CMake/SlicerCPack.cmake:159 (include)
    CMake/LastConfigureStep/CMakeLists.txt:44 (include)
  
  CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message):
    system runtime library file does not exist:
    'MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.CRT/concrt140.dll'
  Call Stack (most recent call first):
    CMake/SlicerCPack.cmake:159 (include)
    CMake/LastConfigureStep/CMakeLists.txt:44 (include)
  
  CMake Warning at C:/Program Files/CMake/share/cmake-3.14/Modules/InstallRequiredSystemLibraries.cmake:558 (message):
    system runtime library file does not exist:
    'MSVC_REDIST_DIR-NOTFOUND/x64/Microsoft.VC141.OPENMP/vcomp140.dll'
  Call Stack (most recent call first):
    CMake/SlicerCPack.cmake:159 (include)
    CMake/LastConfigureStep/CMakeLists.txt:44 (include)
</code></pre>
</details>
<p>Slicer inner-build CMakeCache.txt contains <code>MSVC_REDIST_DIR:PATH=MSVC_REDIST_DIR-NOTFOUND</code>.</p>
<p>The files that are not found are available at “c:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Redist\MSVC\14.16.27012\x64\Microsoft.VC141.CRT”.</p>
<p><code>MSVC_REDIST_DIR</code> is correctly found for VS2015 and VS2019 toolsets:</p>
<ul>
<li><code>MSVC_REDIST_DIR:PATH=C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Redist/MSVC/14.21.27702</code></li>
<li><code>MSVC_REDIST_DIR:PATH=C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/redist</code></li>
</ul>
<p>As far as I remember, I only installed (and updated) Visual Studio Community edition using the default installer. I don’t know why there are files in both “Microsoft Visual Studio” and “Microsoft Visual Studio 14.0” subfolders.</p>

---

## Post #34 by @jamesobutler (2019-07-16 21:58 UTC)

<p>I have never had VS 2017 IDE installed on my system (it’s new) and still had the CMake warnings when using VS2019 generator and VS2017 toolset.</p>
<p>I posted <a href="https://gitlab.kitware.com/cmake/cmake/issues/19488" rel="nofollow noopener">https://gitlab.kitware.com/cmake/cmake/issues/19488</a> detailing the issue.</p>

---

## Post #35 by @jamesobutler (2019-07-23 13:00 UTC)

<p>I issued a <a href="https://gitlab.kitware.com/cmake/cmake/merge_requests/3585" rel="nofollow noopener">merge request</a> in CMake for the <code>MSVC_REDIST_DIR-NOTFOUND</code> issue. It has been merged and will be included in the CMake 3.15.1 release which will probably come out in 2 weeks or so.</p>
<p>So one less issue towards building Slicer with a newer visual studio toolset.</p>

---

## Post #36 by @jamesobutler (2019-07-28 20:32 UTC)

<p>CMake 3.15.1 was released with that fix.<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://blog.kitware.com/wp-content/uploads/2017/04/xExternalFavicon.png.pagespeed.ic.BxFzGTIFZT.png" class="site-icon" width="16" height="16">
      <a href="https://blog.kitware.com/cmake-3-15-1-available-for-download/" target="_blank" title="05:20PM - 26 July 2019" rel="nofollow noopener">Kitware Blog – 26 Jul 19</a>
  </header>
  <article class="onebox-body">
    <img src="https://blog.kitware.com/wp-content/uploads/2019/06/Release_ParaView.jpg" class="thumbnail" width="" height="">

<h3><a href="https://blog.kitware.com/cmake-3-15-1-available-for-download/" target="_blank" rel="nofollow noopener">CMake 3.15.1 available for download - Kitware Blog</a></h3>

<p>We are pleased to announce that CMake 3.15.1 is now available for download. Please use the latest release from our download page: https://cmake.org/download/ Thanks for ... Read More</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> Is there anything else preventing the change for the Windows Slicer nightly build being built with a newer toolset(v142 or at least v141) and updating to use the latest Qt LTS version (5.12.4)? <a href="https://blog.qt.io/blog/2019/06/17/qt-5-12-4-released-support-openssl-1-1-1/" rel="nofollow noopener">https://blog.qt.io/blog/2019/06/17/qt-5-12-4-released-support-openssl-1-1-1/</a></p>

---

## Post #37 by @jcfr (2019-07-28 21:26 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Thanks for the note <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>CMake 3.15.1 was released with that fix.</p>
</blockquote>
<ul>
<li>Newer CMake version has been installed on windows and macos build machines, then corresponding dashboard scripts have been <a href="https://github.com/Slicer/DashboardScripts/commit/f18c14da834634298aece29208fc0d0fdd529e86">updated</a></li>
<li>docker image used for linux build is also being <a href="https://github.com/dockbuild/dockbuild/pull/61">regenerated</a> to include newer CMake</li>
</ul>
<blockquote>
<p>Is there anything else preventing the change for the Windows Slicer nightly build being built with a newer toolset(v142 or at least v141) and updating to use the latest Qt LTS version (5.12.4)?</p>
</blockquote>
<p>It is a matter of taking the time to install the binaries on windows and update the dashboard script. for sake of consistency, I suggest we update the Qt version on all platforms.</p>
<p>Todo:</p>
<ul>
<li>Install Qt 5.12.4 on windows  build machine (overload)</li>
<li>Update <a href="https://github.com/Slicer/SlicerBuildEnvironment/blob/master/Docker/qt5-centos7/qt-installer-noninteractive.qs#L43">qt-installer-noninteractive.qs</a> in <code>qt5-centos7</code> docker image to use Qt 5.12.4</li>
<li>To allow building Qt on macOS, create branch <code>5.12.4</code> based of <a href="https://github.com/jcfr/qt-easy-build/tree/5.11.2">5.11.2</a> in <a href="https://github.com/jcfr/qt-easy-build" class="inline-onebox">GitHub - jcfr/qt-easy-build: Scripts allowing to easily build Qt with OpenSSL support on Linux, macOS or Windows</a>, then build Qt on factory-south-macos and update dashboard scripts</li>
</ul>

---
