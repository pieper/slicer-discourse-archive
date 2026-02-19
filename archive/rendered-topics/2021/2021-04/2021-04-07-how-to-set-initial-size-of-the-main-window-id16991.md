---
topic_id: 16991
title: "How To Set Initial Size Of The Main Window"
date: 2021-04-07
url: https://discourse.slicer.org/t/16991
---

# How to set initial size of the main window?

**Topic ID**: 16991
**Date**: 2021-04-07
**URL**: https://discourse.slicer.org/t/how-to-set-initial-size-of-the-main-window/16991

---

## Post #1 by @spycolyf (2021-04-07 21:03 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>How do I set the initial size and location of the main SlicerQREADS window. A physician complained it comes up too small and I agreed. Any solutions?</p>
<p>Thanks</p>

---

## Post #2 by @jcfr (2021-04-07 21:16 UTC)

<blockquote>
<p>A physician complained it comes up too small and I agreed. Any solutions?</p>
</blockquote>
<p>Last size of application is currently saved in the settings after the application is closed.</p>
<p>How would like to compute the initial size ?</p>
<p>Once you answer that question, it will be possible setting <code>slicer.util.mainWindow().size</code> if it has not already been saved in the settings.</p>

---

## Post #3 by @spycolyf (2021-04-07 21:31 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="16991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Last size of application is currently saved in the settings after the application is closed.</p>
<p>How would like to compute the initial size ?</p>
<p>Once you answer that question, it will be possible setting <code>slicer.util.mainWindow().size</code> if it has not already been saved in the settings.</p>
</blockquote>
</aside>
<p>OK, for some reason, mine is not remembering from previous runs. Ok, I will try to look inti that. thanks</p>

---

## Post #4 by @pieper (2021-04-07 21:40 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="3" data-topic="16991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>OK, for some reason, mine is not remembering from previous runs.</p>
</blockquote>
</aside>
<p>I’ve seen this behavior on mac.</p>

---

## Post #5 by @pieper (2021-04-07 21:43 UTC)

<p>If you need a workaround you can also do something like <code>slicer.util.mainWindow().setGeometry(20,20, 500, 500)</code></p>

---

## Post #6 by @spycolyf (2021-04-07 22:07 UTC)

<p>Hello <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>That worked as far as being able to set the geometry, but it would be nice if I could, for instance, center it and set the size proportional to the screen geometry.</p>
<p>Thanks</p>

---

## Post #7 by @pieper (2021-04-07 22:13 UTC)

<p>yes, you can query the screen size from <code>slicer.app</code> and do all those calculations.  See <a href="https://doc.qt.io/qt-5/qguiapplication.html" class="inline-onebox">QGuiApplication Class | Qt GUI 5.15.3</a> and search for <code>screen</code> for details.</p>

---

## Post #8 by @spycolyf (2021-04-07 23:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="16991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>nd search for <code>screen</code> for details.</p>
</blockquote>
</aside>
<p>OK, I hope the save-settings thing starts working again. That would be best. This issue was actually mentioned by the chairman of the Apps Oversight Committee after my demo.</p>

---

## Post #9 by @spycolyf (2021-04-08 01:00 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>FYI: I won’t need this if it could remember the last geometry upon closing the window. That’s the root of the problem. So, if you could solve that, I’m cool.</p>

---

## Post #10 by @jcfr (2021-04-08 00:51 UTC)

<p>For reference, the setting of initial window size related to the SlicerQReads demo is now tracked in issue <a href="https://github.com/KitwareMedical/SlicerQReads/issues/62">SlicerQReads#62</a></p>

---

## Post #11 by @pieper (2021-04-08 20:40 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="9" data-topic="16991">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>FYI: I won’t need this if it could remember the last geometry upon closing the window.</p>
</blockquote>
</aside>
<p>I looked a couple times and it’s not instantly obvious.  It bugs me but not enough to fix it myself.</p>

---

## Post #12 by @jamesobutler (2021-04-08 20:52 UTC)

<p>For reference that issue regarding remembering window size on macOS is being tracked at <a href="https://github.com/Slicer/Slicer/issues/4601" class="inline-onebox" rel="noopener nofollow ugc">Settings save on application exit does not work · Issue #4601 · Slicer/Slicer · GitHub</a>.</p>

---

## Post #13 by @jamesobutler (2021-04-08 20:54 UTC)

<p>That GitHub issue is currently assigned to you <a class="mention" href="/u/pieper">@pieper</a>. If you don’t have plans to fix it, I guess you should remove yourself from the issue so that it doesn’t appear you are actively working on it or plan to work on it. I think it was assigned to you being a macOS user.</p>

---

## Post #14 by @pieper (2021-04-09 00:17 UTC)

<p>Thanks for making the link <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I unassigned myself so it’s up for grabs.  I could test if someone proposes a fix.</p>

---

## Post #15 by @spycolyf (2021-06-30 17:48 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Currently, when SlicerQREADS is launched for the first time, it sets the main window to a default size and then upon exiting, it stores the last size so that subsequent launches will bring up the window in in that size. Doctors are complaining about that initial size being too small. Could you please tell me where that initial default size is set?</p>
<p>Thanks</p>

---

## Post #16 by @pieper (2021-06-30 18:01 UTC)

<p>You can use the <code>--settings-path</code> option to find where the settings are installed on your system (<a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#user-specific-settings" class="inline-onebox">Application settings — 3D Slicer documentation</a>) and then you can pre-configure it for uses which ever values you prefer.  Compare the files before and after doing your config to decide what to change.</p>
<p>Another option is to change the default in your custom app (search the code for where the main window size is set).</p>

---

## Post #17 by @spycolyf (2021-07-01 15:29 UTC)

<p>Great!</p>
<p>So the setting is maintained in C:\Users\userID\AppData\Roaming\Mayo Clinic\SlicerQReads.ini</p>
<p>It resides in the [MainWindow] group and looks like this…</p>
<p><code>geometry=@ByteArray(\x1\xd9\xd0\xcb\0\x3\0\0\0\0\x2\x1d\0\0\x1\b\0\0\x5\x61\0\0\x3\x61\0\0\x2\x1e\0\0\x1'\0\0\x5</code>\0\0\x3<code>\0\0\0\0\0\0\0\0\a\x80\0\0\x2\x1e\0\0\x1'\0\0\x5</code>\0\0\x3<code>)</code></p>
<p>When I delete it, SlicerQREADS comes up very small. And then when I exit, the geometry parameter is created.</p>
<p>So I did as you said and pre-configured it by …</p>
<ol>
<li>Launching SlicerQREADS and setting the main window to the desired size, and then exiting</li>
<li>Copying the “geometry=” parameter from SlicerQReads.ini to the installation folder, C:\QREADS_3D_MPR\share\SlicerQReads-4.13\SlicerQReadsDefaultSettings.ini</li>
<li>Deleting the “geometry=” parameter from SlicerQReads.ini</li>
<li>Launched SlicerQREADS again and IT WORKED!!! YES!</li>
</ol>
<p>So I’m hoping that adding the “geometry=” parameter to my DefaultSettings.ini in my source C:\SlicerQREADS_Source\Applications\SlicerQReadsApp\Resources\Settings folder, will carry over to my build.</p>
<p>Thanks for the tip!</p>

---

## Post #18 by @jamesobutler (2021-07-01 15:37 UTC)

<p>Just curious, <a class="mention" href="/u/spycolyf">@spycolyf</a> what is the new desired initial window size? Upon first launching the Slicer app is it to be fully maximized? Then closing of the app saves the current size to be used in the next subsequent session.</p>

---

## Post #19 by @spycolyf (2021-07-01 15:48 UTC)

<p>Yes, fully maximized would be great. That would work for different monitor sizes. But, the ideal size would be the size and position of the QREADS app main window that launches SlicerQREADS via DOS command.</p>

---

## Post #20 by @spycolyf (2021-07-01 16:45 UTC)

<p>Hey <a class="mention" href="/u/jamesobutler">@jamesobutler</a> , why did you ask?</p>
<p>Is there an easy way to maximize it on initial launch?</p>

---

## Post #21 by @lassoan (2021-07-18 03:02 UTC)

<p>You can add <code>slicer.util.mainWindow().showMaximized()</code> to the startup script to maximize the window. You can use any other Qt functions to position the main window anywhere.</p>

---
