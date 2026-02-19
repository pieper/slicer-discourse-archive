---
topic_id: 5932
title: "Sequences Possible To Save Multiple Sequences To One File"
date: 2019-02-26
url: https://discourse.slicer.org/t/5932
---

# [Sequences] Possible to save multiple sequences to one file?

**Topic ID**: 5932
**Date**: 2019-02-26
**URL**: https://discourse.slicer.org/t/sequences-possible-to-save-multiple-sequences-to-one-file/5932

---

## Post #1 by @adamrankin (2019-02-26 16:16 UTC)

<p>Is it possible to save multiple sequences to a single file?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>

---

## Post #2 by @mholden8 (2019-02-26 17:01 UTC)

<p>We had talked about implementing an export feature for sequence browser nodes: <a href="https://github.com/SlicerRt/Sequences/issues/13" rel="nofollow noopener">https://github.com/SlicerRt/Sequences/issues/13</a>.</p>
<p>In Perk Tutor, we implemented a solution for exporting a sequence browser node as a single file. This solution should already work for almost any type of node sequence. We use it regularly for transform and tracked ultrasound sequences. We can think about moving this functionality to Sequences extension.</p>
<p>In the short term, you can install Perk Tutor extension and try it out for your data. Note that exporting is not available through the generic save dialog; you must export from one of the Perk Tutor modules directly. You can reload in the usual way (e.g. drag-and-drop).</p>

---

## Post #3 by @adamrankin (2019-02-26 17:09 UTC)

<p>Not bad! It would be nice if the sequence browser node was savable if all the contained sequences were compatible (same index type, etc…)</p>

---
