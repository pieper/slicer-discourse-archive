# Gen Registration (Brains) fails despite overlap of series

**Topic ID**: 2644
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/gen-registration-brains-fails-despite-overlap-of-series/2644

---

## Post #1 by @alex (2018-04-20 11:25 UTC)

<p>Dear Slicer community,</p>
<p>My apologies for posting this again as new Topic. I had initially added that to a discussion from July 2017 initiated by Rewati K but then realized that this discussion was marked as solved… by no means is my intention to spam this forum.</p>
<p>I am following tutorial: <a href="https://www.slicer.org/w/images/b/ba/NRR-CTgLiverAblation.pdf" rel="nofollow noopener">https://www.slicer.org/w/images/b/ba/NRR-CTgLiverAblation.pdf</a><br>
to register T1 and T2 liver MRI images. I created mask for both sequences, and the sequences definitively overlap in the 3D space! however, I am getting the same error message as Rewati K posted on July 2017</p>
<p>General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>itk::ExceptionObject (0xfb3160)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Nightly/Slicer-0-build/ITKv4/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx<br>
Line: 205<br>
Description: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0xb3c290): Joint PDF summed to zero<br>
General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>I tried multiple initial splines and I am truly getting desperate. I’m using Slicer 4.8 on Ubuntu 16.04. Any help/suggestion is much appreciated. I uploaded the NRRD files and a screenshot from the GUI interface to the following folder: <a href="https://www.dropbox.com/sh/ly2rbeyoxe3ja07/AAC1UKMLWrZm_vOEUXAK0dDsa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/ly2rbeyoxe3ja07/AAC1UKMLWrZm_vOEUXAK0dDsa?dl=0</a></p>
<p>Thank you very much!<br>
Alex</p>

---

## Post #2 by @alex (2018-04-20 03:26 UTC)

<p>Dear Slicer community,</p>
<p>I am following tutorial: <a href="https://www.slicer.org/w/images/b/ba/NRR-CTgLiverAblation.pdf" rel="nofollow noopener">https://www.slicer.org/w/images/b/ba/NRR-CTgLiverAblation.pdf</a><br>
to register T1 and T2 liver MRI images. I created mask for both sequences, and the sequences definitively overlap in the 3D space! however,  I am getting the same error message as Rewati</p>
<p>General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>itk::ExceptionObject (0xfb3160)<br>
Location: “unknown”<br>
File: /home/kitware/Dashboards/Nightly/Slicer-0-build/ITKv4/Modules/Registration/Metricsv4/include/itkMattesMutualInformationImageToImageMetricv4.hxx<br>
Line: 205<br>
Description: itk::ERROR: MattesMutualInformationImageToImageMetricv4(0xb3c290): Joint PDF summed to zero<br>
General Registration (BRAINS) standard error:</p>
<p>ExceptionObject caught !</p>
<p>I tried multiple initial splines and I am truly getting desperate. I’m using Slicer 4.8 on Ubuntu 16.04. Any help/suggestion is much appreciated. I uploaded the NRRD files and a screenshot from the GUI interface to the following folder:  <a href="https://www.dropbox.com/sh/ly2rbeyoxe3ja07/AAC1UKMLWrZm_vOEUXAK0dDsa?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/ly2rbeyoxe3ja07/AAC1UKMLWrZm_vOEUXAK0dDsa?dl=0</a></p>
<p>Thank you very much!<br>
Alex</p>

---

## Post #3 by @ihnorton (2018-04-20 13:56 UTC)

<p>You may need to initialize with a manual transform. You could also try the Slicer Elastix extension.</p>

---

## Post #4 by @fedorov (2018-04-20 22:52 UTC)

<p><a class="mention" href="/u/alex">@alex</a> looking at the screenshot you shared, it is quite difficult to troubleshoot a failure when you have multiple registration phases selected. If your initial transform is not good, all subsequent phases will fold.</p>
<p>I suggest you give it a try as follows:</p>
<ol>
<li>uncheck all registration phases, keep center of ROI initializer, and see if you get any meaningful result</li>
<li>if result in 1 is reasonable, try selecting Rigid phase</li>
<li>if result in 2 is not reasonable, try manual initial alignment using Transforms module, and use manual initialization transform instead of the automatic initializer, as suggested by Isaiah.</li>
</ol>

---

## Post #5 by @lassoan (2018-04-21 14:36 UTC)

<p>I’ve tried with both BRAINS and Elastix registrations and due to some reasons, neither of them worked very well.</p>
<p>I could only make BRAINS give meaningful output by rescaling the voxels values. In the attached files, they voxels were floating-point numbers in a range of about [-1, 10]; multiplying the values by 100 and converting to <code>short</code> type allowed the registration to complete, but the result was not great. When I enabled masking, I always got the dreaded <code>Joint PDF summed to zero</code> error. I thought it could be do to the low number of samples, but even increasing that did not help.</p>
<p>Elastix gave some result, but it did not aligned the liver well either and masks did not make a difference.</p>
<p>Maybe with further parameter tuning you could make one of these image-based registration modules work, but the images may not be similar enough so that you could register them properly.</p>
<p>If you can afford manual segmentation of the organ of interest (using Segment Editor), then you can register them using Segment Registration extension. Or, if you can identify enough corresponding anatomical landmarks in the images then you can use SlicerIGT extension’s Fiducial registration wizard module to perform landmark-based registration.</p>

---

## Post #6 by @alex (2018-04-21 17:29 UTC)

<p>Thank you all for helpful responses.<br>
Please allow a few follow-up questions – my apologies upfront if they are grounded on my lack of experience.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a>:</p>
<ul>
<li>Step 1 worked. Subsequently rigid failed but it worked with affine and b-spline. Why is that? Granted the masks overlap, so probably should be close to Eigenmatrix or is the failure b/c there is overlap of mask <span class="hashtag">#1</span> over <span class="hashtag">#2</span> on several sides?</li>
<li>Re transform initialization settings: if I chose initial transform matrix (created in transform module), I notice difference between mode set to "none’ versus “useCenterOfRoOIAlign”. I assume in “none” it is applied to the entire volume and in “use…” only to mask regions?? I don’t find clear documentation on it and wanted to clarify.</li>
</ul>
<p><a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<ul>
<li>These are MRI images that were NTK4Bias corrected followed by normalization. I thought that this would be the appropriate order prior to registering? Why did rescaling help for BRAINS to work?</li>
<li>I like really like your Elastix module. I tried different settings and got it to work but - however the results were not so good. On the Elastix wiki I found some example for liver MRI. Do these dataset examples correspond to “Inputs/Present” settings in the Slicer interface? <a href="http://elastix.bigr.nl/wiki/index.php/Par0047" rel="nofollow noopener">http://elastix.bigr.nl/wiki/index.php/Par0047</a>
</li>
</ul>

---

## Post #7 by @lassoan (2018-04-21 19:25 UTC)

<aside class="quote no-group" data-username="alex" data-post="6" data-topic="2644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar"> alex:</div>
<blockquote>
<p>Do these dataset examples correspond to “Inputs/Present” settings in the Slicer interface?</p>
</blockquote>
</aside>
<p>Yes. Note that you can edit these presets to better suite your needs. Par0047 is for 4D data sets, so I don’t think it is applicable as is to a simple 3D volume.</p>

---

## Post #8 by @alex (2018-04-21 22:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for your quick response. Yes, I understand that Par0047 is for 4D data. I actually have  a lot of these 4D series (dynamic pre and post contrast images) and would really like to try it.  I don’t see Par0047 prepopulated in the default Elastix module. Is there a way to load it in?</p>

---

## Post #9 by @lassoan (2018-04-21 22:51 UTC)

<p>You can add presets by editing the text and xml files in the presets folder. You can find the location in advanced section.</p>

---

## Post #10 by @fedorov (2018-04-22 17:32 UTC)

<aside class="quote no-group" data-username="alex" data-post="6" data-topic="2644">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/db5fbb/48.png" class="avatar"> alex:</div>
<blockquote>
<p>I assume in “none” it is applied to the entire volume and in “use…” only to mask regions??</p>
</blockquote>
</aside>
<p>“None” means you need to provide initial transform. “useCenterOfRoOIAlign” will derive the initial transform automatically by first aligning the centroids of the masks you provide, and next doing some sparse search of the optimal similarity measure by rotating one of the images.</p>

---

## Post #11 by @lassoan (2018-04-22 22:53 UTC)

<p>I’ve checked the scene that <a class="mention" href="/u/alex">@alex</a> attached and the initial alignment looked good. The images seem to be just too different, so registration is difficult and it requires careful parameter tuning.</p>

---

## Post #12 by @alex (2018-04-23 02:33 UTC)

<p>All, thank you very much! Your input has been tremendously helpful. I refined the masks and now it is actually working well. Thanks again!</p>

---
