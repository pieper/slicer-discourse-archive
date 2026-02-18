# SlicerCustomAppTemplate Build failed

**Topic ID**: 24073
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/slicercustomapptemplate-build-failed/24073

---

## Post #1 by @Mrwa_Awoda (2022-06-28 07:39 UTC)

<p>OS: Windows.10<br>
Cmake version 3.22.2<br>
VStudio version: 17.0.5 2022<br>
Python 3:10 (64-bit)</p>
<p>hello there,<br>
I tried to build the SlicerCustomAppTemplate as it is as steps say in <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> and I get so many “Failed” and errors …</p>
<p>Slicer version I installed in my pc is 4.11 and the version I built (according to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>) is 4.13, will that gonna cause me a problem in any way?</p>
<p>I get this warning in CMake:</p>
<pre><code class="lang-auto">&gt; CMake Warning (dev) at G:/W/SR/slicersources-src/CMake/SlicerMacroExtractRepositoryInfo.cmake:87 (message):
&gt;   Skipping repository info extraction: directory [G:/W/S] is not a GIT
&gt;   checkout
&gt; Call Stack (most recent call first):
&gt;   G:/W/SR/slicersources-src/CMake/SlicerVersion.cmake:99 (SlicerMacroExtractRepositoryInfo)
&gt;   G:/W/SR/slicersources-src/CMakeLists.txt:332 (include)
&gt; This warning is for project developers.  Use -Wno-dev to suppress it.
</code></pre>
<p>and first error was:</p>
<pre><code class="lang-auto">9&gt;------ Build started: Project: bzip2, Configuration: Release x64 ------
9&gt;Creating directories for 'bzip2'
9&gt;Building Custom Rule G:/W/SR/slicersources-src/CMakeLists.txt
9&gt;Performing download step (git clone) for 'bzip2'
9&gt;Cloning into 'bzip2'...
9&gt;fatal: unable to access 'https://github.com/commontk/bzip2.git/': Could not resolve host: github.com
9&gt;Cloning into 'bzip2'...
9&gt;fatal: unable to access 'https://github.com/commontk/bzip2.git/': Could not resolve host: github.com
9&gt;Cloning into 'bzip2'...
9&gt;fatal: unable to access 'https://github.com/commontk/bzip2.git/': Could not resolve host: github.com
9&gt;-- Had to git clone more than once:
9&gt;CMake Error at slicersources-build/bzip2-prefix/tmp/bzip2-gitclone.cmake:31 (message):
9&gt;  Failed to clone repository: 'https://github.com/commontk/bzip2.git'
9&gt;
9&gt;
9&gt;          3 times.
9&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(242,5): error MSB8066: Custom build for 'G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-mkdir.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-download.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-update.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-patch.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-configure.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-build.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-generate_project_description.rule;G:\W\SR\CMakeFiles\6cf71889da89bd29a67e3c1b07672240\bzip2-install.rule;G:\W\SR\CMakeFiles\f17b097b3d5dff0a140c4b8814ae85bb\bzip2-complete.rule;G:\W\SR\CMakeFiles\bd5e72b23bb3644be4e169074b908c95\bzip2.rule;G:\W\SR\slicersources-src\CMakeLists.txt' exited with code 1.
9&gt;Done building project "bzip2.vcxproj" -- FAILED.
</code></pre>
<p>Here is the CMake  configure output: <a href="https://docs.google.com/document/d/1kzUGDeKVQ08CgP45BlmEFbRxvREtA2K6uggslpoGs6s/edit?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">CMake configure output - Google Docs</a><br>
and the Build Output: <a href="https://docs.google.com/document/d/1UBjP_Q4T_dEjxKOo7KgtpfkBCCTLExb_r4-a6MUZEX0/edit?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">SlicerCustomAppTemplate Build Output - Google Docs</a></p>

---

## Post #2 by @cpinter (2022-06-28 08:56 UTC)

<p>Did you just download the SlicerCustomAppTemplate code as zip and uncompressed? In that case you should do a proper Git clone instead.</p>
<blockquote>
<p>Slicer version I installed in my pc is 4.11 and the version I built (according to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">Windows — 3D Slicer documentation</a>) is 4.13, will that gonna cause me a problem in any way?</p>
</blockquote>
<p>No.</p>

---

## Post #3 by @Mrwa_Awoda (2022-07-02 18:44 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="24073">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Did you just download the SlicerCustomAppTemplate code as zip and uncompressed?</p>
</blockquote>
</aside>
<p>No, I followed the instructions in “BUILD.md” file in VSCode editor after executing the two lines code in Step1 here <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a> so I can be able to have a Cmakelists.txt file for the build!</p>

---

## Post #4 by @cpinter (2022-07-04 11:37 UTC)

<p>OK thanks! The errors also suggest that the script was not able to access github (<code>fatal: unable to access 'https://github.com/commontk/bzip2.git/': Could not resolve host: github.com</code>). Either a momentary issue on the server or your own internet connection. Maybe firewall issues but I never had that with github connections. I suggest trying again until this specific error is gone and it either succeeds or another type of error happens.</p>

---

## Post #5 by @Mrwa_Awoda (2022-07-04 13:42 UTC)

<p>Oooookay, appreciate your reply… let me try again and see!</p>

---
