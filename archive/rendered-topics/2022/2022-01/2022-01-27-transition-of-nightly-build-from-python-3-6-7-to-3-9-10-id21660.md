# Transition of nightly build from Python 3.6.7 to 3.9.10

**Topic ID**: 21660
**Date**: 2022-01-27
**URL**: https://discourse.slicer.org/t/transition-of-nightly-build-from-python-3-6-7-to-3-9-10/21660

---

## Post #1 by @jcfr (2022-01-27 16:17 UTC)

<p>Few days ago, the version of CPython integrated in Slicer has been updated from  3.6.7 to 3.9.10 (see <a href="https://github.com/Slicer/Slicer/commit/34e48e8aef5dad19ec8a955d6f48a1940846e3f3">Slicer@34e48e8ae</a>).</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>As of 2022.01.27, 10:39am ET, I expect <strong>all identified issues</strong> to be <strong>resolved</strong> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> .</td>
</tr>
</tbody>
</table>
</div><h3><a name="p-73091-acknowledgments-1" class="anchor" href="#p-73091-acknowledgments-1" aria-label="Heading link"></a>Acknowledgments</h3>
<p>This was made possible by the contributions and help of many <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>More specifically, I would like to acknowledge the specific help of <a class="mention" href="/u/fbordignon">@fbordignon</a>,  <a class="mention" href="/u/jamesobutler">@jamesobutler</a> &amp; <a class="mention" href="/u/lassoan">@lassoan</a> for the Slicer integration <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=15" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"> as well as <a class="mention" href="/u/fbordignon">@fbordignon</a>, <a href="https://github.com/dand-oss">dand-oss</a> and <a href="https://github.com/dbrnz">dbrnz</a> for the contributions related to the update of <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem">python-cmake-buildsystem</a> to support CPython 3.7, 3.8 and 3.9 <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=15" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<h3><a name="p-73091-status-of-jan-27th-nightly-builds-2" class="anchor" href="#p-73091-status-of-jan-27th-nightly-builds-2" aria-label="Heading link"></a>Status of Jan 27th nightly builds</h3>
<p>While working on addressing the <a href="https://github.com/Slicer/Slicer/pull/6138">PR-6138</a>, we disabled the nightly build.</p>
<p>After manually updating the Slicer source checkout on each build machine, we just <strong>restarted them</strong>.</p>
<p>This was done  by disabling the source checkout update setting the env. variable <code>run_ctest_with_update</code> to <code>FALSE</code> (see <a href="https://github.com/Slicer/Slicer/blob/169638177c555484f4524e60d78859aec52408b5/CMake/SlicerDashboardDriverScript.cmake#L245-L258">here</a>)</p>
<h3><a name="p-73091-status-of-transition-3" class="anchor" href="#p-73091-status-of-transition-3" aria-label="Heading link"></a>Status of transition</h3>
<p>Following the transition, we had a few issues to address.</p>
<p>For future reference, here is the list of associated pull requests:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6131">PR-6131</a></td>
<td><code>COMP: Update python packages to latest</code></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6132">PR-6132</a></td>
<td><code>STYLE: Upgrade python syntax to 3.9 and newer</code></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6133">PR-6133</a></td>
<td><code>COMP: Update LibFFI to fix macOS link error related to HAVE_AS_X86_PCREL test</code></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6134">PR-6134</a></td>
<td><code>COMP: Fix windows build updating SimpleITK install step</code></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6137">PR-6137</a></td>
<td><code>BUG: Fix use of removed time.clock() method</code></td>
</tr>
</tbody>
</table>
</div><p>and more recently this one:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6138">PR-6138</a></td>
<td><code>BUG: Fix compiled python module import on windows</code></td>
</tr>
</tbody>
</table>
</div><h3><a name="p-73091-notes-related-to-osadd_dll_directory-4" class="anchor" href="#p-73091-notes-related-to-osadd_dll_directory-4" aria-label="Heading link"></a>Notes related to <code>os.add_dll_directory</code></h3>
<p>Starting with CPython 3.8, the directories associated with dependencies of compiled python modules are expected to be added using the <a href="https://docs.python.org/3/library/os.html#os.add_dll_directory">os.add_dll_directory</a> function from the CPython standard library.</p>
<p>This snippet from the porting notes is particularly relevant:</p>
<blockquote>
<p>DLL dependencies for extension modules and DLLs loaded with <a href="https://docs.python.org/3/library/ctypes.html#module-ctypes"> <code>ctypes</code> </a> on Windows are now resolved more securely. Only the system paths, the directory containing the DLL or PYD file, and directories added with <a href="https://docs.python.org/3/library/os.html#os.add_dll_directory"> <code>add_dll_directory()</code> </a> are searched for load-time dependencies. Specifically, <code>PATH</code> and the current working directory are no longer used, and modifications to these will no longer have any effect on normal DLL resolution. If your application relies on these mechanisms, you should check for <a href="https://docs.python.org/3/library/os.html#os.add_dll_directory"> <code>add_dll_directory()</code> </a> and if it exists, use it to add your DLLs directory while loading your library. Note that Windows 7 users will need to ensure that Windows Update KB2533623 has been installed (this is also verified by the installer). (Contributed by Steve Dower in <a href="https://bugs.python.org/issue36085">bpo-36085</a>.)</p>
</blockquote>
<p><em>Source: <a href="https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew">https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew</a></em></p>
<p>To address this in Slicer, we added two modules generated by <a href="https://github.com/Slicer/Slicer/blob/169638177c555484f4524e60d78859aec52408b5/SuperBuild/python_configure_python_launcher.cmake#L88-L127">SuperBuild/python_configure_python_launcher.cmake</a>:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>slicer_dll_directories.py</code></td>
<td>Helper module for providing additional search paths for native dependencies when importing extension modules or loading DLLs using ctypes.</td>
</tr>
<tr>
<td><code>sitecustomize.py</code></td>
<td>Ensures additional search paths are systmatically added when using <code>PythonSlicer</code> or <code>Slicer</code>. See <a href="https://docs.python.org/3/library/site.html">https://docs.python.org/3/library/site.html</a></td>
</tr>
</tbody>
</table>
</div><h3><a name="p-73091-notes-related-to-python-cmake-buildsystemhttpsgithubcompython-cmake-buildsystempython-cmake-buildsystem-5" class="anchor" href="#p-73091-notes-related-to-python-cmake-buildsystemhttpsgithubcompython-cmake-buildsystempython-cmake-buildsystem-5" aria-label="Heading link"></a>Notes related to <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem">python-cmake-buildsystem</a></h3>
<p>The project now supports building the following versions of CPython:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>2.7.3 to 2.7.15</td>
</tr>
<tr>
<td>3.5.1 to 3.5.10</td>
</tr>
<tr>
<td>3.6.0 to 3.6.15</td>
</tr>
<tr>
<td>3.7.0 to 3.7.12</td>
</tr>
<tr>
<td>3.8.0 to 3.8.12</td>
</tr>
<tr>
<td>3.9.0 to 3.9.10</td>
</tr>
</tbody>
</table>
</div><p>Additionally, since starting with CPython 3.7 on Linux, and CPython 3.8 on Windows, the LibFFI dependencies is not included anymore in CPython sources anymore.</p>
<p>To address this, we now have a fork of the project adding CMake support.</p>
<p>Last, note that the plan is to contribute  this changes updating the existing pull request (<a href="https://github.com/libffi/libffi/pull/535">PR-535</a> - <code>Add cmake configuration files</code>) <img src="https://emoji.discourse-cdn.com/twitter/facepunch.png?v=15" title=":facepunch:" class="emoji" alt=":facepunch:" loading="lazy" width="20" height="20">  <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=15" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>
<p>See <a href="https://github.com/python-cmake-buildsystem/libffi/tree/libffi-cmake-buildsystem-v3.4.2-2021-06-28-f9ea416">python-cmake-buildsystem/libffi@libffi-cmake-buildsystem-v3.4.2-2021-06-28-f9ea416</a></p>
<h3><a name="p-73091-notes-related-to-the-ctkapplauncherhttpsgithubcomcommontkapplauncher-6" class="anchor" href="#p-73091-notes-related-to-the-ctkapplauncherhttpsgithubcomcommontkapplauncher-6" aria-label="Heading link"></a>Notes related to the <a href="https://github.com/commontk/AppLauncher">CTKAppLauncher</a></h3>
<p>While working on <a href="https://github.com/Slicer/Slicer/pull/6138">PR-6138</a>, we also:<br>
this also led me to:</p>
<ul>
<li>
<p>updated the deployment target of the pre-build macOS binary package from 10.6 (Snow Leopard, released in 2009) to 10.13 (High Sierra, release in 2017). This is consistent with the Slicer macOS deployment target being 10.13.</p>
</li>
<li>
<p>transition the macOS continuous integration from TravisCI to GitHub Actions</p>
</li>
<li>
<p>fixed an issue happening when building the launcher against Qt &gt;= 5.14. See <a href="https://github.com/commontk/AppLauncher/commit/ef13633cd89b59ee491a59dc0d18c2fa01ada220">commontk/AppLauncher@ef13633</a></p>
</li>
<li>
<p>published a static build of Qt 5.15.2 for macOS. See <a href="https://github.com/jcfr/qt-static-build/releases/tag/qt-5.15.2-macosx10.13-static-x86_64" class="inline-onebox">Release qt-5.15.2-macosx10.13-static-x86_64 · jcfr/qt-static-build · GitHub</a></p>
</li>
</ul>
<h3><a name="p-73091-related-posts-7" class="anchor" href="#p-73091-related-posts-7" aria-label="Heading link"></a>Related posts</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/how-to-update-slicers-python-version-from-3-6-7-to-3-7/20409" class="inline-onebox">How to update Slicer's Python version from 3.6.7 to 3.7?</a></li>
<li><a href="https://discourse.slicer.org/t/how-to-update-python-version-from-3-67-to-3-8/16650" class="inline-onebox">How to update Python version from 3.67 to 3.8</a></li>
</ul>

---

## Post #2 by @lassoan (2022-01-27 20:05 UTC)

<p>Thanks a lot to all, it works!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dc441a50b44e2ba0bda3c836166c94e4d85cb89.png" data-download-href="/uploads/short-url/4fkk5OzfdbDb7yr9fYhOyeCF1Ut.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc441a50b44e2ba0bda3c836166c94e4d85cb89_2_690x162.png" alt="image" data-base62-sha1="4fkk5OzfdbDb7yr9fYhOyeCF1Ut" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc441a50b44e2ba0bda3c836166c94e4d85cb89_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc441a50b44e2ba0bda3c836166c94e4d85cb89_2_1035x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1dc441a50b44e2ba0bda3c836166c94e4d85cb89_2_1380x324.png 2x" data-dominant-color="BDBDBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1483×349 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
