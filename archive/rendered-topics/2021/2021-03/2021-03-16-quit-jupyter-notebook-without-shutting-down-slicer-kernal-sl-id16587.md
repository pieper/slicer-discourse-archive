# Quit Jupyter notebook without shutting down Slicer kernal - Slicer instance is persisting

**Topic ID**: 16587
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/quit-jupyter-notebook-without-shutting-down-slicer-kernal-slicer-instance-is-persisting/16587

---

## Post #1 by @Carly_L (2021-03-16 23:50 UTC)

<p>Hello,</p>
<p>I was running a Jupyter notebook script connected to a Slicer kernel. I accidentally quite the instance of Jupyter notebook (closed out of the window in browser) without first shutting down the Slicer kernel. Now I have an instance of Slicer that still says “Application is managed by Jupyter” and if closed it reopens itself.</p>
<p>Restarting the computer did not resolve the issue (this has worked in the past but isn’t in this current case). Reopening Jupyter in the browser did not help, as it doesn’t recognize any kernels as being open/running.</p>
<p>Does anyone know of a way to kill the Slicer instance that is being managed by Jupyter if Jupyter doesn’t seem to recognize the connection?</p>
<p>Thank you in advance for any assistance!<br>
-Carly</p>

---

## Post #2 by @lassoan (2021-03-26 03:22 UTC)

<p>This is a very common complaint for Jupyter.</p>
<aside class="quote no-group" data-username="Carly_L" data-post="1" data-topic="16587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carly_l/48/4271_2.png" class="avatar"> Carly_L:</div>
<blockquote>
<p>Restarting the computer did not resolve the issue</p>
</blockquote>
</aside>
<p>Restarting the computer should resolve this because Jupyter server is shut down when you restart your computer and the server is not started automatically when you log in. Hibernating or putting your computer to sleep will not help, as it does not shut down applications.</p>
<aside class="quote no-group" data-username="Carly_L" data-post="1" data-topic="16587">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carly_l/48/4271_2.png" class="avatar"> Carly_L:</div>
<blockquote>
<p>Does anyone know of a way to kill the Slicer instance that is being managed by Jupyter if Jupyter doesn’t seem to recognize the connection?</p>
</blockquote>
</aside>
<p>You can get the URL of running jupyter servers (so that you can open them in your web browser and shut down) as described <a href="https://github.com/Slicer/SlicerJupyter#shutdown-all-slicer-jupyter-kernels">here</a>.</p>
<p>Alternatively, you can open Windows Task manager, go to “Details” tab, right-click on each <code>python-real.exe</code> process and choose “End task”.</p>

---

## Post #3 by @Carly_L (2021-03-26 16:07 UTC)

<p>Thank you Andras!</p>
<p>The problem does appear to have resolved after a couple more restarts - not sure why the first attempts with that did not work; it sounds like they should have based on the way the Jupyter server is set up.</p>
<p>Thank you also for the information about getting the URL of the running Jupyter servers and the approach of using Windows Task Manager as an alternative approach. Greatly appreciate your helpful advice on this issue!</p>

---
