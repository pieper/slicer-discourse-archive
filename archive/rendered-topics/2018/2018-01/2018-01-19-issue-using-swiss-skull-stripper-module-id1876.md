# Issue using Swiss Skull Stripper Module

**Topic ID**: 1876
**Date**: 2018-01-19
**URL**: https://discourse.slicer.org/t/issue-using-swiss-skull-stripper-module/1876

---

## Post #1 by @dlevitas (2018-01-19 22:11 UTC)

<p>Hello,</p>
<p>I just started trying out 3D Slicer: currently using version 4.9.0</p>
<p>I thought I entered the correct information into the GUI, but when I went to run it I received the following error:</p>
<pre><code>Swiss Skull Stripper standard error:

Failed to read input atlas label volume.

itk::ImageFileReaderException (0x104a50388)
Location: "unknown" 
File: /Users/kitware/Dashboards/Nightly/Slicer-0-
build/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx
Line: 143
Description:  Could not create IO object for reading file 
/var/folders/0c/l9qjt85j7ns3j3lctwhs82wc1kd6y7/T/Slicer-dlevitas/CACHI_vtkMRMLLabelMapVolumeNodeB.nrrd

The file doesn't exist. 

Filename = /var/folders/0c/l9qjt85j7ns3j3lctwhs82wc1kd6y7/T/Slicer-
dlevitas/CACHI_vtkMRMLLabelMapVolumeNodeB.nrrd
</code></pre>
<p>I already converted my Dicoms using a different program, and my atlas and input files are in NIFTI format; however, I’m unsure if things are failing because the files aren’t in .nrrd format.</p>
<p>Does anyone have any suggestions regarding this issue? Thanks for the help.</p>
<p>Dan</p>

---

## Post #2 by @lassoan (2018-01-19 22:22 UTC)

<p>Try to change temporary folder in Application Settings to a simpler one (when your username contain non-ascii characters then the default temporary folder location may not work).</p>
<p>Also, right now we are changing many things in the nightly builds, so for a couple of weeks it may be better to use the stable version (4.8).</p>

---

## Post #3 by @dlevitas (2018-01-22 19:26 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. I installed the stable version for Mac OS X (ver 4.8.1), and changed the temporary folder, but I continue to get a similar error:</p>
<pre><code>Swiss Skull Stripper standard error:

Failed to read input atlas label volume.

itk::ImageFileReaderException (0x105ae8938)
Location: "unknown" 
File: /Users/kitware/Dashboards/Package/Slicer-481-
package/ITKv4/Modules/IO/ImageBase/include/itkImageFileReader.hxx
Line: 143
Description:  Could not create IO object for reading file 
/Users/dlevitas/Desktop/3Dslicer/CFJGF_vtkMRMLLabelMapVolumeNodeB.nrrd
The file doesn't exist. 
Filename = /Users/dlevitas/Desktop/3Dslicer/CFJGF_vtkMRMLLabelMapVolumeNodeB.nrrd
</code></pre>
<p>It seems that it can’t find the CFJGF_vtkMRMLLabelMapVolumeNodeB.nrrd file, but I’m unsure where this file would be, or how to perform the skull strip without it.</p>

---

## Post #4 by @lassoan (2018-01-22 20:04 UTC)

<p>For “Atlas mask volume” you have to select atlasMask volume. Note that the volume only shows up there if it is loaded as “labelmap”. Unfortunately, atlasMask.mha file is not loaded as labelmap by default but in the <code>Add data</code> window you have to check <code>Show options</code> and then check <code>LabelMap</code>.</p>
<p><a class="mention" href="/u/lorensen">@Lorensen</a> Could you rename the atlas mask file to <code>atlasImage-label.mha</code>? If a volume’s file name ends with <code>-label</code> then it is loaded as <code>LabelMap</code> by default and it would make it much easier to use the module. Or, even better, extensions can register their own data sets in Sample Data module, so the user could easily go to Sample Data module and download the mask by a single click. See how it is done for Sequences module: <a href="https://github.com/SlicerRt/Sequences/tree/master/SequenceSampleData">https://github.com/SlicerRt/Sequences/tree/master/SequenceSampleData</a></p>

---

## Post #5 by @dlevitas (2018-01-22 21:41 UTC)

<p>I was having trouble navigating the GUI, however, I managed to solve my problem by using this in the terminal command line:</p>
<pre><code>/Applications/Slicer.app/Contents/Extensions-26813/SwissSkullStripper/lib/Slicer-4.8/cli-modules/SwissSkullStripper --atlasMRI atlas_with_skull.nii.gz --atlasMask atlas_no_skull_mask.nii.gz input_data.nii.gz output_brain_no_skull.nii.gz output_mask_no_skull.nii.gz</code></pre>

---

## Post #6 by @lassoan (2018-01-22 22:59 UTC)

<p>You can also use default atlas by not specifying any atlas image or mask inputs at all.</p>

---

## Post #7 by @Saima (2020-01-24 06:50 UTC)

<p>Hi andras,<br>
I have used skull stripper multiple times. it does do good with sample data. but not with other data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d90561cb75fae80f8a7f4d7c1933610022255d1a.png" data-download-href="/uploads/short-url/uXR8NOLYP4QuWUFmkuCqO6h29pE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d90561cb75fae80f8a7f4d7c1933610022255d1a_2_360x500.png" alt="image" data-base62-sha1="uXR8NOLYP4QuWUFmkuCqO6h29pE" width="360" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d90561cb75fae80f8a7f4d7c1933610022255d1a_2_360x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d90561cb75fae80f8a7f4d7c1933610022255d1a_2_540x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d90561cb75fae80f8a7f4d7c1933610022255d1a.png 2x" data-dominant-color="395269"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">584×809 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I fix the above problem. it misses the brain portion.</p>
<p>Thank you<br>
Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2020-01-24 10:03 UTC)

<p>If your images are too different from the default atlas then you can use one of your own typical images and corresponding segmentation as input.</p>

---

## Post #10 by @jshen (2022-01-14 01:14 UTC)

<p>Hi Andras,</p>
<p>I am having the same issue as Saima and I am trying to create a atlas using my own typical images as you said in your last reply. I am a bit stuck, do you have any resources or tutorials that can help with explain this process?</p>
<p>Regards,<br>
James</p>

---

## Post #11 by @lassoan (2022-01-15 21:22 UTC)

<p>The atlas is simply a single image and corresponding labelmap. You can choose these images in the atlas section and skull stripping should just work. If not then describe in detail what did you do, what did you expect to happen, and what happened instead.</p>

---

## Post #12 by @jshen (2022-02-06 03:03 UTC)

<p>Hi Andras,</p>
<p>I tried two methods: 1) I used my own T1 MRI DICOM image set and the default atlas and mask image files obtained from the Swedish Skull Stripper module documentation page. I ran into problems as this seemed to have stripped away a layer of brain along with the skull. I expected that the Swedish Skull Stripper module would leave the full brain intact while stripping away the skull and dura. See attached screenshots.</p>
<ol start="2">
<li>I used a patient mask I created in 3D slicer using the Segment Editor module using my own MRI image set. The same result occurred, the output was too small and the module eroded too much of the brain (see attached screenshot). I tried to make the input mask bigger so I used the entire skull as a mask, unsuccessfully.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4518997ae7cdb41b97d0ab1982bf6bb3ca6dd82f.jpeg" data-download-href="/uploads/short-url/9RfEhv92o05IzO4NjCYNbZTlbYj.jpeg?dl=1" title="3DSlicer_SwedishSkullStripper_BeforeRun.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4518997ae7cdb41b97d0ab1982bf6bb3ca6dd82f_2_690x374.jpeg" alt="3DSlicer_SwedishSkullStripper_BeforeRun.PNG" data-base62-sha1="9RfEhv92o05IzO4NjCYNbZTlbYj" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4518997ae7cdb41b97d0ab1982bf6bb3ca6dd82f_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4518997ae7cdb41b97d0ab1982bf6bb3ca6dd82f_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4518997ae7cdb41b97d0ab1982bf6bb3ca6dd82f_2_1380x748.jpeg 2x" data-dominant-color="A8ACBA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_SwedishSkullStripper_BeforeRun.PNG</span><span class="informations">1921×1043 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Before run, with default atlas mask</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1278c5ffb22ec53077419d9713798252dfbbade6.png" data-download-href="/uploads/short-url/2DplILjA60PqGf74f34f2yNh2LQ.png?dl=1" title="3DSlicer_SwedishSkullStripper_AfterRun1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278c5ffb22ec53077419d9713798252dfbbade6_2_690x373.png" alt="3DSlicer_SwedishSkullStripper_AfterRun1" data-base62-sha1="2DplILjA60PqGf74f34f2yNh2LQ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278c5ffb22ec53077419d9713798252dfbbade6_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278c5ffb22ec53077419d9713798252dfbbade6_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278c5ffb22ec53077419d9713798252dfbbade6_2_1380x746.png 2x" data-dominant-color="A4A5B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_SwedishSkullStripper_AfterRun1</span><span class="informations">1921×1041 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After applying Swedish Skull Stripper with default mask, some areas of brain stripped</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9303fa31cc9b70d951b2d55e7bd48428b0021ab0.jpeg" data-download-href="/uploads/short-url/kYyHZqQeavYOECPLGazdbKdQHhS.jpeg?dl=1" title="3DSlicer_SwedishSkullStripper_AfterRun2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9303fa31cc9b70d951b2d55e7bd48428b0021ab0_2_690x373.jpeg" alt="3DSlicer_SwedishSkullStripper_AfterRun2.PNG" data-base62-sha1="kYyHZqQeavYOECPLGazdbKdQHhS" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9303fa31cc9b70d951b2d55e7bd48428b0021ab0_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9303fa31cc9b70d951b2d55e7bd48428b0021ab0_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9303fa31cc9b70d951b2d55e7bd48428b0021ab0_2_1380x746.jpeg 2x" data-dominant-color="A0A7BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_SwedishSkullStripper_AfterRun2.PNG</span><span class="informations">1923×1042 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
After applying Swedish Skull Stripper with default mask, overlaid with patient volume input</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53656b21b303ef28a2f8ee41d7082c125bf8c93d.png" data-download-href="/uploads/short-url/bTKUVlDpL7WV2N60HBS28SUn3FX.png?dl=1" title="3DSlicer_SwedishSkullStripper_UsingCustomMask" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53656b21b303ef28a2f8ee41d7082c125bf8c93d_2_690x374.png" alt="3DSlicer_SwedishSkullStripper_UsingCustomMask" data-base62-sha1="bTKUVlDpL7WV2N60HBS28SUn3FX" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53656b21b303ef28a2f8ee41d7082c125bf8c93d_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53656b21b303ef28a2f8ee41d7082c125bf8c93d_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53656b21b303ef28a2f8ee41d7082c125bf8c93d_2_1380x748.png 2x" data-dominant-color="969BA3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3DSlicer_SwedishSkullStripper_UsingCustomMask</span><span class="informations">1921×1042 503 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Using Swedish Skull Stripper with a custom mask, output overlaid with patient volume input</p>

---

## Post #13 by @lassoan (2022-02-06 04:00 UTC)

<p>Could you share the data sets that you used for these tests so that we can see if something special about this data that makes it a difficult problem or there is a software bug?</p>

---

## Post #14 by @jshen (2022-02-08 00:02 UTC)

<p>Hi Andras,</p>
<p>Sure! I have the files linked here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing">
  <header class="source">

      <a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/ServiceLogin?service=wise&amp;passive=1209600&amp;continue=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing&amp;followup=https:%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1nl1k6z7f_joCk96DIR4s--dCKAc4XLlj?usp%3Dsharing" target="_blank" rel="noopener nofollow ugc">Meet Google Drive – One place for all your files</a></h3>

  <p>Google Drive is a free way to keep your files backed up and easy to reach from any phone, tablet, or computer. Start with 15GB of Google storage – free.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regards,<br>
James</p>

---

## Post #15 by @lassoan (2022-02-10 04:53 UTC)

<p>I’ve checked the image and it seems that the problem is that the default atlas image of SwissSkullStripper is just too different from your image.</p>
<p>I’ve created a brain segmentation from the HNCMA atlas and it worked much better - you can download the files from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHx-5S8h8e_6RZVkh1HA?e=8q1F4a">here</a> and select them as <code>atlas volume</code> and <code>atlas mask volume</code> in the Atlas section.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edf8d27fc93f8ef1535a3c2517ee2c6ed4f1bc92.jpeg" data-download-href="/uploads/short-url/xXcg6q6gGbJdSaGtc2oDdaVJuqC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edf8d27fc93f8ef1535a3c2517ee2c6ed4f1bc92_2_690x420.jpeg" alt="image" data-base62-sha1="xXcg6q6gGbJdSaGtc2oDdaVJuqC" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edf8d27fc93f8ef1535a3c2517ee2c6ed4f1bc92_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edf8d27fc93f8ef1535a3c2517ee2c6ed4f1bc92_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edf8d27fc93f8ef1535a3c2517ee2c6ed4f1bc92_2_1380x840.jpeg 2x" data-dominant-color="9EA0A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1169 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If the result is not still not good enough then you can either fix it up manually in the Segment Editor module or use an atlas that looks more similar to your image.</p>

---
