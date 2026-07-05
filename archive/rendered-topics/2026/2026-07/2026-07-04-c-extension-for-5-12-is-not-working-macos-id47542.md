---
topic_id: 47542
title: "C++ extension for 5.12 is not working (MacOS)"
date: 2026-07-04
url: https://discourse.slicer.org/t/47542
last_bumped: 2026-07-04T16:16:32.211Z
---

# C++ extension for 5.12 is not working (MacOS)

**Topic ID**: 47542
**Date**: 2026-07-04
**URL**: https://discourse.slicer.org/t/c-extension-for-5-12-is-not-working-macos/47542

---

## Post #1 by @muratmaga (2026-07-04 05:27 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/lassoan">@lassoan</a> this is urgent:</p>
<p>I just downloaded 5.12 for my MacOS, and quite a few of the C++ extension are installed but non-functional for due to library mismatch. I need these extensions for my SlicerMorph workshop starting on Monday:</p>
<ol>
<li>SurfaceMarkups</li>
<li>Model2Model distance</li>
<li>Markups2Models</li>
<li>Sandbox</li>
<li>SegmentEditorExtraEffects</li>
</ol>
<p>[Qt] Error(s):</p>
<p>[Qt] Cannot load library /Applications/Slicer.app/Contents/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.dylib, 0x0085): Library not loaded: <span class="mention">@rpath</span>/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib</p>
<p>[Qt] Referenced from:  /Applications/Slicer.app/Contents/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.dylib</p>
<p>[Qt] Reason: tried: ‘/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/Frameworks/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/Frameworks/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/MacOS/../Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file))</p>
<p>[Qt] Error(s):</p>
<p>[Qt] Cannot load library /Applications/Slicer.app/Contents/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: <span class="mention">@rpath</span>/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib</p>
<p>[Qt] Referenced from: &lt;9E032141-621C-3FE9-9137-A62E008DB619&gt; /Applications/Slicer.app/Contents/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib</p>
<p>[Qt] Reason: tried: ‘/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/Frameworks/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/Frameworks/QtCore.framework/Versions/5/Frameworks/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/MacOS/../Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/MarkupsToModel/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file))</p>
<p>dlopen(/Applications/Slicer.app/Contents/Extensions-34621/Sandbox/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerCombineModelsModuleLogicPython.so, 0x0002): Library not loaded: <span class="mention">@rpath</span>/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib</p>
<p>Referenced from:  /Applications/Slicer.app/Contents/Extensions-34621/Sandbox/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerCombineModelsModuleLogicPython.so</p>
<p>Reason: tried: ‘/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/MacOS/../Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/Sandbox/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file)</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>dlopen(/Applications/Slicer.app/Contents/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerSegmentEditorFastMarchingModuleLogicPython.so, 0x0002): Library not loaded: <span class="mention">@rpath</span>/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib</p>
<p>Referenced from: &lt;76343D83-A509-3A6C-8A39-11770DC16B0A&gt; /Applications/Slicer.app/Contents/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerSegmentEditorFastMarchingModuleLogicPython.so</p>
<p>Reason: tried: ‘/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/qRestAPI-build/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/qRestAPI-build/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/Applications/Slicer.app/Contents/MacOS/../Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/CTK-build/CMakeExternals/Install/lib/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file), ‘/System/Volumes/Preboot/Cryptexes/OS/D/S/A/teem-build/bin/Extensions-34621/SegmentEditorExtraEffects/lib/Slicer-5.12/libopenjp2.7.dylib’ (no such file)</p>

---

## Post #2 by @muratmaga (2026-07-04 05:39 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> This is claude’s diagnosis:</p>
<p>This is a <strong>known Slicer packaging bug on macOS</strong>, not a problem with your install or with SurfaceMarkup specifically — and I confirmed it directly on your machine: every C++ loadable extension you have installed (<strong>SurfaceMarkup, MarkupsToModel, Sandbox, SegmentEditorExtraEffects</strong>) has the same defect, so they will all fail to load the same way.</p>
<p><strong>The chain of causes:</strong></p>
<ol>
<li>Slicer 5.12 ships DCMTK with JPEG 2000 support via OpenJPEG. DCMTK’s <code>dcmjp2kcs</code> module exported <code>openjp2</code> in its <em>public</em> CMake link interface, so every extension that links anything DCMTK-related (which is essentially any C++ extension, via the Slicer base libraries) ends up with a direct load command on <code>libopenjp2.7.dylib</code> — even though none of them use JPEG 2000. I verified with <code>otool -L</code>: your SurfaceMarkup module directly references <code>@rpath/Extensions-34621/SurfaceMarkup/lib/Slicer-5.12/libopenjp2.7.dylib</code>.</li>
<li>The extension packaging step rewrites that reference to point inside the extension’s own lib folder, but <strong>never copies <code>libopenjp2.7.dylib</code> into the extension package</strong>. The file simply isn’t there, so <code>dlopen</code> fails and the module doesn’t load. (The garbage “tried: /D/S/A/teem-build/…” paths are leftover rpaths from the factory build machine — a red herring.)</li>
</ol>
<p>This was fixed upstream three days ago in <a href="https://github.com/Slicer/Slicer/pull/9263" rel="noopener nofollow ugc">Slicer PR #9263</a> (merged 2026-06-30, to <code>main</code>), which makes DCMTK link OpenJPEG privately — the PR description even cites MarkupsToModel as the affected example. A related fix, <a href="https://github.com/Slicer/Slicer/pull/9228" rel="noopener nofollow ugc">PR #9228</a>, addressed the missing lib in the main app package. Because the 5.12 stable app (rev 34621) is already released, the extensions built for it still carry the over-linked reference until the factory’s stable build tree picks up the fix and rebuilds the extensions.</p>

---

## Post #3 by @jamesobutler (2026-07-04 10:53 UTC)

<p>Indeed this issue is present for specifically macOS when using Slicer 5.12. It was fixed in the recent preview. For Monday you’ll either need to use latest Slicer Preview or continue to use Slicer 5.10.</p>
<p>A Slicer 5.12.1 won’t be finalized yet for Monday.</p>

---

## Post #4 by @lassoan (2026-07-04 11:25 UTC)

<p>Sorry for the inconvenience. Automated testing and testing on developer computers did not detect this issue, as it only appears if the application is installed, on macOS, when the extension contain loadable modules.</p>
<p>You can use other versions, as <a class="mention" href="/u/jamesobutler">@jamesobutler</a> described. Some more details:</p>
<p>If convenient installation is important then Slicer-5.10 is the better option, because it is signed, so you don’t need jump through a lot of hoops to allow installation. → <a href="https://download.slicer.org/?version=5.10" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>
<p>If you need some of the latest features or fixes then you can use yesterday’s preview release. Don’t use the very latest version, because depending on the time of day, the extension on macOS may not be available yet (due to some macOS factory issue, which will be fixed in the next couple of days by replacing the machine). → <a href="https://download.slicer.org/?date=2026-06-30" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>

---

## Post #5 by @muratmaga (2026-07-04 13:17 UTC)

<p>Unfortunately 5.10 lacks some of the features so it is not an option. And I don’t want to make people to download multiple versions either.</p>
<p>I am curious why it takes so long to build the stable. Looks like PR is from 3 days ago?</p>

---

## Post #6 by @pieper (2026-07-04 14:43 UTC)

<p>It’s not the build time, it’s the manual steps required to sign and update things that make it a bit of a pain now to generate a patch release.</p>
<p>For Monday I’d suggest just using the Preview build and removing the quarantine flag on macs.</p>
<p>People can just do <code>xattr -dr com.apple.quarantine /Applications/Slicer.app</code></p>

---

## Post #7 by @lassoan (2026-07-04 16:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="47542">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>And I don’t want to make people to download multiple versions either</p>
</blockquote>
</aside>
<p>There is no need for multiple versions. Everyone can download the same working Slicer Preview Release from this link: <a href="https://download.slicer.org/?date=2026-07-02">https://download.slicer.org/?date=2026-07-02</a>.</p>
<p>The annoying part is the 4-5 extra clicks needed for installing an unsigned package on Windows and macOS. On macOS those extra clicks are in System Settings (or need to type the terminal as <a class="mention" href="/u/pieper">@pieper</a> described above).</p>

---
