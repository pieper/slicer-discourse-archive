---
topic_id: 12002
title: "Is It Possible To Create A Model Node With 2 Cylinders"
date: 2020-06-12
url: https://discourse.slicer.org/t/12002
---

# Is it possible to create a Model Node with 2 cylinders?

**Topic ID**: 12002
**Date**: 2020-06-12
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-a-model-node-with-2-cylinders/12002

---

## Post #1 by @Pablo_Javier (2020-06-12 16:26 UTC)

<p>I want to create a model node which includes two or more cylinders. Is that possible ?( I don´t want a node per cylinder)</p>

---

## Post #2 by @lassoan (2020-06-12 16:29 UTC)

<p>Would you like to create a cylinder with a cylindrical hole in it? You can create that by appending output of vtkClyinderSources, with the internal polydata turned inside out using vtkReverseSense.</p>

---

## Post #3 by @Pablo_Javier (2020-06-12 16:46 UTC)

<p>I want to create 2 or more independent cylinders into a single Model node.</p>

---

## Post #4 by @lassoan (2020-06-12 17:20 UTC)

<p>OK, then just append the output of the cylinder sources by using vtkAppendPolyData and set its output as input of the model node.</p>

---

## Post #5 by @Pablo_Javier (2020-06-12 23:09 UTC)

<p>Thank you so much! It worked!</p>

---
