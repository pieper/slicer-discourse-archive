---
topic_id: 6481
title: "Slicer No Main Window Python Script In Windows Command Promp"
date: 2019-04-12
url: https://discourse.slicer.org/t/6481
---

# Slicer --no-main-window --python-script in windows command prompt not working

**Topic ID**: 6481
**Date**: 2019-04-12
**URL**: https://discourse.slicer.org/t/slicer-no-main-window-python-script-in-windows-command-prompt-not-working/6481

---

## Post #1 by @Allison_Clement (2019-04-12 15:16 UTC)

<p>I am trying to submit a python code to slicer python interactor via the windows command line. I can run my slicer using --python-script mypath. When I add --no-main-window before the --python-script mypath, the code does not run.</p>
<p>Thanks!<br>
AC</p>

---

## Post #2 by @cpinter (2019-04-12 23:44 UTC)

<p>Maybe it helps if you look at an example for a script that does run without main window:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">SlicerRT/BatchProcessing at master · SlicerRt/SlicerRT</a></h3>

  <p><a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing" target="_blank" rel="noopener">master/BatchProcessing</a></p>

  <p><span class="label1">Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Allison_Clement (2019-04-15 15:24 UTC)

<p>My .py file runs when using --python-script, without --no-main-window prior.</p>

---

## Post #5 by @lassoan (2019-04-15 15:34 UTC)

<aside class="quote no-group" data-username="Allison_Clement" data-post="1" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/allison_clement/48/3249_2.png" class="avatar"> Allison_Clement:</div>
<blockquote>
<p>does not run</p>
</blockquote>
</aside>
<p>Is any error displayed? Is any error logged in the application log? Which Slicer version do you use?</p>

---

## Post #6 by @Allison_Clement (2019-04-15 20:21 UTC)

<p>Currently using Slicer 4.8.1 , there is no error it seems to be running in the background when I look at the task manager however the that I request to save in the python code are not being saved.</p>

---

## Post #7 by @lassoan (2019-04-15 20:41 UTC)

<p>Let us know if the problem persists with latest stable version (4.10.1).</p>

---

## Post #8 by @tbillah (2020-04-16 16:53 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, same problem on Win10 PowerShell, Slicer-4.10.2:</p>
<blockquote>
<p>.\Slicer.exe --help<br>
.\Slicer.exe --launch python-real</p>
</blockquote>
<p>Nothing happens, no errors are displayed either.</p>

---

## Post #9 by @lassoan (2020-04-16 18:03 UTC)

<p>It works as intended but I can see how this may be confusing.</p>
<p>In official Slicer releases on Windows, Slicer.exe is not a console application, so you just don’t see the output. It is still there, for example run this instead (<code>more</code> is a console application, so it can display text):</p>
<pre><code>.\Slicer.exe --help | more
</code></pre>
<p>For Python, we included a launcher that is built as a console application. Use that for running Python interactively:</p>
<pre><code>.\SlicerPython.exe</code></pre>

---

## Post #10 by @tbillah (2020-04-16 19:02 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, I am aware of <code>SlicerPython.exe </code>. But that won’t have knowledge of additional settings like <code>Slicer.exe --launch python-real</code> has.</p>
<p>See my use case below:</p>
<blockquote>
<p>C:\Users\tashr\Downloads\“Slicer 4.10.2”\Slicer.exe --launch python-real .\Test\run_test.py</p>
</blockquote>
<p>The above command is the Windows variant of a Linux command minus the <code>.exe</code>, that I would like to run on PowerShell. Let me know if there is a way of doing that.</p>
<p>By the way, I followed your <code>| more</code> idea and the following works fine:</p>
<blockquote>
<p>C:\Users\tashr\Downloads\“Slicer 4.10.2”\Slicer.exe --launch python-real .\Test\run_test.py | more</p>
</blockquote>

---

## Post #11 by @lassoan (2020-04-16 19:22 UTC)

<p>PythonSlicer.exe inherits all launcher settings from Slicer.exe (as you can see it from <code>additionalSettingsFilePath=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/SlicerLauncherSettings.ini</code> line in <code>PythonSlicerLauncherSettings.ini</code>), and it runs <code>python-real.exe</code>. Therefore, <code>Slicer.exe --launch python-real.exe ...args...</code> does exactly the same as <code>PythonSlicer.exe ...args...</code>, the only difference is that one is a console application, while the other is not.</p>
<p>By the way, you can capture output of <code>Slicer.exe</code> by redirecting it to an output file:</p>
<pre><code>Slicer.exe --help &gt;output.txt</code></pre>

---

## Post #12 by @tbillah (2020-04-16 19:33 UTC)

<p>Sorry, I should have mentioned, <code>SlicerPython.exe .\Test\run_test.py</code> did not find one of the SlicerDMRI modules I installed.</p>
<p>I do confirm that the module is found by:</p>
<ul>
<li>Slicer GUI</li>
<li><code>C:\Users\tashr\Downloads\“Slicer 4.10.2”\Slicer.exe --launch python-real .\Test\run_test.py | more</code></li>
</ul>
<p>which is why I am convinced that <code>SlicerPython.exe</code> doesn’t find them.</p>

---

## Post #13 by @lassoan (2020-04-16 19:57 UTC)

<p>SlicerApp-real.exe loads more libraries than python-real.exe, but there should be no difference between if you start python-real.exe when you use Slicer.exe/PythonSlicer.exe launchers.</p>
<p>Can you post the exact Python command that succeeds when executed using <code>Slicer.exe --launch python-real</code> but not when launched using <code>PythonSlicer.exe</code>?</p>

---

## Post #14 by @tbillah (2020-04-16 20:11 UTC)

<p>Does not succeed:</p>
<blockquote>
<p>C:\Users\tashr\Downloads"Slicer 4.10.2"\bin\SlicerPython.exe .\Test\run_test.py</p>
</blockquote>
<p>succeeds:</p>
<blockquote>
<p>C:\Users\tashr\Downloads"Slicer 4.10.2"\Slicer.exe --launch python-real .\Test\run_test.py | more</p>
</blockquote>
<p>Here, I am measuring success in terms of the exec’s ability to find ExtensionModules I installed.</p>
<p>Here is the <a href="https://github.com/pnlbwh/SlicerDiffusionQC/blob/master/Test/run_test.py" rel="noopener nofollow ugc">Test/run_test.py</a> script anyway and <a href="https://github.com/pnlbwh/SlicerDiffusionQC/blob/master/diffusionqclib/diffusionqclib/gradient_process.py#L36" rel="noopener nofollow ugc">this</a> is the line that fails:</p>
<blockquote>
<p>masking_cli = distutils.spawn.find_executable(“DiffusionWeightedVolumeMasking”)</p>
</blockquote>

---

## Post #15 by @lassoan (2020-04-16 20:21 UTC)

<p>When trying to execute:</p>
<pre><code>masking_cli = distutils.spawn.find_executable("DiffusionWeightedVolumeMasking")
</code></pre>
<p>I get this error:</p>
<pre><code>AttributeError: module 'distutils' has no attribute 'spawn'
</code></pre>
<p>Probably Python2/3 issue. Slicer-4.10 will be retired very soon, so I would not spend time with issues that are only reproducible there. Can you provide an example for latest Slicer-4.11?</p>

---

## Post #16 by @tbillah (2020-04-16 20:30 UTC)

<p>Sorry, I have Slicer-4.10 only.</p>
<pre><code class="lang-python">distutils.__version__
'2.7.13'
</code></pre>

---

## Post #17 by @lassoan (2020-04-16 20:32 UTC)

<p>I can only help with issues that I can reproduce in Slicer-4.11. You can install Slicer-4.11 from <a href="http://download.slicer.org">download.slicer.org</a>. If you are still based on Slicer-4.10 then it may be a good time to start transitioning to Slicer-4.11.</p>

---

## Post #19 by @tbillah (2020-04-16 20:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, can you try this?</p>
<pre><code class="lang-python">import distutils.spawn
masking_cli = distutils.spawn.find_executable("DiffusionWeightedVolumeMasking")
</code></pre>

---

## Post #20 by @lassoan (2020-04-16 21:27 UTC)

<p>There is indeed a difference between these (one finds the application, while the other does not):</p>
<pre><code>Slicer.exe --launch python-real.exe -c "import distutils.spawn; print(distutils.spawn.find_executable('DiffusionWeightedVolumeMasking'))" 2&gt;&amp;1 | more

PythonSlicer.exe -c "import distutils.spawn; print(distutils.spawn.find_executable('DiffusionWeightedVolumeMasking'))" 2&gt;&amp;1 | more
</code></pre>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Why Slicer.exe adds extensions to PATH env variable, while PythonSlicer does not?</p>
<pre><code>Slicer.exe --launch python-real.exe -c "import os; print(os.environ['PYTHONPATH'])" 2&gt;&amp;1 | more

PythonSlicer.exe -c "import os; print(os.environ['PYTHONPATH'])" 2&gt;&amp;1 | more</code></pre>

---

## Post #21 by @jcfr (2020-04-16 21:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why Slicer.exe adds extensions to PATH env variable, while PythonSlicer does not?</p>
</blockquote>
</aside>
<p>Because it was not designed to do so. It is currently a wrapper around the standard python interpreter.</p>
<p>To illustrate, here are the associated launcher settings:</p>
<details>
<summary>
PythonSlicerLauncherSettings.ini</summary>
<pre><code class="lang-auto">[General]
launcherNoSplashScreen=true
launcherSplashImagePath=
launcherSplashScreenHideDelayMs=
additionalLauncherHelpShortArgument=
additionalLauncherHelpLongArgument=
additionalLauncherNoSplashArguments=


additionalSettingsFilePath=/home/jcfr/Projects/Slicer-Release/Slicer-build/SlicerLauncherSettings.ini
additionalSettingsExcludeGroups=General,Application,ExtraApplicationToLaunch

[Application]
path=&lt;APPLAUNCHER_DIR&gt;/./python
arguments=
name=PythonSlicer
revision=
organizationDomain=
organizationName=

[ExtraApplicationToLaunch]


[Environment]
additionalPathVariables=PYTHONPATH

[LibraryPaths]
1\path=/home/jcfr/Projects/Slicer-Release/python-install/lib
2\path=/home/jcfr/Projects/Slicer-Release/OpenSSL
size=2

[Paths]
1\path=&lt;APPLAUNCHER_DIR&gt;
size=1

[EnvironmentVariables]
PYTHONHOME=/home/jcfr/Projects/Slicer-Release/python-install
PYTHONNOUSERSITE=1
PIP_REQUIRE_VIRTUALENV=0
SSL_CERT_FILE=&lt;APPLAUNCHER_DIR&gt;/../../Slicer-build/share/Slicer-4.11/Slicer.crt



[PYTHONPATH]
1\path=/home/jcfr/Projects/Slicer-Release/python-install/lib/python3.6
2\path=/home/jcfr/Projects/Slicer-Release/python-install/lib/python3.6/lib-dynload
3\path=/home/jcfr/Projects/Slicer-Release/python-install/lib/python3.6/site-packages
size=3
</code></pre>
</details>
<details>
<summary>
PythonSlicerLauncherSettingsToInstall.ini</summary>
<pre><code class="lang-auto">[General]
launcherNoSplashScreen=true
launcherSplashImagePath=
launcherSplashScreenHideDelayMs=
additionalLauncherHelpShortArgument=
additionalLauncherHelpLongArgument=
additionalLauncherNoSplashArguments=


additionalSettingsFilePath=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/SlicerLauncherSettings.ini
additionalSettingsExcludeGroups=General,Application,ExtraApplicationToLaunch

[Application]
path=&lt;APPLAUNCHER_DIR&gt;/./python-real
arguments=
name=PythonSlicer
revision=
organizationDomain=
organizationName=

[ExtraApplicationToLaunch]


[Environment]
additionalPathVariables=PYTHONPATH

[LibraryPaths]
1\path=&lt;APPLAUNCHER_DIR&gt;/../bin
2\path=&lt;APPLAUNCHER_DIR&gt;/../lib/Slicer-4.11
3\path=&lt;APPLAUNCHER_DIR&gt;/../lib/Python/lib
size=3

[Paths]
1\path=&lt;APPLAUNCHER_DIR&gt;
size=1

[EnvironmentVariables]
PYTHONHOME=&lt;APPLAUNCHER_DIR&gt;/../lib/Python
PYTHONNOUSERSITE=1
PIP_REQUIRE_VIRTUALENV=0
SSL_CERT_FILE=&lt;APPLAUNCHER_DIR&gt;/../share/Slicer-4.11/Slicer.crt



[PYTHONPATH]
1\path=&lt;APPLAUNCHER_DIR&gt;/../lib/Python/lib/Python/lib/python3.6
2\path=&lt;APPLAUNCHER_DIR&gt;/../lib/Python/lib/Python/lib/python3.6/lib-dynload
3\path=&lt;APPLAUNCHER_DIR&gt;/../lib/Python/lib/Python/lib/python3.6/site-packages
4\path=&lt;APPLAUNCHER_DIR&gt;/../bin/Python
size=4
</code></pre>
</details>

---

## Post #23 by @lassoan (2020-04-16 23:12 UTC)

<p>It does not help if I add <code>--launcher-additional-settings "c:/Users/andra/AppData/Local/NA-MIC/Slicer 4.11.0-2020-04-12/bin/SlicerLauncherSettings.ini"</code>, which is not surprising since <code>SlicerPythonLauncherSettings.ini</code> already includes it, see:</p>
<pre><code>additionalSettingsFilePath=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/SlicerLauncherSettings.ini
additionalSettingsExcludeGroups=General,Application,ExtraApplicationToLaunch
</code></pre>
<p>Where do extension paths (such as <code>C:/Users/andra/AppData/Roaming/NA-MIC/Extensions-28946/DiffusionQC/Lib/site-packages</code>) get added to PYTHONPATH?</p>

---

## Post #24 by @tbillah (2020-04-17 13:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, another relevant question, what’s the difference between <code>SlicerPython</code> and <code>PythonSlicer</code> ?<br>
I understand that the <code>PythonInteractor</code> runs <code>PythonSlicer</code> though. On the other hand, when an extension (some python packages) is installed using <code>ExtensionManger</code>, which python has knowledge of the python packages?</p>

---

## Post #25 by @lassoan (2020-04-17 14:36 UTC)

<aside class="quote no-group" data-username="tbillah" data-post="24" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>what’s the difference between <code>SlicerPython</code> and <code>PythonSlicer</code> ?</p>
</blockquote>
</aside>
<p>We had to rename SlicerPython to PythonSlicer, because some Python IDEs (specifically PyCharm, but potentially others) only recognized Python*.exe files as Python interpreters. We have not removed SlicerPython for backward compatibility but eventually it will go away (see <a href="https://github.com/Slicer/Slicer/issues/4843">related issue</a>).</p>
<aside class="quote no-group" data-username="tbillah" data-post="24" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tbillah/48/4139_2.png" class="avatar"> tbillah:</div>
<blockquote>
<p>On the other hand, when an extension (some python packages) is installed using <code>ExtensionManger</code> , which python has knowledge of the python packages?</p>
</blockquote>
</aside>
<p>My understanding is that regardless of which launcher (Slicer.exe or PythonSlicer.exe) executes python-real.exe, extensions should be added to path/pythonpath. However, this does not seem to be the case. <a class="mention" href="/u/jcfr">@jcfr</a> do you know why?</p>
<p>Slicer modules will only be available if you execute SlicerApp-real.exe.</p>

---

## Post #26 by @jcfr (2020-04-17 15:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, this does not seem to be the case. <a class="mention" href="/u/jcfr">@jcfr</a> do you know why?</p>
</blockquote>
</aside>
<p>To ensure it includes the <code>PATH</code> and <code>PYTHONPATHS</code> associated with Slicer extensions are also available, the additional launcher settings for the associated revision of Slicer need to be loaded.</p>
<p>In the Slicer launcher, that mapping is described by the following :</p>
<pre><code class="lang-auto">[Application]
name=Slicer
revision=28975
organizationDomain=www.na-mic.org
organizationName=NA-MIC
</code></pre>
<p>This ensured setting file like <code>/home/jcfr/.config/NA-MIC/Slicer-28975.ini</code> is found by the launcher.</p>
<p>If you manually add a similar section to the settings of <code>PythonSlicer</code>, could you check the extension settings are found ?</p>

---

## Post #27 by @lassoan (2020-04-17 17:26 UTC)

<p>Thanks for the explanation. Adding application name, revision, and organizationName fixes the problem!</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think about adding these lines to PythonSlicer launcher settings so that Python modules, DLLs, and executables provided by extensions can be found when using Slicer’s Python environment? I think these would be useful when using Python IDEs or running batch processing scripts.</p>

---

## Post #28 by @jcfr (2020-05-05 08:00 UTC)

<p>This should be fixed in</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/4912" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/4912" target="_blank">BUG: Ensure PythonSlicer loads extension settings</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jcfr:4603-ensure-python-launcher-load-extensions-settings</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-05" data-time="07:59:55" data-timezone="UTC">07:59AM - 05 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 72 additions and 6 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/4912/files" target="_blank">
          <span class="added">+72</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #29 by @jcfr (2021-11-26 15:32 UTC)

<p>This should now be fixed. Corresponding changes have been integrated.</p>

---

## Post #30 by @Saima (2023-08-15 03:31 UTC)

<p>Dear Andras,<br>
how can we run the slicer python scripted module from the command line?</p>
<p>regards,<br>
Saima</p>

---

## Post #31 by @lassoan (2023-08-15 05:28 UTC)

<p>You can start the application, instantiate its logic class, and call method of that logic object.</p>

---

## Post #32 by @Saima (2023-08-15 06:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="31" data-topic="6481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>n start the application</p>
</blockquote>
</aside>
<p>should i be doing this slicer.exe --python-code “instructions you specified seperated by comma” --no-main-window</p>
<p>regards,<br>
Saima</p>

---

## Post #33 by @Saima (2023-08-16 02:15 UTC)

<p>Hi Andras,<br>
Could you please tell me what is wrong in the below command line</p>
<p>(base) useradmin@DEP59365:/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64$ **</p>
<p>./Slicer --python-code “s=getModuleLogic(‘SurfaceModelNodesSelector’);s.process(”/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/25_manually_picking_points/models")" --no-splash --testing --no-main-window</p>
<p>**<br>
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
File “”, line 1<br>
s=getModuleLogic(‘SurfaceModelNodesSelector’);s.process(/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/25_manually_picking_points/models)<br>
^<br>
SyntaxError: invalid syntax<br>
double free or corruption (!prev)<br>
error: [/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #34 by @Saima (2023-08-16 02:18 UTC)

<p>The module i am trying to run is not a registered module. can I still run using command line??</p>
<p>(base) useradmin@DEP59365:/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64$ ./Slicer --python-code “s=getModuleLogic(‘SurfaceModelNodesSelector’);s.process(‘/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/25_manually_picking_points/models’)” --no-splash --testing --no-main-window<br>
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
The module “SurfaceModelNodesSelector” has not been registered.<br>
The following modules have been registered: (“ACPCTransform”, “AddManyMarkupsFiducialTest”, “AddScalarVolumes”, “Annotations”, “AtlasTests”, “BRAINSDWICleanup”, “BRAINSDeface”, “BRAINSFit”, “BRAINSFitRigidRegistrationCrashIssue4139”, “BRAINSIntensityNormalize”, “BRAINSROIAuto”, “BRAINSResample”, “BRAINSResize”, “BRAINSStripRotation”, “BRAINSTransformConvert”, “Cameras”, “CastScalarVolume”, “CheckerBoardFilter”, “ColorLegendSelfTest”, “Colors”, “CompareVolumes”, “CreateDICOMSeries”, “CropVolume”, “CropVolumeSelfTest”, “CropVolumeSequence”, “CurvatureAnisotropicDiffusion”, “DICOM”, “DICOMEnhancedUSVolumePlugin”, “DICOMGeAbusPlugin”, “DICOMImageSequencePlugin”, “DICOMPatcher”, “DICOMScalarVolumePlugin”, “DICOMSlicerDataBundlePlugin”, “DICOMVolumeSequencePlugin”, “DMRIInstall”, “DWIConvert”, “Data”, “DataProbe”, “Decimation”, “DynamicModeler”, “Endoscopy”, “EventBroker”, “ExecutionModelTour”, “ExtensionWizard”, “ExtractSkeleton”, “FiducialLayoutSwitchBug1914”, “FiducialRegistration”, “GaussianBlurImageFilter”, “GradientAnisotropicDiffusion”, “GrayscaleFillHoleImageFilter”, “GrayscaleGrindPeakImageFilter”, “GrayscaleModelMaker”, “HistogramMatching”, “ImageLabelCombine”, “ImportItkSnapLabel”, “JRC2013Vis”, “LabelMapSmoothing”, “LandmarkRegistration”, “Markups”, “MarkupsInCompareViewersSelfTest”, “MarkupsInViewsSelfTest”, “MaskScalarVolume”, “MedianImageFilter”, “MergeModels”, “ModelMaker”, “ModelToLabelMap”, “Models”, “MultiVolumeExplorer”, “MultiVolumeImporter”, “MultiVolumeImporterPlugin”, “MultiplyScalarVolumes”, “N4ITKBiasFieldCorrection”, “NeurosurgicalPlanningTutorialMarkupsSelfTest”, “OrientScalarVolume”, “PETStandardUptakeValueComputation”, “PerformMetricTest”, “PerformanceTests”, “Plots”, “PlotsSelfTest”, “PluggableMarkupsSelfTest”, “ProbeVolumeWithModel”, “RSNA2012ProstateDemo”, “RSNAQuantTutorial”, “RSNAVisTutorial”, “Reformat”, “ResampleDTIVolume”, “ResampleScalarVectorDWIVolume”, “ResampleScalarVolume”, “RobustStatisticsSegmenter”, “SampleData”, “ScenePerformance”, “SceneViews”, “ScreenCapture”, “SegmentEditor”, “SegmentStatistics”, “Segmentations”, “SelfTests”, “Sequences”, “ShaderProperties”, “SimpleFilters”, “SimpleRegionGrowingSegmentation”, “SliceLinkLogic”, “Slicer4Minute”, “SlicerBoundsTest”, “SlicerMRBMultipleSaveRestoreLoopTest”, “SlicerMRBMultipleSaveRestoreTest”, “SlicerMRBSaveRestoreCheckPathsTest”, “SlicerOrientationSelectorTest”, “SlicerScriptedFileReaderWriterTest”, “SlicerTransformInteractionTest1”, “SubjectHierarchy”, “SubjectHierarchyCorePluginsSelfTest”, “SubjectHierarchyGenericSelfTest”, “SubtractScalarVolumes”, “SurfaceToolbox”, “Tables”, “TablesSelfTest”, “Terminologies”, “Texts”, “ThresholdScalarVolume”, “Transforms”, “Units”, “UtilTest”, “VectorToScalarVolume”, “ViewControllers”, “ViewControllersSliceInterpolationBug1926”, “VolumeRendering”, “VolumeRenderingSceneClose”, “Volumes”, “VotingBinaryHoleFillingImageFilter”, “WebEngine”, “WebServer”, “Welcome”, “sceneImport2428”)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/Python/slicer/util.py”, line 1275, in getModuleLogic<br>
module = getModule(module)<br>
File “/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/Python/slicer/util.py”, line 1196, in getModule<br>
raise RuntimeError(“Could not find module with name ‘%s’” % moduleName)<br>
RuntimeError: Could not find module with name ‘SurfaceModelNodesSelector’<br>
double free or corruption (!prev)<br>
error: [/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #35 by @lassoan (2023-08-16 12:07 UTC)

<p>You need to use <code>"</code> for marking the start and end of the Python code in the command-line argument list, therefore you can only use <code>'</code> in the python code. The fix is to replace all <code>"</code> by <code>'</code> in the Python code that you pass via the command-line argument.</p>

---

## Post #36 by @Saima (2023-08-17 01:21 UTC)

<p>I did what you recommended and have the following:</p>
<p>The module i am trying to run is not a registered module. can I still run using command line??</p>
<p>(base) useradmin@DEP59365:/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64$ ./Slicer --python-code “s=getModuleLogic(‘SurfaceModelNodesSelector’);s.process(‘/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/25_manually_picking_points/models’)” --no-splash --testing --no-main-window<br>
qSlicerMarkupsModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
qSlicerSequencesModulePrivate::addToolBar: no main window is available, toolbar is not added<br>
The module “SurfaceModelNodesSelector” has not been registered.<br>
The following modules have been registered: (“ACPCTransform”, “AddManyMarkupsFiducialTest”, “AddScalarVolumes”, “Annotations”, “AtlasTests”, “BRAINSDWICleanup”, “BRAINSDeface”, “BRAINSFit”, “BRAINSFitRigidRegistrationCrashIssue4139”, “BRAINSIntensityNormalize”, “BRAINSROIAuto”, “BRAINSResample”, “BRAINSResize”, “BRAINSStripRotation”, “BRAINSTransformConvert”, “Cameras”, “CastScalarVolume”, “CheckerBoardFilter”, “ColorLegendSelfTest”, “Colors”, “CompareVolumes”, “CreateDICOMSeries”, “CropVolume”, “CropVolumeSelfTest”, “CropVolumeSequence”, “CurvatureAnisotropicDiffusion”, “DICOM”, “DICOMEnhancedUSVolumePlugin”, “DICOMGeAbusPlugin”, “DICOMImageSequencePlugin”, “DICOMPatcher”, “DICOMScalarVolumePlugin”, “DICOMSlicerDataBundlePlugin”, “DICOMVolumeSequencePlugin”, “DMRIInstall”, “DWIConvert”, “Data”, “DataProbe”, “Decimation”, “DynamicModeler”, “Endoscopy”, “EventBroker”, “ExecutionModelTour”, “ExtensionWizard”, “ExtractSkeleton”, “FiducialLayoutSwitchBug1914”, “FiducialRegistration”, “GaussianBlurImageFilter”, “GradientAnisotropicDiffusion”, “GrayscaleFillHoleImageFilter”, “GrayscaleGrindPeakImageFilter”, “GrayscaleModelMaker”, “HistogramMatching”, “ImageLabelCombine”, “ImportItkSnapLabel”, “JRC2013Vis”, “LabelMapSmoothing”, “LandmarkRegistration”, “Markups”, “MarkupsInCompareViewersSelfTest”, “MarkupsInViewsSelfTest”, “MaskScalarVolume”, “MedianImageFilter”, “MergeModels”, “ModelMaker”, “ModelToLabelMap”, “Models”, “MultiVolumeExplorer”, “MultiVolumeImporter”, “MultiVolumeImporterPlugin”, “MultiplyScalarVolumes”, “N4ITKBiasFieldCorrection”, “NeurosurgicalPlanningTutorialMarkupsSelfTest”, “OrientScalarVolume”, “PETStandardUptakeValueComputation”, “PerformMetricTest”, “PerformanceTests”, “Plots”, “PlotsSelfTest”, “PluggableMarkupsSelfTest”, “ProbeVolumeWithModel”, “RSNA2012ProstateDemo”, “RSNAQuantTutorial”, “RSNAVisTutorial”, “Reformat”, “ResampleDTIVolume”, “ResampleScalarVectorDWIVolume”, “ResampleScalarVolume”, “RobustStatisticsSegmenter”, “SampleData”, “ScenePerformance”, “SceneViews”, “ScreenCapture”, “SegmentEditor”, “SegmentStatistics”, “Segmentations”, “SelfTests”, “Sequences”, “ShaderProperties”, “SimpleFilters”, “SimpleRegionGrowingSegmentation”, “SliceLinkLogic”, “Slicer4Minute”, “SlicerBoundsTest”, “SlicerMRBMultipleSaveRestoreLoopTest”, “SlicerMRBMultipleSaveRestoreTest”, “SlicerMRBSaveRestoreCheckPathsTest”, “SlicerOrientationSelectorTest”, “SlicerScriptedFileReaderWriterTest”, “SlicerTransformInteractionTest1”, “SubjectHierarchy”, “SubjectHierarchyCorePluginsSelfTest”, “SubjectHierarchyGenericSelfTest”, “SubtractScalarVolumes”, “SurfaceToolbox”, “Tables”, “TablesSelfTest”, “Terminologies”, “Texts”, “ThresholdScalarVolume”, “Transforms”, “Units”, “UtilTest”, “VectorToScalarVolume”, “ViewControllers”, “ViewControllersSliceInterpolationBug1926”, “VolumeRendering”, “VolumeRenderingSceneClose”, “Volumes”, “VotingBinaryHoleFillingImageFilter”, “WebEngine”, “WebServer”, “Welcome”, “sceneImport2428”)<br>
Traceback (most recent call last):<br>
File “”, line 1, in<br>
File “/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/Python/slicer/util.py”, line 1275, in getModuleLogic<br>
module = getModule(module)<br>
File “/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/Python/slicer/util.py”, line 1196, in getModule<br>
raise RuntimeError(“Could not find module with name ‘%s’” % moduleName)<br>
RuntimeError: Could not find module with name ‘SurfaceModelNodesSelector’<br>
double free or corruption (!prev)<br>
error: [/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #37 by @lassoan (2023-08-17 12:58 UTC)

<p>You can only use modules that are loaded. You can add the module to the additional module paths before launching Slicer or you can run a Python script instead of calling methods of a Python-scripted module (using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#run-a-python-script-file-in-the-slicer-environment"><code>--python-script /path/to/myscript.py</code></a>).</p>

---

## Post #38 by @William_Kuo (2024-02-20 01:16 UTC)

<p>Hi!<br>
I am having the same issue.</p>
<p>The first script does not works:<br>
slicerCommand = r"Slicer.exe --python-script {} --no-splash --no-main-window".format(slicerScript)</p>
<p>The second script works:<br>
slicerCommand = r"Slicer.exe --python-script {}".format(slicerScript)</p>
<p>I input these commands into os.system()<br>
I process segmentations and export stl with these scripts. I can see the result of my processing with the second script through an stl output, but I don’t see it with the first script, no stl file is outputted.</p>
<p>The only difference is that my slicer script is ran without a GUI, which is substantially faster. This is relevant because I work with large datasets and my focus is on automating and accelerating a pipeline.</p>

---

## Post #39 by @lassoan (2024-02-24 02:35 UTC)

<p>You will not have access to many Slicer functions that are related to the GUI if you disable the main window. To make batch orocessing faster, I would recommend to laun h several Slicer instances (as many as your computer can handle) and run many commands on it (e.g., if you need to process 2000 patient data then don’t start a new Slicer instance for each but process 100 patients before restarting Slicer). You can use SlicerWeb module to send commands to an already running Slicer.</p>

---

## Post #40 by @ckolluru (2024-03-15 16:36 UTC)

<p>I probably have a similar issue. When I run the following command:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
</code></pre>
<p>It works fine in the python console of Slicer application. However, running it with the -no-main-window option returns a <code>NoneType</code> object for <code>layoutManager</code>. Is there a workaround?</p>

---

## Post #41 by @pieper (2024-03-15 16:43 UTC)

<p>If there’s no mainWindow, there will be no threeDWidget either.</p>
<p>Maybe you want something like this:</p>
<pre><code class="lang-auto">Slicer --python-code "slicer.util.mainWindow().hide(); print(slicer.app.layoutManager().threeDWidget(0))"
</code></pre>
<p>where the main window is offscreen.  You should still be able to render and screen grab from the widget, but you’ll need to test as the behavior may not be defined across platforms.</p>

---

## Post #42 by @ckolluru (2024-03-15 17:01 UTC)

<p>Thank you. I think this should work.</p>

---
