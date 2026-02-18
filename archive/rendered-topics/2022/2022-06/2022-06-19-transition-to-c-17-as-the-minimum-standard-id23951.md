# Transition to C++17 as the minimum standard

**Topic ID**: 23951
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/transition-to-c-17-as-the-minimum-standard/23951

---

## Post #1 by @jamesobutler (2022-06-19 22:47 UTC)

<p>I propose that on <span data-date="2022-07-04" class="discourse-local-date" data-timezone="America/New_York" data-email-preview="2022-07-04T04:00:00Z UTC">2022-07-04T04:00:00Z</span> Slicer transition to set the minimum C++ standard to C++17. See the following pull request for previous discussion and what will be integrated to complete this change.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6237">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6237" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6237" target="_blank" rel="noopener nofollow ugc">COMP: Require at least C++17</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:c++17-standard</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-03-02" data-time="17:04:58" data-timezone="UTC">05:04PM - 02 Mar 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 3 additions and 3 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6237/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+3</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Qt 6 has a C++ minimum version that is now C++17. https://www.qt.io/blog/qt6-dev<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6237" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">elopment-hosts-and-targets

This commit bumping to C++17 was originally included in #6108 with other supported platform minimum version bumps. This was moved into its own independent PR based on feedback to separate this decision from the other platform version changes needed for Qt 6 and for other reasons as well.

From my initial testing when #6108 was first submitted Slicer I had the following report:
- ✅C++17 built on Windows 10 using Visual Studio 2019 with v142 toolset completed successfully with this PR. All tests cases were run and passed successfully where the failing tests were the same as the already failing tests.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Visual Studio 2017 (15.7) was announced to officially conform with the C++ standard of C++11, C++14 and C++17</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://devblogs.microsoft.com/cppblog/announcing-msvc-conforms-to-the-c-standard/">
  <header class="source">
      <img src="https://devblogs.microsoft.com/cppblog/wp-content/uploads/sites/9/2018/10/Microsoft-Favicon.png" class="site-icon" width="18" height="18">

      <a href="https://devblogs.microsoft.com/cppblog/announcing-msvc-conforms-to-the-c-standard/" target="_blank" rel="noopener nofollow ugc" title="06:50PM - 07 May 2018">C++ Team Blog – 7 May 18</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:558/350;"><img src="https://devblogs.microsoft.com/cppblog/wp-content/uploads/sites/9/2018/08/cplusplusfeature.png" class="thumbnail" width="558" height="350"></div>

<h3><a href="https://devblogs.microsoft.com/cppblog/announcing-msvc-conforms-to-the-c-standard/" target="_blank" rel="noopener nofollow ugc">Announcing: MSVC Conforms to the C++ Standard</a></h3>

  <p>Achieving conformance with the C++ Standards has been a long road for the Visual C++ team. If you’ve seen us at any conferences lately, you’ve probably seen the MSVC Conformance slide. (You can grab a copy of the slide or watch the 2017 CppCon talk...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jamesobutler (2022-06-27 11:57 UTC)

<p>Reminder to developers that this will happen in a week. You can like the original post to serve as your acknowledgment.</p>

---

## Post #3 by @jamesobutler (2022-07-04 20:23 UTC)

<p>A approval to my PR is needed from another developer to be able to execute on the original proposed timeline.</p>

---

## Post #4 by @jamesobutler (2022-07-04 23:53 UTC)

<p>To follow up, the corresponding PR has been merged.</p>

---
