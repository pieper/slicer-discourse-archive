# CircleCI build failures

**Topic ID**: 20828
**Date**: 2021-11-29
**URL**: https://discourse.slicer.org/t/circleci-build-failures/20828

---

## Post #1 by @lassoan (2021-11-29 14:36 UTC)

<p>A few weeks ago all our circleCI builds on pull requests (such as <a href="https://app.circleci.com/pipelines/github/Slicer/Slicer/2796/workflows/90ce1a63-466e-4a1f-acde-9ed2b8223896/jobs/2796">this</a>) started to fail because the build is not completed within 60 minutes.</p>
<p>I’ve checked our usage and it seems that we would need to pay at least $100 per month (<a href="https://app.circleci.com/settings/plan/github/Slicer/overview?intent=purchase-performance-plan" class="inline-onebox">CircleCI</a>) to cover our needs, and I’m not sure if the maximum build timeout can be adjusted even then. If it can be then we may potentially need to pay more. Another risk of the “pay-as-you-go” pricing of circleCI is that if we mess up something and builds don’t end for many hours and we don’t notice that in time then the charges can go up a lot.</p>
<p>Should we try to speed up the build? For example we could try creating the docker image after Slicer build is completed and do an incremental build instead of a full build for each pull request. This would potentially miss some rare build errors (that only occur when building from scratch), but we would get results much faster, so developers could fix the issues more quickly and circleCI would charge less (or could remain free).</p>
<p>Or, should we switch to GitHub actions?</p>
<p>Or set up runners on our computers? It would be no problem to allocate a few computers in the PerkLab for continuous builds, if there is someone to help me with the setup.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @adamrankin (2021-11-29 14:42 UTC)

<p>We (VASST, Robarts) can also contribute some runners if that’s the route we take.</p>

---

## Post #3 by @pieper (2021-11-29 15:01 UTC)

<p>I’d be happy to contribute runner machines, but in general we’d get a lot more value from breaking up the build into manageable sets of dependencies that could be rebuilt intelligently.  I think gh actions could be a better infrastructure for this since we can set up a build matrix.  But it will require someone working through all the details.  Runners might be an easier short-term solution.</p>

---

## Post #4 by @Sam_Horvath (2021-11-29 15:59 UTC)

<p>We will look into why the build is going over time.  For the CircleCI builds we are using a Docker image with the dependencies already built.</p>
<p>We can look at doing an incremental build of Slicer for CircleCI</p>

---

## Post #5 by @Sam_Horvath (2021-11-29 16:06 UTC)

<p>This appears to be the first commit where the timeout failure becomes permanent: <a href="https://github.com/Slicer/Slicer/commit/409c7f035aa9015863cffc827ed37661322a550d" class="inline-onebox">BUG: Fix window/level presets in Volumes module · Slicer/Slicer@409c7f0 · GitHub</a></p>
<p>However, looking at older commits that passed, it seems that the timeout has changed?  Older commits are going as much as 2 hrs in some cases and <a href="https://app.circleci.com/pipelines/github/Slicer/Slicer/2693/workflows/ca7cd642-7301-44cc-be22-dfd7b9972db3/jobs/2693">passing</a>. We would need to trim quite a bit off the build to fix that it seems, so an incremental build may be necessary.</p>

---

## Post #6 by @lassoan (2021-11-29 16:14 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="5" data-topic="20828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>However, looking at older commits that passed, it seems that the timeout has changed?</p>
</blockquote>
</aside>
<p>Yes, it seems that circleCI has changed its policy. I saw that a few weeks ago ITK maintainers disabled circleCI builds, too, for the same reason.</p>

---

## Post #7 by @jcfr (2021-11-30 06:17 UTC)

<p>This should be addressed by the following pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6051">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6051" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6051" target="_blank" rel="noopener">COMP: Add "CI" GitHub action workflow to replace CircleCI</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:transition-ci-to-github-action</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-30" data-time="06:06:21" data-timezone="UTC">06:06AM - 30 Nov 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 5 files with 81 additions and 42 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6051/files" target="_blank" rel="noopener">
          <span class="added">+81</span>
          <span class="removed">-42</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">To avoid the newly introduced 60-minute CircleCI limit, this commit
removes the<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6051" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> continuous integration pipeline based on CircleCI and adds
a new workflow based on GitHub Action.

The new CI workflow also:
- introduces a "private" action called "slicer-build" responsible for
  fetching the latest "slicer/slicer-base" image and starting the build
- uploads the generated Slicer package as an artifact with a retention
  time of 1 day.

See https://discourse.slicer.org/t/circleci-build-failures/20828</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @rbumm (2021-12-01 08:01 UTC)

<p>It would be great to have a faster initial build after a new Slicer fork / branch.</p>
<p>What does make the S4R or S4D directory so extremely big?<br>
Windows: Could we not just provide the outer build files (DLLs and lib files)  as they are and let them only compile new if dependencies change?</p>

---
