---
topic_id: 7881
title: "Extension Wizard File Open Dialogs Hang Ui For Several Secon"
date: 2019-08-05
url: https://discourse.slicer.org/t/7881
---

# Extension Wizard - file open dialogs hang UI for several seconds

**Topic ID**: 7881
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/extension-wizard-file-open-dialogs-hang-ui-for-several-seconds/7881

---

## Post #1 by @hherhold (2019-08-05 14:14 UTC)

<p>7/31/19 nightly on MacOS 10.14.4.</p>
<ol>
<li>Open slicer</li>
<li>Go to Extension Wizard</li>
<li>Click “Select Extension” (or anything that opens a file select dialog)</li>
</ol>
<p>UI freezes (meaning window manager) - mouse movement continues, but dialog opens EXTREMELY slowly, and once it opens, it responds VERY slowly. MacOS UI Dock also does not respond - almost looks like window manager is overloaded/momentarily hung.</p>
<p>I should note that it <em>is</em> operational and useable, just <em>very</em> slow for these operations.</p>

---

## Post #2 by @pieper (2019-08-05 14:33 UTC)

<p>Yes, I’m seeing something similar with the nightly.  If started in a terminal (e.g. with <code>/Applications/Slicer-4.11.0-2019-07-19.app/Contents/MacOS/Slicer</code>) I see messages like this appear until the extension window shows up.  Once it’s up it seems to work fine.  This is only on the nightly, 4.10.2 works fine for me.</p>
<pre><code class="lang-auto">[27972:100867:0805/102712.778974:ERROR:gl_context_cgl.cc(137)] Error creating context.
[27972:100867:0805/102712.798547:ERROR:gl_context_cgl.cc(137)] Error creating context.
"{3db9d341-53ba-4a2e-8962-4409eca87c7e}: 5: Operation canceled"
"{4891af70-fea6-4635-8816-9627c110eaf5}: 5: Operation canceled"
"{fbc2e3b6-f01e-44d3-8435-7fb1b48c4f3f}: 5: Operation canceled"
"{9dc4382b-cba6-4d58-91fe-93290d349288}: 5: Operation canceled"
"{17831f79-0336-492a-8854-5d933668c421}: 5: Operation canceled"
"{16c14595-6939-489e-a004-4e51a32d1bdb}: 5: Operation canceled"
"{c8853a8f-36ce-4dbc-9364-558eafbc7d94}: 5: Operation canceled"
"{bedbcf6e-7b05-4ca9-8766-8b1424fc7076}: 5: Operation canceled"
"{d1afaf15-073f-4f18-95aa-dd0dc52328c7}: 5: Operation canceled"
"{99ea99c9-1b2b-4632-82e4-6fb4ea293d4e}: 5: Operation canceled"
"{124fc397-84e4-4923-99bb-c86db8ae777c}: 5: Operation canceled"
"{139bdfbe-86e9-411c-91cc-3002b100e6fa}: 5: Operation canceled"
"{9fc50f60-bfb5-4d37-82bc-92ad197d19f0}: 5: Operation canceled"
"{6071fe8f-cd84-48e6-9755-8e923aa0cb0b}: 5: Operation canceled"
"{66b3b4c5-0a8a-44a9-bb90-15296be5c742}: 5: Operation canceled"
"{34e50472-12b0-48ea-994e-34fe9068fe7a}: 5: Operation canceled"
"{6b8acfcb-8d4f-4355-9cc3-22410d21d08f}: 5: Operation canceled"
"{48575e31-ef58-47c7-bae7-a6a4b72e8335}: 5: Operation canceled"
"{ceb132f1-217c-471f-a3ab-41dc9ceb49d5}: 5: Operation canceled"
"{f456950f-09fb-44e1-bf4d-49981662a254}: 5: Operation canceled"
"{332f5221-e05f-460e-8700-89c156e995dc}: 5: Operation canceled"
"{5fa1e706-50fe-4a19-81a6-9987833368e4}: 5: Operation canceled"
</code></pre>
<p>On the mac you can use the Activity Monitor application’s Sample Process option to get an idea of what’s going on, or you can use Instruments from Xcode for a more fine grained look.</p>

---

## Post #3 by @hherhold (2019-08-05 14:53 UTC)

<p>OK. It’s not a huge deal as I don’t use the Extension Wizard often, once something is set up I’m more or less done and then I develop in emacs or whatever. Odd that it makes OpenGL hang for some weird reason. I wonder what’s being fed to create the context (and why this needs to be done to open a file dialog).</p>
<p>Thanks for looking at it.</p>

---

## Post #4 by @lassoan (2019-08-05 15:11 UTC)

<p>It may be caused by the extension manager. Does it happen if you remove Slicer-NNN.ini file? Does it happen if you rename the entire NA-MIC folder in your profile folder?</p>

---

## Post #5 by @pieper (2019-08-05 15:23 UTC)

<p>I believe there are a couple issues - the webengine in the qt version we are using seems to have a graphics context issue, and then the option to restore previous extensions sometimes seems to have networking issues.  I don’t end up using it a lot either so I haven’t looked any deeper.</p>

---

## Post #6 by @jamesobutler (2019-08-05 17:26 UTC)

<p>I’ve been working on getting the nightly Slicer builds to all use Qt 5.12.4, so hopefully once that is complete it will fix the QWebEngine error here.</p>
<p>The current macOS nightly uses Qt 5.10.0 which was released December 2017 while macOS 10.14 which <a class="mention" href="/u/hherhold">@hherhold</a> is using wasn’t originally released until September 2018.</p>
<p>Qt 5.12 is a LTS release so it will have longer support/bug fixes for new macOS releases.</p>

---

## Post #7 by @lassoan (2019-08-15 19:47 UTC)

<p><a class="mention" href="/u/che85">@che85</a> told me today he has issues with slow Slicer startup and long 10-20 second delay when displaying any file dialog on his Mac. Using Instruments tool showed that the delay is most likely caused by tccd process. This may be also related to the “Allow Slicer application to control your computer?” question that is shown on some Macs.</p>
<p>Others have experienced this issue, too, for example <a href="https://forum.freecadweb.org/viewtopic.php?style=4&amp;f=4&amp;t=31343&amp;sid=e93aa3b1b276fa037e7758890d735ca2" rel="nofollow noopener">FreeCAD</a> and <a href="https://discussions.apple.com/thread/8612641?page=2" rel="nofollow noopener">Skyrim</a>.</p>
<p>Hopefully updating to a more recent Qt will solve this. <a class="mention" href="/u/jamesobutler">@jamesobutler</a> if you have a preview build that uses a recent Qt version then it would be great if you could send it to <a class="mention" href="/u/che85">@che85</a> for testing.</p>

---

## Post #8 by @hherhold (2019-11-08 00:06 UTC)

<p>Any progress on this? I still get these hangs occasionally.</p>

---

## Post #9 by @lassoan (2019-11-08 00:32 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> did you have a chance to build Slicer with a more recent Qt? Could you create a package that <a class="mention" href="/u/hherhold">@hherhold</a> or <a class="mention" href="/u/che85">@che85</a> could test?</p>

---

## Post #10 by @jamesobutler (2019-11-08 01:20 UTC)

<p>Sorry, I do not. I was borrowing a system during my development period back then.</p>
<p>Qt 5.12 series upgrading will require upgrades to the Slicer factory build machines as specified in my PRs there <a href="https://github.com/Slicer/DashboardScripts/pulls" rel="nofollow noopener">https://github.com/Slicer/DashboardScripts/pulls</a>. Currently unclear if and when support for that would be coming around.</p>
<p>At the time I was doing various work to make Slicer easier to build using the latest compilers as that is the source of the problem for many basic users building from source.</p>

---

## Post #11 by @lassoan (2019-11-08 02:36 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you create a Slicer Mac package with a latest possible Qt version so that people with the startup/filedialog hang issue coult try it?</p>

---

## Post #12 by @hherhold (2019-11-08 02:52 UTC)

<p>I can build from source with Qt 5.12 and see what happens. I seem to remember last time I built it locally it worked okay, but that was some months ago - I stopped building from source when I started doing only Python development.</p>

---

## Post #13 by @hherhold (2019-11-09 15:42 UTC)

<p>My local build using Qt 5.12 does not have the problem. I did run a ‘make package’ and ran into errors towards the end, starting with:</p>
<pre><code>768 - fixing item /Volumes/CT_Work/SB/Slicer-build/bin/libqSlicerApp.dylib with @rpath/lib/Slicer-4.11
Error copying file "@rpath/libSimpleITKBasicFilters0-1.3.1.dylib" to "/Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/lib/Slicer-4.11/libSimpleITKBasicFilters0-1.3.1.dylib".
chmod: /Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/lib/Slicer-4.11/libSimpleITKBasicFilters0-1.3.1.dylib: No such file or directory
</code></pre>
<p>This went on for a while, then recovered and finished with:</p>
<pre><code>776 - fixing item /usr/local/Cellar/qt/5.12.0/lib/QtWebEngineCore.framework/Versions/5/QtWebEngineCore with @rpath/Frameworks
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't open input file: /Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/Frameworks/QtWebEngineCore.framework/Versions/Current/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess for writing (Permission denied)
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't lseek to offset: 0 in file: /Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/Frameworks/QtWebEngineCore.framework/Versions/Current/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess for writing (Bad file descriptor)
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't write new headers in file: /Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/Frameworks/QtWebEngineCore.framework/Versions/Current/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess (Bad file descriptor)
error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/install_name_tool: can't close written on input file: /Volumes/CT_Work/SB/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.11.0-2019-11-07-macosx-amd64/Slicer.app/Contents/Frameworks/QtWebEngineCore.framework/Versions/Current/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess (Bad file descriptor)
CPack: Create package
CPack Error: Error executing: /usr/bin/hdiutil detach "/Volumes/Slicer-4.11.0-2019-11-07-macosx-amd64"
CPack Error: Error detaching temporary disk image.
CPack Error: Problem compressing the directory
CPack Error: Error when generating package: Slicer
make: *** [package] Error 1
</code></pre>
<p>The Slicer app packed into the dmg did seem to work, though, but I didn’t test it extensively (yet).</p>

---

## Post #14 by @hherhold (2019-11-09 15:43 UTC)

<p>I’m happy to post that DMG somewhere for testing/use if these packaging errors are ignorable.</p>

---

## Post #15 by @lassoan (2019-11-09 15:55 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="14" data-topic="7881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’m happy to post that DMG somewhere</p>
</blockquote>
</aside>
<p>I would be great. Dropbox, OneDrive, etc. should work.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> have you tried to build and package, too? Have you experienced similar packaging issues?</p>

---

## Post #16 by @hherhold (2019-11-09 16:12 UTC)

<p>Disk image uploading now, should be ready in a few mins.</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/sh/do60w766ojk0b8i/AAB-lJq80hIr2V3ozXBsHgt9a?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-folder_dropbox-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/sh/do60w766ojk0b8i/AAB-lJq80hIr2V3ozXBsHgt9a?dl=0" target="_blank" rel="nofollow noopener">Slicer build</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #17 by @lassoan (2019-11-09 16:26 UTC)

<p><a class="mention" href="/u/che85">@che85</a> Could you try the package above and see if you still have the issues of long startup time and long time required for file selection dialogs to show up. Thanks!</p>

---

## Post #18 by @pieper (2019-11-09 17:05 UTC)

<p>Interesting - I tried the build that <a class="mention" href="/u/hherhold">@hherhold</a> made, and it gave me the dialog box shown below when I tried to open the extension manager. The extension manager dialog does show up but is blank.  Today’s factory nightly build on the same mac works fine, and the extension manager takes just a second or two to start up and displays correctly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ad45a053e7391b8d32e49423b6e591ba14a1f8.png" data-download-href="/uploads/short-url/wUF3cKlmN0ZcAclcFWXvXrrFfHa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6ad45a053e7391b8d32e49423b6e591ba14a1f8_2_208x500.png" alt="image" data-base62-sha1="wUF3cKlmN0ZcAclcFWXvXrrFfHa" width="208" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6ad45a053e7391b8d32e49423b6e591ba14a1f8_2_208x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6ad45a053e7391b8d32e49423b6e591ba14a1f8_2_312x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6ad45a053e7391b8d32e49423b6e591ba14a1f8_2_416x1000.png 2x" data-dominant-color="C9C8C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">584×1399 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @lassoan (2019-11-09 17:20 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> What MacOSX version do you use? Have you experienced slow startup and long  wait before file selection dialogs show up? Do you remember that the OS asked you for permission to Slicer control your computer? Did you give permission? (these slowdowns are caused by waiting for tccd process and it is likely related to some security or accessibility checks).</p>

---

## Post #20 by @hherhold (2019-11-09 17:41 UTC)

<p>This is kind of odd. When I run the app from the package, I get the window manager hang. When I run it from the command line (i.e., Slicer-build/Slicer), I do not get the hang.</p>
<p>I wonder if it’s a problem with improper packaging, and not all the correct libraries are included, and Slicer falls back on system-installed libraries? (totally shooting in the dark here…)</p>

---

## Post #21 by @pieper (2019-11-09 17:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="7881" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> What MacOSX version do you use? Have you experienced slow startup and long wait before file selection dialogs show up? Do you remember that the OS asked you for permission to Slicer control your computer? Did you give permission? (these slowdowns are caused by waiting for tccd process and it is likely related to some security or accessibility checks).</p>
</blockquote>
</aside>
<p>I’m testing on 10.14.6.  It does ask for permissions from time to time but I decline and it doesn’t seem to matter.</p>
<p>I’m installing the latest 10.15 on an older machine now, so I can test that out and let you know.</p>
<aside class="quote no-group" data-username="hherhold" data-post="20" data-topic="7881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I wonder if it’s a problem with improper packaging, and not all the correct libraries are included, and Slicer falls back on system-installed libraries? (totally shooting in the dark here…)</p>
</blockquote>
</aside>
<p>Interesting idea - in the Activity Monitor if you select a process and click the info icon (i in circle) you can list all the open files and ports, which will show you which libs are in use, so you could compare.</p>

---

## Post #22 by @hherhold (2019-11-09 18:31 UTC)

<p>There’s nothing obviously different in the libs at first glance. The packaged one is using the packaged libraries, which (presumably) came from my system, as that’s where it was built using Qt 5.12 from Homebrew.</p>

---

## Post #23 by @pieper (2019-11-09 20:07 UTC)

<p>On macos 10.15, both the factory preview and <a class="mention" href="/u/hherhold">@hherhold</a>’s build take about 10 seconds to bring up the extension manager.  4.10.2 opens right away.</p>
<p>On a side note, slicer seems to run fine on 10.15, but with stricter default security permissions - you must manually go to the security settings and manually approve each version of the app, you can’t just use the context menu Open.</p>

---

## Post #24 by @Sunderlandkyl (2019-11-09 20:29 UTC)

<p>Sorry for the delay, I had to update some build scripts for MacOS 10.14, but it looks like it was successful.<br>
I built Slicer using the latest Qt LTS release (5.12.5).</p>
<p>Here is the link:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/l2zlcbyzurr7w6c/Slicer-4.11.0-2019-11-07-macosx-amd64.dmg?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/l2zlcbyzurr7w6c/Slicer-4.11.0-2019-11-07-macosx-amd64.dmg?dl=0" target="_blank" rel="nofollow noopener">Slicer-4.11.0-2019-11-07-macosx-amd64.dmg</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #25 by @rkikinis (2019-11-09 20:39 UTC)

<p>Where are those security settings to be found?</p>

---

## Post #26 by @pieper (2019-11-09 21:51 UTC)

<p>When I first tried to run it only offered cancel or move the app to the trash.  I cancel, and then in the System Preferences under Security &amp; Privacy there was a button added to enable running the app.  After that it worked.</p>

---

## Post #27 by @lassoan (2019-11-09 22:22 UTC)

<p>Could everybody with a Mac report the following for a recent Slicer preview release:</p>
<ul>
<li>MacOSX version, Slicer version</li>
<li>application startup time</li>
<li>time to show a file selection dialog (menu: File / Add data / Choose file to add)</li>
<li>time to show Extension wizard window</li>
</ul>
<p>Thank you!</p>

---

## Post #28 by @hherhold (2019-11-10 15:20 UTC)

<p>OK, I found out something rather odd.  This is with the 11-7 slicer nightly build (downloaded Saturday PM).</p>
<p>Test:</p>
<ol>
<li>Run slicer</li>
<li>Go to screen capture module</li>
<li>Hit … for dialog box to pick output directory.</li>
</ol>
<p>When I run slicer by double-clicking on the app, the dialog box always freezes halfway through its “zoom up” process. It hangs the window manager completely for several seconds. It will also sometimes hang the WM after it is up.</p>
<p>When I open a terminal window and run slicer from the command line (i.e., cd Desktop/Slicer.app/Contents/MacOS; ./Slicer) I <em>never</em> get these hangs.</p>
<p>Could it be some environment variable or path difference between running from the WM by double-clicking vs running on the command line?</p>
<p>This is MacOS 10.14.4.</p>

---

## Post #29 by @lassoan (2019-11-10 15:42 UTC)

<p>This freeze of the window manager is due to the tccd system process hanging for tens of seconds. This is what we try to fix.</p>
<p>Do you experience this issue with Slicer built with Qt-5.12.5?</p>

---

## Post #30 by @hherhold (2019-11-10 16:11 UTC)

<p>I was not able to run the 5.12.5 slicer because (I think) it’s built for 10.15, and I’m running 10.14.4.</p>
<p>Also, I thought the tccd problem was only referring to 10.15.</p>

---

## Post #31 by @lassoan (2019-11-10 16:21 UTC)

<p>You can use Instruments (I think it comes with xcode) to see what’s happening while the file dialog hangs. Maybe you can also try the package that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> built.</p>

---

## Post #32 by @hherhold (2019-11-10 16:34 UTC)

<p>That’s the one I can’t run (the one <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> built with 5.12.5).</p>
<p>On 10.14.4, if I put Slicer into the “it can control your machine” list in security settings, I do not get the dialog box hang. I mistakenly thought that was a 10.15-only issue.</p>

---

## Post #33 by @Sunderlandkyl (2019-11-11 14:31 UTC)

<p>Here are some nightly stats:</p>
<ul>
<li>MacOS: 10.14.6</li>
<li>Slicer Nightly (2019-11-09)</li>
<li>Startup: 11.0s</li>
<li>File dialog: 0.0s</li>
<li>Extension manager: 6.1s</li>
</ul>

---

## Post #34 by @lassoan (2019-11-11 14:38 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="32" data-topic="7881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>if I put Slicer into the “it can control your machine” list in security settings, I do not get the dialog box hang</p>
</blockquote>
</aside>
<p>This is a very important finding.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> do you see any difference in file dialog display time if you change security settings for Slicer application?</p>

---

## Post #35 by @Sunderlandkyl (2019-11-11 15:06 UTC)

<p>Slicer is not in the list of apps that can “control your computer”, and I am unable to add it.</p>
<p>I restarted the Mac, and now I’m seeing different behavior (same Nightly as before 2019-11-09):<br>
Startup: Hangs OS for ~33.4s on startup (total startup time (45.5s).<br>
File dialog: 0.0s<br>
Extension manager: Hangs OS for 56.4s.</p>
<p>Trying to determine why I can’t add security options for Slicer.</p>

---

## Post #36 by @che85 (2019-11-11 15:17 UTC)

<p>I have a similar issue. Slicer shows up in the accessibility list, but I cannot check it. I also reinstalled, removed Slicer, but that didn’t change anything.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2d5eac60e301a848c9d622893843be6423b90cc.png" data-download-href="/uploads/short-url/wmGdRmXBuA7P55UAil1X77eOVly.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2d5eac60e301a848c9d622893843be6423b90cc_2_569x500.png" alt="image" data-base62-sha1="wmGdRmXBuA7P55UAil1X77eOVly" width="569" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2d5eac60e301a848c9d622893843be6423b90cc_2_569x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2d5eac60e301a848c9d622893843be6423b90cc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2d5eac60e301a848c9d622893843be6423b90cc.png 2x" data-dominant-color="37383B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">780×685 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #37 by @Sunderlandkyl (2019-11-13 19:03 UTC)

<p>Andras and I did some more digging into this issue.</p>
<p>Logged tccd using this command:</p>
<blockquote>
<p>log stream --debug --predicate ‘subsystem == “com.apple.TCC”’</p>
</blockquote>
<p>During startup, there is a 50sec window where tccd is presumably checking the application signature:</p>
<blockquote>
<p>2019-11-13 12:41:30.733517-0500 0x7694f    Info        0xa9379              199    0    tccd: [com.apple.TCC:access] adhoc signed StaticCode :0x7fa6d33950e0 START<br>
2019-11-13 12:42:23.224389-0500 0x7694f    Info        0xa9379              199    0    tccd: [com.apple.TCC:access] adhoc signed StaticCode :0x7fa6d33950e0 END</p>
</blockquote>
<p>This seems to be the main cause of the hang in MacOS 10.14 for many unsigned applications.</p>
<p>Creating an ad-hoc signing with the following command allows Slicer to open without the delay:</p>
<blockquote>
<p>codesign --force --deep -s - /Applications/Slicer.app/Contents/MacOS/Slicer</p>
</blockquote>

---

## Post #38 by @lassoan (2019-11-14 00:30 UTC)

<p><a class="mention" href="/u/che85">@che85</a> <a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/pieper">@pieper</a> could you check if using the codesign command above fixes the temporary system hang for you?</p>

---

## Post #39 by @hherhold (2019-11-20 14:30 UTC)

<p>Yep - works. (Sorry for slow reply.)</p>
<p>Just tried on 11-18 build, freshly downloaded. Dialog box hang, then did codesign, then dialog box does not hang.</p>

---

## Post #40 by @lassoan (2019-11-20 16:16 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, could we try to do such self-signing with some default (non-trusted) signature? TCC does not seem to delay requests from executables that are at least self-signed.</p>
<p>Self-signing may not work between different computers/users (maybe TCC only accepts self-signed executables from the current user?), but it might worth a try, as it is a simpler process than accessing the official Kitware signing computer.</p>

---

## Post #41 by @jcfr (2019-11-26 22:48 UTC)

<blockquote>
<p>could we try to do such self-signing with some default (non-trusted) signature?</p>
</blockquote>
<p>While creating the self-signed certificate, worth noting that the following message is reported:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27b06f05bc484d9329d33b212bbd1dc594193ab4.png" alt="image" data-base62-sha1="5F6CYYBK7lfJdFgRwEdfDZQJP1O" width="255" height="108"></p>

---

## Post #42 by @jcfr (2019-11-26 23:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/rkikinis">@rkikinis</a> <a class="mention" href="/u/hherhold">@hherhold</a> A self-signed package corresponding to the most recent nightly is now available for download at <a href="https://data.kitware.com/#item/5dddb66daf2e2eed3533ec79">https://data.kitware.com/#item/5dddb66daf2e2eed3533ec79</a></p>
<p>Note that the signing was manually done</p>

---

## Post #43 by @rkikinis (2019-11-27 00:07 UTC)

<p>On Mac Catalina 10.15.1 : Both the dmg and slicer require opening with a right mouse click, but do not require going to preference/security. Workable.</p>

---

## Post #44 by @pieper (2019-11-27 01:06 UTC)

<p>I did some testing using various versions with commands like this:</p>
<pre><code class="lang-auto">time /Applications/"Slicer 2.app"/Contents/MacOS/Slicer --python-code "exit()"
</code></pre>
<p>All the release builds, both 4.10.2 and the nighlies and the new self-signed version from Jc complete in about 10-12 seconds.  My local debug build takes about 30 seconds for the same command line, whether I self-sign it or not.</p>
<p>I didn’t see anything particularly informative in the log stream command.</p>

---

## Post #45 by @Sunderlandkyl (2019-11-27 17:36 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I can confirm that the signed package doesn’t cause the hang. The only regression is that the installer requires a right-click to open.</p>

---
