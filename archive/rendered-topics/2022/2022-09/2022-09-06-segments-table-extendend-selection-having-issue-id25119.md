# Segments Table Extendend Selection having issue

**Topic ID**: 25119
**Date**: 2022-09-06
**URL**: https://discourse.slicer.org/t/segments-table-extendend-selection-having-issue/25119

---

## Post #1 by @ssv (2022-09-06 11:24 UTC)

<p>Slicer Version : 5.1.0<br>
OS : Windows 11</p>
<p>I am trying to do extended selection mode on segments table the selection works from top to bottom  . But when i select bottom to top its only select one row</p>
<pre><code class="lang-auto">getModuleWidget('SegmentEditor').editor.Form.SegmentsTableView.setSelectionMode(qt.QAbstractItemView().ExtendedSelection)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52fe7cf98ea4c671418c2073a02fc318e59dc066.png" alt="Screenshot 2022-09-06 114549" data-base62-sha1="bQcoeYR5gQzCavS7m58aRT9YT1Y" width="687" height="255"></p>

---
