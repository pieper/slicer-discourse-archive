---
topic_id: 20871
title: "How To Change The Slice Fill In Segmentations In A Python Sc"
date: 2021-12-01
url: https://discourse.slicer.org/t/20871
---

# How to change the slice fill in 'Segmentations' in a python script

**Topic ID**: 20871
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/how-to-change-the-slice-fill-in-segmentations-in-a-python-script/20871

---

## Post #1 by @koeglfryderyk (2021-12-01 22:24 UTC)

<p>I created a .py script to automatically create some segmentations and now I also want to automatically change the slice fill to 0 and slice outline to 1. How can I do that? I can’t find the appropriate documentation.</p>
<p>Also a more general question: what’s the best way to look for code or commands that correspond to elements and actions in the user interface?</p>

---

## Post #2 by @lassoan (2021-12-02 18:17 UTC)

<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="20871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>I created a .py script to automatically create some segmentations and now I also want to automatically change the slice fill to 0 and slice outline to 1. How can I do that? I can’t find the appropriate documentation.</p>
</blockquote>
</aside>
<p>Display settings are stored in the display node. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-segmentation-display-options">example</a> and <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html">API reference</a> for details.</p>
<aside class="quote no-group" data-username="koeglfryderyk" data-post="1" data-topic="20871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/koeglfryderyk/48/14638_2.png" class="avatar"> koeglfryderyk:</div>
<blockquote>
<p>Also a more general question: what’s the best way to look for code or commands that correspond to elements and actions in the user interface?</p>
</blockquote>
</aside>
<p>We collect python scripting examples of all frequently used features in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>. If you don’t find something then you can look up by following the technique described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">here</a>. If you get stuck then post here on the forum.</p>
<hr>
<p>Do you have any suggestion of how to improve our documentation or make things easier to find? How did you try to find the relevant piece of documentation?</p>

---

## Post #3 by @koeglfryderyk (2021-12-02 19:26 UTC)

<p>Thanks, that worked beautifully!</p>
<p>At the moment I don’t have any suggestions. I can only say that I didn’t find the API Reference very helpful, what helped me the most was the script repository and questions posted here. I feel like examples were the most helpful.</p>
<p>If I come up with any suggestions I’ll make sure to share them</p>

---
