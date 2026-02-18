# slicer does not open

**Topic ID**: 17792
**Date**: 2021-05-25
**URL**: https://discourse.slicer.org/t/slicer-does-not-open/17792

---

## Post #1 by @surgeon (2021-05-25 13:25 UTC)

<p>Operating system: windows 10 home<br>
Slicer version:4.13.0-2021-5-22<br>
Expected behavior: opens<br>
Actual behavior: does not open</p>
<p>in installed 3D slicer on a new computer, i opened the program and installed extensions from the extension manager.  when rebooting the software did not start at all.  i uninstalled it and reinstalled to check about what was wrong in the extensions i added, but this time slicer did not work at all</p>

---

## Post #2 by @pieper (2021-05-25 19:15 UTC)

<p>Probably you will need to remove the settings files and Slicer should start again:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=settings#settings-file-location" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/settings.html?highlight=settings#settings-file-location</a></p>
<p>It would be good if you could test if the issue is repeatable and if so document the exact extensions you installed that led to the application not starting.</p>

---

## Post #3 by @lassoan (2021-05-26 04:50 UTC)

<p>Has Slicer-4.11 or Slicer-4.13 ever worked on this computer? Maybe its graphics capabilities are not sufficient to run Slicer. What CPU and graphics do you have in this computer?</p>

---

## Post #4 by @mfs797 (2022-03-14 12:57 UTC)

<p>Dear all [<a class="mention" href="/u/lassoan">@lassoan</a>] ,<br>
I’ve jus installed 3DSlicer on my computer and it does not open nor create any log file or wathever. It does nothing, not even the threat of starting.<br>
Those are the specs of my computer :<br>
Operating system : windows 10 home ; version : 21H2<br>
Processor : Intel(R) Core™ i7-4500U CPU @ 1.80GHz   2.40 GHz<br>
RAM : 6.00 GB (5.89 GB usable)<br>
Processor graphics : Intel(R) HD Graphics 4400<br>
Shader version : 5.0<br>
Open GL : 4.3<br>
Open CL : 1.2<br>
3DSlicer version : 4.11.20210226 ; revision : 29738<br>
NOTE: I also tried with the 4.13.0 preview release and nothing.<br>
What do you think is happening?<br>
Thanks in advance!</p>

---

## Post #5 by @lassoan (2022-03-14 13:06 UTC)

<p>We need to balance between backward compatibility and utilizing new hardware features. As a result, we only support running Slicer on computers that are not older than 5 years. See details <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">here</a>.</p>
<p>4th generation Intel CPUs (such as i7-4500U) were released around 2013, so they are well beyond the 5-year cut-off.</p>

---

## Post #6 by @Eduardo_Hernandez (2022-11-08 01:41 UTC)

<p>I’ve jus installed 3DSlicer 5.0.3 on my computer and it just stays on white screen and does not open anything, not even the threat of starting.<br>
Those are the specs of my computer :<br>
Operating system : windows 10 pro ; version : 21H2<br>
Processor : Intel(R) Core™ i3-2365M CPU @ 1.40GHz   1.40 GHz<br>
RAM : 12.00 GB (11.8 GB usable)<br>
Processor graphics : Intel(R) HD Graphics 3000<br>
Shader version : 5.0<br>
Open GL : 4.3<br>
Open CL : 1.2<br>
3DSlicer version : 5.0.3  ; revision : 30893</p>
<p>What do you think is happening?<br>
Thanks in advance!</p>

---

## Post #7 by @lassoan (2022-11-08 01:50 UTC)

<p>i3-2365M CPU was released more than 10 years ago. We need to balance between backward compatibility and taking advantage of new hardware capabilities, and thus we preserve backward compatibility with hardware that was released up to 5 years ago.</p>
<p>If you do not have a more recent computer then you can use free or paid cloud computers to run Slicer on. You may try using a software renderer See some more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">here</a>.</p>

---

## Post #9 by @lassoan (2023-12-05 16:00 UTC)

<p>2 posts were split to a new topic: <a href="/t/slicer-does-not-start-on-older-computer-intel-i3-2365m-release-date-2012/33235">Slicer does not start on older computer (Intel i3-2365M, release date 2012)</a></p>

---
