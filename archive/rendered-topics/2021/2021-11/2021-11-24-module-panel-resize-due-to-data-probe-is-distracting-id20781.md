# Module panel resize due to Data Probe is distracting

**Topic ID**: 20781
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/module-panel-resize-due-to-data-probe-is-distracting/20781

---

## Post #1 by @mikebind (2021-11-24 20:29 UTC)

<p>On recent Slicer preview versions, the module panel automatically resizes based on the size of the contents.  This is an understandable design decision.  As someone who often is switching between modules, I personally would prefer that the slice views not be changing sizes as I do so, but there are advantages either way and I can live with it as it is now.</p>
<p>However, there is one case where I think the auto-resizing is both very annoying and potentially functionally problematic, and that is when mousing over the slice views causes the Data Probe module to change dimensions. This causes a resizing of slice views, which causes the point under the mouse to change, which causes a change in the Data Probe data to change.  If I position my mouse cursor near the edge of the image volume in the slice view, I can get into a state where the shift gets into an endless loop where one state is “Out of Frame”, which increases the size of the Data Probe module and causes a shrinkage of the slice view, which puts my (non-moving) cursor inside the frame of the slice view, which decreases the size of the Data Probe, which expands the slice view, which puts the cursor outside the frame, etc.   This case is a vivid illustration of why this is a problem, as just putting my mouse cursor in one location should not possibly lead to an oscillation in the partition sizes.</p>
<p>The obvious solution for this is to not allow the Data Probe to trigger resizing of the side panel, instead it must use whatever space is available.</p>
<p>If you are having trouble reproducing, I can record a video and share it. The problem can be generated near the edges of displayed segments as well as near the edge of the volume, so it is not sufficient to catch the “Out of Frame” case.</p>

---

## Post #2 by @lassoan (2021-11-26 03:38 UTC)

<p>This behavior has been around for a few years, so it is not a regression, but I agree that it can be quite annoying. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has implemented an important fix about a year ago: if you set the width of the left panel manually once then the DataProbe will not make the vertical separator jump again.</p>
<p>Can you verify that after you drag-and-drop the vertical separator there is no more jumping around as you move the mouse between viewers and the left panel?</p>
<p>It would be nice if this manual initial adjustment was not needed but some initial width would be automatically set by default.</p>

---

## Post #3 by @mikebind (2021-11-29 16:11 UTC)

<p>Testing this, the behavior I get is that the Data Probe will still expand the left panel, but it will no longer shrink it.  This prevents oscillation, but does not prevent a single jarring shift from just mousing over a slice view.  If the left panel is manually decreased in size by dragging the divider, then moving the mouse over the slice view will again expand the left panel until it is wide enough to hold whatever is in the Data Probe. There does not appear to be a way to prevent auto-expansion of the left panel.</p>

---

## Post #4 by @muratmaga (2021-11-29 16:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This behavior has been around for a few years, so it is not a regression, but I agree that it can be quite annoying. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> has implemented an important fix about a year ago: i</p>
</blockquote>
</aside>
<p>I find this behavior quite annoying too, but I also understand the potential for use for it. Would it be possible to turn this into an application setting, in which the default is auto-resize the module window, but it can be turned off?</p>

---

## Post #5 by @lassoan (2021-11-29 16:44 UTC)

<p>I agree that oscillation of the left panel is jarring. A single expansion might be unexpected but understandable when a module needs more space. I don’t see how you could otherwise fulfill conflicting requirements of the user wanting the left panel to be a certain size but the widgets that the module must display not fitting in that amount of space. Alternative solutions that I can think of - cut off the part that does not fit, add a horizontal scrollbar, show a popup to get permission from the user to make the panel wider - all sound much worse than a quick automatic size adjustment.</p>
<p>We try to keep the left panel size narrow (there is automatic test for each module GUI), but not all issues may be captured and there may be cases (e.g., some content makes a window too wide) that should be addressed specifically. If you run into any of these then you can submit an issue for that or discuss it here.</p>
<p>I think the main issue is that there is no initial size - oscillation can still happen until the user adjusts the width manually once. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you know how could we achieve the same effect (make the size not decrease automatically) without a manual adjustment of the splitter? Would that have any negative side effects?</p>

---

## Post #6 by @Sunderlandkyl (2021-11-29 18:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="20781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think the main issue is that there is no initial size - oscillation can still happen until the user adjusts the width manually once. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you know how could we achieve the same effect (make the size not decrease automatically) without a manual adjustment of the splitter? Would that have any negative side effects?</p>
</blockquote>
</aside>
<p>I’ve made a PR here that I think should fix this issue for good (fingers crossed). I’ve just made it so that the horizontal size policy of the data probe is “Ignored”.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6048">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6048" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6048" target="_blank" rel="noopener nofollow ugc">BUG: Prevent data probe from expanding horizontally</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>Sunderlandkyl:data_probe_size2</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-29" data-time="17:59:00" data-timezone="UTC">05:59PM - 29 Nov 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Sunderlandkyl" target="_blank" rel="noopener nofollow ugc">
            <img alt="Sunderlandkyl" src="https://avatars.githubusercontent.com/u/9222709?v=4" class="onebox-avatar-inline" width="20" height="20">
            Sunderlandkyl
          </a>
        </div>

        <div class="lines" title="2 commits changed 1 files with 8 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6048/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+8</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">By setting the the horizontal size policy of the data probe widget to "Ignored",<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6048" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> the widget will use as much space as is provided horizontally, but will never cause the module panel to change size.
The widget can still expand vertically, allowing strings that are too long to be displayed in a single line to be wrapped and not truncated.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2021-11-30 03:50 UTC)

<p>The pull request has been merged and will be available in the Slicer Preview Release from Wednesday. It resolves all the width changes due to information appearing in the Data Probe. The module panel may still become wider when switching between modules, due to different minimum width requirements of modules (depending on the module and content displayed in the module widget).</p>

---

## Post #8 by @lassoan (2023-03-21 01:51 UTC)



---
