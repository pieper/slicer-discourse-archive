# How can I find the error log after a crash?

**Topic ID**: 24389
**Date**: 2022-07-19
**URL**: https://discourse.slicer.org/t/how-can-i-find-the-error-log-after-a-crash/24389

---

## Post #1 by @wrc (2022-07-19 10:23 UTC)

<p>Hi, I am developing an extension based on ParrallelProcessing. It works well in most cases but fails sometimes. The 3D Slicer window closes automatically during calculation. So I cannot find the log on view-error log. Does 3D Slicer save logs in any folder? I would like to know the path on both Windows and MacOS.</p>

---

## Post #2 by @cpinter (2022-07-19 15:20 UTC)

<p>You can find past logs in the menu <code>Help / Report a bug</code></p>

---

## Post #3 by @pieper (2022-07-19 16:36 UTC)

<p>It’s possible that some error or log messages from subprocesses launched by ParallelProcesses are not logged.  If you think that’s happening maybe you can design a test case based on your experience and we can add proper logging to the extension.</p>

---

## Post #4 by @wrc (2022-07-21 00:56 UTC)

<p>Thank you for your reply. I found the error may come from:<br>
<code>self.start("PythonSlicer", [self.scriptPath,])</code> in <code>Process.run()</code></p>
<p>Now I want to check is there any wrong in my parallel script. However, 3D Slicer cannot show any log in the parallel script. Also, file output like numpy.savetxt is not allowed. Do you know how to show log in the parallel script?</p>

---

## Post #5 by @lassoan (2022-07-21 09:27 UTC)

<aside class="quote no-group" data-username="wrc" data-post="4" data-topic="24389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/6de8d8/48.png" class="avatar"> wrc:</div>
<blockquote>
<p>Also, file output like numpy.savetxt is not allowed. Do you know how to show log in the parallel script?</p>
</blockquote>
</aside>
<p>We don’t do anything that would interfere with numpy, so <code>numpy.savetxt</code> should work well. What errors do you get?</p>
<p>I’ve submitted a <a href="https://github.com/pieper/SlicerParallelProcessing/pull/11">pull request</a> that makes the captures the log of the background process and adds it to the application log, which should help with finding any errors.</p>

---
