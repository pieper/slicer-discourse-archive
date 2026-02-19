---
topic_id: 9083
title: "Building Slicer With Latest Vtk"
date: 2019-11-08
url: https://discourse.slicer.org/t/9083
---

# Building slicer with latest VTK

**Topic ID**: 9083
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/building-slicer-with-latest-vtk/9083

---

## Post #1 by @lassoan (2019-11-08 14:49 UTC)

<p>More and more VTK problems are surfacing for which it is very hard to find the potential VTK patches that we could backport (virtual reality Qt widget, <a href="https://discourse.slicer.org/t/setting-of-markerstyle-does-not-work/9073/9">plot marker style issue</a>, etc.). So, it is time to bit the bullet and try to switch to the latest VTK master.</p>
<p>I tried it on Windows, quickly failed with vtkWrappingTools-8.90.lib not found, and asked help on VTK forum (see <a href="https://discourse.vtk.org/t/vtk-build-fails-cannot-open-input-file-lib-release-vtkwrappingtools-8-90-lib/2074">here</a>).</p>
<p>I’ll use this topic to give updates on my efforts and ask for help.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @pieper (2019-11-08 15:00 UTC)

<p>Makes sense - probably if you fix on windows the solutions should transfer to other platforms, but if you want me to try mac or linux builds let me know.</p>

---

## Post #3 by @lassoan (2019-11-08 15:21 UTC)

<p>Yes, it would be great if you could try it on Mac, too. I’ve pushed what I have now to a branch and submitted a pull request: <a href="https://github.com/Slicer/Slicer/pull/1252">https://github.com/Slicer/Slicer/pull/1252</a>. You can push changes directly to that branch (all maintainers should have write access).</p>

---

## Post #4 by @jcfr (2019-11-08 15:27 UTC)

<p>Agreed, the transition to latest VTK is long overdue.</p>
<p>I anticipate the following challenges:</p>
<ul>
<li>wrapping of our VTK classes, I don’t think the new VTK build system allows to externally wrap VTK classes without using the VTK build system (like what ParaView is doing)</li>
<li>building of extension like SlicerVR</li>
</ul>

---

## Post #5 by @lassoan (2019-11-08 15:39 UTC)

<p>VTK wrapping of external code may have been removed from VTK but it is reimplemented for example in vtkDICOM by David Gobbi: <a href="https://github.com/dgobbi/vtk-dicom/blob/master/CMakeLists.txt">https://github.com/dgobbi/vtk-dicom/blob/master/CMakeLists.txt</a>. It belongs into VTK, since this will be needed by many other libraries, but for now we can copy-paste the solution of vtkDICOM. Probably <a class="mention" href="/u/jcfr">@jcfr</a> we’ll need your help with this.</p>
<p>vtkOpenVR is a very special case, because it is a remote module with its source code stored in the VTK main repository. This “neither here nor there” state does not make much sense for me, maybe it is like this for Ken’s convenience, and maybe it has been changed since VTK-8.2. I guess it will either become a proper remote module (like spline reslicer or dicom) or a regular built-in VTK module. If it becomes a built-in module we lose the ability to do updates for stable releases and we’ll be forced to ship third-party DLLs with Slicer core. These limitations are tolerable, but it would be better if vtkOpenVR would simply become a remote module.</p>

---

## Post #6 by @lassoan (2019-11-09 23:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="9083">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I tried it on Windows, quickly failed with vtkWrappingTools-8.90.lib not found, and asked help on VTK forum (see <a href="https://discourse.vtk.org/t/vtk-build-fails-cannot-open-input-file-lib-release-vtkwrappingtools-8-90-lib/2074">here </a>).</p>
</blockquote>
</aside>
<p>This problem has been resolved (it was caused by a recent regression in VTK master - now fixed).</p>
<p>Next <a href="https://discourse.vtk.org/t/build-error-in-vtk-based-project-include-called-with-wrong-number-of-arguments-include-only-takes-one-file/2078">problem came up during CTK configuration</a>. It was due to VTK_USE_FILE not being generated at all (instead of creating a placeholder file). I’ll implement a check in CTK to only attempt to use the file for old VTK versions.</p>

---

## Post #7 by @lassoan (2019-11-11 19:31 UTC)

<p>It seems that vtkWrapPython.cmake and vtkWrapHierarchy.cmake files are gone in VTK-8.90 and it is replaced by <a href="https://github.com/Kitware/VTK/blob/master/CMake/vtkModuleWrapPython.cmake">vtkModuleWrapPython.cmake</a>, which can wrap complete modules.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> What do you think would be a good approach? I don’t think we would want to make all Slicer components VTK modules, so vtkModuleWrapPython would not be directly applicable. Should we copy-paste Python wrapper CMake scripts from VTK-8.2 to Slicer and maintain them?</p>
<p>I’ve asked on the VTK forum, too: <a href="https://discourse.vtk.org/t/vtkwrappython-disappeared-from-vtk-8-90/2084">https://discourse.vtk.org/t/vtkwrappython-disappeared-from-vtk-8-90/2084</a>.</p>

---

## Post #8 by @lassoan (2019-11-12 14:00 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> We need to make a decision about Python wrapping. Please review the option listed <a href="https://discourse.vtk.org/t/vtkwrappython-disappeared-from-vtk-8-90/2084/4">here</a> and add your comments. Thanks!</p>

---

## Post #9 by @cpinter (2020-01-31 20:11 UTC)

<p>My <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW33_2020_GranCanaria/Projects/VTKBuild/README.md">continuation</a> of <a class="mention" href="/u/lassoan">@lassoan</a>’s work can be found in this PR:<br>
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
<p>There are two errors, neither preventing Slicer build. However, there is an error about not finding a python dll on startup. At least a bit more work is needed.</p>

---

## Post #10 by @jcfr (2020-02-01 18:20 UTC)

<p>Thanks for the update <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="9083">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>here is an error about not finding a python dll on startup</p>
</blockquote>
</aside>
<p>If I recall, the issue was related to also passing <code>Python3_*</code> variables to external project expecting it. More details at <a href="https://github.com/Slicer/Slicer/pull/1312#issuecomment-581054327" class="inline-onebox">CLI - When module is entered - WidgetRepresentation should be reset to match associated node · Issue #1312 · Slicer/Slicer · GitHub</a></p>

---
