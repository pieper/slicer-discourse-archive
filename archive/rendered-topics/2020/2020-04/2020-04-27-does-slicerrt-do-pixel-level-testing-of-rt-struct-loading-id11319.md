---
topic_id: 11319
title: "Does Slicerrt Do Pixel Level Testing Of Rt Struct Loading"
date: 2020-04-27
url: https://discourse.slicer.org/t/11319
---

# Does SlicerRT do pixel level testing of RT Struct loading?

**Topic ID**: 11319
**Date**: 2020-04-27
**URL**: https://discourse.slicer.org/t/does-slicerrt-do-pixel-level-testing-of-rt-struct-loading/11319

---

## Post #1 by @pieper (2020-04-27 16:43 UTC)

<p>Hi -</p>
<p>We are adding RT display support to OHIF and are planning testing strategy (just display of structs from tcia for now).  We are hoping to emulate what SlicerRT does in this regard.  The question came up as to whether any of the test do pixel level tests of the rendering?</p>
<p>Thanks</p>

---

## Post #2 by @cpinter (2020-04-28 08:37 UTC)

<p>SlicerRT does not test rendering at all, we rely on Slicer to render the data (which are all normal data types) as it is supposed to. SlicerRT does test import and conversion of the RT data types, which checks number of nodes, and number of non-zero voxels, vertices, etc. The functions are tested similarly, with the output being checked in this manner. One special case is DVH, for which we implemented a specific DVH comparison method. These DVH tests also help in catching errors with data loading and conversion, because any geometric misalignment in either the dose or the segmentation results in a different pass rate, which triggers test failure. If you have any questions, please don’t hesitate to ask.</p>

---

## Post #3 by @pieper (2020-04-28 13:17 UTC)

<p>Thank you <a class="mention" href="/u/cpinter">@cpinter</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Yes, it makes sense for SlicerRT to test the quantitative results since that will catch all manner of regressions.  Since we will only be rendering in OHIF we’ll need to find some other approaches.  Some kinds of cross-checking against SlicerRT and other RT display tools is probably our best bet.</p>

---
