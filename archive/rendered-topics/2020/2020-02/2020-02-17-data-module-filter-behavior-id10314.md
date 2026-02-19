---
topic_id: 10314
title: "Data Module Filter Behavior"
date: 2020-02-17
url: https://discourse.slicer.org/t/10314
---

# Data module filter behavior

**Topic ID**: 10314
**Date**: 2020-02-17
**URL**: https://discourse.slicer.org/t/data-module-filter-behavior/10314

---

## Post #1 by @giovform (2020-02-17 18:05 UTC)

<p>Hi, I have a directory structure within the data module, and I noticed if I write in the filter box a string that doesn’t match any names, it collapses all the directories, and I have to open them all again. If there is a match, the collapse doesn’t happen. Is this intentional?</p>

---

## Post #2 by @cpinter (2020-02-18 14:42 UTC)

<p>This does not sound intentional. I find it strange that if there is a match it does not collapse, but it does otherwise. This suggests to me that the problem is in Qt’s sort filter proxy model, but it would need to be investigated.</p>

---
