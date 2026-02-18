# Shortcut keys doesnt work properly on Dental Segmentator 3dSlicer 5.8.0

**Topic ID**: 41286
**Date**: 2025-01-25
**URL**: https://discourse.slicer.org/t/shortcut-keys-doesnt-work-properly-on-dental-segmentator-3dslicer-5-8-0/41286

---

## Post #1 by @Esteban_Barreiro (2025-01-25 16:57 UTC)

<p>Hi there!</p>
<p>Im using 3dSlicer 5.8.0 and the shortcut ESC doesnt work properly on Dental Segmentator, it does not cancel the editing effect as in the Segment Editor Extra Effects.</p>
<p>Also you cant change the name of the segments by double click them. It opens the colour tab, where you can change the names but you must select again the color you want it to be.</p>

---

## Post #2 by @jamesobutler (2025-01-25 18:37 UTC)

<aside class="quote no-group" data-username="Esteban_Barreiro" data-post="1" data-topic="41286">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/esteban_barreiro/48/5430_2.png" class="avatar"> Esteban_Barreiro:</div>
<blockquote>
<p>the shortcut ESC doesnt work properly on Dental Segmentator, it does not cancel the editing effect as in the Segment Editor Extra Effects.</p>
</blockquote>
</aside>
<p>Did the ESC key work differently prior to Slicer 5.8.0 when using Dental Segmentator? If not, is this a feature request for the Dental Segmentator extension?</p>
<aside class="quote no-group" data-username="Esteban_Barreiro" data-post="1" data-topic="41286">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/esteban_barreiro/48/5430_2.png" class="avatar"> Esteban_Barreiro:</div>
<blockquote>
<p>Also you cant change the name of the segments by double click them. It opens the colour tab, where you can change the names but you must select again the color you want it to be.</p>
</blockquote>
</aside>
<p>A change was made in Slicer Preview starting around mid-November 2024 where the terminology selector would appear when double clicking on the segment name in the segments table. This change in behavior was led by <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a>. You can go back to Slicer 5.6.2 behavior where double clicking on the segment name allows to immediately edit the name by going to “Edit-&gt;Application Settings-&gt;Segmentations-&gt;Use standard terminology for segments” and uncheck this setting. Please provide your thoughts about this change so we can improve the functionality as needed.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/fb23f956db9ac1160d91ce4e1414220e1914569a">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/fb23f956db9ac1160d91ce4e1414220e1914569a" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/fb23f956db9ac1160d91ce4e1414220e1914569a" target="_blank" rel="noopener nofollow ugc">ENH: Introduce setting for using standard terminology in segments table</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2024-11-12" data-time="14:05:28" data-timezone="UTC">02:05PM - 12 Nov 24 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/cpinter" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
          cpinter
        </a>
      </div>

      <div class="lines" title="changed 12 files with 329 additions and 154 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/fb23f956db9ac1160d91ce4e1414220e1914569a" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+329</span>
          <span class="removed">-154</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Previously the segments table used the terminology selector with double-clicking<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/fb23f956db9ac1160d91ce4e1414220e1914569a" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> the color, but allowed direct editing when double-clicking the name. Instead of this inconsistent behavior, now we have a new option in settings for using standard terminology. If turned on, both the name and the color shows the terminology selector, otherwise a simple color picker and text editor, respectively.
In addition to the checkbox in Application Settings, this commit adds a checkable action to the context menu of the segments in the segments table.
The segments tables may choose a different setting key to have a behavior independent of the default setting (which is Segmentations/SegmentsTableUseStandardTerminology).

Re #6975</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Esteban_Barreiro (2025-01-25 19:11 UTC)

<p>Allright! thanks a lot!</p>

---
