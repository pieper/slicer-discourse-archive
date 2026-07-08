---
topic_id: 47550
title: "Nninteractive (slicer client) is stuck"
date: 2026-07-06
url: https://discourse.slicer.org/t/47550
last_bumped: 2026-07-07T16:37:59.509Z
---

# Nninteractive (slicer client) is stuck

**Topic ID**: 47550
**Date**: 2026-07-06
**URL**: https://discourse.slicer.org/t/nninteractive-slicer-client-is-stuck/47550

---

## Post #1 by @muratmaga (2026-07-06 14:11 UTC)

<p>It doesn’t pass this stage during the module initialization. This is on ubuntu 24.04</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e4efe878577b8e294e58879f2982f8a55592cb6.jpeg" data-download-href="/uploads/short-url/22zVB4dmuusLLOkx42U5i3eB0i2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4efe878577b8e294e58879f2982f8a55592cb6_2_690x394.jpeg" alt="image" data-base62-sha1="22zVB4dmuusLLOkx42U5i3eB0i2" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4efe878577b8e294e58879f2982f8a55592cb6_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4efe878577b8e294e58879f2982f8a55592cb6_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4efe878577b8e294e58879f2982f8a55592cb6_2_1380x788.jpeg 2x" data-dominant-color="9EA0A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1099 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Switch to module:  “SlicerNNInteractive”<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject: Cannot create children for a parent that is in a different thread.<br>
(Parent is qSlicerModuleManager(0x3d3c9760), parent’s thread is QThread(0x3b1f83f0), current thread is QThread(0x40e44840)<br>
QObject::startTimer: Timers can only be used with threads started with QThread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread<br>
QObject::setParent: Cannot set parent, new parent is in a different thread</p>

---

## Post #2 by @muratmaga (2026-07-06 14:17 UTC)

<p>Seems to happen on windows too.</p>

---

## Post #3 by @pieper (2026-07-06 17:47 UTC)

<p>Thanks for reporting <a class="mention" href="/u/muratmaga">@muratmaga</a>.  Yes, I noticed this too and it’s been investigated.  Probably there will be a fix in 5.12.1.  <a class="mention" href="/u/ebrahim">@ebrahim</a> do you think that’s possible?</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/9256">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/9256" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/9256" target="_blank" rel="noopener">Crash running nnInteractive extension</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-06-25" data-time="21:23:36" data-timezone="UTC">09:23PM - 25 Jun 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Pip install dialog crashes during module setup.

## Steps to reprodu<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ce

* Install nnInteractive extension
* restart slicer
* enter module 
* dialog flashes and then crash


## Environment
- Slicer version: Slicer-5.11.0-2026-06-15
- Operating system: Mac + 26.5.1 (25F80)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @ebrahim (2026-07-06 18:41 UTC)

<p>The fix would be in NNInteractive and not in Slicer, right? I’m looking at where the discussion ended in <a href="https://github.com/Slicer/Slicer/issues/9256">the issue</a></p>

---

## Post #5 by @ebrahim (2026-07-06 19:14 UTC)

<p>Will be addressed here: <a href="https://github.com/coendevente/SlicerNNInteractive/pull/100" class="inline-onebox">BUG: Avoid threaded pip install with Slicer 5.12 by ebrahimebrahim · Pull Request #100 · coendevente/SlicerNNInteractive · GitHub</a></p>

---

## Post #6 by @muratmaga (2026-07-06 19:37 UTC)

<p>This is nice, but given that the author of the extension hasn’t interacted with any of the PRs from the last 3-4 months (including the one <a class="mention" href="/u/lassoan">@lassoan</a> introduced for self-contained installation), that’s probably not going to get merged anytime soon.</p>

---

## Post #7 by @pieper (2026-07-06 23:28 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a>, since the extension worked in 5.10, and then crashes 5.12 I think this is a Slicer regression and we should somehow make it failsafe.  We don’t know who else might have depended on this older behavior.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> FYI, the DKFZ team behind nnInteractive contacted me and <a class="mention" href="/u/lassoan">@lassoan</a> that that will be making an updated SlicerNNInteractive extension available but it’s not ready yet.  This will support a new version with improved features.  So things are in flux for a while.</p>

---

## Post #8 by @ebrahim (2026-07-07 13:39 UTC)

<p>It’s more of an API change than a regression.</p>
<p>5.10 to 5.12 API change is acceptable, the extension has to be updated to adapt. If the extension is abandoned by the original author and we still want it in 5.12, then we can fork it. But I feel it’s too early to call it abandoned.</p>
<p>When we were putting together <code>slicer.packaging</code> we had to make a choice as to whether the progress bar is given to everyone using <code>pip_install</code> by default or whether it’s opt-in. In one case many extensions get automatic benefit while a few extensions need to be updated, and in the other case only extensions that update to explicitly invoke the new functionality get the benefit. Andras and I thought about this and opted for the first one.</p>

---

## Post #9 by @ebrahim (2026-07-07 14:00 UTC)

<p>Hmm… on more thought I suppose a failsafe within Slicer is easy</p>
<p>But this would not be us fixing a regression. This would be us being nice, which I guess we should be <img src="https://emoji.discourse-cdn.com/twitter/neutral_face.png?v=15" title=":neutral_face:" class="emoji" alt=":neutral_face:" loading="lazy" width="20" height="20"></p>
<p>I think I can get a failsafe out soon</p>

---

## Post #10 by @lassoan (2026-07-07 16:37 UTC)

<p>We discussed this at the developer meeting and <a class="mention" href="/u/ebrahim">@ebrahim</a> will try to get a fix in Slicer-5.12.1 (only add progress bar if <code>pip_install</code> is called from the main thread).</p>

---
