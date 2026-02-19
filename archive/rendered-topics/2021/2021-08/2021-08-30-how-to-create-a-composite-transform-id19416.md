---
topic_id: 19416
title: "How To Create A Composite Transform"
date: 2021-08-30
url: https://discourse.slicer.org/t/19416
---

# How to create a composite transform

**Topic ID**: 19416
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/how-to-create-a-composite-transform/19416

---

## Post #1 by @atracsys-sbt (2021-08-30 20:10 UTC)

<p>Hi,<br>
In my scripted module, up until now I have been using transform concatenation by applying a parent transform to another and then to a model. However, I would like to merge both transforms in a more permanent way and after some research, I saw that Slicer supports composite transforms, but I couldn’t find an example of this, even through the UI.<br>
Thanks for any help !</p>

---

## Post #2 by @lassoan (2021-08-30 23:53 UTC)

<p>You can create composite transform by hardening a transform on another.</p>

---

## Post #3 by @atracsys-sbt (2021-08-31 08:20 UTC)

<p>Indeed, but apparently this does not work for a transform that changes constantly like one streamed from openIGTlink for example. If the streamed transform is the parent, it hardens the child transform given the values at the exact moment of the hardening. If it’s reverse, the hardening does not hold since the child transform is constantly updated.</p>

---

## Post #4 by @lassoan (2021-08-31 13:29 UTC)

<p>Yes, this is how it works. Hardening would not make sense for constantly changing transforms. You probably want to combine transforms (compute an output transform by combining input transforms) using “Combine transforms” module in SlicerIGT extension.</p>

---

## Post #5 by @atracsys-sbt (2021-08-31 13:46 UTC)

<p>All right, thanks for clarifying !</p>

---
