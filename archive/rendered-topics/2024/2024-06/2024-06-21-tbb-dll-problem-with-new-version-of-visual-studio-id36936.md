---
topic_id: 36936
title: "Tbb Dll Problem With New Version Of Visual Studio"
date: 2024-06-21
url: https://discourse.slicer.org/t/36936
---

# TBB DLL problem with new version of Visual Studio

**Topic ID**: 36936
**Date**: 2024-06-21
**URL**: https://discourse.slicer.org/t/tbb-dll-problem-with-new-version-of-visual-studio/36936

---

## Post #1 by @cpinter (2024-06-21 09:53 UTC)

<p>Hi all,</p>
<p>I recently encountered something really strange, and since I saw this problem on three different machines, I think it is caused by the latest versions of Visual Studio.</p>
<p>If we build Slicer (in Debug or Release, occurs with both), although the splash screen shows up, this error appears, and then Slicer exits.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae30ef6e7cdf57a0c4893daccdf76658f0517f06.png" alt="Screenshot 2024-06-21 104356" data-base62-sha1="oQXVeP5YTKeX3zmnrfzHzVirXYG" width="398" height="150"></p>
<p>The superbuild tree contains files with such name<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a7a5718ff55e9947e9e4ccc5234d22c3acbdec9.png" data-download-href="/uploads/short-url/htumzFByrI23tGqpGlOllZ6EmWB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a7a5718ff55e9947e9e4ccc5234d22c3acbdec9.png" alt="image" data-base62-sha1="htumzFByrI23tGqpGlOllZ6EmWB" width="317" height="499" data-dominant-color="E0E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">365×574 7.16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I suspect is that the issue was introduced with an update of Visual Studio, because everything worked with MSVC compiler version 14.39.33519, but we had the TBB issue with version 14.40.33807.</p>
<p>Does anyone have any idea how to fix this? Thank you very much!</p>

---

## Post #2 by @cpinter (2024-06-21 11:51 UTC)

<p>An update: I thought the name of the folder was the same as the MSVC version, which for some reason isn’t. For example the folder<br>
<code>C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.35.32215</code> contains MSVC <code>19.35.32215.0</code>. The versions above correspond to the directory name.</p>

---

## Post #3 by @lassoan (2024-06-21 12:37 UTC)

<p>Does copying tbb123.dll into the folder that contains <code>SlicerApp-real.exe</code> fix the issue?</p>
<p>Does the issue occur only in the build tree or also in the install tree (if you create an install package)?</p>

---

## Post #4 by @jamesobutler (2024-06-21 14:00 UTC)

<p>There is some FindVcvars.cmake update stuff needed for VS 17.10 which has MSVC 1940.</p>
<p>It had been updated on the scikit-built side, but I’ve backported the required changes on the Slicer side. I haven’t tried yet if this is all that is needed to fix your issue, but definitely required for MSVC 1940 usage.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7815">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7815" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7815" target="_blank" rel="noopener nofollow ugc">ENH: Update FindVcvars for future MSVC versions</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:findvcvars-future-support</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-06-21" data-time="13:58:30" data-timezone="UTC">01:58PM - 21 Jun 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7815/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This is based on FindVcvars.cmake as of https://github.com/scikit-build/cmake-Fi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7815" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ndVcvars/commit/ccf29dc00cde21d78140b1b9698d6bf075b3ab76.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @cpinter (2024-06-21 16:30 UTC)

<p>Thanks a lot for the answers!</p>
<p>I tried different things, but to unblock the work I ended up rebuilding with the v142 toolset. It worked. But I messed up my v143 build tree, so to be able to help solve this issue (I know about at least one other person who had it) I started a new build with the problematic compiler version. I’ll report back on Monday.</p>
<p>Have a great weekend!</p>
<p>(<a class="mention" href="/u/jamesobutler">@jamesobutler</a> I’ll update and try!)</p>

---

## Post #6 by @RolandLau (2024-06-24 01:11 UTC)

<p>I tried using v142 toolset and v143 toolset 14.39.33519,both encountered this tbb12 dll issue.<br>
So I think this may not be a toolset version problem?</p>

---

## Post #7 by @sfrisken (2024-06-24 23:41 UTC)

<p>I get the same error trying to build with VS 2022. Has anyone been able to figure this out? I’m trying to build my first loadable module for Project week – should I install a different version of Visual Studio? If so, could you please tell me which one?</p>

---

## Post #8 by @cpinter (2024-06-25 09:01 UTC)

<p>v142 worked for me.</p>
<p>My latest clean v143 build also showed missing VTK OpenGL DLL issues, but I went ahead with updating Slicer as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> suggested, I’ll see if they disappear. (Yesterday was holiday here so didn’t have access to the computers at the office)</p>

---

## Post #9 by @cpinter (2024-06-25 10:38 UTC)

<p>The very latest Slicer (b0ed88351af465159b101fc434802c83fd438522) did not work as is, I had the same TBB DLL errors.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="36936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does copying tbb123.dll into the folder that contains <code>SlicerApp-real.exe</code> fix the issue?</p>
</blockquote>
</aside>
<p>I copied all DLLs from <code>S5R\tbb-install\redist\intel64\vc14</code> to <code>S5R\Slicer-build\bin\Release</code> and it solves the issue, Slicer starts. Although it took forever the first time (much longer than a normal “first time after restart”). I observed this long startup with v142 as well though, but this is a brand new computer so maybe it’s that (but definitely not performance issue, this is a really strong computer).</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="36936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does the issue occur only in the build tree or also in the install tree (if you create an install package)?</p>
</blockquote>
</aside>
<p>Packaging fails with</p>
<pre><code class="lang-auto">  CMake Error at C:/d/S5R/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake:408 (file):
    file INSTALL cannot find "C:/d/S5R/tbb-install/redist/intel64/tbb12.dll":
    File exists.
  Call Stack (most recent call first):
    C:/d/S5R/Slicer-build/cmake_install.cmake:142 (include)


EXEC : CPack error : Error when generating package: Slicer [c:\d\S5R\Slicer-build\PACKAGE.vcxproj]
</code></pre>

---

## Post #10 by @jamesobutler (2024-06-25 11:46 UTC)

<p>The following likely needs updating to say 1949 as it appears it is never setting tbb_vsdir. It has been an unusual case that 1940 is still Visual Studio 2022.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/b0ed88351af465159b101fc434802c83fd438522/SuperBuild/External_tbb.cmake#L81-L83">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/b0ed88351af465159b101fc434802c83fd438522/SuperBuild/External_tbb.cmake#L81-L83" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b0ed88351af465159b101fc434802c83fd438522/SuperBuild/External_tbb.cmake#L81-L83" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/b0ed88351af465159b101fc434802c83fd438522/SuperBuild/External_tbb.cmake#L81-L83</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="81" style="counter-reset: li-counter 80 ;">
          <li>elseif (NOT MSVC_VERSION VERSION_GREATER 1939)</li>
          <li>  # VS2022 is expected to be binary compatible with VS2015</li>
          <li>  set(tbb_vsdir vc14)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @sfrisken (2024-06-25 15:30 UTC)

<p>Quick update: I tried Csaba’s dll move and that also worked on my laptop with VS 2022. Slicer builds and runs. I know its only a temporary solution but it allows me to keep moving :-). Thanks!<br>
Sarah</p>

---

## Post #12 by @cpinter (2024-07-02 11:46 UTC)

<p>Now that project week is over, I’d like to ask if there is any plan to address this issue? I remember we had a time several years ago when we had to use an older compiler. I’d be fine with that, but please give an update in case you had the chance to discuss it at the PW.</p>
<p>The reason I’m asking is that I typically have many different Slicer builds, and I’m just about to switch to a new machine, and I’d like to avoid rebuilding everything more times than needed. So the question is basically should I wait or help, or proceed with the build using the v142 switch everywhere? Thank you very much!</p>

---

## Post #13 by @jamesobutler (2024-07-02 12:38 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="36936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>So the question is basically should I wait or help</p>
</blockquote>
</aside>
<p>If you can help confirm that the change mentioned below works that would be great!</p>
<aside class="quote" data-post="10" data-topic="36936">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tbb-dll-problem-with-new-version-of-visual-studio/36936/10">TBB DLL problem with new version of Visual Studio</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The following likely needs updating to say 1949 as it appears it is never setting tbb_vsdir. It has been an unusual case that 1940 is still Visual Studio 2022.
  </blockquote>
</aside>


---

## Post #14 by @cpinter (2024-07-02 12:54 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="13" data-topic="36936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If you can help confirm that the change mentioned below works that would be great!</p>
</blockquote>
</aside>
<p>I already checked, it didn’t. See:</p>
<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="36936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The very latest Slicer (b0ed88351af465159b101fc434802c83fd438522) did not work as is, I had the same TBB DLL errors.</p>
</blockquote>
</aside>
<p>Let me know if you were thinking of something else.</p>

---

## Post #15 by @jamesobutler (2024-07-02 14:47 UTC)

<p>I think there may be some confusion. What I described in the below link is code that is not in a Slicer PR and not on Slicer <code>main</code>. A local change needs to be applied and tested.</p>
<aside class="quote" data-post="10" data-topic="36936">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/tbb-dll-problem-with-new-version-of-visual-studio/36936/10">TBB DLL problem with new version of Visual Studio</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The following likely needs updating to say 1949 as it appears it is never setting tbb_vsdir. It has been an unusual case that 1940 is still Visual Studio 2022.
  </blockquote>
</aside>


---

## Post #16 by @cpinter (2024-07-02 14:48 UTC)

<p>Sorry I’ll revise it again then and let you know!</p>

---

## Post #17 by @cpinter (2024-07-02 15:16 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> The change you propose (change 1939 to 1949) works. Is this acceptable for everyone? <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>If so I can do a PR. Thanks for the help!</p>

---

## Post #18 by @jamesobutler (2024-07-02 15:21 UTC)

<p>Yes I think that change makes sense considering Visual Studio 2022 having a MSVC version &gt; 1939 was unexpected and I think this place in TBB is the remaining location where this MSVC version stuff could go wrong. A PR would be appreciated! Thanks for your testing.</p>

---

## Post #19 by @cpinter (2024-07-02 15:35 UTC)

<p>This is the PR: <a href="https://github.com/Slicer/Slicer/pull/7833" class="inline-onebox">COMP: Update acceptable VS2022 MSVC version for TBB install by cpinter · Pull Request #7833 · Slicer/Slicer · GitHub</a></p>

---
