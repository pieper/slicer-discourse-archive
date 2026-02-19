---
topic_id: 25129
title: "How To Add An Observer To The Sequence Browser Of Module Seq"
date: 2022-09-07
url: https://discourse.slicer.org/t/25129
---

# How to add an observer to the Sequence-Browser of module Sequences?

**Topic ID**: 25129
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/how-to-add-an-observer-to-the-sequence-browser-of-module-sequences/25129

---

## Post #1 by @sunshine (2022-09-07 02:17 UTC)

<p>Hi everyone,</p>
<p>I am trying to write my first extension module, and would like to synchronize the sequence browser in module Sequences and the module I am working on.</p>
<p>How can I add an observer to the Sequence Browser of module Sequences?<br>
And how to change the selection of the sequence browser of module Sequences using codes?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @sunshine (2022-09-07 03:52 UTC)

<p>Found it. Instead of calling the sequences widget (no signal), we need to call toolBar().<br>
Signal:   <code>slicer.modules.sequences.toolBar().activeBrowserNodeChanged.connect()</code><br>
Aquire:   <code>slicer.modules.sequences.toolBar().activeBrowserNode()</code><br>
Assign:  <code>slicer.modules.sequences.widgetRepresentation().setActiveBrowserNode()</code></p>

---
