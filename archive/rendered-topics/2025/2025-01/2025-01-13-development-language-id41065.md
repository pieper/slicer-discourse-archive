---
topic_id: 41065
title: "Development Language"
date: 2025-01-13
url: https://discourse.slicer.org/t/41065
---

# Development Language

**Topic ID**: 41065
**Date**: 2025-01-13
**URL**: https://discourse.slicer.org/t/development-language/41065

---

## Post #1 by @Reza_Mohammadi (2025-01-13 23:31 UTC)

<p>Dear Sir/Madam,<br>
As far as I understood, 3D Slicer is using C++ and Qt for development. As there are several experience, I just want to know, what are the best language for developing a medical device? For instance, in the field of radiotherapy treatment planning system.</p>

---

## Post #2 by @pieper (2025-01-13 23:41 UTC)

<p>There are lots of considerations of course, but my general approach is to do as much as possible in a high level language like python to really nail down the functionality you need, and then if there are performance critical sections of the code, consider how to make high performance replacements, which could be in C++, but might also be in a GPU shader language or something else like CUDA or OpenCL.</p>

---
