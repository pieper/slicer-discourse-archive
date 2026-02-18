# Can't launch latest preview (7/17) on Windows 11

**Topic ID**: 43771
**Date**: 2025-07-18
**URL**: https://discourse.slicer.org/t/cant-launch-latest-preview-7-17-on-windows-11/43771

---

## Post #1 by @muratmaga (2025-07-18 18:20 UTC)

<p>I just installed the latest preview on a windows 11 machine, and Slicer fails to launch after the splash screen. There is no failure in the error log either. I tried launching from the command line and same story, no error being printed out to indicate why it is not launch.</p>
<p>The only thing that might be suspicious is that I am on a RDP connection to this machine. But 5.8.1 launches perfectly fine.</p>
<p>Here are the log entries from the failed launch sessions:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Session start time .......: 20250718_111700
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Slicer version ...........: 5.9.0-2025-07-17 (revision 33792 / 5338596) win-amd64 - installed release
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Memory ...................: 32436 MB physical, 37300 MB virtual
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - CPU ......................: GenuineIntel , 28 cores, 28 logical processors
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - DCMTK configuration ......: version 3.6.8, no SSL
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Application path .........: C:/Users/amaga/AppData/Local/slicer.org/Slicer 5.9.0-2025-07-17/bin
[DEBUG][Qt] 18.07.2025 11:17:00 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 18.07.2025 11:17:03 [Python] (C:\Users\amaga\AppData\Local\slicer.org\Slicer 5.9.0-2025-07-17\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 18.07.2025 11:17:03 [Python] (C:\Users\amaga\AppData\Local\slicer.org\Slicer 5.9.0-2025-07-17\lib\Slicer-5.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
</code></pre>

---

## Post #2 by @Sam_Horvath (2025-07-18 18:35 UTC)

<p>Yeah, I think this might be the RDP connection to the machine, launches fine for me on my Win11 machine. Will test through RDP on my end and report back.</p>

---

## Post #3 by @Sam_Horvath (2025-07-18 18:43 UTC)

<p>So, I was able to successfully launch the 7/17 installer while connected to my machine though RDP.  Logs look identical to yours.</p>

---

## Post #4 by @muratmaga (2025-07-18 18:44 UTC)

<p>Installer worked for me without any problems on RDP, what about launching the application? Any other ideas how to generate diagnostics to understand what’s blocking it?</p>

---

## Post #5 by @Sam_Horvath (2025-07-18 18:49 UTC)

<p>Sorry, i mistyped.  I was able to launch the actual application fine as well through RDP.</p>

---

## Post #6 by @muratmaga (2025-07-18 18:50 UTC)

<p>I managed to login into the system directly. It went a little further this time, I briefly saw “Setting up UI” (or somethign along that line) as the final step in the splash screen, and then it failed again.</p>
<p>So not RDP related on my end.</p>

---

## Post #7 by @jcfr (2025-07-18 23:38 UTC)

<p>This is most likely related to a regression that should be fixed following integration of <a href="https://github.com/Slicer/Slicer/pull/8589">PR-8589</a> (<code>BUG: Fix crashes caused by range-based loops over temporary Qt containers</code>)</p>

---
