---
topic_id: 19304
title: "About D Pointer Structure Of Slicer Application"
date: 2021-08-23
url: https://discourse.slicer.org/t/19304
---

# About d pointer structure of slicer application

**Topic ID**: 19304
**Date**: 2021-08-23
**URL**: https://discourse.slicer.org/t/about-d-pointer-structure-of-slicer-application/19304

---

## Post #1 by @xianger-qi (2021-08-23 07:05 UTC)

<p>there are a question about d pointer structure of slicer application that is why using a number of d pointer, q pointer to wrap classes. Even if those classes locate in the same project. In my view, the purpose of d pointer is convenient software update by replacing dynamic libraries without recompiling the whole source files. But Using d pointer, q pointer structure in the internal project confuses me. Thanks for reading!</p>

---

## Post #2 by @lassoan (2021-08-23 13:34 UTC)

<p>We welcome any suggestions to improve the documentation of this. If you still have any doubts about why and how the mechanism works then let us know.</p>

---

## Post #3 by @xianger-qi (2021-08-24 01:21 UTC)

<p>Thansk for replaying!! I just want to know what is the purpose for d pointer (Q_D)and q(Q_Q) pointer in slicer application.</p>

---

## Post #4 by @lassoan (2021-08-24 01:56 UTC)

<p>You can learn more about the private implementation (PIMPL) idiom here: <a href="https://stackoverflow.com/questions/25250171/how-to-use-the-qts-pimpl-idiom" class="inline-onebox">c++ - How to use the Qt's PIMPL idiom? - Stack Overflow</a></p>

---
