---
topic_id: 23065
title: "Utilise Slicer Gui When Effect Module Is Running"
date: 2022-04-21
url: https://discourse.slicer.org/t/23065
---

# Utilise Slicer GUI when effect/module is running

**Topic ID**: 23065
**Date**: 2022-04-21
**URL**: https://discourse.slicer.org/t/utilise-slicer-gui-when-effect-module-is-running/23065

---

## Post #1 by @Karthik (2022-04-21 04:26 UTC)

<p>Hi.<br>
I have written a segment editor effect. This effect usually takes about 8 minutes to run. However, during this time, Slicer is frozen and hence I cannot use it for anything else. Is it possible to still utilise slicer to view dicom data or work in other modules outside segment editor whilst my effect is running?</p>
<p>How can I utilise slicer when a module/effect is running in order to save time.</p>

---

## Post #2 by @cpinter (2022-04-21 13:48 UTC)

<p>If the Segment Editor effect is in C++ you could try to make it multi-threaded so that it runs on a worker thread, allowing the main Slicer thread to run.</p>
<p>In Python, real multithreading is more complicated, but you could try this extension: <a href="https://github.com/pieper/SlicerParallelProcessing" class="inline-onebox">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate on data in parallel</a></p>

---
