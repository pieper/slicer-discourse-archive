---
topic_id: 25849
title: "How Does 3Dslicer Compile Offline Locally"
date: 2022-10-23
url: https://discourse.slicer.org/t/25849
---

# How does 3Dslicer compile offline locally

**Topic ID**: 25849
**Date**: 2022-10-23
**URL**: https://discourse.slicer.org/t/how-does-3dslicer-compile-offline-locally/25849

---

## Post #1 by @lhf (2022-10-23 13:02 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2022-10-23 13:03 UTC)

<p>See build instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">here</a>.</p>

---

## Post #3 by @lhf (2022-10-24 02:24 UTC)

<p>If I download all of 3DSLICER’s libraries locally, can I compile them on my computer without the network?</p>

---

## Post #4 by @lassoan (2022-10-24 02:39 UTC)

<p>Slicer need to download dozens of additional libraries. You can download all the packages, github repositories, etc. manually and configure the build to use those. For example, it should be possible to replace each reference to a <code>github.com/...</code> git repository by a local folder; set up pip to install packages from already downloaded files, etc.</p>
<p>You may also just build Slicer once to automatically download all dependencies, inspect them, and after that build again from those sources without network connection.</p>
<p>What is the reason for needing a build without network connection?</p>

---

## Post #5 by @lhf (2022-10-24 02:49 UTC)

<p>thank,Local compilation does not require downloading the corresponding library from the Internet, which improves the speed of compilation.</p>

---

## Post #6 by @lhf (2022-10-24 02:53 UTC)

<p>If I download all of Slicer’s dependent libraries, how do I configure it (or configure it via cmake) so that I can compile locally without connecting to the network?</p>

---

## Post #7 by @lassoan (2022-10-24 03:52 UTC)

<aside class="quote no-group" data-username="lhf" data-post="5" data-topic="25849">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/9de0a6/48.png" class="avatar"> lhf:</div>
<blockquote>
<p>Local compilation does not require downloading the corresponding library from the Internet,</p>
</blockquote>
</aside>
<p>Network access does not significantly affect the build time. The first build may be slightly slower if you have a very, very slow network, but typically you download a library in a few ten seconds, but then build may takes tens of minutes. Also, this only slows down the first build. During subsequent builds, there is just a quick check if something is changed in the remote repository.</p>

---

## Post #8 by @lhf (2022-10-24 04:05 UTC)

<p>Thank you very much for your reply.</p>

---
