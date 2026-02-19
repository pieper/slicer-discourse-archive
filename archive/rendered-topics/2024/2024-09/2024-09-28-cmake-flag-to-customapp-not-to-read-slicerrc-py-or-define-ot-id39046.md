---
topic_id: 39046
title: "Cmake Flag To Customapp Not To Read Slicerrc Py Or Define Ot"
date: 2024-09-28
url: https://discourse.slicer.org/t/39046
---

# CMake Flag to CustomApp not to read `slicerrc.py` or define other file?

**Topic ID**: 39046
**Date**: 2024-09-28
**URL**: https://discourse.slicer.org/t/cmake-flag-to-customapp-not-to-read-slicerrc-py-or-define-other-file/39046

---

## Post #1 by @apparrilla (2024-09-28 17:10 UTC)

<p>Hi everyone!<br>
I´ve some trouble betweeen CustomApp and normal Slicer because first one read slicerrc.py file. Is ther any way to complie CustomApp not to read this file or define a custom rc file to be saved instead?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2024-09-29 03:39 UTC)

<p>Good catch! Custom Slicer applications should be completely independent from standard 3D Slicer applications. By default, a custom application’s startup script name should be determined by the application name, such as <code>.&lt;applicationname&gt;rc.py</code>.</p>
<p>It should be also possible to disable using a startup script for a custom application. It is probably already feasible by setting a custom environment variable in the launcher or by passing <code>--ignore-slicerrc</code> argument to the main application in the launcher, but it would be nice to have a dedicated CMake option or application configuration flag for it.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> scary do you think?</p>

---

## Post #3 by @apparrilla (2024-09-29 06:30 UTC)

<p>Even should be nice to link it to “Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR” flag not to loose portability…</p>

---

## Post #4 by @pieper (2024-09-29 12:19 UTC)

<p>Agreed, the custom app should be completely independent of Slicer in terms of settings, rc file, etc.</p>

---

## Post #5 by @jcfr (2024-09-30 13:44 UTC)

<p>In the past, we have applied a patch like the following. Generalizing as discussed above would indeed be sensible.</p>
<pre data-code-wrap="diff"><code class="lang-diff">diff --git a/Base/QTCore/qSlicerCoreCommandOptions.cxx b/Base/QTCore/qSlicerCoreCommandOptions.cxx
index 41bc603fb53..df309efdb5b 100644
--- a/Base/QTCore/qSlicerCoreCommandOptions.cxx
+++ b/Base/QTCore/qSlicerCoreCommandOptions.cxx
@@ -128,8 +128,9 @@ bool qSlicerCoreCommandOptions::ignoreRest() const
 bool qSlicerCoreCommandOptions::ignoreSlicerRC()const
 {
   Q_D(const qSlicerCoreCommandOptions);
-  return d-&gt;ParsedArgs.value("ignore-slicerrc").toBool() ||
-      this-&gt;isTestingEnabled();
+  //return d-&gt;ParsedArgs.value("ignore-slicerrc").toBool() ||
+  //    this-&gt;isTestingEnabled();
+  return true;
 }
</code></pre>

---

## Post #6 by @cpinter (2024-09-30 13:57 UTC)

<p><a class="mention" href="/u/apparrilla">@apparrilla</a> I have been using conditions like this to differentiate how the slicerrc file is used in each case. This may be useful in the short term.</p>
<pre><code class="lang-auto">if slicer.app.mainApplicationName == 'Slicer':
</code></pre>
<p>If we are redesigning this part, I suggest moving the file to another place, to decrease the number of paths where relevant Slicer related files are stored, and to make it easier to find files for any given application. More concretely, the user folder’s root only contains this one file, but I think we could move it to where the app’s main configuration file is located: <code>AppData/Roaming/[org.name]</code> (on Windows). Then we may want to change its name as well to correspond to the application name.</p>

---

## Post #7 by @apparrilla (2026-02-11 17:44 UTC)

<p>Hi everyone again!</p>
<p>Is there any update for this task? Is there any new flag to add to CMakeList.txt to redirect my CustomSlicer to an internal rc.py saved in anywhere as c:/user/applicationname/?</p>
<p>Thanks on advance!</p>

---
