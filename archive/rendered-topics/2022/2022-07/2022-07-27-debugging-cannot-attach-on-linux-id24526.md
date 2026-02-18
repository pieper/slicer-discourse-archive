# Debugging cannot attach on Linux?

**Topic ID**: 24526
**Date**: 2022-07-27
**URL**: https://discourse.slicer.org/t/debugging-cannot-attach-on-linux/24526

---

## Post #1 by @cpinter (2022-07-27 12:49 UTC)

<p>Hi all,</p>
<p>I’m trying to debug Slicer (few commits after 5.0.3) on Ubuntu 20.04. I built Slicer in debug mode, and tried the following:</p>
<ul>
<li>Attach debugger from VS Code after starting the debug Slicer with its launcher (Slicer-build/Slicer), but specifying the PID of SlicerApp-real. It thinks for a while, then detaches itself, saying the process was “Killed” [1]</li>
<li>Launch Slicer from VS Code
<ul>
<li>It starts alright if I just specify SlicerApp-real, but then, because the environment is not set I guess, I cannot use SimpleITK, which would be needed to get to the point I want to debug</li>
<li>When I launch VS Code using the Slicer launcher, then try to launch SlicerApp-real, it gives me a traceback [2] and does not start Slicer</li>
</ul>
</li>
<li>Attach debugger using gdb. I get the exact same issue as the first bullet</li>
</ul>
<p>I did the permanent solution from the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html#gdb-debug-by-attaching-to-running-process-recommended">debug howto</a> (editing that file), but haven’t restarted the computer, not sure if it’s an issue.</p>
<p>[1]</p>
<pre><code class="lang-auto">[1] + Killed                     /usr/bin/pkexec "/usr/bin/gdb" --interpreter=mi --tty=${DbgTerm} 0&lt;"/tmp/Microsoft-MIEngine-In-14i5barx.5at" 1&gt;"/tmp/Microsoft-MIEngine-Out-0lrss5ki.qlq"
</code></pre>
<p>[2]</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/csaba/Slicer/sD/python-install/lib/python3.9/site.py", line 73, in &lt;module&gt;
    import os
  File "/home/csaba/Slicer/sD/python-install/lib/python3.9/os.py", line 29, in &lt;module&gt;
    from _collections_abc import _check_methods
  File "/home/csaba/Slicer/sD/python-install/lib/python3.9/_collections_abc.py", line 12, in &lt;module&gt;
    GenericAlias = type(list[int])
TypeError: 'type' object is not subscriptable
[1] + Done(1)                    "/usr/bin/gdb" --interpreter=mi --tty=${DbgTerm} 0&lt;"/tmp/Microsoft-MIEngine-In-p215jlbf.je2" 1&gt;"/tmp/Microsoft-MIEngine-Out-k3buhqsc.s15"
</code></pre>
<p>Any help would be appreciated. Thank you!</p>

---

## Post #2 by @cpinter (2022-08-01 09:29 UTC)

<p>I managed to attach the VS debugger to Slicer. Two things I did differently than the above. First, I restarted the computer (so maybe the “permanent solution” for debugging kicked in, not sure if it needed a restart), second, I attached the process during the PID window was shown (as in --attach-process). I managed to get a partial callstack, but then, when loading more of the stack gdb crashed. So still painful…</p>

---
