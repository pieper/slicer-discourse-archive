# Build failure of certain extensions on Mac factory due to missing svn

**Topic ID**: 18813
**Date**: 2021-07-20
**URL**: https://discourse.slicer.org/t/build-failure-of-certain-extensions-on-mac-factory-due-to-missing-svn/18813

---

## Post #1 by @cpinter (2021-07-20 09:37 UTC)

<p>It seems that certain extensions reliably fail to build on Mac due to missing svn command. For example SlicerRT or SlicerHeart:</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2323746" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=2323746</a><br>
<a href="https://slicer.cdash.org/viewBuildError.php?buildid=2323865" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=2323865</a></p>
<p>The source code of these extensions does not seem to contain anything SVN related. The only common thing is that both are superbuild extensions, but none of the built subprojects have SVN repositories.</p>
<p>Any ideas how to fix the Mac factory build for these extensions? Thanks!</p>

---

## Post #2 by @jamesobutler (2021-07-20 12:25 UTC)

<p>There are 2 factory macOS build machines (factory-south-macOS.kitware and computron-macOS-tests.kitware).</p>
<p>See <a href="https://discourse.slicer.org/t/mac-factory-error-svn-error-failed-to-locate-svn/16938/4" class="inline-onebox">Mac factory error - "svn: error: Failed to locate 'svn'." - #4 by lassoan</a></p>

---

## Post #3 by @cpinter (2021-07-20 12:36 UTC)

<p>Thanks. Sorry, should have done a search.</p>

---

## Post #4 by @jcfr (2021-07-20 14:18 UTC)

<p>Help finalizing this PR that removes SVN support would be great:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5562">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5562" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5562" target="_blank" rel="noopener">Simplify build system removing extension build svn support</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:simplify-build-system-removing-extension-build-svn-support</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-01" data-time="16:55:29" data-timezone="UTC">04:55PM - 01 Apr 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="2 commits changed 26 files with 26 additions and 143 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5562/files" target="_blank" rel="noopener">
          <span class="added">+26</span>
          <span class="removed">-143</span>
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


---
