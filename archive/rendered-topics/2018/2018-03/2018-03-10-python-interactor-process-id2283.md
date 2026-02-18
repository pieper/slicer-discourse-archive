# Python Interactor process

**Topic ID**: 2283
**Date**: 2018-03-10
**URL**: https://discourse.slicer.org/t/python-interactor-process/2283

---

## Post #1 by @Fadwa_Darwaish (2018-03-10 22:06 UTC)

<p>I would like to know the process name/number to link to the Python interactor</p>
<p>Thank you<br>
Fadwa</p>

---

## Post #2 by @jcfr (2018-03-10 22:13 UTC)

<p>Hi Fadwa,</p>
<p>Since python is embedded into Slicer, getting the PID of the application  should answer  the question.</p>
<p>Here are the command you can enter in the interactor:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.app.applicationPid()
18082L
</code></pre>
<p>On unix, this is the same value that would be returned by the <code>ps</code> command:</p>
<pre><code class="lang-auto"> ps aux | grep Slicer
jcfr     18080  0.0  0.0 141592 12672 pts/4    Sl+  17:08   0:00 ./Slicer
jcfr     18082  2.2  0.6 4416196 405612 pts/4  SNl+ 17:08   0:03 /home/jcfr/Projects/Slicer-Qt5-VTK9-RelWithDebInfo/Slicer-build/bin/./SlicerApp-real
</code></pre>

---
