---
topic_id: 4161
title: "Profiling 3Dslicer"
date: 2018-09-21
url: https://discourse.slicer.org/t/4161
---

# Profiling 3DSlicer

**Topic ID**: 4161
**Date**: 2018-09-21
**URL**: https://discourse.slicer.org/t/profiling-3dslicer/4161

---

## Post #1 by @Davide_Punzo (2018-09-21 11:34 UTC)

<p>Hi all,</p>
<p>I need to properly profile the CPU and RAM usage of 3DSlicer. I tried few tools on windows like VS, C++ memory validator and mtuner. To these software you can give just the binaries, they will start it, then you play with the software and you get the stats. Unfortunately I didn’t manage to use them because while Slicer.exe is the startup exe file, the one to profile is SlicerApp-real.exe.</p>
<p>Does anyone have experience in profiling Slicer?</p>
<p>Thanks,</p>
<p>Davide.</p>

---

## Post #2 by @pieper (2018-09-21 12:09 UTC)

<p>Hi <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> - I’ve used Instruments on the mac and it’s quite good (it’s part of Xcode).  Also vTune from Intel is nice.  I’ve used it on linux but I believe it works the same on windows  Both can attach to a running process.</p>
<p>Another option that might work is to launch the your windows tool using the slicer launcher (e.g. <code>Slicer.exe --launch tool.exe</code>) and then the environment will be set up for slicer to run.  This is what we do to launch visual studio for debugging on windows.  It works as long as the tool.exe doesn’t have conflicting path requirements that get confused by Slicer’s environment.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @Davide_Punzo (2018-09-21 12:10 UTC)

<p>ok, thanks for the info Steve, I’ll try.</p>

---

## Post #4 by @jdx-john (2018-09-21 16:18 UTC)

<p>Has anyone ever released any information on their profiling efforts or would be prepared to?</p>

---
