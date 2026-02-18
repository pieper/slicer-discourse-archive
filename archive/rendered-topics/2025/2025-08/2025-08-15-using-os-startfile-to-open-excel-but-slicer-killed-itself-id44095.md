# Using os.startfile to open Excel but Slicer killed itself

**Topic ID**: 44095
**Date**: 2025-08-15
**URL**: https://discourse.slicer.org/t/using-os-startfile-to-open-excel-but-slicer-killed-itself/44095

---

## Post #1 by @aiden.zhu (2025-08-15 15:16 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.8.1<br>
Expected behavior:  open a csv-file via Excel<br>
Actual behavior:  After Excel opens the file, Slicer-3D kills itself (crash?).</p>
<pre><code class="lang-auto">if self.flt_OpenExcelNow_CheckBox.isChecked():
    try:
      tmp= os.startfile( "the_file_nam.csv" )
      print(tmp)
      return
    except:
      print('Done or something wrong? ')
      return
</code></pre>

---
