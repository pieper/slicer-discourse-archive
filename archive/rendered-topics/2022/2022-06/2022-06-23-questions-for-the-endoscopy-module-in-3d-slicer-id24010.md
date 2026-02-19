---
topic_id: 24010
title: "Questions For The Endoscopy Module In 3D Slicer"
date: 2022-06-23
url: https://discourse.slicer.org/t/24010
---

# Questions for the endoscopy module in 3D slicer

**Topic ID**: 24010
**Date**: 2022-06-23
**URL**: https://discourse.slicer.org/t/questions-for-the-endoscopy-module-in-3d-slicer/24010

---

## Post #1 by @rbb428 (2022-06-23 12:55 UTC)

<p>Hi,<br>
I read a lot post on 3D slicer form about endoscopy module in 3D slicer. However i still don’t get it. I am not quite sure about the process of creating a path and using an endoscopy module to fly through. I am trying to use the atlas database of a brain from SPL and view the model in a way of endoscopy because i want to do some simulation about the endoscopy in brain surgical. Can you help me to explain the workflow to get this done. Thank you so much!</p>

---

## Post #2 by @pieper (2022-06-23 14:28 UTC)

<p>The Endoscopy module only provides some simple path following but it’s meant to be easy to use.</p>
<p>The documentation is here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/endoscopy.html</a></p>
<p>It seemed to be missing some context so I added a paragraph here:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6449/files">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6449/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6449" target="_blank" rel="noopener">DOC: endoscopy usage</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Slicer:doc-endoscopy</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-06-23" data-time="14:26:47" data-timezone="UTC">02:26PM - 23 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 3 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6449/files" target="_blank" rel="noopener">
          <span class="added">+3</span>
          <span class="removed">-0</span>
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

<p>See if this makes sense and if we need more detail comment on the pull request.</p>

---

## Post #3 by @rbb428 (2022-06-24 07:46 UTC)

<p>I tried this but when i add a mark up point. The fly through view doesn’t show up. The button for generating the path isn’t working. Also, when i select the point, i can only one markup point not a series points to guide the path. So i am not sure how these work.</p>

---

## Post #4 by @lassoan (2022-06-24 13:06 UTC)

<p>There was an error in Endoscopy module in Slicer-5.0.2. It has been already fixed, so you can use a recent Slicer Preview Release until a new Slicer Stable Release becomes available.</p>

---

## Post #5 by @rbb428 (2022-06-27 02:12 UTC)

<p>Thanks so much! will try the preview version <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---
