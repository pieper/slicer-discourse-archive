# MacBook Air M2 for 3D Slicer

**Topic ID**: 25354
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/macbook-air-m2-for-3d-slicer/25354

---

## Post #1 by @MZA (2022-09-20 11:13 UTC)

<p>Hi,<br>
Does the new MacBook Air M2 with 8-core GPU and 8 GB of RAM meet the requirements to run 3D Slicer smoothly?<br>
Respects,</p>

---

## Post #2 by @pieper (2022-09-20 11:47 UTC)

<p>Yes, in my experience for routine Slicer tasks it works well.</p>

---

## Post #3 by @jamesobutler (2022-09-20 12:06 UTC)

<p>There have been some reports of issues using the scissors tool in the Segment Editor module on Apple Silicon based machines.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6490">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6490" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6490" target="_blank" rel="noopener nofollow ugc">Slowdowns or hangs when running on ARM (M1) Mac systems</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-08-04" data-time="05:47:24" data-timezone="UTC">05:47AM - 04 Aug 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Two users reported slowdowns when using M1 mac systems:

&gt; I’m u<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">sing 3D Slicer 4.11.20210226 (latest at time of writing) on my Windows PC without any performance issues, and I can segment CT scans (thorax, abdomen, wrists, etc) without any performance issues. Unfortunately I’m experiencing severe performance issues with the same version, and also 4.13.0-2022-03-15, on my MacBook Pro M1 (2020, 16 GB, macOS Monterey 12.3). I’m getting either a ever-lasting spinning beach ball or it crashes. I’ve tried it without any plugins. 

https://discourse.slicer.org/t/performance-issues-on-mac-m1/22564

https://discourse.slicer.org/t/issues-running-slicer-on-macbook-m1-max/23974/3

## Environment

- MacBook Pro M1 (2020, 16 GB, macOS Monterey 12.3)
- MacBook M1 max</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @pieper (2022-09-20 12:49 UTC)

<p>I haven’t been able to reproduce the reported slowdowns on the M2 mac air, even with the scene provided by <a class="mention" href="/u/sannpeterson">@sannpeterson</a>.  It would be good to hear what experience other people are having.  It’s possible that an OS update fixed some issue or other.</p>

---

## Post #5 by @hherhold (2022-09-20 12:53 UTC)

<p>(apologies for the slightly off-topic question, but I’m hoping M1 and M2 users could chime in…)</p>
<p><a class="mention" href="/u/pieper">@pieper</a>, have you done any volume rendering on an M1 or M2 Mac? I’m curious about the “unified” CPU and GPU ram, and how that’s handled with large datasets.</p>

---

## Post #6 by @pieper (2022-09-20 12:58 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> I haven’t done extensive testing, but it seems pretty good for a lightweight laptop.  If I use the CTACardio sample data I notice some slowdown if I maximize the 3D view.</p>

---

## Post #7 by @hherhold (2022-09-20 12:59 UTC)

<p>Hmm, sounds good. (Always thinking of the next computer.)</p>
<p>Thanks!!!</p>

---

## Post #8 by @pieper (2022-09-20 13:28 UTC)

<p>For comparison, my 3 year old mac pro with AMD Radeon Pro W5700X 16 GB doesn’t show much slowdown for the same data on a 4k monitor (of course the mac pro is like 100 times bigger!)</p>

---

## Post #9 by @hherhold (2022-09-20 13:32 UTC)

<p>Yeah, my 2019 MBP 16" with AMD Radeon Pro 5500M 8 GB still does quite well. A little concerned over the loss of a discrete GPU in the new Macs.</p>
<p>But that’s a problem for another day</p>
<p>Thanks again!</p>

---

## Post #10 by @MZA (2022-09-21 16:57 UTC)

<p>You think if I do segmentation of cerebral arteries and veins I will face a slowdown?</p>

---

## Post #11 by @pieper (2022-09-21 21:27 UTC)

<p>I don’t know - if you know of a sample dataset of comparable complexity then people could try on various machines and compare results.</p>

---
