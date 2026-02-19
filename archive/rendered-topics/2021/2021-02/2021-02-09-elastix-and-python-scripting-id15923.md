---
topic_id: 15923
title: "Elastix And Python Scripting"
date: 2021-02-09
url: https://discourse.slicer.org/t/15923
---

# Elastix AND Python Scripting

**Topic ID**: 15923
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/elastix-and-python-scripting/15923

---

## Post #1 by @HodaGH (2021-02-09 21:06 UTC)

<p>Hi all,</p>
<p>I want to perform groupwise registration as described here <a href="https://simpleelastix.readthedocs.io/GroupwiseRegistration.html" class="inline-onebox" rel="noopener nofollow ugc">Groupwise Registration — SimpleElastix 0.1 documentation</a> with python scripting. Should I build Elastix from scratch or is there a way to do it with 3D slicer ?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2021-02-09 21:17 UTC)

<p>You can get Elastix by installing SlicerElastix extension or downloading Elastix binaries from their website or pip install SimpleElastix (<code>pip_install('SimpleElastix')</code>). You can use all these from Python in Slicer.</p>

---

## Post #3 by @mikebind (2021-04-05 16:32 UTC)

<p>On the current stable (4.11.20210226), <code>pip_install('SimpleElastix')</code> gives the following error for me:</p>
<pre><code>ERROR: Could not find a version that satisfies the requirement SimpleElastix
ERROR: No matching distribution found for SimpleElastix
</code></pre>
<p>Should this work?</p>

---

## Post #4 by @lassoan (2021-04-26 22:23 UTC)

<p>It looks like the SimpleElastix package is only for Python2. It relies on SimpleITK for current Python versions: <a href="https://pypi.org/project/SimpleITK-SimpleElastix/" class="inline-onebox">SimpleITK-SimpleElastix · PyPI</a></p>

---
