---
topic_id: 19472
title: "Launching Slicer With Only Slicelet Displayed On Mac"
date: 2021-09-01
url: https://discourse.slicer.org/t/19472
---

# Launching Slicer with only Slicelet displayed on mac

**Topic ID**: 19472
**Date**: 2021-09-01
**URL**: https://discourse.slicer.org/t/launching-slicer-with-only-slicelet-displayed-on-mac/19472

---

## Post #1 by @hina-shah (2021-09-01 20:18 UTC)

<p>Hi All,</p>
<p>I’m trying to launch Slicer with just a single module on Mac. Would the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">steps here</a> work with Mac as well? Has anybody tried this? I tried a few things, but couldn’t get it to work.</p>
<p>My aim is to let my user click on ‘ModulName.app’ and show the module with ModuleName with only necessary GUI components of Slicer. I’ve been able to do this on Windows, but we would like to have a version for Mac as well.</p>
<p>Thank you!<br>
HIna</p>

---

## Post #2 by @pieper (2021-09-01 20:32 UTC)

<p>I’ve never tried the settings approach, but it should work the same on mac as anywhere else.  Another option is to remove the files related to modules you don’t want to load.  There’s also the <a href="https://github.com/pieper/CustomSlicerGenerator">CustomSlicerGenerator</a> although I haven’t used it in a while.  Of course, building your own <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">SlicerCAT</a> is the most powerful approach.</p>

---

## Post #3 by @hina-shah (2021-09-02 03:33 UTC)

<p>Thanks Steve! I think SlicerCAT is too much work for the simple single module that I’m trying to create.</p>
<p>These are the steps that I followed for my scripted module</p>
<ul>
<li>Copy the <code>ModuleName.py</code> and  <code>ModuelName.ui</code>  in <code>Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules</code> and <code>Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/Resources/UI</code> respectively</li>
<li>Make a copy of <code>bin/SlicerLauncherSettings.ini</code> and rename it to <code>ModuleNameLauncherSettings.ini</code></li>
<li>Make edits in <code>ModuleNameLauncherSettings.ini</code> as:</li>
</ul>
<blockquote>
<p>[General]<br>
additionalSettingsFilePath=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/SlicerLauncherSettings.ini<br>
additionalSettingsExcludeGroups=General,Application,ExtraApplicationToLaunch<br>
launcherNoSplashScreen=false<br>
launcherSplashImagePath=&lt;APPLAUNCHER_DIR&gt;/bin/Slicer-SplashScreen.png<br>
launcherSplashScreenHideDelayMs=3000<br>
additionalLauncherHelpShortArgument=-h<br>
additionalLauncherHelpLongArgument=–help<br>
additionalLauncherNoSplashArguments=–no-splash,–help,–version,–home,–program-path,–no-main-window,–settings-path,–temporary-path</p>
<p>[Application]</p>
<p>path=&lt;APPLAUNCHER_DIR&gt;/bin/ModuleName<br>
arguments=–python-code “slicer.util.selectModule(‘ModuleName’)”<br>
name=ModuleName<br>
revision=29738<br>
<a href="http://organizationDomain=www.na-mic.org">organizationDomain=www.na-mic.org</a><br>
organizationName=NA-MIC</p>
<p>[ExtraApplicationToLaunch]</p>
</blockquote>
<ul>
<li>Rename <code>Contents/MacOS/Slicer</code> to <code>Contents/MacOS/ModuleName</code></li>
</ul>
<p>I’m confused about the path in the [Application] section of the .ini file, since there’s no <code>bin/Slicer</code>  (which is what the original SlicerLauncherSettings.ini file was pointing to), and hence no <code>bin/ModuleName</code> as well.<br>
MacOS packaging works differently, and I’m afraid I need help understanding how things are connected to make this work.</p>
<p>Thank you!<br>
Hina</p>

---

## Post #4 by @jcfr (2021-09-02 05:32 UTC)

<aside class="quote no-group" data-username="hina-shah" data-post="1" data-topic="19472">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/hina-shah/48/695_2.png" class="avatar"> hina-shah:</div>
<blockquote>
<p>I’m trying to launch Slicer with just a single module on Mac.</p>
</blockquote>
</aside>
<p>Slicer accepts the option <code>--modules-to-ignore</code>, from the command line, specifying the list of modules to ignore as <code>ModuleNameA,ModuleNameB,...</code> should allow you to achieve this.</p>
<aside class="quote no-group" data-username="hina-shah" data-post="1" data-topic="19472">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/hina-shah/48/695_2.png" class="avatar"> hina-shah:</div>
<blockquote>
<p>My aim is to let my user click on ‘ModulName.app’ and show the module with ModuleName with only necessary GUI components of Slicer. I’ve been able to do this on Windows, but we would like to have a version for Mac as well.</p>
</blockquote>
</aside>
<p>This command line parameter has its equivalent in the revision specific settings file shipped along side the application, on macOS it would be <code>Slicer.app/Contents/www.na-mic.org/Slicer-NNNNN.ini</code> here <code>NNNNN</code> is the slicer revision.</p>
<p>In this file, there is the following:</p>
<pre><code class="lang-auto">[Extensions]
....

[Modules]
AdditionalPaths=@Invalid()
IgnoreModules=@Invalid()
</code></pre>
<p>Setting <code>IgnoreModules</code> to the list of modules should allow to achieve the desired effect on all platforms.</p>
<h3><a name="p-65553-updating-default-settings-eg-home-module-1" class="anchor" href="#p-65553-updating-default-settings-eg-home-module-1" aria-label="Heading link"></a>Updating default settings (e.g home module)</h3>
<ul>
<li>Create an empty the file <code>Slicer.app/Contents/www.na-mic.org/Slicer.ini</code> (or equivalent on Linux and Windows)</li>
<li>Configure Module settings or any other settings of your choice</li>
</ul>
<p>The setting found in the install tree will now be used and should allow you to create a zip file on all platform.</p>
<h3><a name="p-65553-notes-about-renaming-2" class="anchor" href="#p-65553-notes-about-renaming-2" aria-label="Heading link"></a>Notes about renaming</h3>
<ul>
<li>
<p>On macOS, you should be able to rename <code>Slicer.app</code> to <code>AnyName.app</code></p>
</li>
<li>
<p>Since the main  application name is hard-coded in the executable at build time, you should not rename the settings files bundled in the package.</p>
</li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7e8515f85efc44674c021336746b4c6d8a3363e4/Base/QTCore/qSlicerCoreApplication.cxx#L1567-L1570">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7e8515f85efc44674c021336746b4c6d8a3363e4/Base/QTCore/qSlicerCoreApplication.cxx#L1567-L1570" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7e8515f85efc44674c021336746b4c6d8a3363e4/Base/QTCore/qSlicerCoreApplication.cxx#L1567-L1570" target="_blank" rel="noopener">Base/QTCore/qSlicerCoreApplication.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/7e8515f85efc44674c021336746b4c6d8a3363e4/Base/QTCore/qSlicerCoreApplication.cxx#L1567-L1570" rel="noopener"><code>7e8515f85</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1567" style="counter-reset: li-counter 1566 ;">
          <li>QString qSlicerCoreApplication::mainApplicationName()const</li>
          <li>{</li>
          <li>  return QString(Slicer_MAIN_PROJECT_APPLICATION_NAME);</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
