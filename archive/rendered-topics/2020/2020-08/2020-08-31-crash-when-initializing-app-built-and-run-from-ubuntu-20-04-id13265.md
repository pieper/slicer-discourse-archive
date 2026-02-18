# Crash when initializing app built and run from Ubuntu 20.04

**Topic ID**: 13265
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/crash-when-initializing-app-built-and-run-from-ubuntu-20-04/13265

---

## Post #1 by @Atabak (2020-08-31 19:56 UTC)

<p>Operating system: Ubuntu 20.04.1 LTS<br>
Slicer version: [v4.11]<br>
Expected behavior: To load Slicer<br>
Actual behavior: Failed Loading Slicer</p>
<p>I finally succeeded in building Slicer, but the software is not loading. I have no clue what the error is.</p>
<p>This is the message I get:</p>
<p>atabak@atabak-X550JX:~/Slicer/Slicer-SuperBuild-Debug/Slicer-build$ ./Slicer<br>
error: [/home/atabak/Slicer/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/527dbda9f74af2749ef409e52ad86d80704f468e.png" data-download-href="/uploads/short-url/bLKyaEuIcQrjg4kCz0I5noAwGqq.png?dl=1" title="Screenshot from 2020-08-31 12-48-44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/527dbda9f74af2749ef409e52ad86d80704f468e.png" alt="Screenshot from 2020-08-31 12-48-44" data-base62-sha1="bLKyaEuIcQrjg4kCz0I5noAwGqq" width="690" height="107" data-dominant-color="472C41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-31 12-48-44</span><span class="informations">798×124 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-31 20:00 UTC)

<p>Slicer-4.10.2 is almost two years old. I would recommend the latest Slicer master for any developments.</p>
<p>I’m not an experienced linux developer, but managed to build and run it a few days ago without any issues on Ubuntu 20.04 just by closely following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">build instructions</a>.</p>

---

## Post #3 by @Atabak (2020-08-31 20:10 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. I mistyped the version. I’ve built the latest version (i.e. Slicer-4.11). I had some problems building it on ubuntu 18 and got some qt randomgenerator errors and I saw in some forum that ubuntu 20 surpassed that problem. So, I built the whole thing on ubuntu 20. but, I still couldn’t load Slicer.</p>
<p>I did run the following command to see what’s going on</p>
<p>./Slicer --launcher-verbose</p>
<p>I only found that there is some missing directory for the following:</p>
<p>info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) → [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]<br>
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) → [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce175031120add8ea6d5e04a0c5d9eeb60dc137.png" data-download-href="/uploads/short-url/k6hSTzwMclgyY8w6aVk29s53CUn.png?dl=1" title="Screenshot from 2020-08-31 13-06-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ce175031120add8ea6d5e04a0c5d9eeb60dc137_2_690x317.png" alt="Screenshot from 2020-08-31 13-06-53" data-base62-sha1="k6hSTzwMclgyY8w6aVk29s53CUn" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ce175031120add8ea6d5e04a0c5d9eeb60dc137_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce175031120add8ea6d5e04a0c5d9eeb60dc137.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ce175031120add8ea6d5e04a0c5d9eeb60dc137.png 2x" data-dominant-color="432439"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-31 13-06-53</span><span class="informations">998×459 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m have no idea what the problem could be. I even spent hours browising through these forums but only found this <a href="https://github.com/Slicer/Slicer/issues/5000" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/5000</a><br>
which is somewhat similar but not totally.</p>

---

## Post #4 by @lassoan (2020-08-31 20:17 UTC)

<p>AdditionalSettings are options. It is not a problem that they are not found.</p>
<p>Output of <code>./Slicer --launcher-verbose</code> for me is the following:</p>
<pre><code class="lang-auto">info: AdditionalSettingsFilePath []
info: LauncherSplashImagePath [/home/osboxes/D/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/./SlicerApp-real]
info: ApplicationToLaunchArguments []
info: AdditionalSettingsFilePath []
info: LauncherDir [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build]
info: LauncherName [Slicer]
info: OrganizationDomain [www.na-mic.org]
info: OrganizationName [NA-MIC]
info: ApplicationName [Slicer]
info: ApplicationRevision [29321]
info: SettingsFileName [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/./SlicerLauncherSettings.ini]
info: SettingsDir [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build]
info: UserAdditionalSettingsDir [/home/osboxes/.config/NA-MIC]
info: UserAdditionalSettingsFileName [/home/osboxes/.config/NA-MIC/Slicer-29321.ini]
info: UserAdditionalSettingsFileBaseName []
info: AdditionalSettingsDir []
info: AdditionalSettingsExcludeGroups []
info: LauncherNoSplashScreen [0]
info: AdditionalLauncherHelpShortArgument [-h]
info: AdditionalLauncherHelpLongArgument [--help]
info: AdditionalLauncherNoSplashArguments [--no-splash,--help,--version,--home,--program-path,--no-main-window,--settings-path,--temporary-path]
info: DetachApplicationToLaunch [0]
info: LoadEnvironment [-1]
info: LauncherSplashImagePath [/home/osboxes/D/Slicer/Applications/SlicerApp/Resources/Images/Slicer-SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/./SlicerApp-real]
info: ApplicationToLaunchArguments []
info: &lt;APPLAUNCHER_DIR&gt; -&gt; [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build]
info: &lt;APPLAUNCHER_NAME&gt; -&gt; [Slicer]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (RegularSettings) -&gt; [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [/home/osboxes/.config/NA-MIC]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
info: &lt;PATHSEP&gt; -&gt; [:]
info: Setting env. variable [SLICER_HOME]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build
info: Setting env. variable [PIP_REQUIRE_VIRTUALENV]:0
info: Setting env. variable [ITK_AUTOLOAD_PATH]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/ITKFactories/.
info: Setting env. variable [PYTHONNOUSERSITE]:1
info: Setting env. variable [PYTHONHOME]:/home/osboxes/D/Slicer-SuperBuild-Release/python-install
info: Setting env. variable [SSL_CERT_FILE]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/share/Slicer-4.11/Slicer.crt
info: Setting env. variable [LD_LIBRARY_PATH]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/.:../lib/Slicer-4.11/qt-loadable-modules:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/cli-modules/.:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/qt-loadable-modules/.:/home/osboxes/D/Slicer-SuperBuild-Release/OpenSSL:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib:/home/osboxes/D/Slicer-SuperBuild-Release/VTK-build/lib/.:/home/osboxes/D/Slicer-SuperBuild-Release/teem-build/bin/.:/home/osboxes/D/Slicer-SuperBuild-Release/DCMTK-build/lib/.:/home/osboxes/D/Slicer-SuperBuild-Release/ITK-build/lib/.:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/CTK-build/bin/.:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/QtTesting-build/.:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/PythonQt-build/.:/home/osboxes/D/Slicer-SuperBuild-Release/LibArchive-install/lib:/home/osboxes/D/Slicer-SuperBuild-Release/SimpleITK-build/SimpleITK-build/lib/.:/home/osboxes/D/Slicer-SuperBuild-Release/SlicerExecutionModel-build/ModuleDescriptionParser/bin/.:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site-packages/numpy/core:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site-packages/numpy/lib:/home/osboxes/D/Slicer-SuperBuild-Release/JsonCpp-build/src/lib_json/.
info: Setting env. variable [PATH]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/.:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/cli-modules/.:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/bin:/home/osboxes/D/Slicer-SuperBuild-Release/teem-build/bin/.
info: Setting env. variable [QT_PLUGIN_PATH]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/CTK-build/bin:/usr/lib/plugins
info: Setting env. variable [PYTHONPATH]:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/.:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/Python:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/qt-loadable-modules/.:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/qt-loadable-modules/Python:/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/lib/Slicer-4.11/qt-scripted-modules:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/lib-dynload:/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site-packages:/home/osboxes/D/Slicer-SuperBuild-Release/VTK-build/lib/python3.6/site-packages:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/CTK-build/bin/Python:/home/osboxes/D/Slicer-SuperBuild-Release/CTK-build/CTK-build/bin/.
info: Starting [/home/osboxes/D/Slicer-SuperBuild-Release/Slicer-build/bin/./SlicerApp-real]
info: launcher-timeout (ms) [-1000]
info: DisableSplash [0]
Switch to module:  "Welcome"
</code></pre>
<p>Do you see any difference compared to yours?</p>
<p>I’ve just use this Ubuntu 20.04 image on virtualbox: <a href="https://www.osboxes.org/ubuntu/">https://www.osboxes.org/ubuntu/</a><br>
Is your computer a physical linux computer that you use for other developments, too?</p>
<p>Can you run a simple OpenGL application, such as glxgears?</p>

---

## Post #5 by @Atabak (2020-08-31 20:47 UTC)

<p>Yes I can run a simple OpenGL application, such as glmark2 (as demonstrated in the image below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66190d4c4f03b9b0a600cf655840a39f66f7549.png" data-download-href="/uploads/short-url/uAvdaaMOsB4IRcl9p8hKtfLpYfL.png?dl=1" title="Screenshot from 2020-08-31 13-36-22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d66190d4c4f03b9b0a600cf655840a39f66f7549_2_690x472.png" alt="Screenshot from 2020-08-31 13-36-22" data-base62-sha1="uAvdaaMOsB4IRcl9p8hKtfLpYfL" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d66190d4c4f03b9b0a600cf655840a39f66f7549_2_690x472.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66190d4c4f03b9b0a600cf655840a39f66f7549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d66190d4c4f03b9b0a600cf655840a39f66f7549.png 2x" data-dominant-color="1F1C1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-31 13-36-22</span><span class="informations">947×649 83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There are some differences between your output and mine:</p>
<p>These are yours:</p>
<blockquote>
<pre><code>info: ApplicationRevision [29321]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [/home/osboxes/.config/NA-MIC]
</code></pre>
</blockquote>
<p>These are mine:</p>
<blockquote>
<pre><code>info: ApplicationRevision [29335]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
</code></pre>
</blockquote>
<p>These are the only 2 differences that I found.</p>
<p>And, yes I have my Linux installed on my SSD. I use Windows 10 on the oracle VM virtual box though.</p>

---

## Post #6 by @lassoan (2020-08-31 20:50 UTC)

<p>Can you get a stack trace of the crash?</p>

---

## Post #7 by @Atabak (2020-08-31 20:55 UTC)

<p>Yes, the following was generated in my syslog:</p>
<blockquote>
<p>Aug 31 13:54:20 atabak-X550JX gnome-shell[2071]: Window manager warning: Invalid WM_TRANSIENT_FOR window 0x3a00004 specified for 0x3a00002.</p>
</blockquote>
<blockquote>
<p>Aug 31 13:54:21 atabak-X550JX kernel: [22784.692296] SlicerApp-real[30426]: segfault at 0 ip 00007f8421bfe9ee sp 00007ffd48fbe448 error 4 in libc-2.31.so[7f8421a9d000+178000]</p>
</blockquote>
<blockquote>
<p>Aug 31 13:54:21 atabak-X550JX kernel: [22784.692302] Code: 0f 84 fd fe ff ff e9 91 81 f3 ff 90 f3 0f 1e fa 89 f8 31 d2 c5 c5 ef ff 09 f0 25 ff 0f 00 00 3d 80 0f 00 00 0f 8f 52 03 00 00  fe 6f 0f c5 f5 74 06 c5 fd da c1 c5 fd 74 c7 c5 fd d7 c8 85 c9</p>
</blockquote>

---

## Post #8 by @lassoan (2020-08-31 21:39 UTC)

<p>Knowing that the crash occurred in libc is not very useful. Can you get a stack trace? This may help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault</a></p>
<p>I’ve tried to start Slicer in gdb on Linux by following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#GDB_debug_with_launch_arguments">these instructions</a>, I get the error below. When I try to debug using VS Code, I get the same error.</p>
<pre><code class="lang-auto">osboxes@osboxes:~/D/Slicer-SuperBuild-Release/Slicer-build$ ./Slicer --launch /usr/bin/gnome-terminal
Fatal Python error: init_import_size: Failed to import the site module
Python runtime state: initialized
Traceback (most recent call last):
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/home/osboxes/D/Slicer-SuperBuild-Release/python-install/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'
</code></pre>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know how to fix this?</p>

---

## Post #9 by @Atabak (2020-08-31 22:05 UTC)

<p>I did as you asked and I got the same error as you have!</p>
<blockquote>
<p>atabak@atabak-X550JX:~/Slicer/Slicer-SuperBuild-Debug/Slicer-build$ ./Slicer --launch /usr/bin/gnome-terminal<br>
Fatal Python error: init_import_size: Failed to import the site module<br>
Python runtime state: initialized<br>
Traceback (most recent call last):<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site.py”, line 553, in <br>
main()<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site.py”, line 539, in main<br>
known_paths = addusersitepackages(known_paths)<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site.py”, line 282, in addusersitepackages<br>
user_site = getusersitepackages()<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site.py”, line 258, in getusersitepackages<br>
user_base = getuserbase() # this will also set USER_BASE<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/site.py”, line 248, in getuserbase<br>
USER_BASE = get_config_var(‘userbase’)<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/sysconfig.py”, line 601, in get_config_var<br>
return get_config_vars().get(name)<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/sysconfig.py”, line 550, in get_config_vars<br>
_init_posix(_CONFIG_VARS)<br>
File “/home/atabak/Slicer/Slicer-SuperBuild-Debug/python-install/lib/python3.6/sysconfig.py”, line 421, in _init_posix<br>
_temp = <strong>import</strong>(name, globals(), locals(), [‘build_time_vars’], 0)<br>
ModuleNotFoundError: No module named ‘_sysconfigdata__linux_x86_64-linux-gnu’</p>
</blockquote>

---

## Post #10 by @lassoan (2020-08-31 22:06 UTC)

<aside class="quote no-group" data-username="Atabak" data-post="9" data-topic="13265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atabak/48/7940_2.png" class="avatar"> Atabak:</div>
<blockquote>
<p>I did as you asked and I got the same error as you have!</p>
</blockquote>
</aside>
<p>Until <a class="mention" href="/u/jcfr">@jcfr</a> gets back to us with a solution for gdb, you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#With_systemd">systemd</a> for getting the stack trace.</p>

---

## Post #11 by @pieper (2020-08-31 22:13 UTC)

<p>I often get debugging hints by running SlicerApp-real with strace to see the last system calls before it dies.  You can start with Slicer --xterm and run it in that shell so you have the environment.</p>
<p>I have also recently built on ubuntu 20.04 with no problems.</p>

---

## Post #12 by @Atabak (2020-08-31 22:54 UTC)

<p>I think this is what you were after. I’m not sure though. Is this it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c9e1bb3f0c1d1682dbadcade77688ce4679042b.png" data-download-href="/uploads/short-url/8EfooFq6s5HS38OhKKFpn4EhARd.png?dl=1" title="Screenshot from 2020-08-31 15-49-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c9e1bb3f0c1d1682dbadcade77688ce4679042b_2_690x403.png" alt="Screenshot from 2020-08-31 15-49-49" data-base62-sha1="8EfooFq6s5HS38OhKKFpn4EhARd" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c9e1bb3f0c1d1682dbadcade77688ce4679042b_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c9e1bb3f0c1d1682dbadcade77688ce4679042b_2_1035x604.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c9e1bb3f0c1d1682dbadcade77688ce4679042b_2_1380x806.png 2x" data-dominant-color="38152D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-08-31 15-49-49</span><span class="informations">1645×961 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2020-09-01 00:05 UTC)

<p>OpenSSL error, as usual… There have been lots of problems with OpenSLL, especially on Linux. Search for error reports on this topic on this forum and the Slicer issue tracker (both are indexed in Google), and try the proposed solutions.</p>
<p>The error occurred while executing an avx2 instruction. Is it possible that your computer does not support __strcmp_avx2 instruction? (not very likely, as then the error should have been invalid instruction, but just in case) How old is your computer? What CPU does it have?</p>

---

## Post #14 by @Atabak (2020-09-01 00:07 UTC)

<p>My Laptop is about 6 years old. This is the processor:<br>
Intel® Core™ i7-4720HQ CPU @ 2.60GHz × 8</p>

---

## Post #15 by @lassoan (2020-09-01 00:15 UTC)

<p>That CPU already supports avx2 (<a href="https://ark.intel.com/content/www/us/en/ark/products/78934/intel-core-i7-4720hq-processor-6m-cache-up-to-3-60-ghz.html">https://ark.intel.com/content/www/us/en/ark/products/78934/intel-core-i7-4720hq-processor-6m-cache-up-to-3-60-ghz.html</a>) so the instruction set should not be an issue.</p>
<p>So, most likely it is one of the other OpenSSL related problems that others have reported before.</p>
<p>Do the official Slicer builds run well?</p>

---

## Post #16 by @Atabak (2020-09-01 00:20 UTC)

<p>By “official” if you mean the user one. yes I used to work with that 4 months ago. But I need the “Developer”.<br>
or by “official Slicer build” you mean the complete slicer-developer build explained here : <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html</a></p>
<p>Yes after upgrading my linux to ubuntu 20 it worked very well.</p>
<p>I hope I answered your question.</p>

---

## Post #17 by @lassoan (2020-09-01 00:25 UTC)

<p>So, packages that you get from <a href="http://download.slicer.org">download.slicer.org</a> work well, but that you build yourself crash on startup? Have you built in debug or release mode?</p>

---

## Post #18 by @Atabak (2020-09-01 00:31 UTC)

<p>Yes those worked very well. And, yes after a successful build of the “developer” in ubuntu 20 I get a crash in the startup when I try to load Slicer.</p>
<p>No, I haven’t built in the debug or release mode. Will that solve my problem stated in the beginning of this thread? I think you are trying to point out that it might be a hard-ware problem. Correct?</p>

---

## Post #19 by @lassoan (2020-09-01 01:06 UTC)

<aside class="quote no-group" data-username="Atabak" data-post="18" data-topic="13265">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/atabak/48/7940_2.png" class="avatar"> Atabak:</div>
<blockquote>
<p>No, I haven’t built in the debug or release mode. Will that solve my problem stated in the beginning of this thread? I think you are trying to point out that it might be a hard-ware problem. Correct?</p>
</blockquote>
</aside>
<p>You always build in “Debug” or “Release” (or “DebWithRelInfo” or “MinSizeRel”) configuration. If you don’t specify build mode then I think the default is “Debug” (more verbose debug information but slower execution time).</p>
<p>Your CPU is quite old but it should still be able to build and run Slicer, so it is not a hardware problem.</p>
<p>I did a quick search. There <a href="https://github.com/Slicer/Slicer/pull/4992">used to be such errors at startup</a> but they have all been fixed. Are you using the latest master version? What is your linux kernel, Qt, OpenSSL, and gcc compiler versions? (you may find some version information in your build log of top-level CMakeCache.txt file)</p>

---

## Post #20 by @Atabak (2020-09-01 23:45 UTC)

<p>Hi Andras,</p>
<p>I am sorry for the late response. I came to a conclusion yesterday that upgrading my ubuntu from 18 to 20 wasn’t a good idea and I decided to build Ubuntu 20 from scratch. And, I successfully built the Slicer-Developer without any errors.</p>
<p>FYI, all the versions of Qt, etc that you asked were based on this instruction:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html</a></p>
<p>So for other users out there, I would suggest not to upgrade their Linux- ubuntu version from 18 to 20 for the purpose of building Slicer cause they won’t be able to load the software itself, probably because of the versions of qt and other necessary softwares that are required for the build.</p>
<blockquote>
<p>cd Slicer-SuperBuild-Debug/Slicer-build<br>
ctest -j4</p>
</blockquote>
<p>There is one more point that I want to mention. When I tried to test Slicer in ubuntu 20 that was upgraded from ubuntu 18 with the instruction mentioned above I had about 240 tests failed out of 680. But in ubuntu 20 that I installed from scratch, I only had 9 tests failed out of 680!</p>
<p>Andras - Thank you for your help throughout the troubleshooting. Your guidance was the main reason I got the intuition to reinstall ubuntu 20 from scratch.</p>
<p>Cheers,<br>
Atabak</p>

---

## Post #21 by @Amir_Zolal (2021-01-14 08:31 UTC)

<p>Hello,</p>
<p>so I still have this problem:</p>
<p>qt5ct: using qt5ct plugin<br>
error: [/home/zolal/Slicer/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
<p>Now, when I try the following:</p>
<p>QT_DEBUG_PLUGINS=1 ./Slicer</p>
<p>Slicer runs!</p>
<p>Now, I have tried various other solutions proposed here in the forum, inclusive disabling Python SSL, but that was not so successful.<br>
So I guess the problem is with QT, any idea how to get nearer to the issue?</p>

---

## Post #22 by @lassoan (2021-01-14 14:56 UTC)

<p>Can you get a stack trace?<br>
Maybe it is the same issue as this: <a href="https://sourceforge.net/p/qt5ct/tickets/77/" class="inline-onebox">qt5ct / Tickets / #77 Krita crashes with qt5ct plugin with Qt5.15</a></p>

---

## Post #23 by @Amir_Zolal (2021-01-14 17:22 UTC)

<p>strace&gt;<br>
<a href="https://pastebin.ubuntu.com/p/mqsy8Ytn94/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://pastebin.ubuntu.com/p/mqsy8Ytn94/</a></p>

---

## Post #24 by @Amir_Zolal (2021-01-14 18:08 UTC)

<p>Somehow I do not understand what all the EAGAIN resource not available means. Is this the problem?</p>

---

## Post #25 by @lassoan (2021-01-14 19:03 UTC)

<p>This file seems to be list of system calls. It is somewhat interesting, but the stack trace could be more informative. Could you print that, too?</p>

---

## Post #26 by @Amir_Zolal (2021-01-14 21:06 UTC)

<p>So, one would think that strace will produce the stacktrace and not a trace of system calls, right? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Now. I tried with gdb, maybe this will help someone:</p>
<p>gdb ./Slicer 2&gt;&amp;1 | tee ~/gdb-Slicer.txt<br>
(gdb) handle SIG33 pass nostop noprint<br>
Signal        Stop	Print	Pass to program	Description<br>
SIG33         No	No	Yes		Real-time event 33<br>
(gdb) set pagination 0<br>
(gdb) set follow-fork-mode child<br>
(gdb) run<br>
Starting program: /home/zolal/Slicer/Slicer-build/Slicer<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
[New Thread 0x7ffff6e35700 (LWP 96055)]<br>
[Attaching after Thread 0x7ffff7622140 (LWP 96054) fork to child process 96056]<br>
[New inferior 2 (process 96056)]<br>
[Detaching after fork from parent process 96054]<br>
[Inferior 1 (process 96054) detached]<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
process 96056 is executing new program: /home/zolal/Slicer/Slicer-build/bin/SlicerApp-real<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
[New Thread 0x7fffd5473700 (LWP 96059)]<br>
qt5ct: using qt5ct plugin<br>
[New Thread 0x7fffcffff700 (LWP 96060)]<br>
[New Thread 0x7fffce9bb700 (LWP 96062)]<br>
[New Thread 0x7fffce1ba700 (LWP 96063)]<br>
[New Thread 0x7fffcd9b9700 (LWP 96064)]<br>
[New Thread 0x7fffcd1b8700 (LWP 96065)]<br>
[New Thread 0x7fffcc9b7700 (LWP 96066)]<br>
[New Thread 0x7fffb7fff700 (LWP 96067)]<br>
[New Thread 0x7fffb3abe700 (LWP 96085)]<br>
[New Thread 0x7fffb2e8d700 (LWP 96086)]<br>
[New Thread 0x7fffb1aff700 (LWP 96087)]<br>
[New Thread 0x7fffb12fe700 (LWP 96088)]</p>
<p>Thread 2.1 “SlicerApp-real” received signal SIGSEGV, Segmentation fault.<br>
[Switching to Thread 0x7fffd6406d40 (LWP 96056)]<br>
0x00007fffe6275d71 in ?? () from /lib/x86_64-linux-gnu/libQt5Widgets.so.5</p>
<p>another funny thing:</p>
<p>running sudo ./Slicer works!!</p>
<p>qmake --version<br>
QMake version 3.1<br>
Using Qt version 5.12.8 in /usr/lib/x86_64-linux-gnu</p>
<p>Somehow I am getting the feeling that this might be related to the fact that my laptop was upgraded from 16.04 -&gt; 18.04 -&gt; 20.04 like in the case of the other user and maybe there is a bug in updating Qt.</p>

---

## Post #27 by @lassoan (2021-01-14 21:08 UTC)

<p>Yes, if sudo works then it suggests that the root cause may be some incorrectly permissions.</p>

---

## Post #28 by @Amir_Zolal (2021-01-16 06:57 UTC)

<p>For future reference: the build using the default Qt version did not work (Qt version 5.12.8 in /usr/lib/x86_64-linux-gnu).</p>
<p>After installing Qt from Qt website using the online installer (with all modules! not the default option, because in default you will miss QtScript etc.) use cmake like this:</p>
<p>cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQt5_DIR=/opt/Qt/5.15.2/gcc_64/lib/cmake/Qt5 …/SlicerSource/</p>
<p>Then make, naturally.<br>
Slicer runs without problems now.</p>

---

## Post #29 by @lassoan (2021-01-16 15:43 UTC)

<p>Thanks for the update. Do you think we should include a note about this in the Slicer build instructions or yours was a very special case?</p>

---

## Post #30 by @Amir_Zolal (2021-01-17 08:40 UTC)

<p>Hi, I think that before you get more similar reports, this was a special case.</p>

---
