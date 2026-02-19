---
topic_id: 7733
title: "Get Slicer Version Within Python Interactor"
date: 2019-07-23
url: https://discourse.slicer.org/t/7733
---

# Get slicer version within Python Interactor

**Topic ID**: 7733
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/get-slicer-version-within-python-interactor/7733

---

## Post #1 by @tbillah (2019-07-23 20:29 UTC)

<p>Is there a way to get my slicer version within the Python Interactor?</p>
<p>For example:</p>
<pre><code class="lang-auto">import sys
print(sys.version)
</code></pre>
<p>gives us Python version. I was wondering if there is a way to get slicer version from the Python console as well.</p>

---

## Post #2 by @jamesobutler (2019-07-23 20:44 UTC)

<p>You’re looking for things like <code>slicer.app.majorVersion</code>, <code>slicer.app.minorVersion</code> and <code>slicer.app.repositoryRevision</code>.</p>

---
