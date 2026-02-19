---
topic_id: 36819
title: "Transfering A Module From Linux To Windows"
date: 2024-06-16
url: https://discourse.slicer.org/t/36819
---

# Transfering a module from Linux to Windows

**Topic ID**: 36819
**Date**: 2024-06-16
**URL**: https://discourse.slicer.org/t/transfering-a-module-from-linux-to-windows/36819

---

## Post #1 by @Saman_Fouladi (2024-06-16 08:00 UTC)

<p>Hello. we developed a custom module on Linux using 3d slicer v 4.11.20210226 and I want to transfer and run this module on windows. I installed the same version of 3d Slicer on windows too. When I want to add my module to 3d slicer (on windows) using Developer tools-&gt; Extension wizard path, I faced with this error: The module factory manager reported an error. One or more of the requested module(s) and/or dependencies thereof may not have been loaded.<br>
I could not find any solution for the error.</p>

---

## Post #2 by @lassoan (2024-06-16 13:18 UTC)

<p>Check for more details in the application log (menu: Help / Report a bug).<br>
Further investigation steps depend on these details and if it is a C++ or Python scripted module.</p>

---

## Post #3 by @cpinter (2024-06-17 08:38 UTC)

<p>Is it a Python module or a C++ module? Are there any dependencies you are aware of? Is there anything preventing you from porting it to the latest Slicer? It would be the most future-proof.</p>

---
