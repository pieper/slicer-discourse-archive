# Help with memory management

**Topic ID**: 22021
**Date**: 2022-02-17
**URL**: https://discourse.slicer.org/t/help-with-memory-management/22021

---

## Post #1 by @bcolbert (2022-02-17 13:03 UTC)

<p>This is kind of a follow-up from my previous question. I have stopped saving mrb and am saving and loading nrrd files. But these are still very large (4gb). No issues with saving but I am having issues with segmenting. I use the grow from seeds function to segment 14 separate structures from background tissue. When I last did this some months ago I was able to paint starting seeds on these structures and then get initial results ~15min after initializing. Now it is taking me hours on a computer with 64gb RAM. Is this a function of the size of the file (i.e., I need to down sample it or otherwise reduce size) or is there something else I can do?</p>

---

## Post #2 by @muratmaga (2022-02-17 17:07 UTC)

<p>Were the ones that took about 15 minutes were downsampled perhaps? Remember the volume of the data increases with cube, so doubling the resolution will increase data volume 8 folds.</p>
<p>If you can downsample to a resolution where you can still see the structures you are interested in sufficient detail. Alternatively use the crop volume to create a subvolume that only contains the region you are interested. The trick is to reduce the data volume using one of these strategies.</p>

---

## Post #3 by @lassoan (2022-02-18 16:57 UTC)

<p>We have made significant performance improvements to Grow from seeds method in recent months, so please try the latest Slicer Preview Release and let us know if the speed is the same or better than before.</p>

---
