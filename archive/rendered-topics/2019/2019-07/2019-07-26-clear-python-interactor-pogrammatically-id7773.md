# Clear Python Interactor pogrammatically

**Topic ID**: 7773
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/clear-python-interactor-pogrammatically/7773

---

## Post #1 by @Manuel (2019-07-26 15:50 UTC)

<p>Is there any posibility to clear the Python Interactor pogrammatically within a loable module?</p>
<p>Thanks in advanced.<br>
Manuel</p>

---

## Post #2 by @jamesobutler (2019-07-26 16:21 UTC)

<p>Just curious, can you provide more information about why you want to clear the python interactor? There might be a better solution to the problem that you are trying to solve.</p>

---

## Post #3 by @Manuel (2019-07-26 16:29 UTC)

<p>In my module, I have some logging infos during the process and at the start of the algorithm within the module, I want to clear the Python Interactor (the resulting logging infos) from the run before.</p>

---

## Post #4 by @jcfr (2019-07-26 19:03 UTC)

<p>You could use the function <code>ctkPythonConsole::clear()</code></p>
<p>From python, the following can be done:</p>
<pre><code class="lang-python">slicer.app.pythonConsole().clear()
</code></pre>
<p>From a C++ loadable module, you would have to do something like this:</p>
<pre><code class="lang-cpp">#include "qSlicerApplication.h"

// CTK includes
#include &lt;ctkPythonConsole.h&gt;

[...]

qSlicerApplication* app = qSlicerApplication::application();
app-&gt;pythonConsole()-&gt;clear();
</code></pre>

---

## Post #5 by @Manuel (2019-07-26 19:27 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="7773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>slicer.app.pythonConsole().clear()</p>
</blockquote>
</aside>
<p>Yes! Thats exactly what I need. Thank you so much Jean!</p>

---
