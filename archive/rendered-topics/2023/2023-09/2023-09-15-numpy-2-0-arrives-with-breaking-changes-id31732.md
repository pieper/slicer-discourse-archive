# Numpy 2.0 arrives with breaking changes

**Topic ID**: 31732
**Date**: 2023-09-15
**URL**: https://discourse.slicer.org/t/numpy-2-0-arrives-with-breaking-changes/31732

---

## Post #1 by @Alex_Vergara (2023-09-15 08:39 UTC)

<p>The numpy team has issued <strong><a href="https://github.com/numpy/numpy/issues/24300" rel="noopener nofollow ugc">this statement</a></strong></p>
<p>Basically you shall temporarily add requirements to pinned numpy&lt;2 version, then create a CI based on numpy2 and correct all relevant errors before migrating.</p>
<p>If you already have a pinned numpy version in Slicer builds, then you have no issues until next release, but users must be warned not to upgrade numpy in any way. Therefore, you shall block numpy upgrades in the pip_install function.</p>

---

## Post #2 by @lassoan (2023-09-15 19:05 UTC)

<p>Since an issue has been created for this topic, I would suggest to continue discussion there:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7230">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7230" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7230" target="_blank" rel="noopener">Support Numpy2 API</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-15" data-time="08:45:00" data-timezone="UTC">08:45AM - 15 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/BishopWolf" target="_blank" rel="noopener">
          <img alt="BishopWolf" src="https://avatars.githubusercontent.com/u/11816952?v=4" class="onebox-avatar-inline" width="20" height="20">
          BishopWolf
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Is your feature request related to a problem? Please describe.

The numpy t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">eam has issued [this statement](https://github.com/numpy/numpy/issues/24300)

## Describe the solution you'd like

Basically you shall temporarily add requirements to pinned numpy&lt;2 version, then create a CI based on numpy2 and correct all relevant errors before migrating.

If you already have a pinned numpy version in Slicer builds, then you have no issues until next release, but users must be warned not to upgrade numpy in any way. Therefore, you shall block numpy upgrades in the pip_install function.

## Describe alternatives you've considered

When numpy 2 is out, every user upgrading numpy will see Slicer crashing. You shall emit a WARNING.

## Additional context

Future Slicer releases shall be compatible with numpy 2 API</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
