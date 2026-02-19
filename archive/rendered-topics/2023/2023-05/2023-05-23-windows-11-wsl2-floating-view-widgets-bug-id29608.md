---
topic_id: 29608
title: "Windows 11 Wsl2 Floating View Widgets Bug"
date: 2023-05-23
url: https://discourse.slicer.org/t/29608
---

# Windows 11 WSL2 floating View Widgets bug

**Topic ID**: 29608
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/windows-11-wsl2-floating-view-widgets-bug/29608

---

## Post #1 by @Thibault_Pelletier (2023-05-23 14:17 UTC)

<p>Hi everyone,</p>
<p>I recently wanted to test an extension build on Linux and used Windows 11 WSL2 for this with a Slicer build from scratch on the main branch.</p>
<p>Everything builds smoothly (which is really great) and GUI support accross WSL 2 worked out of the box (I may have set-up something at some point but I’m not entirely sure).</p>
<p>While testing in this environment, I noticed the following behavior for the Slice views floating menus :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4641609b0d5a07525b489bdfb07c8a5eef97f42.png" alt="image" data-base62-sha1="s1m15S9cbiN6Gs63pEhtrCC27m2" width="512" height="110"></p>
<p>The position of the floating menus is not correctly anchored and it’s impossible to click on the different options.</p>
<p>I have seen this behavior only for the view menus (2D and 3D widget) and not for the “standard” QMenu options.</p>
<p>This problem is not really blocking or anything and it’s not the expected way to run 3D Slicer but I wanted to know if others have seen / fixed this behavior.</p>
<p>Best,<br>
Thibault</p>

---

## Post #2 by @lassoan (2023-05-23 19:27 UTC)

<p>I’ve tried this and it seems that popups generally appear at the correct location. I’ve found that only the Welcome window, slice view controller (and maybe the volume rendering preset selector) is not at the right place.</p>
<p>There are a lot of mappings between local widget and global coordinates when positioning the <a href="https://github.com/commontk/CTK/blob/master/Libs/Widgets/ctkBasePopupWidget.cpp">slice view controller popup base class</a>, probably some of those calls don’t work correctly in WSLg. It would be nice if you could debug what goes wrong. You can access all widgets and their methods in Python, so you could investigate this without configuring a C++ debugger.</p>

---

## Post #3 by @Thibault_Pelletier (2023-05-24 05:20 UTC)

<p>Hi Andras,</p>
<p>Thanks for the feedback and the link.<br>
I will have a look and see if I can find where the problem comes from!</p>
<p>Best,<br>
Thibault</p>

---

## Post #4 by @Amos_Gutman (2024-07-01 08:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae25b1645e20e4d040494f9cdb09f70e05e95ff8.png" data-download-href="/uploads/short-url/oQzPRUlyN7PY2YgP2C3UrlyKGLu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae25b1645e20e4d040494f9cdb09f70e05e95ff8_2_690x105.png" alt="image" data-base62-sha1="oQzPRUlyN7PY2YgP2C3UrlyKGLu" width="690" height="105" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae25b1645e20e4d040494f9cdb09f70e05e95ff8_2_690x105.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae25b1645e20e4d040494f9cdb09f70e05e95ff8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae25b1645e20e4d040494f9cdb09f70e05e95ff8.png 2x" data-dominant-color="3B4659"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1031×158 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
happens with intelij as well</p>
<p>the popup window should appear on where the square and it is not ancored to the right place</p>

---

## Post #5 by @lassoan (2024-07-26 04:21 UTC)

<p>Thanks for the information. It indicates that the root cause of thr issue is that WSL2 works incorrectly, or at least differently than a linux desktop. The problem will likely to be fixed in WSL2, but probably some workaround could be inplemented in Slicer as well.</p>
<p>However, it is hard to justify spending time with investigating this, when Slicer runs natively on Windows, including all AI tools, with GPU acceleration, etc. What is the motivation for running Slicer on Windows via WSL2?</p>

---

## Post #6 by @Thibault_Pelletier (2024-07-26 05:43 UTC)

<p>Thank you <a class="mention" href="/u/amos_gutman">@Amos_Gutman</a> for the information and <a class="mention" href="/u/lassoan">@lassoan</a> for the analysis!</p>
<p>On my end, the main reason for using 3D Slicer in WSL2 was for two things :</p>
<ul>
<li>Testing / evaluating extensions which may not be available on Windows. That was the case for one of the modules from the AMASS extension for mesh segmentation which relied on pytorch 3D which was not available on Windows then (not sure if it has changed since).</li>
<li>Dev purposes to make sure extensions developed on Windows also work as expected on Linux (for this I could also use a dual boot / VM)</li>
</ul>
<p>So the only use case which would be relevant would be the first one but I don’t think this would justify the time investment.</p>

---

## Post #7 by @lassoan (2024-07-26 06:08 UTC)

<p>Thanks for the information. Quick testing on Linux is a good use case, as it is simpler than setting up dual-boot or GPU-accelerated virtual machine on Windows. For quick testing, the popups appearing at incorrect location/not working is probably tolerable as there are workarounds (the same features are available in docking widgets, which work well).</p>
<p>Fornl future reference, related issue in the issue tracker:</p>
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
