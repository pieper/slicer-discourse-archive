# Watershed, Fast marching, and Flood filling effects in Segment editor

**Topic ID**: 104
**Date**: 2017-04-13
**URL**: https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104

---

## Post #1 by @lassoan (2017-04-13 14:06 UTC)

<p>Three semi-automatic segmentation effects have added to the Segment editor. They are available in the latest nightly build, by installing the new SegmentEditorExtraEffects extension:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcd7e45bcb3ec95798c05e4aac7191ff76f21174.png" data-base62-sha1="qWAjhokjmVFt65j74WCBxLQxFYM" width="128" height="128"></p>
<p>They are all semi-automatic methods, which grow segmentation from seeds/points defined by the user.</p>
<p><strong>Watershed:</strong> similar to grow from seeds. Advantage: smoothness of the segments can be enforced. Disadvantage: much slower.</p>
<p>Input:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a871f85e08685c5fafc0c5a30364eb601f8fc92.png" data-base62-sha1="m311SZhQqYiJdLJfcS9MUVgcWBQ" width="596" height="399"></p>
<p>Preview:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9029072f77f5a988008adb42a859442728aab7b.png" data-base62-sha1="uXL6vwV9eErjJYUG4ohwc7H2an1" width="596" height="399"></p>
<p>Final result:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ab28d335fc3cba9efb3b44f951d2097e8edafdf.png" data-base62-sha1="m4w4FT57z6LIoYujlGcn4yVB2Kb" width="596" height="399"></p>
<p><strong>Fast marching:</strong> expands the current segment to regions with similar intensity.<br>
Input:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4dfba5f73866f0b34f9ae67fda654f805afa92e.png" data-base62-sha1="wEIcio9A3K3UILxtEXPsCYmeCHY" width="596" height="399"><br>
Output:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d56d5eed8efff2304fce059a2a27dc014b6db82.png" data-base62-sha1="1U0fBvwzB4LaTEfik5N5FPPxZoS" width="596" height="399"></p>
<p><strong>Flood filling:</strong> clicking in the image adds points around the click position to the current segment. Intensity tolerance is adjustable. Neighborhood size parameter can be used to prevent leakage.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79a696c16e778ab397483d7c1acd3576a98d4687.png" data-base62-sha1="hmaGIpyFTxoV6k3ceC8wYTanRUr" width="596" height="399"></p>

---

## Post #2 by @agirault (2017-04-13 19:21 UTC)

<p>That’s exciting, thank you <a class="mention" href="/u/lassoan">@lassoan</a>! Looking forward to testing those.</p>

---

## Post #3 by @lassoan (2017-08-02 13:05 UTC)

<p>2 posts were split to a new topic: <a href="/t/flood-filling-segment-editor-effect-does-not-fill-the-image/806">Flood filling segment editor effect does not fill the image</a></p>

---

## Post #4 by @monstercolorfun_co (2017-11-29 21:44 UTC)

<p>Hi, Perhaps I have some contributions to boost the processing times very much.</p>
<p>I researched about flood-fill recently and implemented an algorythm that was 10^1000000 times more efficient on memory instructions, using 3-4 of them, and multiple times faster than all previous versions that I found described on the web in codes whilst also being able to add codes from them too, and that could be speeded up by the 3D processes of the ones I found on the web. I wrote an account here: <a href="http://unity3dmc.blogspot.fr/2017/02/ultimate-3d-floodfill-scanline.html" rel="nofollow noopener">http://unity3dmc.blogspot.fr/2017/02/ultimate-3d-floodfill-scanline.html</a></p>

---

## Post #5 by @lassoan (2017-11-30 04:39 UTC)

<p><a class="mention" href="/u/monstercolorfun_co">@monstercolorfun_co</a> Thanks for sharing this.</p>
<p>For us, the main challenge is not computation time, as typically medical images that we work with consists of 100-200 million voxels, but a segmented structure is rarely bigger than a few 10 million voxels. Flood filling time is not noticeable.</p>
<p>Our problem is leaking: we often want to prevent flood filling to propagate through narrow bridges. <a href="https://www.vtk.org/doc/nightly/html/classvtkImageThresholdConnectivity.html">VTK’s flood fill filter</a> has an option for defining neighborhood size and minimum fill rate, but it’s not perfect, as it also removes small details from the filled region. Maybe it could be fixed easily (e.g., by expanding the final flood fill result by neighborhood size), but maybe a completely different approach would be needed.</p>
<p>If you were interested in exploring flood filling algorithms that don’t leak, and contribute an implementation using BSD-type license, then we would be happy to try it.</p>

---

## Post #6 by @Justin_Cramer (2018-06-01 16:48 UTC)

<p>I’d love to use these new tools but I can’t get the extension to work. I installed the SegmentEditorExtraEffects extension in the 4/9/2018 nightly build, did the restart, and the icons aren’t available. I uninstalled and reinstalled also, and gave it permission to install the MarkupsToModel dependency. Working in Windows 10. Thanks for any advice.</p>

---

## Post #7 by @lassoan (2018-06-01 17:34 UTC)

<p>Use the latest stable or the latest nightly. If you still have problems then send the application log (menu: Help / Report a bug).</p>

---

## Post #8 by @Justin_Cramer (2018-06-01 19:01 UTC)

<p>I’m using the build from 5/20. Here’s my error logs:</p>
<h2>After install, before restart:</h2>
<p>“Retrieving extension metadata [ extensionId: 225963]”<br>
“Downloading extension [ itemId: 360938]”<br>
“Retrieving extension metadata [ extensionId: 225914]”<br>
“Downloading extension [ itemId: 360889]”<br>
“Installed extension SegmentEditorExtraEffects (225963) revision b6cdcaa”<br>
“Installed extension MarkupsToModel (225914) revision a63c166”<br>
QPixmap::scaled: Pixmap is a null pixmap</p>
<h2>After restart:</h2>
<p>Session start time …: 2018-06-01 14:56:08<br>
Slicer version …: 4.9.0-2018-05-20 (revision 27197) win-amd64 - installed release<br>
Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
Memory …: 16309 MB physical, 19253 MB virtual<br>
CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Additional module paths …: C:/Users/Justin Cramer/AppData/Roaming/NA-MIC/Extensions-27197/SegmentEditorExtraEffects/lib/Slicer-4.9/qt-scripted-modules, C:/Users/Justin Cramer/AppData/Roaming/NA-MIC/Extensions-27197/MarkupsToModel/lib/Slicer-4.9/qt-loadable-modules<br>
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
libpng warning: iCCP: known incorrect sRGB profile<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module:  “SegmentEditor”<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
QPixmap::scaled: Pixmap is a null pixmap</p>

---

## Post #9 by @lassoan (2018-06-02 00:06 UTC)

<p>This version is not the latest nightly or latest stable version. Could you please test with both of these versions and let us know if they work?</p>

---

## Post #10 by @Justin_Cramer (2018-06-02 23:12 UTC)

<p>Ok, I tried it on latest stable (4.8.1) and nightly build from 6/1 with same result. I’ve pasted log from 4.8.1 attempt below. Have tried on 3 different Windows 10 machines with no difference. I don’t have access to OSX or Linux right now. Thanks again for your help.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 02.06.2018 18:08:55 [] (unknown:0) - Session start time .......: 2018-06-02 18:08:55
[DEBUG][Qt] 02.06.2018 18:08:55 [] (unknown:0) - Slicer version ...........: 4.8.1 (revision 26813) win-amd64 - installed
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Memory ...................: 16322 MB physical, 19266 MB virtual
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 16 logical processors
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Additional module paths ..: C:/Users/neurorad/AppData/Roaming/NA-MIC/Extensions-26813/SegmentEditorExtraEffects/lib/Slicer-4.8/qt-scripted-modules, C:/Users/neurorad/AppData/Roaming/NA-MIC/Extensions-26813/MarkupsToModel/lib/Slicer-4.8/qt-loadable-modules
[DEBUG][Python] 02.06.2018 18:08:56 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 02.06.2018 18:08:56 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 02.06.2018 18:08:57 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 02.06.2018 18:08:57 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 02.06.2018 18:08:57 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Number of registered modules: 141
[DEBUG][Qt] 02.06.2018 18:08:56 [] (unknown:0) - Number of instantiated modules: 141
[DEBUG][Qt] 02.06.2018 18:08:57 [] (unknown:0) - Number of loaded modules: 141
[DEBUG][Qt] 02.06.2018 18:08:57 [] (unknown:0) - Switch to module:  "SegmentEditor"
</code></pre>

---

## Post #11 by @lassoan (2018-06-03 00:52 UTC)

<p>I’ve just tried the nightly build on a Windows machine and the effects showed up correctly. Could you please post a screenshot of your screen when you switch to the Segment Editor module?</p>

---

## Post #12 by @Justin_Cramer (2018-06-03 17:59 UTC)

<p>Yeah I’m sure it’s something simple I’m overlooking but can’t figure it out. I rebooted…latest updates installed to Windows 10, otherwise fresh install of Slicer. It’s my impression that the extra tools show up as additional icons in the Segement Editor… Here are screenshots of Segment Editor and my Extensions manager:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b52419372f90b2c233cacba5b526e0211fa16550.png" data-download-href="/uploads/short-url/pQrLij5wL7O7fsFPZ4Fc3MUp0o8.png?dl=1" title="extensions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b52419372f90b2c233cacba5b526e0211fa16550_2_690x446.png" alt="extensions" data-base62-sha1="pQrLij5wL7O7fsFPZ4Fc3MUp0o8" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b52419372f90b2c233cacba5b526e0211fa16550_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b52419372f90b2c233cacba5b526e0211fa16550_2_1035x669.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b52419372f90b2c233cacba5b526e0211fa16550_2_1380x892.png 2x" data-dominant-color="FAFBFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">extensions</span><span class="informations">2995×1936 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3d5af0113fee953776d5fc6b1b163f126682f15.jpeg" data-download-href="/uploads/short-url/udYyNAGOhwqdwwEsirHT7cHML9X.jpg?dl=1" title="segment_editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d5af0113fee953776d5fc6b1b163f126682f15_2_690x441.jpg" alt="segment_editor" data-base62-sha1="udYyNAGOhwqdwwEsirHT7cHML9X" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d5af0113fee953776d5fc6b1b163f126682f15_2_690x441.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d5af0113fee953776d5fc6b1b163f126682f15_2_1035x661.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3d5af0113fee953776d5fc6b1b163f126682f15_2_1380x882.jpg 2x" data-dominant-color="909090"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment_editor</span><span class="informations">3000×1920 624 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2018-06-03 18:44 UTC)

<p>Yes, the extra icons should show up in the  Segment Editor module, but they don’t. Could you try to uninstall the extension, restart Slicer, and reinstall. When you reinstall, wait 1 minute before restarting Slicer, to make sure the extension is fully downloaded and installed.</p>
<p>If it still does not work then we can set up a meeting with remote desktop sharing during the coming week (just Send me a few timeslots that would work for you in a private message).</p>

---

## Post #14 by @lassoan (2018-06-04 17:43 UTC)

<p>Mystery solved: SegmentEditor module was set as startup module, so it was initialized immediately when Slicer started - before SegmentEditorExtraEffects extensions had a chance to register the additional effects.</p>
<p>I’ll push a fix for this soon, but until then the workaround is not to set SegmentEditor as startup module.</p>

---

## Post #15 by @lassoan (2018-06-05 14:18 UTC)

<p>Segment Editor initialization has been fixed (r27233), in nightly versions downloaded tomorrow or later, all effects will show up correctly in Segment Editor, even if it is used as startup module.</p>

---

## Post #16 by @cpinter (2018-06-05 14:29 UTC)

<p>Yaay for using Segment Editor as startup module <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #17 by @AndyM (2019-02-18 14:27 UTC)

<p>Hi these effects are so nice , and gives best output.<br>
i like to use python coding.<br>
Can i call/use this effects from Slicer python interactor?</p>

---

## Post #18 by @prorai (2019-02-22 13:38 UTC)

<p>Yes I’m also interested to use this by python code.</p>

---

## Post #19 by @lassoan (2019-02-22 14:37 UTC)

<aside class="quote no-group" data-username="AndyM" data-post="17" data-topic="104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7ab992/48.png" class="avatar"> AndyM:</div>
<blockquote>
<p>Can i call/use this effects from Slicer python interactor?</p>
</blockquote>
</aside>
<p>All Slicer features are available from Python scripting. See examples for using Segment Editor effects from Python in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #21 by @lassoan (2022-02-04 04:25 UTC)

<p>A post was split to a new topic: <a href="/t/algorithm-used-in-watershed-effect-in-segment-editor/21796">Algorithm used in Watershed effect in Segment Editor</a></p>

---
