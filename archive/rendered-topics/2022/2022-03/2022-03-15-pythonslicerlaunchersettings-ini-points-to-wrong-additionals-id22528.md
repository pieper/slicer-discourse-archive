---
topic_id: 22528
title: "Pythonslicerlaunchersettings Ini Points To Wrong Additionals"
date: 2022-03-15
url: https://discourse.slicer.org/t/22528
---

# `PythonSlicerLauncherSettings.ini` points to wrong `additionalSettingsFilePath`

**Topic ID**: 22528
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/pythonslicerlaunchersettings-ini-points-to-wrong-additionalsettingsfilepath/22528

---

## Post #1 by @keri (2022-03-15 19:06 UTC)

<p>Hi,</p>
<p>It seems that in SlicerCAT the Python settings file <code>PythonSlicerLauncherSettings.ini-&gt;additionalSettingsFilePath</code> (located in <code>d/python-install/bin/</code>) points to the unexistent file:<br>
<code>d/slicersources-build/Slicer-build/SlicerLauncherSettings.ini</code></p>
<p>as I understand it should point to:<br>
<code>d/Slicer-build/[SlicerCAT]LauncherSettings.ini</code></p>
<p>As a result if I simply run <code>PythonSlicer</code> without slicer GUI then I have no initialized paths/env vars.</p>
<p>SlicerCAT built with Slicer <code>main</code> branch at latest git commit <code>5e6a904aea97578ce91d0c7ebc0d9c2af11472bb</code><br>
Ubuntu 20.04</p>

---

## Post #2 by @keri (2022-03-15 22:56 UTC)

<p>Almost the same problem with the <code>SlicerDesignerLauncherSettings.ini</code>.</p>
<p><strong>Let me explain a little bit:</strong><br>
as I understand <a href="https://github.com/Slicer/Slicer/blob/d14f18f386f83943d6717cedb5d18f1ce423cada/CMake/SlicerCPack.cmake#L88" rel="noopener nofollow ugc">SlicerCPack.cmake</a> is responsible for building the files <code>SlicerDesignerLauncherSettings.ini</code> and <code>PythonSlicerLauncherSettings.ini</code>.</p>
<p>From the above link you can see <code>ADDITIONAL_SETTINGS_FILEPATH_BUILD "${Slicer_BINARY_DIR}/${Slicer_BINARY_INNER_SUBDIR}/SlicerLauncherSettings.ini"</code> (for both Designer and Python)</p>
<p>Then I go <strong>/d/CMakeCache.cmake</strong> and I can see:<br>
<code>Slicer_BINARY_DIR:STATIC=/home/kerim/Documents/Colada/d/slicersources-build</code></p>
<p>And in <strong>/d/Slicer-Build/CMakeCache.cmake</strong>:<br>
<code>Slicer_BINARY_DIR:STATIC=/home/kerim/Documents/Colada/d/Slicer-build</code></p>
<p>Then in the main <strong>CMakeLists.txt</strong> you can find that <a href="https://github.com/Slicer/Slicer/blob/d14f18f386f83943d6717cedb5d18f1ce423cada/CMakeLists.txt#L74" rel="noopener nofollow ugc">Slicer_BINARY_INNER_SUBDIR</a> points to:<br>
<code>set(Slicer_BINARY_INNER_SUBDIR Slicer-build)</code></p>
<p>I believe that is the root of the problem.<br>
When configuring Pythons settings file the var <code>Slicer_BINARY_DIR</code> is set to <code>slicersources-build</code>.<br>
And when configuring the Designer script it is set to <code>Slicer-build</code> dir.</p>
<p>The second point is that for Custom APP <code>SlicerLauncherSettings.ini</code>  is renamed to <code>[SlicerCAT]LauncherSetting.ini</code>. Thus it should be renamed within <code>SlicerCPack.cmake</code> function (accept some variable with app name).<br>
App renaming also concerns the <a href="https://github.com/Slicer/Slicer/blob/d14f18f386f83943d6717cedb5d18f1ce423cada/CMake/SlicerCPack.cmake#L92" rel="noopener nofollow ugc">LauncherInstall.ini</a></p>
<p>Please take a look. If I’m right I could work on that</p>

---

## Post #3 by @lassoan (2022-03-17 01:24 UTC)

<p>I haven’t been developing SlicerCAT-based applications recently. Maybe <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> or <a class="mention" href="/u/cpinter">@cpinter</a> can confirm if they can reproduce the issue (and if yes then why it does not impact their workflow). Most likely a fix is needed and it would be useful if you could work on that and submit a pull request.</p>

---

## Post #4 by @cpinter (2022-03-17 09:46 UTC)

<p>Hi! It seems you made good progress with investigating the root cause. I think the easiest would be if you submitted a pull request with the solution you find best and we can discuss the details there.</p>
<p>I haven’t encountered these issues because I don’t use PythonSlicer alone, and I launch designer from a normal Slicer build (the widget xml descriptors are the same so any reasonably recent Slicer-launched designer works the same).</p>
<p>Thanks!</p>

---

## Post #5 by @keri (2022-03-19 02:03 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/6274" rel="noopener nofollow ugc">PR is created</a></p>

---
