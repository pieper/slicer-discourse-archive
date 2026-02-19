---
topic_id: 32670
title: "Python Debug Against Slicer Head"
date: 2023-11-08
url: https://discourse.slicer.org/t/32670
---

# Python debug against Slicer `HEAD`

**Topic ID**: 32670
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/python-debug-against-slicer-head/32670

---

## Post #1 by @jhlegarreta (2023-11-08 13:27 UTC)

<p>Hi,<br>
I have visited the 3D Slicer documentation Python debugging documentation:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html" class="inline-onebox" rel="noopener nofollow ugc">Python debugging — 3D Slicer documentation</a></p>
<p>And have visited the <code>SlicerDebuggingTools</code> <code>README</code>:<br>
<a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a></p>
<p>I am wondering whether there is the possibility to debug a given Python code (e.g. a Python test script in an extension) against the 3D Slicer <code>HEAD</code> that we may have checked out and compiled.</p>
<p>Otherwise, using an installed version of Slicer does not strictly guarantee that any fix to a given extension will work with the 3D Slicer <code>HEAD</code>.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-11-09 03:06 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="32670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>I am wondering whether there is the possibility to debug a given Python code (e.g. a Python test script in an extension) against the 3D Slicer <code>HEAD</code> that we may have checked out and compiled.</p>
</blockquote>
</aside>
<p>Yes, this is the preferred method of testing extensions, as this method works for both Python and C++ modules. (it may be hard to ensure ABI compatibility of C++ code built on different computers)</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="32670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Otherwise, using an installed version of Slicer does not strictly guarantee that any fix to a given extension will work with the 3D Slicer <code>HEAD</code>.</p>
</blockquote>
</aside>
<p>If you reproduce a problem on your computer and then fix it on your computer then it is practically guaranteed that the problem will be fixed on the factory computer, too.</p>

---

## Post #3 by @jhlegarreta (2023-11-14 21:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yes, this is the preferred method of testing extensions, as this method works for both Python and C++ modules. (it may be hard to ensure ABI compatibility of C++ code built on different computers)</p>
</blockquote>
</aside>
<p>OK. Thanks. Not sure why, but from the documentation I had the impression that I had to use a release version, but I guess I missed parts of it.</p>
<p>Will give it a try when I’ll have the time.</p>

---
