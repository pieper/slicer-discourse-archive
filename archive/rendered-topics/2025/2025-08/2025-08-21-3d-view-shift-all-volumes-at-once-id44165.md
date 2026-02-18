# 3D View - shift all volumes at once

**Topic ID**: 44165
**Date**: 2025-08-21
**URL**: https://discourse.slicer.org/t/3d-view-shift-all-volumes-at-once/44165

---

## Post #1 by @gambix (2025-08-21 19:40 UTC)

<p>Hi. I very recently started to (try) to use slicer, so lots to learn yet..</p>
<p>I use it to visualise core samples, and I have a collection of a 1m object that is split into different dicom volumes. That is the way i got the data.</p>
<p>I can represent/render all volumes in the 3D view, but only know how to shift the rendering of 1 volume at a time… is there a way to combine/lock/whatever so i can shift the rendering of all at once?</p>
<p>thank you</p>

---

## Post #2 by @mau_igna_06 (2025-08-21 20:18 UTC)

<p>You can stitch together the volumes so they become one, that may be good enough if the volumes are not too many or not too big and it does not cause you to run out of memory.</p>
<p>See this tool:</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/d63af3b96686cc7f21510fee1ca88ea3/PerkLab/SlicerSandbox#stitch-volumes" class="thumbnail">

  <h3><a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes" target="_blank" rel="noopener nofollow ugc">GitHub - PerkLab/SlicerSandbox: Collection of utilities that are not polished...</a></h3>

    <p><span class="github-repo-description">Collection of utilities that are not polished implementations but can be useful to users</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @gambix (2025-08-21 20:23 UTC)

<p>Thank you very much! I tried to look for ways to join them together with little success as i’m not aware of what tools exist.<br>
I’ll have a go… and drop a line if anything goes wrong <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=14" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---
