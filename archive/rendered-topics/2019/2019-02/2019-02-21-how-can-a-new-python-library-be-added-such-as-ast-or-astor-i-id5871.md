# How can a new python library be added such as ast or astor in the python interpreter?

**Topic ID**: 5871
**Date**: 2019-02-21
**URL**: https://discourse.slicer.org/t/how-can-a-new-python-library-be-added-such-as-ast-or-astor-in-the-python-interpreter/5871

---

## Post #1 by @carlos-luque (2019-02-21 16:36 UTC)

<p>Hello everyone<br>
I´m working the supporting the i18n for script modules, which was started in the 30th project week. In this process, the libraries <em>ast</em> and <em>astor</em> are utilited. The library ast is included in 3d Slicer, but the library astor is not included. I´d like to know how to add new libraries such as astor in the python interperter when the slicer is building.</p>
<p>Thanks in the advances.<br>
Carlos Luque</p>

---

## Post #2 by @Alex_Vergara (2019-02-21 16:49 UTC)

<p>try this solution <a href="https://discourse.slicer.org/t/module-for-internal-dosimetry-in-nuclear-medicine/3317/14?u=alex_vergara" class="inline-onebox">Module for Internal Dosimetry in Nuclear Medicine</a></p>
<p>basically at the end do</p>
<pre><code class="lang-auto">install_and_import('astor')
</code></pre>

---

## Post #3 by @jcfr (2019-02-21 18:16 UTC)

<aside class="quote no-group" data-username="carlos-luque" data-post="1" data-topic="5871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos-luque/48/976_2.png" class="avatar"> carlos-luque:</div>
<blockquote>
<p>the libraries <em>ast</em> and <em>astor</em> are utilited</p>
</blockquote>
</aside>
<p>This could be done like the other python library in Slicer. For example, see <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_python-idna.cmake">https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_python-idna.cmake</a></p>

---

## Post #4 by @carlos-luque (2019-02-22 15:14 UTC)

<p>Hello all,<br>
Thanks for your helps.<br>
I  added the astor in 3D Slicer.</p>

---
