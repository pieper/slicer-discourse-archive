---
topic_id: 14261
title: "Problem In Using Segmentmesher"
date: 2020-10-27
url: https://discourse.slicer.org/t/14261
---

# Problem in using segmentmesher

**Topic ID**: 14261
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/problem-in-using-segmentmesher/14261

---

## Post #1 by @Aep93 (2020-10-27 01:36 UTC)

<p>Hello,<br>
I encountered a problem while using segmentmesher. I used slicer 4.10.1 in the past and now I am moving to the newest stable version. I found that the segmentmesher in the previous version needs considerably less RAM than the one in the latest version; I checked this with multiple examples and I can post some of them with details here if necessary. I should mention that I use the same settings for segmentmesher on both versions.<br>
Any ideas on where this problem is coming from?<br>
It is true that we are always encouraged to use the newest version but in this case, I could use old segmentmesher for generating mesh for my model while the new version needs a lot of RAM which leads to killing the process due to lack of RAM on my system. On the other hand, I have to use the newest version to benefit from the updates.<br>
Any helps on this is greatly appreciated.<br>
I have attached the python codes of segment mesher of both version in case they can be helpful.</p>
<p><a href="https://github.com/A-ep93/SlicerTest/blob/main/compare.zip?raw=true" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/A-ep93/SlicerTest/blob/main/compare.zip?raw=true</a></p>

---

## Post #2 by @lassoan (2020-10-27 02:08 UTC)

<p>In Slicer-4.11.20200930 we upgraded to latest Cleaver2 version (in Slicer-4.10.2 we use a 3 years old version). Some command-line arguments slightly changed, as spacing is now correctly taken into account, while previously it was ignored (and the parameters were interpreted in voxel space).</p>
<p>You can get the same quality results with the same memory usage as before, but you may need to adjust the <code>--feature-scaling</code>, <code>--sampling-rate</code>, and <code>--lipschitz</code> parameters as described <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters">here</a>.</p>

---

## Post #3 by @Aep93 (2020-10-27 02:41 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I know that you updated the cleaver for the new version. In fact, I was one of the users who asked for it <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:">.<br>
I know that the command lines are changed and I considered that. But there I think there is something else that causing the problem. I even checked it with another version (4.11.0). In that version, the cleaver is not still updated, but it still needs more RAM in comparison to the 4.10.1. Having this in mind, do you have any idea on what can cause this problem?</p>

---

## Post #4 by @lassoan (2020-10-27 02:51 UTC)

<p>You can ask Cleaver developers, but I don’t think there was a change in the algorithm that would have increased the memory usage. All Cleaver changes looked mostly cosmetics and bugfixes, nothing fundamental.</p>

---

## Post #5 by @Aep93 (2020-10-27 02:58 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Is there any way to find the changes of segmentmesher from time to time?<br>
It can help me to track the changes and better explaining it to cleaver developers.</p>

---

## Post #6 by @lassoan (2020-10-27 03:09 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="5" data-topic="14261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Is there any way to find the changes of segmentmesher from time to time?</p>
</blockquote>
</aside>
<p>It’s all on github, so you can compare any versions very easily. The Cleaver upgrade commit is here: <a href="https://github.com/lassoan/SlicerSegmentMesher/commit/2c42c47dc1dd37318026b17fb63c844855dcfcb2" class="inline-onebox">Update Cleaver2 to latest master version · lassoan/SlicerSegmentMesher@2c42c47 · GitHub</a></p>
<p>As you can see, the only relevant changes are updating Cleaver2 version (repository and git hash) and command-line argument names and default values.</p>

---

## Post #7 by @Aep93 (2020-10-27 18:36 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>. I did lots of trial and errors in different versions. I found that adding these lines results in increasing the RAM needed for calculations:</p>
<pre><code># Set reference geometry in labelmapVolumeNode
referenceGeometry_Segmentation = slicer.vtkOrientedImageData()
inputSegmentation.GetSegmentation().SetImageGeometryFromCommonLabelmapGeometry(referenceGeometry_Segmentation, None,
  slicer.vtkSegmentation.EXTENT_REFERENCE_GEOMETRY)
slicer.modules.segmentations.logic().CopyOrientedImageDataToVolumeNode(referenceGeometry_Segmentation, labelmapVolumeNode)

# Add margin
extent = labelmapVolumeNode.GetImageData().GetExtent()
paddedExtent = [0, -1, 0, -1, 0, -1]
for axisIndex in range(3):
  paddingSizeVoxels = int((extent[axisIndex * 2 + 1] - extent[axisIndex * 2]) * paddingRatio)
  paddedExtent[axisIndex * 2] = extent[axisIndex * 2] - paddingSizeVoxels
  paddedExtent[axisIndex * 2 + 1] = extent[axisIndex * 2 + 1] + paddingSizeVoxels
labelmapVolumeNode.GetImageData().SetExtent(paddedExtent)
labelmapVolumeNode.ShiftImageDataExtentToZeroStart()
</code></pre>
<p>I deleted this in several versions up to 4.11.0 and it worked without error and resulted in considerably lower RAM usage. However, in the last version (4.11.20200930), when I delete these lines, the segmentmesher does not work and give this error:</p>
<pre><code>Nrrd file read error: No zero crossing in indicator function. Not a valid file or need a lower sigma value.
</code></pre>
<p>Now I have two questions:</p>
<ol>
<li>Why I get an error in the last version when I delete these lines while other versions work well?</li>
<li>Can we modify these codes to result in lower RAM usage without deleting them?</li>
</ol>
<p>Your help is greatly appreciated.</p>

---

## Post #8 by @lassoan (2020-10-27 18:43 UTC)

<p>Exporting the segmentation to labelmap and padding of the image should not result in significant memory increase, as the whole image should not be more than a few hundred MB in size and you are expected to have at least 5-10GB of free memory.</p>
<blockquote>
<p>Nrrd file read error: No zero crossing in indicator function. Not a valid file or need a lower sigma value.</p>
</blockquote>
<p>Most likely you get this error because you are using an old Cleaver version (where indicator functions are used by default) with a new Slicer version (that does not set the --segmentation option because it does not exist in current Cleaver version).</p>
<p>If you want to experiment with various older Cleaver versions then you probably need to do it by using the command-line. You can find all the Cleaver command-line options that Slicer uses in the application log and you have the option in Segment Mesher to preserve data sets that it provided to Cleaver.</p>

---

## Post #9 by @Aep93 (2020-10-27 20:30 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
I checked the nrrd file created during using segmentmesher in my temp folder. Its size is about 2.1 gb and I think it is very large. I have 64 GB of RAM but I am not still able to get the mesh I want. Is there any way to change my segmentation so that it results in smaller labelmap file?<br>
This way maybe I do not need even to delete that code lines and I can use the segmentmesher as it is.<br>
Thanks in advance</p>

---

## Post #10 by @lassoan (2020-10-27 21:24 UTC)

<p>2.1GB image is very big for a patient image. I guess you oversampled the image so that you can create margins more accurately. What is the spacing of the volume and number of voxels along each axis?</p>

---

## Post #11 by @Aep93 (2020-10-27 21:47 UTC)

<p>So my problem is definitely related to this large volume. Spacing is 1mm in all directions and dimensions are 1012,1024,1014.<br>
Are there anyways so that I can reduce my generated label maps size without the need to do all segmentations again?</p>

---

## Post #12 by @Aep93 (2020-10-28 01:37 UTC)

<p>Hello again <a class="mention" href="/u/lassoan">@lassoan</a>. I could reduce the size of my current segmentatin by changing the master volume to a smaller one in segment editor. Now my generated label map is about 500mb.<br>
I reinstalled everything (slicer + segmentmesher) but gain, I get this error:</p>
<pre><code>Generate mesh using: /home/user/.config/NA-MIC/Extensions- 
29402/SegmentMesher/lib/Slicer-4.11/cleaver-cli: ['--input_files', '/tmp/Slicer- 
user/SegmentMesher/20201027_210026_627/inputLabelmap.nrrd', '--output_path', 
'/tmp/Slicer-user/SegmentMesher/20201027_210026_627/', '--output_format', 
'vtkUSG', '--fix_tet_windup', '--strip_exterior', '--verbose', '--feature_scaling', '2', '-- 
 sampling_rate', '0.2']

Nrrd file read error: No zero crossing in indicator function. Not a valid file or need a lower sigma value.

Command 'cleaver-cli' returned non-zero exit status 11.
</code></pre>
<p>I am using the last stable version of slicer with the last segmentmesher. So what is causing this error now?</p>
<p>Thanks in advance for your help.</p>

---
