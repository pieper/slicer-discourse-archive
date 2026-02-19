---
topic_id: 27733
title: "How Do I Import External Modules To 3D Slicer"
date: 2023-02-10
url: https://discourse.slicer.org/t/27733
---

# How do I import external modules to 3d slicer?

**Topic ID**: 27733
**Date**: 2023-02-10
**URL**: https://discourse.slicer.org/t/how-do-i-import-external-modules-to-3d-slicer/27733

---

## Post #1 by @dsa934 (2023-02-10 00:38 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>When creating extension code, import external libraries (e.g paramiko, etc) as follows.</p>
<pre><code class="lang-auto"># some extension codes

import paramiko
import ....

</code></pre>
<p>In a general IDE, a virtual environment is built using Anaconda and then packages are installed (in python). or using c-make (in c++) How can I add the above packages to 3D Slicer?</p>

---

## Post #2 by @pieper (2023-02-10 15:09 UTC)

<p>You should be able to do <code>pip_install("paramiko")</code> in the Slicer python console and the import.</p>

---
