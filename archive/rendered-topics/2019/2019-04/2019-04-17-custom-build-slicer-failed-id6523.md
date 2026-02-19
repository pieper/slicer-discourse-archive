---
topic_id: 6523
title: "Custom Build Slicer Failed"
date: 2019-04-17
url: https://discourse.slicer.org/t/6523
---

# Custom build Slicer failed

**Topic ID**: 6523
**Date**: 2019-04-17
**URL**: https://discourse.slicer.org/t/custom-build-slicer-failed/6523

---

## Post #1 by @Littlehhh (2019-04-17 09:50 UTC)

<p>I use the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a>  to custom the slicer. When I set the option like this <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b431bb94b6ead12f7d692b2c9b24a540e4f3d7f2.png" data-download-href="/uploads/short-url/pI4uMR241qg8AwnfHTMkJX5DrHA.png?dl=1" title="%E6%8D%95%E8%8E%B7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b431bb94b6ead12f7d692b2c9b24a540e4f3d7f2.png" alt="%E6%8D%95%E8%8E%B7" data-base62-sha1="pI4uMR241qg8AwnfHTMkJX5DrHA" width="690" height="278" data-dominant-color="F2F1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E6%8D%95%E8%8E%B7</span><span class="informations">1141×461 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when it build,  “ctkAbstractPythonManager.h”: No such file or directory [D:\t2\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj]    Slicer	D:\Projects\Slicer\Base\QTCore\qSlicerCorePythonManager.h	25	<br>
the error appears</p>
<p>I want to know if it is the right way to let slicer lighter ,  and the right way to build costum slicer</p>

---

## Post #2 by @jcfr (2019-04-17 13:32 UTC)

<p>Thanks for reporting the problem.</p>
<p>To help address the issue and better understand the context (which options were exactly enabled or disabled, …), here are few suggestions:</p>
<ul>
<li>could you check that the version of Slicer found at the top of the <code>CMakeLists.txt</code> is a recent one. If not, I suggest you update it to be the most recent one. See <a href="https://github.com/Slicer/Slicer/commits/master" rel="nofollow noopener">https://github.com/Slicer/Slicer/commits/master</a>. This will ensure the most recent fixes are included.</li>
<li>could you try to configure and build the project using the command line.
<ul>
<li>(1) remove all files from the build directories</li>
<li>(2) Open windows command line terminal</li>
<li>(3) configure the project with a command like this one <code>cmake.exe -DSlicer_USE_XYZ:BOOL=OFF ... -G "Visual Studio 14 2015" D:\Projects\Slicer</code>. This will allow to easily reproduce the problem.</li>
<li>(4) build the project using a command line like <code>cmake --build D:\t2\Slicer-build --config Release -- /m</code>. The <code>/m</code> allows to do a parallel build using Visual Studio.</li>
</ul>
</li>
</ul>

---

## Post #3 by @Littlehhh (2019-04-17 15:57 UTC)

<p>Thanks for reply!</p>
<p>I want to build a lighter slicer, so I want to custom the Slicer to remove extra modules that I don’t want.</p>
<h2><a name="p-23193-about-slicer-source-1" class="anchor" href="#p-23193-about-slicer-source-1" aria-label="Heading link"></a>About Slicer Source</h2>
<p>I have git clone the Slicer repository on my machine and before the build, I always use commands <code>git pull origin</code> to sync from remote repo</p>
<h2><a name="p-23193-about-options-2" class="anchor" href="#p-23193-about-options-2" aria-label="Heading link"></a>About Options</h2>
<p>Here is the screenshot of the Options in CMakeList.txt from the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c07ef95c1d58183fc2a07e15fc9bb8e0bef2c715.png" data-download-href="/uploads/short-url/rsTIkshvoXOEpwXw0C0o1Aih5jf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c07ef95c1d58183fc2a07e15fc9bb8e0bef2c715.png" alt="image" data-base62-sha1="rsTIkshvoXOEpwXw0C0o1Aih5jf" width="690" height="411" data-dominant-color="F2F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×716 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ecb1a47cd7156fc99a5ed301f6b71f710a26987.png" data-download-href="/uploads/short-url/8XuKpDLGecPKZUbs6jlofEnSb3x.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ecb1a47cd7156fc99a5ed301f6b71f710a26987.png" alt="image" data-base62-sha1="8XuKpDLGecPKZUbs6jlofEnSb3x" width="690" height="411" data-dominant-color="F7F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×716 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-23193-about-build-3" class="anchor" href="#p-23193-about-build-3" aria-label="Heading link"></a>About Build</h2>
<p>My platform is Win10 X64 version 17763<br>
Here is command-line in my batch file and I use it to generate the VS projects.</p>
<pre data-code-wrap="bat"><code class="lang-bat">
mkdir D:\\S1D

cd /d D:\\t3

"D:\\Library\\cmake-3.14.0-rc3-win64-x64\\bin\\cmake.exe" -G "Visual Studio 15 2017 Win64" -T "v140" -Dslicersources_SOURCE_DIR=D:\\Projects\\Slicer -DQt5_DIR:PATH=D:\\Library\\Qt\\Qt5.10.0\\5.10.0\\msvc2015_64\\lib\\cmake\\Qt5 D:\\Projects\\test

</code></pre>
<p>And then I use the VS2017 open the .sln to finish the ALL_BUILD.</p>
<p>When it build at Slicer projects, it stopped and throw a error just like this<br>
Can not open include file<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abd2ac669a1ba51cd1f2a8925d8145771f61ed11.png" alt="image" data-base62-sha1="ow10OMGqumCq560HEHnHBCH3LvX" width="690" height="14" data-dominant-color="1C7FC1"><br>
I try to add the required .h and .cxx dir in Slicer project include path, It still the same error.</p>
<h2><a name="p-23193-about-something-else-i-want-to-know-4" class="anchor" href="#p-23193-about-something-else-i-want-to-know-4" aria-label="Heading link"></a>About Something else I want to know</h2>
<ol>
<li>
<p>It seems that the Options in the SlicerCustomAppTemplate are not the whole options, Where can I get the whole options</p>
</li>
<li>
<p>ALL of the Options in SlicerCustomAppTemplate can be TURN OFF? Which ones can be turned off, or Which ones can not be turned off.</p>
</li>
<li>
<p>How to build the Slicer faster.</p>
</li>
</ol>
<h2><a name="p-23193-thanks-for-your-reply-5" class="anchor" href="#p-23193-thanks-for-your-reply-5" aria-label="Heading link"></a>Thanks for your reply</h2>

---

## Post #4 by @lassoan (2019-04-17 16:12 UTC)

<p>Most likely the problem is that the source code path (“D:\Projects\Slicer”) is too long. Try to use “D:\S4” instead.</p>
<aside class="quote no-group" data-username="Littlehhh" data-post="3" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<p>It seems that the Options in the SlicerCustomAppTemplate are not the whole options, Where can I get the whole options</p>
</blockquote>
</aside>
<p>You can modify any Slicer build options. What options would you like to change?</p>
<aside class="quote no-group" data-username="Littlehhh" data-post="3" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<p>ALL of the Options in SlicerCustomAppTemplate can be TURN OFF? Which ones can be turned off, or Which ones can not be turned off.</p>
</blockquote>
</aside>
<p>You can turn off all features that you don’t need. You can search for the name of the option in Slicer source code to see what the impact of turning it off.</p>
<aside class="quote no-group" data-username="Littlehhh" data-post="3" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<p>How to build the Slicer faster.</p>
</blockquote>
</aside>
<p>Disable all modules that you don’t need will make building and running Slicer much faster.</p>
<p>Note that build time should not be a concern, since a complete build takes only a few hours on a desktop computer (and maybe up to a day on a very slow laptop). After that, you’ll only need to modify and build your own custom modules, which should take just a couple of minutes for a rebuild and a few ten seconds for a regular build.</p>

---

## Post #5 by @Littlehhh (2019-04-17 17:42 UTC)

<p>But I have a successful build with the same source code path with the fully slicer features, When I use the    SlicerCustomAppTemplate and turn off some features, it doesn’t work.</p>

---

## Post #6 by @jcfr (2019-04-17 17:45 UTC)

<aside class="quote no-group quote-modified" data-username="Littlehhh" data-post="3" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<p>“D:\Library\cmake-3.14.0-rc3-win64-x64\bin\cmake.exe” -G “Visual Studio 15 2017 Win64” -T “v140” -Dslicersources_SOURCE_DIR=D:\Projects\Slicer -DQt5_DIR:PATH=D:\Library\Qt\Qt5.10.0\5.10.0\msvc2015_64\lib\cmake\Qt5 D:\Projects\test</p>
</blockquote>
</aside>
<p>Thanks, that is helpful. Looks like you are building with default options associated with the template (where python is disabled), we should be able to fix the issue.</p>
<p>Note  that we will soon setup continuous integration for the <code>SlicerCustomAppTemplate</code> project itself, this should allow us to catch such regression.</p>

---

## Post #7 by @jcfr (2019-04-17 18:12 UTC)

<blockquote>
<p>when it build, “ctkAbstractPythonManager.h”: No such file or directory [D:\t2\Slicer-build\Base\QTGUI\qSlicerBaseQTGUI.vcxproj] Slicer D:\Projects\Slicer\Base\QTCore\qSlicerCorePythonManager.h 25<br>
the error appears</p>
</blockquote>
<p>That said, it is strange to see this error because with <code>Slicer_USE_PYTHONQT</code> set to <code>OFF</code> in your build tree, there should be no attempt to build the <code>qSlicerCorePythonManager</code> class.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/Base/QTGUI/CMakeLists.txt#L306-L320" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/Base/QTGUI/CMakeLists.txt#L306-L320</a></p>
<p><a href="https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/Base/QTCore/CMakeLists.txt#L221-L249" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/Base/QTCore/CMakeLists.txt#L221-L249</a></p>

---

## Post #8 by @Littlehhh (2019-04-18 01:12 UTC)

<p>Thanks for your reply！<br>
I will try to build Slicer in a clean environment on another machine later on.</p>
<h2>something confusing</h2>
<ul>
<li>If I can use the same slicer source for multiple builds, will they interfere with each other?</li>
<li>Are the fully custom build options in<br>
<a href="https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/CMakeLists.txt" rel="nofollow noopener">Slicer/CMakeList.txt</a>?</li>
</ul>
<p>Great experience in Slicer forum, Not only the Q&amp;A edit system but also your reply! THANKS.</p>

---

## Post #9 by @Littlehhh (2019-04-18 02:14 UTC)

<h2>Another question about SlicerCustomAppTemplate</h2>
<p>What the difference between the<br>
<code>option(Slicer_BUILD_xxxx_SUPPORT OFF/ON)</code><br>
between</p>
<pre><code class="lang-auto">set(Slicer_CLIMODULES_ENABLED or DISABLED
  )
set(Slicer_QTLOADABLEMODULES_ENABLED or DISABLED
  )
set(Slicer_QTSCRIPTEDMODULES_ENABLED or DISABLED
  )
</code></pre>
<p>For example:<br>
<code>option(Slicer_BUILD_DICOM_SUPPORT "Build application with DICOM support" ON)</code><br>
and</p>
<pre><code class="lang-auto">set(Slicer_CLIMODULES_ENABLED
   CreateDICOMSeries
  )
set(Slicer_QTSCRIPTEDMODULES_ENABLED
   DICOM
   DICOMLib
   DICOMPatcher
   DICOMPlugins
  )
</code></pre>
<p>What do they stand for and what the differences?</p>

---

## Post #10 by @lassoan (2019-04-18 02:23 UTC)

<p><code>Slicer_???MODULES_ENABLED</code> can be used to disable entire class of modules. I would recommend to disable modules by name instead.</p>
<p>If you don’t need DICOM support at all, then disable <code>Slicer_BUILD_DICOM_SUPPORT</code>. If you want to have some DICOM reading/writing capabilities then enable it and just disable whatever DICOM related module you don’t need.</p>

---

## Post #11 by @jcfr (2019-04-18 02:32 UTC)

<aside class="quote no-group" data-username="Littlehhh" data-post="8" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<ul>
<li>If I can use the same slicer source for multiple builds, will they interfere with each other?</li>
</ul>
</blockquote>
</aside>
<p>You can share the source between different build. Just be aware that the Git hash written in the <code>CMakeLists.txt</code> may not correspond to the source associated with a given build.</p>
<aside class="quote no-group" data-username="Littlehhh" data-post="8" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/littlehhh/48/3484_2.png" class="avatar"> Littlehhh:</div>
<blockquote>
<ul>
<li>Are the fully custom build options in<br>
<a href="https://github.com/Slicer/Slicer/blob/8b2910fb9738dec05815ac853714634a7cfe04b2/CMakeLists.txt">Slicer/CMakeList.txt</a>?</li>
</ul>
</blockquote>
</aside>
<p>The options listed in the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/CMakeLists.txt">CMakeLists.txt</a> of your custom  application are a subset of the <a href="https://github.com/Slicer/Slicer/blob/master/CMakeLists.txt">one</a> found in the one of Slicer.</p>
<p>We only listed the most common one, but all the other option could be set similarly.</p>

---

## Post #12 by @Littlehhh (2019-04-18 02:39 UTC)

<p>I mean that the CMakeList.txt in Slicer source root dir can get the full options? I want to know where can I get the other options.<br>
And I still confuse about the difference <code>option(Slicer_BUILD_xxxx_SUPPORT OFF/ON)</code> and <code>set(Slicer_CLIMODULES_ENABLED or DISABLED )</code></p>
<p>Thanks for reply!</p>

---

## Post #13 by @jcfr (2019-04-18 03:02 UTC)

<blockquote>
<p>`Slicer_BUILD_xxxx_SUPPORT OFF/ON</p>
</blockquote>
<p>This allows to build Slicer  without the capabilities of loading a type of modules. When the option is disabled, Slicer won’t even attempt to look for the type of modules.</p>
<blockquote>
<p><code>Slicer_CLIMODULES_ENABLED or DISABLED</code></p>
</blockquote>
<p>This allows to build Slicer with or without a specific list of modules of type CLI. But it will not prevent slicer from looking for CLI modules. For example, starting Slicer specifying <code>--additional-module-paths /path/to/folder/with/modules</code> will look for modules in <code>/path/to/folder/with/modules</code>.</p>

---

## Post #14 by @Littlehhh (2019-04-18 10:34 UTC)

<p>I have tried to build the Slicer using the same options on another machine, it still failed with the same error.And When I Turn ON the Option Slicer_WITH_PYTHONQT, it can build successfully. So Maybe there is a BUG in  somewhere?</p>

---

## Post #15 by @jcfr (2019-04-18 13:55 UTC)

<blockquote>
<p>it still failed with the same error</p>
</blockquote>
<p>This is now fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28153">r28153</a></p>
<p>For reference, the complete error was:</p>
<pre><code class="lang-auto">In file included from /home/jcfr/Projects/Slicer-Qt5-VTK8/Base/QTGUI/qSlicerPythonManager.h:17:0,
                 from /home/jcfr/Projects/Slicer-Qt5-VTK8/Base/QTGUI/qSlicerWebPythonProxy.cxx:30:
/home/jcfr/Projects/Slicer-Qt5-VTK8/Base/QTCore/qSlicerCorePythonManager.h:25:39: fatal error: ctkAbstractPythonManager.h: No such file or directory
compilation terminated.
</code></pre>

---

## Post #16 by @Littlehhh (2019-04-18 15:17 UTC)

<p>Thank you so much, it works correctly now. so exciting.</p>

---

## Post #17 by @jhlegarreta (2023-07-29 15:10 UTC)

<p>Hello,<br>
I have run into the same issue:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5695300037/job/15438164734#step:6:21778" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@f5ad4d8 · GitHub</a><br>
while trying to turn off Python support:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5695300037/job/15438164734#step:6:2939" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@f5ad4d8 · GitHub</a></p>
<p>with the <code>HEAD</code> Slicer (e.g. <a href="https://github.com/Slicer/Slicer/commit/d13d03dce2d4e84f88a1b51289209d9bcefcd63a" class="inline-onebox" rel="noopener nofollow ugc">DOC: Update segmenteditor.md with info on node references · Slicer/Slicer@d13d03d · GitHub</a>).</p>
<p>Thus, I assume Python if necessary to build Slicer. Am I right?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> I am trying to turn off as many CLI modules as possible to speed up building, but I guess I need to keep them enabled to later build the <code>SlicerDMRI</code> module? Let me know if I’m wrong; if this is not necessary, the command line argument flag to disable them all would be <code>-DSlicer_CLIMODULES_DISABLED</code> ?</p>
<p>Otherwise, what would be the correct command line argument flag to turn off the e.g. <code>AddScalarVolumes</code> CLI: <code>-DSlicer_BUILD_AddScalarVolumes=OFF</code> ?</p>
<p>Thanks.</p>

---

## Post #18 by @pieper (2023-07-29 17:45 UTC)

<p>Slicer is meant to be buildable without python, but it’s not tested regularly so dependencies may creep in.  This is true of all cmake options that aren’t part of the standard preview builds, so changing any of the defaults may be expected to require some debugging.  Once you have the CI set up, maybe we also want to pick some build paths that we want to test on a regular basis using github actions.</p>
<p>BTW, it’s probably easier/faster to experiment using a big multi-core machine rather than using the CI machines.</p>

---

## Post #19 by @jhlegarreta (2023-07-30 01:18 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="17" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Thus, I assume Python if necessary to build Slicer. Am I right?</p>
</blockquote>
</aside>
<p>Removing <code>-DSlicer_USE_PYTHONQT=OFF</code> made the build past that point, so Python is necessary to build Slicer.</p>
<p>Past that point I run into</p>
<pre><code class="lang-auto">CMake Error at Libs/vtkTeem/CMakeLists.txt:151 (vtkMacroKitPythonWrap):
  Unknown CMake command "vtkMacroKitPythonWrap".
</code></pre>
<p>at:  <a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5701134575/job/15451559662#step:6:43108" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@a20943a · GitHub</a></p>
<p>Which was solved following:<br>
<a href="https://discourse.slicer.org/t/unknown-cmake-command-vtkmacrokitpythonwrap-in-snapshot-release-for-vtkteem/13838/4" class="inline-onebox">Unknown CMake command "vtkMacroKitPythonWrap" in snapshot release for vtkTeem - #4 by cpinter</a></p>
<p>Slicer looks to be building now:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5701565727/job/15452403081#step:6:1" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@35e3b27 · GitHub</a></p>

---

## Post #20 by @slicer365 (2023-07-30 13:15 UTC)

<p>Yes, it is, but there is also a problem. For example, I want to change the name of my custom software. It seems that it should be rebuilt.Is there any way that I can change the name of the entire software without rebuilding?</p>

---

## Post #21 by @lassoan (2023-07-30 13:48 UTC)

<p>Thanks a lot for these tests and feedbacks, they are very useful.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="19" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>so Python is necessary to build Slicer.</p>
</blockquote>
</aside>
<p>Python is not required to build Slicer. If you get a build error when Python is turned off then that is a bug that we’ll fix. It would be nice if you could submit a bug report to track it.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="19" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Past that point I run into</p>
<pre><code class="lang-auto">CMake Error at Libs/vtkTeem/CMakeLists.txt:151 (vtkMacroKitPythonWrap):
  Unknown CMake command "vtkMacroKitPythonWrap".
</code></pre>
</blockquote>
</aside>
<p>vtkAddon is a required dependency. Have you somewhere disabled vtkAddon? Or it was missed from some extension/module template or the custom application template?</p>
<aside class="quote no-group" data-username="slicer365" data-post="20" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>For example, I want to change the name of my custom software</p>
</blockquote>
</aside>
<p>Making some parameters modifiable without rebuild or even starting from a clean build may require very significant amount of development work. In cases where the parameter is not meant to be frequently modified, requiring a rebuild is reasonable.</p>
<p>Do you have a good use case for frequently changing the application name? Do you find that a top-level build after changing the CMake variable is not sufficient to change the application name?</p>

---

## Post #22 by @slicer365 (2023-07-30 13:58 UTC)

<p>In fact, I may help users develop different slicer-based software, but the basic functions of these software are the same, and of course there are some things that need to be changed.<br>
And the name of each software is different, because it is developed for different users, but in order to change the name of the software, I need to recompile the whole program, which is really a waste of time.<br>
I tried to change the cmake file, but it didn’t work.</p>

---

## Post #23 by @pieper (2023-07-30 14:04 UTC)

<p>thanks for the feedback on your use cases <a class="mention" href="/u/slicer365">@slicer365</a>.</p>
<p>An alternative to consider is different launch scripts for different customized Slicer versions.  The launch script can have a custom name, but re-use the Slicer system under the hood.  If people develop only using Python they don’t even need to compile Slicer at all.</p>
<p>It’s true that rebuilding from scratch can be time consuming, but adding more configuration options makes it harder to test and therefore more likely that people will experience build failures.</p>

---

## Post #24 by @lassoan (2023-07-30 14:09 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="22" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>, I may help users develop different slicer-based software</p>
</blockquote>
</aside>
<p>In this case I would recommend to maintain a separate build tree for each application.</p>
<p>If you need very fast build then you can consider switching to use Linux, as default build tools on Linux can do parallel builds correctly and very efficiently. With a 3-year-old computer with i9 CPU and fast disk, Slicer is built from scratch (not a rebuild but a clean build from source, with all dependencies) in 30 minutes. Rebuild after some CMake variable changes may take a minute or so.</p>

---

## Post #25 by @jhlegarreta (2023-07-30 17:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Python is not required to build Slicer. If you get a build error when Python is turned off then that is a bug that we’ll fix. It would be nice if you could submit a bug report to track it.</p>
</blockquote>
</aside>
<p><a href="https://github.com/Slicer/Slicer/issues/7136" class="inline-onebox" rel="noopener nofollow ugc">Slicer build fails if `Slicer_USE_PYTHONQT` is turned off · Issue #7136 · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>vtkAddon is a required dependency. Have you somewhere disabled vtkAddon? Or it was missed from some extension/module template or the custom application template?</p>
</blockquote>
</aside>
<p>I turned it off. If it is required, then wondering why it should be exposed/users can turn it off:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5701134575/job/15451559662#step:6:24" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@a20943a · GitHub</a></p>
<p>Build failure:<br>
<a href="https://github.com/jhlegarreta/SlicerDMRI/actions/runs/5701134575/job/15451559662#step:6:43108" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add GitHub actions build, test workflow file for CI · jhlegarreta/SlicerDMRI@a20943a · GitHub</a></p>

---

## Post #26 by @lassoan (2023-07-30 18:08 UTC)

<p>Thanks for submitting the issue.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="25" data-topic="6523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>If it is required, then wondering why it should be exposed/users can turn it off</p>
</blockquote>
</aside>
<p>I don’t think there should be a build option for it, as it contains code that should be part of VTK, which is a required dependency. <a class="mention" href="/u/jcfr">@jcfr</a> is there a specific reason for having a <code>Slicer_BUILD_vtkAddon</code> build option?</p>

---
