---
topic_id: 20740
title: "Save Directory According To Subject Hierarchy"
date: 2021-11-23
url: https://discourse.slicer.org/t/20740
---

# Save directory according to subject hierarchy

**Topic ID**: 20740
**Date**: 2021-11-23
**URL**: https://discourse.slicer.org/t/save-directory-according-to-subject-hierarchy/20740

---

## Post #1 by @Kanga (2021-11-23 05:21 UTC)

<p>Apologies if this is already possible, but it would be really helpful for me to save data nodes in a folder structure equivalent to the subject hierarchy (or maybe even arbitrary attributes) via GUI (I’m trying to use minimal code for a clinic-friendly handover document).<br>
I know we can create a subject hierarchy from a folder structure, how about the reverse?</p>
<p>Excellent software, btw <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2021-11-23 15:22 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-files-to-directory-structure-matching-subject-hierarchy-folders">this code snippet</a> to save nodes to the file system in the same directory structure as the subject hierarchy tree.</p>
<p>You can run this script on a keyboard combination (see how to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">assign Ctrl+Shift+S keyboard shortcut here</a>) or you can override the default save dialog (or just update the paths automatically before showing the save dialog), add a toolbar button, custom module (especially if you already provide a module for some application-specific features), etc. All these just require a couple of lines of Python script.</p>

---

## Post #3 by @Kanga (2021-11-24 03:00 UTC)

<p>Thanks Andras for your very informative answer!</p>

---
