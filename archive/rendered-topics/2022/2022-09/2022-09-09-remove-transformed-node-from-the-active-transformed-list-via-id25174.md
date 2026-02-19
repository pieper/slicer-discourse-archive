---
topic_id: 25174
title: "Remove Transformed Node From The Active Transformed List Via"
date: 2022-09-09
url: https://discourse.slicer.org/t/25174
---

# Remove transformed node from the active transformed list via python script

**Topic ID**: 25174
**Date**: 2022-09-09
**URL**: https://discourse.slicer.org/t/remove-transformed-node-from-the-active-transformed-list-via-python-script/25174

---

## Post #1 by @Edgaras_Misiulis (2022-09-09 11:29 UTC)

<p>Dear 3D Slicer support,</p>
<p>How to remove transformed node from the active transformed list via python script?</p>
<p>There is a great tutorial on how to set and observe transformation:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=transform#apply-a-transform-to-a-transformable-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=transform#apply-a-transform-to-a-transformable-node</a></p>
<p>however I could not find an opposing similar solution for removal</p>
<p>Thank you, Edgaras</p>

---

## Post #2 by @Edgaras_Misiulis (2022-09-09 14:01 UTC)

<p>I have found the solution:<br>
transformableNode.SetAndObserveTransformNodeID(None)</p>

---
