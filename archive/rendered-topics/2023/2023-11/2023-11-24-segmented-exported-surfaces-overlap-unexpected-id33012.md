# Segmented, exported surfaces overlap (unexpected)

**Topic ID**: 33012
**Date**: 2023-11-24
**URL**: https://discourse.slicer.org/t/segmented-exported-surfaces-overlap-unexpected/33012

---

## Post #1 by @mau_igna_06 (2023-11-24 19:56 UTC)

<p>I first segmented the bone (green), then I painted the yellow-browinsh segment without allowing overlap with the green one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d06fa6e8a52a88ad1ea2bab02b46e14bb56920c.jpeg" data-download-href="/uploads/short-url/1Rf9N8Uw74nFtD5VDTeDnumVqr2.jpeg?dl=1" title="Captura de pantalla 2023-11-24 163632_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d06fa6e8a52a88ad1ea2bab02b46e14bb56920c_2_690x397.jpeg" alt="Captura de pantalla 2023-11-24 163632_2" data-base62-sha1="1Rf9N8Uw74nFtD5VDTeDnumVqr2" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d06fa6e8a52a88ad1ea2bab02b46e14bb56920c_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d06fa6e8a52a88ad1ea2bab02b46e14bb56920c_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d06fa6e8a52a88ad1ea2bab02b46e14bb56920c_2_1380x794.jpeg 2x" data-dominant-color="8E8E87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-11-24 163632_2</span><span class="informations">1849×1066 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I did “export visible segments to models”. The 3D models of the segments <em><strong>do</strong></em> overlay. Check this image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/417ba177c33addd418bae190864ce5097b332355.jpeg" data-download-href="/uploads/short-url/9lhUCmcxr1GCPIpjCotluCv21tH.jpeg?dl=1" title="Captura de pantalla 2023-11-24 163709_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/417ba177c33addd418bae190864ce5097b332355_2_690x424.jpeg" alt="Captura de pantalla 2023-11-24 163709_2" data-base62-sha1="9lhUCmcxr1GCPIpjCotluCv21tH" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/417ba177c33addd418bae190864ce5097b332355_2_690x424.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/417ba177c33addd418bae190864ce5097b332355_2_1035x636.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/417ba177c33addd418bae190864ce5097b332355_2_1380x848.jpeg 2x" data-dominant-color="8D8B8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2023-11-24 163709_2</span><span class="informations">1848×1138 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is unexpected. Is it a bug?</p>
<p>I’m using Slicer 5.2.2 stable release</p>

---

## Post #2 by @mau_igna_06 (2023-11-27 21:25 UTC)

<p>Could someone comment on this?</p>
<p>Thanks a lot</p>

---

## Post #3 by @mikebind (2023-11-27 22:19 UTC)

<p>I suspect this is due to each segment being smoothed independently in the conversion to the closed surface representation.  In the Segmentations module, click the dropdown next to “Closed Surface” to access and modify the conversion parameters.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/6629803a743fb04d8c98ed0560a9cb90b541aead.png" alt="image" data-base62-sha1="ezLCgEN0Ava47wddHpXiyUx9GUJ" width="396" height="174"><br>
This will raise the following window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1581a1b70ebd9e6030d66ab143e7396b09340222.png" data-download-href="/uploads/short-url/34fLdggOOMY4CwVsCjwJfemrQX0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1581a1b70ebd9e6030d66ab143e7396b09340222_2_373x500.png" alt="image" data-base62-sha1="34fLdggOOMY4CwVsCjwJfemrQX0" width="373" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1581a1b70ebd9e6030d66ab143e7396b09340222_2_373x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1581a1b70ebd9e6030d66ab143e7396b09340222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1581a1b70ebd9e6030d66ab143e7396b09340222.png 2x" data-dominant-color="E1E3E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">471×631 66.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Click on the conversion path step (the line in the upper section), and then try changing the Joint smoothing flag to 1.</p>
<p>I tried a quick search in the documentation to see if I could find a reference to this, but didn’t find anything.  However, I think this should do what you want.</p>

---

## Post #4 by @mau_igna_06 (2023-11-27 22:47 UTC)

<p>Thanks for the answer. I’ll check and get back</p>

---

## Post #5 by @cpinter (2023-11-28 14:01 UTC)

<p>Your source representation (i.e. the one that you can consider most faithful to the real world object) is binary labelmap. When you convert these labelmaps to closed surface, then by default you apply smoothing. If the artifacts you get from smoothing are undesired, then you can always disable smoothing.</p>
<p>In that case, however, you get a surface that consists of blocks and it cannot be rendered nicely. Another thing you can do is supersample the segmentation’s binary labelmap, so that it has a higher resolution than the anatomical image. Then you may do less smoothing when you do the conversion to reduce the artifacts you do not want.</p>
<p>You can read very briefly about representations here:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a><br>
In a bit more detail:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://scholar.google.ca/citations?view_op=view_citation&amp;hl=en&amp;citation_for_view=LbnADQ0AAAAJ:qUcmZB5y_30C">
  <header class="source">
      <img src="https://scholar.google.ca/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://scholar.google.ca/citations?view_op=view_citation&amp;hl=en&amp;citation_for_view=LbnADQ0AAAAJ:qUcmZB5y_30C" target="_blank" rel="noopener">scholar.google.ca</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://scholar.google.ca/citations?view_op=view_citation&amp;hl=en&amp;citation_for_view=LbnADQ0AAAAJ:qUcmZB5y_30C" target="_blank" rel="noopener">Polymorph segmentation representation for medical image computing</a></h3>

  <p>C Pinter, A Lasso, G Fichtinger, Computer methods and programs in biomedicine, 2019 - Cited by 63</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
In even more detail:<br>
<a href="https://qspace.library.queensu.ca/handle/1974/26422" class="onebox" target="_blank" rel="noopener">https://qspace.library.queensu.ca/handle/1974/26422</a></p>

---

## Post #6 by @mau_igna_06 (2023-11-28 17:33 UTC)

<p>Hi <a class="mention" href="/u/mikebind">@mikebind</a>, thanks for your answer</p>
<p>I did not notice any change by using “Joint smoothing” and exporting the models together (there is still collision between the extracted meshes)</p>

---

## Post #7 by @mau_igna_06 (2023-11-28 17:36 UTC)

<p>Thanks a lot for your answer <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>I’ll read more about links you provided on weekend since this is only for a feature of a side-project I have</p>

---

## Post #8 by @mikebind (2023-11-28 18:04 UTC)

<p>Thanks for the detailed references <a class="mention" href="/u/cpinter">@cpinter</a>!  Since it looks like you are the expert on this, can you describe what the “Joint smoothing” parameter does in the conversion, if it is not ensuring that touching surfaces do not overlap?</p>

---

## Post #9 by @pieper (2023-11-29 00:04 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> it would be good if you could try the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/modelmaker.html#:~:text=Joint%20Smoothing%20(JointSmoothing)%3A%20This%20will%20ensure%20that%20all%20resulting%20models%20fit%20together%20smoothly%2C%20like%20jigsaw%20puzzle%20pieces.%20Otherwise%20the%20models%20will%20be%20smoothed%20independently%20and%20may%20overlap.">JointSmoothing option from the older ModelMaker</a>. That mode was specifically added to provide watertight boundaries because the vertices of both models were moved identically during the smoothing process, so there was never any gap between the meshes for adjacent segments.  There may still be some aspects of the older code that need to be incorporated in the segmentations infrastructure.</p>
<p>This topic has come up before, but it’s still not clear to me that we can easily get the same output meshes that we get with ModelMaker.</p>
<aside class="quote" data-post="4" data-topic="4044">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/surface-rendering-of-many-segments/4044/4">surface rendering of many segments</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We have that option in Smoothing effect but not in the automatic conversion between segment representations. The assumption is that smoothing operation in “binary labelmap to closed surface” conversion is only used for removing staircase artifacts and so it does not require adjustment of the geometry. 
We would need to implement some new mechanism in segmentation infrastructure to allow joint conversion of multiple segments, because right now conversion happens segment by segment.
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="1" data-topic="6692">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/exported-stl-files-from-the-segmentation-has-intersection-penetration/6692">Exported STL files from the segmentation has intersection/penetration</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version: 4.10.1 
Hi everyone, 
I want to create models for mandible and teeth from a CBCT scan. After importing the DICOM file to 3Dslicer and completing the segmentation process I used segmentations/export to export the segmentations as STL models. Then I import those STL files into Meshmixer and I found out the models have intersections! (the surface of the teeth model penetrates the surface of the bone model as you can see in the image). I noticed that 3D …
  </blockquote>
</aside>

<aside class="quote quote-modified" data-post="9" data-topic="6692">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/exported-stl-files-from-the-segmentation-has-intersection-penetration/6692/9">Exported STL files from the segmentation has intersection/penetration</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/tekk_ya">@Tekk_ya</a> you might try a slightly different pathway to get “watertight” models. 

export the segmentation to a label map
run the ModelMaker module with the “Joint Smoothing” operation enabled

what this will do is apply the same smoothing operation to matching vertices from the different segments so that no gaps are introduced.  In the example below the yellow/green surfaces use the default and the red/blue use Joint Smoothing. 
<a class="mention" href="/u/lassoan">@lassoan</a> I don’t see that the segmentation closed surface option ex…
  </blockquote>
</aside>


---

## Post #10 by @lassoan (2023-11-29 00:36 UTC)

<p>By enabling “Joint smoothing” option in segmentation conversion parameters, we perform the exact same algorithm as in the Model maker module. The only difference is that it is performed for each layer. If your segments are non-overlapping but they are in separate layers (e.g., because you enabled overlap before) then you can collapse them into one layer in Segmentations module’s Layers section.</p>

---

## Post #11 by @pieper (2023-11-29 04:54 UTC)

<p>If the segments were overlapping then yes, I can see they cannot be made watertight.  But I still don’t see that this is the case in the data <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> posted.  It will be good to get some clarity on on this.</p>

---

## Post #12 by @cpinter (2023-11-29 10:11 UTC)

<p>I just tried joint smoothing (5.5.0-2023-11-10 r32231 / 48b6d55, Win11), and I found that if smoothing factor is larger than 0, then we lose the triangles.</p>
<p>Btw I never used joint smoothing here in the conversion parameters but I assume that it should work preserving the cells.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d69b65872bb6841426a33275b1aa94dd5f090d6.mp4">
  </div><p></p>

---

## Post #13 by @mau_igna_06 (2023-12-09 20:34 UTC)

<p>Hi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2dbb0050016578d5376871fbc735a94a2afde88.png" data-download-href="/uploads/short-url/wmSAnAObVcXIFCmCrVoEpsCiJ9m.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dbb0050016578d5376871fbc735a94a2afde88_2_689x353.png" alt="image" data-base62-sha1="wmSAnAObVcXIFCmCrVoEpsCiJ9m" width="689" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dbb0050016578d5376871fbc735a94a2afde88_2_689x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dbb0050016578d5376871fbc735a94a2afde88_2_1033x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2dbb0050016578d5376871fbc735a94a2afde88_2_1378x706.png 2x" data-dominant-color="97979D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2558×1311 505 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried all last three options on the dialog, to update the 3D surface of two touching segments on a segmentation, then exported them as models and named the different resulting folders as a binary table (e.g. folder named 100 means it was created using conversion parameters “Joint smoothing”=1, “SurfaceNets smoothing”=0, “Conversion method”=0)</p>
<p><a href="https://file.io/t7pu1SOXR3QA" rel="noopener nofollow ugc">Download SceneFile</a><br>
(Done with latest Slicer Preview release from today)</p>
<p>Hope this helps on debugging</p>

---

## Post #14 by @pieper (2023-12-09 21:09 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="13" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I tried all last three options on the dialog</p>
</blockquote>
</aside>
<p>Where there gaps in all methods?</p>

---

## Post #15 by @mau_igna_06 (2023-12-09 21:17 UTC)

<p>No collisions (that is watertightness between segments) was achieved using:<br>
“Joint smoothing”=0, “SurfaceNets smoothing”=1</p>
<p>The names of the folders that are visible on the earlier picture explain a bit what I found after each export</p>

---

## Post #16 by @mau_igna_06 (2023-12-12 21:16 UTC)

<p>Is this considered solved?</p>

---

## Post #17 by @mikebind (2023-12-12 21:29 UTC)

<p>I’m not sure I fully follow all the results here.  Is your conclusion that you were only able to achieve non-collision by accepting bad smoothing?  That is, there was not a method you found which gave good smoothing results without also introducing overlaps or inappropriate gaps between smoothed segments?</p>

---

## Post #18 by @mau_igna_06 (2023-12-12 21:36 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="17" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Is your conclusion that you were only able to achieve non-collision by accepting bad smoothing? That is, there was not a method you found which gave good smoothing results without also introducing overlaps or inappropriate gaps between smoothed segments?</p>
</blockquote>
</aside>
<p>It appears to be like that.<br>
The problem is avoiding the overlaps</p>

---

## Post #19 by @mikebind (2023-12-12 21:50 UTC)

<p>I’m surprised.  From my admittedly naïve perspective, I don’t see why this is an especially difficult problem.  It is easily detectable from the source labelmap exactly where two segments are in contact.  Couldn’t that contact surface be smoothed, and then that shared surface be connected to each of the two segments for that region of the smoothed representation (with same triangluation but reversed surface normals for each to keep the proper sense of inside vs outside)?  Mentally, that’s what I always assumed “joint smoothing” was doing under the hood.</p>

---

## Post #20 by @pieper (2023-12-12 22:05 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="19" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Couldn’t that contact surface be smoothed, and then that shared surface be connected to each of the two segments for that region of the smoothed representation (with same triangluation but reversed surface normals for each to keep the proper sense of inside vs outside)? Mentally, that’s what I always assumed “joint smoothing” was doing under the hood.</p>
</blockquote>
</aside>
<p>This is exactly what I had understood too based on the description from Bill Lorensen back in the day that he was using <a href="https://insight-journal.org/browse/publication/740">this algorithm</a> and then doing the same mesh operations to both sides of the shared interface.  But I checked with Mauro’s data by exporting to labelmap and running JointSmoothing in ModelMaker and it does have the same behavior.  Looking at the implementation it seems that it doesn’t use the Cuberille approach.</p>

---

## Post #21 by @lassoan (2023-12-13 00:06 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="19" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I don’t see why this is an especially difficult problem.</p>
</blockquote>
</aside>
<p>This is interesting because for me this problem is not just extremely hard but actually seems impossible to solve. When multiple segments meet at a sharp corner then you cannot make the surface of every segment smooth without introducing gaps or overlaps between segments.</p>
<p>Isosurfaces without smoothing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7172c0cc2f9b3036990650547a94a84048792223.jpeg" data-download-href="/uploads/short-url/gbBOjHxUcVCq3hIISQxN8On1F7B.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7172c0cc2f9b3036990650547a94a84048792223_2_620x499.jpeg" alt="image" data-base62-sha1="gbBOjHxUcVCq3hIISQxN8On1F7B" width="620" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7172c0cc2f9b3036990650547a94a84048792223_2_620x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7172c0cc2f9b3036990650547a94a84048792223_2_930x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7172c0cc2f9b3036990650547a94a84048792223_2_1240x998.jpeg 2x" data-dominant-color="74664D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1375×1108 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Smoothing causes overlap and gap, which could be reduced by joint smoothing, but could not be fully eliminated (unless you accept to have larger gap or sharp edges in some segments):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61973c14cbb6307847258c5aecdef4bffed1c057.jpeg" data-download-href="/uploads/short-url/dVkkFQDGrMTJTN8JEe65Z0mVzD1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61973c14cbb6307847258c5aecdef4bffed1c057_2_617x500.jpeg" alt="image" data-base62-sha1="dVkkFQDGrMTJTN8JEe65Z0mVzD1" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61973c14cbb6307847258c5aecdef4bffed1c057_2_617x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61973c14cbb6307847258c5aecdef4bffed1c057_2_925x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61973c14cbb6307847258c5aecdef4bffed1c057_2_1234x1000.jpeg 2x" data-dominant-color="75654D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1373×1111 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="pieper" data-post="20" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Looking at the implementation it seems that it doesn’t use the Cuberille approach</p>
</blockquote>
</aside>
<p>Slicer’s Model Maker has been always using <code>vtkWindowedSincPolyDataFilter</code> for joint smoothing (since the very first commit in 2006). I don’t think cuberille isosurfacing has ever been implemented in VTK or used in Slicer. For labelmaps with multiple labels it is not useful anyway (as the isosurface in a labelmap image is not smooth).</p>
<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I just tried joint smoothing (5.5.0-2023-11-10 r32231 / 48b6d55, Win11), and I found that if smoothing factor is larger than 0, then we lose the triangles.</p>
</blockquote>
</aside>
<p>I remember it was working before but I can confirm that no surface, only points are visible in Slicer-5.6.1. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you have a look?</p>
<p>I’ve updated this issue that tracks the status of this feature:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/4604">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4604" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4604" target="_blank" rel="noopener">Add joint smoothing option to labelmap to surface conversion</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:04:03" data-timezone="UTC">01:04AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Medium
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=4604). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #22 by @mikebind (2023-12-13 05:47 UTC)

<p>Yes, places where more than two segments touch would need to be handled as a special case where sharper edges would need to be allowed.  It’s not clear to me that forbidding sharp edges but allowing introduction of overlaps and gaps is a better solution than enforcing mating surfaces but allowing sharp edges. Looking at the documentation for vtkWindowedSincPolyDataFilter, it seems like it has some ability to treat certain edges as special (internal FeatureEdges or external BoundaryEdges) and subject to different smoothing rules.  Again, I’m quite ignorant of how these things <em>really</em> work, but if I were trying to conceptually design how I think it <em>could</em> work, I would maybe first extract any 1D chains of edges which are shared more than 2 segments, and smooth each of those first.  Next, contiguous 2D surfaces which are shared by 2 segments could be identified.  The outer edge boundaries of those surfaces (where the interface contacts non-segment voxels) could be smoothed next, and then the interiors of those surfaces, holding the outer boundary edges constant.  Lastly, the rest of the segment boundaries can be smoothed as currently, with the only difference that the interface surfaces can not be moved.  Maybe there are issues I’m not thinking of which would make such a scheme unworkable, but it seems plausible to me.</p>

---

## Post #23 by @pieper (2023-12-13 15:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="33012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer’s Model Maker has been always using <code>vtkWindowedSincPolyDataFilter</code> for joint smoothing (since the very first commit in 2006). I don’t think cuberille isosurfacing has ever been implemented in VTK or used in Slicer.</p>
</blockquote>
</aside>
<p>Yes, Bill must have been referring to an algorithm that never made it into the main codebase - he talked about having a multi-label Cuberille approach that took all touching segments into account when doing the smoothing, along the lines <a class="mention" href="/u/mikebind">@mikebind</a> describes.  It doesn’t matter too much for visualization, which is probably why they ended up doing the windowed sinc a approach, but his motivation was watertight 3D printing.</p>

---

## Post #24 by @Thibault_Pelletier (2023-12-18 07:59 UTC)

<p>Hi everyone!</p>
<p>There was this thread on the VTK Discourse on the smoothing using the newly integrated vtkSurfaceNets3D method : <a href="https://discourse.vtk.org/t/new-isocontouring-filter-for-discrete-labled-volumetric-data-vtksurfacenets3d/10614/11" class="inline-onebox" rel="noopener nofollow ugc">New Isocontouring filter for discrete, labled volumetric data: vtkSurfaceNets3D - #11 by will.schroeder - Development - VTK</a></p>
<p>From my understanding, both the joint smoothing option and separate smoothing options should be possible using this class.</p>
<p>Best,<br>
Thibault</p>

---
