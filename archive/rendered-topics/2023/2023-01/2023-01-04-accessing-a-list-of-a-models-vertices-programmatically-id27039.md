---
topic_id: 27039
title: "Accessing A List Of A Models Vertices Programmatically"
date: 2023-01-04
url: https://discourse.slicer.org/t/27039
---

# Accessing a list of a Model's Vertices programmatically?

**Topic ID**: 27039
**Date**: 2023-01-04
**URL**: https://discourse.slicer.org/t/accessing-a-list-of-a-models-vertices-programmatically/27039

---

## Post #1 by @stevenagl12 (2023-01-04 23:57 UTC)

<p>How would you go about accessing a list of a model’s vertices programmatically once a model has been added to the scene?</p>

---

## Post #2 by @pieper (2023-01-05 00:12 UTC)

<p>This example is for fiber bundles but the access to the poly data is the same with <code>slicer.util.arrayFromModelPoints</code>.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-tract-fiberbundle-streamline-points" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#iterate-over-tract-fiberbundle-streamline-points</a></p>

---

## Post #3 by @stevenagl12 (2023-01-08 22:47 UTC)

<p>Alright thank you very much.</p>

---
