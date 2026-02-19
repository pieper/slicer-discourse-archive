---
topic_id: 7782
title: "Cant Save The Scene And The Segmentations Allocation Error R"
date: 2019-07-27
url: https://discourse.slicer.org/t/7782
---

# Can't save the scene and the segmentations - allocation ERROR, results undefined

**Topic ID**: 7782
**Date**: 2019-07-27
**URL**: https://discourse.slicer.org/t/cant-save-the-scene-and-the-segmentations-allocation-error-results-undefined/7782

---

## Post #1 by @NoobForSlicer (2019-07-27 19:59 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1564d42a6b4dbc38dd219830e23a945610b05883.jpeg" data-download-href="/uploads/short-url/33g3c4uNpn9c9yYIt8GQpcjGevF.jpeg?dl=1" title="3d%20slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1564d42a6b4dbc38dd219830e23a945610b05883_2_690x448.jpeg" alt="3d%20slicer" data-base62-sha1="33g3c4uNpn9c9yYIt8GQpcjGevF" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1564d42a6b4dbc38dd219830e23a945610b05883_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1564d42a6b4dbc38dd219830e23a945610b05883_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1564d42a6b4dbc38dd219830e23a945610b05883_2_1380x896.jpeg 2x" data-dominant-color="EBEBF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d%20slicer</span><span class="informations">1621×1054 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is the error I sadly get…</p>
<p>This file and Segmentations are barely 1 gb while I have 16 GB on this computer.</p>
<p>I wonder what could cause this?</p>

---

## Post #2 by @NoobForSlicer (2019-07-28 08:20 UTC)

<p>hmm my page file for virtual memory is currently 20 GB allocated and I have 16 gb ram.</p>
<p>The Segmentations all together are: 300 KB.</p>
<p>I am puzzled.</p>

---

## Post #3 by @cpinter (2019-07-28 12:14 UTC)

<p>What is in the log? Can you please check in the menu: About / Report an error</p>

---

## Post #4 by @NoobForSlicer (2019-07-28 12:37 UTC)

<p>sure I will as soon as I get back home <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Thanks for replying, will post as soon as I’m home</p>

---

## Post #5 by @NoobForSlicer (2019-07-28 13:45 UTC)

<p>Alright just attempted to repeat the same thing and slicer crashed</p>

---

## Post #6 by @NoobForSlicer (2019-07-28 13:45 UTC)

<p>I will try it now again</p>

---

## Post #7 by @NoobForSlicer (2019-07-28 14:06 UTC)

<p>Session start time …: 2019-07-28 15:45:29<br>
Slicer version …: 4.10.0 (revision 27501) win-amd64 - installed release<br>
Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
Memory …: 16308 MB physical, 36721 MB virtual<br>
CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Additional module paths …: C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/SegmentationWizard/lib/Slicer-4.10/qt-scripted-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/MarkupsToModel/lib/Slicer-4.10/qt-loadable-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/IntensitySegmenter/lib/Slicer-4.10/cli-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/LAScarSegmenter/lib/Slicer-4.10/cli-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/LASegmenter/lib/Slicer-4.10/cli-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/IASEM/lib/Slicer-4.10/cli-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/IASEM/lib/Slicer-4.10/qt-scripted-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/VolumeClip/lib/Slicer-4.10/qt-scripted-modules, C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/SlicerFab/lib/Slicer-4.10/qt-scripted-modules<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/SlicerFab/lib/Slicer-4.10/qt-scripted-modules/BitmapGenerator.py”, line 21<br>
self.parent.contributors = [“Steve Pieper (Isomics, Inc.), Steve Keating (MIT), Ahmed Hosny (Harvard), James Weaver (Harvard)”, Andras Lasso (Queens)] # replace with “Firstname Lastname (Organization)”<br>
^<br>
SyntaxError: invalid syntax<br>
loadSourceAsModule - Failed to load file “C:/Users/User1/AppData/Roaming/NA-MIC/Extensions-27501/SlicerFab/lib/Slicer-4.10/qt-scripted-modules/BitmapGenerator.py”  as module “BitmapGenerator” !<br>
Fail to instantiate module  “BitmapGenerator”<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module:  “Welcome”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/32344 r/Segmentation.seg.nrrd” “[0.13s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/32423 r/Segmentation.seg.nrrd” “[0.11s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/3 1231312r/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/23423 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/1 12312r/Segmentation_1.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/5 1231231r/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/4 123131231r/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/12313123 R/Segmentation.seg.nrrd” “[0.00s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/123123 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/12312 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/1231231 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/312333 R/Segmentation.seg.nrrd” “[0.00s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/1112331 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/23213231 R/Segmentation_1.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/32131333 R/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/12311 r/Segmentation_1.seg.nrrd” “[0.15s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/131233 r/Segmentation.seg.nrrd” “[0.00s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/421239898 r/Segmentation.seg.nrrd” “[0.03s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 1/New ones new ones july 28/8987908 r/Segmentation.seg.nrrd” “[0.02s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/890890l/Segmentation.seg.nrrd” “[0.16s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/3 890890/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/890890l/Segmentation.seg.nrrd” “[0.06s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/0890890l/Segmentation.seg.nrrd” “[0.04s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/089089 l/Segmentation.seg.nrrd” “[0.13s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/0890890l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/4 890890 l/Segmentation.seg.nrrd” “[0.02s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/4 890890l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/2 890890l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/378979l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/5879789l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/789789l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/789789789l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/9789l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/789789 l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/78978 l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/78978 l/Segmentation.seg.nrrd” “[0.01s]”<br>
“Segmentation” Reader has successfully read the file “C:/Users/User1/Downloads/Segmented/Bottle Model 2/new ones july 28/7897 L/Segmentation.seg.nrrd” “[0.00s]”<br>
Switch to module:  “Data”<br>
Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_1</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_2</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_3</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_4</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_5</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_6</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_7</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_8</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_9</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_10</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_11</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_12</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_13</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_14</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_15</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_16</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_6) already exists in the target segmentation. Generate a new unique segment ID: Segment_6_17</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_18</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_3) already exists in the target segmentation. Generate a new unique segment ID: Segment_3_19</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_4) already exists in the target segmentation. Generate a new unique segment ID: Segment_4_20</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_5) already exists in the target segmentation. Generate a new unique segment ID: Segment_5_21</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_22</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_23</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_24</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_2) already exists in the target segmentation. Generate a new unique segment ID: Segment_2_25</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_3) already exists in the target segmentation. Generate a new unique segment ID: Segment_3_26</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_4) already exists in the target segmentation. Generate a new unique segment ID: Segment_4_27</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_5) already exists in the target segmentation. Generate a new unique segment ID: Segment_5_28</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_29</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_2) already exists in the target segmentation. Generate a new unique segment ID: Segment_2_30</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_3) already exists in the target segmentation. Generate a new unique segment ID: Segment_3_31</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_4) already exists in the target segmentation. Generate a new unique segment ID: Segment_4_32</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_33</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_2) already exists in the target segmentation. Generate a new unique segment ID: Segment_2_34</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_3) already exists in the target segmentation. Generate a new unique segment ID: Segment_3_35</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_4) already exists in the target segmentation. Generate a new unique segment ID: Segment_4_36</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_6) already exists in the target segmentation. Generate a new unique segment ID: Segment_6_37</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_38</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_39</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_40</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_41</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_42</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_43</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_44</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_45</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_46</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_47</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_48</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_49</p>
<p>Warning: In D:\D\S\Slicer-4100\Libs\vtkSegmentationCore\vtkSegmentation.cxx, line 1292<br>
vtkSegmentation (000002466EF8CB30): CopySegmentFromSegmentation: Segment with the same ID as the copied one (Segment_1) already exists in the target segmentation. Generate a new unique segment ID: Segment_1_50</p>
<p>Switch to module:  “SegmentEditor”<br>
Unable to allocate 1644719412 elements of size 1 bytes.</p>
<p>“Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”</p>

---

## Post #8 by @lassoan (2019-07-28 14:43 UTC)

<p>You have run out of memory. File size on disk may be misleading if the file is compressed (labelmaps may be compressed with a ratio of thousands to one).</p>
<p>Can you copy-paste header of the files you loaded? Why do you load so many files? Do you store one srgment per file? How did you create the input files?</p>

---

## Post #9 by @NoobForSlicer (2019-07-28 16:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you copy-paste header of the files you loaded?</p>
</blockquote>
</aside>
<ul>
<li>Yes I will try to figure out what a header of the file is and how to see it so I can post it here.</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Why do you load so many files?</p>
</blockquote>
</aside>
<ul>
<li>My computer could not handle segmenting on a volume that was huge.</li>
<li>So I cropped it and have segmented smaller parts of the design individually.</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you store one srgment per file?</p>
</blockquote>
</aside>
<ul>
<li>Mostly I have one segmentation per seg.nrrd file.</li>
<li>Sometimes in rare cases I have 4-6.</li>
</ul>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="7782">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How did you create the input files?</p>
</blockquote>
</aside>
<ul>
<li>
<p>So I cropped the big volume and have segmented smaller parts of the design individually.</p>
</li>
<li>
<p>Segmenting on smaller cropped nrrd files that were at most 100 mb and normally just 1-2mb was also problematic when I segment more than 2-3 things, I had to uncheck the eye thing to make them invisible and then it worked better. (this is with or without show 3d option enabled and in all three or just one (red slice) showing). Basically in simple words if I added more than 3 segments it started lagging.</p>
</li>
<li>
<p>Luckily mostly I had only 1 thing to segment per 1 file so the latter was a minor issue</p>
</li>
<li>
<p>This explains why I load so many files because I now would like to have the segmentations in 1 file and export them.</p>
</li>
<li>
<p>I then opened Slicer and just loaded the seg.nrrd files. In Data module I simply put all the segments under one segmentation and deleted rest of the segmentations. This way it looked neat to me and easier to navigate.</p>
</li>
<li>
<p>Turns out I can not export them anymore. I was little bit scared that issues could happen and if you remember I was the one that asked just 7 days ago how many segmentations can I load it and if it only depends on the memory. I was quite skeptic that everything will go smooth… Out of some noob experience I know that I never do things out of first attempt sadly and it is mostly my mistake somewhere that got away and I didn’t see it. It’s just I am puzzled here what could have been my mistake.</p>
</li>
</ul>
<p>Could it be that cropped files still carry some information along with them from that big volume that they were cropped out? So when I add 40 cropped out files together it overloads the system because of some reason? Or could it be that Slicer does its calculations somehow in a weird way where it doesn’t care if the nrrd file I loaded is small, it only cares about the highest and the lowest and then considers the differences between them as a volume to calculate in as well… So then I have something that is 5 meters above the first segment and Slicer somehow upon exporting or saving calculates it all as one since I deleted all other segmentations and put all the semgnets under one remaining semgnetation, it can only save one seg.nrrd file. This means it can only use one header. It means that the positions will be calculated with reference to that one file and then we ended up with a huge volume? Even though that semgnetation nrrd file would have a “huge volume” generally speaking it is just 40 small segmented parts in 3D, why would it be such a problem? Or Slicer doesn’t work that way and doesn’t care if the 3d segments are small, it only cares if the NRRD file has big volume?</p>
<p>Hm…</p>

---

## Post #10 by @muratmaga (2019-07-28 17:18 UTC)

<blockquote>
<p>Blockquote<br>
Even though that semgnetation nrrd file would have a “huge volume” generally speaking it is just 40 small segmented parts in 3D, why would it be such a problem? Or Slicer doesn’t work that way and doesn’t care if the 3d segments are small, it only cares if the NRRD file has big volume?</p>
</blockquote>
<p>This is a common misconception. Just because your segmentation contains a tiny fraction of the volume, it doesn’t mean that it takes only a little space in memory. As <a class="mention" href="/u/lassoan">@lassoan</a> already explained, because they are mostly 0s (or some other constant) for the empty space, they compress very well. But loaded into Slicer, they can require as much memory as the original volume. Since I don’t know what the dimensions of your master volume is, I will just make up a number and say that is 1024x1024x1024 (so about 1GB data if its 8 bit grayscale). By exporting every segmentation as a separate file, and loading them into Slicer individually, effectively you loaded a 1GB file 40 times, causing an out of memory error.</p>
<p>Again, I don’t know the specifics of your dataset, but most likely if you kept your segments in one file, each of which had their unique segment ids, you wouldn’t have this problem.</p>

---

## Post #11 by @NoobForSlicer (2019-07-28 17:38 UTC)

<p>If I have 70 small seg.nrrd files each 1-5 MB in size, so it is definitely not 1GB per file.</p>
<p>There are not 8 bits of grey or anything. Those are only seg.nrrd files I’ve imported. No color nor grey at all, nothing.</p>
<p>I have just imported seg.nrrd files with only segmentations and most often just one small segment.  There are no images neither grey nor color ones.</p>
<p>All segments  in those seg.nrrd files are small. I then just put them together in one bigger seg file. This might increase the volume indeed but then again we are talking only about seg file which is nowhere near 1 GB since it contains no color information or anything.</p>
<p>I really don’t understand this…</p>
<p>Even if what I did somehow increases the memory consumption by 1000, then from 1 MB it would be 1 GB. I’ve allocated over 40GB virtual +16 real ram memory, this means I could go 5000 more than this.</p>
<p>Something just doesn’t add up here…</p>

---

## Post #12 by @muratmaga (2019-07-28 18:01 UTC)

<p>That goes to the specifics of how these segmentations are represented in the computer, and there are people who can explain this better than me. But essentially you still need to use memory to tell the software there is no color. By keeping the segments together in a single file, you get rid of the redundant memory consumption.</p>
<p>You have a total memory resource of 56GB, which is shared among your OS, and all other programs beside Slicer running at the time, all of which is going to affect the available memory that you can use to your specific tasks in Slicer.</p>

---

## Post #13 by @NoobForSlicer (2019-07-28 18:31 UTC)

<p>That is what I did, I’ve put all segments under one segmentation in Data module.</p>
<p>Still crashes… The error I actually posted here was when I did that.</p>
<p>I could allocate more memory to this but I don’t know why isn’t it showing up.<br>
I’ve put in 60GB in my Performance options in windows settings for virtual memory.<br>
But it only takes 40 GB. I don’t know why…</p>
<p>I have an external USB hard drive with 6 TB memory. I have clicked to use that as well and allocated 200 GB but Slicer doesn’t seem to use it. It doesn’t even show up.</p>
<p>I am not sure if I can purchase 128 GB or more of RAM, that would be too expensive I think.I sitll don’t know if it that would make it work.</p>
<p>I have exported files one by one and put them together  in 3ds max, 0 problems… But why? I still can’t understand that a 70 low poly models can be so heavy and devastating… I really would like to handle this problem so I can learn from it as well.</p>
<p>I am still trying to get the header of those seg.nrrd files because that would give you guys insight what the hell I am actually loading and how big or small it is I guess. But I can’t since I have no clue where to find the header…</p>
<p>Lassoan asked a good question about it but I still didn’t figure out how to find the header in those files. Still searching, will let you guys know if I manage to find it, wish me luck</p>

---

## Post #14 by @NoobForSlicer (2019-07-28 18:39 UTC)

<p>I mean, I literally have seventy of  14 KB seg.nrrd files loaded in and it needs  100+ GB to save it in one scene? (it crashes whether I merge them into 1 seg.nrrd file or leave them under separate seg.nrrd files…</p>
<p>I must be doing something horribly wrong here…</p>

---

## Post #15 by @muratmaga (2019-07-28 19:18 UTC)

<p>Can you share your data (70 segmentation files and your original master volume you derived the segmentations)</p>

---

## Post #16 by @NoobForSlicer (2019-07-28 19:38 UTC)

<p>Sadly I am not allowed to, especially since this is a public forum…</p>
<p>I already solved the problem manually exported them one by one.</p>
<p>But I am just curious because I want to learn and Slicer was amazing for me… If I figure out what Andras Lasso was saying and find how to see the header of those files I am sure i can post that since that is just metadata I guess… but that should give us valuable insights so we all understand what the heck can show 14 KB on the disk and then require 100+ GB to be saved <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #17 by @NoobForSlicer (2019-07-28 19:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a6ec313ce0563d44a385de538075112ad27f50b.jpeg" data-download-href="/uploads/short-url/cU0hhZVdKGWu6fdc5cFoQqWLMGT.jpeg?dl=1" title="file%20sizes" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a6ec313ce0563d44a385de538075112ad27f50b_2_172x500.jpeg" alt="file%20sizes" data-base62-sha1="cU0hhZVdKGWu6fdc5cFoQqWLMGT" width="172" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a6ec313ce0563d44a385de538075112ad27f50b_2_172x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a6ec313ce0563d44a385de538075112ad27f50b_2_258x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a6ec313ce0563d44a385de538075112ad27f50b_2_344x1000.jpeg 2x" data-dominant-color="C4DDF2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">file%20sizes</span><span class="informations">403×1168 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here you can see some of those were 6 KB in size <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @muratmaga (2019-07-28 22:56 UTC)

<p>No, that just the file size after compression. What lassoan was asking something like this:<br>
<a href="http://teem.sourceforge.net/nrrd/format.html#general.1" class="onebox" target="_blank" rel="nofollow noopener">http://teem.sourceforge.net/nrrd/format.html#general.1</a></p>
<p>Try importing one of your seg.nrrd files as a volume (not as a segmentation), and use the Volumes module to report it is dimensions, and data types.</p>

---

## Post #19 by @lassoan (2019-07-29 03:37 UTC)

<p>It may be surprising, but actually a 1GB labelmap may be stored on a few KB if it only contains a small structure. For editing, we sometimes need to allocate the full labelmap in memory, uncompressed, that’s why you need a lot of RAM.</p>
<p>Usually when you have a small structure, segmentation infrastructure only allocates memory to store that small region, but in unusual workflows, it may be possible that the full extent of the labelmap remains allocated. If you can provide sample volumes (we don’t need your actual segmentation, just similarly sized random scribbles will suffice) and a description of what you want to achieve then we can investigate more and give more specific advice.</p>

---
