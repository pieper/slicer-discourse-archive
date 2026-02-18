# Random number generator and reproducibility issues

**Topic ID**: 20009
**Date**: 2021-10-05
**URL**: https://discourse.slicer.org/t/random-number-generator-and-reproducibility-issues/20009

---

## Post #1 by @muratmaga (2021-10-05 04:17 UTC)

<p>We running into an issue where, when we run the same dataset couple times back to back, we get slightly different results. These are subtle differences, but when combined, they are enough to create extra variation and impact the results.</p>
<p>So how does one go about reproducibility in SLicer? Normally we would do things like specifying a specific seed for RNG, but if we do that does that impact operations in Slicer, or only within our module? Is there some examples we can take a look at ?</p>
<p><a class="mention" href="/u/chz31">@chz31</a> <a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #2 by @lassoan (2021-10-05 16:40 UTC)

<p>This is not application-level feature, but it is up to the algorithm to expose an interface for specifying a random seed. Algorithms should not use any global shared random number generator but an object that the algorithm owns. In VTK you would use an object of <a href="https://vtk.org/doc/nightly/html/classvtkRandomSequence.html">this class</a>, in ITK you would use <a href="https://itk.org/Doxygen310/html/classitk_1_1Statistics_1_1RandomVariateGeneratorBase.html">this class</a>, etc.</p>
<p>Of course, most algorithms still won’t produce exactly the same results on different computers (different CPU, C runtime, etc. give different results for the same floating-point operations) and for each run (due to multi-threaded implementation). In theory, you could achieve 100% reproducibility of the results, but since it requires turning off most optimizations, run single-threaded, and building everything from source on all platforms, this requires a lot of extra effort. What is even worse is that the resulting algorithm implementation would not suitable for end users, as it would be just so much slower than the approximate implementation.</p>
<p>I think putting a lot of effort into 100% reproducibility of a tiny part of a workflow (running some processing algorithm on some data) is actually harmful, because it takes the time away from the real goal: reproducibility of the entire workflow. The entire workflow includes imaging, specifying additional user inputs, processing, visualization of results, etc. This requires open-source code, open data, automatic testing, documentation, training, tutorials, etc., which may not sound as exciting but essential for the overall advancement of a field.</p>

---

## Post #3 by @muratmaga (2021-10-05 16:56 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20009">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is not application-level feature, but it is up to the algorithm to expose an interface for specifying a random seed. Algorithms should not use any global shared random number generator but an object that the algorithm owns. In VTK you would use an object of <a href="https://vtk.org/doc/nightly/html/classvtkRandomSequence.html">this class </a>, in ITK you would use <a href="https://itk.org/Doxygen310/html/classitk_1_1Statistics_1_1RandomVariateGeneratorBase.html">this class</a>, etc.</p>
</blockquote>
</aside>
<p>Just clarify, if I do<br>
np.random.seed(1)<br>
will that affect all Slicer session on my specific module?</p>

---

## Post #4 by @jcfr (2021-10-05 17:55 UTC)

<p>Ideally, you should not used the legacy interface to seed random numbers.</p>
<pre><code class="lang-python">    def seed(self, seed=None):
        """
        seed(self, seed=None)
        Reseed a legacy MT19937 BitGenerator
        Notes
        -----
        This is a convenience, legacy function.
        The best practice is to **not** reseed a BitGenerator, rather to
        recreate a new one. This method is here for legacy reasons.
        This example demonstrates best practice.

        &gt;&gt;&gt; from numpy.random import MT19937
        &gt;&gt;&gt; from numpy.random import RandomState, SeedSequence
        &gt;&gt;&gt; rs = RandomState(MT19937(SeedSequence(123456789)))
        # Later, you want to restart the stream
        &gt;&gt;&gt; rs = RandomState(MT19937(SeedSequence(987654321)))
        """
[...]
</code></pre>
<p>References:</p>
<ul>
<li><a href="https://github.com/numpy/numpy/blob/v1.19.5/numpy/random/mtrand.pyx#L222-L245" class="inline-onebox">numpy/mtrand.pyx at v1.19.5 · numpy/numpy · GitHub</a></li>
</ul>

---

## Post #5 by @jcfr (2021-10-05 18:01 UTC)

<p>Also worth noting that seeding the generator using <code>numpy.random.seed</code> impacts other modules using the legacy interface.</p>
<p>So it should not be done in module logic and only reserved for testing.</p>
<p>For some more background, see <a href="https://stackoverflow.com/questions/57728209/why-using-numpy-random-seed-is-not-a-good-practice" class="inline-onebox">python - Why using numpy.random.seed is not a good practice? - Stack Overflow</a></p>

---
