# Latest master does not build in Debug mode

**Topic ID**: 191
**Date**: 2017-04-26
**URL**: https://discourse.slicer.org/t/latest-master-does-not-build-in-debug-mode/191

---

## Post #1 by @dzenanz (2017-04-26 00:05 UTC)

<p>I started clean builds of c9dc6c8008bfc3978e36b8032f14ccaa895680fc in debug and release on Win10 with VS2013 x64. Release mode builds without error. In debug mode I get below errors. I think I had all settings with default values. Is this a known problem or a recent regression?</p>
<pre><code>54&gt;C:\Dev\Slicer-deb\BRAINSTools\BRAINSFit\BRAINSFit.cxx(25): fatal error C1083: Cannot open include file: 'BRAINSFitCLP.h': No such file or directory [C:\Dev\Slicer-deb\Slicer-build\Modules\Remote\BRAINSTools\BRAINSFit\BRAINSFitLib.vcxproj]
51&gt;LINK : fatal error LNK1104: cannot open file 'python27_d.lib' [C:\Dev\Slicer-deb\SimpleITK-build\SimpleITK-build\Wrapping\Python\SimpleITK_PYTHON.vcxproj] [C:\Dev\Slicer-deb\SimpleITK-build\SimpleITK.vcxproj]</code></pre>

---

## Post #2 by @lassoan (2017-04-26 00:40 UTC)

<p>I had issues building Slicer after yesterday’s big build configuration changes. Starting the build from scratch solved the problem, for both Release and Debug, Win10, VS2013 x64, latest master version (ae6f222b1c87ca99215c7bc0e67d2d9c0530f2d0).</p>

---

## Post #3 by @lassoan (2017-04-26 02:45 UTC)

<p>I’ve successfully built latest master version in debug mode using VS2013 from scratch on another computer, too.</p>

---

## Post #4 by @dzenanz (2017-04-26 13:17 UTC)

<p>Thanks for confirming a temporary regression Andras. I will try with ae6f222b1c87ca99215c7bc0e67d2d9c0530f2d0 on my laptop later today.</p>

---

## Post #5 by @blowekamp (2017-04-26 14:20 UTC)

<p>Hello,</p>
<p>This is a known issue with SimpleITK and Slicer in debug mode.</p>
<p>When Slicer is compiled in debug mode, it still compiles Python in release mode. There are only a couple libraries which link against Python and the Slicer run time. These are compiles in different modes Debug and Release. SimpleITK lacks the creative code that is in VTK which defines certain preprocessor definitions before including the Python header to mix Release and Debug libraries.</p>
<p>I even have a prototype branch to add the hack to SimpleITK:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/blowekamp/SimpleITK/tree/SIMPLEITK-576_SupportReleasePythonWithDebugSimpleITK" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/321061?s=400&amp;v=4" class="thumbnail onebox-avatar" width="420" height="420">

<h3><a href="https://github.com/blowekamp/SimpleITK/tree/SIMPLEITK-576_SupportReleasePythonWithDebugSimpleITK" target="_blank" rel="nofollow noopener">blowekamp/SimpleITK</a></h3>

<p>Contribute to blowekamp/SimpleITK development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/blowekamp/SimpleITK/commit/0ce47be294da6462434f255622bd62ca792739e9" target="_blank" rel="nofollow noopener">github.com/blowekamp/SimpleITK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/blowekamp/SimpleITK/commit/0ce47be294da6462434f255622bd62ca792739e9" target="_blank" rel="nofollow noopener">WIP: to test this</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2014-09-02" data-time="18:24:03" data-timezone="UTC">06:24PM - 02 Sep 14 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/blowekamp" target="_blank" rel="nofollow noopener">
          <img alt="blowekamp" src="https://avatars1.githubusercontent.com/u/321061?v=4" class="onebox-avatar-inline" width="20" height="20">
          blowekamp
        </a>
        
      </div>

      <div class="lines" title="changed 4 files with 103 additions and 2 deletions">
        <a href="https://github.com/blowekamp/SimpleITK/commit/0ce47be294da6462434f255622bd62ca792739e9" target="_blank" rel="nofollow noopener">
          <span class="added">+103</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Change-Id: I2e8229f3ba85c28482c4d7311a3890fe048241c4</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If someone is willing  continue work on the patch and help with this Slicer specific customization in SimpleITK, that would be wonderful.</p>
<p>-Brad</p>

---

## Post #6 by @lassoan (2017-04-26 19:45 UTC)

<p>That’s right, I keep forgetting about this (I disable SimpleITK in my debug builds by default).</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a>, I can offer fixing specific problems and testing on Windows. Can you set up a Slicer branch that checks out your patched SimpleITK version and contains all the patches for Slicer that you’ve added so far?</p>

---

## Post #7 by @blowekamp (2017-04-27 13:24 UTC)

<p>Great! Thank you for volunteering to help! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=5" title=":grinning:" class="emoji" alt=":grinning:"></p>
<p>Slicer is due of an upgrade to SimpleITK 1.0, too. I’ll base the Python debug patch on that for your testing.</p>
<p>I don’t know if we should try to upgrade Slicer to sitk 1.0 first, then get this debug patch, or do them both at the same time.</p>

---

## Post #8 by @lassoan (2017-04-27 13:29 UTC)

<p>We can try doing SimpleITK upgrade and debug-mode patch at once. If we run into major difficulties then we can roll back and try one step at a time.</p>

---
