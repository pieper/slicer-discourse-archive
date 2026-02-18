# Packaging error for custom markups module

**Topic ID**: 23523
**Date**: 2022-05-22
**URL**: https://discourse.slicer.org/t/packaging-error-for-custom-markups-module/23523

---

## Post #1 by @chir.set (2022-05-22 09:39 UTC)

<p>Hi,</p>
<p>One library is missing during packaging while building a custom markups module, which fails to show when installed with the extensions manager pointing to a local *.gz package.</p>
<p>The build directory <em>lib/Slicer-5.1/qt-loadable-modules/</em> contains 9 files, while only 8 files are included in the <em>lib/Slicer-5.1/qt-loadable-modules/</em> directory of the package.</p>
<p>The missing library is <em>libqSlicer${MODULE_NAME}Module.so</em>.</p>
<p>I can manage using --additional-module-paths pointing to the build tree. Reporting as I suppose it may need a fix.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-05-23 02:57 UTC)

<p>Please compare your code to how a custom NURBS surface markup is implemented in the <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup">SurfaceMarkup extension</a>. For example, make sure you remove <code>NO_INSTALL</code> from the CMakeLists.txt.</p>

---

## Post #3 by @chir.set (2022-05-23 07:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="23523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>remove <code>NO_INSTALL</code> from the CMakeLists.txt</p>
</blockquote>
</aside>
<p>Yes this solves the issue.</p>
<p>I had a quick glance at the SurfaceMarkup extension, I noted that the NURBS algorithm allows to create concave surfaces in particular. This is highly interesting, and I’m wondering if something similar can be achieved with a tube or a sphere primitive, rather than a plane. I’ll delve into that as time permits.</p>
<p>Thank you very much.</p>
<p>P.S : I could not find a way to change the title of this discussion, it’s obviously not a packaging error.</p>

---
