# Should we do something about EM segmenter?

**Topic ID**: 4382
**Date**: 2018-10-06
**URL**: https://discourse.slicer.org/t/should-we-do-something-about-em-segmenter/4382

---

## Post #1 by @lassoan (2018-10-06 21:01 UTC)

<p>Should we do something about EM segmenter? Test failures on the dashboard indicate that it is not working anymore. It seems that TCL/Python bridge is not functional.</p>

---

## Post #2 by @pieper (2018-10-08 21:47 UTC)

<p>I vote for removing EMSegment - it’s not being supported by the original developers and I haven’t heard from user’s having much luck with it lately, even when it was working.  If anyone knows differently please speak up.</p>
<p>The <a href="http://slicer.cdash.org/testDetails.php?test=9196440&amp;build=1393939">tcl/python issue</a> looks fixable, but I believe that bridge code is only used in EMSegment so there may be no point in maintaining it.</p>

---

## Post #3 by @jcfr (2018-10-13 08:31 UTC)

<p>As discussed with the author of EMSegment modules, there are no resources to maintain it. For now, we will simply disable the TCL support in Slicer which will automatically disable the building of EMSegment modules.</p>
<p>If users express interest, we can revisit.</p>

---

## Post #4 by @Padma_Naveena (2019-05-30 09:27 UTC)

<p>Hello</p>
<p>I was looking at automatic segmentation on 3d slicer and EM Segmentation popped up. I was not able to find it on the modules, therefore i checked on the forum and found out the news.</p>
<p>I wanted to know that is there a possibility of applying this module to other parts apart from Brain MRIs if it still existed as a slicer module. I wanted to do segmentation on multiple MRIs and thought something like this would help.<br>
Please advice me.</p>
<p>Thank You!</p>

---

## Post #5 by @lassoan (2019-05-30 12:46 UTC)

<p>All classic automatic segmentation methods (that were developed in the last few decades) have been abandoned and all efforts are directed to make deep learning based methods work. Even when limitations of this new approach will become apparent, it is very unlikely that classic methods, such as the EM segmenter, would ever return, as computing infrastructure, skills of researchers, familiarity of clinicians, and investment of companies and hospitals will all make the landscape more favorable for deep learning based methods.</p>

---
