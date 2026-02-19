---
topic_id: 22867
title: "Dll Linkage Error"
date: 2022-04-07
url: https://discourse.slicer.org/t/22867
---

# DLL linkage error 

**Topic ID**: 22867
**Date**: 2022-04-07
**URL**: https://discourse.slicer.org/t/dll-linkage-error/22867

---

## Post #1 by @SiddarthGanesh (2022-04-07 22:01 UTC)

<div class="md-table">
<table>
<thead>
<tr>
<th>Severity</th>
<th>Code</th>
<th>Description</th>
<th>Project</th>
<th>File</th>
<th>Line</th>
<th>Suppression State</th>
</tr>
</thead>
<tbody>
<tr>
<td>Warning</td>
<td>C4273</td>
<td>‘archive_write_set_format_cpio’: inconsistent dll linkage</td>
<td>C:\v\out\build\x64-Debug\v</td>
<td>C:\v\out\build\x64-Debug\LibArchive\libarchive\archive_write_set_format_cpio.c</td>
<td>6</td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @lassoan (2022-04-09 10:25 UTC)

<p>This is just a warning, probably it is because libarchive gets into your project from multiple sources. You can ignore it, unless you experience any problems with libarchive.</p>

---
