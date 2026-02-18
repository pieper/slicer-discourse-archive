# Many core experiment

**Topic ID**: 12944
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/many-core-experiment/12944

---

## Post #1 by @pieper (2020-08-11 18:04 UTC)

<p>Just as a test, I created an <a href="https://cloud.google.com/compute/docs/machine-types#n2d_machine_types">N2D</a> type virtual machine on Google Cloud with 224 cores running Ubuntu 20.04.</p>
<p>I did a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa">standard linux build</a> with the default settings, so SimpleITK and Testing enabled.</p>
<p>It took just under 20 minutes to build everything with <code>make -j 500</code>.</p>
<p>Watching <code>top</code>, there were a few places where a single <code>perl</code> or <code>cmake</code> process was a chokepoint but it was amazing to see how fast the C++ compilation went.</p>

---

## Post #2 by @pieper (2020-08-11 18:09 UTC)

<p>Oh, and I should mention the machine costs under $6 per hour.</p>

---

## Post #3 by @lassoan (2020-08-11 18:10 UTC)

<p>Wow. On some computers, download of the binary takes longer then this build time.</p>
<p>It could be interesting to build with TBB support enabled.</p>

---

## Post #4 by @pieper (2020-08-11 18:12 UTC)

<p>I wasn’t able to try running because I couldn’t set up a GPU on it.  I think the limit is 16 cores if you need a GPU.  But we could probably try some CLIs.  Or tunnel X through ssh.</p>

---

## Post #5 by @lassoan (2020-08-11 18:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="12944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I couldn’t set up a GPU on it</p>
</blockquote>
</aside>
<p>In theory, it should be possible to use a software renderer (Mesa), but I guess it may not be trivial to set up.</p>

---

## Post #6 by @pieper (2020-08-11 18:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="12944">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In theory, it should be possible to use a software renderer (Mesa), but I guess it may not be trivial to set up.</p>
</blockquote>
</aside>
<p>The problem I ran into is that I couldn’t start the X server without a display card on the system.  It might be possible to do that with Xdummy like it is in the containerized Slicer.</p>
<p>Or actually, it could be interesting to just run the docker slicer version and see how it performs.  It should be possible to build and run a TBB optimized Slicer inside the container environment and it should be able to access the same cores.</p>
<p>Is there any particular multithreaded workload that would worth trying?</p>

---

## Post #7 by @lassoan (2020-08-11 18:45 UTC)

<p>Loading a very large volume and interactively segmenting it (with 3D display) and visualizing it could be interesting. Also, Sequence registration with the sample cardiac sequence data sets (using SlicerElastix).</p>
<p>But I guess this massively parallel system could be best leveraged with your parallel CLI execution module.</p>

---
