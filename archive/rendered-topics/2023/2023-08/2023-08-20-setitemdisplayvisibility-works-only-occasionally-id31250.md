---
topic_id: 31250
title: "Setitemdisplayvisibility Works Only Occasionally"
date: 2023-08-20
url: https://discourse.slicer.org/t/31250
---

# SetItemDisplayVisibility works only occasionally

**Topic ID**: 31250
**Date**: 2023-08-20
**URL**: https://discourse.slicer.org/t/setitemdisplayvisibility-works-only-occasionally/31250

---

## Post #1 by @moraleda (2023-08-20 14:14 UTC)

<p>Hi there,</p>
<p>I am creating multiple lineNodes and storing them in multiple folders with Python console in Slicer. E.g. I have folder1 with line1-1, line2-2 and folder2 with line2-1, line2-2. After creating, I want to set visibility to 0 and deexpand the folders. But the following code works only for deexpanding the folders and it just ignores the first line.</p>
<pre><code class="lang-auto">for folderID in folderIDsList:
    shNode.SetItemDisplayVisibility(folderID,0)
    shNode.SetItemExpanded(folderID, 0)
</code></pre>
<p>Lets say ‘folderIDsList = [30,42]’. If I then run single line command ‘shNode.SetItemDisplayVisibility(42,0)’ it also does not do anything.<br>
But if I click with my mouse on the Eye by the folder in the module panel and run the for-loop again, it works!</p>
<p>Could you please explain this behavior to me?</p>
<p>Thank a lot!</p>
<p>Ps.: ‘shNode = slicer.mrmlScene.GetSubjectHierarchyNode()’</p>

---

## Post #2 by @lassoan (2023-08-20 14:17 UTC)

<p>Display nodes are created when needed, for example when you click on the eye icon of a folder item. You can also create a folder display node and set it in the folder item using Python scripting.</p>

---

## Post #3 by @moraleda (2023-08-21 08:38 UTC)

<p>Thank you for the explanation!</p>
<p>I then found more out here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#manipulate-subject-hierarchy-item" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>(Maybe it is useful for future readers.)</p>

---
