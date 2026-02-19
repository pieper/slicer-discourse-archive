---
topic_id: 27325
title: "Get Path Node File Path Directory"
date: 2023-01-18
url: https://discourse.slicer.org/t/27325
---

# Get path node (file path directory)

**Topic ID**: 27325
**Date**: 2023-01-18
**URL**: https://discourse.slicer.org/t/get-path-node-file-path-directory/27325

---

## Post #1 by @lucas_sd (2023-01-18 12:32 UTC)

<p>Hi everybody,</p>
<p>Im working in a module, and I need to save the path directory of a node.</p>
<p>I would like to know if there is a command to get this (like getdirofnode, obtain something like ‘/User/data/etc/’, and save it like a variable).</p>
<p>Thanks, Lucas.</p>

---

## Post #2 by @jamesobutler (2023-01-18 13:52 UTC)

<p>Review information regarding the “Storage Node”.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#the-storage-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#the-storage-node</a></p>
<p>Then check out the script repository for various example usages of the storage node. You should be able to put together various examples that fit your specific use case.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>

---

## Post #3 by @lucas_sd (2023-01-18 14:54 UTC)

<p>Hi James, thanks for the info,</p>
<p>Finally I coud do it using the functions GetStorageNode() and GetFullNameFromFileName().</p>
<p>Thanks, Lucas.</p>

---
