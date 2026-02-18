# Changes to the Markups Module

**Topic ID**: 19871
**Date**: 2021-09-26
**URL**: https://discourse.slicer.org/t/changes-to-the-markups-module/19871

---

## Post #1 by @smrolfe (2021-09-26 16:20 UTC)

<p>Several updates to the Markups module and the addition of a Markups toolbar were added in commit: <a href="https://github.com/Slicer/Slicer/commit/09d12ae6f7598fe8490b691d17a35dcca5bd344a" class="inline-onebox" rel="noopener nofollow ugc">ENH: Improve control point state management and add markups toolbar · Slicer/Slicer@09d12ae · GitHub</a> and are available in the latest preview version.</p>
<p>The <a href="https://discourse.slicer.org/t/proposed-changes-to-markups-to-support-unplaced-points/12714">motivation for these changes</a> was to add support for unplaced or missing control points. These states make it possible to create landmark templates for efficient placing of pre-named points, which is a common feature in other landmarking software. The position status can now be accessed and changed in the control points table of the Markups menu. Additionally, the number of control points in any markup node can now be locked, preventing the addition of new points and the deletion of named points.</p>
<p>While making these updates, we found that the current system of adding new points via the mouse mode menu made it difficult to tell which markup was being edited. To resolve this, a Markups toolbar was added to display/select the active markup node and provide access to several node properties without opening the Markups module.</p>
<p>In the Markups toolbar, the “Create new node and initiate placement” and the “Continue placement” functions have been explicitly separated, to prevent confusion about whether a new node would be created on entering placement mode. The “Place” button in the mouse mode toolbar is now replaced with a button that toggles the Markups toolbar (where new nodes can be created), when there are no active nodes that can accept more points in the scene.</p>
<p>Placement of annotation nodes is not included in the Markups toolbar. Previously, the placement of markups or annotation type nodes was not well distinguished, which was especially problematic as the Annotation nodes are a legacy type that are planned to be phased out. Creation of Annotation type nodes has been moved to the Annotation module to avoid confusion and so they will only be placed intentionally. A shortcut to the Annotation module has been added to the Markups toolbar to prompt the user and reduce the number of clicks needed to place a node.</p>
<p>The issues and fixes related to these changes are being tracked <a href="https://github.com/Slicer/Slicer/issues/5889" rel="noopener nofollow ugc">here</a>, so please update with any feedback.</p>
<p>I made a short video demonstrating the new functionality of the <a href="https://youtu.be/ddd1U61eVlo" rel="noopener nofollow ugc">Markups module and toolbar</a> and related changes to creating legacy <a href="https://youtu.be/dDYxDFehS3k" rel="noopener nofollow ugc">Annotations</a>.</p>
<p>Many thanks to <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/muratmaga">@muratmaga</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, <a class="mention" href="/u/ezgimercan">@ezgimercan</a> and others who helped and advised on these updates.</p>

---

## Post #2 by @smrolfe (2021-09-27 19:57 UTC)

<p>I’ve added a tutorial showing how the new options to create unplaced control points and lock the number of points in a node can be used to make <a href="https://youtu.be/m-z9vNRIhxg" rel="noopener nofollow ugc">templates for landmarking</a>.</p>

---

## Post #3 by @jamesobutler (2021-09-29 03:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eefba976ea8613faf8b76fee2c157203494313fb.png" data-download-href="/uploads/short-url/y68OUTtFOFqItIRpTgsgELYNoWT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eefba976ea8613faf8b76fee2c157203494313fb.png" alt="image" data-base62-sha1="y68OUTtFOFqItIRpTgsgELYNoWT" width="690" height="339" data-dominant-color="CBCED1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×433 29.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have had trouble easily understanding the position status options in the markups control points context menu.</p>
<ul>
<li>
<p>“Set position missing for highlighted fiducial(s)” → It is actually functioning as a toggle that Sets or Unsets the position missing. I see it toggling between different states in the last column of the table. Can it instead only do the action stated? “Unset position” for instance does not act as a toggle for unsetting/restoring position. It only unsets.</p>
</li>
<li>
<p>Upon quick reading “Unset position…” and “Set position…” based on their sentence structure they initially appear to be the opposites of each other however they are not. The latter is “Set position missing” which is an unrelated “Set” action. What do you think about the following rewording and reordering:</p>
<ul>
<li>Restore position of highlighted fiducial(s)</li>
<li>Unset position of highlighted fiducial(s)  ← or “Clear position…”</li>
<li>Edit position of highlighted fiducial(s)</li>
<li>Skip position of highlighted fiducial(s) ← Formerly “Set position missing…”</li>
</ul>
</li>
</ul>
<p>The above order also matches the order when cycling through the position status states in the last column of the table. Restore/complete → unset → edit → skip</p>
<p>“Unset” also sounds a bit technical compared to maybe “Clear”. Maybe Clear/Restore just seems like more natural pairs than Unset/Restore?</p>

---

## Post #4 by @muratmaga (2021-09-29 04:22 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="19871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<ul>
<li>Restore position of highlighted fiducial(s)</li>
<li>Unset position of highlighted fiducial(s) ← or “Clear position…”</li>
<li>Edit position of highlighted fiducial(s)</li>
<li>Skip position of highlighted fiducial(s) ← Formerly “Set position missing…”</li>
</ul>
</blockquote>
</aside>
<p>These look good to me.</p>

---

## Post #5 by @lassoan (2021-09-29 14:24 UTC)

<p>Thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I like your naming suggestions, too. The recommended order is better, too, but I think we should start with the Edit action (Edit, Skip, Restore, Clear), because Edit and Skip are the most commonly needed right-click menu actions (Restore is rarely needed and Clear is available by a single click on the state icon).</p>

---

## Post #6 by @jamesobutler (2021-09-29 16:52 UTC)

<p>Sure, I’m fine with it starting with edit as the top entry. So you agree with “Clear” instead of “Unset”? If so, I think that will be good to make it a bit less technical sounding.</p>

---

## Post #7 by @lassoan (2021-09-29 18:22 UTC)

<p>I agree that “Clear position” sounds better than “Unset position”. Since the “clear” word is not used in markups for anything else, it should not be a problem to have a slight mismatch between the source code and GUI; and a bit less obvious match between set/unset operation names.</p>

---

## Post #8 by @jamesobutler (2021-09-29 22:02 UTC)

<p>PR issued for this naming and reordering</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5919">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5919" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5919" target="_blank" rel="noopener nofollow ugc">ENH: Reorder and rename control point position status options for clarity</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:position-status-name-and-order</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-29" data-time="22:02:02" data-timezone="UTC">10:02PM - 29 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 4 files with 22 additions and 21 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5919/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+22</span>
          <span class="removed">-21</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally from discussion starting at https://discourse.slicer.org/t/changes-to<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5919" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">-the-markups-module/19871/3?u=jamesobutler

"Clear" is chosen over "Unset" since it is less technical. Action order is based on the cycle order when click in the position status column of the markups control point table.

| Current | This PR |
|----------|---------|
| ![image](https://user-images.githubusercontent.com/15837524/135353453-fecd3318-5cf7-40e8-a6e8-c34011e5dec3.png)| ![image](https://user-images.githubusercontent.com/15837524/135353330-bf9ee5cd-2885-494b-96a0-3936350a31b0.png)|
|![image](https://user-images.githubusercontent.com/15837524/135351384-e9c090ea-6880-4e68-a7c7-d7951b08aa5a.png)|![image](https://user-images.githubusercontent.com/15837524/135353255-f23b08b8-8708-4186-a9b1-b19ba1ab57c5.png)|

Also including minor commit `STYLE: Use control point terminology in context menu` which should been included in 1669e8c94d54d6763e381e837ae90113ed31deb7 as it relates to consistently using the "control point" terminology rather than "point" or some other incorrect uses such as "fiducial" or "markup".

| Current | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/135354587-5d57f5d4-4a88-41e2-9ab9-3569d19c785c.png)|![image](https://user-images.githubusercontent.com/15837524/135354613-928c0f8a-65ca-4d5b-a3fa-29fecb3c2193.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @chir.set (2021-10-02 17:01 UTC)

<p>The ‘Persistent’ option is no longer available.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c51bfe15066c1f4869ec742d4de957b8f0d95d77.png" alt="Screenshot_20211002_185334" data-base62-sha1="s7I2bT7kJI8usp7VOih43vNDkXB" width="131" height="64"></p>
<p>Or I may have missed in the ‘Markups properties’ module.</p>
<p>This was very convenient when placing multiple fiducial points. Now we have to click on the fiducial icon in the toolbar every time.</p>
<p>Is it a deprecated function? If yes, is it definitively removed ? Or is it restorable for fiducial placement ?</p>
<p>Thank you.</p>

---

## Post #10 by @muratmaga (2021-10-02 17:06 UTC)

<p>It is there. It is now called “place multiple points” as persistence wasn’t a very clear term.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eac8ef5bab0660e824d81b077e712719abd760f.png" data-download-href="/uploads/short-url/4nm1MW5mGlHDpHFngVr3RSzzuer.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eac8ef5bab0660e824d81b077e712719abd760f_2_690x65.png" alt="image" data-base62-sha1="4nm1MW5mGlHDpHFngVr3RSzzuer" width="690" height="65" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1eac8ef5bab0660e824d81b077e712719abd760f_2_690x65.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eac8ef5bab0660e824d81b077e712719abd760f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eac8ef5bab0660e824d81b077e712719abd760f.png 2x" data-dominant-color="DFE4EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×81 8.39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @chir.set (2021-10-02 17:15 UTC)

<p>Ah, and there’s much more in the complete toolbar. Mine was truncated to the right.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99ffe47c09f4cc5f160471abf4dad5609bd910e6.png" alt="Screenshot_20211002_191222" data-base62-sha1="lYliBQLd5qkAB9wtIa4ge9EB60m" width="565" height="117"></p>
<p>When the markups toolbar is positioned in a second row, it shows up completely.</p>
<p>Thanks for the quick reply.</p>

---

## Post #12 by @muratmaga (2021-10-02 20:38 UTC)

<p>Yes, I think the length of the toolbar is one of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>’s concerns.</p>

---

## Post #13 by @lassoan (2021-10-03 03:01 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="11" data-topic="19871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Ah, and there’s much more in the complete toolbar. Mine was truncated to the right.</p>
</blockquote>
</aside>
<p>In dark mode it is hard to see the toolbar expansion button. This button indicates that only a part of the toolbar is visible and when the button is clicked then the hidden part is displayed. We should adjust the color theme to make the button clearly visible.</p>
<p>The toolbar could be made somewhat smaller (at the cost of requiring more clicks to access functions on it), but the idea is that users would move it to a second toolbar row. I think we initialize the Sequence toolbar to be in the second row and probably we should do the same for this toolbar, too.</p>

---

## Post #14 by @ezgimercan (2021-10-11 22:26 UTC)

<p>Thanks Sara and the team! This one feature I’ve been waiting for a very long time…</p>
<p>I’ve been using the updated module for a while now. I’ve integrated it into our workflow and it changed my landmarking experience a lot. I am mostly using it to mark a list of anatomical points on lots of skull CTs. I’ve created a “template” markups file with empty points and fill that out for every sample. It is much more efficient compared to my old method (of keeping a PDF file open for the order of points and naming them using Python scripts before saving).</p>
<p>I haven’t used it for other markup node types (curves, angles etc) yet but I am looking forward to. We have a couple projects starting that will use curves to mark regions, so this tool will definitely come handy.</p>
<p>One other thing, I am having trouble finding the function call for adding “undefined” points to a node through Python. And for some reason, my Slicer instance crashes when I try to autocomplete [fiducial node].logic.Add … methods. I’ve just started using preview version (just for this update) so I need to investigate if it’s because of these updates or something else.</p>
<p>There is room for improvement in terms of GUI but I am super happy with the functionality (also kinda suck at picking function/button names and designing icons).</p>

---

## Post #15 by @mikebind (2021-10-11 22:44 UTC)

<p>As a workaround, you can add points at an arbitrary location and then unset their location.</p>
<pre><code class="lang-auto">F = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLFiducialNode')
tempLocation = vtk.vtkVector3d(0,0,0)
newControlPointIndex = F.AddControlPointWorld(tempLocation, 'my-landmark-label')
F.UnsetNthControlPointPosition( newControlPointIndex )
</code></pre>
<p>to add a single control point with an unset location, or<br>
<code>F.UnsetAllControlPoints()</code><br>
if you want to add several and then unset them all.</p>

---

## Post #16 by @ezgimercan (2021-10-11 22:46 UTC)

<p>Unset!<br>
I was searching under SetNthControlPoint… group. Thanks, Mike!</p>

---

## Post #17 by @smrolfe (2021-10-11 22:47 UTC)

<p>Thanks for your feedback <a class="mention" href="/u/ezgimercan">@ezgimercan</a>. Could you send a few lines of code to replicate the Slicer crash?</p>

---

## Post #18 by @ezgimercan (2021-10-11 22:51 UTC)

<p>a = loadMarkups(&lt;your markup file .mrk.json&gt;)<br>
a.logic.Add</p>
<p>then click tab and select a function. When I hit enter, it freezes and crashes.</p>
<p>This is the last line of log file:<br>
[DEBUG][Qt] 11.10.2021 15:45:21 [] (unknown:0) - Python console user input: a=loadMarkups("/home/emerc1/XXX.mrk.json")</p>
<p>Version 2021-10-10, Linux, + SlicerMorph</p>

---

## Post #19 by @smrolfe (2021-10-11 22:55 UTC)

<p>Thanks <a class="mention" href="/u/ezgimercan">@ezgimercan</a>! It’s not replicating on my Mac, but I’ll give it a try on Linux.</p>

---

## Post #20 by @mikebind (2021-10-11 23:07 UTC)

<p>I’m not sure if it is related, but I ran into something like this crash a while back <a href="https://discourse.slicer.org/t/reproducible-slicer-crash-on-attempted-tab-completion-on-nightly-2020-01-08/10146" class="inline-onebox">Reproducible Slicer crash on attempted tab completion, on Nightly 2020-01-08</a> .  Unfortunately, it wasn’t really sorted out at the time, and it went away in a more recent preview release, so I don’t think it was pursued any further.</p>

---

## Post #21 by @mikebind (2021-10-11 23:15 UTC)

<p>I also can reproduce the crash <a class="mention" href="/u/ezgimercan">@ezgimercan</a> describes.  I am running 4.13.0-2021-09-26 on Windows. On opening Slicer with an empty scene, the following leads to a crash:</p>
<pre><code class="lang-auto">F = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode')
F.logic.Ad
</code></pre>
<p>Pressing the tab key after typing <code>F.logic.Ad</code> pops up a list of functions, and if I click one of them, Slicer crashes.  I did notice that Slicer will not auto-complete ‘logic’, after typing <code>F.lo</code>, perhaps that indicates that F.logic isn’t supposed to be accessed in this way??</p>

---

## Post #22 by @ezgimercan (2021-10-11 23:20 UTC)

<p>Probably. It doesn’t make sense to access the logic of a markups node - but you can <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"><br>
It wasn’t something I wanted to, it just happened when I was browsing through functions to find “unset” function. It seemed weird because it lists the functions but crashes when you try to autocomplete.</p>

---

## Post #23 by @lassoan (2021-10-13 15:45 UTC)

<p>I’ve fixed the crash, the returning incorrect list of autocompletions for non-existing members (<code>F.logic</code> does not exist), and the problem of the interpreter getting stuck in an error state after invalid autocomplete (or other errors).</p>
<p>I’ve also improved ordering of autocompletions: the list starts with methods&amp;attributes, followed by constants, and ends private Python members.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/997">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/997" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/997" target="_blank" rel="noopener">Fix python autocomplete</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>lassoan:fix-python-autocomplete</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-13" data-time="15:42:10" data-timezone="UTC">03:42PM - 13 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="2 commits changed 2 files with 60 additions and 1 deletions">
        <a href="https://github.com/commontk/CTK/pull/997/files" target="_blank" rel="noopener">
          <span class="added">+60</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fix incorrect autocomplete in the Python console and improve ordering of attribu<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/997" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tes in the autocomplete list.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #24 by @ezgimercan (2021-10-13 20:03 UTC)

<p>Having used it a little bit more, I have a couple ‘very-specific-to-my-use-case’ suggestions, more like discussion points. I would love to have your opinion on them since I cannot decide how to improve/fix them.</p>
<p><strong>Skipping a landmark / Selected or highlighted control point</strong></p>
<p>My main use case is to load a fiducial template (usually 50-70 points) and mark the control points one by one on 3D rendering (sometimes on 2D slice views). There is usually a few control points missing in each scan, so I need to use “skip” button once or twice in each scan. Currently, it sets the state of highlighted control point as “skipped” but the highlight or selection stays on the last marked control point (unless you are in the persistent mode).</p>
<ul>
<li>
<p>If you are not using persistent mode, you either need to go into place mode, then click on the “skip” button; or select the next control point from the list (simply go to the list and click or if the next point is out of the screen, scroll down and then click to select) and click on “skip”. If you go into the place mode, even if you click “skip”, you stay in the place mode.</p>
</li>
<li>
<p>The workaround is to use the persistent mode, the selection auto-advances and you can simply click “skip” when you don’t want to mark that point. But then you need to go into and out of placement mode a lot if you are also interacting with the rendering (rotate, translate etc).</p>
</li>
</ul>
<p>I think the behavior is that the selection (highlighted control point) advances to the next “empty” control point when you go into the “place” mode - and only when you are in Markups module, it doesn’t advance or change when you are in another module and keep marking points. I wonder what could go wrong if the selection advances to the next “empty” point when a point is marked? You probably need an exception when there is no more “empty” points in the list.</p>
<p>I understand the idea of marking a point “missing” (skip it) when you ‘attempt’ to mark it by going into place mode (hence advancing the selection) but my thinking is usually like this: “look at the list to see which point I need to mark next, then adjust the 3D view or slice views to find it, then go into place mode and place it”. Not “first go into place mode, cannot find the point, click skip”.</p>
<p><strong>Auto-scroll control point list</strong></p>
<p>In the same scenario of marking points one by one from the list, my fist action is to look at the list to see which points are coming. Currently, if I marked the last visible point from the list, I need to scroll down to see the next point - or again, go into the place mode so the selection advances and control point list automatically scrolls down. As I said, I don’t like to go into the place mode or use persistent mode as I adjust 3D view and slice views a lot when I am marking points. I think it would be nice to auto-scroll the list so that the selected point is not the last one, maybe 2nd or 3rd one from the visible portion of the list.</p>
<p><strong>Keyboard shortcut for skip button</strong></p>
<p>I also LOVE the ‘p’ keyboard shortcut that comes with SlicerMorph startup script for “dropping” a control point where the mouse is. I like to keep mouse actions for interaction - it is easy to move the mouse cursor unintentionally when clicking to mark a point. It’s much better to position your mouse, and press a key from your keyboard.</p>
<p>This is something <a class="mention" href="/u/smrolfe">@smrolfe</a> and I discuss a lot, the shortcuts for going into the placement mode and persistent mode are too complex. Once reprogrammed, they could be a workaround for the highlight auto-advance + skip issue. I would love to be able to program another keyboard shortcut for “skip” button (if possible, “skip the next empty point”, not “skip the selected point”). If there was a shortcut even for only the current functionality (skip the selected point), you could mark a temporary point with “p” shortcut and make it “unset” or “skipped” by this new shortcut. Let me know if this is possible to program.</p>
<p><strong>FCSV export</strong></p>
<p>I know we are transitioning from fcsv to JSON, but since Slicer still supports fcsv exports, I wanted to note that currently the column headings for the last few fields are not written. When you want to read them as csv files into R, for example, R complains about the mismatch between columns and column headings.</p>
<hr>
<p>Again, although  these are minor improvements in larger Slicer-verse, they will have huge returns for my research team since most of what our students do is marking anatomical landmarks on hundreds of CTs.</p>

---

## Post #25 by @muratmaga (2021-10-13 21:46 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="24" data-topic="19871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I also LOVE the ‘p’ keyboard shortcut that comes with SlicerMorph startup script for “dropping” a control point where the mouse is. I like to keep mouse actions for interaction - it is easy to move the mouse cursor unintentionally when clicking to mark a point. It’s much better to position your mouse, and press a key from your keyboard.</p>
</blockquote>
</aside>
<p>There is currently quite a bit of problem with right-click context menus (e.g., MarkupEditor plugin doesn’t work yet with the new markups changes), and we will eventually provide keyboard shortcuts for these actions in SlicerMorph. Shortcuts in core is a bit more problematic as it is really to hard to come by with keyboard shortcuts that (1) everyone agrees on how it works, (2) not assigned to something else before, (3)  and it doesn’t require you use four of your fingers to create the shortcut (alt+ctrl+shift+P).</p>
<aside class="quote no-group" data-username="ezgimercan" data-post="24" data-topic="19871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>I know we are transitioning from fcsv to JSON, but since Slicer still supports fcsv exports, I wanted to note that currently the column headings for the last few fields are not written. When you want to read them as csv files into R, for example, R complains about the mismatch between columns and column headings.</p>
</blockquote>
</aside>
<p>Yeah, that’s exactly the problem of fcsv format. it is not possible to grow it with new features. So with the new stable release I think we (as in SlicerMorph) will probably expect everyone to switch to Json. There is a json parser in SlicerMorphR package (<a href="http://github.com/SlicerMorph/SlicerMorphR" class="inline-onebox">GitHub - SlicerMorph/SlicerMorphR: R convenience functions for importing SlicerMorph dataset</a>), but I have not had time to try with the updates to markups. If you can try and let us know, it will be great.</p>

---

## Post #26 by @ezgimercan (2021-10-13 21:54 UTC)

<p>Just being able to program shortcuts for certain functions is enough for me. I couldn’t find how to access skip button functionality from Python yet, or more specifically the index of highlighted control point, but if it’s something that could be exposed, I can add it to my startup script.</p>
<p>I will test the JSON parser from SlicerMorphR. I had my own little dummy one but it only reads coordinates and the coordinate system. I agree JSON is better and generalizable.</p>

---

## Post #27 by @smrolfe (2021-10-13 22:47 UTC)

<p>Callbacks for three new shortcuts can be accessed in the Markups toolbar:</p>
<ul>
<li>slicer.modules.markups.toolBar().onPlacePointShortcut(): initiates placement mode in the current node</li>
<li>slicer.modules.markups.toolBar().onCreateNodeShortcut(): Continues point placement of the current markup class in a new node</li>
<li>slicer.modules.markups.toolBar().onTogglePersistenceShortcut(): toggles the persistence</li>
</ul>
<p>The <a href="https://github.com/Slicer/Slicer/blob/b646ac412ca039b69510b531e651f1312e400067/Modules/Loadable/Markups/Widgets/qMRMLMarkupsToolBar.cxx#L101" rel="noopener nofollow ugc">current shortcuts</a> are not very convenient, but you can customize them using the method <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts" rel="noopener nofollow ugc">here</a>.</p>
<p>Adding a shortcut for “skip the current point” would be easy. Another option might be “advance to the next point” which would skip the current point if unplaced.</p>
<p>At one point we discussed adding tooltips with the new shortcuts to the toolbar, but at that time the toolbar actions were not parallel to the keyboard actions. In the final version, this is no longer true, so it would be good to add these tooltips now.</p>

---

## Post #28 by @DIV (2021-10-22 05:36 UTC)

<p>Sara,<br>
that’s a very helpful tutorial.  The logic of how the Markups module was intended to be used is much clearer to me now than it was from either just opening Slicer† or reading the documentation at <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Markups" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/Modules/Markups</a> .  It would therefore be good to link to the tutorial(s) from the documentation page.<br>
The latest documentation page at <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a> currently does not have such a link.  It is a bit improved on the 4.10 documentation, but is still not making the conceptual hierarchy of objects (nor sequence of actions) quite as clear as your video.  Maybe some definitions there would help? (To me “node” sounded like a point in 3D space, rather than a collection of mark-ups, and “control point” sounded like either a guide for a spline or a handle on a graphics object.)</p>
<p>—DIV</p>
<p>† It could perhaps have been a bit more intuitive if the <strong>Control Points</strong> panel were open by default when a Node is created.  Having it closed by default made me think it was something that didn’t often need to be interacted with by the user.</p>

---

## Post #29 by @smrolfe (2021-10-22 15:24 UTC)

<p>Thanks <a class="mention" href="/u/div">@DIV</a> for this feedback. The documentation for the Markups will be updated sometime soon, probably in the next few weeks, so it helps to hear what might be useful.</p>

---
