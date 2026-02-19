---
topic_id: 4521
title: "Building Slicer 4 10 0 From Source On Ubuntu 18 04"
date: 2018-10-24
url: https://discourse.slicer.org/t/4521
---

# Building SLicer 4.10.0 from source on Ubuntu 18.04

**Topic ID**: 4521
**Date**: 2018-10-24
**URL**: https://discourse.slicer.org/t/building-slicer-4-10-0-from-source-on-ubuntu-18-04/4521

---

## Post #1 by @brhoom (2018-10-24 21:57 UTC)

<p>Slicer 4.10.0 with Qt4.8 and VTK 7 is built from source successfully on Ubuntu 18.04 but I had to add  this line  to the main CMakeList.txt file due to some error related to c11 support.</p>
<pre><code> set (CMAKE_CXX_STANDARD 11)
</code></pre>
<p>after  these two  lines</p>
<pre><code> set(_msg "Setting C++ standard")
 message(STATUS "${_msg}")</code></pre>

---

## Post #2 by @brhoom (2018-10-28 12:59 UTC)

<p>One more thing:</p>
<p>I am not CMake expert but there should be some restriction about building priorities. When I use</p>
<pre><code>       make -j 8
</code></pre>
<p>The build stop with error. It would be nice to arrange this so one can benefit from parallel build.</p>

---

## Post #3 by @lassoan (2018-10-28 14:16 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="2" data-topic="4521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>The build stop with error</p>
</blockquote>
</aside>
<p>What is the error? Parallel build should work (it is not managed by setting priorities but setting correct dependencies between build targets).</p>

---

## Post #4 by @chir.set (2018-10-28 15:21 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="2" data-topic="4521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>so one can benefit from parallel build</p>
</blockquote>
</aside>
<p>Parallel build does work. I usually build with -j12 on Arch (nproc x 2, good or bad).</p>

---

## Post #5 by @brhoom (2018-10-28 15:29 UTC)

<p>I am doing a new parallel build now i.e. -j 8. I am using Qt5 and VTK 8, as soon as I get an error, I will report it here.</p>

---

## Post #6 by @pieper (2018-10-28 15:34 UTC)

<p>Yes, parallel builds work fine, but often the actual build error is hard to see because other build output causes it to scroll offscreen.  In this case I often use a command like <code>make -j20; make</code> so the actual error shows up efficiently.</p>

---

## Post #7 by @chir.set (2018-10-28 15:59 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="4521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>a command like <code>make -j20; make</code> so the actual error shows up efficiently.</p>
</blockquote>
</aside>
<p>I usually redirect stderr to a timestamped log file :</p>
<blockquote>
<p>nice -n19 make Slicer -j12 2&gt; ~/tmp/slicer_build_err_$(date +%F_%H%M%S).log</p>
</blockquote>
<p>Build errors are easily tracked this way.</p>
<p>Just a suggestion.</p>

---

## Post #8 by @brhoom (2018-10-28 19:07 UTC)

<p>Thanks for the tips. The build just completed without error. It seems the previous one had some strange problem. Next step, test building on Windows 10.</p>

---
