# Volume rendering shows a solid box

**Topic ID**: 4390
**Date**: 2018-10-14
**URL**: https://discourse.slicer.org/t/volume-rendering-shows-a-solid-box/4390

---

## Post #1 by @Gary (2018-10-14 05:53 UTC)

<p>Hi everyone,</p>
<p>As a beginner of this excellent software, Could anyone teach me how to get the surface of the border, which is the line between white and black region?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a746d203928ad5f6a68daa0c91fee903818b7b.png" data-download-href="/uploads/short-url/jdcmUIl4tRsR6pL4icuIfiS2Bl1.png?dl=1" title="NEWCapture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_690x427.png" alt="NEWCapture" data-base62-sha1="jdcmUIl4tRsR6pL4icuIfiS2Bl1" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86a746d203928ad5f6a68daa0c91fee903818b7b_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86a746d203928ad5f6a68daa0c91fee903818b7b.png 2x" data-dominant-color="63636F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">NEWCapture</span><span class="informations">1376×853 65.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jcfr (2018-10-14 09:01 UTC)

<p>Hi Gary,</p>
<p>Thanks for reaching out.</p>
<p>for sake of completness, here are the two other comment you posted in an identical post:</p>
<ul>
<li>
<p>I am trying to find the volume rendering of 2d pictures. After click the volume rendering button, it shows me a black solid box, which is not what I want.</p>
</li>
<li>
<p>The goal is to find the surface between black and white region of the picture. Could anyone give me some tips or instructions?</p>
</li>
</ul>
<p>Ps: Generally speaking we try to avoid asking the same question multiple time with a difference title, if needed, you should be able to edit the title of your post.</p>

---

## Post #3 by @jcfr (2018-10-14 09:08 UTC)

<p>You could use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor</a> to threshold your image and erase the wanted region, then you could use the <code>Segment Statistics</code> module to get information like the number of voxel. From there, you should be able to compute the surface using metatdata specific to your image (or “picture”)</p>
<div class="youtube-onebox lazy-video-container" data-video-id="fM_rxfDTRi0" data-video-title="Segment statistics - new module in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fM_rxfDTRi0" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fM_rxfDTRi0/maxresdefault.jpg" title="Segment statistics - new module in 3D Slicer" width="" height="">
  </a>
</div>
<aside class="quote quote-modified" data-post="1" data-topic="3252">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f0a364/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-statistics-volume-calculation/3252">Segment Statistics Volume Calculation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am new to Slicer and have a few questions about the Segment Statistics Module, particularly how it calculates volume. I am currently segmenting muscle groups, subcutaneous and intramuscular fat within a single slice from MR Images of the thigh. I have read that the Labelmap Statistics calculates volume as the product of the pixel spacing (mm3) and the pixel count. I am curious if Slicer is using the actual pixel dimensions given in the DICOM header combined with the slice thickness or n…
  </blockquote>
</aside>


---

## Post #4 by @Gary (2018-10-14 20:36 UTC)

<p>Sorry about posting same questions multiple times and Thanks for your reply.</p>
<p>The goal is to get the lines between white region and black region, and these lines will form a surface without the black and white region.</p>
<p>Here is what I did, I used the threshold to mark the white region, and use Islands to remove the white part. How could I remove the black region and obtain the boundary surface.</p>

---

## Post #5 by @lassoan (2018-10-16 19:04 UTC)

<p>The main problem is that all volume rendering presets assume that background is darker than the object that you would like to see. In your case, the object is dark and background box is bright, therefore you’ll only see a solid box.</p>
<p>The simplest is probably to invert your image by using SimpleFilters module: Filter = ShiftScaleImageFilter, Scale = -1.</p>
<p>If you don’t want to change your input image then you need to adjust volume rendering transfer functions to make bright values transparent. Something like this should work:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/864503757ba074e04fea6153177038d19d507b0b.png" alt="image" data-base62-sha1="j9NQbU2qIJgFcLRaAMrf74oSVPZ" width="565" height="454"></p>
<p>I’ve added an “inverted” volume rendering preset, CT-Air, which will be available in nightly builds that you download tomorrow or later. If you choose this preset and adjust “Shift” slider then dark structures should show up in the 3D view.</p>

---

## Post #6 by @Gary (2018-10-17 04:10 UTC)

<p>Thanks for your patient and reply Andras.I tried it on my computer, and it works now!!!</p>
<p>By the way, Do we have mesh in 3D slicer? Because I would like to collect data of every point on the surface.</p>
<p>Thanks for your help again, I do really appreciate it.</p>

---

## Post #7 by @lassoan (2018-10-17 04:40 UTC)

<aside class="quote no-group" data-username="Gary" data-post="6" data-topic="4390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>Do we have mesh in 3D slicer?</p>
</blockquote>
</aside>
<p>Yes. Post a new topic about what you would like to have exactly.</p>

---

## Post #8 by @lassoan (2018-10-17 04:41 UTC)

<aside class="quote no-group" data-username="Gary" data-post="6" data-topic="4390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>I tried it on my computer, and it works now!!!</p>
</blockquote>
</aside>
<p>Would you mind posting a screenshot of the end result?</p>

---

## Post #9 by @Gary (2018-10-17 04:09 UTC)

<p>Thanks for your patient and reply Andras.I tried it on my computer, it works now.<br>
By the way, Do we have mesh in 3D slicer? Because I would like to collect data of every point on the surface.</p>

---

## Post #10 by @lassoan (2018-10-18 01:01 UTC)

<aside class="quote no-group" data-username="Gary" data-post="9" data-topic="4390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/839c29/48.png" class="avatar"> Gary:</div>
<blockquote>
<p>Do we have mesh in 3D slicer?</p>
</blockquote>
</aside>
<p>Yes. Post a new topic about what you would like to have exactly.</p>

---

## Post #11 by @Gary (2018-10-20 01:21 UTC)

<p>Here is what I got from 3D Slicer.<br>
By the way, could I do surface mesh rather than volume mesh on this software, and export them as .stl file.<br>
Because I would like to use and analyze the surface mesh data.I<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69c51acaec39496c75a355ae7db870a54dc20e3a.png" data-download-href="/uploads/short-url/f5GqBLSOprZ37H5IQSiEAO0ZMM2.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c51acaec39496c75a355ae7db870a54dc20e3a_2_690x359.png" alt="Capture" data-base62-sha1="f5GqBLSOprZ37H5IQSiEAO0ZMM2" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c51acaec39496c75a355ae7db870a54dc20e3a_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c51acaec39496c75a355ae7db870a54dc20e3a_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69c51acaec39496c75a355ae7db870a54dc20e3a_2_1380x718.png 2x" data-dominant-color="908E91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1789×933 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @cpinter (2018-10-20 15:50 UTC)

<p>Yes, image segmentation is one of the major features that have seen a lot of improvements lately, see<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #13 by @Gary (2018-10-21 02:10 UTC)

<p>Thanks for your reply, could you give me a hint about how to do the surface mesh on 3D slicer?</p>

---

## Post #14 by @lassoan (2018-10-21 02:32 UTC)

<p>Once your segmentation is completed, the easiest way to export a surface mesh file is to use <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428"><em>Export to files</em> function</a> in Segment Editor module.</p>

---

## Post #15 by @Gary (2018-10-21 02:57 UTC)

<p>Thanks for your reply Andras,</p>
<p>After I change the brighter setting, which only show the black region rather than the white region, could I directly do the surface triangle mesh and export the files as .stl file?</p>
<p>If I can export the files as .stl format, will the data only contain the black region, or both white and black region?</p>

---

## Post #16 by @lassoan (2018-10-21 03:14 UTC)

<p>If you need only an STL file then you don’t need volume rendering. You can use Segment Editor module’s Threshold effect to create a segment, click <em>Show 3D</em> to verify how the mesh looks in 3D, and save as STL using <em>Export to files</em> feature.</p>

---

## Post #17 by @Gary (2018-10-27 18:04 UTC)

<p>Thanks for your help Andras, I finished the first step, your suggestions are really helpful!!</p>
<p>By the way, is there any way to remove the outside surface(connected), to get the volume as the file attached?</p>
<p>There should be two holes on the top of the heart, and I want to remove the surface parts that are connected to those two holes.</p>
<p>Andras Lasso <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> 于2018年10月20日周六 下午11:24写道：</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c9654292351a3fd9886efec9bbcc0859d5909c.png" data-download-href="/uploads/short-url/76qSOb5ofzWK5G1DgxL2e6qa0aw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c9654292351a3fd9886efec9bbcc0859d5909c_2_690x373.png" alt="image" data-base62-sha1="76qSOb5ofzWK5G1DgxL2e6qa0aw" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c9654292351a3fd9886efec9bbcc0859d5909c_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c9654292351a3fd9886efec9bbcc0859d5909c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c9654292351a3fd9886efec9bbcc0859d5909c.png 2x" data-dominant-color="E9CDCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×485 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
