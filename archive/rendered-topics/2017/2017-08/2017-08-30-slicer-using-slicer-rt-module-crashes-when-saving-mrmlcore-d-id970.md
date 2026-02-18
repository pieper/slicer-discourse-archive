# Slicer (using Slicer RT module) crashes when saving. 'MRMLcore.dll' error from Windows event log

**Topic ID**: 970
**Date**: 2017-08-30
**URL**: https://discourse.slicer.org/t/slicer-using-slicer-rt-module-crashes-when-saving-mrmlcore-dll-error-from-windows-event-log/970

---

## Post #1 by @LauDel (2017-08-30 15:08 UTC)

<p>Operating system: Windows 7 Enterprise 64bit<br>
Slicer version: 4.6.2<br>
Expected behavior: The scene should be saved as mrml scene OR separate components (both approaches fail)<br>
Actual behavior: Slicer hangs for a few seconds on the saving screen, then slicer becomes unresponsive and windows gives the error ‘Slicerapp-real doesn’t work anymore’ and I’m forced to select ‘close program’. No error is given.</p>
<p>I found the error in Windows event log. It is filed as an application error where SlicerApp-real.exe failed were the  module  MRMLCore.dll gave an error.</p>
<p>This problem happens everytime I try to save my work. Maybe of importance: I run slicer as an administrator because if i don’t i cannot access my installed modules (there are strict admin-user rights at my institution)</p>
<p>Any help would be much appreciated!</p>
<p>Greetings,<br>
Laurence</p>

---

## Post #2 by @cpinter (2017-08-30 15:26 UTC)

<p>Hi Laurence,</p>
<p>4.6.2 is approaching its first birthday, and many issues have been fixed and many features added since then. Even if we find the root of the problem, it is unlikely we fix a 10-month old release. Please try the latest nightly.</p>

---

## Post #3 by @LauDel (2017-08-31 06:50 UTC)

<p>Hello Csaba,</p>
<p>Thank you for your feedback. I’ve installed the latest nightly, hower SlicerRT is not available (yet). I really need<br>
this module because I have to import RT Structure sets. So this is not an option for me.</p>
<p>Greetings,<br>
Laurence</p>

---

## Post #4 by @cpinter (2017-08-31 12:49 UTC)

<p>It is available now.</p>
<p>In the future you can download nightlies from past days using this modifier in the url<br>
<a href="http://download.slicer.org/?offset=-1" class="onebox" target="_blank">http://download.slicer.org/?offset=-1</a></p>

---
