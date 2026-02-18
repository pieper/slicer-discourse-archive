# Exceptions in Slicer in kernel 6.0

**Topic ID**: 25808
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/exceptions-in-slicer-in-kernel-6-0/25808

---

## Post #1 by @Alex_Vergara (2022-10-20 12:50 UTC)

<p>When I moved my linux system to use the new kernel 6.0 I started noticing a lot of exceptions like this one.</p>
<pre><code class="lang-auto">QVariant::save: unable to save type ‘PythonQtSafeObjectPtr’ (type id: 1132).
</code></pre>
<p>Some extensions don’t worked anymore (SlicerRT, SlicerElastix, probably others but not yet tested)</p>

---

## Post #2 by @lassoan (2022-10-20 20:51 UTC)

<p>Can you add breakpoint into the Qt logger in CTK to see where this message comes from?</p>
<p>What do you mean by not working? Crashing, hanging, modules not appearing, computing different results, rendering issues?</p>

---
