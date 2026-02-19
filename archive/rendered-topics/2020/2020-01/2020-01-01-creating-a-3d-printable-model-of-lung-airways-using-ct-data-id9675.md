---
topic_id: 9675
title: "Creating A 3D Printable Model Of Lung Airways Using Ct Data"
date: 2020-01-01
url: https://discourse.slicer.org/t/9675
---

# Creating a 3d printable model of lung airways using CT data

**Topic ID**: 9675
**Date**: 2020-01-01
**URL**: https://discourse.slicer.org/t/creating-a-3d-printable-model-of-lung-airways-using-ct-data/9675

---

## Post #1 by @Shahid_Khan (2020-01-01 11:14 UTC)

<p>Hey. I am currently trying to make a 3d printable model of the human bronchial airway using CT data. If anyone can tell me the process for it?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2020-01-01 15:52 UTC)

<p>You may be able to segment airways using Threshold effect then cut off irrelevant parts using Scissors effect.</p>
<p>If a single global threshold cannot capture everything then you can put seeds inside airways and outside and use “Grow from seeds” effect to create a complete segmentation. The advantage of this approach is that you can add further seeds until you get a segmentation with sufficient details.</p>
<p>If you have trouble obtaining good segmentation then post screenshots highlighting the issues.</p>

---

## Post #3 by @Shahid_Khan (2020-01-02 04:27 UTC)

<p>Also, from where we can get detailed CT dicom data of lungs online? I need airways atleast till 7th generation (G7). Please help</p>

---

## Post #4 by @lassoan (2020-01-02 04:55 UTC)

<p><a href="https://www.cancerimagingarchive.net/">TCIA</a> contains lots of lung images (with ground truth segmentations available in <a href="http://medicaldecathlon.com/">Medical Decathlon</a>). However, it is always the best to ask data from your clinical collaborators - they can also validate quality of your processed data and results, keep your focus on the right clinical priorities, etc.</p>

---

## Post #5 by @Shahid_Khan (2020-01-02 05:47 UTC)

<p>We have sample CT chest data available in 3d slicer but it is not in DICOM format. I downloaded an extension named ‘Airway Segmentation CLI’ for segment airways using non-dicom data. I have some doubts on how to use that module. Please help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edf807fcda0fae1df613b9a42862c88444fe061b.png" data-download-href="/uploads/short-url/xXaz1suqqChgBOYoVSxKWNAI0bN.png?dl=1" title="Screenshot (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edf807fcda0fae1df613b9a42862c88444fe061b_2_690x431.png" alt="Screenshot (1)" data-base62-sha1="xXaz1suqqChgBOYoVSxKWNAI0bN" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edf807fcda0fae1df613b9a42862c88444fe061b_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edf807fcda0fae1df613b9a42862c88444fe061b_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edf807fcda0fae1df613b9a42862c88444fe061b_2_1380x862.png 2x" data-dominant-color="9F9FA6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (1)</span><span class="informations">1440×900 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Amine (2020-01-02 08:48 UTC)

<p>I recommend using the other airway segmentation module, not the CLI (it is easier), it will create a model from the label map as well</p>

---

## Post #7 by @Shahid_Khan (2020-01-02 09:31 UTC)

<p>When I am doing with that using  sample CT chest data available in 3-D slicer, this is what it is showing with other airway segmentation extension-<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531e3300100e659a24d52397155aa181f9254d6e.png" data-download-href="/uploads/short-url/bRikyA6xDxQZedMQlFuTugL8WEC.png?dl=1" title="Screenshot (120)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531e3300100e659a24d52397155aa181f9254d6e_2_690x387.png" alt="Screenshot (120)" data-base62-sha1="bRikyA6xDxQZedMQlFuTugL8WEC" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531e3300100e659a24d52397155aa181f9254d6e_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/531e3300100e659a24d52397155aa181f9254d6e_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/531e3300100e659a24d52397155aa181f9254d6e.png 2x" data-dominant-color="B2B2B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (120)</span><span class="informations">1366×768 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Amine (2020-01-02 12:12 UTC)

<p>It is a bug when using non dicom images as they don’t have certain tags, you can use <a href="https://github.com/amineaza/Slicer/blob/master/AirwaySegmentation.py" rel="nofollow noopener">this fix</a> to bypass it and make it work , simply replace the file located in Slicer_install_dir\lib\Slicer-4.10\qt-scripted-modules\AirwaySegmentation.py with that one after backing up the original.</p>

---

## Post #9 by @Shahid_Khan (2020-01-03 04:07 UTC)

<p>‘AirwaySegmentation.py’ is not showing in the folder you mentioned. I have downloaded the extension in the 3-D slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6883814b09cb579bede5a9311c77d510a5e2e73.png" data-download-href="/uploads/short-url/skio0cY5S8x9hwm9u9pTMapL2RZ.png?dl=1" title="Screenshot (122)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6883814b09cb579bede5a9311c77d510a5e2e73_2_690x387.png" alt="Screenshot (122)" data-base62-sha1="skio0cY5S8x9hwm9u9pTMapL2RZ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6883814b09cb579bede5a9311c77d510a5e2e73_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6883814b09cb579bede5a9311c77d510a5e2e73_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6883814b09cb579bede5a9311c77d510a5e2e73.png 2x" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (122)</span><span class="informations">1366×768 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @Sameer123 (2023-10-01 17:04 UTC)

<p>Sir have you created your lung airways model?</p>

---

## Post #11 by @rbumm (2023-10-02 13:26 UTC)

<p>You may want to try to use the “airway segmentation” in Lung CT Analyzer → Lung CT Segmenter module.</p>

---

## Post #12 by @Sameer123 (2023-10-02 17:47 UTC)

<p>Sir this module is not available in 3D slicer 5.3.0 version.</p>
<p>Thanks &amp; Regards:<br>
Sameer Verma,<br>
Ph.D. (Research Scholar),<br>
National Institute of Technology, Rourkela<br>
Odisha (India)-769008.<br>
Phone: +917042554240</p>

---

## Post #13 by @rbumm (2023-10-03 04:44 UTC)

<p>I can not test it now, but you could switch to 5.4.0 where it is available.</p>

---

## Post #14 by @Eserval (2023-10-03 13:35 UTC)

<p>Hello everyone,</p>
<p>I’d like to suggest a workflow that has proven effective for me:</p>
<ol>
<li>Use the Lung CT segmenter to quickly and precisely isolate the airway.</li>
<li>Remove all other segmentations such as PA, PV, Thoracic cavity, left lung, right lung, etc.</li>
<li>Create a new segmentation, which I refer to as “Tracheal Wall”, and duplicate the airway using logical operators.</li>
<li>Apply the margin effect to expand your Tracheal Wall by 0.5 cm.</li>
<li>Subtract the original airway segmentation from the Tracheal Wall using logical operations. This will result in a hollowed airway.</li>
<li>Export a STL file using the Segmentation module</li>
</ol>
<p>While you can opt to use the hollow effect directly, I’ve found that it doesn’t produce a satisfactory “air space” in the more distal bronchus.</p>
<p>I`ve been using it for some airway surgery planing</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e215455b76c1d3e5c373fee6528b951da942af0a.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e215455b76c1d3e5c373fee6528b951da942af0a.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e215455b76c1d3e5c373fee6528b951da942af0a.mp4</a>
    </video>
  </div><p></p>
<p>And also some realistic printed models for segmentectomy robotic surgery training</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10709da213a6cdd36da924d486403de86dc343db.jpeg" data-download-href="/uploads/short-url/2lqUTw0heJ7JXTb9thaaSkU9hP5.jpeg?dl=1" title="20230808_174120" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10709da213a6cdd36da924d486403de86dc343db_2_375x500.jpeg" alt="20230808_174120" data-base62-sha1="2lqUTw0heJ7JXTb9thaaSkU9hP5" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10709da213a6cdd36da924d486403de86dc343db_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10709da213a6cdd36da924d486403de86dc343db_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/10709da213a6cdd36da924d486403de86dc343db_2_750x1000.jpeg 2x" data-dominant-color="9F9A93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20230808_174120</span><span class="informations">1920×2560 671 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It works well for me… I hope this is helpful</p>

---

## Post #15 by @Sameer123 (2023-11-02 06:17 UTC)

<p>Sir I have downloaded the slicer 5.4.0 version but could not able to generate lung airways model upto 6th generation. Can you please help?</p>
<p>Thanks &amp; Regards:<br>
Sameer Verma,<br>
Ph.D. (Research Scholar),<br>
National Institute of Technology, Rourkela<br>
Odisha (India)-769008.<br>
Phone: +917042554240</p>

---

## Post #16 by @rbumm (2023-11-02 07:03 UTC)

<p>The details of airway segmentation very much depend on the starting material you are working with. Please use thin sliced CT (1 mm) for good results.</p>

---

## Post #17 by @Sameer123 (2023-11-02 07:10 UTC)

<p>Sir can you please provide some open source links to download CT scan dicom file for lungs airways (thin sliced).</p>
<p>Thanks &amp; Regards:<br>
Sameer Verma,<br>
Ph.D. (Research Scholar),<br>
National Institute of Technology, Rourkela<br>
Odisha (India)-769008.<br>
Phone: +917042554240</p>

---

## Post #18 by @rbumm (2023-11-02 11:25 UTC)

<p>We could probably share the lung023 volume from the Monailabel training dataset if that is ok <a class="mention" href="/u/diazandr3s">@diazandr3s</a> is there an official link to that data?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57841927e465affbc30080986456a7be9453f217.jpeg" data-download-href="/uploads/short-url/cucyFoDOyVK3Bs2ULkwll6dcSjR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57841927e465affbc30080986456a7be9453f217_2_690x253.jpeg" alt="image" data-base62-sha1="cucyFoDOyVK3Bs2ULkwll6dcSjR" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57841927e465affbc30080986456a7be9453f217_2_690x253.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57841927e465affbc30080986456a7be9453f217_2_1035x379.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57841927e465affbc30080986456a7be9453f217_2_1380x506.jpeg 2x" data-dominant-color="929297"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1888×694 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the meantime you can use:</p>
<p><a href="https://drive.google.com/drive/folders/1h_UQLL71yrXwqkUtNZ4a6NtvEobAuPyR?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1h_UQLL71yrXwqkUtNZ4a6NtvEobAuPyR?usp=sharing</a></p>

---

## Post #19 by @diazandr3s (2023-11-02 11:52 UTC)

<p>As <a class="mention" href="/u/lassoan">@lassoan</a> already posted <a href="https://discourse.slicer.org/t/creating-a-3d-printable-model-of-lung-airways-using-ct-data/9675/4">here</a>, either TCIA or <a href="http://medicaldecathlon.com/" rel="noopener nofollow ugc">Medical Segmentation</a> Decathlon (MSD) datasets are available to download.</p>
<p>MSD datasets are not in DICOM format though.</p>
<p>For lung airway segmentation, you could use <a href="https://github.com/Project-MONAI/MONAILabel/tree/main" rel="noopener nofollow ugc">MONAI Label</a> to create your AI model.</p>

---

## Post #20 by @Sameer123 (2023-11-04 06:47 UTC)

<p>Thank you so much sir for providing the google drive link it worked for me in generating airways model.<br>
Can you please tell how I can import this 3D slicer file into the Ansys fluent software for the computational simulation purpose.</p>

---

## Post #21 by @rbumm (2023-11-04 07:29 UTC)

<p>I personally have no experience, but here is what ChatGPT has to say:<br>
I’m glad to hear that the Google Drive link was helpful for your airways model project.</p>
<p>To import a 3D model from Slicer into ANSYS Fluent for computational fluid dynamics (CFD) simulations, you typically need to go through several steps to ensure the model is suitable for CFD analysis. Here’s a general process:</p>
<ol>
<li>
<p><strong>Export from 3D Slicer:</strong></p>
<ul>
<li>Make sure your model is properly segmented and converted into a 3D surface model in Slicer.</li>
<li>Export the geometry from 3D Slicer in a format compatible with ANSYS. The commonly used formats are STL (stereolithography) or VRML (Virtual Reality Modeling Language).</li>
</ul>
</li>
<li>
<p><strong>Preparation of the Geometry:</strong></p>
<ul>
<li>Once you have your STL or VRML file, you might need to import it into a CAD software like ANSYS SpaceClaim or DesignModeler to clean and prepare the geometry.</li>
<li>Operations you might need to perform include removing small features that are not relevant to the flow, repairing any gaps or overlaps in the surface mesh, and ensuring that the model is watertight.</li>
</ul>
</li>
<li>
<p><strong>Mesh Generation:</strong></p>
<ul>
<li>After preparing your geometry, the next step is mesh generation, which can also be done within ANSYS workbench using tools like ANSYS Meshing.</li>
<li>Ensure that your mesh is fine enough to capture the important features of the flow, especially in areas where there are expected to be high gradients (like near walls).</li>
<li>Check the quality of your mesh using criteria such as skewness, aspect ratio, and orthogonality.</li>
</ul>
</li>
<li>
<p><strong>Setup in ANSYS Fluent:</strong></p>
<ul>
<li>Once your mesh is ready, import it into ANSYS Fluent.</li>
<li>Set up the boundary conditions, material properties, and physical models (laminar or turbulent flow, heat transfer, etc.) according to your simulation needs.</li>
<li>Initialize the flow field and start your simulation with an appropriate time step and convergence criteria.</li>
</ul>
</li>
<li>
<p><strong>Simulation and Post-processing:</strong></p>
<ul>
<li>Monitor the residuals and other important parameters to ensure the convergence of your simulation.</li>
<li>After the simulation is complete, use Fluent’s post-processing tools to analyze the results, visualize flow patterns, and extract relevant data.</li>
</ul>
</li>
</ol>
<p>Remember, CFD simulations are complex and require careful setup and validation. Ensure that your model boundaries reflect the physical system accurately and that you’ve considered the necessary physical phenomena in your simulation.</p>
<p>If you run into any issues specific to the file formats or steps within ANSYS tools, it may be helpful to consult ANSYS documentation, tutorials, or reach out to the ANSYS user community for advice tailored to the exact version of the software you’re using.</p>

---

## Post #22 by @Sameer123 (2023-11-04 12:30 UTC)

<p>Thankyou sir for your response!!!</p>

---

## Post #23 by @D_Dand (2024-02-07 16:02 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="21" data-topic="9675">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>ANSYS SpaceClaim</p>
</blockquote>
</aside>
<p>Thank you very much for the workflow suggestion.<br>
For the step 2. For preparation of the Geometry, can STL files be imported into CAD software like Ansys spaceclaim? I use Solidworks and it seems it does not give you a good detailed model. Besides, would you suggest using Solidworks or Ansys spaceclaim?</p>

---

## Post #24 by @rbumm (2024-02-09 14:25 UTC)

<p>I have no personal experience with Ansys SpaceClaim or Solidworks -</p>
<p>Maybe <a href="https://discourse.slicer.org/t/is-there-a-guide-for-3d-printing-anatomical-structures/34001/2">this</a> helps …</p>

---

## Post #25 by @D_Dand (2024-02-12 22:56 UTC)

<p>Thank you very much! You are very responsive. I am curious if you ever try to export file from Slicer and then import to and CAD software. So far, I see Slicer is just able to convert file into meshing file (STL etc.) but CAD.</p>

---

## Post #26 by @rbumm (2024-02-15 12:08 UTC)

<p>No, unfortunately I have not used CAD software with Slicer or 3D printing yet - but have imported STL into Meshmixer (free for Windows).</p>

---
