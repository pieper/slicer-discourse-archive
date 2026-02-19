---
topic_id: 28616
title: "Markup Shortkeys And Model Interaction"
date: 2023-03-28
url: https://discourse.slicer.org/t/28616
---

# Markup shortkeys and model interaction

**Topic ID**: 28616
**Date**: 2023-03-28
**URL**: https://discourse.slicer.org/t/markup-shortkeys-and-model-interaction/28616

---

## Post #1 by @philippe (2023-03-28 11:25 UTC)

<p>Hello,</p>
<p>I apologize in advance if the answer is clearly stated somewhere but I cannot find a definite answer to my questions below. I found bits and pieces of informations but I may not be using the right keywords.  Some pointers would be helpful.</p>
<p>We are trying to use the markup module / control point to process quite a bit of data. For this we will use templates on a rough segmentation model and the result will be used to initialize other tools.</p>
<p>Efficient interactions with the 3D model are essential to position the points. This interaction seems cumbersome in Slicer compared to some other tools (meshlab for example, but meshlab does not have the 3D image). More specifically, once in the markup / control point is ready to be click (with the red sphere and name shown):</p>
<ul>
<li>
<p>how to rotate the model (without clicking on the arrow). The middle button translates, the right button exits the selection (but does not toggle), space to toggle between tools only seems to work in segmentation, ctrl, alt do not seem to be work as modifyiers, etc…</p>
</li>
<li>
<p>how to change the center of rotation to a point clicked on a model ? (e.g. double click in meshlab, middle click some other tool we use, etc).</p>
</li>
<li>
<p>how to implement modifyers/shortcuts if none of this is available? (I found posts of shortcuts but if there was somewhere an example with a modifyier (e.g. alt with left click rotates but and returns to the current mode), that would be useful</p>
</li>
<li>
<p>optionnally how to change the depth of the camera / perspective angle to end up viewing inside or between an objects? (“using the z buffer” in some other tools etc, ctrl whee/alt/etc in meshlab, position camera tool in sketchup…). I know about model clip. This one is less important to us.</p>
</li>
</ul>
<p>Thanks<br>
Philippe</p>

---

## Post #2 by @lassoan (2023-03-28 21:11 UTC)

<p>The good news is that most of the behavior customization (adding/changing keyboard shortcuts, small navigation features, etc.) are all quite easy to do, using very little Python scripting. We can also make changes in Slicer core to satisfy any requirements that are generally useful.</p>
<aside class="quote no-group" data-username="philippe" data-post="1" data-topic="28616">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>how to rotate the model (without clicking on the arrow). The middle button translates, the right button exits the selection (but does not toggle), space to toggle between tools only seems to work in segmentation, ctrl, alt do not seem to be work as modifyiers, etc…</p>
</blockquote>
</aside>
<p>I’ve created a pull request that allows view manipulation during point placement by holding down the Alt key. See below.</p>
<aside class="quote no-group" data-username="philippe" data-post="1" data-topic="28616">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>how to change the center of rotation to a point clicked on a model ? (e.g. double click in meshlab, middle click some other tool we use, etc).</p>
</blockquote>
</aside>
<p>You can already use “Refocus camera on this point” feature for this. It is available in the right-click menu of any control point of a markup. You can create a separate markup node for this that you can lock in place, change color, etc. to distinguish from your landmark points.</p>
<p>I’ve implemented a right-click menu to set any point (without adding a markup point). See below.</p>
<aside class="quote no-group" data-username="philippe" data-post="1" data-topic="28616">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/f14d63/48.png" class="avatar"> philippe:</div>
<blockquote>
<p>optionnally how to change the depth of the camera / perspective angle to end up viewing inside or between an objects? (“using the z buffer” in some other tools etc, ctrl whee/alt/etc in meshlab, position camera tool in sketchup…). I know about model clip. This one is less important to us.</p>
</blockquote>
</aside>
<p>You can change the perspective projection angle by copy-pasting this into the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">for cameraNode in getNodesByClass("vtkMRMLCameraNode"):
    cameraNode.SetViewAngle(80)
</code></pre>
<p>It would be easy to add a GUI for this, but it has not come up as a need.</p>
<p>Pull request that adds Alt modifier for view manipulation and camera refocusing to view context menu:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6916">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6916" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6916" target="_blank" rel="noopener">View manipulation during markup point placement</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:point-placement-shortcuts</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-03-28" data-time="21:06:50" data-timezone="UTC">09:06PM - 28 Mar 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 6 files with 130 additions and 12 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6916/files" target="_blank" rel="noopener">
            <span class="added">+130</span>
            <span class="removed">-12</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Small improvements to allow view manipulation during markup point placement.</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Your group places lots of points, so this discussion should be interesting. Please have a look at this discussion and the pull request and let us know if you have any comments or suggestions.</p>

---

## Post #3 by @philippe (2023-03-29 17:02 UTC)

<p>Wow. Thanks for your fast response.<br>
This is great news.</p>
<p>We will keep an eye on the pull request for when it makes it in the nightly windows build.</p>
<p>I had not seen the right key menu and, for the camera angle, I confirm it is good enough to paste in the console. It is really helpful to click points in partially hidden location but it is not like we do that every minute.</p>
<p>Thanks again<br>
Philippe</p>

---

## Post #4 by @smrolfe (2023-03-30 17:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> We tried the Alt modifiers in this pull request and they work well. I think this will be a very useful feature!</p>
<p>One thing to note: I initially tried on a VNC connection with alternate Windows mappings for Alt+mouse motion that overrode the Slicer shortcuts. This might not be a common use case, but I wonder if it might be worth considering a different modifier key?</p>

---

## Post #5 by @lassoan (2023-03-30 18:45 UTC)

<p>Thank you for the feedback.</p>
<p>VNC stealing the Alt key is a niche use case - I don’t think it should impact the general use case.  For that special case it is possible to re-map the keys using some custom Python scripting (and all these new Alt shortcuts are just additions to the existing shortcuts anyway).</p>

---

## Post #6 by @lassoan (2023-03-30 18:46 UTC)

<p>The pull request is now merged, the new features will be available in the Slicer Preview Release from tomorrow.</p>

---

## Post #7 by @philippe (2023-03-31 16:29 UTC)

<p>Fantastic.<br>
It works fine for me (windows 10 machine, both alt and change of camera center).<br>
That will clearly help.<br>
This is also the fastest change I have ever seen after posting a question for me ;-).<br>
Thanks again Andras.</p>

---
