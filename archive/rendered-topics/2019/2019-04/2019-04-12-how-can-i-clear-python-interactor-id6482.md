---
topic_id: 6482
title: "How Can I Clear Python Interactor"
date: 2019-04-12
url: https://discourse.slicer.org/t/6482
---

# How can I clear Python Interactor?

**Topic ID**: 6482
**Date**: 2019-04-12
**URL**: https://discourse.slicer.org/t/how-can-i-clear-python-interactor/6482

---

## Post #1 by @Hadi-Fooladi (2019-04-12 15:18 UTC)

<p>Hi,</p>
<p>I’m using 3D-Slicer v4.10.1 and I’m wondering how can I clear <strong>Python Interactor</strong>?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-04-12 15:31 UTC)

<p>For me it works to use the right-click context menu and select all then delete.</p>

---

## Post #3 by @Hadi-Fooladi (2019-04-12 15:55 UTC)

<p>Thanks Steve. It worked.</p>

---

## Post #4 by @aiden.zhu (2024-03-29 13:21 UTC)

<p>is there a python function to do the “clearing” here?<br>
Thanks</p>
<p>just found solution from <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>You could use the function <code>ctkPythonConsole::clear()</code></p>
<p>From python, the following can be done:</p>
<pre><code class="lang-auto">slicer.app.pythonConsole().clear()
</code></pre>
<p>From a C++ loadable module, you would have to do something like this:</p>
<pre><code class="lang-auto">#include "qSlicerApplication.h"

// CTK includes
#include &lt;ctkPythonConsole.h&gt;

[...]

qSlicerApplication* app = qSlicerApplication::application();
app-&gt;pythonConsole()-&gt;clear();
</code></pre>

---

## Post #5 by @pieper (2024-03-29 13:24 UTC)

<p>You could use:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.pythonShell().reset()
</code></pre>

---

## Post #6 by @aiden.zhu (2024-03-29 13:25 UTC)

<p>Thanks a lot for the quick response. That works well.</p>

---
