---
topic_id: 47030
title: "Problems with extension manager"
date: 2026-05-14
url: https://discourse.slicer.org/t/47030
last_bumped: 2026-05-18T17:21:36.701Z
---

# Problems with extension manager

**Topic ID**: 47030
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/problems-with-extension-manager/47030

---

## Post #1 by @jaimigray (2026-05-14 15:10 UTC)

<p>Hi team! I’m having some problems with Slicer not loading the extensions manager correctly. This is happening with newer and older versions of slicer. When I launch Slicer, it opens a separate blank window called “vtkOutputWindow”, and when I launch the extension manager, some weird triangle things briefly flash across the screen, and then the extension manager window loads, but I can’t see any of my extension or install anymore, it’s just a blank window with tabs but no extension icons. Is this a problem with my PC, and if so how do I fix it?</p>

---

## Post #2 by @muratmaga (2026-05-14 16:36 UTC)

<p>There were some problems with the extension manager for a short interval. But as far as I know it works fine for current stable and preview for the time being.</p>
<p>What it would help.</p>
<ol>
<li>The version(s) of Slicer you are using and the operating system</li>
<li>Whether you are behind a corporate/university network or on your own home (if you didn’t try switching networks)</li>
<li>And the logs from problematic Slicer sessions.</li>
</ol>

---

## Post #3 by @jaimigray (2026-05-18 13:22 UTC)

<p>Hi Murat,</p>
<p>This was happening with the current preview version, and I also went back and tried with versions 5.9 and 5.10, and had the same issue.</p>
<p>I have tried on my PC, connected to the UT vpn and also disconnected from the vpn. The issue occurred with both. It is only happening on my own PC, I am still able to use Slicer on our image processing lab PCs.</p>
<p>LOG:</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Session start time …: 20260518_081842</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Slicer version …: 5.11.0-2026-02-23 (revision 34437 / 2938bea) win-amd64 - installed release</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Operating system …: Windows / Professional / (Build 26200, Code Page 65001) - 64-bit</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Memory …: 64980 MB physical, 69076 MB virtual</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - CPU …: GenuineIntel , 22 cores, 22 logical processors</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - DCMTK configuration …: version 3.7.0, no SSL</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Internationalization …: disabled, language=</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Developer mode …: disabled</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Application path …: C:/Users/jag9357/AppData/Local/slicer.org/3D Slicer 5.11.0-2026-02-23/bin</p>
<p>[DEBUG][Qt] 18.05.2026 08:18:42 [] (unknown:0) - Additional module paths ..: <a href="http://slicer.org/Extensions-34437/Sandbox/lib/Slicer-5.11/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/Sandbox/lib/Slicer-5.11/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34437/Sandbox/lib/Slicer-5.11/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/Sandbox/lib/Slicer-5.11/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34437/MorphoDepot/lib/Slicer-5.11/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/MorphoDepot/lib/Slicer-5.11/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34437/SegmentEditorExtraEffects/lib/Slicer-5.11/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/SegmentEditorExtraEffects/lib/Slicer-5.11/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34437/SegmentEditorExtraEffects/lib/Slicer-5.11/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/SegmentEditorExtraEffects/lib/Slicer-5.11/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34437/SlicerMorph/lib/Slicer-5.11/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/SlicerMorph/lib/Slicer-5.11/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-34437/SurfaceMarkup/lib/Slicer-5.11/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/SurfaceMarkup/lib/Slicer-5.11/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34437/MarkupsToModel/lib/Slicer-5.11/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/MarkupsToModel/lib/Slicer-5.11/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-34437/SurfaceWrapSolidify/lib/Slicer-5.11/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-34437/SurfaceWrapSolidify/lib/Slicer-5.11/qt-scripted-modules</a></p>
<p>[INFO][Stream] 18.05.2026 08:18:44 [] (unknown:0) -</p>
<p>[WARNING][Python] 18.05.2026 08:19:02 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Python\Lib\site-packages\pydicom\misc.py:82) - get_frame_offsets is deprecated and will be removed in v4.0</p>
<p>[WARNING][Qt] 18.05.2026 08:19:04 [] (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[DEBUG][Python] 18.05.2026 08:19:06 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Python\Lib\site-packages\git\cmd.py:1270) - Popen([‘git’, ‘version’], cwd=C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23, stdin=None, shell=False, universal_newlines=False)</p>
<p>[DEBUG][Python] 18.05.2026 08:19:06 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Python\Lib\site-packages\git\cmd.py:1270) - Popen([‘git’, ‘version’], cwd=C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23, stdin=None, shell=False, universal_newlines=False)</p>
<p>[WARNING][Qt] 18.05.2026 08:19:07 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>
<p>[WARNING][Qt] 18.05.2026 08:19:11 [] (unknown:0) - void __cdecl ctkComboBox::setCurrentUserDataAsString(class QString) : No item found with user data string “5”</p>
<p>[DEBUG][Python] 18.05.2026 08:19:11 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Slicer-5.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 18.05.2026 08:19:11 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Slicer-5.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[DEBUG][Qt] 18.05.2026 08:19:11 [] (unknown:0) - Switch to module: “Welcome”</p>
<p>[DEBUG][Python] 18.05.2026 08:19:13 [Python] (C:\Users\jag9357\AppData\Local\slicer.org\3D Slicer 5.11.0-2026-02-23\lib\Slicer-5.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: FormatMarkups</p>
<p>[INFO][Python] 18.05.2026 08:19:13 [Python] (:3) - Adding SlicerMorph Volume Rendering Presets</p>
<p>[WARNING][Qt] 18.05.2026 08:19:18 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.</p>
<p>[WARNING][Qt] 18.05.2026 08:19:18 [] (unknown:0) - Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!</p>
<p>[WARNING][Qt] 18.05.2026 08:19:19 [] (unknown:0) - Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!</p>
<p>[WARNING][Qt] 18.05.2026 08:19:21 [] (unknown:0) - A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a> was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a> and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>.</p>

---

## Post #4 by @muratmaga (2026-05-18 15:59 UTC)

<p>if this is happening with other versions, that it should be a problem with your computer settings. But I don’t know what it might cause, Claude thinks it is a “GPU driver’” or wrong GPU issue. I pasted here the suggestions, might be worthwhile to give a try as they are pretty simple:</p>
<p><code>An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile.</code></p>
<p>Combined with the standalone <strong>vtkOutputWindow</strong> opening, the briefly-flashing triangles, and the <strong>blank extension manager</strong> (which is a Qt WebEngine / Chromium view that needs working hardware-accelerated OpenGL), this is almost certainly a <strong>GPU / OpenGL driver problem on that specific PC</strong> — not a Slicer bug, not a network/VPN issue, and not something tied to a particular Slicer version (which is why 5.9, 5.10, and the preview all behave the same, and why lab PCs are fine).</p>
<p>Likely root causes, most common first:</p>
<ol>
<li>
<p><strong>Outdated, broken, or wrong GPU driver.</strong> Update via the vendor utility (NVIDIA GeForce Experience / NVIDIA App, AMD Adrenalin, or Intel Driver &amp; Support Assistant). Don’t rely on Windows Update — it ships stale OpenGL drivers. If a recent driver was just installed, try a clean reinstall (DDU in safe mode, then vendor installer) or roll back to the previous version.</p>
</li>
<li>
<p><strong>Slicer running on integrated GPU instead of the dedicated one.</strong> Windows Settings → System → Display → Graphics → find/add <code>SlicerApp-real.exe</code> (in <code>…\3D Slicer 5.11.0-…\bin\</code>) → set to “High performance”. Reboot, relaunch.</p>
</li>
<li>
<p><strong>Remote-desktop / display-mirroring / GPU-virtualization software</strong> (Parsec, Sunshine, NVIDIA Broadcast/Game Filter overlay, monitor-calibration utilities, OBS virtual camera hooks) intercepting the OpenGL context. Try with those quit.</p>
</li>
<li>
<p><strong>Corrupt OpenGL/D3D translation layer</strong> — uninstalling and reinstalling Slicer into a fresh folder, after clearing <code>%LOCALAPPDATA%\NA-MIC\</code> settings, occasionally clears stuck state.</p>
</li>
</ol>
<p>Quick diagnostic you can suggest: in Slicer, Help → “Report a bug” or in the Python console run <code>import vtk; print(vtk.vtkRenderWindow().ReportCapabilities())</code> after opening a 3D view — the OpenGL vendor/renderer line will reveal whether Slicer is sitting on the integrated GPU or a software rasterizer (Microsoft Basic / llvmpipe), which would confirm the diagnosis.</p>

---

## Post #5 by @jamesobutler (2026-05-18 16:30 UTC)

<aside class="quote no-group" data-username="jaimigray" data-post="1" data-topic="47030">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar"> jaimigray:</div>
<blockquote>
<p>it opens a separate blank window called “vtkOutputWindow”</p>
</blockquote>
</aside>
<p>^This is unrelated to your issue and something recently fixed in <a href="https://github.com/Slicer/Slicer/commit/180437e360c078617270f4d84ccda9f0e0edb779" class="inline-onebox" rel="noopener nofollow ugc">ENH: Do not log warning if cache file location is default · Slicer/Slicer@180437e · GitHub</a> .</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="47030">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><strong>Slicer running on integrated GPU instead of the dedicated one.</strong> Windows Settings → System → Display → Graphics → find/add <code>SlicerApp-real.exe</code> (in <code>…\3D Slicer 5.11.0-…\bin\</code>) → set to “High performance”. Reboot, relaunch.</p>
</blockquote>
</aside>
<p>^Slicer already by default sets this setting to “High performance” as of <a href="https://github.com/Slicer/Slicer/commit/fd55fbc130a45d5f85e0e04b294d2a8169bc811d" class="inline-onebox" rel="noopener nofollow ugc">ENH: Set Windows registry key to use high performance graphics · Slicer/Slicer@fd55fbc · GitHub</a> .</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="47030">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>uninstalling and reinstalling Slicer into a fresh folder, after clearing <code>%LOCALAPPDATA%\NA-MIC\</code> settings,</p>
</blockquote>
</aside>
<p>^This is describing an old location. The correct location for recent versions is <code>%LOCALAPPDATA%\slicer.org</code></p>
<p>I would suspect your issue is actually related to the policies applied to your computer about what sites it can load including the backend that hosts the extension manager. There are some explanations of this topic at the below link. Has the extension manager worked previously on this specific computer you are using? Or is it a newly set up computer and/or are you on a new academic/corporate network which often applies restrictive web policies? I often face my own issues in a corporate network that blocks successful download of packages from the extensions manager.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/user_guide/extensions.html#extensions-manager-does-not-show-any-extensions">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions.html#extensions-manager-does-not-show-any-extensions" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions.html#extensions-manager-does-not-show-any-extensions" target="_blank" rel="noopener nofollow ugc">Error retrieving extension metadata - Extensions — 3D Slicer  documentation</a></h3>

  <p>When starting the extensions manager, the “Extensions manager is starting, please wait…” message is displayed immediately and normally list of extensions should show up within 10-20 seconds. If startup takes longer (several minutes) then most likely...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @jaimigray (2026-05-18 17:21 UTC)

<p>Thanks for the info. I’m using a laptop that was provided to me by UT. After what you said, I just tried running Slicer as administrator and did not have any problems with the extension manager.</p>
<p>I have not had to do this previously, and have been running multiple versions of Slicer on this PC over the past two years with no issues. UT is always pushing updates to it, and I think it was after one of those that the issue arose. For now, I can work around it by running Slicer as administrator.</p>

---
