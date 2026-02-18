# SegmentEditor Islands effect keeps the islands in the original segment

**Topic ID**: 8037
**Date**: 2019-08-14
**URL**: https://discourse.slicer.org/t/segmenteditor-islands-effect-keeps-the-islands-in-the-original-segment/8037

---

## Post #1 by @muratmaga (2019-08-14 20:49 UTC)

<p>I am trying to do use the islands effect to separate individual bones. While, it finishes correctly, it still retains the new created islands/segments in the original segment. I thought the behavior was to move them to the newly created segments. See screen captures. This is with  r28340 on windows 10.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a924d815060f76d48f7ba9ab8ccb4c4196ced5c.jpeg" data-download-href="/uploads/short-url/1vwe4f3DYiPtI9PT90OJdtP8Uqw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a924d815060f76d48f7ba9ab8ccb4c4196ced5c_2_434x500.jpeg" alt="image" data-base62-sha1="1vwe4f3DYiPtI9PT90OJdtP8Uqw" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a924d815060f76d48f7ba9ab8ccb4c4196ced5c_2_434x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a924d815060f76d48f7ba9ab8ccb4c4196ced5c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a924d815060f76d48f7ba9ab8ccb4c4196ced5c.jpeg 2x" data-dominant-color="8A96B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×726 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After i turned off the segments that are right hindlimbs and forelimbs, they are still visible in segment_1 (green large chunk)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fea00d1e34b0d7f95d168c9e2d07aee90ce801.jpeg" data-download-href="/uploads/short-url/7QvjyjNskC7YZCgeB1iZuqZCARX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36fea00d1e34b0d7f95d168c9e2d07aee90ce801_2_445x500.jpeg" alt="image" data-base62-sha1="7QvjyjNskC7YZCgeB1iZuqZCARX" width="445" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36fea00d1e34b0d7f95d168c9e2d07aee90ce801_2_445x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36fea00d1e34b0d7f95d168c9e2d07aee90ce801_2_667x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36fea00d1e34b0d7f95d168c9e2d07aee90ce801.jpeg 2x" data-dominant-color="8B96B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">688×772 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t recall the functionality being like this. If this change was intentional, I find this behavior tedious. It requires me doing additional logical operations to remove them from the original segment.</p>
<p>I am not sure if it is relevant, but there is this error in the log file</p>
<blockquote>
<p>[WARNING][Qt] 14.08.2019 13:29:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1</p>
<p>[INFO][Python] 14.08.2019 13:35:34 [Python] (C:\Slicer 4.11.0-2019-08-09\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects\SegmentEditorIslandsEffect.py:187) - 18 islands created (78 ignored)</p>
<p>[INFO][Stream] 14.08.2019 13:35:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - 18 islands created (78 ignored)</p>
<p>[CRITICAL][Qt] 14.08.2019 13:35:58 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - void __cdecl qSlicerSegmentEditorAbstractEffect::modifySelectedSegmentByLabelmap(class vtkOrientedImageData *,enum qSlicerSegmentEditorAbstractEffect::ModificationMode,const int <span class="chcklst-box fa fa-square-o fa-fw"></span>) : Invalid segment selection</p>
</blockquote>

---

## Post #2 by @lassoan (2019-08-15 03:16 UTC)

<p>You can choose the behavior using Masking / Modify other segments option. “Overwrite all” replaces content in the original segments, “Allow overlap” preserves the original segments.</p>

---

## Post #3 by @muratmaga (2019-08-15 04:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Unfortunately it happens with ‘overwrite all option’ (i.e., it doesn’t overwrite the initial segment)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf1d3f3305a9c61a4aacbcf996f247b3f2cd6cee.png" data-download-href="/uploads/short-url/tyduQsqIfz8kWPGmEU7i2Y8yaGG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf1d3f3305a9c61a4aacbcf996f247b3f2cd6cee_2_690x106.png" alt="image" data-base62-sha1="tyduQsqIfz8kWPGmEU7i2Y8yaGG" width="690" height="106" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf1d3f3305a9c61a4aacbcf996f247b3f2cd6cee_2_690x106.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf1d3f3305a9c61a4aacbcf996f247b3f2cd6cee_2_1035x159.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf1d3f3305a9c61a4aacbcf996f247b3f2cd6cee.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×176 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
There is this error in the log file:</p>
<blockquote>
<p>Loaded volume from file: C:/Users/Murat/Downloads/IntensityWindowingImageFilter Output.nrrd. Dimensions: 869x998x1295. Number of components: 1. Pixel type: unsigned char.</p>
<p>“Volume” Reader has successfully read the file “C:/Users/Murat/Downloads/IntensityWindowingImageFilter Output.nrrd” “[1.00s]”</p>
<p>Switch to module: “SegmentEditor”</p>
<p>ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1</p>
<p>28 islands created (14632 ignored)</p>
<p>28 islands created (14632 ignored)</p>
<p>void __cdecl qSlicerSegmentEditorAbstractEffect::modifySelectedSegmentByLabelmap(class vtkOrientedImageData *,enum qSlicerSegmentEditorAbstractEffect::ModificationMode,const int <span class="chcklst-box fa fa-square-o fa-fw"></span>) : Invalid segment selection</p>
</blockquote>

---

## Post #4 by @lassoan (2019-08-15 17:08 UTC)

<p>I think the behavior haven’t changed in the last few years:</p>
<ul>
<li>“Split islands to segments” option does not modify the original segment (you can delete the original segment if you no longer need it)</li>
<li>“Add selected island” does overwrite the original segment if “overwrite all” is chosen</li>
</ul>
<p>Do you find these behaviors not optimal for your workflow? Do you find any difference compared to Slicer-4.10?</p>

---

## Post #5 by @muratmaga (2019-08-15 17:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks, I have to give it a more careful try with the preview version. Dataset is on my home computer.</p>
<p>The issue is, after the island effect segmentation is not fully done. I still have to operate on Segment_1 (e.g., isolate pelvis, the skull, left forelimb, vertebral column etc), yet Segment_1 is unmodified. It is ok for it to remain unmodified, but at the end of the operation I would like to have a segment that I can carry on the remaining segmentation tasks without having to do additional logical operations. If I delete the segment_1, I don’t have anything else to carry those operations.</p>
<p>For example, if I want to segment the thorax, I would like to use the fact that both forelimbs and scapula are already segmented.</p>
<p>I haven’t been using the segment editor as much as the old editor personally, so may be am missing something here. What I described was the behavior in the old island effect.</p>

---

## Post #6 by @lassoan (2019-08-15 18:17 UTC)

<p>Island effect has many modes. Do you have problem with the behavior of “Split islands to segments”?</p>

---

## Post #7 by @hjhedgar (2019-08-29 03:27 UTC)

<p>We are having the same problem with islands module, split island to segments option with the “overwrite all” selected. See screenshot. This is different than the behavior in stable version, which actually “splits” the segment into new segments. This behavior requires an additional operation to “subtract” the newly created island (or islands) from the original.<br>
See screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1c3099fa02ce1875e783814600db180f4e3e828.jpeg" data-download-href="/uploads/short-url/n50JOa2ssXaEdkdkIi9z34CXGOs.jpeg?dl=1" title="55%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1c3099fa02ce1875e783814600db180f4e3e828_2_690x393.jpeg" alt="55%20PM" data-base62-sha1="n50JOa2ssXaEdkdkIi9z34CXGOs" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1c3099fa02ce1875e783814600db180f4e3e828_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1c3099fa02ce1875e783814600db180f4e3e828_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1c3099fa02ce1875e783814600db180f4e3e828_2_1380x786.jpeg 2x" data-dominant-color="ADACAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">55%20PM</span><span class="informations">2862×1632 961 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @muratmaga (2019-08-30 13:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have a chance to replicate the issue with the split islands behavior?</p>

---

## Post #9 by @lassoan (2019-08-30 14:24 UTC)

<p>I did not try it again since my first answer.</p>
<p>"Split islands to segments” option does not modify the original segment. Do you find that the behavior is different in latest stable vs latest preview version?</p>
<p>You can delete the original segment if you no longer need it by a single click. Is the problem that you need to do this extra click?</p>

---

## Post #10 by @muratmaga (2019-08-30 17:51 UTC)

<p>Hi Andras,</p>
<p>If you look at the image on the <a class="mention" href="/u/hjhedgar">@hjhedgar</a> post above, if you delete the segment_1 (green), which is the original, you will no longer have any segment that contains the hand on the left side as a single structure. This was not the behavior in the stable version.</p>
<p>Currently the solution we found is to subtract every other segment from the original, and that gets tedious as the number your islands  increase.</p>
<p>I think keeping the original segment is a good idea, except the result of split islands to segment should output two additional segments, a left foot only, a right foot only, and then the original.</p>
<p>What we have instead is the original (untouched segment) and only the right hand. That’s our issue with the current behavior.</p>

---

## Post #11 by @lassoan (2019-08-30 19:37 UTC)

<p>This sounds like a bug, will test again. What masking settings do you use?</p>

---

## Post #12 by @muratmaga (2019-08-30 20:36 UTC)

<p>Same as the screen capture, (editable everywhere, overwrite all segments)</p>

---

## Post #13 by @lassoan (2019-09-01 02:17 UTC)

<p>I could reproduce and <a href="https://github.com/Slicer/Slicer/commit/f5c1095ce34ac6f835617ab79e8a48fb4ef685ea">fixed the issue</a>. The problem was that due to some recent changes, current node selection was lost when the new segments were added. Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/hjhedgar">@hjhedgar</a> for reporting the issue and providing all the details.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> You’ve recently investigated and fixed a similar problem of losing current segment selection. Could you have a look at this, too - why current selected segment ID is cleared when running <code>slicer.vtkSlicerSegmentationsModuleLogic.ImportLabelmapToSegmentationNode</code>? Thank you!</p>

---

## Post #14 by @Sunderlandkyl (2019-09-03 14:37 UTC)

<p><a href="https://github.com/Slicer/Slicer/pull/1204" rel="nofollow noopener">This pull request</a> should fix the segment selection issue for most cases.</p>

---

## Post #15 by @Saima (2021-06-08 03:59 UTC)

<p>Hi Andras,<br>
split island to segments is not working for my case.</p>
<p>I am doing it to split one labelmap. It ignores 113 islands 0 created.<br>
0 islands created (113 ignored).</p>
<p>Also I noticed the one segment in the segment editor it diappears although the label is still there but its empty now.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #16 by @muratmaga (2021-06-08 05:35 UTC)

<p>Split islands has a minimum island size option. If your individual islands are less than this value (which has a default of 1000 voxels), they will be removed. Try reducing this number and see if the islands are retained.</p>

---

## Post #17 by @Saima (2021-06-08 05:41 UTC)

<p>Yes I get it now. Thanks alot</p>

---
