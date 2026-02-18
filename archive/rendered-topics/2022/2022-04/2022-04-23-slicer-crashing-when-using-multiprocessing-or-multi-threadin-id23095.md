# Slicer crashing when using multiprocessing or multi threading

**Topic ID**: 23095
**Date**: 2022-04-23
**URL**: https://discourse.slicer.org/t/slicer-crashing-when-using-multiprocessing-or-multi-threading/23095

---

## Post #1 by @vanlangk (2022-04-23 09:59 UTC)

<p>Hi guys,</p>
<p>I am currently working on a voice interface for 3D slicer. I’m implementing it using a scripted module for 3d Slicer where it creates a child process, and then continually listens for words from the child process (by checking a queue). It must then perform a change to the mrml scene using this received word (e.g., selecting the ROI tool; applying a window preset to a selected volume; changing the color lookup table of a volume).</p>
<p>My first issue is that when I start a child process using python multiprocessing, this results in the Slicer application crashing. Is python multiprocessing not supported by Slicer?</p>
<p>Furthermore, I am running into an issue when implementing listening. I have tried using a qt timer to constantly check the queue, but for some reason the behavior is unstable, and the applications crashes when I click something in the tool bar (e.g, change a module, select a different markup). I also tried creating a child thread which constantly checks the word queue, but this creates unstable and delayed behavior (I have seen forum posts saying that Slicer does not support multi threading). Lastly, I tried a solution using signals, but the signal handler has a massive delay (I’m not sure if 3D Slicer supports signals).</p>
<p>Have my approaches been wrong, or maybe there’s an error in the code I’m writing?</p>
<p>Any advice would be greatly appreciated, cheers!</p>

---

## Post #2 by @pieper (2022-04-23 14:55 UTC)

<p>Have a look at how things are done here: <a href="https://github.com/pieper/SlicerParallelProcessing" class="inline-onebox">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate on data in parallel</a></p>
<p>The <a href="https://doc.qt.io/qt-5/qprocess.html">QProcess</a> is a very nice abstraction of OS processes and provides a clean set of signals for state changes and also exposes the input, output, and error in a way that you can get signals when it’s valid to read/write, so there’s a clean integration with the event loop and no messy timers required.</p>

---

## Post #3 by @vanlangk (2022-04-25 01:03 UTC)

<p>Hi Steve,</p>
<p>Thanks a lot for your prompt response! I’ll have a look at the resources you sent through and implement my program accordingly. I’ll keep you guys posted on how things work out.</p>

---
