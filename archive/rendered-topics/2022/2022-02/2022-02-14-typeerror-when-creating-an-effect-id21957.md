---
topic_id: 21957
title: "Typeerror When Creating An Effect"
date: 2022-02-14
url: https://discourse.slicer.org/t/21957
---

# TypeError when creating an Effect

**Topic ID**: 21957
**Date**: 2022-02-14
**URL**: https://discourse.slicer.org/t/typeerror-when-creating-an-effect/21957

---

## Post #1 by @Karthik (2022-02-14 14:06 UTC)

<p>I created an Effect inside Segment Editor. I looked at other effects (both default effects and those in SegmentEditorExtraEffects) to create my effect. However, when I launch Slicer application, it gives the following error.</p>
<p>TypeError: <strong>init</strong>() takes 1 positional argument but 2 were given<br>
TypeError: module.<strong>init</strong>() argument 1 must be str, not qSlicerScriptedLoadableModule<br>
TypeError: <strong>init</strong>() takes 1 positional argument but 2 were given<br>
Traceback (most recent call last):<br>
File “/home/karthik/…/SegmentEditorBR.py”, line 27, in registerEditorEffect<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’</p>
<p>Although it does not affect the working of my effect (i.e., the effect is still functional), this error message is very annoying. It shows up in the Python Interactor upon launch of Slicer itself. Please suggest how to get rid of this error.</p>
<p>I created the effect through Extension Wizard. I modified the name of the effect but other than that I haven’t touched the other effect parameters.</p>

---

## Post #2 by @DaoMaoDuc (2022-03-03 07:38 UTC)

<p>I have the same issue. I try to find out the cause of that problem for days and double checked my code multiple times. As Karthik has described: Error messages without any impact on the workflow.</p>

---
