---
topic_id: 40678
title: "Flickering Issues On Ubuntu 24 04"
date: 2024-12-13
url: https://discourse.slicer.org/t/40678
---

# Flickering Issues on Ubuntu 24.04

**Topic ID**: 40678
**Date**: 2024-12-13
**URL**: https://discourse.slicer.org/t/flickering-issues-on-ubuntu-24-04/40678

---

## Post #1 by @Kulizoop (2024-12-13 12:09 UTC)

<p>Dear Community,</p>
<p>I upgraded from Ubuntu 22.04 to 24.04 and since then, Slicer is constantly flickering when using it.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a5d12991508e6950a92e56140d7f2a460a06390.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f2bb3bf7a8641d8d118128658802b6f4c706873.jpeg">
  </div><p></p>
<p>Does anybody else experience the same issues or knows where this might come from?</p>
<p>I use 5.7 but the issue also appears in 5.6.</p>
<p>Thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @cpinter (2024-12-13 16:29 UTC)

<p>We use 24.04 and there is no flickering. Maybe the display drivers have been upgraded incorrectly? I’d start there (but I’m no Linux expert)</p>

---

## Post #3 by @Kulizoop (2024-12-15 18:12 UTC)

<p>I have found out that the issue only appears on wayland and not on xorg.</p>
<p>So the drivers are up-to-date and seem to be okay - but thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I too don’t understand enough why Xorg works and wayland does not, but this seems to be a temporary fix.</p>

---

## Post #4 by @chir.set (2024-12-15 18:29 UTC)

<aside class="quote no-group" data-username="Kulizoop" data-post="3" data-topic="40678">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/aca169/48.png" class="avatar"> Kulizoop:</div>
<blockquote>
<p>on wayland and not on xorg</p>
</blockquote>
</aside>
<p>I don’t have flickering issues on Wayland in Arch. There are other troubles like excessive console messages, splash screen and other windows strictly positioned according to KDE rules with self-built Slicer but not with  downloadable factory archive.</p>
<p>All these are resolved however with:</p>
<blockquote>
<p>export QT_QPA_PLATFORM=“xcb”</p>
</blockquote>
<p>You may add this line to a startup bash script to simplify things, if it’s not done already.</p>

---

## Post #5 by @Kulizoop (2024-12-19 11:09 UTC)

<p>Thank you for your answer. I have no experience with bash scripts, so the following 2 lines are what I use. However, this does not fix the issue yet</p>
<pre><code class="lang-auto">#!/bin/bash
export QT_QPA_PLATFORM="xcb"
/opt/Slicer5.7.0/Slicer "$@"
</code></pre>

---

## Post #6 by @Kulizoop (2025-03-11 14:12 UTC)

<p>The problem was entirely removed by upgrading the nvidia driver from 550 to 570.</p>

---
