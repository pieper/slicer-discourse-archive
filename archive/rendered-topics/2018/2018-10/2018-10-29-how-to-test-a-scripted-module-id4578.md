---
topic_id: 4578
title: "How To Test A Scripted Module"
date: 2018-10-29
url: https://discourse.slicer.org/t/4578
---

# How to test a scripted module

**Topic ID**: 4578
**Date**: 2018-10-29
**URL**: https://discourse.slicer.org/t/how-to-test-a-scripted-module/4578

---

## Post #1 by @kayarre (2018-10-29 20:57 UTC)

<p>I modified the SlicerCaseIterator module, but I don’t actually know how to test/debug it.</p>
<p>the command i  use is <code>~/tools/Slicer-4.10.0-linux-amd64/Slicer --additional-module-paths ~/build/slicer/SlicerCaseIterator/SlicerCaseIterator</code></p>
<p>but it fails to load which means there is an error, but I am not sure how get the errors to show up.<br>
is there a better way beyond adding the <code>--launcher-verbose</code> option?</p>

---

## Post #2 by @pieper (2018-11-26 18:58 UTC)

<p>Any script errors on startup show up in the terminal and in the python console.  Also if you start with a working module (like unmodified SlicerCaseIterator) and you enable developer mode (in the preferences dialog) then you can incrementally reload and debug the script.</p>

---
