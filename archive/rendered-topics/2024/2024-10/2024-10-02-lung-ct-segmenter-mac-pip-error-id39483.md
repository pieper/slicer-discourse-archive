---
topic_id: 39483
title: "Lung Ct Segmenter Mac Pip Error"
date: 2024-10-02
url: https://discourse.slicer.org/t/39483
---

# Lung CT Segmenter Mac pip error

**Topic ID**: 39483
**Date**: 2024-10-02
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter-mac-pip-error/39483

---

## Post #1 by @alexjin (2024-10-02 03:24 UTC)

<p>Hi, when I use the Lung CT Segmenter extension, I get the following error:</p>
<pre><code class="lang-auto">Failed to compute results: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'https://github.com/JoHof/lungmask/archive/master.zip']' returned non-zero exit status 1.
</code></pre>
<p>I tried with both ARM and Intel Macs and both got the same error, but it worked when I tried on PC.</p>

---

## Post #2 by @alexjin (2024-10-11 12:16 UTC)

<p>Fixed by pip install 2.0.6 version of fill-void instead of the newest release</p>

---

## Post #3 by @lassoan (2024-10-11 13:39 UTC)

<p>Thanks for the update! Please report this (with some more details) at the issue tracker of the model’s repository: <a href="https://github.com/JoHof/lungmask" class="inline-onebox">GitHub - JoHof/lungmask: Automated lung segmentation in CT</a></p>

---
