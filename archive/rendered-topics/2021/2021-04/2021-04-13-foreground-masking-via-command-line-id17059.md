---
topic_id: 17059
title: "Foreground Masking Via Command Line"
date: 2021-04-13
url: https://discourse.slicer.org/t/17059
---

# Foreground Masking via command line

**Topic ID**: 17059
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/foreground-masking-via-command-line/17059

---

## Post #1 by @PaoloZaffino (2021-04-13 11:11 UTC)

<p>Hi all,<br>
I would need an automatic way of running Foreground Masking via command line.</p>
<p>As far as I understood it is not a cli module, so I need to load the image and run the mask generation via a python script.<br>
However, I didn’t find a way for accessing its logic.</p>
<p>Any suggestion?<br>
Thanks a lot.</p>
<p>Paolo</p>

---

## Post #2 by @pieper (2021-04-13 17:33 UTC)

<p>Hi Paolo -</p>
<p>Can you elaborate on what you mean by Foreground Masking ?</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @PaoloZaffino (2021-04-13 20:19 UTC)

<p>Hi Steve,<br>
I mean this module:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/ForegroundMasking" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/4.10/Modules/ForegroundMasking</a></p>
<p>Thanks,<br>
Paolo</p>

---

## Post #4 by @pieper (2021-04-13 22:07 UTC)

<p>Hmm, I don’t recall that one, perhaps we deprecated it.  But it looks like you can do the same thing with the segment editor pretty easily.</p>

---

## Post #5 by @PaoloZaffino (2021-04-16 19:16 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>, I got it !</p>

---

## Post #6 by @lassoan (2021-04-18 13:10 UTC)

<p>If volume geometries are matching then you can also do masking (or combine volumes with various functions) using standard numpy array operations. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Mask_volume_using_segmentation">this example</a> in the script repository.</p>

---

## Post #7 by @PaoloZaffino (2021-04-20 12:00 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
thanks for answering.<br>
I was interested in generating the mask, so I think I’ll give a try to something different to foreground masking.</p>
<p>Paolo</p>

---

## Post #8 by @lassoan (2021-04-20 12:47 UTC)

<p>Otsu (and about 6-8 other) automatic threshold computation methods are available in Threshold effect and morphological opening is available in Smoothing effect in Segment Editor. You can use these effects from Python as shown in examples in the script repository.</p>

---

## Post #9 by @du5t (2023-11-28 05:42 UTC)

<p>Hello,</p>
<p>I had to process thousands of CTs recently, using batch processing method with python script.</p>
<p>This is the part of the script and I hope this might helpful :</p>
<pre data-code-wrap="python"><code class="lang-python">roi = slicer.modules.brainsroiauto #Foreground Masking cli module
seg1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
params = {}
params['inputVolume'] = volume      
params['outputROIMaskVolume'] = seg1
params['outputClippedVolumeROI'] = 'None'
params['otsuPercentileThreshold'] = 0.01
params['ROIAutoDilateSize'] = 0
params['outputVolumePixelType'] = 'short'

slicer.cli.runSync(roi, None, params)

labelmapVolumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(seg1, labelmapVolumeNode1, volume)
slicer.util.saveNode(labelmapVolumeNode1, resultpath + 'ROI/' + file)

slicer.mrmlScene.Clear()
</code></pre>

---
