---
topic_id: 10457
title: "Python Wrapping Some Elements Missing"
date: 2020-02-27
url: https://discourse.slicer.org/t/10457
---

# Python wrapping (some elements missing)

**Topic ID**: 10457
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/python-wrapping-some-elements-missing/10457

---

## Post #1 by @RafaelPalomar (2020-02-27 14:24 UTC)

<p>Hello,</p>
<p>I’m playing with building slicer with SLICER_SUPERBUILD=OFF and trying to get a modular and installable version of slicer in linux. So far, I managed to build the dependencies from the superbuild, 3D Slicer libs, 3D slicer app (without Slicer Launcher) including CLI and Python support. I build also the Slicer modules separately (not all-in or all-out as one would normally would)</p>
<p>Though I see all the *Python.so and the *PythonD.so files are generated (both for Slicer libraries and for the modules), I cannot access some MRML nodes (e.g., slicer.vtkMRMLSegmentEditorNode does not exist). However other nodes like slicer.vtkMRMLAbstractViewNode are avalable. It seems to me that the Slicer-Libs are wrapped and available properly but not the loadable modules.</p>
<p>I know this is a weird setup and very specific, but if anyone has any intuition on what should I be looking for or what could I test to find the problem, please let me know.</p>
<p>Best,<br>
Rafael.</p>

---

## Post #2 by @RafaelPalomar (2020-02-28 08:21 UTC)

<p>Maybe just to narrow down the question. What is the mechanism by which MRML nodes are added to the slicer python namespace? This would probably help me find the problem.</p>
<p>Thanks!</p>

---

## Post #3 by @RafaelPalomar (2020-02-28 13:11 UTC)

<p>Digging a little bit more…I see that</p>
<p><code>   import vtkSlicerSegmentationsModuleMRMLPython</code></p>
<p>works. Then trying</p>
<pre><code>vtkSlicerSegmentationsModuleMRMLPython.vtkMRMLSegmentEditorNode()
</code></pre>
<p>fails</p>
<pre><code>Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: this class cannot be instantiated</code></pre>

---

## Post #4 by @pieper (2020-02-28 15:25 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> -</p>
<p>This sounds like an interesting project - is your goal to be able to use standard vtk/itk/python linux packages to build Slicer?  This could be really helpful, but just FYI, we’ve been down this path before (it might still be possible to apt-get install Slicer version 3 on debian) but run into a lot of problems getting bug fixes and other updates into upstream packages.  Since all the code is under coninuous development, the Slicer build process requires we be able to build and distribute our own versions of dependencies in some cases.</p>
<p>That said, it sounds like you are on the right path.  Be sure all the libraries are in the python path, and also be careful about the order of importing.  As I recall if you don’t import in the correct sequence not all the subclass methods are instantiated for a class (you might <code>strace</code> the Slicer launcher process to see what all is being read in and in what sequence).</p>

---

## Post #5 by @RafaelPalomar (2020-02-28 16:00 UTC)

<p>Hello <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>thank you for the reply. Yes, that’s the main idea. I see that Slicer has the basic infrastructure to achieve this, is just that it has not been developed any further for very long time. Particularly, all the CMake plumbing related to the install tree.</p>
<p>I’ve been digging a little more and found that the <code>vtkSlicerSegmentationsModuleMRML_WRAP_DEPENDS</code> variable when I build the loadable modules separately lacks the following dependencies compared to the standard superbuild Slicer: <code>vtkAddon;vtkSegmentationCore;vtkTeem;vtkITK;FreeSurfer;MRMLCore;MRMLLogic;MRMLDisplayableManager;MRMLCLI;vtkSlicerSubjectHierarchyModuleLogic;SlicerBaseLogic;qSlicerBaseQTCLI</code> which I would think are needed to complete the implementation (parent classes). This might explain the error when trying to instantiate the MRML nodes and maybe (silently) causes the no inclusion in the slicer python namespace.</p>
<p>This is the last bit I need to get a workable version of Slicer integrated in the OS, so I hope I can solve it and we can discuss further on the next NA-MIC Week <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @pieper (2020-02-28 17:20 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="5" data-topic="10457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>This is the last bit I need to get a workable version of Slicer integrated in the OS, so I hope I can solve it and we can discuss further on the next NA-MIC Week <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>Excellent idea! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @RafaelPalomar (2020-03-02 13:08 UTC)

<p>Hello,</p>
<p>for reference, if anyone experience similar issues, the problem is related to what I exposed in my last post. Slicer does not install any xxxHierarchy.txt file these are needed in the install tree; in addition, the mapping of Slicer_WRAP_HIERARCHY_FILES_CONFIG variable with the right install paths is needed for the SlicerConfig.cmake file for the install tree.</p>
<p>The solution for me was to modify the  vtkMacroKitPythonWrap.cmake to install the generated hierarchy files, modify SlicerGenerateSlicerConfig.cmake to record the install path of the hierarchy files and register them in SlicerInstallConfig.cmake.in.<br>
(<a href="https://github.com/RafaelPalomar/Slicer/tree/systole-patches/Slicer" rel="nofollow noopener">https://github.com/RafaelPalomar/Slicer/tree/systole-patches/Slicer</a>).</p>
<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/jcfr">@jcfr</a> Based on the experience of this post, I think that a MRMLNode B, inheriting from a MRMLNode A which belongs to an external module, will not be wrapped in Python. For this to work in a build tree, a “ModuleConfig.cmake” file would be needed (I don’t think it exists now?). For an install tree I would advocate for a creation of a drop-in directory in the install tree where all the modules drop a configuration file exposing all the needed variables. Does this make any sense?</p>

---

## Post #8 by @pieper (2020-03-02 15:10 UTC)

<aside class="quote no-group" data-username="RafaelPalomar" data-post="7" data-topic="10457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar"> RafaelPalomar:</div>
<blockquote>
<p>For an install tree I would advocate for a creation of a drop-in directory in the install tree where all the modules drop a configuration file exposing all the needed variables. Does this make any sense?</p>
</blockquote>
</aside>
<p>Sounds good to me (but I haven’t looked at these things in a long time and I don’t know what current practices are on the VTK side.)</p>

---

## Post #9 by @lassoan (2020-03-03 02:50 UTC)

<p>I would recommend to first help with migrating Slicer to VTK-8.90 (VTK-9 preview) as Python wrapping is changed completely. For example, hierarchy files are not used anymore.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> how far did you get with updating Slicer to VTK-8.90?</p>

---

## Post #10 by @cpinter (2020-03-03 09:19 UTC)

<p>I haven’t had the chance to work on this since our last conversations<br>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/1312" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/1312" target="_blank">Build with vtk89</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>cpinter:build-with-vtk89</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-01-29" data-time="20:16:04" data-timezone="UTC">08:16PM - 29 Jan 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank">
          <img alt="cpinter" src="https://avatars0.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="6 commits changed 55 files with 1165 additions and 105 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/1312/files" target="_blank">
          <span class="added">+1165</span>
          <span class="removed">-105</span>
        </a>
      </div>
    </div>

  </div>
</div>
  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I think we are very close, just a few more issues to address.</p>

---

## Post #11 by @kayarre (2020-05-07 03:05 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> is there  an update on this effort. I am not sure what I am looking at when I follow that link provided.</p>

---

## Post #12 by @cpinter (2020-05-07 08:31 UTC)

<p>The link above is redirected to an unrelated issue. The original pull request belongs to the old repository, which has been renamed to SlicerGitSVNArchive, that’s why.</p>
<p>As far as I know <a class="mention" href="/u/jcfr">@jcfr</a> got some funding for the VTK update work, and probably will get to it as soon as he has capacity. This is the issue where you can follow the events and related commits: <a href="https://github.com/Slicer/Slicer/issues/4696">https://github.com/Slicer/Slicer/issues/4696</a></p>

---
