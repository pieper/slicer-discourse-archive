# Grow from seeds does not work if painting only one segment

**Topic ID**: 32452
**Date**: 2023-10-27
**URL**: https://discourse.slicer.org/t/grow-from-seeds-does-not-work-if-painting-only-one-segment/32452

---

## Post #1 by @Investigacion_y_des1 (2023-10-27 14:38 UTC)

<p>Hello! Im having trouble with Grow From Seeds. Basically, sometimes it works… sometimes it doesnt. Im about to give up and start working with some other software. Does it happen to any of you, with this option? I will gladly listen to your recomendations, thank you so much,</p>
<p>Mercedes.-</p>

---

## Post #2 by @lassoan (2023-10-28 16:09 UTC)

<p>It is not an algorithm that sometimes works sometimes doesn’t - it is very predictable, consistently separating regions that have a slight intensity difference between them.</p>
<p>If you can share your scene or a screen capture video then we can give advice about what to do differently. (upload the file somewhere and post the link here)</p>

---

## Post #3 by @Investigacion_y_des1 (2023-10-30 18:46 UTC)

<p>I was able to solve it, thank you for your answer !</p>

---

## Post #4 by @pieper (2023-10-30 18:48 UTC)

<p>That’s great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>If you hit an issue that others might learn from it would be great if you could report what that was and how you got past it.</p>

---

## Post #5 by @Investigacion_y_des1 (2023-10-31 12:27 UTC)

<p>Of course, my mistake was that I tried to segment just one segment (many spots on one segment). I realised that in order for this option to work, you have to work on, al least, two segments. Inspite it doesn’t make much sense to me, it works this way. I didn’t have problems since. I´m grateful for the quick answers tough, It really makes me feel less lonely in this learning path <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20">  I’m learning by myself, and many times I don’t understand and get frustrated. Thanks !</p>

---

## Post #6 by @lassoan (2023-10-31 12:34 UTC)

<p>You need to have at least two competing segments because this effect performs competitive region growind: segments are grown until they fill the entire region of interest or reach another segment. If you only have one segment then that will fill the entire region.</p>

---

## Post #7 by @lassoan (2023-10-31 15:20 UTC)

<p>I’ve submitted a pull request that adds a popup window to remind the user that two input segments are needed. It’ll be in the Slicer Preview Release within a couple of days:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7326">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7326" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7326" target="_blank" rel="noopener">ENH: Make Grow from seeds effect input requirements more clear</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:show-grow-from-seeds-input-req</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-31" data-time="15:19:16" data-timezone="UTC">03:19PM - 31 Oct 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 32 additions and 11 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7326/files" target="_blank" rel="noopener">
            <span class="added">+32</span>
            <span class="removed">-11</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Grow from seeds effect requires at least 2 visible segments as input if no edita<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7326" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ble region is specified, and at least 1 visible segment if editable region is specified. When the requirement was not fulfilled then the user did not know what was wrong, because there was no visible notification on the GUI (only in the application log), see for example https://discourse.slicer.org/t/grow-from-seeds-does-not-work-if-painting-only-one-segment/32452/6

This commit adds display of the error in a popup window if there are not enough input segments. A notification on the status bar is added if segmentation is canceled due to removal of an input segment.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
