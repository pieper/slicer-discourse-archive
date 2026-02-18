# Why is slicer very slow to start the first time，but fast to start the second time？

**Topic ID**: 31858
**Date**: 2023-09-23
**URL**: https://discourse.slicer.org/t/why-is-slicer-very-slow-to-start-the-first-time-but-fast-to-start-the-second-time/31858

---

## Post #1 by @icedream (2023-09-23 06:26 UTC)

<p>Is there a way to quickly open Slicer after restarting the computer?</p>

---

## Post #2 by @slicer365 (2023-09-23 07:42 UTC)

<p>Maybe you installed some modules and they need to download the specific python packages when first start.</p>

---

## Post #3 by @pieper (2023-09-23 14:52 UTC)

<p>Slicer uses a lot of shared libraries, so depending on your platform they may need to be reloaded and cached after rebooting.  What OS are you using?</p>

---

## Post #4 by @icedream (2023-09-24 03:52 UTC)

<p>thank you pieper , i use win11 for slicer , is it possible to cache the shared libraries in the background when the computer started use some script? these is friendly from some user who don’t familier with slicer.</p>

---

## Post #5 by @lassoan (2023-09-24 12:59 UTC)

<p>The easiest way to cache the binaries in memory would be to launch Slicer at startup with a script, without showing the application window. You can even make the application quit right after it started, but then if you use other applications then the binaries may be unloaded.</p>
<p>But there may be better ways to make Slicer available immediately when you need it (for example, using its server interface). Can you describe how you use Slicer and how the first longer startup time interferes with your workflow?</p>

---

## Post #6 by @icedream (2023-09-24 14:35 UTC)

<p>i use SlicerCAT for some hight school for custom application , I make some customized plugins for professors according to their needs，Slicer is a very powerful foundational framework with strong stability and scalability，But the first startup speed was a bit slow, and one professor asked me how to solve it, but I couldn’t think of a good solution，So I came to the community to ask for help，thank you very much for reply <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #7 by @pieper (2023-09-24 14:54 UTC)

<p>Thanks for the extra background <a class="mention" href="/u/icedream">@icedream</a> - if you are doing a custom app that only exposes a subset of features you might also want to disable any modules that you don’t need.  CLI and Shared modules can be turned off in cmake lists files (just comment them out or delete them) and that may improve startup time, speed your build time, and make your redistribution binary smaller too.</p>
<p>Starting the application at boot or login time is an option that some commercial software uses, but that tends to slow down the computer overall even when the user isn’t using the app, so I don’t like that option much unless you’re sure your app is the main purpose of the computer.</p>

---

## Post #8 by @icedream (2023-09-25 03:11 UTC)

<p>thank you pieper for repsponse<br>
The first suggestion on reducing unnecessary plugins is very good. I have already applied it in the project, which can significantly reduce some loading time and software package size<br>
The second suggestion is that I cannot solve the problem. I have provided the professor with a computer that can only run the Slicer program. If i want to accelerate the startup time of the Slicer program, are there any suggestions?</p>

---

## Post #9 by @pieper (2023-09-25 13:52 UTC)

<aside class="quote no-group" data-username="icedream" data-post="8" data-topic="31858">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/48db29/48.png" class="avatar"> icedream:</div>
<blockquote>
<p>I have provided the professor with a computer that can only run the Slicer program. If i want to accelerate the startup time of the Slicer program, are there any suggestions?</p>
</blockquote>
</aside>
<p>Since it’s a dedicated computer for this app, then setting it up so the app is loaded at startup or user login as <a class="mention" href="/u/lassoan">@lassoan</a> suggested makes sense.  The total time will be about the same but it may feel faster to the user.</p>
<p>The other, more in-depth approach would be to profile the app and see where the time is taken.  From previous experience I guess it’s loading shared libraries and creating the python bindings.  If your custom app is or could be pure C++, then you could turn off python completely.  It may also be possible to statically link much of the application, although that’s not the use case Slicer’s build and runtime systems are optimized for so you may hit some roadblocks.</p>

---

## Post #10 by @icedream (2023-09-25 14:10 UTC)

<p>Thanks for your patience <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
in your advice i think i can do the speed work in two ways<br>
1.the quick way : start slicer when the computer start in no gui mode<br>
2.the in-depth way:print every step slicer function time cost ,Find which steps can be optimized to save time</p>

---
