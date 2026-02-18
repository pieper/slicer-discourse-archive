# Slicer 4.10 not starting after fresh build

**Topic ID**: 4558
**Date**: 2018-10-27
**URL**: https://discourse.slicer.org/t/slicer-4-10-not-starting-after-fresh-build/4558

---

## Post #1 by @christian (2018-10-27 20:32 UTC)

<p>Hi,</p>
<p>I just build Slicer 4.10 with Qt5 and VTK8 from source on a linux machine (Linux Mint 19). The problem is that Slicer does not start and throws this message:</p>
<pre><code class="lang-auto">./Slicer-build/Slicer
</code></pre>
<pre><code class="lang-auto">qt5ct: using qt5ct plugin
error: [/home/christian/builds/Slicer-4.10.0-build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>If I run Slicer with the gdb flag I got the following message:</p>
<pre><code class="lang-auto">./Slicer-build/Slicer --gdb
</code></pre>
<pre><code class="lang-auto">Fatal Python error: Py_Initialize: Unable to get the locale encoding
  File "/home/christian/builds/Slicer-4.10.0-build/python-install/lib/python2.7/encodings/__init__.py", line 123
    raise CodecRegistryError,\
                            ^
SyntaxError: invalid syntax

Current thread 0x00007f1fbeb25f80 (most recent call first):
error: [/usr/bin/gdb] exit abnormally - Report the problem.
</code></pre>
<p>So I guess something went wrong with the python installation. Unfortunatly I have no idea how to solve that problem. It would be great if you can help me.</p>

---

## Post #2 by @pieper (2018-10-28 15:43 UTC)

<p>Starting up with gdb is the right approach, and yes, you want to use the launcher for that if you can but there can be conflicts between gdb’s python and the environment Slicer needs to start up.  Refer to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions">this documentation.</a></p>
<p>In this case the SyntaxError in the encodings file is odd - maybe you can try patching around that and then retrying?</p>

---

## Post #3 by @lassoan (2018-10-28 16:24 UTC)

<aside class="quote no-group" data-username="christian" data-post="1" data-topic="4558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b2d939/48.png" class="avatar"> christian:</div>
<blockquote>
<p>Py_Initialize: Unable to get the locale encoding</p>
</blockquote>
</aside>
<p>This error reported to occur when Slicer’s embeded Python environment is mixed with some other Python environments. See this post for details: <a href="https://discourse.slicer.org/t/python-real-different-from-python-interpreter/2496/2" class="inline-onebox">python-real different from python interpreter - #2 by jcfr</a>. <a class="mention" href="/u/pieper">@pieper</a>’s suggestion above should fix the gdb launching issue and then hopefully you can find the root cause of the crash.</p>

---

## Post #4 by @jcfr (2018-10-29 10:25 UTC)

<p>Hi Christian,</p>
<p>Instead of starting Slicer with gdb, I suggest you attached the debugger. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#GDB_debug_by_attaching_to_running_process_.5BRECOMMENDED.5D">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#GDB_debug_by_attaching_to_running_process_.5BRECOMMENDED.5D</a></p>
<p>Alternatively, you could also debug the Qt plugin loading setting up the environment variable <code>QT_DEBUG_PLUGINS</code>:</p>
<pre><code class="lang-auto">QT_DEBUG_PLUGINS=1 ./Slicer
</code></pre>
<p>See <a href="http://doc.qt.io/qt-5/debug.html#environment-variables-recognized-by-qt">http://doc.qt.io/qt-5/debug.html#environment-variables-recognized-by-qt</a></p>

---

## Post #5 by @christian (2018-10-29 20:19 UTC)

<p>Thanks for all the quick responses. I will try on Wednesday.</p>

---
