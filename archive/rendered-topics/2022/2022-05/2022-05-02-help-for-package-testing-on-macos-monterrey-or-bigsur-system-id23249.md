# Help for package testing on macOS Monterrey or BigSur system

**Topic ID**: 23249
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/help-for-package-testing-on-macos-monterrey-or-bigsur-system/23249

---

## Post #1 by @jcfr (2022-05-02 22:00 UTC)

<h3><a name="p-77542-context-1" class="anchor" href="#p-77542-context-1" aria-label="Heading link"></a>Context</h3>
<p>To perform some testing to check if issue <a href="https://github.com/Slicer/Slicer/issues/6347">Slicer#6347</a> reported by <a class="mention" href="/u/che85">@che85</a> is specific to recent macOS system or if it is related to specific network &amp; proxy settings.</p>
<h3><a name="p-77542-help-needed-2" class="anchor" href="#p-77542-help-needed-2" aria-label="Heading link"></a>Help needed</h3>
<p>Two ways you could help:</p>
<ol>
<li>
<p>Reach out privately to <a class="mention" href="/u/jcfr">@jcfr</a> to schedule a hangout</p>
</li>
<li>
<p>Perform these steps and report back:</p>
<ul>
<li>Download <a href="https://download.slicer.org/bitstream/626eaacee8408647b391200a">this package</a></li>
<li>Open and “move” the application into your download folder.
<ul>
<li><small> <em><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20">  Do not directly run from the mounted application</em></small></li>
</ul>
</li>
<li>Right click on <code>Slicer</code> application, select <code>Open</code>
<ul>
<li><small> <em><img src="https://emoji.discourse-cdn.com/twitter/warning.png?v=15" title=":warning:" class="emoji" alt=":warning:" loading="lazy" width="20" height="20">  since this package is not yet signed, you will likely have to accept the warning and try twice.</em></small></li>
</ul>
</li>
<li>Click on the extension manager icon <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18b1a32f3505eb835a78af445604acf5071bb606.png" data-download-href="/uploads/short-url/3ws2PRcQyMtthmGMjsCJwZ5oEoC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18b1a32f3505eb835a78af445604acf5071bb606.png" alt="image" data-base62-sha1="3ws2PRcQyMtthmGMjsCJwZ5oEoC" width="24" height="24"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">128×128 16.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Attempt to install any extension</li>
<li><strong>Question</strong>: Is an error like the following is reported after clicking on the “Install” button ? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8da5956a9d331c5a8ad0c584a380dd8ced4cfee.png" data-download-href="/uploads/short-url/xdUAbDHRrIVMbIye6qDkloR76ai.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8da5956a9d331c5a8ad0c584a380dd8ced4cfee.png" alt="image" data-base62-sha1="xdUAbDHRrIVMbIye6qDkloR76ai" width="224" height="68"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">449×137 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
</ol>

---

## Post #2 by @hherhold (2022-05-02 22:05 UTC)

<p>How recent of a preview release to test this?</p>

---

## Post #3 by @jcfr (2022-05-02 22:08 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="2" data-topic="23249" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>How recent of a preview release to test this?</p>
</blockquote>
</aside>
<p>Since the issue indicates</p>
<blockquote>
<blockquote>
<p>just tested on older Slicer preview versions and it’s happening for all of them.</p>
</blockquote>
</blockquote>
<p>feedback related to a recent installation of a preview build would be helpful too if that it is easier for you to check.</p>

---

## Post #4 by @hherhold (2022-05-02 22:27 UTC)

<p>DOH - should have read issue, sorry. Checking.</p>

---

## Post #5 by @hherhold (2022-05-02 22:35 UTC)

<p>I did not get the error described above - the extensions installed correctly (SlicerMorph, which includes a few extensions, etc).</p>
<p>I did get a crash on exit, however - stack trace below. Re-opening Slicer, trying an extension, and then exiting Slicer dit not repeat the crash.</p>
<p>This is on macOS Monterey 12.1, MacBook Pro 16" (2019).</p>
<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [4415]
Path:                  /Users/USER/Downloads/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.0.1 (5.0.1)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2022-05-02 18:30:59.0736 -0400
OS Version:            macOS 12.1 (21C52)
Report Version:        12
Bridge OS Version:     6.1 (19P647)
Anonymous UUID:        35B3F1AE-3AB0-EA88-9149-17BDBEC361AB

Sleep/Wake UUID:       733D78D9-C625-4583-8C2D-569FE60E808B

Time Awake Since Boot: 62000 seconds
Time Since Wake:       7698 seconds

System Integrity Protection: enabled

Crashed Thread:        0  CrBrowserMain  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       UNKNOWN_0xD at 0x0000000000000000
Exception Codes:       0x000000000000000d, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [4415]

VM Region Info: 0 is not in any region.  Bytes before following region: 4502261760
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      __TEXT                      10c5b1000-10c5f3000    [  264K] r-x/rwx SM=COW  .../MacOS/Slicer

Thread 0 Crashed:: CrBrowserMain Dispatch queue: com.apple.main-thread
0   QtWidgets                     	       0x10dd46675 QWidgetPrivate::setParent_sys(QWidget*, QFlags&lt;Qt::WindowType&gt;) + 37
1   QtWidgets                     	       0x10dd3099d QWidget::setParent(QWidget*, QFlags&lt;Qt::WindowType&gt;) + 637
2   libqSlicerBaseQTGUI.dylib     	       0x10cd64063 qSlicerApplicationPrivate::~qSlicerApplicationPrivate() + 131
3   libqSlicerBaseQTGUI.dylib     	       0x10cd6413e qSlicerApplicationPrivate::~qSlicerApplicationPrivate() + 14
4   libqSlicerBaseQTCore.dylib    	       0x10d6513e6 qSlicerCoreApplication::~qSlicerCoreApplication() + 38
5   Slicer                        	       0x10c5eeb0f main + 527
6   dyld                          	       0x10e5ef4fe start + 462
</code></pre>

---

## Post #6 by @jcfr (2022-05-02 23:01 UTC)

<p>Thanks for the feedback that is very helpful. Thanks for taking the time <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>The crash is unfortunate, I would be curious is this is systematic after installing extension.</p>

---

## Post #7 by @pieper (2022-05-02 23:37 UTC)

<p>I also got the crash on exit after running the extension manager.  Install worked for Segmentation Extra Effects, so probably not extension-specific.  Oddly it’s a slightly different stack trace.</p>
<pre><code class="lang-auto">-------------------------------------
Translated Report (Full Report Below)
-------------------------------------

Process:               Slicer [3899]
Path:                  /Users/USER/Downloads/Slicer.app/Contents/MacOS/Slicer
Identifier:            org.slicer.slicer
Version:               5.0.1 (5.0.1)
Code Type:             X86-64 (Native)
Parent Process:        launchd [1]
User ID:               501

Date/Time:             2022-05-02 19:33:22.3666 -0400
OS Version:            macOS 12.3.1 (21E258)
Report Version:        12
Bridge OS Version:     6.4 (19P4243)
Anonymous UUID:        3797FBED-83D2-B47D-D4EA-26F22AA011DE


Time Awake Since Boot: 1300 seconds

System Integrity Protection: enabled

Crashed Thread:        0  CrBrowserMain  Dispatch queue: com.apple.main-thread

Exception Type:        EXC_BAD_ACCESS (SIGSEGV)
Exception Codes:       UNKNOWN_0xD at 0x0000000000000000
Exception Codes:       0x000000000000000d, 0x0000000000000000
Exception Note:        EXC_CORPSE_NOTIFY

Termination Reason:    Namespace SIGNAL, Code 11 Segmentation fault: 11
Terminating Process:   exc handler [3899]

VM Region Info: 0 is not in any region.  Bytes before following region: 4525027328
      REGION TYPE                    START - END         [ VSIZE] PRT/MAX SHRMOD  REGION DETAIL
      UNUSED SPACE AT START
---&gt;  
      __TEXT                      10db67000-10dba9000    [  264K] r-x/rwx SM=COW  .../MacOS/Slicer

Thread 0 Crashed:: CrBrowserMain Dispatch queue: com.apple.main-thread
0   libqSlicerBaseQTGUI.dylib     	       0x10e31a072 qSlicerApplicationPrivate::~qSlicerApplicationPrivate() + 146
1   libqSlicerBaseQTGUI.dylib     	       0x10e31a13e qSlicerApplicationPrivate::~qSlicerApplicationPrivate() + 14
2   libqSlicerBaseQTCore.dylib    	       0x10ec073e6 qSlicerCoreApplication::~qSlicerCoreApplication() + 38
3   Slicer                        	       0x10dba4b0f main + 527
4   dyld                          	       0x112fbf51e start + 462

&lt;cruft removed&gt;
</code></pre>

---

## Post #8 by @jcfr (2022-05-03 15:46 UTC)

<p>Thanks <a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> for the help, during today’s hangout we identified the issue and will be submitting a fix.</p>
<p>we will then release <code>v5.0.3</code></p>

---

## Post #9 by @jcfr (2022-05-03 16:33 UTC)

<p>To close the loop, here is the associated fix: <a href="https://github.com/Slicer/Slicer/pull/6348" class="inline-onebox">BUG: Fix on exit Segfault ensuring ExtensionsManagerDialog is deleted once by jcfr · Pull Request #6348 · Slicer/Slicer · GitHub</a></p>

---

## Post #10 by @che85 (2022-05-04 14:31 UTC)

<p>It turns out, that I had an outdated OpenSSL version installed which is the reason why I couldn’t install any extensions.</p>

---
