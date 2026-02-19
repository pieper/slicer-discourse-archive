---
topic_id: 7078
title: "Automatic Install Of Python Packages"
date: 2019-06-07
url: https://discourse.slicer.org/t/7078
---

# Automatic install of Python packages

**Topic ID**: 7078
**Date**: 2019-06-07
**URL**: https://discourse.slicer.org/t/automatic-install-of-python-packages/7078

---

## Post #1 by @smrolfe (2019-06-07 23:33 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/python3-switch-and-python-package-install/6534/2">Python3 switch and python package install</a>:</p>
<p>Are there any updates on the automatic installation of Python packages required by extensions? The packages we’d like to use can be installed manually, but the user needs admin privileges.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jcfr">@jcfr</a>, do you know if automatic installation is likely to be available sometime soon? Thanks!</p>

---

## Post #2 by @jcfr (2019-06-08 00:50 UTC)

<blockquote>
<p>do you know if automatic installation is likely to be available sometime soon?</p>
</blockquote>
<p>To put things in  context, are these packages you would like to have available after the user install <a href="https://github.com/SlicerMorph/SlicerMorph/">SlicerMorph</a> extension ?</p>

---

## Post #3 by @smrolfe (2019-06-08 04:31 UTC)

<p>Yes, thanks. For example, we plan to provide sample scripts to manipulate our module’s data output and would like to use the Pandas package in the scripts. It would be very convenient if we could have this package automatically downloaded with our extension.</p>

---

## Post #4 by @pieper (2019-06-08 19:46 UTC)

<p>On mac (and probably linux) this works:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import os
&gt;&gt;&gt; os.system('PythonSlicer -m pip install pandas')
0
&gt;&gt;&gt; import pandas
</code></pre>
<p>On windows, this process pops up the access control permission dialog:</p>
<pre><code class="lang-auto">import os
os.system('powershell.exe Start-Process cmd.exe -Verb runAs')
</code></pre>
<p>And then in the shell I could run this:</p>
<pre><code class="lang-auto">"c:\Program Files\Slicer 4.11.0-2019-06-02\bin\PythonSlicer.exe" -m pip install pandas
</code></pre>
<p>We should be able to streamline this and integrate it with the extension install process.</p>
<p>We discussed this on the developer call the other day and were thinking we should start collecting this information along with guidelines about which python packages should work and which might cause trouble.</p>

---

## Post #5 by @lassoan (2019-06-08 19:54 UTC)

<p>We plan to add a <code>slicer.util.pip</code> command that launches pip as admin (displays UAC popup) on Windows.</p>
<p>We could also add some higher-level helper function that would ask user confirmation in a popup before installing anything, explain what version of what package will be installed, and could display errors, etc.</p>

---

## Post #6 by @muratmaga (2019-06-09 07:41 UTC)

<p>So both of these answers assume user have admin rights?</p>

---

## Post #7 by @lassoan (2019-06-09 12:20 UTC)

<p>If Slicer is installed to a folder that requires admin rights then yes, currently you need admin rights to install Python packages. If this is a problem then there are many way to address this.</p>
<p>We can change Slicer install location to be in the user’s folder (e.g., AppData) instead of the shared “Program Files” folder. We could also allow users to choose the folder. This should be very easy (modification of a few lines).</p>
<p>We could try to make pip manage packages in two folders (core packages pre-installed with Slicer in “Program Files” and additional packages installed by extensions in user’s folder). We would do something unusual, so it may be hard to implement and maintain this solution.</p>
<p>We could install all extensions to the user’s folder. Probably we would need to copy core extensions from the Slicer core folder in Program Files on or before starting Slicer the first time. If would not be a very simple mechanism, but it could allow sharing a single Slicer installation to be used by multiple Python environments and it would be possible to reset the default environment (because it is stored in a read-only location).</p>

---

## Post #8 by @muratmaga (2019-06-10 01:39 UTC)

<p>I think modifying the windows installer would be a good place to start. I just tried installing with a normal user account, and once UAC pop ups, it asks me for an admin account password. Hitting the cancel button, cancels the whole installation process. Instead, the behavior should be asking whether they want to install to their user space or somewhere else where admin rights is not required.</p>
<p>The whole getting the updates through new preview installs is really challenging to coordinate in corporate networks…</p>

---

## Post #9 by @jcfr (2019-06-10 13:29 UTC)

<p>It should be possible to ask if Slicer should be installed for all users or the current user.</p>
<p>If we put some work in the installer, it may be worth revisiting the use of NSIS and instead look at WIX.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>two folders (core packages pre-installed with Slicer in “Program Files” and additional packages installed by extensions in user’s folder). We would do something unusual, so it may be hard to implement and maintain this solution.</p>
</blockquote>
</aside>
<p>This makes me think of what is done with virtualenv. That said, you are right it may be more cumbersome to implement</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="7078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could install all extensions to the user’s folder.</p>
</blockquote>
</aside>
<p>On windows and Linux, this is already the case. Extensions are installed in the user folder.</p>

---

## Post #10 by @lassoan (2019-06-11 13:15 UTC)

<p>I’ve submitted a <a href="https://github.com/Slicer/Slicer/pull/1151/files" rel="nofollow noopener">pull request</a> to change the default install location to AppData (c:\Users&lt;username&gt;\AppData\Local) and turned off requirement for an admin account.</p>
<p>Installing in user-specific folder may be a good thing, because then installing random Python packages would not impact other users.</p>
<p>The only drawback I can think of is that after this change it will be a bit more work to create an installation tree shared between all users on that computer. However, it is not that difficult to do: you need to manually select All Users\AppData as installation folder and move the start menu shortcuts to All Users\Start menu. We can just add these instructions to the documentation.</p>

---

## Post #11 by @Sam_Horvath (2019-06-11 13:35 UTC)

<p>Also, as an FYI, we are planning to work on the slicer.util.pip functionality and the automatic install of packages for extensions during the upcoming project week.</p>

---

## Post #12 by @muratmaga (2019-06-11 14:50 UTC)

<p>Would the same slicer installation be usable by other other user accounts if the default it c:\Users&lt;username&gt;? I thought those folders are specific to the user, unless explicitly allowed.</p>
<p>Perhaps you can let user manually choose a folder that they can write to (e.g., c:\Slicer-4.11) which then can be shared by other users of the same computer?</p>

---

## Post #13 by @jamesobutler (2019-06-11 15:07 UTC)

<p>Visual Studio Code has a User Installer and a System Installer for <a href="https://code.visualstudio.com/download" rel="noopener nofollow ugc">download</a>. I know this program does this to allow easier frequent updates using the user install.</p>
<blockquote>
<p>VS Code provides both Windows user and system level setups. Installing the user setup does not require Administrator privileges as the location will be under your user Local AppData (LOCALAPPDATA) folder. User setup also provides a smoother background update experience.</p>
<p>The system setup requires elevation to Administrator privileges and will place the installation under Program Files.</p>
</blockquote>
<p><a href="https://code.visualstudio.com/docs/setup/windows#_user-versus-system-setup" rel="noopener nofollow ugc">source</a></p>

---

## Post #14 by @lassoan (2019-06-11 15:53 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="7078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would the same slicer installation be usable by other other user accounts</p>
</blockquote>
</aside>
<p>Yes, everything is still doable (see my post <a href="https://discourse.slicer.org/t/automatic-install-of-python-packages/7078/10">above</a>). However, we need to choose between which of these use cases we want to support by default:</p>
<ul>
<li>A. User (does not need to be administrator) installs Slicer and any extensions.</li>
<li>B. Knowledgeable administrator sets up Slicer and all necessary extensions for all users on a shared computer.</li>
</ul>
<p>Since use case A is much more common, I think we should make that easy for users, and let experts deal with the few required extra steps needed for a shared installation.</p>
<p>We could create two installers as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> suggested above, but I am not sure if it is worth the extra effort (it would impact packaging and release download infrastructure, lead to more questions from users, etc.).</p>

---

## Post #15 by @lassoan (2019-06-12 14:01 UTC)

<p>I’ve integrated the <a href="https://github.com/Slicer/Slicer/commit/25eea0d87aa41bf09097514262c2c1e450aae05a" rel="nofollow noopener">change</a>, from tomorrow, Slicer-4.11 install will note require admin rights on Windows and Python packages can be installed as regular user.</p>
<p>Slicer install tree can be accessed as <code>%LOCALAPPDATA%\NA-MIC</code> (usually it resolves to something like <code>C:\Users\&lt;username&gt;\AppData\Local\NA-MIC</code>).</p>
<p>Previous behavior (install to Program Files, require admin privileges) can be restored by adjusting <code>Slicer_CPACK_NSIS_INSTALL_ROOT</code> and <code>Slicer_CPACK_NSIS_INSTALL_REQUIRES_ADMIN_ACCOUNT</code> variables when configuring Slicer build).</p>

---

## Post #16 by @lassoan (2019-06-12 22:26 UTC)

<p>I went ahead and <a href="https://github.com/Slicer/Slicer/commit/b26a7eefc2813d04bd1005be6dd6ccc41984154a">added a slicer.util.pip_install function</a> because <a class="mention" href="/u/ungi">@ungi</a> will give a Slicer tutorial at CARS conference next week where he needs to walk through participants installing Python packages, and typing <code>pip_install("tensorflow")</code> in Slicer is much easier than locating Slicer’s Python, start a command terminal there, and type <code>PythonSlicer.exe -m pip install tensorflow</code>. We can refine the syntax and add features later.</p>

---
