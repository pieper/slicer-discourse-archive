# Data copied from Windows to Mac

**Topic ID**: 21679
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/data-copied-from-windows-to-mac/21679

---

## Post #1 by @Kim_Geboers (2022-01-28 14:55 UTC)

<p>Operating system: macOS Monterey 12.2<br>
Slicer version: 4.11.20210226</p>
<p>Dear 3D-Slicer users,<br>
I recently bought a MacBook Pro and have installed 3D-Slicer without any problems. My previous laptop was a Windows, so I wanted to transfer all my data from Slicer to my MacBook. The problem is, when I open an already completed file (meaning it is segmented etc), it is blank. When I check the “Data” compartment, it is also blank. Is there something extra that I need to download from Slicer (internally in the program) or do I need to convert my data (Windows versus OS)? Or am I forgetting something? I hope you guys can help me!<br>
Sincerely,<br>
Kim Geboers</p>

---

## Post #2 by @hherhold (2022-01-28 15:17 UTC)

<p>I move data between windows and Mac all the time, so there aren’t any file format conversions. Make sure you’ve moved all the files in a project - the mrml file points to the volume, segmentations, models, markups, etc - these are all separate files, unless you’ve saved it as an mrb bundle file.</p>
<p>The documentation has detailed info on files and saving:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---

## Post #4 by @Kim_Geboers (2022-01-28 18:29 UTC)

<p>Thank you very much for your reply! It has been a while since I first installed 3D-Slicer, so I forgot that I had to load the data first… (or choose a directory, which I did before - meaning that I just needed to do this once and put all the slicer data in this trajectory).</p>

---
