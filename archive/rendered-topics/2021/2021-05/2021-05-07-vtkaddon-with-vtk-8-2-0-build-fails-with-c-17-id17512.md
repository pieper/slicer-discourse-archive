# vtkAddon with VTK 8.2.0 build fails with C++17

**Topic ID**: 17512
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/vtkaddon-with-vtk-8-2-0-build-fails-with-c-17/17512

---

## Post #1 by @keri (2021-05-07 18:56 UTC)

<p>Hi,</p>
<p>VTK 8.2.0 in <code>VTK/Common/Core/vtkMath.h</code> needs to have the following include:</p>
<pre><code class="lang-cpp">#include &lt;algorithm&gt; // for std::clamp
</code></pre>
<p>aimed to support <code>C++17</code> (and higher).</p>
<p>With MSVC I used to successfully compile Slicer with C++17 but now I’m working on Ubuntu and the build fails with error (GCC 9.3):</p>
<pre><code class="lang-cpp">In file included from /vtkAddon/vtkOrientedBSplineTransform.cxx:13:
/VTK/Common/Core/vtkMath.h: In static member function ‘static T vtkMath::ClampValue(const T&amp;, const T&amp;, const T&amp;)’:
/VTK/Common/Core/vtkMath.h:1516:15: error: ‘clamp’ is not a member of ‘std’
 1516 |   return std::clamp(value, min, max);
      |               ^~~~~
make[2]: *** [CMakeFiles/vtkAddon.dir/build.make:121: CMakeFiles/vtkAddon.dir/vtkOrientedBSplineTransform.cxx.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:95: CMakeFiles/vtkAddon.dir/all] Error 2
make: *** [Makefile:149: all] Error 2
</code></pre>
<p>By the way <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Common/Core/vtkMath.h#L51" rel="noopener nofollow ugc">VTK 9 has fixed this</a></p>

---

## Post #2 by @lassoan (2021-05-07 20:26 UTC)

<p>Thanks for reporting this. In Slicer, we don’t support building VTK8.2 with C++17 (C++17 is disabled in Slicer superbuild), so they do not have to be compatible, but the change you suggest is harmless, so if you submit a pull request to vtkAddon then we’ll merge it.</p>

---

## Post #3 by @keri (2021-05-07 20:36 UTC)

<p>In best scenario I should push a PR to VTK 8.2.0 as <code>#include &lt;algorithm&gt;</code> should normally reside there.<br>
Less accurate decision is probably to put <code>#include &lt;algorithm&gt;</code> before including <code>vtkMath.h</code> in <code>vtkAddon</code>.</p>
<p>I don’t know (I’m not much experienced git user) is it possible to push PR to VTK 8.2.0 (or is it worth it?)?<br>
If not I will try to push PR to <code>vtkAddon</code></p>

---

## Post #4 by @keri (2021-05-08 11:54 UTC)

<p>I decided to <a href="https://github.com/Slicer/vtkAddon/pull/21" rel="noopener nofollow ugc">make PR to vtkAddon</a></p>

---

## Post #5 by @jamesobutler (2021-05-08 12:05 UTC)

<p>Reading <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/17615" class="inline-onebox" rel="noopener nofollow ugc">VTK 8.2 does not compile with c++17 (#17615) · Issues · VTK / VTK · GitLab</a>, it appears that VTK 8.2 never was explicitly supporting C++17.</p>
<p>Is there a reason you are not building Slicer with VTK9 where it does not have this issue with C++17? The Slicer preview builds are already using VTK9 well. If you are building a Slicer custom application or building Slicer from source you would just need to set the VTK version to use as “9” instead of the default “8”.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Should the default Slicer build option for VTK be switched to “9” now? Most VTK9 related issues have been resolved and since it is used in the Slicer preview packages now it is likely worthy of being the default CMake option?</p>

---

## Post #6 by @keri (2021-05-08 14:16 UTC)

<p>Hi,</p>
<p>Thank you for information.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="17512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Is there a reason you are not building Slicer with VTK9 where it does not have this issue with C++17?</p>
</blockquote>
</aside>
<p>Actually I would prefer VTK 9, but when I’m trying to force VTK 9 in SlicerCAT with the line-code in my CMakeLists.txt:</p>
<pre data-code-wrap="bash"><code class="lang-bash">set(Slicer_VTK_VERSION_MAJOR 9) # or set(Slicer_VTK_VERSION_MAJOR:STRING "9")
</code></pre>
<p>I can see that Slicer still builds VTK 8.2.0. So for now I just tried to fix VTK 8.2.0 bug and in the near future I will try to investigate why I can’t build it against VTK 9.</p>
<p>I took a first look how <code>External_VTK.cmake</code> works:</p>
<pre data-code-wrap="bash"><code class="lang-bash">  if("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "8")

    set(_git_tag "97904fdcc7e73446b3131f32eac9fc9781b23c2d") # slicer-v8.2.0-2018-10-02-74d9488523

    set(vtk_egg_info_version "8.2.0")

  elseif("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "9")

    set(_git_tag "f3c1a72fbf0f7287575ae876efced9c85776d9b4") # slicer-v9.0.20201111-733234c785

    set(vtk_egg_info_version "9.0.20201111")

  else()

    message(FATAL_ERROR "error: Unsupported Slicer_VTK_VERSION_MAJOR: ${Slicer_VTK_VERSION_MAJOR}")

  endif()
</code></pre>
<p>and it is quite straghtforward. But as I said SlicerCAT have built VTK 8.2.0 for me.</p>

---

## Post #7 by @jamesobutler (2021-05-08 16:24 UTC)

<p>You will need to make sure your SlicerCAT is using the latest Slicer repo git hash and then you can select Slicer_VTK_VERSION_MAJOR as “9” and it should build well. If you are using an earlier Slicer git hash version that could’ve been when VTK9 support wasn’t working appropriately.</p>
<p>You should keep the VTK git hash version that Slicer specified in External_VTK which is a specific Slicer fork of VTK.</p>

---

## Post #8 by @lassoan (2021-05-09 15:17 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="17512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Should the default Slicer build option for VTK be switched to “9” now? Most VTK9 related issues have been resolved and since it is used in the Slicer preview packages now it is likely worthy of being the default CMake option?</p>
</blockquote>
</aside>
<p>Good point. I’ve submitted a pull request to change the default VTK version to 9:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5633">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5633" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/5633" target="_blank" rel="noopener">ENH: Set default VTK version to 9</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:use-vtk9-by-default</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-09" data-time="15:15:36" data-timezone="UTC">03:15PM - 09 May 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/5633/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Slicer Preview Releases are built with VTK9 and there are no major issues, there<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5633" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">fore we update the default VTK version to 9.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
