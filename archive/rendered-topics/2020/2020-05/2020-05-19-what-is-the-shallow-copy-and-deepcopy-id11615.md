---
topic_id: 11615
title: "What Is The Shallow Copy And Deepcopy"
date: 2020-05-19
url: https://discourse.slicer.org/t/11615
---

# What is the Shallow Copy and DeepCopy

**Topic ID**: 11615
**Date**: 2020-05-19
**URL**: https://discourse.slicer.org/t/what-is-the-shallow-copy-and-deepcopy/11615

---

## Post #1 by @loubna (2020-05-19 10:12 UTC)

<p>Hi to everyone;</p>
<p>SomeOne can tell me what is the difference between Shallow Copy, DeepCopy and simple affectation?</p>
<p>for exemple: what is the difference between:</p>
<p>1- vtkImagedata* image = filter-&gt;GetOutput();<br>
2- image -&gt;ShallowCopy (filrer-&gt;GetOutput());<br>
3- image-&gt; DeepCopy(filter-&gt;GetOutput());</p>
<p>Thank’s in advance</p>

---

## Post #2 by @James_Hoctor (2020-05-19 14:19 UTC)

<p><a href="https://en.wikipedia.org/wiki/Object_copying" rel="nofollow noopener">This wiki page</a> describes deep versus shallow copy in general, but you likely want to know about the specific differences in vtkImageData. In particular, <a href="https://vtk.org/doc/nightly/html/classvtkDataObject.html#a04a5fb60bdbc929ce84f0cd14d911dbe" rel="nofollow noopener">this part of the VTK documentation</a> indicates that the deep copy copies pipeline connections that are not copied in the shallow copy. Perhaps <a href="https://discourse.vtk.org/" rel="nofollow noopener">the VTK discourse</a> would be a good place for this question.</p>

---

## Post #3 by @lassoan (2020-05-19 23:31 UTC)

<p>The wiki page describes this well. In practice, ShallowCopy can be much faster for large data sets, but you need to be very careful when you use it, as data sharing with the source node may have unintended side effects. Most often ShallowCopy is used with a source object that gets deleted soon after the copy.</p>

---
