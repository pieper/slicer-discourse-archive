# Slicer on WSL2 exited when opening Extension Manager

**Topic ID**: 37133
**Date**: 2024-07-01
**URL**: https://discourse.slicer.org/t/slicer-on-wsl2-exited-when-opening-extension-manager/37133

---

## Post #1 by @chz31 (2024-07-01 21:42 UTC)

<p>I’m trying to run Slicer 5.6.2 on WSL2 Ubuntu 22.04. It was installed using <code>tar xzvf</code>. However, whenever I tried to open Extension Manager, Slicer just crashed. Does Slicer not support WSL2 or should I build it instead? Thanks!</p>
<p>Here is the message printed out on the terminal when I opened a Slicer:</p>
<pre><code class="lang-auto">Switch to module:  "Welcome"
Sandboxing disabled by user.
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.
error: [/home/chz31/Slicer-5.6.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @muratmaga (2024-07-01 22:01 UTC)

<p>Chi,<br>
Running Slicer over WSL2 is not a very good experience. Is there a specific reason you want to do that? In fact if you do have to use WSL2, probably it would be better to use a dockerized version (i.e., run docker from WSL2).</p>
<p>As for the error, it is complaining about openGl. Did you make sure you install the proper WSL2/CUDA driver to support 3D graphics? I only managed to do that with recent Nvidia GPUs. This might help some: <a href="https://docs.nvidia.com/cuda/wsl-user-guide/index.html" class="inline-onebox">CUDA on WSL</a></p>

---

## Post #3 by @chz31 (2024-07-01 22:11 UTC)

<p>Thanks, Murat! You are probably right. Rendering did not use the GPU.</p>
<p>I did not have access to Linux currently and was not sure if my old gaming laptop was compatible with Ubuntu, so I tested it in WSL2. I should probably try JetStream.</p>
<p>I believe I had the driver properly installed. WSL2 actually just used the Nvidia driver installed on Windows. I could install cuda toolkit in WSL2 and trained a deep learning model using the GPU (I used nerfstudio to run our photogrammetry data. I could not figure out how to export a proper 3D model though).</p>
<p>I forgot to attach the error log. It probably did not tell anything useful:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Session start time .......: 20240701_170305
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) linux-amd64 - installed release
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Operating system .........: Linux / 5.15.153.1-microsoft-standard-WSL2 / #1 SMP Fri Mar 29 23:14:13 UTC 2024 / UTF-8 - 64-bit
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Memory ...................: 7867 MB physical, 2048 MB virtual
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz, 6 cores, 12 logical processors
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Application path .........: /home/chz31/Slicer-5.6.2-linux-amd64/bin
[DEBUG][Qt] 01.07.2024 17:03:05 [] (unknown:0) - Additional module paths ..: /home/chz31/extensions/SlicerMorph/SkyscanReconImport, /home/chz31/extensions/SlicerMorph/MeshDistanceMeasurement, /home/chz31/extensions/SlicerMorph/ImportSurfaceToSegment, /home/chz31/extensions/SlicerMorph/SlicerMorphSampleData, /home/chz31/extensions/SlicerMorph/Animator, /home/chz31/extensions/SlicerMorph/MarkupEditor, /home/chz31/extensions/SlicerMorph/ImportFromURL, /home/chz31/extensions/SlicerMorph/MorphologikaLMConverter, /home/chz31/extensions/SlicerMorph/ExportAs, /home/chz31/extensions/SlicerMorph/GPA, /home/chz31/extensions/SlicerMorph/VolumeToModel, /home/chz31/extensions/SlicerMorph/IDAVLMConverter, /home/chz31/extensions/SlicerMorph/MorphoSourceImport, /home/chz31/extensions/SlicerMorph/ProjectSemiLM, /home/chz31/extensions/SlicerMorph/ExportMorphoJLandmarkFile, /home/chz31/extensions/SlicerMorph/ALPACA, /home/chz31/extensions/SlicerMorph/CreateSemiLMPatches, /home/chz31/extensions/SlicerMorph/SegmentEndocranium, /home/chz31/extensions/SlicerMorph/FastModelAlign, /home/chz31/extensions/SlicerMorph/OBJFile, /home/chz31/extensions/SlicerMorph/ImageStacks, /home/chz31/extensions/SlicerMorph/QuickAlign, /home/chz31/extensions/SlicerMorph/FormatMarkups, /home/chz31/extensions/SlicerMorph/HiResScreenCapture, /home/chz31/extensions/SlicerMorph/PseudoLMGenerator, /home/chz31/extensions/SlicerMorph/MorphPreferences, /home/chz31/extensions/SlicerMorph/GEVolImport, /home/chz31/extensions/SlicerMorph/PlaceSemiLMPatches, /home/chz31/extensions/SlicerMorph/MergeMarkups
[WARNING][Qt] 01.07.2024 17:03:12 [] (unknown:0) - libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[WARNING][Qt] 01.07.2024 17:03:12 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 01.07.2024 17:03:13 [Python] (/home/chz31/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 01.07.2024 17:03:13 [Python] (/home/chz31/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 01.07.2024 17:03:13 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Python] 01.07.2024 17:03:14 [Python] (/home/chz31/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: ExportAs
[DEBUG][Python] 01.07.2024 17:03:14 [Python] (/home/chz31/Slicer-5.6.2-linux-amd64/lib/Slicer-5.6/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: FormatMarkups
[INFO][Python] 01.07.2024 17:03:14 [Python] (&lt;string&gt;:3) - Adding SlicerMorph Volume Rendering Presets
</code></pre>

---

## Post #4 by @muratmaga (2024-07-02 05:37 UTC)

<p>Maybe try this and see if other less complex GUI applications launch?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/microsoft/wslg">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/microsoft/wslg" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/0f804cf009a245d3f9da3fadbadef1a8f7cedb6ac6a77f3604e6dcd29dbc02dc/microsoft/wslg" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/microsoft/wslg" target="_blank" rel="noopener">GitHub - microsoft/wslg: Enabling the Windows Subsystem for Linux to include...</a></h3>

  <p>Enabling the Windows Subsystem for Linux to include support for Wayland and X server related scenarios - microsoft/wslg</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2024-07-04 15:54 UTC)

<p>The Extension Manager uses Chromium to let users browse the Extensions Catalog website. Maybe Chromium has some issues on WSL2.</p>
<p>Can you try if you can use Google Chrome browser (that is also based on Chromium) in your WSL2?</p>

---

## Post #6 by @chz31 (2024-07-05 17:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Sorry for the late response. I might mess my WSL2 up when I reinstall a different version of cudatoolkit. I somehow could not install Chrome. I’ll reinstall WSL2 and post the update soon.</p>

---

## Post #7 by @chz31 (2024-07-05 23:35 UTC)

<p>Sorry for the late response. I could install and open Google Chrome browser in WSL2, but somehow Slicer still exited whenever I opened Extension Manager.</p>

---

## Post #8 by @muratmaga (2024-07-06 00:30 UTC)

<p>Did you apt install the required packages for Slicer?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#ubuntu-22-04-jammy-jellyfish-20-04-focal-fossa-debian-12-bookworm-debian-11-bullseye-debian-10-buster" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#ubuntu-22-04-jammy-jellyfish-20-04-focal-fossa-debian-12-bookworm-debian-11-bullseye-debian-10-buster</a></p>

---

## Post #9 by @chz31 (2024-07-06 00:59 UTC)

<p>Yes, I did that by running <code>sudo apt-get install libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2 qt5dxcb-plugin libsm6</code> for Ubuntu 22.04, which is the version for WSL2.</p>
<p>I can install extensions via Extension Wizard, though. I would say it might be a Chromium issue in WSL2.</p>

---

## Post #10 by @muratmaga (2024-07-06 02:43 UTC)

<aside class="quote no-group" data-username="chz31" data-post="9" data-topic="37133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chz31/48/77363_2.png" class="avatar"> chz31:</div>
<blockquote>
<p>I can install extensions via Extension Wizard, though. I would say it might be a Chromium issue in WSL2.</p>
</blockquote>
</aside>
<p>You can probably try to install chromium in wsl2 and test that: <a href="https://linuxconfig.org/ubuntu-22-04-chromium-browser-installation">https://linuxconfig.org/ubuntu-22-04-chromium-browser-installation</a></p>

---

## Post #11 by @chz31 (2024-07-06 22:33 UTC)

<p>Yes, I can install and open chrominum-browser and use it with no problem.</p>
<p>I did get some warning messages printed out. but they seem to not disrupt the browser functions:</p>
<pre><code class="lang-auto"> 2024/07/06 17:29:51.936431 cmd_run.go:1138: WARNING: cannot start document portal: dial unix /run/user/1000/bus: connect: no such file or directory
libpxbackend-1.0.so: cannot open shared object file: No such file or directory
Failed to load module: /home/chz31/snap/chromium/common/.cache/gio-modules/libgiolibproxy.so
libpxbackend-1.0.so: cannot open shared object file: No such file or directory
Failed to load module: /home/chz31/snap/chromium/common/.cache/gio-modules/libgiolibproxy.so
[221612:221825:0706/172954.448365:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172954.448471:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172954.448498:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172954.448518:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172954.786342:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172954.786475:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221822:0706/172955.007529:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172955.105509:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221825:0706/172955.105670:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221612:0706/172955.320720:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.NameHasOwner: object_path= /org/freedesktop/DBus: unknown error type:
[221612:221823:0706/172955.320899:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221894:0706/172955.355699:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.Properties.Get: object_path= /org/freedesktop/UPower: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.UPower was not provided by any .service files
[221612:221894:0706/172955.356052:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.UPower.GetDisplayDevice: object_path= /org/freedesktop/UPower: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.UPower was not provided by any .service files
[221612:221894:0706/172955.356425:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.UPower.EnumerateDevices: object_path= /org/freedesktop/UPower: org.freedesktop.DBus.Error.ServiceUnknown: The name org.freedesktop.UPower was not provided by any .service files
[221612:221612:0706/172955.384103:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.NameHasOwner: object_path= /org/freedesktop/DBus: unknown error type:
[221612:221840:0706/172955.384537:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory

(chrome:221612): IBUS-WARNING **: 17:29:55.437: Failed to mkdir /home/chz31/snap/chromium/2905/.config/ibus/bus: Not a directory
[221612:221612:0706/172955.439434:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.NameHasOwner: object_path= /org/freedesktop/DBus: unknown error type:
[221612:221823:0706/172955.439850:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221612:0706/172955.442239:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.NameHasOwner: object_path= /org/freedesktop/DBus: unknown error type:
[221612:221823:0706/172955.442405:ERROR:bus.cc(407)] Failed to connect to the bus: Failed to connect to socket /run/user/1000/bus: No such file or directory
[221612:221612:0706/172955.456367:ERROR:object_proxy.cc(576)] Failed to call method: org.freedesktop.DBus.NameHasOwner: object_path= /org/freedesktop/DBus: unknown error type:
MESA: error: ZINK: failed to choose pdev
glx: failed to create drisw screen
[221846:221846:0706/172956.075811:ERROR:viz_main_impl.cc(166)] Exiting GPU process due to errors during initialization
[221882:7:0706/172956.236489:ERROR:command_buffer_proxy_impl.cc(132)] ContextResult::kTransientFailure: Failed to send GpuControl.CreateCommandBuffer.
</code></pre>

---

## Post #12 by @yuan_li (2024-07-19 05:29 UTC)

<p>Hi Chi,<br>
I am new to Slicer and I experienced the same error while I clicked the extension manager and Slicer crashed in the WSL.<br>
May I ask how did you manage to install extensions via Extension Wizard?<br>
Thank you!</p>

---

## Post #13 by @chz31 (2024-07-19 06:26 UTC)

<p>Yes, I did manage to use Extension Wizard to install a git cloned extension.</p>

---

## Post #14 by @chz31 (2024-07-20 04:50 UTC)

<p><a class="mention" href="/u/yuan_li">@yuan_li</a> Sorry, I did not see the detail of your question. Here is the tutorial: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/extensionwizard.html" class="inline-onebox" rel="noopener nofollow ugc">Extension Wizard — 3D Slicer documentation</a> and <a href="https://www.youtube.com/watch?v=QsxzjQb05D4" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=QsxzjQb05D4</a></p>
<p>You can go to a GitHub repository of an extension and download the zip or git clone it (for example, <a href="https://github.com/SlicerMorph/SlicerMorph" rel="noopener nofollow ugc">SlicerMorph</a>), then you just go to the Extension Wizard and click “Select Extension” to select the downloaded folder.</p>

---

## Post #15 by @yuan_li (2024-07-22 01:18 UTC)

<p>No worries, thank you for your help! I manage to install the needed packages.<br>
Thank you again for your time and help!</p>

---

## Post #16 by @lassoan (2024-07-22 22:16 UTC)

<p>Only those extensions can be installed from github repository zip archives that only contain Python scripted modules. If you want to install any Python extension then you can do it by a few lines Python commands, as shown in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension">script repository</a>.</p>
<p>However, there are a couple of other issues with Slicer on WSL2. We don’t plan to work on them until we learn about use cases, but I’ve added an issue to track them anyway:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7864">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7864" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7864" target="_blank" rel="noopener">Compatibility with Windows Subsystem for Linux (WSL2)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-07-22" data-time="22:15:22" data-timezone="UTC">10:15PM - 22 Jul 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Some users would like to run Slicer in WSL2, but there are a couple of issues th<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">at would be nice to fix.

# How to run Slicer on WSL2

## Setup

- Start PowerShell as Administrator

Run command:

```
wsl --install
```

Start wsl:

```
wsl
```

- Create user, password.
- Get information on what linux distribution is installed:

```
cat /etc/os-release
```

- Get prerequisites from here: https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux

For example, for ubuntu 22.04:

```
sudo apt-get install libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2 qt5dxcb-plugin libsm6
```

- Install Slicer: get the download link from https://download.slicer.org, then download and unpack:

```
cd /tmp
wget https://download.slicer.org/bitstream/669c9155e53aec320c786090 -O Slicer.tar.gz
tar -xvzf Slicer.tar.gz
```

## Start Slicer

- Start wsl:

```
wsl
```

- Start Slicer:

```
/tmp/Slicer-5.7.0-2024-07-20-linux-amd64/Slicer
```

# Experienced issues

## Extensions manager crashes

Workaround: install extensions using the Python console

```
extensionNames = ["SlicerIGT", "SegmentEditorExtraEffects"]
em = slicer.app.extensionsManagerModel()
em.interactive = False  # prevent display of popups
restart = False  # we will restart manually after all extensions were installed
update = True
for extensionName in extensionNames:
    if not em.installExtensionFromServer(extensionName, restart):
        raise ValueError(f"Failed to install {extensionName} extension")
    print(f"Installed {extensionName}")
slicer.util.restart()
```

## Cannot use view controllers (that appear when push-pin button is clicked)

View contollers appear slightly shifted and buttons do not react.

Workaround: use `View Controllers` module to adjust view settings

## Popup windows appear out of place

Confirmation popups etc. appear far away from the application window.

Workaround: none. The popup windows are still functional.

## Rendering is slow

## Switching to Volume Rendering module crashes the application</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
