---
topic_id: 32950
title: "Scripted Cli Python Module"
date: 2023-11-22
url: https://discourse.slicer.org/t/32950
---

# Scripted/cli Python module

**Topic ID**: 32950
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/scripted-cli-python-module/32950

---

## Post #1 by @PaoloZaffino (2023-11-22 11:38 UTC)

<p>Hi all,<br>
I was wondering if it is possible to write a scripted Python module that can be used both via GUI and command line.</p>
<p>Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @pieper (2023-11-22 17:31 UTC)

<p>Hi Paolo -</p>
<p>Sure, you should be able to add a cli wrapper that uses the same logic classes as a a module’s GUI uses.  If it’s just python code it could use any python or if you have dependencies you could either use PythonSlicer or <code>Slicer --no-splash --no-main-window</code> to run it.</p>

---

## Post #3 by @PaoloZaffino (2023-11-22 20:38 UTC)

<p>Thanks a lot <a class="mention" href="/u/pieper">@pieper</a>!<br>
I got it.</p>
<p>Paolo</p>

---
