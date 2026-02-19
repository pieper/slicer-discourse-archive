---
topic_id: 960
title: "Bone Segmentation To Create 3D Printable Stl"
date: 2017-08-28
url: https://discourse.slicer.org/t/960
---

# Bone segmentation to create 3D-printable STL

**Topic ID**: 960
**Date**: 2017-08-28
**URL**: https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960

---

## Post #1 by @Hanaana (2017-08-28 13:43 UTC)

<p>Hello everyone,</p>
<p>I need your support</p>
<p>I got this stl as you can see it doesnt look good for further analysis. Can<br>
you please tell me how i can   modify my stl by modifing my NIfTI data. As<br>
i dont know how to edit my stl data after generating it. Any ideas and<br>
method will be with a great help.</p>
<p>Thanks in advance</p>
<p>​<br>
1.3.12.2.1107.5.2.19.45406.20141202103253422220…<br>
<a href="https://drive.google.com/file/d/0Bzs8bzC2MHdeQ0ZkOXFSLTdVSGc/view?usp=drive_web" rel="nofollow noopener">https://drive.google.com/file/d/0Bzs8bzC2MHdeQ0ZkOXFSLTdVSGc/view?usp=drive_web</a><br>
​​<br>
femur.stl<br>
<a href="https://drive.google.com/file/d/0Bzs8bzC2MHdebnc4dVlKT2FOUnM/view?usp=drive_web" rel="nofollow noopener">https://drive.google.com/file/d/0Bzs8bzC2MHdebnc4dVlKT2FOUnM/view?usp=drive_web</a><br>
​</p>

---

## Post #2 by @lassoan (2017-08-31 05:13 UTC)

<p>In the STL that you linked, large portions of the bone is missing, so I don’t think it make sense to “fix” it. Instead, I would recommend to redo the segmentation.</p>
<p>I would recommend to use the latest nightly version of Slicer and perform the following steps:</p>
<ul>
<li>reduce image noise: use <code>Cast Scalar Volume' module to convert input volume to Float type; use </code>Simple Filters<code>module with</code>GradientAnisotropicDiffusionImageFilter` on the converted volume</li>
<li>go to Segment Editor module, use the noise-reduced volume as master volume</li>
<li>create two new “seed” segments, paint one segment inside the bone, the other segment outside the bone</li>
<li>use <code>Grow from seeds</code> effect to segment the bone (click <code>Initialize</code> then make additional paint strokes as needed; finally click <code>Apply</code>)</li>
<li>delete the non-bone (background) segment</li>
<li>create 3D representation by clicking <code>Create surface</code> button</li>
<li>smooth the result by using <code>Smoothing</code> effect</li>
</ul>
<p>See results below (green: original STL; brown: segmentation using the above-described steps):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28dbb433882132183c1cc2e141588a45c7419bdf.jpeg" data-download-href="/uploads/short-url/5PrOmomufdbX1MNOdplghs6vXEr.jpg?dl=1" title="image_00002"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/28dbb433882132183c1cc2e141588a45c7419bdf_2_587x499.jpg" alt="image_00002" data-base62-sha1="5PrOmomufdbX1MNOdplghs6vXEr" width="587" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/28dbb433882132183c1cc2e141588a45c7419bdf_2_587x499.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/28dbb433882132183c1cc2e141588a45c7419bdf_2_880x748.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/28dbb433882132183c1cc2e141588a45c7419bdf_2_1174x998.jpg 2x" data-dominant-color="787F86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_00002</span><span class="informations">2048×1742 845 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Hanaana (2017-08-31 14:39 UTC)

<p>Prof. Doc. Andras,</p>
<p>Thank you so much for the support.</p>
<p>The segmentaion went fantastically for me. However, when it comes to the<br>
last step of saving the model. I didnt have the option to save as an STL my<br>
model.</p>
<p>Looking forward to hearing from you as well as whoever has been through<br>
this same issue.</p>
<p>Best,</p>
<p>Hanaa</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2.png" data-download-href="/uploads/short-url/9YJwj1rb3n1SAgAPoswEup3tMiu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_690x431.png" alt="image" data-base62-sha1="9YJwj1rb3n1SAgAPoswEup3tMiu" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_1380x862.png 2x" data-dominant-color="BDBDD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×900 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-08-31 14:53 UTC)

<p>See instructions for exporting to model node (that can be saved as STL file) here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations#How_to</a></p>

---

## Post #5 by @Hanaana (2017-08-31 15:05 UTC)

<p>Prof. Doc. Andras,<br>
Dear Everyone,</p>
<p>I was writing back to you . I  have fixed the stl export issue. I used<br>
segmentaions module&gt;export,models&gt;export. and finally could save it as a<br>
stl file.</p>
<p>Thank you again Professor for the support.</p>
<p>All the best,</p>
<p>Hanaa<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8221859b64bb3489a001570df8f497b14ca66c9.png" data-download-href="/uploads/short-url/zp5sAzpaU71khPDyJPAu0nLWAsN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8221859b64bb3489a001570df8f497b14ca66c9_2_690x431.png" alt="image" data-base62-sha1="zp5sAzpaU71khPDyJPAu0nLWAsN" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8221859b64bb3489a001570df8f497b14ca66c9_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8221859b64bb3489a001570df8f497b14ca66c9_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8221859b64bb3489a001570df8f497b14ca66c9_2_1380x862.png 2x" data-dominant-color="BFBFDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×900 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2.png" data-download-href="/uploads/short-url/9YJwj1rb3n1SAgAPoswEup3tMiu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_690x431.png" alt="image" data-base62-sha1="9YJwj1rb3n1SAgAPoswEup3tMiu" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45f11c2395b0f038ce308a544dbe05f1d4ef67e2_2_1380x862.png 2x" data-dominant-color="BDBDD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×900 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @deepmech (2017-09-04 16:59 UTC)

<p>hello sir<br>
i am also suffering to edit the .stl model. i didnot try to edit in slicer but import it to Catia v5.<br>
i am engineering student.<br>
i had converted .stl file to .igs format but it is not editable in any format.<br>
i have to perform FE  analyses thats why i converted to that format to open in any FE software.<br>
thanks</p>

---

## Post #7 by @vilem (2017-09-04 19:59 UTC)

<p>Hi<br>
You can’t edit the stl file directly – although you work with the mesh editing (edit the triangles in the mesh) – you have to transform the mesh to surfaces – and edit them. To export to IGES or any other format would not help – it only transform the coordinates of nodes of each triangle surface (plate) and vector o fit.<br>
Vilem</p>

---

## Post #8 by @deepmech (2017-09-05 07:48 UTC)

<p>thank you sir for reply<br>
how to perform  1): transform the mesh<br>
to surfaces<br>
:<br>
presently i am using meshmixer  after 3D slicer to rectify or smoothing the<br>
surfaces, i will try there if possible.</p>
<p>thanks again</p>

---

## Post #9 by @deepmech (2017-09-05 15:10 UTC)

<p>hello vilem Vrbicky<br>
is any tutorial is available related to mesh editing, i  haven,t get the success in edit it???</p>

---

## Post #10 by @lassoan (2017-09-05 15:59 UTC)

<aside class="quote no-group" data-username="deepmech" data-post="8" data-topic="960">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e0b2c6/48.png" class="avatar"> deepmech:</div>
<blockquote>
<p>presently i am using meshmixer  after 3D slicer to rectify or smoothing the surfaces</p>
</blockquote>
</aside>
<p>MeshMixer is a very nice tool but you should be very careful in using it for surfaces obtained from medical images. The main limitation of MeshMixer is that it cannot show you the original image along with the extracted surface, so if you apply some processing there is no way you can assess that the “cleaned up” surface is still follows the original image closely enough. If you do some processing in MeshMixer then you always have to load the processed surface into Slicer to verify that the result is still valid.</p>
<p>Note that you have a number of smoothing option in Slicer: you can smooth the master volume before segmentation (there are a large number of image processing filters in SimpleFilters module); or use the Smoothing effect in Segment Editor.</p>

---

## Post #11 by @lassoan (2017-09-05 16:03 UTC)

<p>How to edit segments:</p>
<p>Segment editor reference manual: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a><br>
Tutorials: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation_for_3D_printing</a><br>
Video tutorial:</p>
<div class="lazyYT" data-youtube-id="Uht6Fwtr9hE" data-youtube-title="How to segment multiple vertebrae in spine CT for 3D printing" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>If you have a surface mesh then you have to import it into a Segmentation node first (using Segmentations module’s Import function).</p>

---

## Post #12 by @deepmech (2017-09-06 07:54 UTC)

<p>thankyou lassoan sir<br>
i learned the smoothing and editing in 3D slicer thats ok.<br>
problem is : we know the bones are made up of two types :1) cortical outer region<br>
2) cancellous inner region</p>
<p>so that i want to keep that two volume separate to provide material properties.<br>
the file from 3D slicer is in .stl format which is considering  one body.<br>
can you give any suggestion related to this???</p>

---

## Post #13 by @lassoan (2017-09-06 22:37 UTC)

<p>Create separate segments for cortical and cancellous bone regions.</p>

---

## Post #14 by @lassoan (2017-09-08 13:35 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-align-segments-to-each-other/1022">How to align segments to each other</a></p>

---

## Post #15 by @deepmech (2017-09-09 13:04 UTC)

<p>hello sir<br>
in segment editor module when i am clicking on color option to change it, it didn’t showing<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/364fea07f5304d6efa3677a7ae388367855765a1.png" data-download-href="/uploads/short-url/7KsZVcXRhbsxnQjwnx44d2Nvwt3.png?dl=1" title="post" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/364fea07f5304d6efa3677a7ae388367855765a1_2_690x287.png" alt="post" data-base62-sha1="7KsZVcXRhbsxnQjwnx44d2Nvwt3" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/364fea07f5304d6efa3677a7ae388367855765a1_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/364fea07f5304d6efa3677a7ae388367855765a1_2_1035x430.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/364fea07f5304d6efa3677a7ae388367855765a1.png 2x" data-dominant-color="B3BCB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">post</span><span class="informations">1357×566 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> option</p>
<p>also sir you told made separate segment for cortical and cancellous bone, how???<br>
what i understand that every bone has outer layer is of cortical bone, how to develop the bone layer exactly above the cancellous of exact dimension.</p>

---

## Post #16 by @lassoan (2017-09-09 16:01 UTC)

<p>Double click on the colored rectangle to open terminology pop-up and change the color there.</p>
<p>There are many ways of separating different bone structures and there is no universally applicable recipe. However, what usually works quite well is segmenting cortical bone by simple thresholding. Then paint with a different segment inside the bone, and with a third segment outside the bone and use grow from seeds effect to generate a complete segmentation. While in preview mode of Grow from seeds, you can modify the seeds interactively to fix potential misclassifications.</p>

---

## Post #17 by @deepmech (2017-09-11 09:18 UTC)

<p>thankyou sir for continuous effort for us this provide me confidence,</p>
<p>in color pop up<br>
there is category &gt; anatomy …&gt; bone&gt; (BUT NO OPTION FOR CORTICAL AND cancelous BONE)<br>
I WANT to know the threshold value for cortical bone and cancellous bone.<br>
how to see the threshold unit in 3D slicer.</p>

---

## Post #18 by @lassoan (2017-09-11 13:30 UTC)

<p>Names, terms you select in the terminology popup do not affect processing. You can look up CT intensity (Hounsfield unit) range for different structures by a simple web search, but the easiest is to choose threshold value based on what you see in the Threshold effect’s preview.</p>
<p>Please avoid using all caps, such as “I WANT”, because</p>
<blockquote>
<p>typing messages in all caps became closely identified with “shouting” or attention-seeking behavior, and may be considered rude</p>
</blockquote>
<p>[<a href="https://en.wikipedia.org/wiki/All_caps" class="inline-onebox">All caps - Wikipedia</a>]</p>

---

## Post #19 by @deepmech (2017-09-12 06:36 UTC)

<p>sorry for that next time no capital letters<br>
thanks for information</p>

---

## Post #20 by @deepmech (2017-10-02 10:23 UTC)

<p>Good afternoon sir<br>
still not succeeded  in creating cortical and cancellous bone.</p>
<p>First i created the cortical bone in segment editor in color of bone<br>
then i changed threshold for capturing cancellous but it also having some coincide threshold and when i created surface and save it, it showing one body.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ecf0133f3d5070e3243d2ed6f9f4d11b6c3b54.jpeg" data-download-href="/uploads/short-url/lOQdaquujMjray8CMVOqngHBofa.jpg?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/98ecf0133f3d5070e3243d2ed6f9f4d11b6c3b54_2_690x367.jpg" alt="Capture2" data-base62-sha1="lOQdaquujMjray8CMVOqngHBofa" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/98ecf0133f3d5070e3243d2ed6f9f4d11b6c3b54_2_690x367.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/98ecf0133f3d5070e3243d2ed6f9f4d11b6c3b54_2_1035x550.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ecf0133f3d5070e3243d2ed6f9f4d11b6c3b54.jpeg 2x" data-dominant-color="C6C2C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1357×723 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>first one for cortical and second for cancellous(but it also come on surface of cortical)</p>
<p>is any video is available for this?<br>
thankyou</p>

---

## Post #21 by @lassoan (2017-10-02 15:01 UTC)

<p>Try to be more conservative with your thresholds, make sure the areas that you include in a segment are definitely correct. Then use <code>Grow from seeds</code> effect to create complete segmentation from those “seed” regions.</p>
<p>You can also use <code>Watershed</code> effect (available in SegmentEditorExtraEffects extension), which takes the same input as <code>Grow from seeds</code> but produces a smoother output. Smoothness is controlled by Object scale, try with 1mm and adjust as needed. The main disadvantage of <code>Watershed</code> is that it is slower compared to <code>Grow from seeds</code>.</p>

---

## Post #22 by @lassoan (2017-10-03 00:03 UTC)

<p>You might also find <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BoneTextureExtension">BoneTextureExtension</a> useful for analyzing bone structure.</p>

---

## Post #23 by @lassoan (2018-05-01 04:28 UTC)

<p>2 posts were split to a new topic: <a href="/t/getting-coordinates-of-mri-visible-markers/2742">Getting coordinates of MRI visible markers</a></p>

---
