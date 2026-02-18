# About the time.sleep

**Topic ID**: 10171
**Date**: 2020-02-09
**URL**: https://discourse.slicer.org/t/about-the-time-sleep/10171

---

## Post #1 by @timeanddoctor (2020-02-09 12:02 UTC)

<pre><code>for _ in range(20):
	n += 1
	print('n')
	time.sleep(1)
</code></pre>
<p>The printing results seems to be printed in the last time… Can I replace the time.sleep in slicer for waiting time?</p>

---

## Post #2 by @pieper (2020-02-09 16:32 UTC)

<p>Hi <a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> -</p>
<p>The native python <code>time</code> package is not integrated with the Slicer application event loop, managed by Qt.  So you need to use <a href="https://doc.qt.io/qt-5/qtimer.html"><code>QTimer</code></a> methods instead.</p>
<p>Something like this:</p>
<pre><code class="lang-auto">for i in range(5):
   qt.QTimer.singleShot(1000*i, lambda i=i: print(i))
</code></pre>
<p>The other advantage is that the application will remain responsive while waiting for the time to elapse.  Of course working asynchronously with the event loop is different from conventional sequential programming models, but it’s central to how the application works.</p>

---

## Post #3 by @lassoan (2020-02-10 00:55 UTC)

<p>If you must stay in a processing loop and still want to update the GUI then you can call <code>slicer.app.processEvents()</code>:</p>
<pre><code class="lang-python">for n in range(20):
    print(n)
    time.sleep(1)
    slicer.app.processEvents()  # update GUI
</code></pre>

---
