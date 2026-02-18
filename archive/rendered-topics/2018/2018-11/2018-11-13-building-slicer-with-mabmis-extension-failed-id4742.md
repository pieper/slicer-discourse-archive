# Building Slicer with MABMIS extension failed

**Topic ID**: 4742
**Date**: 2018-11-13
**URL**: https://discourse.slicer.org/t/building-slicer-with-mabmis-extension-failed/4742

---

## Post #1 by @rasoul (2018-11-13 10:02 UTC)

<p>Hi everyone<br>
I want to build slicer with an Extension(MABMIS) but I have errors. the system specification is:<br>
Windows 7.<br>
Visual studio 2015 x64.<br>
cmake 3.12 x64.</p>
<p>The steps I did are as follows:<br>
1- As I want to build an extension(MABMIS), I put it in D:\S\Modules\CLI folder and added its name to D:\S\Modules\CLI\CMakeLists.txt .<br>
2- I configured the source Successfully using CMake GUI and adding QT5.1 path variable and also turning SimpleITK bool to off. Then I generated it and closed the Cmake UI.<br>
3- As there were no Slicer.exe in S4D\Slicer-build folder, I Open Slicer.sln in S4D directory using Visual studio and built All_Build in debug mode.<br>
The error is:</p>
<pre><code>49&gt;  CMake Error at Modules/CLI/MultiAtlas/CMakeLists.txt:12 (find_package):
49&gt;    By not providing "FindSlicer.cmake" in CMAKE_MODULE_PATH this project has
49&gt;    asked CMake to find a package configuration file provided by "Slicer", but
49&gt;    CMake did not find one.
49&gt;
49&gt;    Could not find a package configuration file provided by "Slicer" with any
49&gt;    of the following names:
49&gt;
49&gt;      SlicerConfig.cmake
49&gt;      slicer-config.cmake
49&gt;
49&gt;    Add the installation prefix of "Slicer" to CMAKE_PREFIX_PATH or set
49&gt;    "Slicer_DIR" to a directory containing one of the above files.  If "Slicer"
49&gt;    provides a separate development package or SDK, be sure it has been
49&gt;    installed.
49&gt;
49&gt;
49&gt;  -- Configuring incomplete, errors occurred!
49&gt;  See also "D:/S4D13/Slicer-build/CMakeFiles/CMakeOutput.log".
49&gt;  See also "D:/S4D13/Slicer-build/CMakeFiles/CMakeError.log".
49&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error 
MSB6006: "cmd.exe" exited with code 1.
50&gt;------ Build started: Project: ALL_BUILD, Configuration: Debug x64 ------
50&gt;  Building Custom Rule D:/S4/CMakeLists.txt
50&gt;  CMake does not need to re-run because D:/S4D13/CMakeFiles/generate.stamp is up-to-date.
========== Build: 48 succeeded, 2 failed, 0 up-to-date, 0 skipped ==========</code></pre>

---

## Post #2 by @fedorov (2018-11-13 14:49 UTC)

<p>That extension is failing on all platforms on the dashboard: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=mabmis">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=mabmis</a></p>
<p>I am not sure if developers of that extension are on this forum. You may need to contact them directly. See contact info at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MABMIS">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MABMIS</a></p>

---

## Post #3 by @dzenanz (2018-11-13 15:12 UTC)

<p>Commit <a href="https://github.com/BrainMeasurement/MultiAtlas/commit/1f54e8d939e03adc8feb22d5e39bda70314d231e" rel="nofollow noopener">1f54e8d</a>, which is referenced in the extensions index is severely out of date. <a href="https://github.com/BrainMeasurement/MultiAtlas/pull/4" rel="nofollow noopener">PR4</a>, which is based on <a href="https://github.com/dzenanz/MultiAtlas" rel="nofollow noopener">my fork</a>, was building with 4.8.1 in February.</p>
<p><a class="mention" href="/u/rasoul">@rasoul</a> Your build process sounds good. It looks like Slicer failed to compile for some reason, and then <code>FindSlicer</code> call in <code>MABMIS</code> failed. You could</p>
<ul>
<li>look higher up in the build log for errors</li>
<li>build solution again - that should try to build only the projects which failed to build the first time and the build log will be much shorter, making errors easier to spot</li>
<li>build Slicer.sln in S4D\Slicer-build (the so called inner build) - this should give more detailed errors related to building Slicer itself</li>
</ul>

---

## Post #4 by @rasoul (2018-11-14 05:58 UTC)

<p>Thanks <a class="mention" href="/u/fedorov">@fedorov</a> and <a class="mention" href="/u/dzenanz">@dzenanz</a>. I built it again and the error is the same one. I am building it again with Slicer 4.8.1.<br>
What wondering me is that <strong>there is no slicer.sln in S4D\Slicer-build directory</strong>. Have I forgotten something during my building?</p>

---

## Post #5 by @rasoul (2018-11-14 11:20 UTC)

<p>Building with slicer 4.8.1 faced with error. But now the error changed to this one.</p>
<blockquote>
<pre><code>49&gt;  CMake Error at Modules/CLI/MultiAtlas/CMakeLists.txt:13 (include):
49&gt;    include called with wrong number of arguments.  include() only takes one
49&gt;    file.
49&gt;  -- ITKIOImageBaseITKCommonitksysitkvnl_algoitkvnlitkv3p_netlibitknetlibitkvclITKTransformITKStatisticsitkNetlibSlatecITKIOTransformBaseITKSpatialObjectsITKPathITKMetaIOD:/S481B/zlib-install/lib/zlib.libITKTransformFactoryITKIOXML
49&gt;  -- Configuring SEM CLI module: IGR3D_MABMIS_Training
49&gt;  -- Configuring SEM CLI module: IGR3D_MABMIS_Testing
49&gt;  -- Configuring SEM CLI module: IGR3D_MABMIS_Direct_Invoke
49&gt;  CMake Error at Modules/CLI/MultiAtlas/CMakeLists.txt:75 (include):
49&gt;    include called with wrong number of arguments.  include() only takes one
49&gt;    file.
49&gt;
49&gt;  CMake Error at Modules/CLI/MultiAtlas/CMakeLists.txt:76 (include):
49&gt;    include called with wrong number of arguments.  include() only takes one
49&gt;    file.
</code></pre>
</blockquote>

---

## Post #6 by @rasoul (2018-11-14 12:13 UTC)

<p>I remove all lines that contains include() in CMakelist.txt and it built successfully.<img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=6" title=":grinning:" class="emoji" alt=":grinning:"><br>
Thank you guys for your helps</p>

---

## Post #7 by @jcfr (2018-11-14 14:06 UTC)

<p>As a side note, make sure you download the code from <a class="mention" href="/u/dzenanz">@dzenanz</a> fork, it contains the latest improvements. See <a href="https://github.com/dzenanz/MultiAtlas" class="inline-onebox">GitHub - dzenanz/MultiAtlas: 3D Slicer Extension for a multi-atlas segmentation technique from UNC's IDEA Group.</a></p>
<aside class="quote no-group" data-username="rasoul" data-post="6" data-topic="4742">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>it built successfully</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="rasoul" data-post="5" data-topic="4742">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>Modules/CLI/MultiAtlas/CMakeLists.txt</p>
</blockquote>
</aside>
<p>Our of curiosity, where is this file ? I failed to find it the extension source repository or the Slicer source repository:</p>
<ul>
<li><a href="https://github.com/dzenanz/MultiAtlas" class="inline-onebox">GitHub - dzenanz/MultiAtlas: 3D Slicer Extension for a multi-atlas segmentation technique from UNC's IDEA Group.</a></li>
<li><a href="https://github.com/Slicer/Slicer/tree/v4.8.1/Modules/CLI" class="inline-onebox">Slicer/Modules/CLI at v4.8.1 · Slicer/Slicer · GitHub</a></li>
</ul>

---

## Post #8 by @rasoul (2018-11-14 14:50 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="4742">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>make sure you download the code from</p>
</blockquote>
</aside>
<p>Yes it was downloaded from <a class="mention" href="/u/dzenanz">@dzenanz</a> fork.</p>
<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="4742">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>where is this file</p>
</blockquote>
</aside>
<p>After I downloaded MABMIS I put it to Slicer-source\Modules\CLI\MultiAtlas directory.</p>

---

## Post #9 by @jcfr (2018-11-14 15:14 UTC)

<aside class="quote no-group" data-username="rasoul" data-post="8" data-topic="4742">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rasoul/48/1493_2.png" class="avatar"> rasoul:</div>
<blockquote>
<p>I downloaded MABMIS I put it to Slicer-source\Modules\CLI\MultiAtlas directory.</p>
</blockquote>
</aside>
<p>That makes sense now.</p>
<p>To avoid modifying Slicer source tree, there are few other approaches:</p>
<h3><a name="p-17769-build-against-slicer-build-tree-1" class="anchor" href="#p-17769-build-against-slicer-build-tree-1" aria-label="Heading link"></a>build against Slicer build tree</h3>
<p>An alternative solution could be to build the extension against your Slicer build tree configuring the extension passing <code>-DSlicer_DIR:PATH=C:\path\to\Slicer-Superbuild\Slicer-build</code>, and then starting Slicer specifying <code>--launcher-additional-settings</code> and <code>--additional-module-paths</code></p>
<p>In the recent Slicer, a launcher is setup for you in the extension build directory.</p>
<h3><a name="p-17769-configure-passing-additional-extension-source-dir-2" class="anchor" href="#p-17769-configure-passing-additional-extension-source-dir-2" aria-label="Heading link"></a>configure passing additional extension source dir</h3>
<p><a href="https://github.com/Slicer/Slicer/blob/589e6b8d29cb13b434c97bd504f386d6e7503038/CMakeLists.txt#L1052-L1054" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/589e6b8d29cb13b434c97bd504f386d6e7503038/CMakeLists.txt#L1052-L1054</a></p>

---

## Post #11 by @rasoul (2018-11-15 05:03 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> for your suggestions.</p>

---

## Post #12 by @FelixBoy (2019-12-02 10:17 UTC)

<p>Hi,I just contacted MABMIS.And the same mistake you’ve encountered.Do you require QT？</p>

---
