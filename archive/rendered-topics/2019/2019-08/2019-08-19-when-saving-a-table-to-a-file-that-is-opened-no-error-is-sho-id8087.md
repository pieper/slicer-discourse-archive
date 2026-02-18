# When saving a table to a file that is opened, no error is shown

**Topic ID**: 8087
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/when-saving-a-table-to-a-file-that-is-opened-no-error-is-shown/8087

---

## Post #1 by @JoostJM (2019-08-19 10:19 UTC)

<p>When trying to save a tablenode to a file that is open (using <code>slicer.util.saveNode</code>), the debug log shows:</p>
<p><code>[ERROR][VTK] 19.08.2019 12:16:13 [vtkDelimitedTextWriter (000000001D364F00)] (D:\D\P\Slicer-0-build\VTK\IO\Core\vtkDelimitedTextWriter.cxx:91) - Unable to open file</code></p>
<p>However, <code>slicer.util.saveNode</code> still returns <code>True</code>. How can I detect if Slicer stored the table successfully from my script?</p>
<p>Slicer 4.11-2019-05-13<br>
Windows 7</p>

---

## Post #2 by @lassoan (2019-08-22 02:28 UTC)

<p>Thanks for reporting this. I’ve fixed this now (in r28455).</p>

---
