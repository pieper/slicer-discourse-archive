---
topic_id: 5000
title: "Editor To Measure Volume"
date: 2018-12-06
url: https://discourse.slicer.org/t/5000
---

# Editor to measure volume

**Topic ID**: 5000
**Date**: 2018-12-06
**URL**: https://discourse.slicer.org/t/editor-to-measure-volume/5000

---

## Post #1 by @Candice_Nguyen (2018-12-06 19:44 UTC)

<p>Operating system:  MAC<br>
Slicer version: 4.11</p>
<p>I am using slicer to measure volume of the brain. I typically trace the area I want with draw effect and fill it. I do same thing slide by slide until the whole volume I am interested in is filled. I then use label statistic to get the volume. The program gives me volume and standard deviation. Can anyone please explain what the standard deviation means? I noticed with some measurements I got larger standard deviations than others. What can I do to improve my method and get a more accurate/precise measurements? Thanks</p>

---

## Post #2 by @cpinter (2018-12-06 20:01 UTC)

<p>First, I’d suggest that you use Segment Editor for segmentation, which has a Fill between slices tool that allows you to skip slices and then automatically fill the gaps in - this would fit your workflow and speed it up (and also the Editor module will be removed in 5.0).<br>
Then you can use Segment Statistics to calculate the volume.</p>
<p>Standard deviation is about the voxel intensities not the volume. The volume is an exact measurement.</p>

---

## Post #3 by @Candice_Nguyen (2018-12-09 20:04 UTC)

<p>So I am trying to use segment editor like you suggested, but as I filled a slide on axial, slides above and below were also filled. What happened if I do not want to include slides below and above?</p>
<p>Also, when I use fill between slides, there seem to be gaps. Will it affect my volume measurement? Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2f380b2e507bfa42a7b3c6ee75ef27ca7324f31.png" data-download-href="/uploads/short-url/wnHBQOxADBtzft0z47J4TTjtKlX.png?dl=1" title="03%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2f380b2e507bfa42a7b3c6ee75ef27ca7324f31_2_690x462.png" alt="03%20PM" data-base62-sha1="wnHBQOxADBtzft0z47J4TTjtKlX" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2f380b2e507bfa42a7b3c6ee75ef27ca7324f31_2_690x462.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2f380b2e507bfa42a7b3c6ee75ef27ca7324f31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2f380b2e507bfa42a7b3c6ee75ef27ca7324f31.png 2x" data-dominant-color="92949F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03%20PM</span><span class="informations">946×634 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @cpinter (2018-12-09 20:33 UTC)

<p>You only fill one slice by default. Based on your screenshot your volume is not axis-aligned. You need to rotate the slice plane so that it aligns with your volume.</p><aside class="quote quote-modified" data-post="4" data-topic="1459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">Segmentation Editor - How to disable painting on adjacent slices?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    If the acquisition was tilted you may need to rotate to volume plane (click the “pushpin” icon in the top-left corner of the slice view, then click the double-arrow button on the left, then the “Rotate to volume plane” icon appears): 
[image] 
Here’s an example drawing on the original slice (patient space) 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee6244f649d4f68c2cd1a14c4e489972a0a5755e.jpeg" data-download-href="/uploads/short-url/y0Qb6Ef1694zMHYIT45Xx6cE0bQ.jpg?dl=1" title="image">[image]</a> 
And here the paint stroke on the right is after rotating the red slice into the acquisition plane and only one plane is painted in the other views. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27e575499b56b012ea2cc088c24f38cb43202281.jpeg" data-download-href="/uploads/short-url/5GWesknjInRIylPfDboX3rTkF8Z.jpg?dl=1" title="image">[image]</a>
  </blockquote>
</aside>


---

## Post #5 by @lassoan (2018-12-09 23:59 UTC)

<p>Yes, what you see is a feature: Slicer’s Segment Editor module allows editing on arbitrarily oriented views, which may intersect multiple slices.</p>
<p>Recent versions of Slicer show a warning button (with an exclamation mark) if any of the slice viewers are not aligned with the current segmentation axes. Click that button to snap each slice view to nearest segmentation axis.</p>
<p>If “Fill between slices” effect finds segments on consecutive slices then it considers them already 3D (already filled). So, you need to work with axis-aligned slice viewers and skip at least one slice between segmented slices.</p>
<p>Volume is reported for exactly what you see. If you see that segmentation is incomplete/inaccurate then you need to fix that before you compute volume.</p>

---

## Post #6 by @Candice_Nguyen (2018-12-15 21:01 UTC)

<p>Where is the ruler option on slicer so I can measure diameter?</p>
<p>Thanks so much for all your helps</p>

---

## Post #7 by @lassoan (2018-12-15 23:46 UTC)

<p>You can use the annotation toolbar to add a ruler - see details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Annotations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Annotations</a></p>

---

## Post #8 by @Candice_Nguyen (2018-12-15 23:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e143de62e202b268cb8633d4068337bd8a30f64c.png" data-download-href="/uploads/short-url/w8MQ0AnqfIetLqpK47vd16SbsMQ.png?dl=1" title="44%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e143de62e202b268cb8633d4068337bd8a30f64c_2_331x500.png" alt="44%20PM" data-base62-sha1="w8MQ0AnqfIetLqpK47vd16SbsMQ" width="331" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e143de62e202b268cb8633d4068337bd8a30f64c_2_331x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e143de62e202b268cb8633d4068337bd8a30f64c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e143de62e202b268cb8633d4068337bd8a30f64c.png 2x" data-dominant-color="070705"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">44%20PM</span><span class="informations">475×717 12.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am not sure why, but slicer is not showing me full view of these two slides and on the other view, I can’t roll between views like how we normally view CT scans. I randomly got it work one time and I could not get it worked again…Please help!!! Thanks…</p>

---

## Post #9 by @lassoan (2018-12-16 00:06 UTC)

<p>Have you loaded your data set using DICOM module (using the DICOM browser that shows patient, study, series list)?</p>
<p>You may have several image series in a study and some of them may be single-slice, so make sure you choose a volumetric image. You can load all series in a study then go to Data module and click on eye icons to choose which one you would like to see.</p>

---

## Post #10 by @Candice_Nguyen (2018-12-16 00:12 UTC)

<p>Yes I used DICOM. I pick patient then the views that have acquisition number to load. Normally it will just load images in three views sagital, coronal and axial. I am not sure what is wrong with this disc (I have not experienced this problem before), like you said some study may be single slice, but I got it to work on same disc, but I can’t get it to work again unfortunately.</p>

---

## Post #11 by @lassoan (2018-12-16 00:14 UTC)

<p>Could you attach a screenshot of your DICOM browser? (erase patient name and ID if it is non-anonymized human patient data)</p>

---

## Post #12 by @Candice_Nguyen (2018-12-16 00:19 UTC)

<p>Unfortunately it is non anonymized.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a073b50e291cc72e36262cf47b33899c186ec82e.png" data-download-href="/uploads/short-url/mTqipiZLDuB6Hxzmn4ilxTFYHRs.png?dl=1" title="35%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a073b50e291cc72e36262cf47b33899c186ec82e_2_690x143.png" alt="35%20PM" data-base62-sha1="mTqipiZLDuB6Hxzmn4ilxTFYHRs" width="690" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a073b50e291cc72e36262cf47b33899c186ec82e_2_690x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a073b50e291cc72e36262cf47b33899c186ec82e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a073b50e291cc72e36262cf47b33899c186ec82e.png 2x" data-dominant-color="DBE3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">35%20PM</span><span class="informations">840×175 20 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I normally picked to open all views with acquisition number that is not 0. I need all three views to work.</p>

---

## Post #13 by @lassoan (2018-12-16 00:26 UTC)

<p>From this screenshot it is not obvious if any of these are volumetric acquisitions. You can verify if there are multiple frames in a series by clicking “Metadata” button: if there is a slider near the top of the window then it confirms that the series contains multiple frames.</p>

---

## Post #14 by @Candice_Nguyen (2018-12-16 00:48 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87bfb4dd2fe00a5feb7062a8358d4f9feac5a63b.png" data-download-href="/uploads/short-url/jmTbDSg8WGbTAArEjrAmaXI9HRx.png?dl=1" title="29%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87bfb4dd2fe00a5feb7062a8358d4f9feac5a63b_2_690x54.png" alt="29%20PM" data-base62-sha1="jmTbDSg8WGbTAArEjrAmaXI9HRx" width="690" height="54" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87bfb4dd2fe00a5feb7062a8358d4f9feac5a63b_2_690x54.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87bfb4dd2fe00a5feb7062a8358d4f9feac5a63b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87bfb4dd2fe00a5feb7062a8358d4f9feac5a63b.png 2x" data-dominant-color="F1F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">29%20PM</span><span class="informations">891×70 5.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is this the slider?</p>
<p>It gotta have multiple frames because I got it to work and measured some volumes…closed it…then can not get it back to work again…</p>

---

## Post #15 by @lassoan (2018-12-16 01:09 UTC)

<p>Did you select a single series when you got this slider? If yes, then it is a volume and if you click “Load” then you should see a volume (a full image in all three orthogonal slice viewers).</p>

---

## Post #16 by @Candice_Nguyen (2018-12-17 01:21 UTC)

<p>Hello,</p>
<p>I got it figure out at last…but now I am having another the problem as I tried to learn to use segment editor instead of editor.</p>
<ol>
<li><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e84cd9e00b85cc1f08b0e1f6e7bdcd671ec80456.png" alt="46%20PM" data-base62-sha1="x91qoP6WcpFg7IkaJOsuTJ92R3E" width="562" height="224"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59d5f3f7bd51019c106f852919ab7081c8698eb0.png" alt="54%20PM" data-base62-sha1="cOISZQjE4Gj9lX1LwOW5PldIV7a" width="574" height="385"></li>
</ol>
<p>How do I pull up segment_1 on segment stat to calculate volume?</p>
<p>With editor, all I have to do is use coronal on editor and pull coronal on stat to get volume. Segment editor and segment stat are more complicated.</p>
<ol start="2">
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6f907bfd15314278847319d257ba5af7862e8a7.jpeg" data-download-href="/uploads/short-url/zeP0a5wUvcU5XzXL1eCJN8ngSFN.jpeg?dl=1" title="IMG_5636" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f907bfd15314278847319d257ba5af7862e8a7_2_374x500.jpeg" alt="IMG_5636" data-base62-sha1="zeP0a5wUvcU5XzXL1eCJN8ngSFN" width="374" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f907bfd15314278847319d257ba5af7862e8a7_2_374x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f907bfd15314278847319d257ba5af7862e8a7_2_561x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f907bfd15314278847319d257ba5af7862e8a7_2_748x1000.jpeg 2x" data-dominant-color="767984"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_5636</span><span class="informations">2138×2851 2.59 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I used fill between slide and got this model but it does not look solid. What did I do wrong?</li>
</ol>
<p>THANKS SO MUCH</p>

---

## Post #17 by @Candice_Nguyen (2018-12-17 01:22 UTC)

<ol start="3">
<li>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5a346ed76607012b43f38dfd0ad07076875d44d.jpeg" data-download-href="/uploads/short-url/pUQeYRMSaot4Tu0TXAPYA7n6jrn.jpeg?dl=1" title="IMG_5637" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a346ed76607012b43f38dfd0ad07076875d44d_2_375x500.jpeg" alt="IMG_5637" data-base62-sha1="pUQeYRMSaot4Tu0TXAPYA7n6jrn" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a346ed76607012b43f38dfd0ad07076875d44d_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a346ed76607012b43f38dfd0ad07076875d44d_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a346ed76607012b43f38dfd0ad07076875d44d_2_750x1000.jpeg 2x" data-dominant-color="646259"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_5637</span><span class="informations">3024×4032 2.36 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
<br>
Why are there color outside the skull? I do not understand how fill in between works so I just want to make sure I get as accurate results as possible.</li>
</ol>
<p>THANKS SO MUCH!!!</p>

---

## Post #18 by @lassoan (2018-12-17 03:00 UTC)

<p>You need to use Segment Editor module (and not the legacy Editor module). Can you confirm that you are using Segment Editor?</p>

---

## Post #19 by @Candice_Nguyen (2018-12-17 18:34 UTC)

<p>Below is what I used from the all modules tab:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5c3679d22f31e8803522d6081daa61e2d354746.png" alt="02%20AM" data-base62-sha1="wMzZARtNYhLNiYK2i7BKzbdwymW" width="293" height="60"></p>

---

## Post #20 by @Candice_Nguyen (2018-12-21 21:40 UTC)

<p>HELP Please!!! THANKS SO MUCH</p>

---

## Post #21 by @lassoan (2018-12-21 22:36 UTC)

<p>It seems that you do the right thing. If the segmentation looks correct in slice and 3D views then the computed volume will be correct, too.</p>
<p>If the segmentation is not accurate then start it again. If you are not yet confident in using the Segment Editor then I would suggest to complete all available <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">segmentation tutorials</a>. You may also call in the weekly hangouts (see posts in community category about dates&amp;times) or can <a href="https://na-mic.github.io/ProjectWeek/" rel="nofollow noopener">attend a project week</a> to learn from Slicer users and developers in person.</p>

---

## Post #22 by @Candice_Nguyen (2018-12-22 19:17 UTC)

<p>Thanks, I will try to improve my technique with segmentation tutorials.</p>
<p>Is there tutorial for segment stat?<br>
I segmented the area I wanted but then I have problem of what to do after that so when I go to segment stat I can pick the area I segmented to measure volume</p>
<p>Pic below shows I segmented 5:coronal_1, but once I go to seg stat, I don’t know what to do to get volume</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7277160c0e34a059150c44c7b30abcce7547c5.png" data-download-href="/uploads/short-url/fL3Lg9xbafRN1dbou7LM2keNywB.png?dl=1" title="23%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7277160c0e34a059150c44c7b30abcce7547c5_2_475x500.png" alt="23%20PM" data-base62-sha1="fL3Lg9xbafRN1dbou7LM2keNywB" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7277160c0e34a059150c44c7b30abcce7547c5_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7277160c0e34a059150c44c7b30abcce7547c5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7277160c0e34a059150c44c7b30abcce7547c5.png 2x" data-dominant-color="EDF1F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">23%20PM</span><span class="informations">593×623 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @Candice_Nguyen (2018-12-22 19:18 UTC)

<p>See above. Thanks so much for your help.</p>

---

## Post #24 by @lassoan (2018-12-22 19:36 UTC)

<p>Click “Select a Table” and create a new table or select an existing table. Then click “Apply”.</p>

---
