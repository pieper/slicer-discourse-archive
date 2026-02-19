---
topic_id: 1494
title: "Open Lung Ct Tiff Files"
date: 2017-11-20
url: https://discourse.slicer.org/t/1494
---

# Open lung CT tiff files

**Topic ID**: 1494
**Date**: 2017-11-20
**URL**: https://discourse.slicer.org/t/open-lung-ct-tiff-files/1494

---

## Post #1 by @laura_rodriguez (2017-11-20 17:54 UTC)

<p>Hello again</p>
<p>One silly question</p>
<p>I am trying to import tiff or bmp files to built a volume with 3dslicer, in theory it works, but, It only builds a multi-volume file, one for each slice. I would like it to build one single volume with all the slices, is it possible? Just in those cases in which I did not have dicom files. here I show you how I am trying to do it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b094cdf17ce63f6708ac23845790a931978ad2eb.png" data-download-href="/uploads/short-url/pc6QvtjZ68H0mW7BoKVoYqRmWaT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b094cdf17ce63f6708ac23845790a931978ad2eb_2_690x289.png" alt="image" data-base62-sha1="pc6QvtjZ68H0mW7BoKVoYqRmWaT" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b094cdf17ce63f6708ac23845790a931978ad2eb_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b094cdf17ce63f6708ac23845790a931978ad2eb_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b094cdf17ce63f6708ac23845790a931978ad2eb.png 2x" data-dominant-color="D7D8DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1113×467 85.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In volume menu this is what appears. I have to change parameters to built them in the correct size, but if I have to do this with each image it can be neverending.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/8639686b3f14afd154a8b0bde07ca17e438f0156.jpeg" alt="image" data-base62-sha1="j9oYz5o3R0TKMXSfEPcV5JNT1bM" width="567" height="354"></p>
<p>I would like to import also *flt files in 3dslicer. Is that possible?</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2017-11-20 17:59 UTC)

<p>See this thread: <a href="https://discourse.slicer.org/t/unable-to-do-3d-rendering-from-a-sequence-of-tiff-images/1345/3">Unable to do 3D rendering from a sequence of tiff images</a></p>

---

## Post #3 by @laura_rodriguez (2017-11-20 19:03 UTC)

<p>I have done all that, if you have a look to the first image you can see single file bottom is uncheck. In Volume menu, they appear each one of the images separately and not building a volume.</p>
<p>Any idea?</p>

---

## Post #4 by @laura_rodriguez (2017-11-20 19:07 UTC)

<p>Forget it, I only have to load one file, I was loading all of them…</p>
<p>Thank you for that.</p>
<p>I am continuing playing with the software</p>
<p>L</p>

---

## Post #5 by @CRISTIAN_ARMANDO_HER (2017-11-28 13:30 UTC)

<p>Hello Laura,</p>
<p>I have the same problem for to load tiff images, but I don’t understand the instructions. Have I to load only a image? then how the volume is building with only a image?</p>
<p>Please, can you explain me how to do that it works?</p>

---

## Post #6 by @lassoan (2017-11-28 13:53 UTC)

<p>What did you do? What did you expect to happen? What happened instead?</p>

---

## Post #7 by @CRISTIAN_ARMANDO_HER (2017-11-28 14:22 UTC)

<p>Hello,<br>
I have the tiff images of a CT Scan. I tried to load the images but the volume is not building, the images appears isolated. So I tried to follow this instructions: <a href="https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a><br>
If I understand the step 2, only a image need to be load. But when I do that only can see that slice.</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2017-11-28 15:03 UTC)

<p>Have you performed this step? “Click on Show Options and uncheck the Single File option”</p>

---

## Post #9 by @Sarang_Goel (2020-12-26 20:29 UTC)

<p>I have done this, but just like cristian, I can only view one image. How can i see the full 3d volume? I have also followed all of the suggested steps above.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d3018c65bc2ce334afc0d69bd6329a8b3a9537a.png" data-download-href="/uploads/short-url/b0POlGBocATNpVIcChlsOjiHVvI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d3018c65bc2ce334afc0d69bd6329a8b3a9537a_2_690x444.png" alt="image" data-base62-sha1="b0POlGBocATNpVIcChlsOjiHVvI" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d3018c65bc2ce334afc0d69bd6329a8b3a9537a_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d3018c65bc2ce334afc0d69bd6329a8b3a9537a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d3018c65bc2ce334afc0d69bd6329a8b3a9537a.png 2x" data-dominant-color="BEBEC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×578 73.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2020-12-26 20:32 UTC)

<p>You do have a volume, but since it came from a non-medical image format the default spacing of 1mm is used.  You need to find out the correct spacing values and type them into the boxes.</p>

---

## Post #11 by @Sarang_Goel (2020-12-26 22:29 UTC)

<p>I don’t understand …  I did as you said, but it still isn’t displaying it correctly:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a42642b5c81f22ec48a3c9d05fc93c7d231a0d5.jpeg" data-download-href="/uploads/short-url/aAVzGb6wgEPFS6DahA5iHGidWQt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a42642b5c81f22ec48a3c9d05fc93c7d231a0d5_2_690x359.jpeg" alt="image" data-base62-sha1="aAVzGb6wgEPFS6DahA5iHGidWQt" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a42642b5c81f22ec48a3c9d05fc93c7d231a0d5_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a42642b5c81f22ec48a3c9d05fc93c7d231a0d5_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4a42642b5c81f22ec48a3c9d05fc93c7d231a0d5_2_1380x718.jpeg 2x" data-dominant-color="7A7981"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1889×985 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @muratmaga (2020-12-26 22:32 UTC)

<p>What do you want to see? All three planes are now visible, use the slides above each slice view to navigate different slices.<br>
Do you want to use 3D view? If so, you will need to use the Volume Rendering module.</p>

---

## Post #13 by @Sarang_Goel (2020-12-26 22:34 UTC)

<p>I do want to see the 3d view, so how would I use the volume rendering module to create it? Btw thank you guys so much for you help!</p>

---

## Post #14 by @muratmaga (2020-12-26 22:44 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="" height="">

<h3><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" target="_blank" rel="noopener nofollow ugc">Volume rendering — 3D Slicer  documentation</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #15 by @Sarang_Goel (2020-12-26 23:21 UTC)

<p>The documentation was very helpful. However, I still have some problems. Do you know what I may do to make the 3d visualization more clear?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925ceb819042ae948667324ac6f3c9dca9abb25b.jpeg" data-download-href="/uploads/short-url/kSMN1E8CJIrQf5eGfhDmo75z3VF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/925ceb819042ae948667324ac6f3c9dca9abb25b_2_690x361.jpeg" alt="image" data-base62-sha1="kSMN1E8CJIrQf5eGfhDmo75z3VF" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/925ceb819042ae948667324ac6f3c9dca9abb25b_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/925ceb819042ae948667324ac6f3c9dca9abb25b_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/925ceb819042ae948667324ac6f3c9dca9abb25b_2_1380x722.jpeg 2x" data-dominant-color="85878A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1005 534 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @muratmaga (2020-12-27 00:10 UTC)

<p>This looks like a clinical CT scan, for which presets provided in the volume rendering module works reasonably well. Did you try chest CT?  You can also use the Shift slider left and right to see if you can improve the visualization.</p>

---

## Post #17 by @lassoan (2020-12-27 01:41 UTC)

<p><a class="mention" href="/u/sarang_goel">@Sarang_Goel</a> please write a bit about your overall goal. You can get much more relevant answers much quicker if we know what you would like to achieve.</p>
<p>What anatomy and disease you are interested in? What is the clinical question you would like to get answered? What kind of visualization, processing, or analysis do you think would help you?</p>

---

## Post #18 by @Sarang_Goel (2020-12-27 01:43 UTC)

<p>So I have tried chest CT, but I am continuously getting the body with the image. However, I just want the lung. If I move the slider, the body does disappear, but so does the lung, leaving only the rib cage. Do you know what may I do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9433ddadf03e24460bf2ba54846b620bc26f323.jpeg" data-download-href="/uploads/short-url/uZZFSZqsQcjBP8cXgtxufs6GVVx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9433ddadf03e24460bf2ba54846b620bc26f323_2_690x369.jpeg" alt="image" data-base62-sha1="uZZFSZqsQcjBP8cXgtxufs6GVVx" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9433ddadf03e24460bf2ba54846b620bc26f323_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9433ddadf03e24460bf2ba54846b620bc26f323_2_1035x553.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d9433ddadf03e24460bf2ba54846b620bc26f323_2_1380x738.jpeg 2x" data-dominant-color="7C7C80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1029 483 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @Sarang_Goel (2020-12-27 01:44 UTC)

<p>So what my goal is to have the lung displayed, while simaltaneously dispalying a series of masked images (of abnormalities). It is centered around covid-19. These masks are already created and are also in tif format.</p>

---

## Post #20 by @lassoan (2020-12-27 02:26 UTC)

<p>For covid lung visualizations, lung segmentation, and volumetric analysis you can use <a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">Lung CT analyzer</a> extension. It is a Python scripted module so you can easily extend and customize it. We can also help making improvements or adding features, just let us know what you need.</p>

---

## Post #21 by @Sarang_Goel (2020-12-27 17:42 UTC)

<p>The results are looking okay, however it keeps capturing other things, such as the space outside the lungs. Do you know how I may stop this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b89b0a92fdcde9c32d6fe7e1ce17a0d85c498d3.jpeg" data-download-href="/uploads/short-url/1E4fBYnvbgcoUZTvtlddB21wnZx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b89b0a92fdcde9c32d6fe7e1ce17a0d85c498d3_2_690x367.jpeg" alt="image" data-base62-sha1="1E4fBYnvbgcoUZTvtlddB21wnZx" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b89b0a92fdcde9c32d6fe7e1ce17a0d85c498d3_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b89b0a92fdcde9c32d6fe7e1ce17a0d85c498d3_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b89b0a92fdcde9c32d6fe7e1ce17a0d85c498d3_2_1380x734.jpeg 2x" data-dominant-color="909488"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1022 351 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @Sarang_Goel (2020-12-27 17:43 UTC)

<p>I may also be worth to note that even if I placed more markers, this still occurs. In the video, they used a dicom file, while I am using a volume of tif files, so that may have something to do with the problem.</p>

---

## Post #23 by @lassoan (2020-12-27 18:24 UTC)

<p>Voxel values in your image is not in Hounsfield units. You need to adjust the lungs threshold range in the advanced section at the bottom.</p>
<p>I would strongly recommend to use DICOM files as inputs, as in consumer file formats, such as TIFF you lose lots of important metadata, such as image geometry (origin, spacing, axis directions) and even image intensity values may be corrupted (as it happens in your case, too).</p>

---

## Post #24 by @Sarang_Goel (2020-12-27 19:14 UTC)

<p>So even after fixing the HU values and the range, none of the results really changed. I do think my TIFF files may not be appropriate for all this. However, thank you all for your help and support!</p>

---

## Post #25 by @rbumm (2020-12-27 20:01 UTC)

<p>You could try to import the lung CT as DICOM files, not as individual TIFF files. Have a look at the CTChest demo dataset (DICOM) available in slicer. This is what you would need. Try to get your own CT data sets as they would be written on a CD (DICOM) from the radiology department. Import such a CD  into slicer. Then run Lung CT Analyzer.  If you need help please let us know.</p>

---

## Post #26 by @lassoan (2020-12-27 20:10 UTC)

<aside class="quote no-group" data-username="Sarang_Goel" data-post="24" data-topic="1494" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sarang_goel/48/9336_2.png" class="avatar"> Sarang_Goel:</div>
<blockquote>
<p>So even after fixing the HU values and the range, none of the results really changed. I do think my TIFF files may not be appropriate for all this. However, thank you all for your help and support!</p>
</blockquote>
</aside>
<p>How did you fix the HU values?<br>
Can you upload your scene saved as .mrb file somewhere so that we can have a look and tell what is the problem?</p>

---

## Post #27 by @Sarang_Goel (2020-12-27 20:24 UTC)

<p>I basically opened my image as a python array and print the min and max HU values, and set them on the slider. I really do think the tiff files won’t work, as they don’t even produce proper images of the other views (other than axial). However, this was a publically available dataset, and dicom files for covid19 arent available as they are a intrusion of the patient’s privacy (because of their metadata, etc.) I think it will be fine, but thank you all for your help!</p>

---

## Post #28 by @lassoan (2020-12-27 20:29 UTC)

<p>You need to set the lung intensity range on the sliders, not the intensity range of the entire volume. You can find out the desired range easily using Threshold effect in Segment Editor module. Anyway, you can use the COVID sample data set in Sample Data module.</p>

---

## Post #29 by @Sarang_Goel (2020-12-27 20:50 UTC)

<p>Ok i did this and it worked! Now i am just wondering how I can display another series of tiff files that I have (that outline the abnormalities) and overlay it with this 3d model.</p>

---

## Post #30 by @lassoan (2020-12-27 22:00 UTC)

<p>If the other series contains discrete label values then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-image-file-as-labelmap-volume">load it as a labelmap volume</a>. After loading, apply the same spacing correction as you did for the CT image.</p>
<p>If you work with medical images, especially 3D, then I would recommend to use nrrd file format, as it can store all essential metadata.</p>

---
