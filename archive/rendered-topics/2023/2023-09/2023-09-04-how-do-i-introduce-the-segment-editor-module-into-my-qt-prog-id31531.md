---
topic_id: 31531
title: "How Do I Introduce The Segment Editor Module Into My Qt Prog"
date: 2023-09-04
url: https://discourse.slicer.org/t/31531
---

# How Do I introduce the Segment Editor module into MY QT program?

**Topic ID**: 31531
**Date**: 2023-09-04
**URL**: https://discourse.slicer.org/t/how-do-i-introduce-the-segment-editor-module-into-my-qt-program/31531

---

## Post #1 by @iwangwangwang (2023-09-04 01:08 UTC)

<p>I’m developing a program that needs image segmentation, so I want to bring in the Segment Editor module of 3d Slicer, or transform my program into a 3D slicer module, which approach is easier to implement and how? Do you have any examples? Ask for answers in good faith.</p>

---

## Post #2 by @pieper (2023-09-04 14:06 UTC)

<p>It’s definitely easier to write a Slicer module than to write a new program.  You can look at examples like MONAI Label, where the Segment Editor is embedded.  Depending on your needs, it’s likely that you can implement everything you need in python and avoid the need to compile from source.</p>

---

## Post #3 by @iwangwangwang (2023-09-05 02:29 UTC)

<p>thanks, as mentioned in my question，image segmentation is just a small but very important part of the functionality in my program，I want to develop my program based on 3dslicer，bring the Segment Editor module of 3d Slicer into my program, or develop my program as a 3D slicer module，I don’t know which method is easier to implement，but python script may be difficult to implement complex functions in my program, include GUI、interactive、algorithm and uniform style etc…<br>
Do you have any good suggestions？<br>
sincerely for your answer.</p>

---

## Post #4 by @iwangwangwang (2023-09-05 02:30 UTC)

<p>thanks, as mentioned in my question，image segmentation is just a small but very important part of the functionality in my program，I want to develop my program based on 3dslicer，bring the Segment Editor module of 3d Slicer into my program, or develop my program as a 3D slicer module，I don’t know which method is easier to implement，but python script may be difficult to implement complex functions in my program, include GUI、interactive、algorithm and uniform style etc…<br>
Do you have any good suggestions？<br>
sincerely for your answer.</p>

---

## Post #5 by @pieper (2023-09-05 12:06 UTC)

<p>It’s great that you want to write a program with more features and maybe you will find Slicer helpful for that, but it’s not always easy to factor out parts for reuse.  It’s an ambitious undertaking to write a big program and you’ll need to study carefully to organize your efforts.  Writing a big C++ program from scratch is a lot of work, but if you don’t need it to be cross-platform and you have only very specific use cases in mind it can be accomplished.  Slicer with python provides a more efficient way solve many problems.</p>

---
