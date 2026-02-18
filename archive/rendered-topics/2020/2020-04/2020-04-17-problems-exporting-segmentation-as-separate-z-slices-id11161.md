# Problems exporting segmentation as separate Z slices

**Topic ID**: 11161
**Date**: 2020-04-17
**URL**: https://discourse.slicer.org/t/problems-exporting-segmentation-as-separate-z-slices/11161

---

## Post #1 by @Davide_Cester (2020-04-17 14:21 UTC)

<p>Hi everybody,</p>
<p>I need some help in exporting segmentations in a way that matches the original data. I searched the forum here and I solved part of the issue, but I can’t move forward.</p>
<p>I have a sequence of DICOM files, each one containing a 512x512 slice of a cardiac CT scan. A segmentation was made from these files with 3DSlicer, resulting in two files, nifti + nrrd. I can visualize everything and it looks good.<br>
Now I’m doing some data analysis and I need the segmentation as a sequence of slices matching the original ones in size, number and z position - what I will do is comparing 2D arrays.</p>
<p>Size (512x512) is not a big problem, I can either add pixels or save DICOM files with the proper size by setting the original volume as reference. The number of slices can also be fixed by adding empty segmentation slices at the beginning and at the end of the sequence.</p>
<p>But alignment along the Z axis seems to be a problem. When I export the segmentation as DICOM and check the Z information, Z spacing is something like 0.39 instead of 0.4 of the original sequence… as a result I can’t add a simple offset to align the two sequences, because I always have misalignments at the beginning or at the end of the sequence.</p>
<p>It looks like my export does not preserve all the properties of the original sequence/volume… what am I understanding or doing wrong? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> Any help would be highly appreciated!</p>
<p>I can also provide examples if needed…</p>

---

## Post #2 by @lassoan (2020-04-17 15:15 UTC)

<p>When you export a segmentation to labelmap, you can choose a reference volume. It ensures that the geometry (origin, spacing, axis directions, and spacing) exactly matches the reference volume’s geometry.</p>
<p>Do you export the data sets using Slicer’s DICOM exporter?<br>
For the original spacing of 0.4, is the exported spacing something like 0.39 or 0.399999999?</p>

---

## Post #3 by @Davide_Cester (2020-04-17 16:26 UTC)

<p>Hi! Thanks for your reply <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>The problem appears when, on the Data view, I right-click on the Segmentation and choose “Export to DICOM…”. The spacing when I read back the files is 0.3925. I think I chose the correct volume, because the output changed from cropped to 512x512, as the original dataset.</p>
<p>However, today I did some more search here on the forum, and it seems that by using “Modules → Converters → Export to DICOM Series” I get better results… I’m currently converting a few datasets to confirm it. Now the spacing offset is a constant .001 which I think is a more than acceptable effect of roundings.</p>
<p>As a side note, I have the impression that the “Reverse dataset” checkbox does not work, and the first slice of the segmentation export always corresponds to the last slice of the original dataset. I know there are different standards, I thought the checkbox could address this… no problem, I’ll reverse the filenames with a script.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e2d9687ba1db37fe6ffd2f041d0159b5cc24e4b.png" alt="Screenshot from 2020-04-17 18-23-53" data-base62-sha1="21qm6aBQHM9KRogmcbfYG5p3GOL" width="301" height="183"></p>

---

## Post #4 by @Davide_Cester (2020-04-17 16:33 UTC)

<p>Just for completeness, this is the procedure that does not work for me:</p><aside class="quote" data-post="1" data-topic="543">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/convert-image-and-segmentation-to-dicom/543">Convert image and segmentation to DICOM</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Andras, 
I am now trying to convert nrrd files to DICOM. The main image is 
converting just fine, but I am not able to figure out how to convert just 
the contour, as it does not show up when using “Create a DICOM series.” How 
can I also convert this file?
  </blockquote>
</aside>

<p>The “Create DICOM Series” seems to work and maybe is also be suitable for automation…</p><aside class="quote" data-post="1" data-topic="7996">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/958977/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/create-a-dicom-series-for-batch-of-images/7996">Create a DICOM Series for batch of images</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I am able to convert a nrrd file to a DICOM series manually using the Create a DICOM Series module, however, I can’t find a way to conduct this process automatically and I have 200 image sets that each need to be converted. Is there any way to do this DICOM creation in batch? 
Thanks!
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2020-04-17 23:39 UTC)

<p>Thanks for the update. Note that “Modules -&gt; Converters -&gt; Export to DICOM Series” exports segmentation as CT image volume, not as a DICOM segmentation object. You might be able to use it in some software but it is not the right thing to do.</p>

---

## Post #6 by @Davide_Cester (2020-04-18 13:45 UTC)

<p>I understand. In my case it should be fine, I need square images and the corresponding square segmentation masks to feed a neural network.</p>
<p>Thanks!</p>

---

## Post #7 by @lassoan (2020-04-18 14:24 UTC)

<p>DICOM format is unnecessarily complex for storing training data for neural networks.</p>
<p>Many people new to this field choose suboptimal formats for storing their training data. A quick overview of what is out there:</p>
<ul>
<li>consumer image file formats (png/jpg/tiff) are too simple, don’t use them for medical image data, as you may end up losing important information due to limited bit depth, unknown slice spacing and axis directions</li>
<li>DICOM is complex, it is hard to write and read them correctly, so there is a high chance that your information get misinterpreted</li>
<li>research file formats hit a good balance between complexity and feature set: they can store all important information without unnecessary complexity. Within these formats:
<ul>
<li>metatimage (mha, mhd): simple research file format, unfortunately you cannot specify axis kinds, so it is limited to handling 3D data (3D+t, 2D+t, etc. storage is ambiguous)</li>
<li>nifti (nii, nii.gz): very specialized and somewhat complex format for neuroimaging, it should only be used for neuroimaging data, where the complexity is actually necessary. <strong>I would only recommend NRRD for storing training data for brain (neuroimaging) applications</strong><br>
-nrrd good general-purpose research file format, it is very simple yet has no significant limitations. <strong>I would recommend NRRD for storing training data in general</strong>
</li>
</ul>
</li>
</ul>

---

## Post #8 by @Davide_Cester (2020-04-18 16:51 UTC)

<p>Thanks, I see your point. We’re using DICOM because we’re at the prototyping stage, I thought it was convenient to just use the original CT DICOM files as they are and convert the segmentation masks to the same format. But I see the meaning of using NRRD… I could probably invest some time in converting the dataset <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @lassoan (2020-04-18 17:25 UTC)

<p>Using DICOM has very strong, unique advantages, but convenience is not one of them. In medical imaging deep learning workflows you would normally use these formats:</p>
<ul>
<li>DICOM for archival: store your original CT data as is, in DICOM; it also makes sense to store segmentation data as proper DICOM segmentation object, too, especially if you share it with other groups (cross-references help in data integrity)</li>
<li>Research file formats (nrrd, nifti) for storing relevant data that you extracted from DICOM files (e.g., extracted images, structure sets, segmentation objects)</li>
<li>Numpy arrays (npy, npz) for normalized/augmented data (e.g., after prealigning, resampling, cropping), they can be read/written more efficiently than research file formats and they don’t need to store any metadata (as they are already normalized)</li>
</ul>
<p>Most medical imaging data sets start at level 2 (research file formats), so you don’t even have the option of storing everything in DICOM. If you are at prototyping level, then you don’t need to worry about DICOM for now, just create a solid process for getting all your data in a convenient research file format.</p>
<p>Later, if things start to get more serious, then DICOM becomes essential. If your are building your own database, then DICOM is good for disciplined, archival-level data storage. You also need DICOM when you connect your software directly to clinical systems, as all your input data will be in DICOM and you need to provide your results in DICOM.</p>

---
