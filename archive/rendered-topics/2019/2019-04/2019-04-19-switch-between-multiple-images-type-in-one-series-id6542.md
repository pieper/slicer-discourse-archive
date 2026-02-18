# Switch between multiple images type in one series

**Topic ID**: 6542
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/switch-between-multiple-images-type-in-one-series/6542

---

## Post #1 by @n2018 (2019-04-19 12:38 UTC)

<p>Hi, could you please tell me, if there is a way to switch between multiple images type in one series?<br>
I have a dicom study and for one series there are several type of contrast (several images types), for every type imageType is different:<br>
[5] ORIGINAL, PRIMARY, M_FFE, M, FFE<br>
[5] ORIGINAL, PRIMARY, M_IR, M, IR<br>
[5] ORIGINAL, PRIMARY, CR_IR, CR, IR<br>
so this series consists of three groups of the same images but in different contrast, when I import this series into slicer and then load them I have only one type of contrast but I want to have all of them in different nodes, is there a way to do it?</p>

---

## Post #2 by @lassoan (2019-04-19 16:59 UTC)

<p>Is this a 4D (3D+t) volume? If you enable advanced mode in the DICOM browser, is there an option to load the series as multi-volume?</p>
<p>Are the number and position of slices the same across all the time points? Which DICOM field can be used to distinguish groups of frames within the sequence?</p>
<p>The best would be if you could share an anonymized example data set that we can investigate.</p>

---

## Post #3 by @n2018 (2019-04-19 17:22 UTC)

<p>It is just 3D volume, but I have an option load the series as multi-volume. The number and position of slices are the same, but number of slices can be different. To distinguish between these different images you can use the field Image Type, as I mentioned above, they are different for different  images. Also, I tried to convert this series by mrtrix <a href="https://mrtrix.readthedocs.io/en/latest/reference/commands_list.html" rel="nofollow noopener">https://mrtrix.readthedocs.io/en/latest/reference/commands_list.html</a> program and this program separates these images as different series which is the desired result, that’s why I suppose it is possible to upload these images as different series</p>

---

## Post #4 by @lassoan (2019-04-19 17:49 UTC)

<aside class="quote no-group" data-username="n2018" data-post="3" data-topic="6542">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/n2018/48/3287_2.png" class="avatar"> n2018:</div>
<blockquote>
<p>separates these images as different series</p>
</blockquote>
</aside>
<p>Are these really different series (have different series instance UID)? If yes, then they should show up as separate loadable items in the DICOM browser.</p>
<p>If not, then you have a few options:</p>
<ul>
<li>Split series by time and load only those that have the same content time. For this, enable in menu: Edit / Application settings / DICOM / Allow loading subseries by time. Then enable advanced mode in DICOM browser, select the series, click Examine, and see if you are offered those subseries that you need.</li>
<li>Use MultiVolumeImporterPlugin to load the series as a multi-volume. The importer will recognize the subseries if they can be split based on one the value the listed <a href="https://github.com/fedorov/MultiVolumeImporter/blob/28cde0cab271a6fe2e3dd6c57f911b90de56428b/MultiVolumeImporterPlugin.py#L37-L55">grouping tags</a> and number and position of frames across all time points is the same.</li>
<li>Use dcm2niix to split the input DICOM series into multiple volumes and load them one by one into Slicer.</li>
</ul>

---

## Post #5 by @n2018 (2019-04-19 18:45 UTC)

<p>thanks a lot, the first option helped, just examined and uploaded my data as volume sequence and see the desired results</p>

---
