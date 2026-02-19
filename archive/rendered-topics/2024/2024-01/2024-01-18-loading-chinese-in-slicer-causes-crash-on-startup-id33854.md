---
topic_id: 33854
title: "Loading Chinese In Slicer Causes Crash On Startup"
date: 2024-01-18
url: https://discourse.slicer.org/t/33854
---

# Loading Chinese in Slicer causes crash on startup

**Topic ID**: 33854
**Date**: 2024-01-18
**URL**: https://discourse.slicer.org/t/loading-chinese-in-slicer-causes-crash-on-startup/33854

---

## Post #1 by @chen-hongbo (2024-01-18 14:40 UTC)

<p>Using Language Tool to load Chinese, starting Slicer results in a crash. However, if Japanese is loaded, the startup is normal.</p>

---

## Post #2 by @lassoan (2024-01-18 14:45 UTC)

<p>Thanks for reporting this. The crash has been already fixed, see details at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7523">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7523" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7523" target="_blank" rel="noopener">Cannot start after setting language to Chinese</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-08" data-time="17:23:21" data-timezone="UTC">05:23PM - 08 Jan 24 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-01-08" data-time="23:16:45" data-timezone="UTC">11:16PM - 08 Jan 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/FFFPrime" target="_blank" rel="noopener">
          <img alt="FFFPrime" src="https://avatars.githubusercontent.com/u/47420679?v=4" class="onebox-avatar-inline" width="20" height="20">
          FFFPrime
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary
When the language is set to **Simplified Chinese** in **Utilities\La<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nguage Tools**, the program cannot be opened after restarting, and the Windows problem report shows that `SlicerApp-real.exe` has stopped working. Switching to **Japanese** will display Japanese normally, switching to **Traditional Chinese** will display English, but it can start normally.

After careful investigation, after deleting the **Slicer_zh-CN.qm** file in the `%LocalAppData%\slicer.org\Slicer 5.6.1\bin\translations`  directory, the program can start normally.

## Steps to reproduce

1. Press Ctrl+4, enter **Extensions Manger**, search for "language", you can see a utility called **LanguagePacks**, restart the software after installation
2. Press Ctrl+2, open **Application Setting**, check **internationalization**, and restart the software.
3. Click **Utilities**→**Language Tools** in the module options, select **Weblate** in the Input translations column, click the **refresh** button, you can see a list of many languages, check **Japanese**, **Simplified Chinese** and **Traditional Chinese**, click **Update translation files** , the translation file will start to download automatically. After downloading, restart the software
4. Open **Language Tools** again, select **Application language** as **Chinese (China)** at the top, click **Restart the application** on the right, and the software will restart.

![repo1](https://github.com/Slicer/Slicer/assets/47420679/00876f83-97b7-4629-b012-85cf9d595775)

5. When starting the software, text such as the initialization module will be displayed, but when it reaches the `Loading module "SegmentEditor"... `stage, it will crash.
![repo2](https://github.com/Slicer/Slicer/assets/47420679/2363c2fb-41ba-451d-99d2-061bef3e1958)

6. Also select the **second** Chinese (China). After restarting, the software can be started normally but it is displayed in **English**.

7. After selecting **Japanese**, the software starts normally and the translation takes effect.
![repo3](https://github.com/Slicer/Slicer/assets/47420679/64d70e7d-09b3-43e3-99e8-951b02c38598)



##  Environment
System: Windows 10 Chinese version
System version: 22H2(19045.3803)
Slicer version: 5.6.1 Stable Release (You see there is no utility named Language Tools in Preview Release )

## Problem log of Windows system
Source: SlicerApp-real.exe
Summary: Stopped working
Date: 2014-01-‎08 23:22
Status: Report Sent
Wrong application path: C:\Users\1233\AppData\Local\slicer.org\Slicer 5.6.1\bin\SlicerApp-real.exe
Problem event name: APPCRASH
Application name: SlicerApp-real.exe
Application version: 0.0.0.0
Application timestamp: 65633afb
Faulty module name: Qt5Widgets.dll
Faulty module version: 5.15.2.0
Faulty module timestamp: 5fa4de1c
Exception code: c0000005
Exception offset: 0000000000032fe9
OS version: 10.0.19045.2.0.0.768.99
Locale ID: 2052
Additional information 1: 6cfd
Additional information 2: 6cfdfc8dd99a7ae0ef76343ef9579a3f
Additional information 3: f94b
Additional information 4: f94bf039ba88192a82b805ca52b38915
Bucket ID: 4ebf9e4a2a29d98d46356509a199b490 (1600296334640395408)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In summary, the problem is caused by incorrect translation of <code>Segmentations</code> module: it is translated as <code>Segmentation</code>, which is the exact same word that is used as module category name.</p>
<p>We fixed the crash in the Slicer Preview Release so that now a warning is logged instead of crash when a module name matches a module category name. However, you still need to modify the Chinese translation to not use the same string as both a module name and a module category name.</p>

---
