---
topic_id: 22148
title: "Edit Segmentation Masks"
date: 2022-02-24
url: https://discourse.slicer.org/t/22148
---

# Edit Segmentation masks

**Topic ID**: 22148
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/edit-segmentation-masks/22148

---

## Post #1 by @Luis_Santos (2022-02-24 02:55 UTC)

<p>Hello everyone! hope you are doing well.</p>
<p>Well. I’m trying to assign my own segmentation algorithm to the input images and put the outoput back in segment editor to edit it. It would help me to improve my model.<br>
I already installed jupyter extension, and followed the scripts commands <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> , but when I tried to edit the imported segmentation, it doesn’t works.<br>
The code I used:</p>
<pre><code class="lang-auto">volume = slicer.util.getNode('patient_1') # imported manually
input_images = slicer.util.arrayFromVolume(volume) # (n, 512,512)
new_masks = np.array(mask_list) # generated from region growing # (n, 512,512)
'''   Create Segmentation Node in scene   '''
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
'''   create a display   '''
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volume)
lung_segment = segmentationNode.GetSegmentation().AddEmptySegment("lung_segment")
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volume)
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName('lung_segment')
slicer.util.updateSegmentBinaryLabelmapFromArray(new_masks, segmentationNode, segmentId, volume)
</code></pre>
<p>It’s working, but I don’t know how to set the segmentation mask editable. Any suggestion?</p>
<p>Thanks in advance</p>
<p>Imported segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81be8d40ed3cc3898113f0d53c92477b04895976.jpeg" data-download-href="/uploads/short-url/ivLQDsRMqCXezBjFFsT2ndR35xc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81be8d40ed3cc3898113f0d53c92477b04895976_2_690x303.jpeg" alt="image" data-base62-sha1="ivLQDsRMqCXezBjFFsT2ndR35xc" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81be8d40ed3cc3898113f0d53c92477b04895976_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/81be8d40ed3cc3898113f0d53c92477b04895976_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81be8d40ed3cc3898113f0d53c92477b04895976.jpeg 2x" data-dominant-color="393233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×601 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Trying to edit with Paint:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ee625983c142f944f7d3a3f54573c38c29c5663.jpeg" data-download-href="/uploads/short-url/dxvY74OGybEsIdK4h0xNBoAPATp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ee625983c142f944f7d3a3f54573c38c29c5663_2_690x229.jpeg" alt="image" data-base62-sha1="dxvY74OGybEsIdK4h0xNBoAPATp" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ee625983c142f944f7d3a3f54573c38c29c5663_2_690x229.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ee625983c142f944f7d3a3f54573c38c29c5663_2_1035x343.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ee625983c142f944f7d3a3f54573c38c29c5663.jpeg 2x" data-dominant-color="3C3D3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1364×454 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Ps.: The Volume is a collection of images that I imported with the option single file unchecked.</p>
<p>Slicer Version: 4.13</p>

---

## Post #2 by @lassoan (2022-02-24 06:03 UTC)

<p>When you scroll up a little bit, do you see the “Select master volume to enable editing” message at the master volume selector? If yes, then you need to select a volume there that will be used as master volume.</p>

---

## Post #3 by @Luis_Santos (2022-02-24 06:23 UTC)

<p>Thanks for replying</p>
<p>Yes, I selected, look:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e82d8c0ab7533bec4434aa9913875075f19e6b0.jpeg" data-download-href="/uploads/short-url/4lUF2agz01korTD4jQFoc1QTgxa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e82d8c0ab7533bec4434aa9913875075f19e6b0_2_690x368.jpeg" alt="image" data-base62-sha1="4lUF2agz01korTD4jQFoc1QTgxa" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e82d8c0ab7533bec4434aa9913875075f19e6b0_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e82d8c0ab7533bec4434aa9913875075f19e6b0_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e82d8c0ab7533bec4434aa9913875075f19e6b0.jpeg 2x" data-dominant-color="414142"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×679 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Some masks don’t look good enough, I’d like to edit them using the paint tool.</p>

---

## Post #4 by @Luis_Santos (2022-02-24 06:31 UTC)

<p>Maybe the color has something to do with it? I must put at the same level? but how can I choose the same color for both?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8868df503b2c3efb1568b2b2150ca5a13144ffad.jpeg" data-download-href="/uploads/short-url/jsJCGdwyc4pKtjudIsP3VQOQKpD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8868df503b2c3efb1568b2b2150ca5a13144ffad_2_690x303.jpeg" alt="image" data-base62-sha1="jsJCGdwyc4pKtjudIsP3VQOQKpD" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8868df503b2c3efb1568b2b2150ca5a13144ffad_2_690x303.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8868df503b2c3efb1568b2b2150ca5a13144ffad_2_1035x454.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8868df503b2c3efb1568b2b2150ca5a13144ffad.jpeg 2x" data-dominant-color="3A3A3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1364×600 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-02-24 06:57 UTC)

<p>Since the lung segment is green, it should appear in green in the slice views. So, it seems that the imported segmentation is invalid. Most likely something is wrong with <code>mask_list</code>. You can try to set the array like this (using simple thresholding at 50) and see if everything works well in that case:</p>
<pre><code class="lang-python">import numpy as np
new_masks = np.zeros(input_images.shape)
new_masks[input_images&gt;50] = 1
</code></pre>
<p>If everything is good then you can fix the issue by making your array more similar to the correct <code>new_masks</code> array content (shape, data type, …).</p>

---

## Post #6 by @Luis_Santos (2022-02-24 07:12 UTC)

<p>It worked, but something is still missing.<br>
Look how curious. I can edit just where I painted.<br>
For example, in this image, when I try to use the eraser to remove the white area, it doesn’t works<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10cfa7348984ef8d19efc32ae3c1b4bb0f29ad7e.jpeg" data-download-href="/uploads/short-url/2oIx802d9iBgRszNV4NSyCt6JyK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10cfa7348984ef8d19efc32ae3c1b4bb0f29ad7e_2_689x305.jpeg" alt="image" data-base62-sha1="2oIx802d9iBgRszNV4NSyCt6JyK" width="689" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10cfa7348984ef8d19efc32ae3c1b4bb0f29ad7e_2_689x305.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/10cfa7348984ef8d19efc32ae3c1b4bb0f29ad7e_2_1033x457.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10cfa7348984ef8d19efc32ae3c1b4bb0f29ad7e.jpeg 2x" data-dominant-color="5F6461"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1292×572 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But When I paint it, then I can erase.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d3cc50c8a726da407a0ccf2f034cb8fa31bebe6.jpeg" data-download-href="/uploads/short-url/mqZa0nVuh2kJXyRuoTqJiftMBg2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d3cc50c8a726da407a0ccf2f034cb8fa31bebe6_2_690x359.jpeg" alt="image" data-base62-sha1="mqZa0nVuh2kJXyRuoTqJiftMBg2" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d3cc50c8a726da407a0ccf2f034cb8fa31bebe6_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d3cc50c8a726da407a0ccf2f034cb8fa31bebe6_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d3cc50c8a726da407a0ccf2f034cb8fa31bebe6.jpeg 2x" data-dominant-color="5E605E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×697 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But the eraser just works on the area I painted <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662b9982ce67731b029ba2e913924d9a59ad1206.jpeg" data-download-href="/uploads/short-url/ezQ73u49zoKUTBES1lcpz3eCrRQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662b9982ce67731b029ba2e913924d9a59ad1206_2_690x327.jpeg" alt="image" data-base62-sha1="ezQ73u49zoKUTBES1lcpz3eCrRQ" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662b9982ce67731b029ba2e913924d9a59ad1206_2_690x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662b9982ce67731b029ba2e913924d9a59ad1206_2_1035x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662b9982ce67731b029ba2e913924d9a59ad1206.jpeg 2x" data-dominant-color="5A5D5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×649 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you very much</p>

---

## Post #7 by @Luis_Santos (2022-02-24 07:27 UTC)

<p>Don’t worry, your solution worked.</p>
<p>Thanks again</p>

---

## Post #8 by @lassoan (2022-02-24 13:41 UTC)

<p>The issue was that <code>updateSegmentBinaryLabelmapFromArray</code> expected the label value to be 1. I"ll make the function more robust so that it works well with any nonzero label value.</p>

---
