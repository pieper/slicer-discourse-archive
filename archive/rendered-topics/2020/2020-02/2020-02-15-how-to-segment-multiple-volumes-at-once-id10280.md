# How to segment multiple volumes at once?

**Topic ID**: 10280
**Date**: 2020-02-15
**URL**: https://discourse.slicer.org/t/how-to-segment-multiple-volumes-at-once/10280

---

## Post #1 by @Xi_Fang (2020-02-15 18:23 UTC)

<p>Currently I can make use of Clara model in 3D slicer to segment CT scans one by one. But I have tens of scans to segment. Loading and segmenting take a lot of time. Thus I wonder if I can segment tens of volumes at once and save all segmentation files?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-02-15 18:29 UTC)

<p>You can load data and run automatic segmentation using a couple of lines of Python code. See examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>. You may find “<a href="https://gist.github.com/lassoan/ef30bc27a22a648ead7f82243f5cc7d5">AI-assisted brain tumor segmentation</a>” particulary relevant.</p>

---

## Post #3 by @Xi_Fang (2020-02-16 00:08 UTC)

<p>Thanks for your reply. I’ll try that!</p>

---

## Post #4 by @Xi_Fang (2020-02-16 01:27 UTC)

<p>Thank you for your great job. I modified the code in your second link. Now I can segment and visualize the liver organ. However, I didn’t know how to save the segmentation file into ‘nii’ format. The segmentationNode seems to be ‘MRMLCorePython.vtkRMLSegmentationNode’. When I try to save it using ‘slicer.util.saveNode’, it always return ‘False’. Looking forward to your response!</p>

---

## Post #5 by @lassoan (2020-02-16 04:50 UTC)

<p>Nifti is developed for neuroimaging and for that it is a good choice, but it has several disadvantages when you try to use it as a general-purpose image file format.</p>
<p>Instead, I would recommend to use nrrd format. It has simple, human-readable header, can be easily customized to store custom fields, it has better support for multidimensional images, etc.</p>
<p>If you absolutely must use nifti (again, I would not recommend) then export the segmentation to binary labelmap and then you can save that in any format you want, including nifti.</p>

---

## Post #6 by @Xi_Fang (2020-02-16 05:23 UTC)

<p>Thanks for your quick response. The nrrd format works.</p>

---

## Post #7 by @Xi_Fang (2020-02-23 14:56 UTC)

<p>Hi, Lasso,<br>
I try to use Clara model to segment my local CT data. But currently, it doesn’t work now. The error is shown as below. Do you have any idea about that?<br>
http.client.RemoteDisconnected: Remote end closed connection without response</p>

---

## Post #8 by @lassoan (2020-02-23 15:20 UTC)

<p>There was a few-hour server outage yesterday and NVidia updated their extension in the last few days - any of these might have caused problems.</p>
<p>Which Slicer version are you using? Did the same version worked before? Do you use your own Clara server or the default Slicer server?</p>

---

## Post #9 by @Xi_Fang (2020-02-23 15:34 UTC)

<p>I use 3D slicer 4.11.0-2020-02-12 and the default slicer server.</p>

---

## Post #10 by @lassoan (2020-02-23 18:27 UTC)

<p>The server has been working well for months but today there seems to be some network connectivity issues with the server. The service should be restored soon or you can set up your own server.</p>

---

## Post #11 by @Xi_Fang (2020-02-25 15:57 UTC)

<p>Thank you. It seems the environment has been restored. However, there is still one volume that can’t be segmented. It may due to the large size of the volume. By the way, Do you have idea if I want to use the Clara model when using in publication. I didn’t find any citation online.</p>

---

## Post #12 by @lassoan (2020-02-25 18:31 UTC)

<aside class="quote no-group" data-username="Xi_Fang" data-post="11" data-topic="10280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xi_fang/48/6041_2.png" class="avatar"> Xi_Fang:</div>
<blockquote>
<p>However, there is still one volume that can’t be segmented.</p>
</blockquote>
</aside>
<p>You need to crop and resample input volume to approximately match inputs used for training.</p>
<aside class="quote no-group" data-username="Xi_Fang" data-post="11" data-topic="10280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xi_fang/48/6041_2.png" class="avatar"> Xi_Fang:</div>
<blockquote>
<p>Do you have idea if I want to use the Clara model when using in publication. I didn’t find any citation online.</p>
</blockquote>
</aside>
<p>I would refer to it as “NVidia Clara AIAA (NVidia, Santa Clara, California, U.S.A.) + the used model’s name” and also cite <a href="https://docs.nvidia.com/clara/aiaa/tlt-mi-ai-an-sdk-getting-started/#aiaa_segmentation_models">papers</a> that describe how the models were trained, and of course <a href="https://www.slicer.org/wiki/CitingSlicer">3D Slicer</a>.</p>

---
