---
topic_id: 12348
title: "Publish An Extension Without Building Slicer"
date: 2020-07-02
url: https://discourse.slicer.org/t/12348
---

# Publish an extension without building Slicer

**Topic ID**: 12348
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/publish-an-extension-without-building-slicer/12348

---

## Post #1 by @TiphaineJh (2020-07-02 19:29 UTC)

<p>Hello,<br>
I am currently developping a python module in slicer 4.11.0 and would like to publish it to the Extensions Catalog of Slicer.<br>
I would like to know if I have to build slicer in order to publish it, and if there is an up to date documentation about it because every doc I found seemed to say that I should build slicer when I don’t think it is necessary if I used python.</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2020-07-02 19:40 UTC)

<p>If you use Python then you don’t have to build Slicer. There are just a few inconveniences:</p>
<ul>
<li>You need to create the .s4ext file manually. It is a simple text files and there are <a href="https://github.com/Slicer/ExtensionsIndex">lots of examples</a>, so it should not be a problem.</li>
<li>You cannot test extension packaging. You need to double-check that you added all extra files that you want to distribute with your extension to the CMakeLists.txt.</li>
</ul>

---
