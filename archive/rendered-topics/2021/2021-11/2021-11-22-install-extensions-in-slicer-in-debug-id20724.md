---
topic_id: 20724
title: "Install Extensions In Slicer In Debug"
date: 2021-11-22
url: https://discourse.slicer.org/t/20724
---

# Install extensions in Slicer in Debug

**Topic ID**: 20724
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/install-extensions-in-slicer-in-debug/20724

---

## Post #1 by @atracsys-sbt (2021-11-22 12:57 UTC)

<p>Hi,<br>
To <a href="https://discourse.slicer.org/t/debug-slicer-crash-from-scripted-module/20657/10">troubleshoot a crash</a>, I’ve compiled Slicer in Debug. However, my scripted module relies on two extensions (IGSIO and IGT) and I now want to launch Slicer in Debug while loading them. From what I have read, this seems possible by adding <code>--launcher-additional-settings</code> and <code>--additional-module-paths</code> to the debug call <code>./Slicer.exe --VisualStudioProject</code>. So far, I can’t manage to see the extensions loaded in Slicer running in Debug.<br>
To better handle the long command, I’ve created my own launcher settings file SlicerWithIGSIOandIGT.ini (see below), but still no luck.<br>
Thanks for helping out !</p>
<p><strong>Edit</strong>: I’ve added line breaks for better readability of the <code>arguments</code> variable, but in the original file there are only spaces between the arguments.</p>
<pre><code class="lang-auto">[General]
launcherNoSplashScreen=false
launcherSplashImagePath=
launcherSplashScreenHideDelayMs=
additionalLauncherHelpShortArgument=
additionalLauncherHelpLongArgument=
additionalLauncherNoSplashArguments=

[Application]
path=D:/S4D/Slicer-build/Slicer.exe
arguments=--launcher-additional-settings
D:/dev-ext/build/SlicerIGT/AdditionalLauncherSettings.ini
D:/dev-ext/build/SlicerIGSIO/inner-build/AdditionalLauncherSettings.ini
--additional-module-paths
D:/dev-ext/build/SlicerIGT/lib/Slicer-4.13/qt-scripted-modules
D:/dev-ext/build/SlicerIGT/lib/Slicer-4.13/qt-loadable-modules/Debug
D:/dev-ext/build/SlicerIGT/lib/Slicer-4.13/cli-modules/Debug
D:/dev-ext/build/SlicerIGSIO/inner-build/lib/Slicer-4.13/qt-scripted-modules
D:/dev-ext/build/SlicerIGSIO/inner-build/lib/Slicer-4.13/qt-loadable-modules/Debug
D:/dev-ext/build/SlicerIGSIO/inner-build/lib/Slicer-4.13/cli-modules/Debug 
name=SlicerWithIGSIOandIGT
revision=
organizationDomain=
organizationName=

[ExtraApplicationToLaunch]


[Environment]
additionalPathVariables=

[LibraryPaths]
size=0

[Paths]
size=0

[EnvironmentVariables]
</code></pre>

---

## Post #2 by @lassoan (2021-11-22 18:32 UTC)

<p>Usually I just add the modules to additional module paths in Slicer (menu: Edit / Application settings / Modules).</p>
<p>If there are additional DLLs then (e.g., OpenIGTLink.dll) then you can add it to a Slicer binary folder (if you add it to a module folder that should work, too, but it will also log an error because that DLL is not a Slicer module) or add their folder to the Slicer main launcher ini file or use an additional launcher ini file.</p>

---
