---
topic_id: 47655
title: "Problem Downloading Slicer"
date: 2026-07-17
url: https://discourse.slicer.org/t/47655
last_bumped: 2026-07-17T15:33:21.109Z
---

# Problem Downloading Slicer

**Topic ID**: 47655
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/problem-downloading-slicer/47655

---

## Post #1 by @kikubamutwe (2026-07-17 13:14 UTC)

<p>I cannot complete the Slicer download.</p>
<p>I have tried using multiple connections in multiple countries (using various remote boxes) and each time the download fails partway through. Some of these connections have 1G capacities.</p>
<p>The download also cannot be resumed because of the server configuration, so using “wget -c” or “curl -c -” does not solve the problem.</p>
<p>Please provide direct download links that are resumable. This will fix the problem for many users.</p>

---

## Post #2 by @pieper (2026-07-17 15:33 UTC)

<p>I’ve always been able to use a command link this on a linux machine to get the latest Preview build.  Does it work for you?</p>
<pre><code class="lang-auto">(cd ~/Downloads; curl -L  "http://download.slicer.org/download?os=linux&amp;stability=any&amp;offset=0" | tar xvfz -)
</code></pre>
<p>Adding resumable downloads is something we’d like to do in the future but the current infrastructure does not support it.</p>

---
