---
topic_id: 25963
title: "Incorporate Cgal In 3D Slicer"
date: 2022-10-29
url: https://discourse.slicer.org/t/25963
---

# Incorporate CGAL in 3D Slicer

**Topic ID**: 25963
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/incorporate-cgal-in-3d-slicer/25963

---

## Post #1 by @ZSoltani (2022-10-29 13:08 UTC)

<p>Hi,<br>
I need to incorporate CGAL in 3D Slicer for generating mesh. Any advise please?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2022-10-29 13:54 UTC)

<p>CGAL free license is GPL (except some basic framework classes, which use permissive LGPL license). GPL is a non-permissive license: it restricts you how you use and distribute whatever you build with it. Even worse, it is a so-called “viral” license, which means that the restrictions do not apply only to the library itself but anything that it is linked to (it restricts even what you can do with the software that you develop yourself).</p>
<p>We put a lot of effort into making Slicer truly open, free, and restriction-free software, in every sense. Therefore, we avoid relying on libraries with such restrictive license as GPL.</p>
<p>VTK library covers much of the features that CGAL offers, and you should be able to find alternative restriction-free libraries for what is missing. If you are desperate to use CGAL and willing to accept some legal risks, you may build executable files from CGAL algorithms and execute those from Slicer, as this might not count as “linking” to CGAL. However, even if you are willing to accept the legal risks right now, your collaborators, or the company that you want to work with, or your future investors may not be that tolerant.</p>

---

## Post #3 by @ZSoltani (2022-10-30 15:26 UTC)

<p>Thank you Andras for your comprehensive answer. That makes complete sense.</p>

---

## Post #4 by @lassoan (2022-11-03 13:02 UTC)

<p>3 posts were split to a new topic: <a href="/t/volumetric-mesh-generation-for-finite-element-analysis-of-spine/26052">Volumetric mesh generation for finite element analysis of spine</a></p>

---
