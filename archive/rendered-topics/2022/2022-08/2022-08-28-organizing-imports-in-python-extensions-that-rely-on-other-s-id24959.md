---
topic_id: 24959
title: "Organizing Imports In Python Extensions That Rely On Other S"
date: 2022-08-28
url: https://discourse.slicer.org/t/24959
---

# Organizing imports in python extensions that rely on other slicer extensions

**Topic ID**: 24959
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/organizing-imports-in-python-extensions-that-rely-on-other-slicer-extensions/24959

---

## Post #1 by @pll_llq (2022-08-28 07:47 UTC)

<p>I have a file in my scripted python extension that interacts with another extension (SlicerIGT Watchdog specifically). I want to import <code>vtkMRMLWatchdogNode</code> in my python code to use it for type hints. When I add it to the import statements like</p>
<pre><code class="lang-python">from slicer import vtkMRMLLinearTransformNode, vtkMRMLWatchdogNode
</code></pre>
<p>the application launches and my module is loaded before SlicerIGT, thus before <code>vtkMRMLWatchdogNode</code> is available in the slicer namespace. This leads to an import error and a failure to load my python extension.</p>
<p>Is there a way to specify a dependency for a slicer python extension or any other way to get around the extension loading order which if I understand correctly is random?</p>

---

## Post #2 by @lassoan (2022-08-28 10:59 UTC)

<p>MRML nodes are imported into the Slicer namespace automatically, you should not attempt to import them manually, as it is either unnecessary or premature.</p>
<p>You must not import any Python modules (other than built-in ones) in the body of the .py file, because order of module discovery is random. The application determines dependencies during module discovery and module loading is ordered based on dependencies that each module declares about itself.</p>
<p>Thr simplest is to observe the startup completed signal and perform actions that you want to do at startup but rely on existence of other modules in the callback function.</p>

---

## Post #3 by @pll_llq (2022-08-28 12:13 UTC)

<p>Thanks. You are right, that import is unnecessary to have working code.</p>
<p>In my case the sole purpose of having that import is to enable certain functionality of my text editor (VSCode) that makes the development process faster and more pleasant in general. When I link the VSCode workspace to the <code>PythonSlicer</code> executable using the <code>python.defaultInterpreterPath</code> setting I get python related tooling (language server and linters) running from slicer.</p>
<p>The workaround is not worth the time in this case.</p>
<p>On the other note, can you please explain a bit what you mean by “must not import any Python modules (other than built-in ones) in the body of the .py file”. Are you referring to slicer python modules (like importing a logic class of another slicer extension) or generic python modules (numpy, torch, etc.)?</p>

---

## Post #4 by @lassoan (2022-08-28 12:36 UTC)

<p>You should not import numpy, torch, etc. either in the .py file body.</p>
<p>Pip-installed modules cannot be added there because the first time the module is discovered, the module is not available yet, so you cannot import it. If you added pip_install in the .py file body then it would cause long delays at application startup (in case of torch, it could be several minutes - so users would assume the application is crashed).</p>
<p>Importing Python modules that are bundled with Slicer, such as numpy, used to be acceptable, but in Python-3.9 and Windows11 we ran into issues (<a href="https://github.com/Slicer/Slicer/issues/5945">Slicer hung during startup</a> due to incorrect stdin/stdout usage in OpenBLAS), so now we don’t recommend importing anything.</p>
<aside class="quote no-group" data-username="pll_llq" data-post="3" data-topic="24959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p>In my case the sole purpose of having that import is to enable certain functionality of my text editor (VSCode) that makes the development process faster and more pleasant in general. When I link the VSCode workspace to the <code>PythonSlicer</code> executable using the <code>python.defaultInterpreterPath</code> setting I get python related tooling (language server and linters) running from slicer.</p>
</blockquote>
</aside>
<p>Time to time I test if I can get anything useful from this, but so far auto-completion, method documentation, syntax highlighting, linting, etc. have all mostly failed for Slicer scripted modules. Could you describe what IDE features work you?</p>

---

## Post #5 by @pll_llq (2022-08-28 12:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you describe what IDE features work you?</p>
</blockquote>
</aside>
<p>I can’t get docstrings for bundled slicer python modules if i’m not using a jupyter kernel.</p>
<p>I run some linting on save. If I link to <code>PythonSlicer</code> the linters don’t yell at me with false-positives like <code>qt</code> or <code>slicer</code> namespaces, thus checking only the code available in the workspace.</p>
<p>I have tried mypy, pylint, flake8 and pycodestyle and all of them worked to the extent of testing my code and not raising false-flags about the things that are expected from the slicer runtime.</p>

---

## Post #6 by @pll_llq (2022-08-28 12:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24959">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Importing Python modules that are bundled with Slicer, such as numpy, used to be acceptable, but in Python-3.9 and Windows11 we ran into issues (<a href="https://github.com/Slicer/Slicer/issues/5945" rel="noopener nofollow ugc">Slicer hung during startup</a> due to incorrect stdin/stdout usage in OpenBLAS), so now we don’t recommend importing anything.</p>
</blockquote>
</aside>
<p>This is very important information. Thanks a lot</p>

---
