# On Ubuntu 22.04, it is not possible to install extensions using either stable or preview build

**Topic ID**: 23819
**Date**: 2022-06-10
**URL**: https://discourse.slicer.org/t/on-ubuntu-22-04-it-is-not-possible-to-install-extensions-using-either-stable-or-preview-build/23819

---

## Post #1 by @Michel_Atieh (2022-06-10 21:47 UTC)

<p>Problem report for Slicer 5.0.2 linux-amd64: [please describe expected and actual behavior]</p>
<p>Hello, I just installed 3D Slicer and am getting the following error. The main issue that I’m having is that I can’t download any extensions, and I can’t even see any that are available for download. I’m using Ubuntu 22.04 LTS Linux as my operating system. Thank you in advance for your support.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Session start time .......: 2022-06-10 23:34:02
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Slicer version ...........: 5.0.2 (revision 30822 / a4420c3) linux-amd64 - installed release
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Operating system .........: Linux / 5.15.0-37-generic / #39-Ubuntu SMP Wed Jun 1 19:16:45 UTC 2022 / UTF-8 - 64-bit
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Memory ...................: 31790 MB physical, 2047 MB virtual
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - CPU ......................: GenuineIntel 12th Gen Intel(R) Core(TM) i7-12700H, 14 cores, 20 logical processors
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Application path .........: /home/michel_atieh/Slicer-5.0.2-linux-amd64/bin
[DEBUG][Qt] 10.06.2022 23:34:02 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 10.06.2022 23:34:06 [Python] (/home/michel_atieh/Slicer-5.0.2-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 10.06.2022 23:34:07 [Python] (/home/michel_atieh/Slicer-5.0.2-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 10.06.2022 23:34:07 [Python] (/home/michel_atieh/Slicer-5.0.2-linux-amd64/lib/Slicer-5.0/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 10.06.2022 23:34:07 [] (unknown:0) - Switch to module:  "Welcome"
[WARNING][Qt] 10.06.2022 23:34:11 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03a82a6dc785a2e98e11dac963b2b1188c24555b.png" data-download-href="/uploads/short-url/wlJ08AFHrMiEqulu7aQ1DBiMLp.png?dl=1" title="bug" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03a82a6dc785a2e98e11dac963b2b1188c24555b_2_690x403.png" alt="bug" data-base62-sha1="wlJ08AFHrMiEqulu7aQ1DBiMLp" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03a82a6dc785a2e98e11dac963b2b1188c24555b_2_690x403.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03a82a6dc785a2e98e11dac963b2b1188c24555b_2_1035x604.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03a82a6dc785a2e98e11dac963b2b1188c24555b_2_1380x806.png 2x" data-dominant-color="3D3E3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bug</span><span class="informations">1840×1076 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2022-06-10 22:21 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Waiting this is addressed, you should be able to download the extension archive from <a href="https://extensions.slicer.org/catalog/All/30822/linux">https://extensions.slicer.org/catalog/All/30822/linux</a> and <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-downloaded-extension-packages">install the extension package from file</a></p>
<p>I was able to reproduce this using the following steps:</p>
<ul>
<li>Install virtual box</li>
<li>Download <code>ubuntu-22.04-desktop-amd64.iso</code> available at <a href="https://releases.ubuntu.com/22.04/" class="inline-onebox">Ubuntu 22.04 LTS (Jammy Jellyfish)</a>
</li>
<li>Follow these instructions to create the virtual box machine: <a href="https://linuxhint.com/install-ubuntu22-04-virtual-box/" class="inline-onebox">How to Install Ubuntu 22.04 on VirtualBox</a>
</li>
<li>Run Ubuntu selecting “Try Ubuntu”</li>
<li>Install prerequisites: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux</a><pre><code class="lang-auto">sudo apt-get install libpulse-dev libnss3 libglu1-mesa
sudo apt-get install --reinstall libxcb-xinerama0
</code></pre>
</li>
<li>Download package from: <a href="https://download.slicer.org/">https://download.slicer.org/</a>
</li>
<li>Extract the archive and <code>Slicer</code>
</li>
</ul>

---

## Post #4 by @jcfr (2022-06-10 22:29 UTC)

<p>Reading the  section <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions"> Extensions Manager / Troubleshooting / Extensions manager does not show any extensions</a>, and trying to execute Slicer after setting the environment variable <code>QTWEBENGINE_DISABLE_SANDBOX</code>, I was able to install extensions.</p>
<pre><code class="lang-auto">QTWEBENGINE_DISABLE_SANDBOX=1 ./Slicer-5.0.2-linux-amd64/Slicer
</code></pre>
<p>or</p>
<pre><code class="lang-auto">export QTWEBENGINE_DISABLE_SANDBOX=1
./Slicer-5.0.2-linux-amd64/Slicer
</code></pre>
<p><a class="mention" href="/u/michel_atieh">@Michel_Atieh</a>  Could you try this approach and report back ?</p>
<p>To make the change permanent to your install of Slicer, consider editing</p>
<pre><code class="lang-auto">/Slicer-5.0.2-linux-amd64/bin/SlicerLauncherSettings.ini
</code></pre>
<p>and adding the environment variable to the <code>[EnvironmentVariables]</code> section.</p>
<pre><code class="lang-diff">[EnvironmentVariables]
SLICER_HOME=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/..
ITK_AUTOLOAD_PATH=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Slicer-5.0/ITKFactories
PIP_REQUIRE_VIRTUALENV=0
SSL_CERT_FILE=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../share/Slicer-5.0/Slicer.crt
PYTHONHOME=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/Python
PYTHONNOUSERSITE=1
+QTWEBENGINE_DISABLE_SANDBOX=1

[QT_PLUGIN_PATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/../lib/QtPlugins
size=1
</code></pre>

---

## Post #5 by @Michel_Atieh (2022-06-11 09:17 UTC)

<p>Hello Jean Christophe,<br>
Thank you very much for your fast response.<br>
I believe your explanation is a little complex for me; could you please simplify it? if possible, write me the steps with what to write, and where to write it.<br>
If you think I’m asking too much, I understand; just let me know when the next stable version of 3D Slicer with this bug fixed is available, and I’ll continue to use 3D Slicer on Windows in the meantime.<br>
Thank you again.</p>

---

## Post #6 by @lassoan (2022-06-11 20:29 UTC)

<aside class="quote no-group" data-username="Michel_Atieh" data-post="5" data-topic="23819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar"> Michel_Atieh:</div>
<blockquote>
<p>if possible, write me the steps with what to write, and where to write it.</p>
</blockquote>
</aside>
<p>I believe <a class="mention" href="/u/jcfr">@jcfr</a> meant that you need to set an environment variable before you run Slicer. You can either edit the <code>SlicerLauncherSettings.ini</code> file as described above or type this into the shell to start Slicer:</p>
<pre><code class="lang-plaintext">export QTWEBENGINE_DISABLE_SANDBOX=1
./Slicer
</code></pre>
<aside class="quote no-group" data-username="Michel_Atieh" data-post="5" data-topic="23819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar"> Michel_Atieh:</div>
<blockquote>
<p>I believe your explanation is a little complex for me; could you please simplify it?</p>
</blockquote>
</aside>
<p>There is such enormous variability across different linux systems and therefore so many potential compatibility issues that users must be experienced in administering their own system, installing various packages, configuring them, adjusting system settings, environment variables, building components from source code, etc. If you are not comfortable learning all these then you might consider using Windows or macOS operating system instead, which do not have such incompatibility issues.</p>

---

## Post #7 by @Michel_Atieh (2022-06-11 21:46 UTC)

<p>Hello Andras, the problem was resolved when I wrote this command<br>
export QTWEBENGINE_DISABLE_SANDBOX=1<br>
./Slicer</p>
<p>I appreciate your response.<br>
Is it something that could be fixed for all users, or is it something particular to my case?</p>

---

## Post #8 by @lassoan (2022-06-11 23:03 UTC)

<aside class="quote no-group" data-username="Michel_Atieh" data-post="7" data-topic="23819">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar"> Michel_Atieh:</div>
<blockquote>
<p>Is it something that could be fixed for all users, or is it something particular to my case?</p>
</blockquote>
</aside>
<p>The problem may be that you are logged in as a root user (because Chromium does not support sandboxing for root users).</p>
<p>We could disable sandboxing for everyone, which would solve this issue, but that would make the system slightly more vulnerable to malicious websites. Since the browser only opens <a href="http://extensions.slicer.org">extensions.slicer.org</a> site, the chance of getting malicious content is very low. Probably the highest risk (but overall still very low risk) is displaying the extension logo images, which are downloaded from external URLs.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think? Should we disable the sandbox? Or could we somehow detect this issue and ask permission from the user to disable the sandbox?</p>

---

## Post #9 by @rkikinis (2022-06-12 00:14 UTC)

<p>Security is good even if sometimes inconvenient</p>
<p>Giving the user the option after explaining seems to me like a good way to go</p>

---

## Post #10 by @S_Chakraborty (2023-01-13 17:26 UTC)

<p>Thank you this helped solve the issue in my Ubuntu 22.10 install of Slicer 5.2.1.<br>
I was able to edit the .ini file as instructed and now the extension manager is showing extensions correctly.</p>

---

## Post #11 by @RafaelPalomar (2023-01-14 02:54 UTC)

<p>It is worth mentioning that this issue was recently solved by adding <code>QTWEBENGINE_DISABLE_SANDBOX=1</code> to the Slicer environment on GNU/Linux (available now on preview release)</p>

---
