---
topic_id: 32978
title: "Slicer Fresh Build Crash Start But Executes With Sudo Permis"
date: 2023-11-23
url: https://discourse.slicer.org/t/32978
---

# Slicer fresh build crash start, but executes with sudo permissions

**Topic ID**: 32978
**Date**: 2023-11-23
**URL**: https://discourse.slicer.org/t/slicer-fresh-build-crash-start-but-executes-with-sudo-permissions/32978

---

## Post #1 by @acsenrafilho (2023-11-23 12:26 UTC)

<p>Hi Slicers!</p>
<p>I am quite embarrassed to ask this, but I have tried to find this topic on the forum and rebuilding Slicer several times with slightly different options. However, it still continues to happen.</p>
<p>The problem is that the Slicer build from the source (Linux system) crashes when starts, but when I call the execution using sudo permission ("sudo ./Slicer) it works normally.  I followed the build instructions on the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#" rel="noopener nofollow ugc">Slicer documentation</a></p>
<p>I copied the terminal output to present my system and Slicer configuration details. The command called was: ./Slicer --launcher-verbose --application-information</p>
<h2><a name="p-103672-terminal-output-1" class="anchor" href="#p-103672-terminal-output-1" aria-label="Heading link"></a>Terminal output</h2>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build$ ./Slicer --launcher-verbose --application-information 
info: AdditionalSettingsFilePath []
info: LauncherSplashImagePath [/home/antonio/Documents/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/./SlicerApp-real]
info: ApplicationToLaunchArguments []
info: AdditionalSettingsFilePath []
info: LauncherDir [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build]
info: LauncherName [Slicer]
info: OrganizationDomain [slicer.org]
info: OrganizationName [slicer.org]
info: ApplicationName [Slicer]
info: ApplicationRevision [31938]
info: SettingsFileName [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/./SlicerLauncherSettings.ini]
info: SettingsDir [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build]
info: UserAdditionalSettingsDir [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org]
info: UserAdditionalSettingsFileName [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini]
info: UserAdditionalSettingsFileBaseName []
info: AdditionalSettingsDir []
info: AdditionalSettingsExcludeGroups []
info: LauncherNoSplashScreen [0]
info: AdditionalLauncherHelpShortArgument [-h]
info: AdditionalLauncherHelpLongArgument [--help]
info: AdditionalLauncherNoSplashArguments [--no-splash,--help,--version,--home,--program-path,--no-main-window,--settings-path,--temporary-path]
info: DetachApplicationToLaunch [0]
info: LoadEnvironment [-1]
info: LauncherSplashImagePath [/home/antonio/Documents/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/./SlicerApp-real]
info: ApplicationToLaunchArguments []
info: &lt;APPLAUNCHER_DIR&gt; -&gt; [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build]
info: &lt;APPLAUNCHER_NAME&gt; -&gt; [Slicer]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (RegularSettings) -&gt; [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
info: &lt;PATHSEP&gt; -&gt; [:]
info: Setting env. variable [QTWEBENGINE_DISABLE_SANDBOX]:1
info: Setting env. variable [SLICER_HOME]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build
info: Setting env. variable [PIP_REQUIRE_VIRTUALENV]:0
info: Setting env. variable [ITK_AUTOLOAD_PATH]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/ITKFactories/.
info: Setting env. variable [PYTHONNOUSERSITE]:1
info: Setting env. variable [PYTHONHOME]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install
info: Setting env. variable [SSL_CERT_FILE]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/share/Slicer-5.4/Slicer.crt
info: Setting env. variable [LibraryPaths]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/cli-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/OpenSSL:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/VTK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/teem-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/DCMTK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/ITK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/CTK-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/QtTesting-build/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/PythonQt-build/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/LibArchive-install/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/SimpleITK-build/SimpleITK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/site-packages/numpy/core:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/site-packages/numpy/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/JsonCpp-build/src/lib_json/.
info: Setting env. variable [LD_LIBRARY_PATH]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/cli-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/OpenSSL:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/VTK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/teem-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/DCMTK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/ITK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/CTK-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/QtTesting-build/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/PythonQt-build/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/LibArchive-install/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/SimpleITK-build/SimpleITK-build/lib/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/site-packages/numpy/core:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/site-packages/numpy/lib:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/JsonCpp-build/src/lib_json/.
info: Setting env. variable [PATH]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/cli-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/bin:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/teem-build/bin/.
info: Setting env. variable [QT_PLUGIN_PATH]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/CTK-build/bin:/usr/lib/plugins
info: Setting env. variable [PYTHONPATH]:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/.:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/lib-dynload:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/site-packages:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/VTK-build/lib/python3.9/site-packages:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/CTK-build/bin/Python:/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/CTK-build/CTK-build/bin/.
info: Starting [/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/./SlicerApp-real]
info: argument [--application-information]
info: launcher-timeout (ms) [-1000]
info: DisableSplash [0]
Session start time .......: 2023-11-23 09:00:21
Slicer version ...........: 5.4.0-2023-08-19 (revision 31938 / 311cb26) linux-amd64 - not installed release
Operating system .........: Linux / 5.15.0-88-generic / #98-Ubuntu SMP Mon Oct 2 15:18:56 UTC 2023 / UTF-8 - 64-bit
Memory ...................: 15778 MB physical, 2047 MB virtual
CPU ......................: GenuineIntel 12th Gen Intel(R) Core(TM) i7-12700H, 14 cores, 20 logical processors
VTK configuration ........: OpenGL2 rendering, Sequential threading
Qt configuration .........: version 5.15.3, with SSL, requested OpenGL 3.2 (core profile)
Internationalization .....: disabled, language=
Developer mode ...........: disabled
Application path .........: /home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin
Additional module paths ..: (none)

antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build$ cmake --version
cmake version 3.27.8

CMake suite maintained and supported by Kitware (kitware.com/cmake).
</code></pre>
<p>I am sorry for the newbie problem, probably I missed something simple in the middle of the configuration.<br>
Any help would be very nice.</p>

---

## Post #2 by @lassoan (2023-11-23 12:43 UTC)

<p>The crash is probably in <code>SlicerApp-real</code> due to trying to access some resources (temporary folder?).</p>
<p>Can you get a stack trace of the crash? That would tell what is the resource that the application cannot access and we could make the error detection and reporting more robust and helpful.</p>

---

## Post #3 by @acsenrafilho (2023-11-23 20:08 UTC)

<p>Hi lassoan,</p>
<p>Can you help me to set up this stack trace execution? I did know how to do it.</p>
<p>I am trying to get more information about it, but any instruction will be very helpful.</p>

---

## Post #4 by @acsenrafilho (2023-11-23 20:17 UTC)

<p>lassoan,</p>
<p>I get a tip on another post in the Slicer forum (<a href="https://discourse.slicer.org/t/cant-start-slicer-on-linux-on-one-machine/8175/2">link</a>) and I copied the final part of the execution:</p>
<pre><code class="lang-auto">access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = -1 EACCES (Permission denied)
access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = -1 EACCES (Permission denied)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3ce0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c80) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3ce0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c80) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3ce0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c80) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3ce0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c80) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3ce0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c80) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3cc0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c60) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3cc0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c60) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3cc0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c60) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3cc0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c60) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3cc0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c40) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3be0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c40) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3be0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c40) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3be0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c40) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3be0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c40) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3be0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c10) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3bb0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c10) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3bb0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c10) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3bb0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c10) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3bb0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3c10) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3bb0) = -1 ENOENT (No such file or directory)
access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = -1 EACCES (Permission denied)
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/code.py", {st_mode=S_IFREG|0644, st_size=10622, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/code.py", {st_mode=S_IFREG|0644, st_size=10622, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/code.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=9978, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d2e90)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=9978, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a~)\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 9979) = 9978
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/codeop.py", {st_mode=S_IFREG|0644, st_size=6326, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/codeop.py", {st_mode=S_IFREG|0644, st_size=6326, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/codeop.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=6520, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d2020)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=6520, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\266\30\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 6521) = 6520
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pydoc.py", {st_mode=S_IFREG|0644, st_size=109545, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pydoc.py", {st_mode=S_IFREG|0644, st_size=109545, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/pydoc.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=85378, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d2df0)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=85378, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\351\253\1\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 85379) = 85378
read(26, "", 1)                         = 0
close(26)                               = 0
mmap(NULL, 262144, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f4ed9388000
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pkgutil.py", {st_mode=S_IFREG|0644, st_size=24276, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pkgutil.py", {st_mode=S_IFREG|0644, st_size=24276, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/pkgutil.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=18628, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d1f80)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=18628, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\324^\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 18629) = 18628
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/sysconfig.py", {st_mode=S_IFREG|0644, st_size=24914, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/sysconfig.py", {st_mode=S_IFREG|0644, st_size=24914, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/sysconfig.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16129, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d1f80)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16129, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340aRa\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 16130) = 16129
read(26, "", 1)                         = 0
close(26)                               = 0
getcwd("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build", 1024) = 67
newfstatat(AT_FDCWD, "/home", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio", {st_mode=S_IFDIR|0750, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/Modules/Setup", 0x7ffc0c5d19c0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/Modules/Setup.local", 0x7ffc0c5d19c0, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/_sysconfigdata__linux2_.py", {st_mode=S_IFREG|0644, st_size=18320, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/_sysconfigdata__linux2_.py", {st_mode=S_IFREG|0644, st_size=18320, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/_sysconfigdata__linux2_.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16219, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffc0c5d1050)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16219, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\307\20]e\220G\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 16220) = 16219
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio", {st_mode=S_IFDIR|0750, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/config-3.9", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
pipe2([26, 27], 0)                      = 0
lseek(1, 0, SEEK_CUR)                   = 0
dup(1)                                  = 28
dup2(27, 1)                             = 1
close(27)                               = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7f4ed8b87000
mprotect(0x7f4ed8b88000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7f4ed9387910, parent_tid=0x7f4ed9387910, exit_signal=0, stack=0x7f4ed8b87000, stack_size=0x7fd1c0, tls=0x7f4ed9387640} =&gt; {parent_tid=[1063867]}, 88) = 1063867
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
pipe2([27, 29], 0)                      = 0
lseek(2, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
dup(2)                                  = 30
dup2(29, 2)                             = 2
close(29)                               = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7f4ed8386000
mprotect(0x7f4ed8387000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7f4ed8b86910, parent_tid=0x7f4ed8b86910, exit_signal=0, stack=0x7f4ed8386000, stack_size=0x7fd1c0, tls=0x7f4ed8b86640} =&gt; {parent_tid=[1063868]}, 88) = 1063868
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
futex(0x560153f6a738, FUTEX_WAKE_PRIVATE, 1) = 1
readlink("/tmp", 0x7ffc0c5d37e0, 1023)  = -1 EINVAL (Invalid argument)
statx(AT_FDCWD, "/tmp/Slicer-antonio", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFDIR|0775, stx_size=4096, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
unlink("/tmp/Slicer-antonio/Slicer_31938_20231123_090021_359.log") = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/CMakeCache.txt", F_OK) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 32
newfstatat(32, "", {st_mode=S_IFREG|0444, st_size=0, ...}, AT_EMPTY_PATH) = 0
read(32, "processor\t: 0\nvendor_id\t: Genuin"..., 1024) = 1024
read(32, "ock_detect avx_vnni dtherm ida a"..., 1024) = 1024
read(32, "cx8 apic sep mtrr pge mca cmov p"..., 1024) = 1024
read(32, "apic_reg vid ple shadow_vmcs ept"..., 1024) = 1024
read(32, "c rdrand lahf_lm abm 3dnowprefet"..., 1024) = 1024
read(32, "i7-12700H\nstepping\t: 3\nmicrocode"..., 1024) = 1024
read(32, "e waitpkg gfni vaes vpclmulqdq r"..., 1024) = 1024
read(32, "gb rdtscp lm constant_tsc art ar"..., 1024) = 1024
read(32, " spec_store_bypass swapgs eibrs_"..., 1024) = 1024
read(32, "lexpriority ept vpid ept_ad fsgs"..., 1024) = 1024
read(32, "ings\t: 20\ncore id\t\t: 12\ncpu core"..., 1024) = 1024
read(32, "ch_capabilities\nvmx flags\t: vnmi"..., 1024) = 1024
read(32, "mperf tsc_known_freq pni pclmulq"..., 1024) = 1024
read(32, "ress sizes\t: 39 bits physical, 4"..., 1024) = 1024
read(32, "lflushopt clwb intel_pt sha_ni x"..., 1024) = 1024
read(32, " yes\ncpuid level\t: 32\nwp\t\t: yes\n"..., 1024) = 1024
read(32, "expriority apicv tsc_offset vtpr"..., 1024) = 1024
read(32, " pdcm sse4_1 sse4_2 x2apic movbe"..., 1024) = 1024
read(32, "ineIntel\ncpu family\t: 6\nmodel\t\t:"..., 1024) = 1024
read(32, "ida arat pln pts hwp hwp_notify "..., 1024) = 1024
read(32, "ca cmov pat pse36 clflush dts ac"..., 1024) = 1024
read(32, "_vmcs ept_mode_based_exec tsc_sc"..., 1024) = 1024
read(32, "m 3dnowprefetch cpuid_fault epb "..., 1024) = 1024
read(32, "\t: 3\nmicrocode\t: 0x430\ncpu MHz\t\t"..., 1024) = 1024
read(32, "vaes vpclmulqdq rdpid movdiri mo"..., 1024) = 1024
read(32, "constant_tsc art arch_perfmon pe"..., 1024) = 1024
read(32, "ypass swapgs eibrs_pbrsb\nbogomip"..., 1024) = 1024
read(32, " ept vpid ept_ad fsgsbase tsc_ad"..., 1024) = 1024
read(32, "core id\t\t: 29\ncpu cores\t: 14\napi"..., 1024) = 1024
read(32, "ities\nvmx flags\t: vnmi preemptio"..., 1024) = 1024
read(32, "_known_freq pni pclmulqdq dtes64"..., 1024) = 1024
read(32, "s\t: 39 bits physical, 48 bits vi"..., 1024) = 1024
read(32, "t clwb intel_pt sha_ni xsaveopt "..., 1024) = 708
read(32, "", 1024)                      = 0
close(32)                               = 0
brk(0x560154484000)                     = 0x560154484000
brk(0x5601544ad000)                     = 0x5601544ad000
brk(0x5601544d5000)                     = 0x5601544d5000
brk(0x5601544f6000)                     = 0x5601544f6000
brk(0x560154517000)                     = 0x560154517000
brk(0x560154538000)                     = 0x560154538000
brk(0x560154560000)                     = 0x560154560000
brk(0x560154581000)                     = 0x560154581000
brk(0x5601545a2000)                     = 0x5601545a2000
brk(0x5601545c3000)                     = 0x5601545c3000
brk(0x5601545eb000)                     = 0x5601545eb000
brk(0x56015460c000)                     = 0x56015460c000
brk(0x56015462d000)                     = 0x56015462d000
brk(0x56015464e000)                     = 0x56015464e000
brk(0x560154676000)                     = 0x560154676000
brk(0x560154697000)                     = 0x560154697000
brk(0x5601546b8000)                     = 0x5601546b8000
brk(0x5601546d9000)                     = 0x5601546d9000
brk(0x560154701000)                     = 0x560154701000
brk(0x560154722000)                     = 0x560154722000
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
openat(AT_FDCWD, "/proc/meminfo", O_RDONLY) = 32
newfstatat(32, "", {st_mode=S_IFREG|0444, st_size=0, ...}, AT_EMPTY_PATH) = 0
read(32, "MemTotal:       16156924 kB\nMemF"..., 1024) = 1024
read(32, "pted:     0 kB\nAnonHugePages:   "..., 1024) = 395
read(32, "", 1024)                      = 0
close(32)                               = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = 32
close(32)                               = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini.lock", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0666) = 32
flock(32, LOCK_EX|LOCK_NB)              = 0
openat(AT_FDCWD, "/proc/sys/kernel/random/boot_id", O_RDONLY|O_CLOEXEC) = 33
read(33, "738c301f-54a0-4d05-bc07-07f88f34"..., 36) = 36
close(33)                               = 0
openat(AT_FDCWD, "/var/lib/dbus/machine-id", O_RDONLY|O_CLOEXEC) = 33
read(33, "10b971ac1a304176906b1f6a23827476", 32) = 32
close(33)                               = 0
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
getpid()                                = 1063841
readlink("/proc/1063841/exe", "/home/antonio/Documents/Slicer-S"..., 256) = 85
getpid()                                = 1063841
write(32, "1063841\nSlicerApp-real\nLOAMRI-Le"..., 107) = 107
fdatasync(32)                           = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", W_OK) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT|AT_SYMLINK_NOFOLLOW, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org", O_RDWR|O_CLOEXEC|O_TMPFILE, 0600) = 33
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", R_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", W_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", X_OK) = -1 EACCES (Permission denied)
fchmod(33, 0664)                        = 0
statx(33, "", AT_STATX_SYNC_AS_STAT|AT_EMPTY_PATH, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=0, ...}) = 0
write(33, "[General]\nDatabaseDirectory_0.7."..., 16157) = 16157
write(33, "RecentFiles\\8\\file=@Variant(\\0\\0"..., 4380) = 4380
lseek(33, 0, SEEK_SET)                  = 0
fdatasync(33)                           = 0
linkat(AT_FDCWD, "/proc/self/fd/33", AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_SYMLINK_FOLLOW) = -1 EEXIST (File exists)
linkat(AT_FDCWD, "/proc/self/fd/33", AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini.hShYsc", AT_SYMLINK_FOLLOW) = 0
close(33)                               = 0
rename("/home/antonio/.config/slicer.org/Slicer.ini.hShYsc", "/home/antonio/.config/slicer.org/Slicer.ini") = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=20537, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
close(32)                               = 0
unlink("/home/antonio/.config/slicer.org/Slicer.ini.lock") = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e00) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e00) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e00) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e00) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e60) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffc0c5d3e00) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = -1 EACCES (Permission denied)
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x7f4f6ecad6b8} ---
+++ killed by SIGSEGV (core dumped) +++
Segmentation fault (core dumped)
</code></pre>
<p>I hope this could help. Please let me know if there is another way to find the problem.</p>
<p>Thank you!</p>

---

## Post #5 by @lassoan (2023-11-23 20:35 UTC)

<p>It is odd that Slicer cannot access this file: <code>/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini</code></p>
<p>Does the file exist?<br>
Can the current user access it?<br>
Does it help if you change permissions so that the current user can access it (or erase the file so that the current user creates it when launching Slicer)?</p>

---

## Post #6 by @acsenrafilho (2023-11-23 20:47 UTC)

<p>Interesting… the file indeed exist, with the following info:</p>
<pre><code class="lang-auto">[Extensions]
FrontendServerUrl=https://extensions.slicer.org
InstallPath=slicer.org/Extensions-31938
LastServerAPI=Girder_v1
ManagerEnabled=true
ServerUrl=https://slicer-packages.kitware.com

[Modules]
AdditionalPaths=@Invalid()
IgnoreModules=@Invalid()
</code></pre>
<p>However, I do not know how this specific file is placed to <code>root</code> access <img src="https://emoji.discourse-cdn.com/twitter/hushed.png?v=12" title=":hushed:" class="emoji" alt=":hushed:" loading="lazy" width="20" height="20"></p>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org$ ls -la
total 16
drwxrwxr-x  3 antonio antonio 4096 Nov 23 08:59 .
drwxrwxr-x 19 antonio antonio 4096 Nov 23 17:13 ..
drwxrwxr-x  2 antonio antonio 4096 Nov 21 18:02 Extensions-31938
-rw-rw-r--  1 root    root     254 Nov 23 08:59 Slicer-31938.ini
</code></pre>
<p>I have changed the file access to my user (<code>antonio</code>, using the command <code>sudo chown antonio:antonio Slicer-31938.ini</code>). However the execution still fails…</p>
<p>The new trace is:</p>
<pre><code class="lang-auto">rename("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini.euTTKB", "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini") = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
close(26)                               = 0
unlink("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini.lock") = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Extensions-31938", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFDIR|0775, stx_size=4096, ...}) = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5650) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55f0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5650) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55f0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5650) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55f0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5650) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55f0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5650) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55f0) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Extensions-31938", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 26
newfstatat(26, "", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_EMPTY_PATH) = 0
getdents64(26, 0x55ff1ce847a0 /* 2 entries */, 32768) = 48
getdents64(26, 0x55ff1ce847a0 /* 0 entries */, 32768) = 0
close(26)                               = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5660) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5600) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5660) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5600) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5660) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5600) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5660) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5600) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5660) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5600) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5640) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55e0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5640) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55e0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5640) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55e0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5640) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55e0) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5640) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55c0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5560) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55c0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5560) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55c0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5560) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55c0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5560) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c55c0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5560) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5590) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5530) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5590) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5530) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5590) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5530) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5590) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5530) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5590) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5530) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/code.py", {st_mode=S_IFREG|0644, st_size=10622, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/code.py", {st_mode=S_IFREG|0644, st_size=10622, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/code.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=9978, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c4810)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=9978, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a~)\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 9979) = 9978
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/codeop.py", {st_mode=S_IFREG|0644, st_size=6326, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/codeop.py", {st_mode=S_IFREG|0644, st_size=6326, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/codeop.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=6520, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c39a0)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=6520, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\266\30\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 6521) = 6520
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pydoc.py", {st_mode=S_IFREG|0644, st_size=109545, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pydoc.py", {st_mode=S_IFREG|0644, st_size=109545, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/pydoc.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=85378, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c4770)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=85378, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\351\253\1\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 85379) = 85378
read(26, "", 1)                         = 0
close(26)                               = 0
mmap(NULL, 262144, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa3e7dd3000
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pkgutil.py", {st_mode=S_IFREG|0644, st_size=24276, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/pkgutil.py", {st_mode=S_IFREG|0644, st_size=24276, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/pkgutil.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=18628, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c3900)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=18628, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340a\324^\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 18629) = 18628
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/sysconfig.py", {st_mode=S_IFREG|0644, st_size=24914, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/sysconfig.py", {st_mode=S_IFREG|0644, st_size=24914, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/sysconfig.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16129, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c3900)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16129, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\323\227\340aRa\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 16130) = 16129
read(26, "", 1)                         = 0
close(26)                               = 0
getcwd("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build", 1024) = 67
newfstatat(AT_FDCWD, "/home", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio", {st_mode=S_IFDIR|0750, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/Modules/Setup", 0x7ffe779c3340, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/Modules/Setup.local", 0x7ffe779c3340, 0) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python/slicer", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/bin/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules", {st_mode=S_IFDIR|0775, st_size=16384, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-loadable-modules/Python", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/lib/Slicer-5.4/qt-scripted-modules", {st_mode=S_IFDIR|0775, st_size=4096, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/_sysconfigdata__linux2_.py", {st_mode=S_IFREG|0644, st_size=18320, ...}, 0) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/_sysconfigdata__linux2_.py", {st_mode=S_IFREG|0644, st_size=18320, ...}, 0) = 0
openat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/__pycache__/_sysconfigdata__linux2_.cpython-39.pyc", O_RDONLY|O_CLOEXEC) = 26
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16219, ...}, AT_EMPTY_PATH) = 0
ioctl(26, TCGETS, 0x7ffe779c29d0)       = -1 ENOTTY (Inappropriate ioctl for device)
lseek(26, 0, SEEK_CUR)                  = 0
lseek(26, 0, SEEK_CUR)                  = 0
newfstatat(26, "", {st_mode=S_IFREG|0644, st_size=16219, ...}, AT_EMPTY_PATH) = 0
read(26, "a\r\r\n\0\0\0\0\307\20]e\220G\0\0\343\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 16220) = 16219
read(26, "", 1)                         = 0
close(26)                               = 0
newfstatat(AT_FDCWD, "/home", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio", {st_mode=S_IFDIR|0750, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents", {st_mode=S_IFDIR|0755, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9", {st_mode=S_IFDIR|0775, st_size=12288, ...}, AT_SYMLINK_NOFOLLOW) = 0
newfstatat(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/python-install/lib/python3.9/config-3.9", {st_mode=S_IFDIR|0775, st_size=4096, ...}, AT_SYMLINK_NOFOLLOW) = 0
pipe2([26, 27], 0)                      = 0
lseek(1, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
dup(1)                                  = 28
dup2(27, 1)                             = 1
close(27)                               = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7fa3e75d2000
mprotect(0x7fa3e75d3000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7fa3e7dd2910, parent_tid=0x7fa3e7dd2910, exit_signal=0, stack=0x7fa3e75d2000, stack_size=0x7fd1c0, tls=0x7fa3e7dd2640} =&gt; {parent_tid=[1377243]}, 88) = 1377243
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
pipe2([27, 29], 0)                      = 0
lseek(2, 0, SEEK_CUR)                   = -1 ESPIPE (Illegal seek)
dup(2)                                  = 30
dup2(29, 2)                             = 2
close(29)                               = 0
mmap(NULL, 8392704, PROT_NONE, MAP_PRIVATE|MAP_ANONYMOUS|MAP_STACK, -1, 0) = 0x7fa3e6dd1000
mprotect(0x7fa3e6dd2000, 8388608, PROT_READ|PROT_WRITE) = 0
rt_sigprocmask(SIG_BLOCK, ~[], [], 8)   = 0
clone3({flags=CLONE_VM|CLONE_FS|CLONE_FILES|CLONE_SIGHAND|CLONE_THREAD|CLONE_SYSVSEM|CLONE_SETTLS|CLONE_PARENT_SETTID|CLONE_CHILD_CLEARTID, child_tid=0x7fa3e75d1910, parent_tid=0x7fa3e75d1910, exit_signal=0, stack=0x7fa3e6dd1000, stack_size=0x7fd1c0, tls=0x7fa3e75d1640} =&gt; {parent_tid=[1377244]}, 88) = 1377244
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
readlink("/tmp", 0x7ffe779c5160, 1023)  = -1 EINVAL (Invalid argument)
statx(AT_FDCWD, "/tmp/Slicer-antonio", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFDIR|0775, stx_size=4096, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
unlink("/tmp/Slicer-antonio/Slicer_31938_20231123_102003_826.log") = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
access("/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/CMakeCache.txt", F_OK) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
openat(AT_FDCWD, "/proc/cpuinfo", O_RDONLY) = 32
newfstatat(32, "", {st_mode=S_IFREG|0444, st_size=0, ...}, AT_EMPTY_PATH) = 0
read(32, "processor\t: 0\nvendor_id\t: Genuin"..., 1024) = 1024
read(32, "ock_detect avx_vnni dtherm ida a"..., 1024) = 1024
read(32, "cx8 apic sep mtrr pge mca cmov p"..., 1024) = 1024
read(32, "apic_reg vid ple shadow_vmcs ept"..., 1024) = 1024
read(32, "c rdrand lahf_lm abm 3dnowprefet"..., 1024) = 1024
read(32, "i7-12700H\nstepping\t: 3\nmicrocode"..., 1024) = 1024
read(32, "e waitpkg gfni vaes vpclmulqdq r"..., 1024) = 1024
read(32, "gb rdtscp lm constant_tsc art ar"..., 1024) = 1024
read(32, " spec_store_bypass swapgs eibrs_"..., 1024) = 1024
read(32, "lexpriority ept vpid ept_ad fsgs"..., 1024) = 1024
read(32, "ings\t: 20\ncore id\t\t: 12\ncpu core"..., 1024) = 1024
read(32, "ch_capabilities\nvmx flags\t: vnmi"..., 1024) = 1024
read(32, "mperf tsc_known_freq pni pclmulq"..., 1024) = 1024
read(32, "ress sizes\t: 39 bits physical, 4"..., 1024) = 1024
read(32, "lflushopt clwb intel_pt sha_ni x"..., 1024) = 1024
read(32, " yes\ncpuid level\t: 32\nwp\t\t: yes\n"..., 1024) = 1024
read(32, "expriority apicv tsc_offset vtpr"..., 1024) = 1024
read(32, " pdcm sse4_1 sse4_2 x2apic movbe"..., 1024) = 1024
read(32, "ineIntel\ncpu family\t: 6\nmodel\t\t:"..., 1024) = 1024
read(32, "ida arat pln pts hwp hwp_notify "..., 1024) = 1024
read(32, "ca cmov pat pse36 clflush dts ac"..., 1024) = 1024
read(32, "_vmcs ept_mode_based_exec tsc_sc"..., 1024) = 1024
read(32, "m 3dnowprefetch cpuid_fault epb "..., 1024) = 1024
read(32, "\t: 3\nmicrocode\t: 0x430\ncpu MHz\t\t"..., 1024) = 1024
read(32, "vaes vpclmulqdq rdpid movdiri mo"..., 1024) = 1024
read(32, "constant_tsc art arch_perfmon pe"..., 1024) = 1024
read(32, "ypass swapgs eibrs_pbrsb\nbogomip"..., 1024) = 1024
read(32, " ept vpid ept_ad fsgsbase tsc_ad"..., 1024) = 1024
read(32, "core id\t\t: 29\ncpu cores\t: 14\napi"..., 1024) = 1024
read(32, "ities\nvmx flags\t: vnmi preemptio"..., 1024) = 1024
read(32, "_known_freq pni pclmulqdq dtes64"..., 1024) = 1024
read(32, "s\t: 39 bits physical, 48 bits vi"..., 1024) = 1024
read(32, "t clwb intel_pt sha_ni xsaveopt "..., 1024) = 708
read(32, "", 1024)                      = 0
close(32)                               = 0
brk(0x55ff1dd1a000)                     = 0x55ff1dd1a000
brk(0x55ff1dd3b000)                     = 0x55ff1dd3b000
brk(0x55ff1dd64000)                     = 0x55ff1dd64000
brk(0x55ff1dd8c000)                     = 0x55ff1dd8c000
brk(0x55ff1ddad000)                     = 0x55ff1ddad000
brk(0x55ff1ddce000)                     = 0x55ff1ddce000
brk(0x55ff1ddef000)                     = 0x55ff1ddef000
brk(0x55ff1de17000)                     = 0x55ff1de17000
brk(0x55ff1de38000)                     = 0x55ff1de38000
brk(0x55ff1de59000)                     = 0x55ff1de59000
brk(0x55ff1de7a000)                     = 0x55ff1de7a000
brk(0x55ff1dea2000)                     = 0x55ff1dea2000
brk(0x55ff1dec3000)                     = 0x55ff1dec3000
brk(0x55ff1dee4000)                     = 0x55ff1dee4000
brk(0x55ff1df05000)                     = 0x55ff1df05000
brk(0x55ff1df2d000)                     = 0x55ff1df2d000
brk(0x55ff1df4e000)                     = 0x55ff1df4e000
brk(0x55ff1df6f000)                     = 0x55ff1df6f000
brk(0x55ff1df90000)                     = 0x55ff1df90000
brk(0x55ff1dfb8000)                     = 0x55ff1dfb8000
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
openat(AT_FDCWD, "/proc/meminfo", O_RDONLY) = 32
newfstatat(32, "", {st_mode=S_IFREG|0444, st_size=0, ...}, AT_EMPTY_PATH) = 0
read(32, "MemTotal:       16156924 kB\nMemF"..., 1024) = 1024
read(32, "pted:     0 kB\nAnonHugePages:   "..., 1024) = 395
read(32, "", 1024)                      = 0
close(32)                               = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", O_RDWR|O_CREAT|O_CLOEXEC, 0666) = 32
close(32)                               = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini.lock", O_RDWR|O_CREAT|O_EXCL|O_CLOEXEC, 0666) = 32
flock(32, LOCK_EX|LOCK_NB)              = 0
openat(AT_FDCWD, "/proc/sys/kernel/random/boot_id", O_RDONLY|O_CLOEXEC) = 33
read(33, "738c301f-54a0-4d05-bc07-07f88f34"..., 36) = 36
close(33)                               = 0
openat(AT_FDCWD, "/var/lib/dbus/machine-id", O_RDONLY|O_CLOEXEC) = 33
read(33, "10b971ac1a304176906b1f6a23827476", 32) = 32
close(33)                               = 0
uname({sysname="Linux", nodename="LOAMRI-Legion", ...}) = 0
getpid()                                = 1377215
readlink("/proc/1377215/exe", "/home/antonio/Documents/Slicer-S"..., 256) = 85
getpid()                                = 1377215
write(32, "1377215\nSlicerApp-real\nLOAMRI-Le"..., 107) = 107
fdatasync(32)                           = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", F_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", W_OK) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT|AT_SYMLINK_NOFOLLOW, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
openat(AT_FDCWD, "/home/antonio/.config/slicer.org", O_RDWR|O_CLOEXEC|O_TMPFILE, 0600) = 33
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", R_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", W_OK) = 0
access("/home/antonio/.config/slicer.org/Slicer.ini", X_OK) = -1 EACCES (Permission denied)
fchmod(33, 0664)                        = 0
statx(33, "", AT_STATX_SYNC_AS_STAT|AT_EMPTY_PATH, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=0, ...}) = 0
write(33, "[General]\nDatabaseDirectory_0.7."..., 15504) = 15504
write(33, "RecentFiles\\7\\file=@Variant(\\0\\0"..., 5743) = 5743
lseek(33, 0, SEEK_SET)                  = 0
fdatasync(33)                           = 0
linkat(AT_FDCWD, "/proc/self/fd/33", AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_SYMLINK_FOLLOW) = -1 EEXIST (File exists)
linkat(AT_FDCWD, "/proc/self/fd/33", AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini.iHMkiG", AT_SYMLINK_FOLLOW) = 0
close(33)                               = 0
rename("/home/antonio/.config/slicer.org/Slicer.ini.iHMkiG", "/home/antonio/.config/slicer.org/Slicer.ini") = 0
statx(AT_FDCWD, "/home/antonio/.config/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=21247, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
close(32)                               = 0
unlink("/home/antonio/.config/slicer.org/Slicer.ini.lock") = 0
access("/home/antonio/.config/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c57e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/home/antonio/.config/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5780) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c57e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5780) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org/Slicer.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c57e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org/Slicer.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5780) = -1 ENOENT (No such file or directory)
access("/etc/xdg/xdg-cinnamon/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c57e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/xdg-cinnamon/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5780) = -1 ENOENT (No such file or directory)
access("/etc/xdg/slicer.org.ini", F_OK) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c57e0) = -1 ENOENT (No such file or directory)
statx(AT_FDCWD, "/etc/xdg/slicer.org.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, 0x7ffe779c5780) = -1 ENOENT (No such file or directory)
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
statx(AT_FDCWD, "/home/antonio/Documents/Slicer-SuperBuild-Debug-5.4.0/Slicer-build/slicer.org/Slicer-31938.ini", AT_STATX_SYNC_AS_STAT, STATX_ALL, {stx_mask=STATX_ALL|STATX_MNT_ID, stx_attributes=0, stx_mode=S_IFREG|0664, stx_size=254, ...}) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
newfstatat(AT_FDCWD, "/etc/localtime", {st_mode=S_IFREG|0644, st_size=1444, ...}, 0) = 0
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
write(5, "\1\0\0\0\0\0\0\0", 8)         = 8
--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=0x7fa47d6f96b8} ---
+++ killed by SIGSEGV (core dumped) +++
Segmentation fault (core dumped)
</code></pre>
<p>I don’t know if changed something…</p>

---

## Post #7 by @lassoan (2023-11-23 20:52 UTC)

<p>Can you enable the current user to access this file, too?</p>
<pre><code>/home/antonio/.config/slicer.org/Slicer.ini
</code></pre>

---

## Post #8 by @acsenrafilho (2023-11-24 11:35 UTC)

<p>Sure, but I listed all files in <code>.config/slicer.org</code> path and all of them were already to access by me.</p>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/.config/slicer.org$ ls -la
total 296
drwxrwxr-x  2 antonio antonio  4096 Nov 23 18:14 .
drwxr-xr-x 29 antonio antonio  4096 Nov 23 18:14 ..
-rw-rw-r--  1 antonio antonio  2116 Nov 18 13:28 qSlicerAboutDialogTest1.ini
-rw-rw-r--  1 antonio antonio  2549 Nov 18 13:28 qSlicerAnnotationsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2579 Nov 18 13:28 qSlicerAnnotationsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2116 Nov 18 13:28 qSlicerApplicationTest1.ini
-rw-rw-r--  1 antonio antonio  2126 Nov 18 13:29 qSlicerAppMainWindowTest1.ini
-rw-rw-r--  1 antonio antonio  2156 Nov 18 13:28 qSlicerCamerasModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2186 Nov 18 13:28 qSlicerCamerasModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  1939 Nov 18 13:28 qSlicerCLIModuleTest1.ini
-rw-rw-r--  1 antonio antonio  2151 Nov 18 13:28 qSlicerColorsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2181 Nov 18 13:28 qSlicerColorsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  3232 Nov 18 13:28 qSlicerCropVolumeModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  3262 Nov 18 13:28 qSlicerCropVolumeModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2111 Nov 18 13:28 qSlicerDataDialogTest1.ini
-rw-rw-r--  1 antonio antonio  2286 Nov 18 13:28 qSlicerDataModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2316 Nov 18 13:28 qSlicerDataModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2191 Nov 18 13:29 qSlicerDynamicModelerModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2221 Nov 18 13:29 qSlicerDynamicModelerModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2146 Nov 18 13:28 qSlicerErrorReportDialogTest1.ini
-rw-rw-r--  1 antonio antonio  2176 Nov 18 13:28 qSlicerEventBrokerModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2206 Nov 18 13:28 qSlicerEventBrokerModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  3256 Nov 18 13:28 qSlicerMarkupsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  3286 Nov 18 13:28 qSlicerMarkupsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2264 Nov 18 13:28 qSlicerModelsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2294 Nov 18 13:28 qSlicerModelsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2151 Nov 18 13:28 qSlicerModelsModuleWidgetTest1.ini
-rw-rw-r--  1 antonio antonio  2171 Nov 18 13:28 qSlicerModelsModuleWidgetTestScene.ini
-rw-rw-r--  1 antonio antonio  2116 Nov 18 13:28 qSlicerModulePanelTest1.ini
-rw-rw-r--  1 antonio antonio   130 Nov 18 13:28 qSlicerModulePanelTest2.ini
-rw-rw-r--  1 antonio antonio  2141 Nov 18 13:28 qSlicerMouseModeToolBarTest1.ini
-rw-rw-r--  1 antonio antonio  2146 Nov 18 13:28 qSlicerPlotsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2176 Nov 18 13:28 qSlicerPlotsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  1949 Nov 18 13:28 qSlicerPyCLIModuleTest1.ini
-rw-rw-r--  1 antonio antonio  2161 Nov 18 13:28 qSlicerReformatModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2191 Nov 18 13:28 qSlicerReformatModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2238 Nov 18 13:28 qSlicerSaveDataDialogCustomFileWriterTest.ini
-rw-rw-r--  1 antonio antonio  2171 Nov 18 13:28 qSlicerSceneViewsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2201 Nov 18 13:28 qSlicerSceneViewsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2459 Nov 18 13:28 qSlicerSegmentationsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2489 Nov 18 13:28 qSlicerSegmentationsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2166 Nov 18 13:28 qSlicerSequencesModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2196 Nov 18 13:28 qSlicerSequencesModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2461 Nov 18 13:28 qSlicerSubjectHierarchyModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2491 Nov 18 13:28 qSlicerSubjectHierarchyModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2151 Nov 18 13:28 qSlicerTablesModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2181 Nov 18 13:28 qSlicerTablesModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2263 Nov 18 13:28 qSlicerTerminologiesModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2293 Nov 18 13:28 qSlicerTerminologiesModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2146 Nov 18 13:28 qSlicerTextsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2176 Nov 18 13:28 qSlicerTextsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  3232 Nov 18 13:28 qSlicerTransformsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  3262 Nov 18 13:28 qSlicerTransformsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2612 Nov 18 13:28 qSlicerUnitsModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2642 Nov 18 13:28 qSlicerUnitsModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2196 Nov 18 13:28 qSlicerViewControllersModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2226 Nov 18 13:28 qSlicerViewControllersModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2410 Nov 18 13:28 qSlicerVolumeRenderingModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2440 Nov 18 13:28 qSlicerVolumeRenderingModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2410 Nov 18 13:28 qSlicerVolumeRenderingModuleWidgetTest1.ini
-rw-rw-r--  1 antonio antonio  2410 Nov 18 13:28 qSlicerVolumeRenderingModuleWidgetTest2.ini
-rw-rw-r--  1 antonio antonio  2171 Nov 18 13:28 qSlicerVolumesIOOptionsWidgetTest1.ini
-rw-rw-r--  1 antonio antonio  3217 Nov 18 13:28 qSlicerVolumesModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  3247 Nov 18 13:28 qSlicerVolumesModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio  2156 Nov 18 13:28 qSlicerVolumesModuleWidgetTest1.ini
-rw-rw-r--  1 antonio antonio  2156 Nov 18 13:28 qSlicerWelcomeModuleGenericTest.ini
-rw-rw-r--  1 antonio antonio  2186 Nov 18 13:28 qSlicerWelcomeModuleWidgetGenericTest.ini
-rw-rw-r--  1 antonio antonio 20697 Nov 23 18:14 Slicer.ini
-rw-rw-r--  1 antonio antonio   120 Nov 18 13:35 Slicer-tmp.ini
</code></pre>
<p>I made a search in the <code>Slicer-Superbuild</code> folder to look at the files with <code>root</code> access, and there are two of them:</p>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0$ find . -user root
./Slicer-build/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorEffects/__pycache__/__init__.cpython-39.pyc
./VTK-build/lib/python3.9/site-packages/vtkmodules/util/__pycache__/numpy_support.cpython-39.pyc
antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0$ ls -la ./Slicer-build/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorEffects/__pycache__/__init__.cpython-39.pyc
-rw-r--r-- 1 root root 1704 Nov 21 18:02 ./Slicer-build/lib/Slicer-5.4/qt-scripted-modules/SegmentEditorEffects/__pycache__/__init__.cpython-39.pyc
antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0$ ls -la ./VTK-build/lib/python3.9/site-packages/vtkmodules/util/__pycache__/numpy_support.cpython-39.pyc
-rw-r--r-- 1 root root 6592 Nov 21 18:02 ./VTK-build/lib/python3.9/site-packages/vtkmodules/util/__pycache__/numpy_support.cpython-39.pyc
</code></pre>
<p>They should be in this way? I do I need to change it to my user access?<br>
By the way, I am wandering why those changes in root access occur on those files. Is there any clue what did I do in the build process that may change it?</p>
<p>By the way, thank you lassoan for all the attention on this matter. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @pieper (2023-11-24 12:58 UTC)

<p>Maybe when you ran <code>sudo ./Slicer</code> some python files got compiled with root-only access.  Maybe do <code>chown -R antonio:antonio .</code> in your superbuild directory <code>.config</code>.  Also what linux is this?  Do the slicer binary packages run okay on this computer?</p>

---

## Post #10 by @acsenrafilho (2023-11-24 15:31 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> , thanks for the ideas</p>
<p>I’ve executed the <code>chown -R</code> command on <code>Slicer-Superbuild</code> and <code>.config/slicer.org</code> folder. All the files were changed to my user access, however the <code>./Slicer</code> execution still crashes.</p>
<p>Sorry to not given the linux SO details before. I am using a fresh install of Linux Mint 21.2 (which is based on Ubuntu 22.04) (<a href="https://www.linuxmint.com/rel_victoria_cinnamon.php" rel="noopener nofollow ugc">link for Linux Mint release notes</a>):</p>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/Documents/Slicer-SuperBuild-Debug-5.4.0$ uname -a
Linux LOAMRI-Legion 5.15.0-89-generic #99-Ubuntu SMP Mon Oct 30 20:42:41 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
</code></pre>
<p>I also downloaded the binary packages for Slicer v5.4.0 and it executes normally.<br>
I made the same execution using the command <code>./Slicer --launch-verbose --application-information</code> just to see if this could help in anything.</p>
<pre><code class="lang-auto">antonio@LOAMRI-Legion:~/Documents/Slicer-5.4.0-linux-amd64$ ./Slicer --launcher-verbose --application-information
info: AdditionalSettingsFilePath []
info: LauncherSplashImagePath [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/SlicerApp-real]
info: ApplicationToLaunchArguments []
info: AdditionalSettingsFilePath []
info: LauncherDir [/home/antonio/Documents/Slicer-5.4.0-linux-amd64]
info: LauncherName [Slicer]
info: OrganizationDomain [slicer.org]
info: OrganizationName [slicer.org]
info: ApplicationName [Slicer]
info: ApplicationRevision [31938]
info: SettingsFileName [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/SlicerLauncherSettings.ini]
info: SettingsDir [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin]
info: UserAdditionalSettingsDir [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org]
info: UserAdditionalSettingsFileName [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Slicer-31938.ini]
info: UserAdditionalSettingsFileBaseName []
info: AdditionalSettingsDir []
info: AdditionalSettingsExcludeGroups []
info: LauncherNoSplashScreen [0]
info: AdditionalLauncherHelpShortArgument [-h]
info: AdditionalLauncherHelpLongArgument [--help]
info: AdditionalLauncherNoSplashArguments [--no-splash,--help,--version,--home,--program-path,--no-main-window,--settings-path,--temporary-path]
info: DetachApplicationToLaunch [0]
info: LoadEnvironment [-1]
info: LauncherSplashImagePath [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/SlicerApp-real]
info: ApplicationToLaunchArguments []
info: &lt;APPLAUNCHER_DIR&gt; -&gt; [/home/antonio/Documents/Slicer-5.4.0-linux-amd64]
info: &lt;APPLAUNCHER_NAME&gt; -&gt; [Slicer]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (RegularSettings) -&gt; [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
info: &lt;PATHSEP&gt; -&gt; [:]
info: Setting env. variable [QTWEBENGINE_DISABLE_SANDBOX]:1
info: Setting env. variable [SLICER_HOME]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/..
info: Setting env. variable [PIP_REQUIRE_VIRTUALENV]:0
info: Setting env. variable [ITK_AUTOLOAD_PATH]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/ITKFactories
info: Setting env. variable [PYTHONNOUSERSITE]:1
info: Setting env. variable [PYTHONHOME]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python
info: Setting env. variable [SSL_CERT_FILE]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../share/Slicer-5.4/Slicer.crt
info: Setting env. variable [LibraryPaths]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../bin:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Teem-1.12.0:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/PythonQt:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/numpy/core:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib
info: Setting env. variable [LD_LIBRARY_PATH]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../bin:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Teem-1.12.0:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/PythonQt:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/numpy/core:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib
info: Setting env. variable [PATH]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../bin:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/cli-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-loadable-modules
info: Setting env. variable [QT_PLUGIN_PATH]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/QtPlugins
info: Setting env. variable [PYTHONPATH]:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/qt-scripted-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/qt-scripted-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-scripted-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-loadable-modules:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/vtkTeem:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../bin/Python:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Slicer-5.4/qt-loadable-modules/Python:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/lib-dynload:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/Python/lib/python3.9/site-packages:/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/../lib/python3.9/site-packages
info: Starting [/home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin/SlicerApp-real]
info: argument [--application-information]
info: launcher-timeout (ms) [-1000]
info: DisableSplash [0]
Session start time .......: 2023-11-24 12:30:01
Slicer version ...........: 5.4.0 (revision 31938 / 311cb26) linux-amd64 - installed release
Operating system .........: Linux / 5.15.0-89-generic / #99-Ubuntu SMP Mon Oct 30 20:42:41 UTC 2023 / UTF-8 - 64-bit
Memory ...................: 15778 MB physical, 2047 MB virtual
CPU ......................: GenuineIntel 12th Gen Intel(R) Core(TM) i7-12700H, 14 cores, 20 logical processors
VTK configuration ........: OpenGL2 rendering, Sequential threading
Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
Internationalization .....: disabled, language=
Developer mode ...........: disabled
Application path .........: /home/antonio/Documents/Slicer-5.4.0-linux-amd64/bin
Additional module paths ..: slicer.org/Extensions-31938/AnomalousFiltersExtension/lib/Slicer-5.4/cli-modules, slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/cli-modules, slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/qt-loadable-modules, slicer.org/Extensions-31938/SlicerDMRI/lib/Slicer-5.4/qt-scripted-modules, slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/cli-modules, slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/qt-loadable-modules, slicer.org/Extensions-31938/UKFTractography/lib/Slicer-5.4/qt-scripted-modules
Switch to module:  "Welcome"
</code></pre>

---

## Post #11 by @pieper (2023-11-24 18:10 UTC)

<p>Hmm, that’s odd.  I don’t have any experience with linux mint, but I can say that I did a build from source this morning on a ubuntu 20.04 with no issues.</p>
<p>Maybe <a class="mention" href="/u/acsenrafilho">@acsenrafilho</a> you could start a fresh build and see if the issue recurs?  Or perhaps as a fallback install docker and try a different distribution.</p>

---

## Post #12 by @acsenrafilho (2023-11-25 15:58 UTC)

<p>Indeed this is odd. I have been using Slicer on Linux Mint for several years (since version 19) and it is the first time I have seen this issue with file permissions on execution.</p>
<p>I am wondering if I may have done something wrong with the dependencies installations or if the cmake setup had some parameters that I need to change.</p>
<p>Just to be sure:</p>
<ol>
<li>I followed the installation procedure in the Slicer documentation (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">relative to Linux section</a>)</li>
<li>I installed the dependencies following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-23-04-lunar-lobster" rel="noopener nofollow ugc">Ubuntu recommendations</a> (since Linux Mint is based on Ubuntu)</li>
<li>The cmake version used was 3.28 which I <a href="https://cmake.org/download/" rel="noopener nofollow ugc">installed from source</a> (using the cmake installation recommendations)</li>
</ol>
<p>The rest of the process I don´t know what gives us a clue… In your opinion, what could be the most probable issue? is it something about Python? The OpenSSL error at first starting execution have something related to it?</p>
<p>I will try to build Slicer again, but I don´t know what parameter may be better to change. Is there any recommendation? or try to use the “default” build again?</p>

---

## Post #13 by @pieper (2023-11-25 16:09 UTC)

<p>I guess I would try the default again.  I typically use a command like</p>
<p><code>time make -j $(nproc) |&amp; tee buildlog</code></p>
<p>to be able to look for anything suspicious in the buildlog.  But there really shouldn’t be anything requiring root permissions just to run a fresh build.</p>
<p>My other suggestion would be to build in Debug mode or RelWithDebInfo so you can step through and see where the crash happens.</p>

---

## Post #14 by @acsenrafilho (2023-11-27 13:35 UTC)

<p>Great tip <a class="mention" href="/u/pieper">@pieper</a>, I have made the build using the default configuration and exported the terminal output in the file bellow:<br>
<a href="https://drive.google.com/file/d/1m_Q8u48x4Yc400E5-n0ONuMluwZR0YsI/view?usp=sharing" rel="noopener nofollow ugc">buildlog</a></p>
<p>This is Google Drive link, please informs me if you have some problem with the access.</p>
<p>I tried to find something in the log, but I confess that I did not know how to filter it properly.</p>
<p>Looking forward for any help.</p>
<p>By the way, the <code>./Slicer</code> execution failed in the same way before.</p>

---

## Post #15 by @pieper (2023-12-01 22:07 UTC)

<p>I don’t see anything out of the ordinary in the build log.</p>
<p>I think single-stepping through the startup process would be the most informative: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html" class="inline-onebox">C++ debugging on GNU/Linux systems — 3D Slicer documentation</a></p>

---
