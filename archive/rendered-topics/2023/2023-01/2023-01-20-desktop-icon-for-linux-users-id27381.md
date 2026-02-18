# Desktop icon for linux users

**Topic ID**: 27381
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/desktop-icon-for-linux-users/27381

---

## Post #1 by @luarpy (2023-01-20 16:50 UTC)

<p>Hello everyone,</p>
<p>I have been using the 3dSlicer software for almost a year now and I got tired of launching the application from the command line. I would like to be able to contribute to create a desktop shortcut according to the <a href="http://freedesktop.org" rel="noopener nofollow ugc">freedesktop.org</a> <a href="https://specifications.freedesktop.org/desktop-entry-spec/latest/" rel="noopener nofollow ugc">specifications</a> used by most GNU/Linux distributions.</p>
<p>As the file should reference the location of the ‘Slicer’ binary and the icon to represent the program on the desktop, I would like to know where you usually leave the download folder for Slicer.</p>
<p>A valid example would be the following for org.slicer.desktop:</p>
<pre><code class="lang-auto">[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Name=3DSlicer
GenericName=DICOMM file slicer
Comment=DICOMM file viewer
Exec=/absolute/path/to/folder/apps/3dslicer/Slicer-latest/Slicer
Icon=/absolute/path/to/folder/.local/share/icons/3dslicer.png
</code></pre>
<p>Perhaps a bash script could be prepared to facilitate copying the org.slicer.desktop file to the common folders where desktop managers check for the presence of *.desktop files such as  <code>/usr/share/applications/, $HOME/.local/share/applications</code>  for direct access from the desktop.</p>

---

## Post #2 by @pieper (2023-01-20 17:00 UTC)

<p>Sounds like a good idea.  I have typically done this manually or as part of an install script, but in general I use the command line.</p>
<p>I would suggest we consider making this a core feature of Slicer.  On startup the application could offer to install the shortcut if it doesn’t already exist.  The dialog could have a “don’t ask again” option for users who don’t ever want the shortcut.  This would be a fairly simple python script (probably easiest to manage in a hidden module that triggers with the <code>onStartupCompleted</code> signal).</p>

---

## Post #3 by @manjula (2023-01-21 05:48 UTC)

<p>It would be great as i also create the desktop icon manually.</p>

---

## Post #4 by @luarpy (2023-01-21 14:09 UTC)

<p>Ok, I agree.<br>
Apologies for not thinking of Microsoft Windows or MacOS users. I thought these operating systems had a shortcut to launch the application.</p>
<p>I was thinking only of Linux because for each distribution when changing the desktop environment or window manager the most common item was *.desktop files.</p>
<p>So an option should be added to accept in the first session whether to create a shortcut or not. I also see important to be able to manage the different versions of Slicer in the system.</p>
<p>For example, when a new version is to be installed, even if there is the previous one, this shortcut would have to refer to the latest version and delete the previous one? Should the user manually delete the previous version of Slicer? I think these are issues to be clarified.</p>

---

## Post #5 by @jamesobutler (2023-01-21 15:36 UTC)

<p>For Windows I have open work that I will be finishing soon for having the option to create a desktop icon during the install process. This is common for installers on Windows. I’m not sure about other platforms. It would be good for other platforms to create desktop shortcuts in whatever manner is standard behavior for that platform.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6761">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6761" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6761" target="_blank" rel="noopener nofollow ugc">ENH: Create Windows Desktop shortcut during install</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:desktop-shortcut</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-04" data-time="21:07:28" data-timezone="UTC">09:07PM - 04 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="3 commits changed 3 files with 1017 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6761/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1017</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">On the Windows platform, running a Slicer installer would create Start Menu shor<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6761" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">tcuts but did not create a desktop shortcut which is pretty common. This PR will create a desktop shortcut as part of the install process.

Note: The Start Menu folder MUI Page has a "Do not create shortcuts" option which will skip start menu and desktop shortcut creation
![image](https://user-images.githubusercontent.com/15837524/210649601-b98f438a-226b-446d-aa4c-632ce32e1f0f.png)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="luarpy" data-post="4" data-topic="27381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>For example, when a new version is to be installed, even if there is the previous one, this shortcut would have to refer to the latest version and delete the previous one? Should the user manually delete the previous version of Slicer?</p>
</blockquote>
</aside>
<p>Since multiple versions of Slicer can be installed at the same time, maintaining previous versions is desired. It is common for people to have various Slicer stable and preview versions installed. Therefore my PR for Windows creates desktop shortcuts with the name and version so it is “Slicer 5.2.1” on the desktop.</p>

---

## Post #6 by @luarpy (2023-01-21 15:52 UTC)

<p>In the case of using a framework such as flatpak to package the application, it would be necessary to see how to manage the installer with multiple versions. As indicated in <a href="https://github.com/Slicer/Slicer/pull/6761" rel="noopener nofollow ugc">issue #6761</a> the case of using a framework such as flatpak to package the application, it would be necessary to see how to manage the installer with multiple versions. As indicated in issue <span class="hashtag">#6761</span> it could be activated or deactivated with a flag in CMake it could be activated or deactivated with a flag in CMake.</p>

---

## Post #7 by @luarpy (2023-01-23 10:27 UTC)

<p>For the Linux part it would be simple if it was to generate a *.desktop file that would have the reference to run the ‘Slicer’ binary depending on the folder that would have the version. It could be a template *.desktop file with some parameters changed such as the execution path and version identifier. There would have to be an image file as an icon in the resources to use it. It does not need more. Then that file would be stored in one of the paths known to the desktop managers and so it could be accessible from anywhere as an executable shortcut. Converting it to an icon on the desktop is as easy as copying the *.desktop file into the Desktop folder of the file system.</p>
<p>I have been going through a couple of resources on how to generate desktop shortcuts with python on Windows. It is possible and therefore everything could be contained within that hidden module, as <a class="mention" href="/u/pieper">@pieper</a> pointed out.</p>
<p>Although I think it would be wise to see if this issue can be addressed at Project Week as it is something that affects the actual use of the application itself.</p>
<p>Next would be to familiarize myself with Slicer modules and prepare a test. The available options could be:</p>
<ul>
<li>
<span class="chcklst-box fa fa-square-o fa-fw"></span> Create a desktop shortcut</li>
<li>
<span class="chcklst-box fa fa-square-o fa-fw"></span> Create a system wide shortcut</li>
<li>
<span class="chcklst-box checked permanent fa fa-check-square fa-fw"></span> Do not ask again</li>
</ul>
<p>I have to familiarize with the hide modules and prepare a test example.</p>

---

## Post #8 by @chir.set (2023-01-23 10:49 UTC)

<aside class="quote no-group" data-username="luarpy" data-post="7" data-topic="27381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>copying the *.desktop file into the Desktop folder of the file system</p>
</blockquote>
</aside>
<p>KDE has 2 desktop modes :</p>
<ul>
<li>Folder mode (default) : anything in the $HOME/Desktop/ directory shows on the desktop</li>
<li>Desktop mode : contrary to what the name suggests, the $HOME/Desktop/ content is ignored. Desktop icons are found in $HOME/.local/share/plasma_icons/</li>
</ul>
<p>This introduces some complications. The second ‘Desktop’ mode can also be left aside as it is an outlier case.</p>

---

## Post #9 by @jamesobutler (2023-01-23 12:39 UTC)

<aside class="quote no-group" data-username="luarpy" data-post="7" data-topic="27381">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/luarpy/48/67016_2.png" class="avatar"> luarpy:</div>
<blockquote>
<p>I have been going through a couple of resources on how to generate desktop shortcuts with python on Windows. It is possible and therefore everything could be contained within that hidden module, as <a class="mention" href="/u/pieper">@pieper</a> pointed out.</p>
</blockquote>
</aside>
<p>For Windows, I would suggest we stick with the creation of the desktop shortcut as a selection when running through the installer as this is familiar behavior on this platform. I’ll address this for Windows when I finalize my PR mentioned in my previous post. For Linux Desktop shortcut creation feel free to do whatever is standard in the Linux community.</p>

---
