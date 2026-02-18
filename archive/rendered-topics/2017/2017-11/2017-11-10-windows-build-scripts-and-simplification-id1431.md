# Windows build scripts and simplification

**Topic ID**: 1431
**Date**: 2017-11-10
**URL**: https://discourse.slicer.org/t/windows-build-scripts-and-simplification/1431

---

## Post #1 by @ihnorton (2017-11-10 12:45 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="15" data-topic="1411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"><a href="https://discourse.slicer.org/t/build-error-pythonqt-visual-studio-2015-qt-5-9-2/1411/15">Build Error PythonQt Visual Studio 2015 Qt 5.9.2</a></div>
<blockquote>
<p>For some time  I have been thinking about creating a “SlicerDevelopmentEnvironment” project on GitHub where we would keep:</p>
<p>This would ne lightweight and allow to store:</p>
<p>batch/shell script to build Slicer<br>
and other misc scripts</p>
<p>Or we could commit batch script directly to Slicer repo.</p>
<p>Here is what was done for ITK: <a href="https://github.com/InsightSoftwareConsortium/ITKDevelopmentEnvironment" class="inline-onebox">GitHub - InsightSoftwareConsortium/ITKDevelopmentEnvironment: A repository of scripts to set up an ITK development environment.</a></p>
</blockquote>
</aside>
<p>In-repo sounds fine for a <code>quickbuild.bat</code> type of script, but remember that this will add another layer of indirection and potential confusion (“I tried the quickbuild.bat but it kept rebuilding everything from scratch and failing after 3 hours! Then I tried the superbuild instructions directly”, etc.).</p>
<p>I think providing a link (or automatic download) of correct Qt binaries would go further to simplify the development process on Windows. The current 5.9.2 official binaries ship both release and debug DLLs + PDBs, however Creator and Designer appear to only be built in release <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20">.</p>
<p>Probably best to keep Docker scripts outside of the repository as they are now.</p>

---

## Post #2 by @lassoan (2017-11-10 13:38 UTC)

<p>I agree that it would be better not to add one more automation layer on top of CMake for building Slicer on a developer computer (fully automated Docker builds is a different story). To make the build process more robust, I would prefer to improve CMake scripts and/or documentation.</p>

---

## Post #3 by @jcfr (2017-11-10 14:27 UTC)

<blockquote>
<p>I would prefer to improve CMake scripts and/or documentation.</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>Regarding CMake improvement, it is a matter of finding:</p>
<ul>
<li>time to move the patch forward and implement tests</li>
<li>the right trade-off between feature creep</li>
</ul>
<p>That said, I have been quite successful in adding and improving features (e.g improved support for cross compilation initiated by  <a class="mention" href="/u/thewtex">@thewtex</a>, …)</p>

---

## Post #4 by @thewtex (2017-11-10 15:01 UTC)

<p>For ITK GitHub CI builds, we are investigating Docker Windows images in addition to Docker Linux images. It looks compelling.</p>

---
