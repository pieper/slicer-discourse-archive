# Flipped volume on 3D view but correct on red/green/yellow

**Topic ID**: 37143
**Date**: 2024-07-02
**URL**: https://discourse.slicer.org/t/flipped-volume-on-3d-view-but-correct-on-red-green-yellow/37143

---

## Post #1 by @coco (2024-07-02 07:51 UTC)

<p>Dear all, I had a very odd thing happenning to me.<br>
I used the crop volume module to create left and right brain hemispheres out of a full brain. First sample went well. Second sample I had this flip between the two hemispheres. What is puzzling is that the red (axial) axis is showing the correct orientation ie right hemisphere whilst the 3D view is showing that same hemisphere but flipped. Don’t pay attention to the ROI which is set on the left hemisphere here.<br>
Any thoughts on what could have happenned ?<br>
To me it seems similar to a previous topic <a href="https://discourse.slicer.org/t/why-does-3d-model-flip-from-other-views/28615">Why does 3D model flip from other views? - Support - 3D Slicer Community</a> but I don’t think the answer was clear or accepted that, like me, the 3D view was mirrored relative to the red/green/yellow axes.<br>
Looks like this could explain the issue: “Slicer displays RAS in the interface” ?</p>
<p>I’m using slicer 5.6.2 on a calculation cluster running linux.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/836d7525ec7e886624982f3600b4d732165993d9.jpeg" data-download-href="/uploads/short-url/iKF3KtfstiddG55MUmLqxs8drPX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/836d7525ec7e886624982f3600b4d732165993d9_2_690x381.jpeg" alt="image" data-base62-sha1="iKF3KtfstiddG55MUmLqxs8drPX" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/836d7525ec7e886624982f3600b4d732165993d9_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/836d7525ec7e886624982f3600b4d732165993d9_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/836d7525ec7e886624982f3600b4d732165993d9_2_1380x762.jpeg 2x" data-dominant-color="848595"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1062 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2024-07-02 14:44 UTC)

<p>Slicer uses the radiological convention for displaying images by default (<a href="https://nipy.org/nibabel/neuro_radio_conventions.html" class="inline-onebox" rel="noopener nofollow ugc">Neuroimaging in Python — NiBabel 5.3.0.dev5+g773e3c40 documentation</a>), so the patient’s left in the slice views is displayed on the right.</p>
<p>If you would like, you change the behavior by following the instructions in this post:</p><aside class="quote quote-modified" data-post="8" data-topic="29883">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883/8">A bit of confusion about the slicer coordinate system</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In Edit-&gt;Application Settings you can change whether patient right is screen left or not. 
[image] 
That work came out of the following PR if you are curious about the conversation that led to it.
  </blockquote>
</aside>


---
