---
topic_id: 26669
title: "Error When Pip Installing In Slicers Python Console"
date: 2022-12-09
url: https://discourse.slicer.org/t/26669
---

# Error when pip installing in Slicer's python console

**Topic ID**: 26669
**Date**: 2022-12-09
**URL**: https://discourse.slicer.org/t/error-when-pip-installing-in-slicers-python-console/26669

---

## Post #1 by @drouin-simon (2022-12-09 21:22 UTC)

<p>Hi everyone,</p>
<p>I’m trying to pip install packages from the Python console in Slicer using the following commands:</p>
<pre><code class="lang-auto">import pip
pip.main(['install','pandas'])
</code></pre>
<p>This works perfectly well on macOS, but on Windows I get the following error (on both 10 and 11, on different machines and with different versions of Slicer: 4.11, 4.13 and 5.2.1):</p>
<pre><code class="lang-auto">WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
--- Logging error ---
...
</code></pre>
<p>Does anyone else have the same problem?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @jamesobutler (2022-12-09 21:56 UTC)

<p><code>pip.main()</code> is indeed old and deprecated within <code>pip</code>.</p>
<p>To install python packages using the python console in Slicer you should use <code>pip_install</code>. See the following resources below for examples and more details.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.pip_install" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.pip_install</a></p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#install-a-python-package</a></p>

---

## Post #3 by @drouin-simon (2022-12-12 21:46 UTC)

<p>Thanks a lot James, It solved my problem!</p>

---
