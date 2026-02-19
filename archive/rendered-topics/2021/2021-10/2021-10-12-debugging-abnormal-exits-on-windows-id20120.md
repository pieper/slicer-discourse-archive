---
topic_id: 20120
title: "Debugging Abnormal Exits On Windows"
date: 2021-10-12
url: https://discourse.slicer.org/t/20120
---

# Debugging abnormal exits on Windows

**Topic ID**: 20120
**Date**: 2021-10-12
**URL**: https://discourse.slicer.org/t/debugging-abnormal-exits-on-windows/20120

---

## Post #1 by @adamaji (2021-10-12 15:59 UTC)

<p>Hi folks,</p>
<p>I’m wondering if anyone has experience debugging abnormal exits/crashes on Windows, and what the best practices are for debugging these – errors like</p>
<p><code>error: [.../SlicerApp-real.exe] exit abnormally - Report the problem.</code></p>
<p>I’m familiar with the resources at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/index.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/debugging/index.html</a> and attaching to processes for line by line debugging, but it seems difficult to use this method to debug my issue. I have an Azure Pipeline where an installed instance of Slicer is called with some custom scripted (Python) modules running through some unit/integration tests, which throws the abnormal exit issue seemingly at random – a certain job may fail once, but rerunning that job can get it to pass.</p>
<p>For this, I think what I want is to dump the stack trace from Slicer automatically whenever a crash has occurred, but I’m not sure how to do this on Windows.</p>

---

## Post #2 by @lassoan (2021-10-12 21:09 UTC)

<p>Probably you can set up automatic stack trace of a crashing application - see for example tips <a href="https://stackoverflow.com/questions/24208767/get-stack-trace-of-a-crash-on-windows-without-installing-visual-studio-c">here</a>.</p>
<p>I’m not sure how detailed the stack trace is without debug symbols. Probably for many functions you only see the address and not the function name. A RelWithDebInfo (Release-mode build with debug information) build could give you more information, but debug symbols (all the .pdb files) for a Slicer build are quite large, about 9GB, so it would not be very easy to distribute those.</p>

---
