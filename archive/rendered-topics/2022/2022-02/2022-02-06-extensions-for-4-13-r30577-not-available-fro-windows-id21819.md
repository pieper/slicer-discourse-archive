# Extensions for 4.13 R30577 not available fro windows?

**Topic ID**: 21819
**Date**: 2022-02-06
**URL**: https://discourse.slicer.org/t/extensions-for-4-13-r30577-not-available-fro-windows/21819

---

## Post #1 by @MarkusHeller (2022-02-06 04:00 UTC)

<p>Sorry for a possibly silly question - I just downloaded and installed the latest 4.13 version for Windows (R30577) and it seems that none of the extensions is currently available for that platform. Did I just happen to grab that version too early and these are still in the process of being built?</p>

---

## Post #2 by @lassoan (2022-02-06 04:01 UTC)

<p>You can see the status of the build in real-time <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">here</a> (you can go to the previous days, too).</p>
<p>Which extension was that you did not find?</p>

---

## Post #3 by @MarkusHeller (2022-02-06 16:16 UTC)

<p>Thanks for the clarification Andras,</p>
<p>I could not find a single extension. All of the extensions I had installed with my previous slicer version appeared greyed out in the extension manager, and the number of available extensions appeared as 0.</p>
<p>That seemed rather strange so I then had a look at the following site:</p>
<p><a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/61fb6e31342a877cb3096f97" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/61fb6e31342a877cb3096f97</a></p>
<p>from which I got the impression that not a single windows extension seemed to be available.</p>

---

## Post #4 by @lassoan (2022-02-06 16:24 UTC)

<p>Today’s nightly extension builds are partially complete (see the status <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">here</a>, a good number of extensions are already available. You can either wait a few more hours or use yesterday’s Slicer Preview Release - see details <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions">here</a>.</p>

---

## Post #5 by @MarkusHeller (2022-02-06 16:38 UTC)

<p>Ok, understood – I did not realise that the mosr recent application was available already while the extensions were still being built. I know where to check for these being ready now, and can certainly wait a bit.</p>

---

## Post #6 by @lassoan (2022-02-06 17:28 UTC)

<aside class="quote no-group" data-username="MarkusHeller" data-post="5" data-topic="21819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/markusheller/48/11046_2.png" class="avatar"> MarkusHeller:</div>
<blockquote>
<p>I did not realise that the mosr recent application was available already while the extensions were still being built</p>
</blockquote>
</aside>
<p>I agree, this is not intuitive. We plan to change this, see details here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4976">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank" rel="noopener">Show new Slicer Preview Release on download page when extension builds are completed</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-11" data-time="18:52:37" data-timezone="UTC">06:52PM - 11 Jun 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-10-18" data-time="15:19:20" data-timezone="UTC">03:19PM - 18 Oct 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In certain timezones (most of Europe) there is a high chance that people don’t f<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ind any extensions for the release they have just downloaded.

It should be possible to somehow synchronize the time the new Slicer Preview Release package shows up on the download page - with the time when extension builds are complete.

Maybe it could be as simple as having an embargo period between 10pm EST and 12pm EST: packages that are uploaded during this time would all show up at the end of the period (at 12pm EST).

See this discussion: https://discourse.slicer.org/t/extension-manager-problems/11946/5?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
