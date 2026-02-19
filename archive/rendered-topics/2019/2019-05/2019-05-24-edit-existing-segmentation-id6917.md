---
topic_id: 6917
title: "Edit Existing Segmentation"
date: 2019-05-24
url: https://discourse.slicer.org/t/6917
---

# Edit existing segmentation

**Topic ID**: 6917
**Date**: 2019-05-24
**URL**: https://discourse.slicer.org/t/edit-existing-segmentation/6917

---

## Post #1 by @Christineseven (2019-05-24 10:05 UTC)

<p>Hello. I would like to ask, in image segmentation, when we have already the predicted mask and we want to correct it.What is the way to remove parts of the mask or add some parts(painting) to the already masks? without paint them from the start,but use the predicted.So just work on the mask with add painting and deleting. Thanks!</p>

---

## Post #2 by @lassoan (2019-05-24 13:38 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html" rel="nofollow noopener">Segment editor module</a> for this. See tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @Christineseven (2019-05-24 13:53 UTC)

<p>Thank you very much for your time:) I mean that we have an MRI image like this <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed80aa5eda828a64e059efa406e5f162d8e97a6f.png" alt="image" data-base62-sha1="xT2P9BEfz9U2X2J07WecCv4DK8v" width="256" height="197"><br>
(this is a polysistic kydney)<br>
and the mask for the kydney, that our model has predicted. Now we want to open them in slicer and edit this mask(just cutting and adding parts to the mask to make it fit better) and retrain our model. But when I use the Segment editor module does not work in this mask! We can paint…but we dont want to paint the whole kydney everywhere to define the mask we want.Also we can erase where we painted, but not in the existed mask for the kydney that we have!!we can erase only if we draw somewhere! We want it to add for example some edges in the mask in some slices where needed,or remove!</p>

---

## Post #4 by @Christineseven (2019-05-24 14:15 UTC)

<p>so, is there a way to load the predicted masks as “masks” and not just series of slices, so that the slicer recognize that they are masks and let us modify them (in the way that it would let us if we have made the mask manualy in slicer)? The files are dicom.</p>

---

## Post #5 by @cpinter (2019-05-24 14:59 UTC)

<p>Segment Editor can edit data that has the type “segmentation” in Slicer. If you load a mask, then it’s most probably a volume node. First, you need to make sure it’s a labelmap. In the loading screen if you open the options part, there will be a checkbox for loading it as labelmap. Alternatively you can convert it to labelmap in the Volumes module. Then you need to import the labelmap as a segmentation. Right-click the labelmap in the Data module and choose “Convert labelmap to segmentation node”. Then if you go the Segment Editor you can edit it, but first you need to select the MRI as Master volume.</p>
<p>Is this data is 3D? The image you pasted above seems strange to me.</p>

---

## Post #6 by @Christineseven (2019-05-28 07:46 UTC)

<p>Thank you for your time!!! I solved it like this, I uploaded the mask and the series(image MRI) and the problem was that it didnt recognize mask so I could not modify it. So these was the steps if someone is interested too<br>
load serie-load mask<br>
-go to volumes</p>
<ul>
<li>select mask</li>
<li>convert to scalar volume</li>
<li>go to editor and put master volume :  series, merge volume : mask</li>
<li>edit selected label mask</li>
<li>apply while you are modifying<br>
-save mask</li>
</ul>

---

## Post #7 by @JoostJM (2019-05-28 10:35 UTC)

<p><a class="mention" href="/u/christineseven">@Christineseven</a>,</p>
<p>If you have to do this for many patients, you can optionally also check out CaseIterator (in the extension manager under “utility”). I wrote this module to easily review a batch of cases, including reviewing (i.e. loading, adapting and saving under a new name) of segmentations. It automatically handles the conversion from labelmap to segmentation, and links it to you image (sets the mastervolume node).</p>
<p>If you have questions on how to use it, I’d be happy to help.</p>

---

## Post #10 by @Tamires_Zanao (2021-06-30 12:31 UTC)

<p>Hi! I followed your instructions and could properly edit the mask, but how should I save it in order to use it as a mask? I tried saving the segmentation (in nifti and in nrrd), but it was probably in the wrong “format”. I couldn’t use it for freesurfer. Thanks a lot!</p>

---

## Post #11 by @lassoan (2021-07-02 05:10 UTC)

<p>This last question was also posted and got answered here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="18429">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tamires_zanao/48/10306_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-save-brain-structural-edited-masks-segment-edited-in-nifti-for-freesurfer-use/18429">How to save brain structural edited masks (segment edited) in nifti for freesurfer use?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi! I automatically generated structural brain masks with the purpose of using FreeSurfer. The masks need some editing, and I used Slicer Segment Editor for it (opened mask as label &gt; imported labelmap as segmentation &gt; add T1 as master volume &gt; edited masks). However, I couldn’t save it as a nifti, so I saved as nrrd and later converted it to nifti. It didn’t work. How can I save my edited mask (in nifti) in order to use them for freesurfer? Do I have to convert the labelmap in something else? 
…
  </blockquote>
</aside>


---
