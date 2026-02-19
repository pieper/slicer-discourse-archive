---
topic_id: 14168
title: "Meshing A Model With Different Parts"
date: 2020-10-20
url: https://discourse.slicer.org/t/14168
---

# Meshing a model with different parts

**Topic ID**: 14168
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/meshing-a-model-with-different-parts/14168

---

## Post #1 by @Aep93 (2020-10-20 19:35 UTC)

<p>Hello all,<br>
Considering a segmented model that includes different parts (bones, ligaments, etc.). In FEM, we may need to have a fine mesh for some parts of the model and a coarse mesh for other parts (for example fine mesh for ligaments and coarse mesh for bones). Is it possible to do this with segment mesher?<br>
I know that cleaver tool of segment mesher has an adaptive mesh option but I think it refines mesh at the regions where two part are in contact with each other and it is not the same thing as I want. Any helps on this is greatly appreciated.<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2020-10-20 19:57 UTC)

<p>Cleaver can take an additional sizing field image, which can be used to specify mesh resolution. This option is not exposed on the graphical user interface but you need to create this field image and pass it to the mesher via additional command-line option. If you find that it works well then we can make it more conveniently available.</p>

---

## Post #3 by @Aep93 (2020-10-20 21:49 UTC)

<p>Thank you very much for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I tried to add a field nrrd file. I apply the following command in the section “cleaver mesh options” of segment mesher:<br>
<code> --sizing_field /user/fields.seg.nrrd</code></p>
<p>However, i get the following error:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/user/.config/NA-MIC/Extensions-27931/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py", line 280, in onApplyButton
    self.logic.createMeshFromSegmentationCleaver(self.inputModelSelector.currentNode(), self.outputModelSelector.currentNode(), self.cleaverAdditionalParametersWidget.text)
  File "/user/.config/NA-MIC/Extensions-27931/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py", line 520, in createMeshFromSegmentationCleaver
    self.logProcessOutput(ep, self.cleaverFilename)
  File "/user/.config/NA-MIC/Extensions-27931/SegmentMesher/lib/Slicer-4.10/qt-scripted-modules/SegmentMesher.py", line 455, in logProcessOutput
    raise subprocess.CalledProcessError(return_code, processName)
CalledProcessError: Command 'cleaver-cli' returned non-zero exit status -6
</code></pre>
<p>Do you have any ideas about the reason of this error?</p>
<p>Also for creating the size field nrrd file, I did this:</p>
<ol>
<li>Convert my main segmentation (for which I want to create mesh) to model in slicer.</li>
<li>Use surface toolbox and decimation tool to make the model coarse in specific regions.</li>
<li>Convert the model to segmentation node and use the new segmentation as the sizing field.<br>
Do you also think this procedure is the correct way of doing this?</li>
</ol>
<p>Thank you very much and I really appreciate your help.</p>

---

## Post #4 by @lassoan (2020-10-21 00:06 UTC)

<p>Can you upload all your inputs somewhere and post theink here so I can easily reproduce what you did?</p>

---

## Post #5 by @Aep93 (2020-10-21 00:47 UTC)

<p>Sure <a class="mention" href="/u/lassoan">@lassoan</a>. I created some test files and uploaded them to the link below:<br>
<a href="https://github.com/A-ep93/SlicerTest/blob/main/test.zip?raw=true" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/A-ep93/SlicerTest/blob/main/test.zip?raw=true</a><br>
The file with the name “Segmentation.seg.nrrd” is the main file I want to mesh and the file with the name “sizing-field.seg.nrrd” is the sizing filed I created (In the sizing field, one of the parts is coarser than the other one).<br>
I am not still sure, whether the sizing field I created is the thing I need for cleaver and I searched the web but I was not able to find any good examples for this. Your help is greatly appreciated.</p>

---

## Post #6 by @Aep93 (2020-10-21 20:38 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I wanted to kindly ask you whether you were able to check my files and if you did, whether you have any suggestions for me.<br>
Thanks for your help in advance.</p>

---

## Post #7 by @lassoan (2020-10-21 20:54 UTC)

<p>Yes, I’ve completed an investigation of how to use custom sizing field with Cleaver:</p>
<p>If you specify a custom sizing field then the segment’s geometry and scaling, multiplier, etc. parameters are not taken into account for determining element size. You need to then compute the entire field yourself. A reasonable approach would be to let Cleaver compute an initial mesh and then you could alter the values in selected regions (make them larger/smaller, depending on the resolution you want).</p>
<p>I’ve tried to changing cleaver-cli to write the computed sizing field and then using that field in the next execution. Unfortunately, this did not work (generated mesh was empty). It may be due to Cleaver making changes to the volume size (adds padding) and discards spacing, origin, and axis direction information when importing/exporting sizing fields, so it is hard to know what image geometry cleaver expects.</p>
<p>Before continuing the investigation, Cleaver should be fixed so that it uses image geometry information (origin, spacing, axis directions) consistently in all inputs and outputs. There are a number of <a href="https://github.com/SCIInstitute/Cleaver2/issues">open issues</a> related to this already, so probably Cleaver developers are aware of this, but I’m not sure when they plan to address them. You can submit a bug report to their repository and see what they say.</p>

---

## Post #8 by @Aep93 (2020-10-21 21:34 UTC)

<p>Thank you so much for working on this <a class="mention" href="/u/lassoan">@lassoan</a>. I really appreciate your help.  I will submit a bug report on the cleaver github page regarding the consistency of the geometry information for the inputs and outputs. But I have two questions now:</p>
<ol>
<li>You said that a reasonable approach for creating the sizing field is to use the cleaver to generate an initial mesh and then modify it as we want and use it as sizing field. I also think it is a good idea. But how is it possible? I mean when we generate meshes with segmentmesher, we have some volumetric models in slicer. As far as I know, most of the slicer modules are for working with surface models and not volumetric ones. Is this correct? If yes, then how should we modifiy those volumetric meshes?</li>
<li>Aren’t we able to do this (modifying meshes in areas we want) by using tetgen instead of cleaver? Do you think it is possible in tetgen?<br>
Thanks in advance</li>
</ol>

---

## Post #9 by @Aep93 (2020-10-22 21:26 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I saw that you updated the cleaver version of segmentmesher. Thank you very much for this.<br>
Now, how should we create the sizing field? You mentioned previously that we can generate an initial model with the cleaver itself and modify it as we want. But how should we obtain the initial sizing field from cleaver? and how should we modify that? Can you please send me the modifications that are needed to be applied on cleaver-cli for this?</p>

---

## Post #10 by @lassoan (2020-10-22 21:45 UTC)

<p>One effective way of creating a sizing field is to paint segments where you want higher resolution, export that segmentation to labelmap node, replace label values by sizing values (using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">standard numpy array operations</a>), then apply Gaussian blurring to make the sizing field smooth. There are of course many other ways and we can also easily automate these steps, once it is confirmed that it all works.</p>

---

## Post #11 by @Aep93 (2020-10-23 00:33 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> for your explanation.<br>
I did what you mentioned on a test file and attached the files <a href="https://github.com/A-ep93/SlicerTest/blob/main/test2.zip?raw=true" rel="noopener nofollow ugc">here</a> as well.<br>
The file with name “Segmentation.seg.nrrd” is the main file I want to mesh. I created a segment for one part (for which I want finer mesh), converted that to label map and increased the value of the sizing field from 1 to 2000 with the following code:</p>
<pre><code>volumeNode = getNode('field')
a = arrayFromVolume(volumeNode)
# Increase image contrast
a[:] = a * 2000.0
arrayFromVolumeModified(volumeNode)
</code></pre>
<p>I did not applied the Gaussian blurring because I muliplied the whole domain by a constant value and I think everything is still smooth for this simple example (is this correct?).</p>
<p>I exported the field with the name “field.nrrd” and used it for the sizing field parameter in segment mesher by writing the following in the “cleaver mesh options”:</p>
<pre><code>--sizing_field /path/field.nrrd
</code></pre>
<p>However, I still get an error when I run segmentmesher. Can you please let me know what is wrong in this procedure?<br>
Thanks in advance.</p>

---

## Post #12 by @lassoan (2020-10-23 00:41 UTC)

<ol>
<li>
<p>You need to replace the 0 label by setting to a constant and/or applying Gaussian blurring.</p>
</li>
<li>
<p>Extensions are rebuilt every night. You need to wait until tomorrow and then reinstall SegmentMesher to get latest Cleaver2 version.</p>
</li>
</ol>

---

## Post #13 by @Aep93 (2020-10-23 00:46 UTC)

<p>Thanks, <a class="mention" href="/u/lassoan">@lassoan</a>. I will replace the zero label with a constant and check again tomorrow and update you with my results. Thank you so much.</p>

---

## Post #14 by @Aep93 (2020-10-24 00:56 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I removed the zero label and used Gaussian blurring and it seems to work! Here is my final mesh which is fine for one part and coarse for another part:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6417366dd9b34ca1590c053ff9b37dd03aa8056.png" data-download-href="/uploads/short-url/uzopbZ0Z2XCBCTKYhZ4TEXDMnRk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6417366dd9b34ca1590c053ff9b37dd03aa8056.png" alt="image" data-base62-sha1="uzopbZ0Z2XCBCTKYhZ4TEXDMnRk" width="690" height="443" data-dominant-color="8D9086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">869×558 57.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, I uploaded my field <a href="https://github.com/A-ep93/SlicerTest/blob/main/fields1.nrrd?raw=true" rel="noopener nofollow ugc">here</a> so that others can check it in the future if they needed a sample case. I used a code similar to the following one and applied Gaussian blur after that:</p>
<pre><code>    volumeNode = getNode('fields')
    a = arrayFromVolume(volumeNode)
    a[a == 0] = 3
    a[a == 1] = 5
    a[a == 2] = 900
    arrayFromVolumeModified(volumeNode)
</code></pre>
<p>I think one may need to play with the sizing values and maybe the sigma (for gaussian blur filter) to obtain the desired mesh. I should mention that I just applied this on a simple model and not my main model and I may need further considerations for main model.<br>
Thank you so much <a class="mention" href="/u/lassoan">@lassoan</a> for all your help for this.</p>
<p>I have two questions now:</p>
<ol>
<li>
<p>I checked some older slicer versions (such as 4.10.1) and to me, it seems that the segmentmesher is not updated for them. Is this right?</p>
</li>
<li>
<p>I still could not find the relation between the generated meshes and sizing values I give. So maybe it is helpful if I can generate some meshes with segmentmesher and check their sizing field. Can you please let me know how should I export the sizing field from segmentmesher?</p>
</li>
</ol>
<p>Thanks in advance.</p>

---

## Post #15 by @lassoan (2020-10-24 01:18 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="14" data-topic="14168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I checked some older slicer versions (such as 4.10.1) and to me, it seems that the segmentmesher is not updated for them. Is this right?</p>
</blockquote>
</aside>
<p>It is always recommended to use the latest stable or preview release (currently, Slicer-4.11.20200930 and Slicer-4.13.1). Nightly extensions updates are only available for these releases.</p>
<aside class="quote no-group" data-username="Aep93" data-post="14" data-topic="14168">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I still could not find the relation between the generated meshes and sizing values I give</p>
</blockquote>
</aside>
<p>The sizing field defines the desired element size. I’m just not sure in what unit. You <a href="https://github.com/SCIInstitute/Cleaver2/issues">submit an issue to Cleaver2 repository</a> asking for clarification.</p>

---
