---
topic_id: 47472
title: "GUI panels from Slicer 5.12.0 shows over other software on Windows 11"
date: 2026-06-26
url: https://discourse.slicer.org/t/47472
last_bumped: 2026-11-04T01:36:05.058Z
---

# GUI panels from Slicer 5.12.0 shows over other software on Windows 11

**Topic ID**: 47472
**Date**: 2026-06-26
**URL**: https://discourse.slicer.org/t/gui-panels-from-slicer-5-12-0-shows-over-other-software-on-windows-11/47472

---

## Post #1 by @Esteban_Barreiro (2026-06-26 14:42 UTC)

<p>Hello.</p>
<p>I’m experiencing some GUI glitches in the Slicer 5.12.0 version.</p>
<p>Some of the menus, from the Red, Green, Yellow viewers stay visible over every other software. I’m on Windows 11.</p>
<p>In the attached image you can see some Slicer menus showing over other software (Paint)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc.jpeg" data-download-href="/uploads/short-url/97p6MU12JGbvgU9fvaKaYOnWy7y.jpeg?dl=1" title="Captura de pantalla 2026-06-26 113730" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_690x371.jpeg" alt="Captura de pantalla 2026-06-26 113730" data-base62-sha1="97p6MU12JGbvgU9fvaKaYOnWy7y" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fe9da8059826c144376f16dda115ea2ad8d6fbc_2_1380x742.jpeg 2x" data-dominant-color="87878C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2026-06-26 113730</span><span class="informations">1917×1032 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2026-06-28 12:37 UTC)

<p>It seems that it is related to pinning the ciew controllers to keep them always visible. Could you please try if tou can reproduce it with Slicer-5.10?</p>

---

## Post #3 by @Esteban_Barreiro (2026-06-28 19:47 UTC)

<p>Hi Andras, thanks for your response.</p>
<p>It doesnt happen in the 5.10 version, just in 5.12.</p>

---

## Post #4 by @jamesobutler (2026-06-29 20:46 UTC)

<p>I can confirm this also happens using Slicer 5.12.0 on macOS. Below shows the pinned pop-up widget displaying over a Finder window. This seems to point to a possible CTK regression where this pop-up widget is maintained.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816.png" data-download-href="/uploads/short-url/aK1mo4PYUZ2HfeZc5qqvETcqx4a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_690x182.png" alt="image" data-base62-sha1="aK1mo4PYUZ2HfeZc5qqvETcqx4a" width="690" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_690x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816_2_1035x273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b49894ba6a8d4dea10012b156333d3a17ced816.png 2x" data-dominant-color="DCDCDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1258×333 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Esteban_Barreiro (2026-07-02 19:23 UTC)

<p>Hi!</p>
<p>Thanks for your response James.</p>
<p>I’m lacking of time, but, should we open a Bug Report on the bugtracker on Github? I’m afraid if I do it, maybe I can’t follow it up as is needed.</p>

---

## Post #6 by @Esteban_Barreiro (2026-11-02 22:15 UTC)

<p>Hello!</p>
<p>I’m trying to report this behavior using the Slicer Bug Tracker, but it looks the page <a href="https://issues.slicer.org/" rel="noopener nofollow ugc">issues.slicer.org</a> is broken. It shows “ERR_CONNECTION_CLOSED”.</p>

---

## Post #7 by @pieper (2026-11-02 23:24 UTC)

<p>Thanks for reporting.  <a href="http://slicer.org">slicer.org</a> was down for a few days, but it’s back now, but probably not all the subdomains have been transferred.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> do we have a way to get a list of the subdomains that should still be set up?  Maybe an AI could build the list for us.</p>

---

## Post #8 by @Sam_Horvath (2026-11-02 23:36 UTC)

<p>I’ll get the redirect fixed up, it’s pretty much the only one that is broken.</p>

---

## Post #9 by @Sam_Horvath (2026-11-02 23:51 UTC)

<p>Please report issues on the Slicer Github, that is where the URL would be pointing anyway</p>

---

## Post #11 by @Esteban_Barreiro (2026-11-04 01:36 UTC)

<p>Done. Thanks!</p>
<aside class="onebox githubissue github-onebox" data-onebox-src="https://github.com/Slicer/Slicer/issues/9532">
    <header class="source github-onebox__header">
  <span class="github-onebox__label" role="img" aria-label="Open issue" title="Open issue">
    <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path></svg>
    <span>Open issue</span>
  </span>
    <a class="github-onebox__repo" href="https://github.com/Slicer/Slicer/issues/9532" target="_blank" rel="noopener nofollow ugc">
      <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656"></path></svg>
      <span>Slicer/Slicer</span>
    </a>
</header>


  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9532" target="_blank" rel="noopener nofollow ugc">GUI glitches in Slicer v5.12.x</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-11-03" data-time="16:52:04" data-timezone="UTC">04:52PM - 03 Nov 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/EstebanBarreiro" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/190802980?v=4" class="onebox-avatar-inline" width="20" height="20">
          EstebanBarreiro
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Pinned view controllers and pop-ups glitches on Windows 11.
Some of the menus, f<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">rom the Red, Green and Yellow viewers stay visible over every other software .

    1. Pin controllers on Green, Yellow, Red viewers to keep them always visible, (also display pop-ups)
    2. Slicer does pinned view controllers stays visible over any other software.
 
- Slicer version: Slicer-5.12.x r34645 / 4e21c19 (every 5.12 version) - built 2026-09-09
- Operating system: Windows 11.
- Same bug described for macOS in this thread: [https://discourse.slicer.org/t/gui-panels-from-slicer-5-12-0-shows-over-other-software-on-windows-11/47472](https://discourse.slicer.org/t/gui-panels-from-slicer-5-12-0-shows-over-other-software-on-windows-11/47472)

&lt;img width="1919" height="1031" alt="Image" src="https://github.com/user-attachments/assets/90d5dab1-e639-418d-913f-78ada4f91a38" /&gt;
&lt;img width="1873" height="953" alt="Image" src="https://github.com/user-attachments/assets/71e6deac-78ba-4594-826f-79a760287b2e" /&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
