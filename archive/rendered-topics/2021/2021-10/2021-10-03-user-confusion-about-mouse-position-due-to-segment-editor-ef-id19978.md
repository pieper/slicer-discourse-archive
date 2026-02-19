---
topic_id: 19978
title: "User Confusion About Mouse Position Due To Segment Editor Ef"
date: 2021-10-03
url: https://discourse.slicer.org/t/19978
---

# User confusion about mouse position due to Segment Editor effect cursor artwork

**Topic ID**: 19978
**Date**: 2021-10-03
**URL**: https://discourse.slicer.org/t/user-confusion-about-mouse-position-due-to-segment-editor-effect-cursor-artwork/19978

---

## Post #1 by @jamesobutler (2021-10-03 19:16 UTC)

<p>Multiple users have told me that they were confused about where their current mouse position was when using a Segment Editor effect that has cursor artwork, specifically the “Draw” effect.</p>
<p>They problem is that they thought the tip of the Pencil in the icon effect was where drawing was going to start rather than at the tip of the smaller blue arrow.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center">“None”</th>
<th style="text-align:center">“Draw”</th>
<th style="text-align:center">“Paint”</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f173ee065ab839fb6691c626960a3fb91743020.jpeg" alt="image" data-base62-sha1="bhFwsWtIcU1T7g50YE32lFY2owM" width="499" height="457"></td>
<td style="text-align:center"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b9beb9d0ce428d04fdd2494dbddb8b3cbf092.jpeg" alt="image" data-base62-sha1="9MnzTNbpeRQKbvFeXUc45ctCeVI" width="494" height="455"></td>
<td style="text-align:center"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/370b333c9af0669d3a75fc9b59fd870f974f60de.jpeg" alt="image" data-base62-sha1="7QWfWbkV0hHqM0x2zoju92EAclU" width="502" height="457"></td>
</tr>
</tbody>
</table>
</div><p>As indicated in <a href="https://github.com/Slicer/Slicer/issues/2432" rel="noopener nofollow ugc">Slicer issue #2432</a>, editor effect cursors were originally added to make it easier for users to know which editor effect was the current one. <a href="https://github.com/Slicer/Slicer/commit/eba54b8dc8fd5ba4b60da6aedf6ce0b865fb25ea" class="inline-onebox" rel="noopener nofollow ugc">ENH: implementation of feature 2432 custom cursors in Editor · Slicer/Slicer@eba54b8 · GitHub</a></p>
<p>It is also a bit unclear to me why the smaller blue arrow is used rather than the standard Qt arrow cursor. The blue arrow cursor is nearly half the dimension of the regular OS level arrow cursor. This likely contributes to the user’s confusion about where their mouse click is going to start the interaction in the slice views.</p>
<p><strong>Options</strong></p>
<ul>
<li>If editor effect cursor icons are the best way to represent clearly the active effect to the user, then maybe a solution is to make it clear that it is just an icon and not the actual cursor shape itself. One possible idea is to draw a black border around the image to more clearly indicate that it is an icon next to the cursor and not the actual cursor shape.</li>
<li>Maybe the effect icon can be removed completely from the slice views with a different technique for better indicating the active editor effect?</li>
</ul>

---

## Post #2 by @lassoan (2021-10-03 20:01 UTC)

<p>I agree that the current effect icons are not good: they are not expressive enough, does not follow standard conventions where applicable, not easy to distinguish from each other. Most likely we will start the Slicer icons redesign project with getting these effect icons and the markups icons. Any suggestions are welcome.</p>
<p>The current mouse cursor icons are generated automatically from the effect icons. It is an advantage for users that they don’t need to learn two icons for the same effect, and for developers that they don’t need to design two icons. Completely removing the custom icon would remove a useful hint for the user, so I don’t think that would be a step in the right direction.</p>
<p>You could try changing the mouse cursor generation by adding the effect icon to a standard white cursor icon and see how it looks. If we go through with this change then we would probably also need to modify the markups plane cursor generation the same way.</p>

---

## Post #3 by @pieper (2021-10-03 20:11 UTC)

<p>I recall that once we had, or tried to have, the standard pointer cursor with the standard hotspot and the editor effect icon superimposed to the lower right.  This addressed the use case well, since you knew where the hotspot was and also had a reminder of what effect is active.  I believe there were some cross-platform issues with cursor image size but those may have gone away in the meantime.</p>

---

## Post #4 by @jamesobutler (2021-10-03 21:48 UTC)

<p>I have done some prototyping where I have replaced the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/CursorBaseArrow.png" rel="noopener nofollow ugc">CursorBaseArrow.png</a> usage with the NullEffect.png and maintained this base image directly above the effect image. This required some adjustment of the hotspot positioning to match the point of the arrow in the <a href="https://github.com/Slicer/Slicer/blob/9e4bd8524a03f0bbf7284b1607adc4dd12da36f9/Modules/Loadable/Segmentations/EditorEffects/Resources/Icons/NullEffect.png" rel="noopener nofollow ugc">NullEffect.png</a>. I also removed some padding that was positioning the effect closer to the arrow icon which was causing overlapping issues. It appears to work well at least on my Windows platform. I could issue a PR for you to help review on other platforms?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/080b2e137736195bef3b7370b28e5debba5e1779.png" alt="image" data-base62-sha1="199LUwIBFpia6nfIwVzXn1HOOPn" width="132" height="126"></p>
<p>Using the same arrow cursor makes it more recognizable and more intuitive to think that the draw will begin at the point of this arrow rather than the smaller blue arrow. I also added a white border around the effect icon to further address the confusion to make it clear the effect image is just an image to match the effect icon and that the tip of the pencil isn’t where the draw is going to begin. I went with the border idea rather than just dropping the transparency of the effect image as in the case of the paint effect, the circular brush can be really large and encompass the effect image. We wouldn’t want a square to completely cover up the image data when we could still use the transparency benefit.</p>

---

## Post #5 by @jamesobutler (2021-10-03 23:55 UTC)

<p>Is the blue color of the current arrow something we want to maintain? Maybe the NullEffect.png just colored with that same blue? Is it blue to be a distinctive mouse mode compared to the None state? Although I guess it isn’t really considered an official Slicer mouse mode state.</p>

---

## Post #6 by @jamesobutler (2021-10-04 15:19 UTC)

<p>I’ve issued the following for others to try it out with the ability to prototype additional changes starting with my code.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5928">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5928" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5928" target="_blank" rel="noopener nofollow ugc">ENH: Make segment effect cursor hotspot position clearer</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:editor-effect-icon</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-04" data-time="15:18:34" data-timezone="UTC">03:18PM - 04 Oct 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 13 additions and 6 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5928/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+13</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Originally from https://discourse.slicer.org/t/user-confusion-about-mouse-positi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5928" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">on-due-to-segment-editor-effect-cursor-artwork/19978. Issuing this PR now so others can try it out 

The "Draw" effect cursor was often mistaken for having the hotspot positioned at the end of the Pencil rather than the end of the blue arrow in the cursor.  The blue arrow has been replaced with the standard white arrow cursor arrow and a white border has been added around the effect image to make it clearer that the hotspot position is not in the effect image.

| Current| This PR |
|---------|---------|
|![image](https://user-images.githubusercontent.com/15837524/135877932-9ae5352a-a08a-4c06-ae05-edfb39e06a56.png)|![image](https://user-images.githubusercontent.com/15837524/135877586-c40785ec-f940-4b88-bf7f-cdd914cea5e5.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @jamesobutler (2021-10-07 23:25 UTC)

<p>Thoughts on the proposed design? I was thinking more and the white cursor does seem to be the correct cursor as if you’re in Window/Level mouse mode and then click a segment editor effect, the mouse mode goes to the white arrow cursor (ViewTransfrom) mode in the mouse mode toolbar.</p>

---
