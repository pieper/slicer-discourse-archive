# Slicer can be installed without administrator privileges on Windows

**Topic ID**: 7137
**Date**: 2019-06-12
**URL**: https://discourse.slicer.org/t/slicer-can-be-installed-without-administrator-privileges-on-windows/7137

---

## Post #1 by @lassoan (2019-06-12 14:12 UTC)

<p>Starting from tomorrow, Slicer-4.11.x versions will not require administrator privileges for installation on Windows.</p>
<p>The change was motivated by requests to make it easier to install Slicer in locked-down environments, and to make it easier to install additional Python packages (administrator command prompt is not needed anymore, and there is no risk that one user breaks Python environment of another).</p>
<p>Slicer install tree can be accessed as  <code>%LOCALAPPDATA%\NA-MIC</code>  (usually it resolves to something like  <code>C:\Users\&lt;username&gt;\AppData\Local\NA-MIC</code> ).</p>
<p>Slicer can still be installed so that it is available for all users by changing the installation path that is offered by default to a location that is accessible to all users (such as Program Files or %ALLUSERSPROFILE%).</p>
<p>Any feedback or questions are welcome.</p>

---

## Post #2 by @hherhold (2019-06-17 01:40 UTC)

<p>While this change is not exactly a “game changer”, it’s pretty close.</p>
<p>Many thanks indeed.</p>

---
