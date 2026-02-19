---
topic_id: 24260
title: "Sys Executable Is Different When Running From Slicer And Fro"
date: 2022-07-10
url: https://discourse.slicer.org/t/24260
---

# `sys.executable` is different when running from Slicer and from PythonSlicer

**Topic ID**: 24260
**Date**: 2022-07-10
**URL**: https://discourse.slicer.org/t/sys-executable-is-different-when-running-from-slicer-and-from-pythonslicer/24260

---

## Post #1 by @keri (2022-07-10 17:09 UTC)

<p>Hi,</p>
<p>I just noticed that when I check <code>sys.executable</code> from Slicer I get:</p>
<pre><code class="lang-auto">import sys; print(sys.executable)
C:/Users/kerim/AppData/Local/NA-MIC/Slicer 5.0.2/bin/PythonSlicer.exe
</code></pre>
<p>But if I run PythonSlicer and then run the same command I get <code>real</code> executable:</p>
<pre><code class="lang-auto">import sys; print(sys.executable)
C:\Users\kerim\AppData\Local\NA-MIC\Slicer 5.0.2\bin\python-real.exe
</code></pre>
<p>What is the possible reason for that?<br>
I would be glad if I could make <code>sys.executable</code> print as <code>PythonSlicer.exe</code> everywhere.</p>
<p>Official stable Slicer <code>5.0.2 r30822 / a4420c3</code> on Windows</p>

---

## Post #2 by @keri (2022-07-10 17:59 UTC)

<p>I’ve found where <a href="https://github.com/Slicer/Slicer/blob/115e32bdf8e478208fc2c75179cf2ecdb555d984/Base/QTCore/qSlicerCoreApplication.cxx#L1114-L1117" rel="noopener nofollow ugc">Slicer modifies the executable from python.exe to PythonSlicer.exe</a>.</p>
<p>Is there a way to modify <code>sys.executable</code> to <code>PythonSlicer.exe</code> when launching python outside Slicer (ie when launching directly from <code>PythonSlicer.exe</code>)? So that I could run <code>PythonSlicer.exe -c "import sys; print(sys.executable)"</code> and see <code>PythonSlicer.exe</code> as output</p>

---

## Post #3 by @jcfr (2022-07-11 19:25 UTC)

<p>To summarize, the value is currently set like this:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th><code>sys.executable</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Slicer</td>
<td><code>/path/to/PythonSlicer.exe</code></td>
</tr>
<tr>
<td>PythonSlicer</td>
<td><code>/path/to/python-real.exe</code></td>
</tr>
</tbody>
</table>
</div><p>In the past, the value associated with <code>sys.executable</code> in the application was <code>SlicerApp-real.exe</code>, it has been changed in <a href="https://github.com/Slicer/Slicer/commit/7aa9c0f5ddfe0b7293cd93b12c4ea2f7eb5a6874" class="inline-onebox">ENH: Set sys.executable in python to 'PythonSlicer' · Slicer/Slicer@7aa9c0f · GitHub</a> to ensure a functioning python interpreter was associated.</p>
<p>For sake of consistency, this should be updated to be:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th><code>sys.executable</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Slicer</td>
<td><code>/path/to/PythonSlicer.exe</code></td>
</tr>
<tr>
<td>PythonSlicer</td>
<td><code>/path/to/PythonSlicer.exe</code></td>
</tr>
</tbody>
</table>
</div>

---

## Post #4 by @keri (2022-07-11 19:59 UTC)

<p>It is possible to set <code>PYTHONSTARTUP</code> env var and run python script every time interpreter started.<br>
But this is not applicable when running code in the way: <code>python -c "import sys; print(sys.executable)"</code>.<br>
in this case we will see <code>python-real.exe</code> anyway</p>

---

## Post #5 by @jcfr (2022-07-11 20:10 UTC)

<p>When using <code>PythonSlicer</code>, setting <code>PYTHONSTARTUP</code> works as expected.</p>
<p>When using <code>Slicer</code>, there are no support for <code>PYTHONSTARTUP</code> environment variable because Slicer application embeds the python library and the logic handling <code>PYTHONSTARTUP</code> (specific to the python interpreter) is not considered.</p>
<p>In the case of the Slicer application, you should instead considering using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">Application Startup File</a></p>
<p>To provide a more targeted answer, could you provide more details ? What are you trying to achieve ?</p>

---

## Post #6 by @jcfr (2022-07-11 20:56 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/use-julia-with-slicer/16765/6">Use Julia with Slicer</a></p>

---
