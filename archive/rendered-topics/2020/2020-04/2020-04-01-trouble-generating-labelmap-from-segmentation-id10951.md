---
topic_id: 10951
title: "Trouble Generating Labelmap From Segmentation"
date: 2020-04-01
url: https://discourse.slicer.org/t/10951
---

# Trouble generating Labelmap from segmentation

**Topic ID**: 10951
**Date**: 2020-04-01
**URL**: https://discourse.slicer.org/t/trouble-generating-labelmap-from-segmentation/10951

---

## Post #1 by @Maxibers (2020-04-01 08:03 UTC)

<p>Good morning,<br>
my goal is to automatically load segmentations and save them in a labelmap format, but i’m having trouble:<br>
When i create the labelmap manually (from the segment editor module), save it manually and load it back its perfect. But when i try to create the labelmap by code one of the label level is sorrounded by another level (there is a grey level sorrounding it,and this is very harmful since i’m trying to train a model to do the segmentation)</p>
<p>How the labelmap looks when created by code before saving it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ecc57bd1ab81837df86b97379c858f5f721bb6d.png" data-download-href="/uploads/short-url/knfBoflhWtOCwtJRlrnD2mX9Y3r.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ecc57bd1ab81837df86b97379c858f5f721bb6d_2_690x462.png" alt="Screenshot" data-base62-sha1="knfBoflhWtOCwtJRlrnD2mX9Y3r" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ecc57bd1ab81837df86b97379c858f5f721bb6d_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ecc57bd1ab81837df86b97379c858f5f721bb6d_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ecc57bd1ab81837df86b97379c858f5f721bb6d.png 2x" data-dominant-color="B6A87C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1355×909 9.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How the labelmap looks after being saved and loaded back:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36f9e6f040e42231bd46598f6e4c4a72ec76ed8.png" data-download-href="/uploads/short-url/rSUfruGSKJpFMpB53HzFXkuckhG.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36f9e6f040e42231bd46598f6e4c4a72ec76ed8.png" alt="Screenshot_1" data-base62-sha1="rSUfruGSKJpFMpB53HzFXkuckhG" width="690" height="462" data-dominant-color="878787"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1355×909 7.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>saved labelmap (black-white) vs original labelmap (colored)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339ad087534630e2cbda6872cc1ae058fc0549aa.png" data-download-href="/uploads/short-url/7mw2su6CcLX0Y3pwUzzxGwTKXQC.png?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/339ad087534630e2cbda6872cc1ae058fc0549aa_2_690x462.png" alt="Screenshot_2" data-base62-sha1="7mw2su6CcLX0Y3pwUzzxGwTKXQC" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/339ad087534630e2cbda6872cc1ae058fc0549aa_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/339ad087534630e2cbda6872cc1ae058fc0549aa_2_1035x693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/339ad087534630e2cbda6872cc1ae058fc0549aa.png 2x" data-dominant-color="9F9781"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">1355×909 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also: when i try to save the labelmap by code in the nightly version only one label is saved (it’s missing all the yellow/top part):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a9608b6c623bef1763331706218a909dd85bed5.png" data-download-href="/uploads/short-url/64Jv0MN90iA27U0MgVomPrZFG9n.png?dl=1" title="Screenshot_3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a9608b6c623bef1763331706218a909dd85bed5.png" alt="Screenshot_3" data-base62-sha1="64Jv0MN90iA27U0MgVomPrZFG9n" width="690" height="462" data-dominant-color="B1B1B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_3</span><span class="informations">1355×909 4.26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The code snippet i’m using:</p>
<blockquote>
<pre><code>slicer.util.loadSegmentation('Input_file_dir')
seg_node = slicer.util.getNode('Input_file_name')
merged_labelmap_node = slicer.vtkMRMLLabelMapVolumeNode()
slicer.mrmlScene.AddNode(merged_labelmap_node)
slicer.vtkSlicerSegmentationsModuleLogic.ExportAllSegmentsToLabelmapNode(seg_node, merged_labelmap_node)
slicer.util.saveNode(merged_labelmap_node, output_file_dir)
</code></pre>
</blockquote>
<p>Any help is greatly appreciated</p>

---

## Post #2 by @lassoan (2020-04-01 13:52 UTC)

<p>If segments do not overlap then in recent Slicer Preview Releases, segmentation is already saved in a simple 3D labelmap format (with some additional metadata that you can safely ignore).</p>
<p>Do you need help with accessing individual slices of a 3D labelmap?</p>
<p>What is your complete data flow for generating training data?</p>

---

## Post #3 by @Maxibers (2020-04-01 15:16 UTC)

<p>to create my training dataset i manually segment my area of interest (a small size cropped volume from a head cbct containing my ROI (the TMJ artic.)) in 3 parts: mandible, cranium, soft tissue. I also smooth them by joint smoothing. Segments should never overlap each other.<br>
Since i already have many saved segmentations (and volumes) i just wanted to convert the segs to labelmaps automatically to create the dataset to feed the model. (i use the code generated by my script directly on py interactor of slicer since i dont want to use a CLI)<br>
I don’t need to access the single slices (i’m using niftynet which does all the deep learning work for me). I’m just concerned (looking at the first trained models i’m getting) that the little grey border on the mandible (the green label in the pics) is actually recognized by the model as cranium (which is actually grey in the scalar volume).<br>
I did not try to train directly with the segmentations files from the latest nightly. Neither did i try using .nrrd files instead of .nii</p>

---

## Post #4 by @Maxibers (2020-04-03 17:32 UTC)

<p>after some research i discovered that my problem was in the interpolation, both in slicer (that altered the scalar volume image to have that grey border around my black label level (pic 2 of the post above)) and in NiftyNet (that altered the image in the same way). By disabling the interpolation on slicer and setting it to nearest neighbor in  NN (just for labels) i think i solved my problem.<br>
Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
