---
topic_id: 12031
title: "Heap Space For Slicer"
date: 2020-06-15
url: https://discourse.slicer.org/t/12031
---

# Heap space for Slicer

**Topic ID**: 12031
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/heap-space-for-slicer/12031

---

## Post #1 by @Deepa (2020-06-15 11:52 UTC)

<p>Hi All,</p>
<p>I am facing memory issues while running tasks like centerline line extraction using Slicer installed on a server.</p>
<p>I’d like to know how to increase the heap space for Slicer.</p>

---

## Post #2 by @pieper (2020-06-15 15:47 UTC)

<p>Hi - It’s what Andras mentioned before.  Ideally you add more RAM, or if not you allocate more swap space (linux) or virtual memory (windows).  There’s nothing slicer-specific required.</p>

---

## Post #3 by @Deepa (2020-06-15 16:19 UTC)

<p>Thank you. I thought there would be Slicer specific options . For instance, I find application specific options mentioned <a href="https://stackoverflow.com/questions/15313393/how-to-increase-application-heap-size-in-eclipse" rel="nofollow noopener">here</a></p>

---

## Post #4 by @muratmaga (2020-06-15 17:19 UTC)

<p>That’s for Java applications. Slicer will utilize up to the physical memory available in your system. If you are using a shared server or a VM, may be the admins are constraining it?</p>

---

## Post #5 by @Deepa (2020-06-15 17:44 UTC)

<p>Thank you. Yes, I am using a shared server.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b54f51893937ba1b39ef6b52d8a176f98b291dc.png" data-download-href="/uploads/short-url/fjv6NQt3VhpFbN8Nb1S9TBvvPTC.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b54f51893937ba1b39ef6b52d8a176f98b291dc.png" alt="Untitled" data-base62-sha1="fjv6NQt3VhpFbN8Nb1S9TBvvPTC" width="690" height="80" data-dominant-color="707070"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">859×100 4.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I could find free swap space at the instant when bad_alloc error appeared. So I am not sure if the swap space has to be increased.</p>

---
