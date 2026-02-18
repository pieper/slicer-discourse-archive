# Retention policy for Preview releases on "slicer-packages.kitware.com"

**Topic ID**: 31305
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/retention-policy-for-preview-releases-on-slicer-packages-kitware-com/31305

---

## Post #1 by @jcfr (2023-08-23 03:18 UTC)

<p><strong>Overview</strong></p>
<p>As of August 22nd 2023, we host 292 Preview releases on our server (<code>slicer-packages.kitware.com</code>).</p>
<p>Note that <code>Preview</code> release are different from <code>Stable</code> releases. Stable releases will never be removed.</p>
<p>This is roughly equivalent to:</p>
<ul>
<li>880 application installers  (<code>292 revisions * 3 operating systems</code>)</li>
<li>150k extension packages  (<code>292 revisions * 3 operating systems * 177 extensions</code>)</li>
<li>Totaling ~800GB (one preview release ~900MB)</li>
</ul>
<p><strong>Retention Policy:</strong></p>
<p>We plan to keep about 180 Preview releases (roughly 6 months’ worth).</p>
<p><strong>Removal Plan:</strong></p>
<p>At 9pm EST daily:</p>
<ul>
<li>Remove 10 oldest Previews until 180 left</li>
<li>Then, remove one daily.</li>
</ul>

---
