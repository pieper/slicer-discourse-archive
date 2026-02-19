---
topic_id: 29321
title: "Add Segmentation With Sphere Brush From Known Coordinates Vi"
date: 2023-05-06
url: https://discourse.slicer.org/t/29321
---

# Add segmentation with sphere brush from known coordinates via scripts

**Topic ID**: 29321
**Date**: 2023-05-06
**URL**: https://discourse.slicer.org/t/add-segmentation-with-sphere-brush-from-known-coordinates-via-scripts/29321

---

## Post #1 by @hapkx (2023-05-06 19:34 UTC)

<p>This problem may be simple, but I can’t find the right solution for the moment.<br>
There are some coordinates, for example(10, 10, 10) and (20, 20, 20), and I want to add ‘paint’ (maybe with a sphere brush) at the corresponding position of each coordinate within one segmentation node, is it possible? What should I do?<br>
Thanks a lot inadvance!</p>

---

## Post #2 by @pieper (2023-05-07 12:09 UTC)

<p>There are <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">examples in the Script Repository</a> that should help.  <a href="https://gist.github.com/lassoan/2d5a5b73645f65a5eb6f8d5f97abf31b">This example</a> in particular is close to what you asked for.</p>

---

## Post #3 by @hapkx (2023-05-07 15:23 UTC)

<p>Thanks alot. I tried this, but it looks like the overlap has become hollow. Is there a solution to this problem?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86216ff78035073e4084eedd95fe5cd094cea8a.png" alt="image" data-base62-sha1="x9KVDz6vCDjafTTF5SrgY4uGcpY" width="107" height="112"></p>

---

## Post #4 by @lassoan (2023-05-08 05:14 UTC)

<p>If you append overlapping meshes then intersecting regions will be considered as “outside” (this allows definition of shapes with holes in them). In your case you don’t want intersections to be hollow, so don’t append the meshes. Instead, you can add the meshes to the segmentation one by one and combine them as segments, using “Logical operations” effect.</p>

---

## Post #5 by @hapkx (2023-05-08 12:55 UTC)

<p>That works. Thank you!</p>

---
