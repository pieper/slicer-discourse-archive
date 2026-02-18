# Change module event

**Topic ID**: 33790
**Date**: 2024-01-16
**URL**: https://discourse.slicer.org/t/change-module-event/33790

---

## Post #1 by @park (2024-01-16 05:18 UTC)

<p>Hi all</p>
<p>I would like to make some function which operates when the module is changed.<br>
(I don’t want to use .slicerrc.py)</p>
<p>Could you give me some tips to implement this ?</p>

---

## Post #2 by @pieper (2024-01-16 21:02 UTC)

<p>Each module has an <code>enter</code> method where it can do things.  Or you can use <code>slicer.util.moduleSelector</code> and connect to the <code>moduleSelected</code> signal.</p>
<p>Like this:</p>
<pre><code class="lang-auto">slicer.util.moduleSelector().connect('moduleSelected(QString)', print)
</code></pre>

---
