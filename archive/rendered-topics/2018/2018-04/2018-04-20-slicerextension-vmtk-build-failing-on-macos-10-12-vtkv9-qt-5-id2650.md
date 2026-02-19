---
topic_id: 2650
title: "Slicerextension Vmtk Build Failing On Macos 10 12 Vtkv9 Qt 5"
date: 2018-04-20
url: https://discourse.slicer.org/t/2650
---

# SlicerExtension-VMTK build failing on MacOS 10.12, VTKv9, Qt 5.10

**Topic ID**: 2650
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/slicerextension-vmtk-build-failing-on-macos-10-12-vtkv9-qt-5-10/2650

---

## Post #1 by @mschumaker (2018-04-20 18:30 UTC)

<p>I’m attempting to build SlicerExtension-VMTK in my Slicer-SuperBuild directory, configuring using CMake 3.11 and using makefiles, and I encounter an error with the VMTK build step:</p>
<pre><code>[  1%] Built target vtkvmtkITK
make[5]: *** No rule to make target `/short/Slicer-SuperBuild/SlicerExtension-VMTK-build/VMTK/vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKHierarchy', needed by `vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKArchetypeImageSeriesReaderPython.cxx'.  Stop.
make[4]: *** [vtkVmtk/Utilities/vtkvmtkITK/CMakeFiles/vtkvmtkITKPythonD.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [VMTK-prefix/src/VMTK-stamp/VMTK-build] Error 2
make[1]: *** [CMakeFiles/VMTK.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>I don’t see any file or directory named vtkvmtkITKHierarchy, so is this an old reference?<br>
Also, I noticed that the script is cloning the VMTK files from <a href="http://gitHub.com/rlizzo/vmtk.git" rel="nofollow noopener">gitHub.com/rlizzo/vmtk.git</a>, rather than <a href="http://github.com/vmtk/vmtk.git" rel="nofollow noopener">github.com/vmtk/vmtk.git</a>. Is there a reason for this?<br>
Any help or advice would be appreciated.</p>

---

## Post #2 by @mschumaker (2018-04-20 18:59 UTC)

<p>I just noticed the open issue on the repository. Is there any workaround I can use?</p><aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK/issues/11">
  <header class="source">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/11" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/SlicerExtension-VMTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/issues/11" target="_blank" rel="noopener nofollow ugc">Slicer extension packaging fails on MacOSX</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2017-10-25" data-time="01:55:04" data-timezone="UTC">01:55AM - 25 Oct 17 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2018-08-07" data-time="16:03:41" data-timezone="UTC">04:03PM - 07 Aug 18 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">See https://discourse.slicer.org/t/vmtk-vessel-filtering-not-working/1263/7</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2018-04-21 19:14 UTC)

<p>Maybe <a class="mention" href="/u/jcfr">@jcfr</a> can help.</p>

---

## Post #4 by @mschumaker (2018-06-13 15:01 UTC)

<p>It looks like this specific problem I was having related to compiling the VMTK package itself. I cloned the vmtk/vmtk.git master branch, turned off USE_SYSTEM_ITK and USE_SYSTEM_VTK, let it install its own ITK 4.13.0 and VTK 8.1.0, and it was able to complete the compilation. I’m not sure if that’s because of referencing problems, or inability to compile VMTK with VTK 9. I haven’t tried compiling SlicerExtension-VMTK again yet.</p>
<p>Also, <a class="mention" href="/u/jcfr">@jcfr</a>, I noticed in the Slicer ExtensionsIndex, <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerVMTK.s4ext" rel="nofollow noopener">https://github.com/Slicer/ExtensionsIndex/blob/master/SlicerVMTK.s4ext</a>, you’ve set the repository reference to be your own fork: <a href="https://github.com/jcfr/SlicerExtension-VMTK" rel="nofollow noopener">https://github.com/jcfr/SlicerExtension-VMTK</a>, revision 5013f532b398f7c9a983bdf65a175ec41ce3292a, but you didn’t do a pull request back to vmtk/SlicerExtension-VMTK. Is there a reason for that?</p>

---

## Post #5 by @jcfr (2018-06-13 15:18 UTC)

<blockquote>
<p>repository reference to be your own fork … Is there a reason for that?</p>
</blockquote>
<p>The exact reference is this on <a href="https://github.com/jcfr/SlicerExtension-VMTK/commits/fix-macos-packaging">https://github.com/jcfr/SlicerExtension-VMTK/commits/fix-macos-packaging</a></p>
<p>I don’t recall the specific. It should probably be integrated back into master.</p>

---

## Post #6 by @jcfr (2018-06-13 15:19 UTC)

<blockquote>
<p>turned off USE_SYSTEM_ITK and USE_SYSTEM_VTK</p>
</blockquote>
<p>VMTK should definitively build against the VTK and ITK provided by Slicer.</p>

---

## Post #7 by @mschumaker (2018-06-13 15:21 UTC)

<blockquote>
<p>VMTK should definitively build against the VTK and ITK provided by Slicer.</p>
</blockquote>
<p>Agreed. I couldn’t get it to do that, so I tried building it on its own separately to figure out what the problem was.</p>

---

## Post #8 by @jcfr (2018-06-13 15:23 UTC)

<p>Also, there are some changes in my fork of VMTK that should be integrated upstream too:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/jcfr/SlicerExtension-VMTK/blob/5013f532b398f7c9a983bdf65a175ec41ce3292a/SuperBuild/External_VMTK.cmake#L26-L30" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/jcfr/SlicerExtension-VMTK/blob/5013f532b398f7c9a983bdf65a175ec41ce3292a/SuperBuild/External_VMTK.cmake#L26-L30" target="_blank">jcfr/SlicerExtension-VMTK/blob/5013f532b398f7c9a983bdf65a175ec41ce3292a/SuperBuild/External_VMTK.cmake#L26-L30</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="26" style="counter-reset: li-counter 25 ;">
<li>#GIT_REPOSITORY "${git_protocol}://github.com/vmtk/vmtk.git"</li>
<li>#GIT_TAG "master"</li>
<li># Use this repository/branch to test changes using nightly builds:</li>
<li>GIT_REPOSITORY "${git_protocol}://github.com/jcfr/vmtk"</li>
<li>GIT_TAG "2b2b250a6da6717270af96ebc6fbfa357dd4ec5c"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @jcfr (2018-06-13 15:30 UTC)

<p>Good news is that all my changes made it to vmtk master</p>

---

## Post #10 by @mschumaker (2018-06-13 15:40 UTC)

<blockquote>
<p>Good news is that all my changes made it to vmtk master</p>
</blockquote>
<p>Ok, thanks. Yes, I see them when I look for your commits to vmtk.<br>
Thanks for committing the SlicerExtension-VMTK changes. It looks like External_VMTK.cmake is still referencing your vmtk fork, though. That may be part of the merge conflict git is complaining about.</p>

---

## Post #11 by @mschumaker (2018-06-13 15:51 UTC)

<p>Fantastic, thanks. Should I try compiling this with VTK9, or will I need to re-compile slicer with VTK8?</p>
<p>Ok, I tried it with VTK9, and the VMTK build is still failing in the same place.</p>

---

## Post #12 by @jcfr (2018-06-13 16:05 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="11" data-topic="2650">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Should I try compiling this with VTK9, or will I need to re-compile slicer with VTK8?</p>
</blockquote>
</aside>
<p>By configuring the extension using a Slicer build tree built using Qt5, VTKv9 will also be used:</p>
<pre><code class="lang-auto">$ echo $Slicer_Qt5_DIR 
/home/jcfr/Projects/Slicer-Qt5-VTK9-Release/Slicer-build

$ cd /tmp
$ git clone git://github.com/vmtk/SlicerExtension-VMTK.git

$ mkdir SlicerExtension-VMTK-build  &amp;&amp; cd $_
$ cmake -DSlicer_DIR:PATH=${Slicer_Qt5_DIR} ../SlicerExtension-VMTK
</code></pre>

---

## Post #13 by @jcfr (2018-06-13 16:06 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="11" data-topic="2650">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>I tried it with VTK9, and the VMTK build is still failing in the same place.</p>
</blockquote>
</aside>
<p>Do you get an error like this one:</p>
<pre><code class="lang-auto">[  2%] Built target tet
make[5]: *** No rule to make target '/tmp/SlicerExtension-VMTK-build/VMTK/vtkVmtk/Common/vtkvmtkCommonHierarchy', needed by 'vtkVmtk/Common/vtkvmtkMathPython.cxx'.  Stop.
make[5]: *** Waiting for unfinished jobs....
[  3%] Python Wrapping - generating vtkvmtkCommonPythonInit.cxx
CMakeFiles/Makefile2:528: recipe for target 'vtkVmtk/Common/CMakeFiles/vtkvmtkCommonPythonD.dir/all' failed
make[4]: *** [vtkVmtk/Common/CMakeFiles/vtkvmtkCommonPythonD.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....

</code></pre>

---

## Post #14 by @mschumaker (2018-06-13 16:07 UTC)

<p>Yes, that’s the same place mine is failing:</p>
<pre><code>make[5]: *** No rule to make target `/short/testing/SlicerExtension-VMTK-Build/VMTK/vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKHierarchy', needed by `vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKArchetypeImageSeriesReaderPython.cxx'.  Stop.
make[4]: *** [vtkVmtk/Utilities/vtkvmtkITK/CMakeFiles/vtkvmtkITKPythonD.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [VMTK-prefix/src/VMTK-stamp/VMTK-build] Error 2
make[1]: *** [CMakeFiles/VMTK.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>Or close enough, anyway.</p>

---

## Post #15 by @mschumaker (2018-06-13 16:14 UTC)

<blockquote>
<p>By configuring the extension using a Slicer build tree built using Qt5, VTKv9 will also be used</p>
</blockquote>
<p>I built with Qt5, and VTK9. I think I rebuilt Slicer last week.</p>
<p>Thanks for your help, I appreciate it.</p>

---

## Post #16 by @jcfr (2018-06-13 18:44 UTC)

<p>The problem seems to be specific to VMTK itself.</p>
<p>I suspect that (1) building VTMTK against VTK9 will also fail and (2) backporting  <a href="https://github.com/Slicer/Slicer/blob/master/CMake/vtkMacroKitPythonWrap.cmake">Slicer/CMake/vtkMacroKitPythonWrap.cmake</a> module to VMTK should help address the problem.</p>

---

## Post #17 by @mschumaker (2018-06-13 19:13 UTC)

<blockquote>
<p>The problem seems to be specific to VMTK itself.</p>
<p>I suspect that (1) building VTMTK against VTK9 will also fail and (2) backporting Slicer/CMake/vtkMacroKitPythonWrap.cmake module to VMTK should help address the problem.</p>
</blockquote>
<p>Thanks for investigating. I’m not sure how to backport Slicer/CMake/vtkMacroKitPythonWrap.cmake, but I can add an issue to the VMTK page requesting VTK9 compatibility.</p>

---

## Post #18 by @Fernando (2018-06-22 15:45 UTC)

<p>I can’t find VMTK in the Extensions Manager:</p>
<pre><code class="lang-auto">No extensions found for win:64-bit, revision: '27261'. Please try a different combination
</code></pre>
<p>Is the error related to this thread?</p>

---

## Post #19 by @mschumaker (2018-06-22 17:14 UTC)

<p>It is. We figured out that the base VMTK package used by the Slicer extension is not able to build with VTK9, which is part of the Slicer build with Qt5. I looked through the nightly build record, and the Slicer VMTK extension has never compiled with the Qt5 SlicerPreview.<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-06-12&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-06-12&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a><br>
I submitted a feature request on the VMTK repository about VTK9 compatibility, but I think the person that could respond to that is on vacation. Or, for some reason, he hasn’t looked at the repository for two weeks.</p>

---

## Post #20 by @lassoan (2018-06-22 18:10 UTC)

<p>You could add comment to the VMTK pull request at least once a week, to show that it is still a problem that requires attention.</p>

---

## Post #21 by @Fernando (2018-06-27 13:00 UTC)

<p>Do you know which is the latest Slicer revision on which VMTK works / how I can figure it out?</p>

---

## Post #22 by @mschumaker (2018-06-27 17:24 UTC)

<p>You can look at the build and testing record for Slicer and extensions at <a href="http://slicer.cdash.org/viewProjects.php" rel="nofollow noopener">http://slicer.cdash.org/viewProjects.php</a>. Open the tools, click Show Filters, and search for the Build Name VMTK. The Slicer4 project uses Qt4.8, and there are successful builds of the VMTK extension there (the Qt5 build is SlicerPreview). The latest ones haven’t built properly because there is a pending pull request at vmtk/SlicerExtension-VMTK that someone needs to review and accept. The last successful build of the extension was on June 13:<br>
<a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-06-13&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-06-13&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>

---

## Post #23 by @mschumaker (2018-06-27 18:52 UTC)

<p>Here’s where I posted about VTK9 compatibility for VMTK. Feel free to add comments expressing your interest.<br>
<a href="https://groups.google.com/forum/#!topic/vmtk-users/rhMaE8W8oi0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://groups.google.com/forum/#!topic/vmtk-users/rhMaE8W8oi0</a></p><aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/vmtk/issues/308">
  <header class="source">

      <a href="https://github.com/vmtk/vmtk/issues/308" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/vmtk</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/vmtk/issues/308" target="_blank" rel="noopener nofollow ugc">VTK9 compatibility of VMTK, for SlicerExtension-VMTK with Qt5 Slicer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-06-13" data-time="20:13:44" data-timezone="UTC">08:13PM - 13 Jun 18 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2018-08-17" data-time="08:47:24" data-timezone="UTC">08:47AM - 17 Aug 18 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mschumak" target="_blank" rel="noopener nofollow ugc">
          <img alt="mschumak" src="https://avatars.githubusercontent.com/u/3884360?v=4" class="onebox-avatar-inline" width="20" height="20">
          mschumak
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'd like to request investigating VTK9 compatibility of VMTK, in anticipation of<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> their stable release. The reason I'm requesting this is to be able to compile SlicerExtension-VMTK with macOS 10.12 and 10.13, which no longer support Qt4. 3D Slicer has introduced a Qt5-compatible version, but it requires VTK9. I've found that I can compile VMTK with 8.1, but I get a build error when trying it with the same VTK version as my Slicer build:

```
[ 37%] Performing build step for 'VMTK'
[  0%] Built target nl
[  1%] Built target vtkvmtkITK
make[5]: *** No rule to make target `/short/testing/SlicerExtension-VMTK-Build/VMTK/vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKHierarchy', needed by `vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKArchetypeImageSeriesReaderPython.cxx'.  Stop.
make[4]: *** [vtkVmtk/Utilities/vtkvmtkITK/CMakeFiles/vtkvmtkITKPythonD.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [VMTK-prefix/src/VMTK-stamp/VMTK-build] Error 2
make[1]: *** [CMakeFiles/VMTK.dir/all] Error 2
make: *** [all] Error 2

```

 I've discussed this with @jcfr, and he's found a similar error. He's submitted a pull request that will fix other macOS issues with SlicerExtension-VMTK, but to keep up with current Slicer development, VTK9 compatibility is needed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #24 by @mschumaker (2018-07-05 14:46 UTC)

<p>I’ve submitted a pull request to the Slicer ExtensionsIndex, so that SlicerVMTK is fetched from vmtk/SlicerExtension-VMTK. At the moment, it’s still trying to fetch from a deleted branch of <a class="mention" href="/u/jcfr">@jcfr</a>’s repository, and failing. I don’t have Write permission - could someone review and accept it? Or may I have Write permission?</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/ExtensionsIndex/pull/1561">
  <header class="source">

      <a href="https://github.com/Slicer/ExtensionsIndex/pull/1561" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/ExtensionsIndex</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/ExtensionsIndex/pull/1561" target="_blank" rel="noopener nofollow ugc">SlicerVMTK source set to github.com/vmtk</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>mschumak:Jun12-VMTK-edit</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-06-28" data-time="14:48:23" data-timezone="UTC">02:48PM - 28 Jun 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/mschumak" target="_blank" rel="noopener nofollow ugc">
            <img alt="mschumak" src="https://avatars.githubusercontent.com/u/3884360?v=4" class="onebox-avatar-inline" width="20" height="20">
            mschumak
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 2 additions and 2 deletions">
          <a href="https://github.com/Slicer/ExtensionsIndex/pull/1561/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The remote source for SlicerVMTK.s4ext was previously set to a personal reposito<span class="show-more-container"><a href="https://github.com/Slicer/ExtensionsIndex/pull/1561" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ry. Fixes have been made in the GitHub.com/vmtk/SlicerExtension-VMTK.git source, and so it can be the source for the extension's code.
This pull request changes the source code manager lines in SlicerVMTK.git to:
scmurl https://github.com/vmtk/SlicerExtension-VMTK
scmrevision master</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #25 by @mschumaker (2018-07-09 15:15 UTC)

<p>I’ve narrowed down what changes in VTK have led to problems compiling VMTK for SlicerPreview. The last VTK9 revision that results in a successful VMTK build was merged into master on Dec 13, 2017: c96fe3bca6bdb7df83252f8a443d8e0428cab956, “Merge branch ‘upstream-expat’ into update-expat”. The commit that follows it deals with vtkWrapHierarchy.</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Kitware/VTK/commit/de1e3d3baf6c90c331f413aa1dff040793968f15">
  <header class="source">

      <a href="https://github.com/Kitware/VTK/commit/de1e3d3baf6c90c331f413aa1dff040793968f15" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/VTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/VTK/commit/de1e3d3baf6c90c331f413aa1dff040793968f15" target="_blank" rel="noopener nofollow ugc">vtkWrapHierarchy: declare that the hierarchy file is an output</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-12-13" data-time="16:31:38" data-timezone="UTC">04:31PM - 13 Dec 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mathstuf" target="_blank" rel="noopener nofollow ugc">
          <img alt="mathstuf" src="https://avatars.githubusercontent.com/u/97253?v=4" class="onebox-avatar-inline" width="20" height="20">
          mathstuf
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 9 deletions">
        <a href="https://github.com/Kitware/VTK/commit/de1e3d3baf6c90c331f413aa1dff040793968f15" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+1</span>
          <span class="removed">-9</span>
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
<p>
For two days after that, I can’t get VTK itself to compile, then with revisions from Dec 15 onwards I get the error we’ve been seeing in the recent build attempts. <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, do you have any insight into why that change would cause problems, and how to address it? Thanks for any assistance.<br>
I wrote more about it in the last comments here:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/vmtk/vmtk/issues/308">
  <header class="source">

      <a href="https://github.com/vmtk/vmtk/issues/308" target="_blank" rel="noopener nofollow ugc">github.com/vmtk/vmtk</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/vmtk/vmtk/issues/308" target="_blank" rel="noopener nofollow ugc">VTK9 compatibility of VMTK, for SlicerExtension-VMTK with Qt5 Slicer</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2018-06-13" data-time="20:13:44" data-timezone="UTC">08:13PM - 13 Jun 18 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2018-08-17" data-time="08:47:24" data-timezone="UTC">08:47AM - 17 Aug 18 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/mschumak" target="_blank" rel="noopener nofollow ugc">
          <img alt="mschumak" src="https://avatars.githubusercontent.com/u/3884360?v=4" class="onebox-avatar-inline" width="20" height="20">
          mschumak
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I'd like to request investigating VTK9 compatibility of VMTK, in anticipation of<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> their stable release. The reason I'm requesting this is to be able to compile SlicerExtension-VMTK with macOS 10.12 and 10.13, which no longer support Qt4. 3D Slicer has introduced a Qt5-compatible version, but it requires VTK9. I've found that I can compile VMTK with 8.1, but I get a build error when trying it with the same VTK version as my Slicer build:

```
[ 37%] Performing build step for 'VMTK'
[  0%] Built target nl
[  1%] Built target vtkvmtkITK
make[5]: *** No rule to make target `/short/testing/SlicerExtension-VMTK-Build/VMTK/vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKHierarchy', needed by `vtkVmtk/Utilities/vtkvmtkITK/vtkvmtkITKArchetypeImageSeriesReaderPython.cxx'.  Stop.
make[4]: *** [vtkVmtk/Utilities/vtkvmtkITK/CMakeFiles/vtkvmtkITKPythonD.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [VMTK-prefix/src/VMTK-stamp/VMTK-build] Error 2
make[1]: *** [CMakeFiles/VMTK.dir/all] Error 2
make: *** [all] Error 2

```

 I've discussed this with @jcfr, and he's found a similar error. He's submitted a pull request that will fix other macOS issues with SlicerExtension-VMTK, but to keep up with current Slicer development, VTK9 compatibility is needed.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #26 by @jcfr (2018-07-20 02:35 UTC)

<p>Hi Folks,</p>
<p>To follow up with this, the build system of VMTK has been fixed and a PR has been submitted, it is currently waiting to be integrated:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/vmtk/vmtk/pull/313">
  <header class="source">

      <a href="https://github.com/vmtk/vmtk/pull/313" target="_blank" rel="noopener">github.com/vmtk/vmtk</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/vmtk/vmtk/pull/313" target="_blank" rel="noopener">Fix python wrapping with vtk9</a>
      </h4>

    <div class="branches">
      <code>vmtk:master</code> ← <code>jcfr:fix-python-wrapping-with-vtk9</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-07-17" data-time="17:41:46" data-timezone="UTC">05:41PM - 17 Jul 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jcfr" target="_blank" rel="noopener">
            <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
            jcfr
          </a>
        </div>

        <div class="lines" title="8 commits changed 8 files with 213 additions and 29 deletions">
          <a href="https://github.com/vmtk/vmtk/pull/313/files" target="_blank" rel="noopener">
            <span class="added">+213</span>
            <span class="removed">-29</span>
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

<p>In the process, we also discovered an  issue in <code>conda-build</code> which has also been fixed in the upstream project:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/conda/conda-build/pull/3027">
  <header class="source">

      <a href="https://github.com/conda/conda-build/pull/3027" target="_blank" rel="noopener">github.com/conda/conda-build</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/conda/conda-build/pull/3027" target="_blank" rel="noopener">fix test/requires being ignored when --no-copy-test-source-files</a>
      </h4>

    <div class="branches">
      <code>conda:master</code> ← <code>msarahan:no_include_test_files_drops_test_deps</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-07-19" data-time="17:24:51" data-timezone="UTC">05:24PM - 19 Jul 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/msarahan" target="_blank" rel="noopener">
            <img alt="msarahan" src="https://avatars.githubusercontent.com/u/38393?v=4" class="onebox-avatar-inline" width="20" height="20">
            msarahan
          </a>
        </div>

        <div class="lines" title="1 commits changed 7 files with 42 additions and 9 deletions">
          <a href="https://github.com/conda/conda-build/pull/3027/files" target="_blank" rel="noopener">
            <span class="added">+42</span>
            <span class="removed">-9</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">addresses https://github.com/vmtk/vmtk/pull/313#issuecomment-406146264

CC @jc<span class="show-more-container"><a href="https://github.com/conda/conda-build/pull/3027" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">fr</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/mschumaker">@mschumaker</a> Thanks for your patience</p>

---

## Post #27 by @mschumaker (2018-07-20 03:11 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Thanks so much for pursuing this! I appreciate your efforts.</p>

---
