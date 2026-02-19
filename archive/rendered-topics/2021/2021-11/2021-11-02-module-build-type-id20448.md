---
topic_id: 20448
title: "Module Build Type"
date: 2021-11-02
url: https://discourse.slicer.org/t/20448
---

# Module build type

**Topic ID**: 20448
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/module-build-type/20448

---

## Post #1 by @kookoo9999 (2021-11-02 03:04 UTC)

<p>Hello all.<br>
I built my module by extension wizard in build type : debug of Slicer Master(S4D).<br>
and I added my moudle(moduel build type:debug) (in S4D) and checked moudle done well.<br>
but I coudn’t add my module to Slicer Release type so I tried to build my moudle for Release and build(release) is failed…<br>
I want to add my module to stable released Slicer app , and when I’m making my module, I want to debug my module.<br>
How Can I to do for this issue??</p>

---

## Post #2 by @lassoan (2021-11-02 20:15 UTC)

<p>Binaries built in debug mode are incompatible with binaries build in release mode. You need to build Slicer and your module in the same mode.</p>
<p>There can be other incompatibilities (compilation flags, build options, C runtime library differences, etc.) between binaries built on different computers, so in general you cannot expect that the module that you build on your own computer will be compatible with the Slicer application built on the official Slicer build machines. Therefore, the recommended, officially supported options are:</p>
<ol>
<li>Build and package Slicer application and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#extensions-build-system">all extensions</a> yourself. You can create a custom application (with custom name, logo, etc.). Bundling all extensions into your custom Slicer package is recommended because you probably don’t want to set up your own extension server.</li>
<li>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#distribute-an-extension">Use Slicer’s extension manager to distribute your extension</a>.</li>
</ol>

---

## Post #3 by @kookoo9999 (2021-11-03 01:13 UTC)

<p>Thansk you <a class="mention" href="/u/lassoan">@lassoan</a>  for reply <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I understand your comment!<br>
If I want to add my moudle to Commercial Slicer(usually download Slicer.exe) , I have to build a Release version of Slicer.<br>
So I’ve decided to build and make in Release.</p>
<p>What I understand is that there is no problem with making my module based on the result of Slicer’s Segmentation Module (requires the Segmentato function). Is this right?</p>
<p>When you work on creating my module in a release environment, how do you debug?<br>
I think of a way to use breakpoint without using debug option.</p>
<p>Thanks for your reading!</p>

---

## Post #4 by @lassoan (2021-11-03 04:30 UTC)

<aside class="quote no-group" data-username="kookoo9999" data-post="3" data-topic="20448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>When you work on creating my module in a release environment, how do you debug?<br>
I think of a way to use breakpoint without using debug option.</p>
</blockquote>
</aside>
<p>You often use a debug-mode build during development. When you are done with the debugging or want to test the application at full speed or distribute it to users then you build in release mode.</p>
<aside class="quote no-group" data-username="kookoo9999" data-post="3" data-topic="20448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kookoo9999/48/12394_2.png" class="avatar"> kookoo9999:</div>
<blockquote>
<p>What I understand is that there is no problem with making my module based on the result of Slicer’s Segmentation Module (requires the Segmentato function). Is this right?</p>
</blockquote>
</aside>
<p>Most likely you don’t actually need to modify the Segmentations module. Customizing the Segment Editor module (clone it an make it more convenient for your use case) makes sense.</p>

---

## Post #5 by @kookoo9999 (2021-11-03 05:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for reply! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You often use a debug-mode build during development. When you are done with the debugging or want to test the application at full speed or distribute it to users then you build in release mode.</p>
</blockquote>
</aside>
<p>Okay I often build in debug type and when I want to test or distribute, I will work in release type!!</p>
<p>Thanks.</p>

---
