---
topic_id: 19042
title: "Command Line Interface Cli Much Slower Compared To Starting"
date: 2021-08-03
url: https://discourse.slicer.org/t/19042
---

# Command Line Interface (CLI) much slower compared to starting in separate python environment

**Topic ID**: 19042
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/command-line-interface-cli-much-slower-compared-to-starting-in-separate-python-environment/19042

---

## Post #1 by @mcfly3001 (2021-08-03 15:17 UTC)

<p>Hi,<br>
I created a small script which generates a transform matrix and publishes the matrix via OpenIGTLink (pyigtlink). This script I want to start together with a Slicer Guidelet application. The application will connect to the OpenIGTLink and receive the transform.<br>
To be able to automatically start the script, I found the CLI solution and adjusted the code accordingly. Now I observed, that the update of the transform is much slower when I start the CLI module compared to manually starting the script with a dedicated python.exe call.<br>
I observe this by going to the “Transforms” UI and manually modifying any of the values of the received transform. When using the CLI version, the matrix keeps the modfied value for a couple of seconds until it changes to the matrix send from the script. When calling the script with python.exe, the transform immediately jumps back to the matrix that was send from the script.</p>
<p>Anyone has an idea why this is the case? Would maybe <a href="https://github.com/pieper/SlicerProcesses" rel="noopener nofollow ugc">SlicerProcesses</a> solve the performance issue? Manually starting the script via python.exe I want to avoid because this would also require to have an extra Python environment installed instead of directly using the python-slicer.exe. Maybe is this already part of the problem, that “python-slicer.exe” is somehow slowing down?<br>
Currently I am working with 4.11.20210226 r29738</p>

---

## Post #2 by @lassoan (2021-08-03 16:15 UTC)

<p>You can use PythonSlicer.exe to run the pyigtlink server, and it should not be slower than any other Python environment. Just make sure you don’t have any outputs or not redirect the output into Slicer’s log, as logging many messages may cause significant slowdown.</p>
<p>If you want to simulate transform changes in Slicer then you don’t need to go through OpenIGTLink, you can simply set up a QTimer and update transform nodes in the callback function.</p>

---

## Post #3 by @jamesobutler (2021-08-03 16:51 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="19042">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>when I start the CLI module compared to manually starting the script with a dedicated python.exe call</p>
</blockquote>
</aside>
<p>I believe this is the important piece of information. A python scripted CLI slicer module can take a second or two to start the <code>run</code> action. This makes it not as instantaneous as calling to a python.exe manually to run a script.</p>
<p>Are there suggestions on how to improve startup performance when calling a Slicer CLI module to run? I’m assuming it is doing extra things such as trying to setup argument types, other potential launcher arguments which makes it not begin execution of the target python code immediately.</p>

---

## Post #4 by @mcfly3001 (2021-08-03 17:06 UTC)

<p>I tried to use <code>slicer.util.launchConsoleProcess</code> with PythonSlicer.exe and as alternative tried to run PythonSlicer.exe directly from command line. It results in the same behaviour. The transform is updated only after ~0.5-2.0 seconds.<br>
Running the script with an installed Python environment is much faster. I just figured out that my virtual-env I was using was based on Python 3.7. I just installed Python 3.6 and retried. It is still much faster when using the python.exe of the Python 3.6 install.</p>
<blockquote>
<p>I believe this is the important piece of information. A python scripted CLI slicer module can take a second or two to start the <code>run</code> action</p>
</blockquote>
<p>That it takes a bit longer during startup would be fine, though the transform matrix is continously slower updated when using PythonSlicer.exe.</p>
<blockquote>
<p>If you want to simulate transform changes in Slicer then you don’t need to go through OpenIGTLink</p>
</blockquote>
<p>I don’t want to simulate. Basically the script connects to another system from where a transform is continously updated. This is done in an endless loop until the script is stopped.</p>
<p>For now I modified the code to generate random numbers to debug when the matrix is updated in the Slicer transform node. With PythonSlicer it often hangs at one number for a couple of seconds. Then it quite quickly updates the transform rapidly and then slows down again. Feels somehow like at a certain point <code>flush</code> is triggered and every change is sent out at once. With regular Python the values are constantly changing.</p>

---

## Post #5 by @lassoan (2021-08-03 18:01 UTC)

<p>Do you see a difference in update rate if you don’t continuously print out a lot of text?</p>
<p>If that does not help then the best is to use a Python profiler instead of trying to guess what takes a long time (see how we did it <a href="https://discourse.slicer.org/t/third-party-library-works-slower-inside-slicers-python-shell-why-how-to-do-performance-profiling/18742/2">here</a>).</p>

---

## Post #6 by @mcfly3001 (2021-08-03 18:14 UTC)

<p>I disabled all logging as well so this should not be the issue. Thanks for the link. I will try to do the profiling and post an update as soon as I found something.</p>

---
