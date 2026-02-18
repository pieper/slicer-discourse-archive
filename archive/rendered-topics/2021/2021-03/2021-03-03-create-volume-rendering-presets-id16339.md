# Create volume rendering presets

**Topic ID**: 16339
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/create-volume-rendering-presets/16339

---

## Post #1 by @mohammed_alshakhas (2021-03-03 17:39 UTC)

<p>i wish to have a simple " save as preset " in the rendering module.</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2021-03-03 19:31 UTC)

<p>The steps to create custom volume rendering presets are described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/volumerendering.html#how-to-register-custom-volume-rendering-presets">here</a>.</p>
<p>It could be certainly made more user friendly, for example by adding a small Python scripted module that would provide GUI to add/remove/edit volume rendering presets. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">Developer tutorials</a> describe how to create a new module, then you would need to copy the volume rendering preset example into the module and adjust it so that it is controlled by the GUI. Would you be interested in giving it a try (or find a student or a friend that is familiar with Python scripting and would be interested in helping you out)?</p>

---

## Post #3 by @mohammed_alshakhas (2021-03-05 14:34 UTC)

<p>Unfortunately I don’t have any help around .</p>

---

## Post #4 by @lassoan (2021-03-05 14:52 UTC)

<p>You can <a href="https://github.com/Slicer/Slicer/issues/new?assignees=&amp;labels=type%3Aenhancement&amp;template=feature_request.md&amp;title=">submit a formal feature request in the issue tracker</a> and if it gets enough attention (<img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> upvotes) from other users then it will be implemented.</p>

---

## Post #5 by @lassoan (2021-03-08 16:21 UTC)

<p>Feature request has been added:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5505" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5505" target="_blank" rel="noopener">Save current volume rendering setting as a preset</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-05" data-time="15:55:28" data-timezone="UTC">03:55PM - 05 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/alshakhasm" target="_blank" rel="noopener">
          <img alt="alshakhasm" src="https://avatars.githubusercontent.com/u/80116383?v=4" class="onebox-avatar-inline" width="20" height="20">
          alshakhasm
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Is your feature request related to a problem? Please describe.
I always start creating my volume rendering from scratch, however, that takes...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
