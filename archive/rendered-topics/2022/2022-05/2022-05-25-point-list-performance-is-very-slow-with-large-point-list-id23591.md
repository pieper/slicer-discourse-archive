# Point list performance is very slow with large point list

**Topic ID**: 23591
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/point-list-performance-is-very-slow-with-large-point-list/23591

---

## Post #1 by @muratmaga (2022-05-25 20:45 UTC)

<p>I am having quite a bit of slowdown with large number of points (500+)? Interactions are very slow, selection and any operations such as our MarkupsEditor, brings Slicer to almost stop. This is with the latest stable, both on Windows and Linux.</p>

---

## Post #2 by @hherhold (2022-05-25 20:51 UTC)

<p>Try hiding the list of points. I posted about this a while back, can’t find the post now because I’m on my phone. Basically the list gets updated on mouse movements, or something like that.</p>

---

## Post #3 by @jamesobutler (2022-05-25 20:53 UTC)

<p>Which version of Slicer are you using? There was a performance improvement committed recently which is available in latest Slicer preview. It is not present in current Slicer 5.0.2 stable.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6379">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6379" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6379" target="_blank" rel="noopener nofollow ugc">Adding new markup control points is very slow if control points table is visible</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-15" data-time="02:37:36" data-timezone="UTC">02:37AM - 15 May 22 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-05-21" data-time="02:12:23" data-timezone="UTC">02:12AM - 21 May 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adding new markup control points is very slow if Markups module is active and co<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntrol points table is visible.

See user error report at https://discourse.slicer.org/t/adding-points-to-point-list-markup-becomes-progressively-slower/23419/4

## Steps to reproduce

- Create a `Point list` markup
- Add 100 control points
- Add one more control point - it takes a fraction of a second
- Go to Markups module, open Control points section
- Add one more control point - it takes several seconds

## Expected behavior

Adding a control point should only take a fraction of a second.

## Environment
- Slicer version: Slicer-5.1.0-2022-05-08
- Operating system: Windows10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @muratmaga (2022-05-25 20:53 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23591">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Which version of Slicer are you using? There was a performance improvement committed recently which is available in latest Slicer preview. It is not present in current Slicer 5.0.2 stable.</p>
</blockquote>
</aside>
<p>OK. I am using the latest stable 5.0.2. Will this be backported to the stable?</p>

---

## Post #5 by @jamesobutler (2022-05-25 20:56 UTC)

<p>Yes, see <a href="https://github.com/Slicer/Slicer/issues/6379#issuecomment-1129059520" rel="noopener nofollow ugc">this comment</a> from <a class="mention" href="/u/jcfr">@jcfr</a> about the fix being a good candidate for 5.0.3.  Backports have not been integrated into <a href="https://github.com/Slicer/Slicer/tree/maintenance/5.0" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer at maintenance/5.0</a> yet, but they will be as part of the 5.0.3 release process.</p>

---
