# SimpleITK install fails on Windows

**Topic ID**: 23373
**Date**: 2022-05-11
**URL**: https://discourse.slicer.org/t/simpleitk-install-fails-on-windows/23373

---

## Post #1 by @keri (2022-05-11 13:22 UTC)

<p>Hi,</p>
<p>I just tried Slicer 3D <a href="https://github.com/Slicer/Slicer/commit/1efef1b35da0f95835c4f56def90629782cd492e" rel="noopener nofollow ugc">master branch</a> clean build on Windows 11, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" rel="noopener nofollow ugc">VS 2022</a> and I get error:</p>
<pre><code class="lang-auto">  Performing install step for 'SimpleITK'
  -- SimpleITK: Removing 'install' log files
  -- SimpleITK: SimpleITK_WORKING_DIR: C:/C/r/SimpleITK-build/SimpleITK-build/Wrapping/Python
  -- SimpleITK: C:/C/r/python-install/bin/PythonSlicer.exe;setup.py;install
  -- SimpleITK: Errors detected - See below.
  CMake Error at C:/C/r/slicersources-src/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
    SimpleITK: install step failed with exit code '1'.

    Outputs also captured in C:/C/r/SimpleITK_install_step_output.txt and
    C:/C/r/SimpleITK_install_step_error.txt.

    Setting env.  variable EP_EXECUTE_DISABLE_CAPTURE_OUTPUTS to 1 allows to
    disable file capture.

  Call Stack (most recent call first):
    C:/C/r/SimpleITK_install_step.cmake:3 (ExternalProject_Execute)



  Traceback (most recent call last):
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\setup.py", line 14, in &lt;module&gt;
      from SimpleITK._version import __version__
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK\__init__.py", line 18, in &lt;module&gt;
      from SimpleITK.SimpleITK import *
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK\SimpleITK.py", line 13, in &lt;module&gt;
      from . import _SimpleITK
  ImportError: DLL load failed while importing _SimpleITK: The specified module could not be found.
</code></pre>
<p>I guess some _SimpleITK’s dependencies not found.<br>
There is no such problem on Ubuntu</p>

---

## Post #2 by @lassoan (2022-05-11 14:13 UTC)

<p>It is almost always due to some invasive Python environment, which got added to the system PATH or other environment variables. See some more information and solution here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#errors-related-to-python" class="inline-onebox">Windows — 3D Slicer documentation</a></p>
<p>If the solution described there does not work then please copy here the error messages that the build output refers to.</p>

---

## Post #3 by @keri (2022-05-11 14:59 UTC)

<p>No I don’t have any other python installed and Windows is almost clean (installed it yesterday as virtual machine).</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the solution described there does not work then please copy here the error messages that the build output refers to.</p>
</blockquote>
</aside>
<p>Do you mean the content of <code>C:/C/r/SimpleITK_install_step_output.txt</code> and <code>C:/C/r/SimpleITK_install_step_error.txt</code> files?<br>
If so then <code>SimpleITK_install_step_output.txt</code> is empty now and <code>SimpleITK_install_step_error.txt</code> contains the same error:</p>
<pre><code class="lang-auto">  Traceback (most recent call last):
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\setup.py", line 14, in &lt;module&gt;
      from SimpleITK._version import __version__
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK\__init__.py", line 18, in &lt;module&gt;
      from SimpleITK.SimpleITK import *
    File "C:\C\r\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK\SimpleITK.py", line 13, in &lt;module&gt;
      from . import _SimpleITK
  ImportError: DLL load failed while importing _SimpleITK: The specified module could not be found.
</code></pre>
<p>I don’t know maybe the content of these files were changed while I was trying to repeat installation by modifying <code>setup.py</code> to discover the error and running it with command (as it is done in <a href="https://github.com/Slicer/Slicer/blob/1efef1b35da0f95835c4f56def90629782cd492e/SuperBuild/External_SimpleITK.cmake#L197" rel="noopener nofollow ugc">External_SimpleITK.cmake</a>):</p>
<pre><code class="lang-auto">cmake -P SimpleITK_install_step.cmake
</code></pre>
<p>Could you please take a look at my VS config:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0321569a383b7814d3df65ae501f6c40dbb0a449.png" alt="image" data-base62-sha1="rGRhpSp091HAuiIlJmoyE5mTCp" width="361" height="426"></p>

---

## Post #4 by @lassoan (2022-05-11 15:06 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I don’t know maybe the content of these files were changed while I was trying to repeat installation by modifying <code>setup.py</code> to discover the error and running it with command (as it is done in <a href="https://github.com/Slicer/Slicer/blob/1efef1b35da0f95835c4f56def90629782cd492e/SuperBuild/External_SimpleITK.cmake#L197">External_SimpleITK.cmake</a>):</p>
</blockquote>
</aside>
<p>It is typically not worth spending time with manually altered builds. Instead, delete your entire build tree and restart the build from scratch. It is very important to not do any manual configuration in CMake but <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#using-command-line-recommended">configure and start your build using a .bat file</a> to make sure that you can anytime rebuild Slicer from scratch with a single click of a button.</p>
<aside class="quote no-group" data-username="keri" data-post="3" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p><code>ImportError: DLL load failed while importing _SimpleITK: The specified module could not be found.</code></p>
</blockquote>
</aside>
<p>This indicates that you had an error earlier during the build. You’ll do a clean build form scratch anyway, so preserve that build log and search for the first error. I usually do that by searching for <code>: err</code> in the full build log.</p>

---

## Post #5 by @jamesobutler (2022-05-11 16:00 UTC)

<p>This error appears very similar to what was discussed in <a href="https://github.com/Slicer/Slicer/issues/6163" class="inline-onebox" rel="noopener nofollow ugc">SimpleITK build error · Issue #6163 · Slicer/Slicer · GitHub</a>.<br>
It was ultimately determined that it was a user’s use of some SimpleITK dependencies in the system path that caused the issue. See <a href="https://github.com/Slicer/Slicer/issues/6163#issuecomment-1041467125" class="inline-onebox" rel="noopener nofollow ugc">SimpleITK build error · Issue #6163 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #6 by @keri (2022-05-11 16:13 UTC)

<p>Thank you for the information.</p>
<p>I’m rebuilding the app and I hope for the miracle <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
If it doesn’t work I will investigate the root of the problem</p>

---

## Post #7 by @keri (2022-05-11 19:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/jamesobutler">@jamesobutler</a> I build <code>HDF5</code> as external project and I noticed that SimpleITK finds <code>HDF5</code> during cmake configuration time</p>
<p>I added HDF5 bin dir to <code>LibraryPaths</code> env var (in SimpleITK_Env.cmake) and the problem was solved.</p>
<p>Thus in my SlicerCAT SimpleITK links to HDF5 while pure Slicer doesn’t have it (only within VTK and/or ITK pure SLicer has HDF5)</p>

---

## Post #8 by @lassoan (2022-05-11 20:21 UTC)

<p>HDF5 is the library that most commonly breaks ITK build. It is always a huge pain. I’m not surprised that it broke your build, too.</p>
<aside class="quote no-group" data-username="keri" data-post="7" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I added HDF5 bin dir to <code>LibraryPaths</code> env var (in SimpleITK_Env.cmake) and the problem was solved.</p>
</blockquote>
</aside>
<p>If this solves all your problems and this workaround is acceptable for you then it is good. I’m not sure if this is the cleanest solution, but if you submit a pull request then I’m sure that at some point <a class="mention" href="/u/jcfr">@jcfr</a> can have a look at it and merge it if there are no better ideas.</p>

---

## Post #9 by @keri (2022-05-11 20:53 UTC)

<p>I agree with you</p>
<p>Sometimes to solve my issues I need to modify Slicer’s <code>External_smth.cmake</code>.<br>
In this case I prepare modified by me <code>External_smth.cmake</code> (in <code>SlicerCAT/CMake</code> dir) and during configuration time I copy this file to <code>slicersources-src/SuperBuild/External_smth.cmake</code> thus replacing Slicer’s original file:</p>
<pre><code class="lang-auto">configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/CMake/External_VTK.cmake" 
    "${slicersources_SOURCE_DIR}/SuperBuild/External_VTK.cmake" COPYONLY
  )
</code></pre>
<p>I can’t do this know (I’m sorry) but in the future some of those dirty solutions should be implemented as a PRs (like with HDF5).</p>
<p><strong>Just in case some of my propositions (for the future):</strong></p>
<ol>
<li>either build HDF5 as external project or add an opportunity to find HDF5 through HDF5_ROOT (probably easier to handle HDF5 versions) var (requires to modify VTK and ITK ext projects). Modified <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_VTK.cmake" rel="noopener nofollow ugc">External_VTK.cmake</a> and <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_ITK.cmake" rel="noopener nofollow ugc">External_ITK.cmake</a>
</li>
<li>ITK uses Eigen as third party libs. Add <code>mark_as_superbuild Eigen3_INCLUDE_DIR</code> to ITK ext project to link to Eigen. Because if some of ext proj also downloads Eigen and these Eigen libs are of different versions then you may face a problem when the compiled lib uses different Eigen libs in the same function for example. It is difficult to trace (I encountered that)</li>
<li>
<code>sqlite</code> is very popular library and it should be built as shared library. It is pretty often that sqlite is a dependency of some project. For now only <code>python</code> uses sqlite. Just in case I prepared <a href="https://github.com/tierra-colada/sqlite-amalgamation" rel="noopener nofollow ugc">shared sqlite project</a> (probably it could be done a little cleaner but it works) and the modified <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_sqlite.cmake" rel="noopener nofollow ugc">External_sqlite.cmake</a>. And probably <code>sqlite</code> should better be renamed to <code>SQLite3</code> as <a href="https://cmake.org/cmake/help/latest/module/FindSQLite3.html" rel="noopener nofollow ugc">CMake prefers</a>
</li>
</ol>

---

## Post #10 by @lassoan (2022-05-12 03:36 UTC)

<aside class="quote no-group" data-username="keri" data-post="9" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>either build HDF5 as external project or add an opportunity to find HDF5 through HDF5_ROOT (probably easier to handle HDF5 versions) var (requires to modify VTK and ITK ext projects). Modified <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_VTK.cmake">External_VTK.cmake</a> and <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_ITK.cmake">External_ITK.cmake</a></p>
</blockquote>
</aside>
<p>HDF5 is so messed up, build errors and ABI incompatibilites caused so much pain for ITK developers that they now just build it internally, using a custom prefix to isolate it from all external implementations.</p>
<p>Anyway, if you want to open this can of worm then you can put an <code>External_HDF5.cmake</code> into the <code>Superbuild</code> folder and set <code>Slicer_USE_SYSTEM_HDF5=ON</code>. It looks like Slicer automatically forwards this as <code>USE_SYSTEM_HDF5=ON</code> to all external projects.</p>
<aside class="quote no-group" data-username="keri" data-post="9" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>ITK uses Eigen as third party libs. Add <code>mark_as_superbuild Eigen3_INCLUDE_DIR</code> to ITK ext project to link to Eigen. Because if some of ext proj also downloads Eigen and these Eigen libs are of different versions then you may face a problem when the compiled lib uses different Eigen libs in the same function for example. It is difficult to trace (I encountered that)</p>
</blockquote>
</aside>
<p>In general, well-behaving libraries, such ITK, VTK, etc. build their own dependencies (such as Eigen, SQLite, HDF5, …) and don’t leak them out on public APIs, or if they do then they use custom prefixes in symbol names and DLL names to avoid any interference with all the other instances of these common libraries.</p>
<aside class="quote no-group" data-username="keri" data-post="9" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p><code>sqlite</code> is very popular library and it should be built as shared library. It is pretty often that sqlite is a dependency of some project. For now only <code>python</code> uses sqlite. Just in case I prepared <a href="https://github.com/tierra-colada/sqlite-amalgamation">shared sqlite project</a> (probably it could be done a little cleaner but it works) and the modified <a href="https://github.com/tierra-colada/Colada/blob/master/CMake/External_sqlite.cmake">External_sqlite.cmake</a>. And probably <code>sqlite</code> should better be renamed to <code>SQLite3</code> as <a href="https://cmake.org/cmake/help/latest/module/FindSQLite3.html">CMake prefers</a></p>
</blockquote>
</aside>
<p>A popular library typically cannot be built as a shared library due to API and ABI incompatibility issues. If it is a small library, such as SQLite, then the simplest is to just build it as a static library. If it is a huge and complex library, such as HDF5, then it may worth building it as a shared library - but then symbol names and shared library names require a custom prefix to ensure that many different versions can coexist.</p>

---

## Post #11 by @keri (2022-05-12 11:10 UTC)

<p>Thank you for the information</p>
<p>Regarding to the Slicer project I expect there most likely should not be ABI issues with generic libs like SQlite, HDF5 as we build everything at once.</p>
<p>In my case I needed to install PROJ and GDAL libs and they require SQlite. As I remember I couldn’t build them with static SQlite.</p>
<p>Current Slicer uses ITK v5.3rc03 wich uses latest Eigen 3.4 but before that ITK used Eigen 3.3 and I had external project Eigen 3.4<br>
I encountered a situation described above: in the same function I had two eigen versions worked differently <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>But I completely understand everything you said and probably in some cases SlicerCAT developers should be ready for things like that</p>

---

## Post #12 by @lassoan (2022-05-12 12:02 UTC)

<aside class="quote no-group" data-username="keri" data-post="11" data-topic="23373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>probably in some cases SlicerCAT developers should be ready for things like that</p>
</blockquote>
</aside>
<p>Sometimes you cannot build everything yourself. For example, extensions can install Python wheels, or you may use some SDKs that contain pre-built binaries.</p>
<p>Sometimes your various software components require different versions of the same library, so you cannot build and use a single version everywhere.</p>

---
