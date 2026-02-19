---
topic_id: 13682
title: "Getting The Code Of Python"
date: 2020-09-24
url: https://discourse.slicer.org/t/13682
---

# getting the code of Python

**Topic ID**: 13682
**Date**: 2020-09-24
**URL**: https://discourse.slicer.org/t/getting-the-code-of-python/13682

---

## Post #1 by @aldoSanchez (2020-09-24 00:07 UTC)

<p>hello<br>
I want to know if someone knows how to see all commands that I’m executing in 3D slicer.<br>
I mean doing an action and seen the code of that accion.</p>

---

## Post #2 by @pieper (2020-09-24 12:09 UTC)

<p>There’s no direct mapping between user actions and python code.</p>
<p>You can look at some of the <a href="https://github.com/Slicer/Slicer/tree/master/Applications/SlicerApp/Testing/Python">Self Tests</a> will give you some ideas about how to control the application via python.  Other than that the process is basically to study the source code to find how any particular feature is implemented and follow the same pattern.  Sometimes this means mapping from C++ to Python, but usually that part is obvious.</p>

---

## Post #3 by @lassoan (2020-09-24 12:52 UTC)

<p>We also provide code snippets for all commonly needed tasks in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> and if you don’t find something then you can just ask here.</p>

---

## Post #4 by @aldoSanchez (2020-09-24 17:29 UTC)

<p>thanks for the information,<br>
I’m trying to work with pure python command lines, I don’t want to use the Qt<br>
the idea is to run everything from a script.</p>

---

## Post #5 by @lassoan (2020-09-24 23:29 UTC)

<p>You can use everything from a script, including using Qt classes. Rendering may require an application window (it can be hidden, but it has to exist). You can also use Slicer as Jupyter notebook kernel.</p>

---
