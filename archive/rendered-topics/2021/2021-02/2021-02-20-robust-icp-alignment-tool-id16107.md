---
topic_id: 16107
title: "Robust Icp Alignment Tool"
date: 2021-02-20
url: https://discourse.slicer.org/t/16107
---

# Robust ICP alignment tool

**Topic ID**: 16107
**Date**: 2021-02-20
**URL**: https://discourse.slicer.org/t/robust-icp-alignment-tool/16107

---

## Post #1 by @manjula (2021-02-20 07:46 UTC)

<p>Hi,</p>
<p>I am again frustrated with the ICP alignment of the surface registration of 3D Slicer.  I am just wondering is it not possible to use this method in 3D Slicer ?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/patmo141/object_alignment">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/patmo141/object_alignment" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/45377a8f72eb41758bb682f82a3be9a59ccd266d15fd5346dd354001ce8dfa4a/patmo141/object_alignment" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/patmo141/object_alignment" target="_blank" rel="noopener nofollow ugc">GitHub - patmo141/object_alignment: picked points and ICP alignment addon for...</a></h3>

  <p>picked points and ICP alignment addon for Blender. Contribute to patmo141/object_alignment development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This is for Blender and even with the basic settings it gives excellent results within less than a 30 seconds out of the box and in 3D Slicer even with max setting results  wich takes minutes results are sub par.</p>
<p>This is what I want to do,</p>
<div class="youtube-onebox lazy-video-container" data-video-id="5Esz1EAnao4" data-video-title="Alignment ICP blender vs 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=5Esz1EAnao4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/5Esz1EAnao4/maxresdefault.jpg" title="Alignment ICP blender vs 3D Slicer" width="" height="">
  </a>
</div>

<p>Though I haven’t add the results of Model to Model distance and view this on shape population view I did it here and the ICP blender results are fantastic.<br>
I know I can get good results with Fiducuial registration method but ICP is much more convenient and is fully automatic rather than been semi automatic.</p>
<p>I can use both software to get what I want but it would be great if this problem many of us has can be fixed in 3D Slicer and I would very much appreciate if someone can fix this.</p>
<p>thank you</p>

---

## Post #2 by @muratmaga (2021-02-20 16:06 UTC)

<p>You can try and see if the rigid alignment in <code>alpaca</code> helps you. İt is available in SlicerMorph.</p><aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:400/400;"><img src="https://avatars.githubusercontent.com/u/45026482?s=400&amp;amp;v=4" class="thumbnail" width="400" height="400"></div>

<h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph</a></h3>

<p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ALPACA" target="_blank" rel="noopener nofollow ugc">master/Docs/ALPACA</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @manjula (2021-02-21 02:41 UTC)

<p>thank <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>is this statement still valid?</p>
<p>“Linux users can only use ALPACA in 3D Slicer versions with date [2020-09-25] or older”</p>
<p>Do I need an older version?</p>

---

## Post #4 by @muratmaga (2021-02-21 02:55 UTC)

<p>Sorry that’s incorrect. Please use the latest preview and SlicerMorph.<br>
I will tell remove that.</p>

---

## Post #5 by @patmo141 (2022-10-08 15:49 UTC)

<p>Thanks for the shout! I worked pretty hard on the alignment tool, and while the underlying method is just plain ole ICP, I did some hacks that I found really helped users get good practical results.</p>
<ol>
<li>Allow filtering of the regions to specific areas or areas to ignore in registrations</li>
<li>Dynamically changing the sample size, to allow the initial iterations to go fast (small sample size) and then increasing</li>
<li>Dynamically shrinking the minimum starting distance per iteration to refine the alignment</li>
</ol>
<p>Glad to see people using it!</p>

---

## Post #6 by @mau_igna_06 (2022-10-08 21:57 UTC)

<aside class="quote no-group" data-username="patmo141" data-post="5" data-topic="16107">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ee7513/48.png" class="avatar"> patmo141:</div>
<blockquote>
<p>Dynamically shrinking the minimum starting distance per iteration to refine the alignment</p>
</blockquote>
</aside>
<p>Hi. I don’t understand what you mean here.</p>
<p>Related: <a href="https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118/5" class="inline-onebox">Partial Surface Registration Tutorial - #4 by mau_igna_06</a></p>

---
