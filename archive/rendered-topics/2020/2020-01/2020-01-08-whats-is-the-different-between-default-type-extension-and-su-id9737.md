---
topic_id: 9737
title: "Whats Is The Different Between Default Type Extension And Su"
date: 2020-01-08
url: https://discourse.slicer.org/t/9737
---

# What's is the different between default type extension and superbuild type extension?

**Topic ID**: 9737
**Date**: 2020-01-08
**URL**: https://discourse.slicer.org/t/whats-is-the-different-between-default-type-extension-and-superbuild-type-extension/9737

---

## Post #1 by @leemoncn (2020-01-08 08:24 UTC)

<p>I read the wiki documents,but i can’t find what’s is the different between default type extension and superbuild type extension?</p>

---

## Post #2 by @lassoan (2020-01-08 14:08 UTC)

<p>You use superbuild type extension if your extension depends on third-party libraries that you need to build as part of the build process (for example, SlicerRT extension builds Plastimatch library; SlicerElastix extension builds Elastix library). For all other cases, you can use the simpler default template.</p>

---

## Post #3 by @Luther (2020-01-09 10:43 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the information</p>

---
