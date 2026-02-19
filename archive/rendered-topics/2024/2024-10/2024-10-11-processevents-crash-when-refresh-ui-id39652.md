---
topic_id: 39652
title: "Processevents Crash When Refresh Ui"
date: 2024-10-11
url: https://discourse.slicer.org/t/39652
---

# ProcessEvents crash when refresh UI

**Topic ID**: 39652
**Date**: 2024-10-11
**URL**: https://discourse.slicer.org/t/processevents-crash-when-refresh-ui/39652

---

## Post #1 by @fqzhice (2024-10-11 10:29 UTC)

<p>I capture real time video in  thread , process image  in slot fuction and try to force update result node in threeDViewWidget  by qSlicerApplication::application()-&gt;processEvents()<br>
slicer crash when run after several times.<br>
the whole process is about 60ms.<br>
How can i force update renderwindow.</p>
<pre><code>*auto threeDView = qSlicerApplication::application()-&gt;layoutManager() \*
</code></pre>
<ul>
<li>
<pre><code>  -&gt;threeDWidget(0)-&gt;threeDView();*
</code></pre>
</li>
<li>auto renderWindow = threeDView-&gt;renderWindow();*</li>
<li>renderWindow-&gt;Render();|*</li>
<li>//threeDView-&gt;forceRender();|*<br>
this has no change on View</li>
</ul>
<p>Any suggestion is very appreciated!</p>

---

## Post #2 by @pieper (2024-10-11 12:42 UTC)

<p>You need to use <code>processEvents</code> very carefully, as you can easily create event loops (e.g. a slot that itself calls <code>processEvents</code> and creates an infinite recursion).  It looks like you are using C++, so you can use a debugger to see what’s going on with your slots.</p>

---

## Post #3 by @lassoan (2024-10-11 13:32 UTC)

<p>We usually capture real-time video in a separate process (e.g, using <a href="https://plustoolkit.github.io/">PLUS</a>) and stream into Slicer via OpenIGTLink. Since the image acquisition happens in another process (we often do it on a different computer, e.g., an ultrasound system) it does not impact interactivity of the application, regardless of how long it takes to acquire (and potentially process, segment, etc.) an image. Running in a separate process also ensures that any instability in the image acquisition process (e.g., crash because the image acquisition hardware is disconnected) does not affect the application, but you can start/stop/restart the acquisition process anytime.</p>
<p>The OpenIGTLink interface module in Slicer takes care of thread-safe update of the images in the scene, so you will not have any crashes. OpenIGTLink is a very lightweight socket-based protocol, which typically adds just a couple of milliseconds latency.</p>
<p>If you insist on running the image acquisition in the same process then you just have to be really careful and knowledgeable. Calling <code>processEvents()</code> from a separate thread should not be necessary, as doing some operations on a background thread does not block the main thread, so event processing on the main thread is already running continuously. You must not call any GUI or rendering related methods from background threads (such as <code>forceRender</code>), because the application will crash. You must not modify the scene content from the background thread, because the application will crash. Instead you always call these methods and modify data on the main thread, based on information that the background thread provides to the main thread via thread-safe communication mechanisms (mutex, queue, etc.). These are all very basic concepts of concurrent processing, yet making everything work correctly usually becomes quite complex in the end. If you don’t want to spend significant amount of time learning all this and then debug random crashes then I would recommend to go with the already implemented and very thoroughly tested OpenIGTLink-based solution.</p>

---

## Post #4 by @fqzhice (2024-10-12 08:41 UTC)

<p>I add xxxnode-&gt;Modified before updateVolumeFromArray,<br>
instead of calling processEvents<br>
and it fixed.</p>

---
