# Why is master-48 branch divergent from trunk history?

**Topic ID**: 1336
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/why-is-master-48-branch-divergent-from-trunk-history/1336

---

## Post #1 by @ihnorton (2017-10-31 19:06 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/381981bd0e8ebedc7c909e3af57068ed1edb3e08.png" alt="image" data-base62-sha1="80hnXifcxM8Cv19PukzviQcO9xS" width="451" height="136"></p>
<p>I noticed this when pushing a branch that I had incidentally created from the <code>master-48</code>… This divergence makes tree downloads much larger than necessary, and will make cherry-picks difficult.</p>

---

## Post #2 by @jcfr (2017-10-31 19:10 UTC)

<p>The difference is inherent to the current relationship to svn.</p>
<p>If a topic is created of <code>master-48</code>, the associated PR should be done against that same base. Then, it should work out pretty well.</p>
<p>I am not sure to understand the difficulty added for cherry-picking.</p>

---

## Post #3 by @jcfr (2017-10-31 19:11 UTC)

<p>Also, to learn more about how the release branch is created. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Release">https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Release</a></p>

---
