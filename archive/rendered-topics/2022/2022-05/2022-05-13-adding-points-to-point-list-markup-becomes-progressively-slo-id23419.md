# Adding points to Point List Markup becomes progressively slower

**Topic ID**: 23419
**Date**: 2022-05-13
**URL**: https://discourse.slicer.org/t/adding-points-to-point-list-markup-becomes-progressively-slower/23419

---

## Post #1 by @Karl_Hahn (2022-05-13 21:53 UTC)

<p>Adding points to Point List Markup becomes progressively slower. It reached multiple seconds to add a point after about 30 points. This does not occur when adding points to e.g. a closed curve.</p>
<p>Please let me know if I can provide any other information. Thanks!</p>
<p>Slicer 5.1, Windows 10 21H2, i7-7820HQ, 32 GB RAM, Quadro M1200</p>

---

## Post #2 by @lassoan (2022-05-14 22:43 UTC)

<p>If you add more than one point then I would recommend to do it in one batch: call <code>StartModify</code>, add your points, and call <code>EndModify</code>. This avoids unnecessary updates.</p>
<p>You can play around with the “AddManyMarkupsFiducialTest” test module. To see what performance you can get. For me, time required for adding 50 points without any event optimization takes 280ms, while with StartModify/EndModify it just takes 46ms. Adding 5000 points takes just 234ms.</p>
<p>if you need to visualize more than a few hundred points and you don’t need to interact with each point separately then you may consider using a model node instead. That can visualize hundreds of thousands of points at interactive frame rates.</p>

---

## Post #3 by @Karl_Hahn (2022-05-14 23:52 UTC)

<p>Hi Andras, thanks for the response.</p>
<p>I see that I wrongly put this question in the “Development” category, when it should likely be in “Support”.</p>
<p>My question deals with the UX of the vanilla Slicer app, without any modification.</p>

---

## Post #4 by @lassoan (2022-05-15 02:47 UTC)

<p>Currently, update of the <code>Control Points</code> section in Markups module is slow. I’ve added a bug report to keep track of this issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6379">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6379" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6379" target="_blank" rel="noopener">Adding new markup control points is very slow if control points table is visible</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-15" data-time="02:37:36" data-timezone="UTC">02:37AM - 15 May 22 UTC</span>
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
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Adding new markup control points is very slow if Markups module is active and co<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntrol points table is visible.

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

<p>As a workaround, you close the <code>Control points</code> section in the Markups module (or switch to a different module) while adding points.</p>

---
