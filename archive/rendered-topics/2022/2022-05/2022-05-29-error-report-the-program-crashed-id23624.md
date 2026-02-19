---
topic_id: 23624
title: "Error Report The Program Crashed"
date: 2022-05-29
url: https://discourse.slicer.org/t/23624
---

# Error report：The program crashed

**Topic ID**: 23624
**Date**: 2022-05-29
**URL**: https://discourse.slicer.org/t/error-report-the-program-crashed/23624

---

## Post #1 by @janus_zhu (2022-05-29 09:08 UTC)

<p>Operation process:</p>
<p>Step 1:</p>
<p>Import CT images,</p>
<p>Step 2:</p>
<p>Use the measuring tool to make 3-4 new measurements.</p>
<p>Step 3:</p>
<p>Open the crosshair(interaction), move, and the program is stuck.</p>
<p>run envirement：<br>
windows10 , slicer lastest version.</p>

---

## Post #2 by @pieper (2022-05-29 13:44 UTC)

<p>Thanks for the report, but we’d need more details in order to help.  Does this happen only with a particular dataset?  Can you replicate the issue using public sample data?</p>
<p>See this section for suggestions about how to get help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#i-want-to-report-a-problem" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#i-want-to-report-a-problem</a></p>

---

## Post #3 by @janus_zhu (2022-05-29 13:48 UTC)

<p>Errors are easy to find:</p>
<ol>
<li>
<p>Open any CT</p>
</li>
<li>
<p>Open the measuring ruler, and then measure several more, such as 1-2</p>
</li>
<li>
<p>Open interaction</p>
</li>
<li>
<p>Drag line</p>
</li>
<li>
<p>Stuck</p>
</li>
</ol>
<p>I have commit url:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6400">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6400" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6400" target="_blank" rel="noopener nofollow ugc">operation: Interaction with messure tools make program crash</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-05-29" data-time="13:54:01" data-timezone="UTC">01:54PM - 29 May 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/januszhu707" target="_blank" rel="noopener nofollow ugc">
          <img alt="januszhu707" src="https://avatars.githubusercontent.com/u/105405296?v=4" class="onebox-avatar-inline" width="20" height="20">
          januszhu707
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
    <p class="github-body-container">Errors are easy to find:

1. Open any CT

2. Open the measuring ruler, and t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">hen measure several more, such as 1-2

3. Open interaction

4. Drag line (cross line)

5. Stuck
--------------------------
System:win10, slicer-2022-05-28
-------------------------------------------------------
Snap images:
 
![image](https://user-images.githubusercontent.com/105405296/170873991-ecf94dce-aa5e-4eb3-96f1-c8ee08c75411.png)


![image](https://user-images.githubusercontent.com/105405296/170873863-c5e58593-b83d-4432-b666-9c36e7968b5b.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @janus_zhu (2022-05-30 02:08 UTC)

<p>thanks!</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/197a96b2c7dc97a873e904e7f52c17fc572db18c">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/197a96b2c7dc97a873e904e7f52c17fc572db18c" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/197a96b2c7dc97a873e904e7f52c17fc572db18c" target="_blank" rel="noopener nofollow ugc">BUG: Fix crash in interactive slice intersections</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-05-30" data-time="01:29:12" data-timezone="UTC">01:29AM - 30 May 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 7 files with 10 additions and 10 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/197a96b2c7dc97a873e904e7f52c17fc572db18c" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+10</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a view contained markups and interactive slice intersections, the applicati<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/197a96b2c7dc97a873e904e7f52c17fc572db18c" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">on could crash while moving and dragging markup control points.

The problem was that when a widget was forced to release the focus the `widget-&gt;Leave(eventData)` method was called with `nullptr`, but the `Leave`
method actually required valid `eventData`.

Fixed the issue by passing valid `eventData` to `SetHasFocus` method, which then can call `Leave` with that `eventData`.

fixes #6400</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
