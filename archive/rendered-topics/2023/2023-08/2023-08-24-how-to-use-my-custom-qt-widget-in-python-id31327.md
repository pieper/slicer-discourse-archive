---
topic_id: 31327
title: "How To Use My Custom Qt Widget In Python"
date: 2023-08-24
url: https://discourse.slicer.org/t/31327
---

# How to use my custom qt-widget in python?

**Topic ID**: 31327
**Date**: 2023-08-24
**URL**: https://discourse.slicer.org/t/how-to-use-my-custom-qt-widget-in-python/31327

---

## Post #1 by @shanfl (2023-08-24 06:57 UTC)

<p>I create a Qt widget named ‘MyWidget’ in Modules-Markups-Widgets project.but in python script ,<br>
it occour error,say: slicer.MyWidget is not found ,but slicer.qSlicerSimpleMarkupsWidget can use.<br>
my ‘MyWidget’ and   qSlicerSimpleMarkupsWidget are in same project . I dont know why?</p>

---

## Post #2 by @jcfr (2023-08-24 13:30 UTC)

<blockquote>
<p>I create a Qt widget named ‘MyWidget’</p>
</blockquote>
<p>Are you asking how to reuse a Qt widget written in C++ from Python ?</p>

---

## Post #3 by @cpinter (2023-08-24 13:33 UTC)

<p>This is fully possible, and I have done it many times. The question is what step you are missing, which we cannot tell from this much information. Please describe your approach in as much detail as possible. How did you add the widget and in what project? What files does it include? Did you add all of them to CMakeLists? Did you build the code? How do you start Slicer? Things like this… Thanks.</p>

---
