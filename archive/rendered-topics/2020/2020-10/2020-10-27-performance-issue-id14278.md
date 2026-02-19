---
topic_id: 14278
title: "Performance Issue"
date: 2020-10-27
url: https://discourse.slicer.org/t/14278
---

# Performance Issue

**Topic ID**: 14278
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/performance-issue/14278

---

## Post #1 by @jrl (2020-10-27 20:02 UTC)

<p>I have a python module that is taking in a volume and outputting a new volume. There’s millions of operations that are being done, which I think is the root cause of the performance issue I am having. Furthermore, when I run the script outside of the slicer application (using the terminal), it takes several minutes for the script to complete. I just wanted to see if there are any suggestions or options that I might have for speeding up the performance of the Slicer module. Because the python script on its own is taking several minutes, is that the key rate-limiting issue? Is there a way to do all of those operations more quickly? Could it help improve performance if I use C++ instead of python? Thank you.</p>

---

## Post #2 by @pieper (2020-10-27 20:11 UTC)

<p>Many operations on volumes can be delegated to existing compiled code, either with numpy, VTK, or SimpleITK.  So it all depends on what you are calculating in your python code.  If there’s no direct implementation with existing filters/operations then sometimes yes, you need to write C++ code.  It’s not the end of the world but there are more steps to deal with (see documentation on writing Loadable to CLI modules).</p>

---

## Post #3 by @jrl (2020-10-28 20:31 UTC)

<ol>
<li>Do you know how significant of an improvement using C++ could be? It would have be extremely significant for it to be worth it to use instead of python</li>
<li>Following up on your comment, if I wanted to edit voxels individually what would be my best bet then? C++? Are there any efficient ways with those libraries you mentioned to do so? I’m not super familiar with VTK or SimpleITK and not sure of an easy way to do that without iterating through the voxels.</li>
</ol>

---

## Post #4 by @pieper (2020-10-28 20:59 UTC)

<p>Here’s a video that demonstrates the difference.  First half is python and second is the same operation in c++.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xcQKj4yp2nw" data-video-title="SlicerCPPYY 2020 04 09" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xcQKj4yp2nw" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xcQKj4yp2nw/maxresdefault.jpg" title="SlicerCPPYY 2020 04 09" width="" height="">
  </a>
</div>

<p>This video was made with a slightly <a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5">experimental approach</a> but should be representative of the speed tradeoffs for some operations where you iterate through large data with python code.</p>

---

## Post #5 by @lassoan (2020-10-28 21:00 UTC)

<aside class="quote no-group" data-username="jrl" data-post="3" data-topic="14278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/fbc32d/48.png" class="avatar"> jrl:</div>
<blockquote>
<p>Do you know how significant of an improvement using C++ could be? It would have be extremely significant for it to be worth it to use instead of python</p>
</blockquote>
</aside>
<p>Iterating through all the voxels of a volume and doing some processing operation on it is typically about 100x faster in C++. This does not mean that you need to use C++, just that you should never ever think about doing pixel-by-pixel processing in Python.</p>
<p>Instead, you can process volumes very efficiently by vector and matrix operations (for example, using numpy) or use other high-level processing functions (in ITK, VTK, SciPy, etc). These tools are all implemented in C++ with a very thin wrapping layer, so they work as fast as raw C++.</p>
<p>You only need to write C++ code if you need to develop new low-level processing algorithms, but that is very rare.</p>

---
