---
topic_id: 1045
title: "Cant Find Staple Filter In Simplefilters"
date: 2017-09-13
url: https://discourse.slicer.org/t/1045
---

# Can't find STAPLE filter in SimpleFilters

**Topic ID**: 1045
**Date**: 2017-09-13
**URL**: https://discourse.slicer.org/t/cant-find-staple-filter-in-simplefilters/1045

---

## Post #1 by @Katrina_Woodford (2017-09-13 20:29 UTC)

<p>Hi all,</p>
<p>The 3DSlicer wiki page for the Simple Filters Module lists a STAPLE Image Filter as one of the filter options. However I can’t seem to find it when using the software.</p>
<p>Can anyone help me locate it?</p>
<p>Thanks,<br>
Katrina</p>

---

## Post #2 by @lassoan (2017-09-13 21:08 UTC)

<p>It seems that <a href="https://github.com/SimpleITK/SlicerSimpleFilters/commit/77eeae334bef866318ed923e786d4af508b994ac">it has been removed</a>. Maybe <a class="mention" href="/u/blowekamp">@blowekamp</a> knows more details.</p>

---

## Post #3 by @blowekamp (2017-09-14 13:39 UTC)

<p>Yes, Andras Lasso is correct it was removed. Here is the archived mailing thread about the discussion:<br>
<a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2016/041191.html" class="onebox" target="_blank" rel="nofollow noopener">http://massmail.spl.harvard.edu/public-archives/slicer-devel/2016/041191.html</a></p>
<p>Could you please create an issue on the repository to fix this filter:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">
      <a href="https://github.com/SimpleITK/SlicerSimpleFilters/issues" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/476215?s=400&amp;v=4" class="thumbnail onebox-avatar" width="337" height="337">

<h3><a href="https://github.com/SimpleITK/SlicerSimpleFilters/issues" target="_blank" rel="nofollow noopener">SimpleITK/SlicerSimpleFilters</a></h3>

<p>A Module for Slicer3D to provide a simple GUI to image filters from the Insight Toolkit. - SimpleITK/SlicerSimpleFilters</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>The documentation should also be updated. And this modules is in need of a bit of TLC.</p>

---

## Post #4 by @Katrina_Woodford (2017-09-16 04:20 UTC)

<p>Thanks Andras and Brad.</p>
<p>I’ve submitted the issue on github as suggested.</p>
<p>Kind regards,<br>
Katrina</p>

---

## Post #5 by @Prashant_Pandey (2020-06-01 18:33 UTC)

<p>Are there any updates to this? I can see the STAPLE algorithm is still missing despite the github issue, and the mailing list link is down for me.</p>

---

## Post #6 by @Prashant_Pandey (2020-06-02 18:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/blowekamp">@blowekamp</a> <a class="mention" href="/u/jcfr">@jcfr</a><br>
I think I fixed one of the issues with the STAPLE filter by reading this discussion <a href="http://slicer-devel-archive.65872.n3.nabble.com/STAPLE-Filter-SimpleFilters-missing-V4-6-td4037712.html" rel="nofollow noopener">http://slicer-devel-archive.65872.n3.nabble.com/STAPLE-Filter-SimpleFilters-missing-V4-6-td4037712.html</a></p>
<p>However I am not sure how to validate if it is working? The algorithm accepts only one volume as input, and from my understanding it should accept multiple binary label maps and output a probability map. However the output is the same as the input. Any ideas?</p>

---

## Post #7 by @lassoan (2020-06-02 20:05 UTC)

<p>How did you fix the issue? Which file have you modified?</p>

---

## Post #8 by @Prashant_Pandey (2020-06-02 20:27 UTC)

<p>For Slicer 4.10.2 in SimpleFilters.py, just above line 956 I inserted:<br>
default = int( max( w.minimum, min(w.maximum, 50)))</p>
<p>And then reinserted the STAPLEImageFilter.json file that was deleted in an earlier commit.</p>

---

## Post #9 by @lassoan (2020-06-02 20:59 UTC)

<p>If you only need to modify Python files then it is easy to test your modifications, as they take effect when you restart Slicer.</p>

---

## Post #10 by @Prashant_Pandey (2020-06-03 14:33 UTC)

<p>That’s not what I meant. I’ve already restarted Slicer and can see the STAPLE is available in Simple Filters.</p>
<p>However when I use it I can’t tell if it’s doing the correct processing. I expect it to produce a probability map as an output but instead it just spits out the input image as the output. If anyone has any experience using STAPLE in ITK I would appreciate their help!</p>

---

## Post #11 by @lassoan (2020-06-03 16:23 UTC)

<p>Probably this question can be answered better on the <a href="https://discourse.itk.org/">ITK forum</a>. If you post your question there, post the link here so that we can follow the discussion.</p>

---
