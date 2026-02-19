---
topic_id: 20454
title: "Multiple Sessions Of Slicer Are Launched In A Loop"
date: 2021-11-02
url: https://discourse.slicer.org/t/20454
---

# Multiple sessions of Slicer are launched in a loop

**Topic ID**: 20454
**Date**: 2021-11-02
**URL**: https://discourse.slicer.org/t/multiple-sessions-of-slicer-are-launched-in-a-loop/20454

---

## Post #1 by @lb123 (2021-11-02 11:20 UTC)

<p>Hi,</p>
<p>I built Slicer 4.13.0 in Ubuntu 20.04.3 LTS. It worked properly and I was able to use Slicer.</p>
<p>Then I built SlicerIGT following these steps:</p>
<pre><code class="lang-auto">$ git clone https://github.com/SlicerIGT/SlicerIGT.git
$ mkdir SlicerIGT-debug
$ cd SlicerIGT-debug
$ cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DSlicer_DIR:PATH=~/Slicer/Slicer-SuperBuild-Debug/Slicer-build ../SlicerIGT
$ make
</code></pre>
<p>When the process completed, I runned Slicer, and multiple sessions of Slicer had been launched in a loop. It happens every time I run Slicer now.</p>
<p>Do you know why it happens? Do you know how to solve it?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-11-02 12:39 UTC)

<p>It seems you store a shell script that starts Slicer in a folder listed among the “Additional module paths”. It leads to an infinite loop of Slicer launches because when Slicer starts, it attempts to run each executable (including shell scripts) that are in “Additional module paths” folders to get basic module information, and if any of those scripts launch Slicer then you start a new loop.</p>
<p>The solution is to only keep Slicer modules (.so, .py, .sh, …) in your module folders and move your helper scripts to a parent folder or subfolder.</p>

---
