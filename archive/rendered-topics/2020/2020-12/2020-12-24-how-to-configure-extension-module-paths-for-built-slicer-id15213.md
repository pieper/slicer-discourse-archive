---
topic_id: 15213
title: "How To Configure Extension Module Paths For Built Slicer"
date: 2020-12-24
url: https://discourse.slicer.org/t/15213
---

# How to configure extension module paths for built Slicer?

**Topic ID**: 15213
**Date**: 2020-12-24
**URL**: https://discourse.slicer.org/t/how-to-configure-extension-module-paths-for-built-slicer/15213

---

## Post #1 by @tbillah (2020-12-24 15:22 UTC)

<p>Hello,</p>
<p>I built a Slicer from source and some extension modules. I have the following:</p>
<pre><code class="lang-auto">[tb571@pnl-z840-2 Slicer]$ ls build/Slicer-build/Slicer
build/Slicer-build/Slicer

[tb571@pnl-z840-2 SlicerExtensionsBuild]$ ls *-build/SlicerWith*
MarkupsToModel-build/SlicerWithMarkupsToModel
MarkupsToModel-build/SlicerWithMarkupsToModelLauncherSettings.ini

SegmentEditorExtraEffects-build/SlicerWithSegmentEditorExtraEffects
SegmentEditorExtraEffects-build/SlicerWithSegmentEditorExtraEffectsLauncherSettings.ini

SlicerFreeSurfer-build/SlicerWithSlicerFreeSurfer
SlicerFreeSurfer-build/SlicerWithSlicerFreeSurferLauncherSettings.ini

UKFTractography-build/SlicerWithUKFTractography
UKFTractography-build/SlicerWithUKFTractographyLauncherSettings.ini
</code></pre>
<p>Now how do I launch a Slicer knowledgeable of all the extension modules? In contrast, when I download a Slicer, it populated <code>~/.config/NA-MIC/Extension-28257.ini</code> that had knowledge of all the downloaded modules.</p>

---

## Post #2 by @pieper (2020-12-24 15:33 UTC)

<p>Hi <a class="mention" href="/u/tbillah">@tbillah</a> -</p>
<p>I find it easiest to just make a shell script that combines the extension builds and scripted modules I need and then I just customize it to add or remove things based on what I’m working on at the moment.</p>
<pre><code class="lang-auto">#!/bin/zsh

# run this from within build tree
LIB_PATH=$(pwd)/inner-build/lib/Slicer-4.13

SLICER_BUILD=/opt/sr/Slicer-build

SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk ${SLICER_BUILD}/Slicer  $* \
  --additional-module-paths \
    ${LIB_PATH}/cli-modules ${LIB_PATH}/qt-loadable-modules ${LIB_PATH}/qt-scripted-modules \
    |&amp; tee /tmp/log
</code></pre>

---

## Post #3 by @tbillah (2020-12-24 16:34 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="15213">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><code>LIB_PATH=$(pwd)/inner-build/lib/Slicer-4.13</code></p>
</blockquote>
</aside>
<p>So do I get that the above has to be repeated for all extension builds I need? For what it’s worth, <code>inner-build</code> directory exists for SlicerDMRI only. The rest of the modules I attached above follow <code>&lt;name&gt;-build/lib/Slicer-4.13</code> pattern.</p>

---

## Post #4 by @pieper (2020-12-24 16:45 UTC)

<aside class="quote no-group" data-username="tbillah" data-post="3" data-topic="15213">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>So do I get that the above has to be repeated for all extension builds I need?</p>
</blockquote>
</aside>
<p>Yes, if you go with the script approach you just set the appropriate lib dir as a variable and then duplicate the lines that add the three paths as needed.</p>

---

## Post #5 by @tbillah (2020-12-24 21:29 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I am trying to load the following modules:</p>
<pre data-code-wrap="vim"><code class="lang-vim">MarkupsToModel-build/lib/Slicer-4.13/qt-loadable-modules
SegmentEditorExtraEffects-build/lib/Slicer-4.13/qt-scripted-modules
SlicerFreeSurfer-build/lib/Slicer-4.13/qt-loadable-modules
UKFTractography-build/lib/Slicer-4.13/cli-modules
UKFTractography-build/lib/Slicer-4.13/qt-loadable-modules
UKFTractography-build/lib/Slicer-4.13/qt-scripted-modules
</code></pre>
<p>I am launching as you suggested:</p>
<pre data-code-wrap="vim"><code class="lang-vim">[tb571@pnl-z840-2 SlicerExtensionsBuild]$ ~/Downloads/Slicer/build/Slicer-build/Slicer --additional-module-paths `ls -d *-build/lib/Slicer-4.13/cli-modules *-build/lib/Slicer-4.13/qt-loadable-modules *-build/lib/Slicer-4.13/qt-scripted-modules`
</code></pre>
<p>However, I find the following errors in one of the log files:</p>
<pre data-code-wrap="vim"><code class="lang-vim">[DEBUG][Qt] 24.12.2020 16:20:35 [] (unknown:0) - Additional module paths ..: MarkupsToModel-build/lib/Slicer-4.13/qt-loadable-modules, SegmentEditorExtraEffects-build/lib/Slicer-4.13/qt-scripted-modules, SlicerFreeSurfer-build/lib/Slicer-4.13/qt-loadable-modules, UKFTractography-build/lib/Slicer-4.13/cli-modules, UKFTractography-build/lib/Slicer-4.13/qt-loadable-modules, UKFTractography-build/lib/Slicer-4.13/qt-scripted-modules
[CRITICAL][Qt] 24.12.2020 16:20:36 [] (unknown:0) -   Error(s):
    The shared library was not found.
[CRITICAL][Qt] 24.12.2020 16:20:36 [] (unknown:0) -   Error(s):
    The shared library was not found.
[CRITICAL][Qt] 24.12.2020 16:20:36 [] (unknown:0) -   Error(s):
    The shared library was not found.
</code></pre>
<p>I tried setting the following but didn’t help:</p>
<blockquote>
<p>export LD_LIBRARY_PATH=/home/tb571/Qt/5.12.3/gcc_64/lib</p>
</blockquote>
<p>I have been trying this for a while so any direction for rescue is appreciated. <img src="https://emoji.discourse-cdn.com/twitter/innocent.png?v=12" title=":innocent:" class="emoji" alt=":innocent:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2020-12-26 05:45 UTC)

<p>Extensions that provide additional shared libraries may need not just the module libraries but also additional folders in LibraryPath, Path, and PYTHONPATH. These are listed in the automatically generated <em>AdditionalLauncherSettings.ini</em> file in the extension’s build folder and can be used to launch Slicer with the extension (convenient for debugging and testing). However, if you add multiple extensions then you have other options:</p>
<ul>
<li>Option A: combine content of <em>AdditionalLauncherSettings.ini</em> files of all the extensions that you use, and use that as additional launcher settings for starting Slicer</li>
<li>Option B: package each extension and install the extension from file using Slicer’s Extensions Manager.</li>
<li>Option C: Use the <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">Slicer Custom Application template</a> to build Slicer and bundle a list of extensions with it.</li>
</ul>
<p>For development (when you often make small changes to the code and rebuild and run) option A typically works better, while for a custom Slicer setup options B and C may be better, as they robust and fully automatic (no need for manual merging of path lists).</p>

---

## Post #7 by @tbillah (2020-12-26 05:48 UTC)

<p>Yeah, I intuitively figured Option A from Steve’s idea. Will follow up with my progress.</p>
<p>The challenge I face is to make that Slicer available to everyone else in the lab. Otherwise, Option B would have been desired.</p>

---

## Post #8 by @lassoan (2020-12-26 16:45 UTC)

<p>You can also just copy extension files into bin and module folders in the Slicer install tree. There will be an even cleaner solution (where you can copy the extension package contents into a single subfolder in the Slicer install tree and all settings in that subfolder, too), which requires merging of <a href="https://github.com/Slicer/Slicer/pull/5029">this PR</a> (will happen soon).</p>

---

## Post #9 by @tbillah (2020-12-26 17:00 UTC)

<blockquote>
<p>You can also just copy extension files into bin and module folders in the Slicer install tree.</p>
</blockquote>
<p>Hi Andras, this is a nicer idea. However, this is the download tree I have:</p>
<details><summary>Downloaded slicer</summary>
<pre data-code-wrap="vim"><code class="lang-vim">Slicer-4.10.2-linux-amd64
├── bin
├── include
├── lib
├── libexec
├── resources
├── share
└── Slicer
</code></pre>
</details>
<p>where there is no <code>module</code> folder.</p>
<p>On the other hand, this is part of my build tree and there is neither <code>bin</code> nor <code>module</code> folder:</p>
<details><summary>Built Slicer</summary>
<pre><code class="lang-auto">[tb571@pnl-z840-2 Slicer]$ tree -L 1 build/
build/
├── BRAINSTools
├── BRAINSTools-prefix
├── bzip2
├── bzip2-build
├── bzip2-install
├── bzip2-prefix
├── CMakeCache.txt
├── CMakeDoxyfile.in
├── CMakeDoxygenDefaults.cmake
├── CMakeFiles
├── cmake_install.cmake
├── CompareVolumes
├── CompareVolumes-prefix
├── CTestCustom.cmake
├── CTestTestfile.cmake
├── CTK
├── CTKAPPLAUNCHER
├── CTKAppLauncher-0.1.27-linux-amd64.tar.gz
</code></pre>
</details>
<p>Could you be more specific about where I should copy these downloaded extension files?</p>
<pre data-code-wrap="vim"><code class="lang-vim">[tb571@grx05 .config]$ tree -L 2 NA-MIC/
NA-MIC/
├── Extensions-28257
│   ├── DiffusionQC
│   ├── DiffusionQC-icon.png
│   ├── DiffusionQC.s4ext
│   ├── MarkupsToModel
│   ├── MarkupsToModel-icon.png
│   ├── MarkupsToModel.s4ext
│   ├── SegmentEditorExtraEffects
│   ├── SegmentEditorExtraEffects-icon.png
│   ├── SegmentEditorExtraEffects.s4ext
│   ├── SlicerDMRI
│   ├── SlicerDMRI-icon.png
│   ├── SlicerDMRI.s4ext
│   ├── UKFTractography
│   ├── UKFTractography-icon.png
│   └── UKFTractography.s4ext
├── Slicer-28257.ini

</code></pre>

---
