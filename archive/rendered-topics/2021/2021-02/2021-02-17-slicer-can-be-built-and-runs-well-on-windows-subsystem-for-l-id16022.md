---
topic_id: 16022
title: "Slicer Can Be Built And Runs Well On Windows Subsystem For L"
date: 2021-02-17
url: https://discourse.slicer.org/t/16022
---

# Slicer can be built and runs well on Windows Subsystem for Linux (WSL2)

**Topic ID**: 16022
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/slicer-can-be-built-and-runs-well-on-windows-subsystem-for-linux-wsl2/16022

---

## Post #1 by @lassoan (2021-02-17 02:20 UTC)

<p>Some information for Windows developers who want to develop/test Slicer on Linux. On current Windows 10 versions, it is <em>very easy</em> to install Linux and run Linux GUI applications such as Slicer, by using Windows Subsystem for Linux (WSL2).</p>
<p>Ubuntu 20.04 shows up as an app in Microsoft Store. If you install and run it you get a linux terminal. By copy-pasting 10-20 lines you can install kubuntu desktop and you can connect to it using Windows remote desktop as explained <a href="https://www.nextofwindows.com/how-to-enable-wsl2-ubuntu-gui-and-use-rdp-to-remote">here</a>.</p>
<p>Slicer build instructions for linux work flawlessly and Slicer runs well (both the locally built version and downloaded releases):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dfb0e690d4113d1e607fab4e2b6e378d01acd5f8.jpeg" data-download-href="/uploads/short-url/vURtZIU7ZeFvoN4UqC4LLPhAunu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb0e690d4113d1e607fab4e2b6e378d01acd5f8_2_690x405.jpeg" alt="image" data-base62-sha1="vURtZIU7ZeFvoN4UqC4LLPhAunu" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb0e690d4113d1e607fab4e2b6e378d01acd5f8_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb0e690d4113d1e607fab4e2b6e378d01acd5f8_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dfb0e690d4113d1e607fab4e2b6e378d01acd5f8_2_1380x810.jpeg 2x" data-dominant-color="999798"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1994×1173 568 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Build speed is good, Slicer performance is near native, there is no problem with networking, file system access, etc. (issues that kept coming up when using VirtualBox, HyperV, etc.). GPU volume rendering works, but it is a software renderer. There is some GPU virtualization support that works for CUDA; and Microsoft is working on improving GUI application support, so probably GPU-accelerated rendering will be available at some point.</p>

---

## Post #4 by @davide445 (2022-01-04 21:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> was able to install Slicer 4.11 on Kubuntu 20.04 on wsl2 on Windows 11, so in theory with GPU aceleration. Works except the 3D view that works (very slow) on internal GPU, crashes always using discrete GPU. In my case the dGPU it’s in fact an external GPU (eGPU) connected trough Thunderbolt to mine laptop (using it just for testing).<br>
Some questions</p>
<ul>
<li>Other Kubuntu packages appear as Windows app directly accessible trough Start menu. I was only able to launch Slicer from Dolphin, didn’t find a way to install it as native wsl2 GUI app (maybe a reason why crashes using eGPU). Using “sudo apt-get install slicer” return there is no repository to install it from. There is any way to have it installed as separate app.</li>
<li>Following <a href="https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps" rel="noopener nofollow ugc">this</a> guide I downloaded ad installed the eGPU Windows driver. This is correct, or need I to download and install the Linux driver in wsl2 Ubuntu installation. I tried that but the installation did not completed correctly.</li>
<li>The eGPU is used since monitoring from Win Task Manager it’s the only one with some load. Trying to display volume rendering on eGPU result in a 100% usage spike and a crash. There is any Slicer log to look on to understand his problems.</li>
</ul>

---

## Post #5 by @muratmaga (2022-01-04 22:11 UTC)

<aside class="quote no-group" data-username="davide445" data-post="4" data-topic="16022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Following <a href="https://docs.microsoft.com/en-us/windows/wsl/tutorials/gui-apps">this</a> guide I downloaded ad installed the eGPU Windows driver. This is correct, or need I to download and install the Linux driver in wsl2 Ubuntu installation. I tried that but the installation did not completed correctly.</p>
</blockquote>
</aside>
<p>I presume those instructions are correct, given that they are written by the group who develop wsl2.</p>
<p>You need to install the driver in windows side (not in wsl2 side). Also note that specific driver supports only turing and newer generations.</p>

---

## Post #6 by @davide445 (2022-01-04 22:12 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="16022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also note that specific driver supports only turing and newer generations.</p>
</blockquote>
</aside>
<p>Using AMD GPU RX 550 4GB (the only spare I get this time for testing). Installed the linked driver that support this generation.</p>

---

## Post #7 by @davide445 (2022-01-05 08:28 UTC)

<p>Tested the eGPU using a native Kubuntu installation and Slicer volume rendering works without problems, so the problem it’s not the setup nor the specific GPU, seems to be something related to wsl2.</p>

---

## Post #8 by @muratmaga (2022-01-18 20:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="16022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is some GPU virtualization support that works for CUDA; and Microsoft is working on improving GUI application support, so probably GPU-accelerated rendering will be available at some point.</p>
</blockquote>
</aside>
<p>I tried the instructions on the <a href="https://github.com/microsoft/wslg#opengl-accelerated-rendering-in-wslg">wsl2 for openGL</a>, which basically requires you to install mesa 21 version inside the ubuntu. After that when I ran the</p>
<pre><code class="lang-auto">glxinfo -B
</code></pre>
<p>I can see the renderer as the NVIDIA gpu (instead of llvmpipes). Further basic tests with glxspheres shows that opengl does work (I can see the load on the Nvidia GPU on windows task manager), although it is quite slow. And while Slicer does initially render MRHead.nrrd as a still image, there can be no interaction on the 3D viewer. Curiously that’s true when I switch to CPU rendering. So something after Mesa 21 package upgrade broke 3D rendering in Slicer, as I was able to do software GPU rendering and CPU rendering on the wsl2 on this system.</p>
<p>Anyways, just reporting that H/W rendering inside WSL2 is still not functional.</p>

---

## Post #9 by @lassoan (2022-01-19 02:42 UTC)

<p>Thanks for the information. I guess more time is needed for this GPU support to mature.</p>

---

## Post #10 by @lassoan (2024-07-22 22:17 UTC)

<p>There are improvements in WSL2 installation and GPU support (much GPU-accelerated rendering and display of GUI application screens work out of the box), but there are still some issues. See details here:</p>
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
