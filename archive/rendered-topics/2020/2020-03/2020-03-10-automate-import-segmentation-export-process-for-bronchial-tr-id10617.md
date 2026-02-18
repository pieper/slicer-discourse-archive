# Automate import-segmentation-export process for bronchial tree

**Topic ID**: 10617
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/automate-import-segmentation-export-process-for-bronchial-tree/10617

---

## Post #1 by @Fluvio_Lobo (2020-03-10 15:14 UTC)

<p>Hello,</p>
<p>I have used 3DSlicer for a few years now, but have not attempted to automate any processes.</p>
<p>My group is interested in segmenting air-filled structures and cavities, which ends-up becoming a very simple and consistent task with thresholding.</p>
<p>Therefore, we would like to know if there is a way of;</p>
<ul>
<li>Automating the tasks of: (1) importing DICOM, (2) segmenting using threshold, (3) exporting .STL</li>
</ul>
<p>and,</p>
<ul>
<li>If said automated operation can be triggered externally via command line, perhaps execute a script that tells slicer to perform these operations?</li>
</ul>

---

## Post #2 by @lassoan (2020-03-10 15:16 UTC)

<p>What is your current workflow? What cavities you segment? Can you post a few screenshots?</p>
<p>What do you do with the exported STL? Have you considered doing automating further processing steps (identification of structures, measuring volumes, etc.) in Slicer?</p>

---

## Post #3 by @Fluvio_Lobo (2020-03-11 14:41 UTC)

<p>Andras,</p>
<p>Thank you for the response!</p>
<p>First of all, our “semi-automated workflow” uses Slicer and <a href="https://www.sidefx.com/" rel="noopener nofollow ugc">Houdini</a>. All of the segmentation and clean-up is done in Slicer, the rest is done in Houdini.</p>
<ol>
<li>
<p>Import CT [Slicer]</p>
</li>
<li>
<p>Create Region of Interest [Slicer]<br>
2.1. This is one of the parts the we are most interesting in automating<br>
2.2. We are creating this region of interest to segment most of the airway without the external components (air outside of the model), but also most of the trachea and lungs<br>
2.3. The model on these pictures is not representative of an amazing result, as some of the external air and lungs are still present – I just wanted you to see what I mean</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f908203c78567e9f43a2141bbdea3ee42172f27a.png" data-download-href="/uploads/short-url/zx2iACRJWOv235GqEYR6AFRkxGW.png?dl=1" title="roi" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f908203c78567e9f43a2141bbdea3ee42172f27a_2_690x373.png" alt="roi" data-base62-sha1="zx2iACRJWOv235GqEYR6AFRkxGW" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f908203c78567e9f43a2141bbdea3ee42172f27a_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f908203c78567e9f43a2141bbdea3ee42172f27a_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f908203c78567e9f43a2141bbdea3ee42172f27a_2_1380x746.png 2x" data-dominant-color="85868D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">roi</span><span class="informations">1920×1040 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>
<p>Crop Volume using ROI [Slicer]<br>
3.1. Crop volume using ROI and generate an isotropic volume (pixelwise)</p>
</li>
<li>
<p>Segment Airway [Slicer]<br>
4.1. Segment airway using threshold tool and defaults for airway under CT</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fceb6cd76a941f4a04acaabf756af113117f6c46.png" data-download-href="/uploads/short-url/A5qIyrc5vt9sLIuV6zieSEJbSyW.png?dl=1" title="segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fceb6cd76a941f4a04acaabf756af113117f6c46_2_690x373.png" alt="segment" data-base62-sha1="A5qIyrc5vt9sLIuV6zieSEJbSyW" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fceb6cd76a941f4a04acaabf756af113117f6c46_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fceb6cd76a941f4a04acaabf756af113117f6c46_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fceb6cd76a941f4a04acaabf756af113117f6c46_2_1380x746.png 2x" data-dominant-color="7B7C81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment</span><span class="informations">1920×1040 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li>Export as STL</li>
</ol>
<p>------------------------------------------- The next steps are done in Houdini -------------------------------------------</p>
<p>It is a little harder to explain the following steps without using the Houdini terminology but, in a nutshell;</p>
<ol>
<li>Import .STL</li>
<li>Create a point-cloud from the volume enclosed by the .STL</li>
<li>Select a starting and end point (mouth, epiglottis)</li>
<li>Automatically determine a path between the starting and end point</li>
<li>Extrude a part that follows said path</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be1aca4a59783b371f02e6472b58d217178beb81.jpeg" data-download-href="/uploads/short-url/r7K7gcpCajBeuun8L1zx5gCVQul.jpeg?dl=1" title="airway_path_side_2.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be1aca4a59783b371f02e6472b58d217178beb81_2_690x434.jpeg" alt="airway_path_side_2.PNG" data-base62-sha1="r7K7gcpCajBeuun8L1zx5gCVQul" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be1aca4a59783b371f02e6472b58d217178beb81_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be1aca4a59783b371f02e6472b58d217178beb81.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be1aca4a59783b371f02e6472b58d217178beb81.jpeg 2x" data-dominant-color="9C9C9C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">airway_path_side_2.PNG</span><span class="informations">727×458 44.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>--------------------------------------------------- What are we looking for? --------------------------------------------------</p>
<ol>
<li>How much of Slicer process can be automated? Scripted?</li>
<li>Can this process be executed through a terminal?</li>
</ol>
<p>Alternatively,</p>
<ol>
<li>How much of what is done in Houdini can be done in Slicer? (open to this)</li>
<li>Could it be scripted, automated, perhaps made into a plugin? (very open to this)</li>
</ol>
<p>Sorry for the wait and thank you for your help!<br>
P.S. I could only add 3 images because I am a N00B</p>

---

## Post #4 by @lassoan (2020-03-11 16:16 UTC)

<p>All the tools that are needed to fully automate this processing workflow are already available in Slicer.</p>
<ul>
<li>Extract airways using Chest Imaging Platform or Segment Editor tools (such as Fast Marching or Local thresholding)</li>
</ul>
<div class="lazyYT" data-youtube-id="tJMGe3FMTk0" data-youtube-title="Airway segmentation from CT in 1 minute using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<ul>
<li>Extract bronchial tree centerline using VMTK extension’s “Centerline extraction” module</li>
<li>Use this centerline model to get shortest path between two points by using the markups curve module (Curve settings / Curve type -&gt; Shortest distance on surface; Model node -&gt; CenterlinComputationModel)</li>
<li>Use a vtkTubeFilter to create a tube model around the selected curve</li>
</ul>
<p>See a short video of the how shortest path is found in real-time in the bronchial tree:</p>
<div class="lazyYT" data-youtube-id="UpfDP6ejCjg" data-youtube-title="Finding shortest path between two points in the bronchial tree" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #5 by @Fluvio_Lobo (2020-03-12 14:21 UTC)

<p>Andras,</p>
<p>Thank you!<br>
We will look over this and see if we have any additional questions</p>

---
