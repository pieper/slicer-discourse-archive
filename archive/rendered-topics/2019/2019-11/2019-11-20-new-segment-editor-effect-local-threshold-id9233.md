# New Segment Editor effect: Local threshold

**Topic ID**: 9233
**Date**: 2019-11-20
**URL**: https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233

---

## Post #1 by @Sunderlandkyl (2019-11-20 17:01 UTC)

<p>Local threshold, a new semi-automatic segmentation method, has been added to the Segment Editor. It is available in both the 4.11.0 and 4.10.2 releases through the SegmentEditorExtraEffects extension. This effect adds connected voxels to segments that are within a specified threshold, and attempts to prevent leaks into other structures through small connecting regions. The result is similar to that of the “Level trace” effect in that it delineates a region within a certain threshold value, however this effect is applied in 3D.</p>
<div class="lazyYT" data-youtube-id="cevlMLyhfK8" data-youtube-title='Segment Editor: New "Local threshold" effect' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>The initial behavior is similar to the threshold effect. Users can specify a threshold range manually, or by drawing on the image to create a histogram (see info <a href="https://discourse.slicer.org/t/new-feature-histogram-for-setting-threshold-range-in-segment-editor/9221">here</a>). Instead of clicking “Apply”, CTRL+clicking on a specific region performs a flood fill using one of 3 algorithms, adding the structure to the current segment:</p>
<ul>
<li>Masking</li>
<li>GrowCut</li>
<li>WaterShed</li>
</ul>
<p>Two additional parameters are also available to prevent leaks:</p>
<ul>
<li>Feature size: Used to separate structures that are connected by regions smaller than the size specified</li>
<li>ROI: Only voxels within the region of interest will be filled</li>
</ul>
<p>Suggestions and feedback are welcome.</p>
<p>Development was funded in part by CANARIE’s Research Software Program, OpenAnatomy, and Brigham and Women’s Hospital through NIH grant R01MH112748.</p>

---

## Post #2 by @sarvpriya1985 (2019-11-28 14:52 UTC)

<p>Hi,</p>
<p>I found it a very nice feature. However, while trying to use it, i found that after selecting a threshold and ctrl plus left click-it doesn’t do anything. I mean no filling is done. Is there anything I am missing?</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #3 by @Sunderlandkyl (2019-11-28 15:23 UTC)

<p>Local threshold effect attempts to reduce leaking and separates the structure that you clicked on by eroding the thresholded area by the “feature size” parameter.</p>
<p>If the area under the mouse would be eroded away, then the local threshold effect will not find the structure. If you reduce the “feature size” parameter, or make sure to click in a non-eroded region, than it should help find the structure.</p>

---

## Post #4 by @hherhold (2020-05-09 13:51 UTC)

<p>Late reply and perhaps this is documented somewhere else, but on MacOS it is command-click to add, not control-click.</p>
<p>Most excellent feature, by the way. Thanks!</p>

---

## Post #5 by @sfglio (2020-06-25 16:44 UTC)

<p>I still don’t succeed on MacOS:<br>
After selecting the right threshold and after I click cmd+left mouse button it does not add the blinking area to the segmentation?<br>
anyone has a solution for that behaviour?</p>

---

## Post #6 by @hherhold (2020-06-25 17:01 UTC)

<p>Did you try it with a sample data download like from the video?</p>

---

## Post #7 by @sfglio (2020-06-25 19:58 UTC)

<p>Yes! But I don’t get it: pressing cmd+left click (I assume mouse left click) - where (in which window) and when should I press these buttons???</p>
<p>e.g if I use level tracing than I just need to left-click on the mouse and I immediately see the segmented area - however in local threshold the region is getting lighter and darker green constantly but if I press cmd+left click nothing happens…<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22141b7923c3bb337dbf1d8dfe99f0c5584e5705.png" data-download-href="/uploads/short-url/4RtjrX8sDJY3xuTRfIPKddBMx4p.png?dl=1" title="Bildschirmfoto 2020-06-25 um 21.54.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22141b7923c3bb337dbf1d8dfe99f0c5584e5705_2_448x500.png" alt="Bildschirmfoto 2020-06-25 um 21.54.49" data-base62-sha1="4RtjrX8sDJY3xuTRfIPKddBMx4p" width="448" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22141b7923c3bb337dbf1d8dfe99f0c5584e5705_2_448x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22141b7923c3bb337dbf1d8dfe99f0c5584e5705.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22141b7923c3bb337dbf1d8dfe99f0c5584e5705.png 2x" data-dominant-color="8A8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-06-25 um 21.54.49</span><span class="informations">572×638 93.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-06-25 20:34 UTC)

<p>That part that you Ctrl-Click on is added to the segment. If nothing is added then it means that the region found at the clicked position is smaller than the feature size. You need to extend the threshold range or decrease “Feature size”.</p>

---

## Post #9 by @sfglio (2020-06-26 08:37 UTC)

<p>In the meantime I accidentially! managed to add a part to the segment, however repeating fails…no matter what feature size I choose (1-10cm) for my threshold, I can’t segment the implant.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03056cca488f6fb42aaa3ecd07c2b9abb885c025.png" data-download-href="/uploads/short-url/qJ3qIAsx5by0blXcKFevj8qzmR.png?dl=1" title="Bildschirmfoto 2020-06-26 um 10.34.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03056cca488f6fb42aaa3ecd07c2b9abb885c025_2_690x341.png" alt="Bildschirmfoto 2020-06-26 um 10.34.55" data-base62-sha1="qJ3qIAsx5by0blXcKFevj8qzmR" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03056cca488f6fb42aaa3ecd07c2b9abb885c025_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03056cca488f6fb42aaa3ecd07c2b9abb885c025_2_1035x511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03056cca488f6fb42aaa3ecd07c2b9abb885c025_2_1380x682.png 2x" data-dominant-color="CDCDD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2020-06-26 um 10.34.55</span><span class="informations">1674×828 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Sunderlandkyl (2020-06-26 14:19 UTC)

<p>Have you tried lowering the feature size all the way to 0?</p>

---

## Post #11 by @sfglio (2020-06-28 19:52 UTC)

<p>Thanks for this hint! now it works very smooth!</p>
<p>I want to most accurately segment the implants (as shown in the figure above) in order to measure the blooming artefact - which algorithm would be the one of choice?<br>
e.g. after using watershed, creating a labelmap and superimposing it with the original scan -&gt; I still can see a thin (white/greyish) border around my segmented implant before the adjacent black circle.<br>
Or would you recommend any other algorithm in order to measure blooming?</p>

---

## Post #12 by @lassoan (2020-06-28 20:15 UTC)

<p>The “difference” is probably not real, it is probably just a result of using linear interpolation for grayscale volumes and nearest neighbor interpolation for segmentation’s binary labelmap representation. You can verify this by disabling interpolation for the volume. You can reduce the difference between these interpolations by reducing the pixel spacing of the input volume (for example, by using Crop volume module) before you start segmentation.</p>

---

## Post #13 by @doc-xie (2020-08-12 07:15 UTC)

<p>Hi Kyle Sunderland,<br>
A very nice function in Local Threshold. But I found it is difficult to understand clearly.How to define the Minimum, Lower, Average, Upper and Maximum value in Local histogram? What the meaning about the red line,  yellow line and the curve between them? Moreover, how to set the Feature Size basing on the Volume?<br>
Thanks,<br>
Dr.Xie</p>

---

## Post #14 by @Sunderlandkyl (2020-08-12 14:26 UTC)

<p>The histogram represents the voxel intensities within the selected region of the image. The red lines on the left and right represent the minimum and maximum voxel intensities in the selected region, while the the the yellow line represents the average intensity. The yellow highlight underneath the histogram shows the current threshold range.</p>
<p>Clicking and dragging on the histogram will let you manually specify the minimum/maximum intensities. The average then becomes the median intensity between the two. Right clicking on the histogram will cancel the manual selection.</p>
<p>If you would like finer control over the threshold range, the threshold range slider can be used without, or in conjunction with the histogram to specify the range.</p>
<p>The required feature size depends on the structure being segmented. A larger feature sizes will prevent leaking through regions that are smaller than the feature size, however for thin structures, a feature size that is larger than the thinnest regions will result in the branches being truncated.</p>

---

## Post #15 by @lassoan (2020-08-12 14:49 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> This is an excellent summary! It would be great if you could add that to <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/README.md">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/README.md</a> (maybe with an additional annotated screenshot). This documentation will be moved to Slicer core documentation when the effect is moved into the Slicer core.</p>

---

## Post #16 by @Henry_Cope (2020-08-24 13:45 UTC)

<p>Hi, I’m trying to use this effect as it is used in your video, but I’m unable to draw a region in the image to obtain a local histogram, nor do I have the local histogram graph visible. Did I somehow not install the correct extension? This is what my control panel looks like:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de771c8fc27a9f0fc61e67f41e04c43e093fd98d.png" data-download-href="/uploads/short-url/vK1c0XBdIje6CnBPSnSxRJV7c7P.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de771c8fc27a9f0fc61e67f41e04c43e093fd98d.png" alt="image" data-base62-sha1="vK1c0XBdIje6CnBPSnSxRJV7c7P" width="331" height="500" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">546×823 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @Sunderlandkyl (2020-08-24 13:51 UTC)

<p><a class="mention" href="/u/henry_cope">@Henry_Cope</a> which version of Slicer are you using? The Histogram is not available in Slicer 4.10.2.</p>

---

## Post #18 by @Henry_Cope (2020-08-24 13:52 UTC)

<p>Ah then that’s the issue! I’m using 4.10.2.<br>
Thank you</p>

---

## Post #19 by @Fadilalat (2020-09-28 13:28 UTC)

<p>Hi! I’m new to slicer and an amateur in this field. But I would like to download the local threshold effect into my slicer (4.10.2). I’ve tried, but I can’t seem to figure it out. Could you maybe help?</p>
<p>Thankyou in advance!</p>

---

## Post #20 by @lassoan (2020-09-28 13:33 UTC)

<p>It is available for Slicer-4.11 version only.</p>

---

## Post #21 by @Nora (2020-11-05 11:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="9233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>added to the segment. If nothing is added then it means that the region found at the clicked positio</p>
</blockquote>
</aside>
<p>Hi all,</p>
<p>This extension sounds promising.</p>
<p>I have few issues though.<br>
So first, I draw a circle around my ROI then I edit the threshold of the local histogram. But how can I save the segment? I tried Ctrl + left click, the area keep blinking.</p>
<p>Another question please, is there any way to use fixed threshold (like 40% of SUVmax in PET)?</p>
<p>Appreciate your help,</p>

---

## Post #22 by @hherhold (2020-11-05 11:34 UTC)

<p>Sounds like you might be on a Mac - it is command + left click for MacOS.</p>

---

## Post #23 by @Buyck (2021-01-05 07:09 UTC)

<p>There seems to be a problem with the installation of the SegmentEditorExtraEffects extension on my Slicer (v. 4.11.20200930). Once installed the “Local Thresholding” tool does not apear amongst my new segmenting tools.</p>
<p>I have already tried:</p>
<ul>
<li>re-installing the program after complete deletion of the program and its files</li>
<li>re-installing the extension</li>
<li>restarting my pc</li>
<li>installing older versions of Slicer</li>
</ul>
<p>Nothing worked…</p>
<p>Can someone help me to obtain the Local Threshold tool?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52bc864d09136f3007429540d727b07a6e459155.jpeg" data-download-href="/uploads/short-url/bNV40HaN4GLbMzTMADINMbNUFOB.jpeg?dl=1" title="Screenshot 2021-01-05 080555" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52bc864d09136f3007429540d727b07a6e459155_2_690x354.jpeg" alt="Screenshot 2021-01-05 080555" data-base62-sha1="bNV40HaN4GLbMzTMADINMbNUFOB" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52bc864d09136f3007429540d727b07a6e459155_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52bc864d09136f3007429540d727b07a6e459155_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52bc864d09136f3007429540d727b07a6e459155.jpeg 2x" data-dominant-color="5A5A60"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-01-05 080555</span><span class="informations">1366×702 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @Sunderlandkyl (2021-01-05 15:27 UTC)

<p>I just tried installing SegmentEditorExtraEffects on the stable release and didn’t encounter any issues. You seem to be missing two segment editor effects: Local Threshold, and Split Volume.</p>
<p>Can you check to see if there are any errors in the log?</p>

---

## Post #25 by @Buyck (2021-01-05 18:10 UTC)

<p>There are indeed error remarks, what can I do to fix this?</p>
<p>Thanks in advance!</p>
<pre><code class="lang-auto">[CRITICAL][Stream] 05.01.2021 19:02:10 [] (unknown:0) -   File "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py", line 6, in &lt;module&gt;

[CRITICAL][Qt] 05.01.2021 19:02:10 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py"  as module "SegmentEditorLocalThresholdLib" !

[CRITICAL][Stream] 05.01.2021 19:02:10 [] (unknown:0) -   File "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThreshold.py", line 27, in registerEditorEffect

[CRITICAL][Stream] 05.01.2021 19:02:10 [] (unknown:0) -   File "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSplitVolumeLib/SegmentEditorEffect.py", line 10, in &lt;module&gt;

[CRITICAL][Qt] 05.01.2021 19:02:10 [] (unknown:0) - loadSourceAsModule - Failed to load file "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSplitVolumeLib/SegmentEditorEffect.py"  as module "SegmentEditorSplitVolumeLib" !

[CRITICAL][Stream] 05.01.2021 19:02:10 [] (unknown:0) -   File "C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSplitVolume.py", line 34, in registerEditorEffect
</code></pre>

---

## Post #26 by @lassoan (2021-01-05 19:04 UTC)

<p>Probably the python files cannot be loaded because Slicer is installed in a folder that contains special characters (F<strong>é</strong>lix). This should not be a problem on recent Windows10 versions. Could you copy here the first 15 lines of the application log (menu: Help/Report a bug) to confirm that your Windows version is too old? If that is indeed the issue then you can either upgrade Windows or install Slicer in a folder that does not have special characters in its path.</p>

---

## Post #27 by @Buyck (2021-01-05 19:28 UTC)

<p>Here is the code:</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:39 [] (unknown:0) - Session start time …: 2021-01-05 20:27:39</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:39 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Operating system …: Windows / Personal / (Build 19041, Code Page 65001) - 64-bit</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Memory …: 8102 MB physical, 16038 MB virtual</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Developer mode enabled …: no</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Prefer executable CLI …: yes</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Application path …: C:/Users/Félix/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin</p>
<p>[DEBUG][Qt] 05.01.2021 20:27:40 [] (unknown:0) - Additional module paths …: C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/Sandbox/lib/Slicer-4.11/qt-scripted-modules</p>
<p>[DEBUG][Python] 05.01.2021 20:27:45 [Python] (C:\Users\Félix\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…</p>
<p>[CRITICAL][Qt] 05.01.2021 20:27:48 [] (unknown:0) - Error(s):</p>
<p>CLI executable: C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py</p>
<p>The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.</p>

---

## Post #28 by @lassoan (2021-01-05 19:39 UTC)

<p>This Windows version should be sufficient.</p>
<p>Does this file exist and contains Python code?<br>
<code>C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py</code></p>

---

## Post #29 by @Buyck (2021-01-05 19:45 UTC)

<p>It appears the folder does contain Python code!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a596602f8c6d91e3d06072d6cc55019e7e3d7ae3.png" data-download-href="/uploads/short-url/nCQXAAerk6vfSlBF2kK5spnAobF.png?dl=1" title="Screenshot 2021-01-05 204448" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a596602f8c6d91e3d06072d6cc55019e7e3d7ae3.png" alt="Screenshot 2021-01-05 204448" data-base62-sha1="nCQXAAerk6vfSlBF2kK5spnAobF" width="690" height="129" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-01-05 204448</span><span class="informations">881×165 8.82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #30 by @lassoan (2021-01-05 20:01 UTC)

<p>Can you compare the file content with this file <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py</a></p>

---

## Post #31 by @lassoan (2021-01-05 20:12 UTC)

<p>It is probably not a coincidence that only Local Threshold and Split Volume effects use SimpleITK and they are the ones that cannot be loaded.</p>
<p>Could you try typing this into the Python console (Ctrl-3) and see if you get an error message?</p>
<pre><code>import SimpleITK as sitk</code></pre>

---

## Post #32 by @Buyck (2021-01-05 20:14 UTC)

<p>This is the responce:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import SimpleITK as sitk<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\Félix\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py”, line 6, in <br>
import SimpleITK as sitk<br>
ModuleNotFoundError: No module named ‘SimpleITK’<br>
Traceback (most recent call last):<br>
File “C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorLocalThreshold.py”, line 27, in registerEditorEffect<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\Félix\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSplitVolumeLib/SegmentEditorEffect.py”, line 10, in <br>
import sitkUtils<br>
File “C:\Users\Félix\AppData\Local\NA-MIC\Slicer 4.11.20200930\bin\Python\sitkUtils.py”, line 4, in <br>
import SimpleITK as sitk<br>
ModuleNotFoundError: No module named ‘SimpleITK’<br>
Traceback (most recent call last):<br>
File “C:/Users/Félix/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorSplitVolume.py”, line 34, in registerEditorEffect<br>
instance.self().register()<br>
AttributeError: ‘NoneType’ object has no attribute ‘register’<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
ModuleNotFoundError: No module named ‘SimpleITK’</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #33 by @Buyck (2021-01-05 20:21 UTC)

<p>There is no difference between the file on my pc and that from github.</p>

---

## Post #34 by @lassoan (2021-01-05 20:22 UTC)

<p>The problem is that SimpleITK is not found. Can you try if it makes a difference if you copy the entire Slicer folder to a path without special characters (for example “c:\tmp\Slicer 4.11.20200930”) and run Slicer from there?</p>

---

## Post #35 by @Buyck (2021-01-05 20:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="34" data-topic="9233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>c:\tmp</p>
</blockquote>
</aside>
<p>It doesn’t chage anything. The program re-installed the extension in the C:\Users\Félix\AppData\Roaming folder and keeps on bugging…</p>

---

## Post #36 by @lassoan (2021-01-05 20:36 UTC)

<p>Could you try removing all the .ini files in <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer settings folder</a> and then start Slicer and see if <code>import SimpleITK as sitk</code> succeeds?</p>

---

## Post #37 by @Buyck (2021-01-05 20:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="36" data-topic="9233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>import SimpleITK as sitk</code></p>
</blockquote>
</aside>
<p>I only have .init_cpython files, the response of slicer was the following:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import SimpleITK as sitk</p>
</blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>ModuleNotFoundError: No module named ‘SimpleITK’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eded49e0caf6b05693f95a553fe5b928916d7e9a.png" data-download-href="/uploads/short-url/xWNy29FihdZSbnsEDk7zB5EVMNA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/eded49e0caf6b05693f95a553fe5b928916d7e9a.png" alt="image" data-base62-sha1="xWNy29FihdZSbnsEDk7zB5EVMNA" width="690" height="378" data-dominant-color="595959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">970×532 42.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #38 by @lassoan (2021-01-05 20:45 UTC)

<p>I meant deleting all files and folders in your Slicer settings folder. Probably it is in <code>C:\Users\Félix\AppData\Roaming\NA-MIC</code>.</p>
<p>I also see that you have some things installed in <code>C:\Users\Public\NA-MIC</code>, which may be the root cause of all issues. Delete the content of that folder, too.</p>
<p>If you don’t want to delete these then you can just move somewhere else (for example, C:\tmp).</p>

---

## Post #39 by @Buyck (2021-01-05 20:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="38" data-topic="9233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>C:\Users\Félix\AppData\Roaming\NA-MIC</code> .</p>
</blockquote>
</aside>
<p>Still the same problem</p>

---

## Post #40 by @lassoan (2021-01-05 20:56 UTC)

<p>We can do a remote debugging session on your computer, write me your availability in a private message. We can probably find and fix the issue in a 10-20 minutes.</p>

---

## Post #41 by @Buyck (2021-01-09 08:56 UTC)

<p>Thank you, that’s very kind but there’s no need for it. I already tried insalling it on a different pc and managed to get the missing tools. However, they were unable to successfully segment the brainvessels of my scans. Thus I had to do it manually <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"></p>
<p>Thanks again for all of your effort to help fix my problem!</p>

---

## Post #42 by @lassoan (2021-01-10 19:31 UTC)

<p>Slicer offers lots of others tools and techniques for brain vessel segmentation. If you are not happy with manual segmentation then let us know and we can help.</p>

---

## Post #43 by @danpak94 (2021-04-22 04:37 UTC)

<p>Thank you for this great new segment editor tool.</p>
<p>I think I might have found a small bug - the ctrl + click didn’t seem to work when using a transform-applied image. If this could be addressed in future versions, I think it would be really helpful (or if this actually isn’t supposed to happen, I would appreciate any pointer on how to fix this behavior). Thanks again!</p>

---

## Post #44 by @lassoan (2021-04-25 13:43 UTC)

<p>SegmentEditorExtraEffects extension serves as an incubator of new effects. They are not fully developed, but they are made available so that users can try it. If they turn out to be useful then they get hardened and polished and moved to the Slicer core.</p>
<p>Local Threshold effect has been proven to be quote useful, so it will likely be moved to Slicer core. Please file a bug report to <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" class="inline-onebox">GitHub - lassoan/SlicerSegmentEditorExtraEffects: Many additional segmentation tools for 3D Slicer's Segment Editor</a> repository to make sure we fix this issue before finalizing this effect.</p>

---

## Post #45 by @lassoan (2023-01-17 19:09 UTC)

<p>A post was split to a new topic: <a href="/t/classify-voxels-via-a-predefined-threshold/27308">Classify voxels via a predefined threshold</a></p>

---

## Post #46 by @nysfour (2023-06-22 19:45 UTC)

<p>For Local threshold, once the region has been established with the yellow demarcating line, how do we fill the segmentation? ‘ctrl click’ is not working no matter what combination of segmentation algorithm I choose</p>

---

## Post #47 by @rbumm (2023-06-23 05:24 UTC)

<p>The whole area of the segmented should be filled with the color of the segment you want to create. Adjust the sliders.<br>
Make sure that you do not have “editable intensity range” checked by accident and that the “minimum diameter” is adequate. Try “Growcut”. Use the latest Slicer version.</p>

---

## Post #48 by @nysfour (2023-06-23 14:17 UTC)

<p>Does the yellow line limit the segment to the interior of the circle? Or does the segment extend past it? Even with these changes I don’t seem to be able to make segments</p>

---

## Post #49 by @Sunderlandkyl (2023-06-23 14:25 UTC)

<p>The range of values in the voxels inside yellow line are used to set the upper and lower range of the threshold.</p>
<p>If you open the “Local histogram” section of the widget you can see a histogram of the voxels and the scalar range contained inside the yellow region.</p>

---

## Post #50 by @nysfour (2023-06-23 14:36 UTC)

<p>so is there any way to just demarcate the region I want to segment? For example, if I want to segment just one organ, could I draw a circle around the organ ROI and fill it with a growing region seed?</p>

---

## Post #51 by @Sunderlandkyl (2023-06-23 14:40 UTC)

<p>You can add a Markups ROI around the organ you want to segment and select it in the ROI field, to force the local threshold to not add any areas outside the box.</p>
<p>Depending on the organ and the “minimum diameter” value, you may not need to specify a ROI.</p>

---

## Post #52 by @nysfour (2023-06-23 14:54 UTC)

<p>Once I’ve made the ROI and selected it for the ROI of the local threshold, then how do I get the segment to grow?</p>

---

## Post #53 by @Sunderlandkyl (2023-06-23 15:00 UTC)

<p>You should be able to ctrl+click (cmd+click on Mac) on one of the regions with the pulsing color.<br>
See video here: <a href="https://www.youtube.com/watch?v=cevlMLyhfK8" class="inline-onebox" rel="noopener nofollow ugc">Segment Editor: New "Local threshold" effect - YouTube</a>.</p>

---

## Post #54 by @nysfour (2023-06-23 15:02 UTC)

<p>And once I ctrl click, should there be a change in color to suggest that a segment was made? I don’t see any appreciable change besides the yellow circle staying in place</p>

---

## Post #55 by @Sunderlandkyl (2023-06-23 15:05 UTC)

<p>It should be filled with the same color as the segment.</p>
<p>What kind of structure are you trying to segment?</p>

---

## Post #56 by @nysfour (2023-06-23 15:11 UTC)

<p>I am using a scalar image and trying to segment anatomical regions. I first compressed the image using the Vector to scalar module, then drew an ROI, then began using the local threshold. I am able to create the ROI and draw the threshold, but I am unable to create a segment. Using the growing region module or segment draw modules both work so I believe I should be able to create segments using this file type</p>

---

## Post #57 by @rbumm (2023-06-23 15:34 UTC)

<p>I dont see yellow lines <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Change the sliders until the structure you want to segment is solidly filled and the surrounding is not, then<br>
CTRL+ left-click</p>
<p>Maybe this helps:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="NmG16cSwUHg" data-video-title="Segmenting a lung nodule with 3D Slicer and &quot;Local Threshold&quot;" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=NmG16cSwUHg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/NmG16cSwUHg/maxresdefault.jpg" title="Segmenting a lung nodule with 3D Slicer and &quot;Local Threshold&quot;" width="" height="">
  </a>
</div>


---

## Post #58 by @nysfour (2023-06-23 15:53 UTC)

<p>For some reason I just can’t get the segment to be created, everything else on my screen looks like the video. I am using the latest Slicer version</p>

---

## Post #59 by @rbumm (2023-06-23 16:02 UTC)

<p>Try it like this:</p>
<p>Use the CT chest sample dataset</p>
<p>use this nodule<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7962ba02c071ba51f314db6d16ee23723b38331.jpeg" alt="image" data-base62-sha1="uLaotveZ8byRkLuOTB3W8MdT2kV" width="466" height="407"></p>
<p>Set the minimum diameter to 1 mm<br>
set the sliders to the positions:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b43b36661a81f9b98a7aff4c4e60c6aba5741fc.png" alt="image" data-base62-sha1="8shdzSoAQssIiXdGuEcC94Hcozi" width="470" height="77"></p>
<p>set everything else to</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f3e2d465da6c4d3931ea414f62b051019e405a7.png" alt="image" data-base62-sha1="6JVEzxReVO8FXkUZOeLTQkoOom3" width="457" height="283"></p>
<p>then CTRL+left click (both same time) into the filled nodule, it will turn green</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0dc459934c212214f3a4cc0b5e14cd06f2871a.png" alt="image" data-base62-sha1="k7OOM9cT0J0vdwhm3bKlSxXitM6" width="220" height="224"></p>

---

## Post #60 by @nysfour (2023-06-23 16:11 UTC)

<p>Thank you very much, that did work. Is there any surefire way to make this work for 2D images?</p>

---

## Post #61 by @rbumm (2023-06-23 16:13 UTC)

<p>No idea, please try and it would be great if you report it here.</p>

---

## Post #62 by @nysfour (2023-06-23 16:24 UTC)

<p>I am a little confused what Local Threshold vs the regular threshold module changes. I don’t seem to be able to threshold within a locality, so using this module seems to just threshold the image as it would have normally without using the ExtraEffects add on. Is there a way to delimit the area that I want to threshold? Even when I create an ROI it doesn’t seem to delimit the growing segment</p>

---

## Post #63 by @rbumm (2023-06-23 17:02 UTC)

<p>By clicking into the locality you were able to threshold in the locality.<br>
Thresholding the whole image would be a different outcome.<br>
I have not used ROI yet with success.</p>

---

## Post #64 by @nysfour (2023-06-23 18:07 UTC)

<p>What creates the locality? I don’t see a definitive demarcation in and outside of the local thresholder as it seems to threshold the whole image no matter where I click or draw</p>

---

## Post #65 by @rbumm (2023-06-24 06:07 UTC)

<p>As I understood it some functions from the Segment Editor Extra Effects package are not yet fully polished and require some more work until they can get included in the standard effects collection.</p>

---

## Post #66 by @Sunderlandkyl (2023-06-26 15:07 UTC)

<p><a class="mention" href="/u/nysfour">@nysfour</a> Could you try running local threshold and attaching the log? If you could also send me a scene with the image that you are trying to segment, it would be helpful. You can send it to me over private message if you can’t share it publicly.</p>

---

## Post #67 by @nysfour (2023-06-26 15:09 UTC)

<p>How do I record the log?</p>

---

## Post #68 by @Sunderlandkyl (2023-06-26 15:16 UTC)

<p>You can find log files in Help → Report a bug. The most recent log will be for the current session.</p>

---

## Post #69 by @Sunderlandkyl (2023-06-26 15:44 UTC)

<p>Thanks for sending the log + data!</p>
<p>The issue is that the GrowCut filter does not work on 2D data.<br>
It should work if you change the segmentation algorithm to “Masking” in the Local threshold effect.</p>
<p>I’ll add a message to let the user know about this limitation if they have an algorithm that is incompatible with their data selected.</p>

---

## Post #70 by @nysfour (2023-06-26 16:58 UTC)

<p>Thank you very much!</p>

---

## Post #71 by @nysfour (2023-06-26 19:07 UTC)

<p>Is there any limitation on how many ROI’s can be added? When I add a first ROI, local thresholder works to segment. However, when a second ROI is added, the program doesn’t generate a new mask, even if the ROI is changed to the secondary box. Is there anything wrong with this group of settings? (R_1 is the added ROI)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90e8486ad2f36c5e886bb5c4c05ddff692eee431.png" alt="image" data-base62-sha1="kFUq0DkCtDz3CkJ0cAFyE6mPwDT" width="527" height="475"></p>

---

## Post #72 by @Sunderlandkyl (2023-06-27 15:04 UTC)

<p>Multiple ROIs should work fine. I tested on 3D images and you can use multiple ROI nodes, or modify a single one between operations.</p>
<p>In 2D however it looks like the ROI doesn’t function correctly. I’m looking into it.</p>

---

## Post #73 by @nysfour (2023-06-27 15:34 UTC)

<p>For the last 2D run I did, I was able to place 2 ROIs and segment within them, but the third ROI I placed prevented any segmentation. I can run more tests and send the logs if that would be helpful</p>

---
