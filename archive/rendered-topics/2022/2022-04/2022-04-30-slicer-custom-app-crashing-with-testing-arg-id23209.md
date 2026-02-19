---
topic_id: 23209
title: "Slicer Custom App Crashing With Testing Arg"
date: 2022-04-30
url: https://discourse.slicer.org/t/23209
---

# Slicer custom app crashing with --testing arg

**Topic ID**: 23209
**Date**: 2022-04-30
**URL**: https://discourse.slicer.org/t/slicer-custom-app-crashing-with-testing-arg/23209

---

## Post #1 by @jamesobutler (2022-04-30 23:25 UTC)

<p>Using the latest of the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">SlicerCustomAppTemplate</a> and using a default configuration that uses Qt 5.15.2, I’m experiencing that it always crashes when running with the <code>--testing</code> command line argument. The output is like the following:</p>
<pre><code class="lang-auto">PS C:\SA\Slicer-build&gt; ./MyName.exe --testing
libpng warning: iCCP: known incorrect sRGB profile
error: [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe] exit abnormally - Report the problem.
PS C:\SA\Slicer-build&gt;
</code></pre>
<p>I tried using the base Slicer custom app configuration because I was originally running into this issue with my actual customized Slicer custom app that I use. I don’t run into that libpng warning with my real app, but I was experiencing the error of the application crashing when using <code>--testing</code>.</p>
<p><strong>Additional Observations:</strong><br>
What I observe when running my custom application with the <code>--testing</code> command line argument is that the launcher splash screen appears to show and close normally, but it never gets to the splash screen that includes the “Loading modules…” type additional text. Instead it crashes and displays the exit abnormally on the command line.</p>
<p><strong>Debugging Attempts:</strong><br>
This crash with the <code>--testing</code> argument does not seem to happen with a local regular Slicer build and also doesn’t happen with a version of Slicer download from the Slicer website. It seems specific to a Slicer custom application. I tried with <a href="http://salt.slicer.org/download/" rel="noopener nofollow ugc">Slicer Salt 3.0.0</a>(a Slicer custom app) and did not run into the issue though notably that version is quite old and hasn’t been updated since July 2020.</p>
<p><strong>Questions:</strong><br>
Any thoughts of why it is crashing early in the launcher process? Is this a known issue?</p>
<p>cc: <a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> for their expertise with the Slicer Custom App.</p>

---

## Post #2 by @cpinter (2022-05-02 09:07 UTC)

<p>For the record this is a ticket about the same problem in the GitHub repo: <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/issues/23" class="inline-onebox">Python automated tests crash · Issue #23 · KitwareMedical/SlicerCustomAppTemplate · GitHub</a></p>

---

## Post #3 by @jamesobutler (2022-05-02 13:25 UTC)

<p>Since it may be launcher related, here’s the full output when I use the <code>--launcher-verbose</code> flag.</p>
<details>
<summary>
Launcher verbose output</summary>
<pre><code class="lang-auto">PS C:\SA\Slicer-build&gt; ./MyName.exe --testing --launcher-verbose
info: AdditionalSettingsFilePath []
info: LauncherSplashImagePath [C:/MyName/Applications/MyNameApp/Resources/Images/SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe]
info: ApplicationToLaunchArguments []
info: AdditionalSettingsFilePath []
info: LauncherDir [C:/SA/Slicer-build]
info: LauncherName [MyName]
info: OrganizationDomain [myname.com]
info: OrganizationName []
info: ApplicationName [MyName]
info: ApplicationRevision [30811]
info: SettingsFileName [C:/SA/Slicer-build/./MyNameLauncherSettings.ini]
info: SettingsDir [C:/SA/Slicer-build]
info: UserAdditionalSettingsDir [C:/Users/JamesButler/AppData/Roaming/myname.com]
info: UserAdditionalSettingsFileName []
info: UserAdditionalSettingsFileBaseName []
info: AdditionalSettingsDir []
info: AdditionalSettingsExcludeGroups []
info: LauncherNoSplashScreen [0]
info: AdditionalLauncherHelpShortArgument [-h]
info: AdditionalLauncherHelpLongArgument [--help]
info: AdditionalLauncherNoSplashArguments [--no-splash,--help,--version,--home,--program-path,--no-main-window,--settings-path,--temporary-path]
info: DetachApplicationToLaunch [0]
info: LoadEnvironment [-1]
info: LauncherSplashImagePath [C:/MyName/Applications/MyNameApp/Resources/Images/SplashScreen.png]
info: LauncherSplashScreenHideDelayMs [3000]
info: ApplicationToLaunch [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe]
info: ApplicationToLaunchArguments []
info: &lt;APPLAUNCHER_DIR&gt; -&gt; [C:/SA/Slicer-build]
info: &lt;APPLAUNCHER_NAME&gt; -&gt; [MyName]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (RegularSettings) -&gt; [C:/SA/Slicer-build]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (UserAdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
info: &lt;APPLAUNCHER_SETTINGS_DIR&gt; (AdditionalSettings) -&gt; [&lt;APPLAUNCHER_SETTINGS_DIR-NOTFOUND&gt;]
info: &lt;PATHSEP&gt; -&gt; [;]
info: Setting env. variable [PYTHONNOUSERSITE]:1
info: Setting env. variable [PIP_REQUIRE_VIRTUALENV]:0
info: Setting env. variable [SLICER_HOME]:C:/SA/Slicer-build
info: Setting env. variable [ITK_AUTOLOAD_PATH]:C:/SA/Slicer-build/lib/MyName-5.0/ITKFactories/Release
info: Setting env. variable [PYTHONHOME]:C:/SA/python-install
info: Setting env. variable [SSL_CERT_FILE]:C:/SA/Slicer-build/share/MyName-5.0/Slicer.crt
info: Setting env. variable [LibraryPaths]:C:/SA/Slicer-build/bin/Release;C:/Qt/5.15.2/msvc2019_64/bin;C:/SA/Slicer-build/../lib/MyName-5.0/qt-loadable-modules;C:/SA/Slicer-build/../lib/MyName-5.0/qt-loadable-modules/Release;C:/SA/Slicer-build/lib/MyName-5.0/cli-modules/Release;C:/SA/Slicer-build/lib/MyName-5.0/qt-loadable-modules/Release;C:/SA/OpenSSL-install/Release/bin;C:/SA/python-install/bin;C:/SA/tbb-install/tbb2019_20191006oss/bin/intel64/vc14;C:/SA/VTK-build/bin/Release;C:/SA/teem-build/bin/Release;C:/SA/DCMTK-build/bin/Release;C:/SA/ITK-build/bin/Release;C:/SA/CTK-build/CTK-build/bin/Release;C:/SA/CTK-build/PythonQt-build/Release;C:/SA/LibArchive-install/bin;C:/SA/SlicerExecutionModel-build/ModuleDescriptionParser/bin/Release;C:/SA/python-install/Lib/site-packages/numpy/core;C:/SA/python-install/Lib/site-packages/numpy/lib;C:/SA/JsonCpp-build/src/lib_json/Release
info: Setting env. variable [PYTHONPATH]:C:/SA/Slicer-build/bin/Release;C:/SA/Slicer-build/bin/Python;C:/SA/Slicer-build/lib/MyName-5.0/qt-loadable-modules/Release;C:/SA/Slicer-build/lib/MyName-5.0/qt-loadable-modules/Python;C:/SA/Slicer-build/lib/MyName-5.0/qt-scripted-modules;C:/SA/python-install/Lib;C:/SA/python-install/Lib/lib-dynload;C:/SA/python-install/Lib/site-packages;C:/SA/VTK-build/bin/Lib/site-packages;C:/SA/CTK-build/CTK-build/bin/Python;C:/SA/CTK-build/CTK-build/bin/Release
info: Setting env. variable [QT_PLUGIN_PATH]:C:/SA/Slicer-build/bin;C:/SA/CTK-build/CTK-build/bin;C:/Qt/5.15.2/msvc2019_64/plugins
info: Setting env. variable [Path]:C:/SA/Slicer-build/bin/Release;C:/Qt/5.15.2/msvc2019_64/bin;C:/SA/Slicer-build/lib/MyName-5.0/cli-modules/Release;C:/SA/python-install/bin;C:/SA/teem-build/bin/Release;C:/SA/Slicer-build/bin/Release;C:/Qt/5.15.2/msvc2019_64/bin;C:/SA/Slicer-build/../lib/MyName-5.0/qt-loadable-modules;C:/SA/Slicer-build/../lib/MyName-5.0/qt-loadable-modules/Release;C:/SA/Slicer-build/lib/MyName-5.0/cli-modules/Release;C:/SA/Slicer-build/lib/MyName-5.0/qt-loadable-modules/Release;C:/SA/OpenSSL-install/Release/bin;C:/SA/python-install/bin;C:/SA/tbb-install/tbb2019_20191006oss/bin/intel64/vc14;C:/SA/VTK-build/bin/Release;C:/SA/teem-build/bin/Release;C:/SA/DCMTK-build/bin/Release;C:/SA/ITK-build/bin/Release;C:/SA/CTK-build/CTK-build/bin/Release;C:/SA/CTK-build/PythonQt-build/Release;C:/SA/LibArchive-install/bin;C:/SA/SlicerExecutionModel-build/ModuleDescriptionParser/bin/Release;C:/SA/python-install/Lib/site-packages/numpy/core;C:/SA/python-install/Lib/site-packages/numpy/lib;C:/SA/JsonCpp-build/src/lib_json/Release
info: Starting [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe]
info: argument [--testing]
info: DisableSplash [0]
libpng warning: iCCP: known incorrect sRGB profile
info: launcher-timeout (ms) [-1000]
error: [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe] exit abnormally - Report the problem.
PS C:\SA\Slicer-build&gt;
</code></pre>
</details>

---

## Post #4 by @jamesobutler (2022-05-02 18:30 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<pre><code class="lang-auto">info: launcher-timeout (ms) [-1000]
error: [C:/SA/Slicer-build/bin/Release/MyNameApp-real.exe] exit abnormally - Report the problem.
</code></pre>
</blockquote>
</aside>
<p>Re ^, the launcher appears to crash at the following point below when the process is started to launch the application.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/AppLauncher/blob/7e87d4cf58c27d5d54477a9c22e2962714923f8b/Base/ctkAppLauncher.cpp#L696-L698">
  <header class="source">

      <a href="https://github.com/commontk/AppLauncher/blob/7e87d4cf58c27d5d54477a9c22e2962714923f8b/Base/ctkAppLauncher.cpp#L696-L698" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/AppLauncher/blob/7e87d4cf58c27d5d54477a9c22e2962714923f8b/Base/ctkAppLauncher.cpp#L696-L698" target="_blank" rel="noopener nofollow ugc">commontk/AppLauncher/blob/7e87d4cf58c27d5d54477a9c22e2962714923f8b/Base/ctkAppLauncher.cpp#L696-L698</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="696" style="counter-reset: li-counter 695 ;">
          <li>this-&gt;Process.start(this-&gt;ApplicationToLaunch, this-&gt;ApplicationToLaunchArguments);</li>
          <li>int timeoutInMs = this-&gt;ParsedArgs.value("launcher-timeout").toInt() * 1000;</li>
          <li>this-&gt;reportInfo(QString("launcher-timeout (ms) [%1]").arg(timeoutInMs));</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>info: SettingsFileName [C:/SA/Slicer-build/./MyNameLauncherSettings.ini]</code></p>
</blockquote>
</aside>
<p>Re ^, this seems weird as the file is actually located at “C:/SA/Slicer-build/MyNameLauncherSettings.ini”.</p>

---

## Post #5 by @cpinter (2022-05-03 08:38 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="23209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Re ^, this seems weird as the file is actually located at “C:/SA/Slicer-build/MyNameLauncherSettings.ini”.</p>
</blockquote>
</aside>
<p>To me it seems to be the same path. Sometimes artifacts like this <code>./</code> may appear during path construction, but it should be still valid.</p>

---

## Post #6 by @jamesobutler (2022-05-03 12:51 UTC)

<p>I also tried using the SlicerCustomAppTemplate to create a custom app that actually still had the same name “Slicer” to see if it was an issue related to the custom name, but it still runs into the same failure with the <code>--testing</code> arg.</p>
<pre><code class="lang-auto">PS C:\SA\Slicer-build&gt; ./Slicer.exe --testing
libpng warning: iCCP: known incorrect sRGB profile
error: [C:/SA/Slicer-build/bin/Release/SlicerApp-real.exe] exit abnormally - Report the problem.
PS C:\SA\Slicer-build&gt;
</code></pre>

---

## Post #7 by @lassoan (2022-05-11 18:49 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="4" data-topic="23209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="23209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>info: SettingsFileName [C:/SA/Slicer-build/./MyNameLauncherSettings.ini]</code></p>
</blockquote>
</aside>
<p>Re ^, this seems weird as the file is actually located at “C:/SA/Slicer-build/MyNameLauncherSettings.ini”.</p>
</blockquote>
</aside>
<p>A new default ini file is created for testing (otherwise tests could mess up the actual settings file).</p>
<p>Normal startup:</p>
<pre><code class="lang-auto">c:\D\S4R\Slicer-build&gt;Slicer.exe --python-code "print(slicer.app.userSettings().fileName())"
Switch to module:  "Welcome"
Loading Slicer RC file [C:/Users/andra/.slicerrc.py]
C:/Users/andra/AppData/Roaming/NA-MIC/Slicer.ini
</code></pre>
<p>Startup in testing mode:</p>
<pre><code class="lang-auto">c:\D\S4R\Slicer-build&gt;Slicer.exe --python-code "print(slicer.app.userSettings().fileName())" --testing
Switch to module:  "Welcome"
C:/Users/andra/AppData/Roaming/NA-MIC/Slicer-tmp.ini
</code></pre>
<p>I would recommend to build the custom application in debug mode to find out what happens. You can add a 10s sleep or display a popup at application startup to pause the execution until you attach a debugger.</p>

---

## Post #8 by @lassoan (2022-05-12 02:27 UTC)

<p>A post was merged into an existing topic: <a href="/t/convert-an-extension-into-standalone-application/23371/4">Convert an extension into standalone application</a></p>

---

## Post #11 by @hansmoda (2025-07-11 02:52 UTC)

<p>I also used slicerCustomAppTemplate and used same Qt version in windows. when I use ctest it will failed by the same reason.<br>
<em>error: [D:/DSI/slicer-build/bin/Release/CustomTestingApp-real.exe] exit abnormally - Report the problem.</em><br>
Is there a solution to this?  We look forward to hearing from you.</p>

---
