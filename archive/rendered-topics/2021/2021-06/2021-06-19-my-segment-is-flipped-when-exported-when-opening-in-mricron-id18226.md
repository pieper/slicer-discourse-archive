---
topic_id: 18226
title: "My Segment Is Flipped When Exported When Opening In Mricron"
date: 2021-06-19
url: https://discourse.slicer.org/t/18226
---

# My segment is flipped when exported when opening in MRIcron

**Topic ID**: 18226
**Date**: 2021-06-19
**URL**: https://discourse.slicer.org/t/my-segment-is-flipped-when-exported-when-opening-in-mricron/18226

---

## Post #1 by @pardisz (2021-06-19 15:57 UTC)

<p>Hi<br>
I painted a segment using a template MRI scan and exported the segment using the same MRI scan as a reference. When I open the same scan in MRIcron and overlay it with the segment I have drawn I can see that it is flipped during the export process (i.e. it looks right in slicer but is flipped upon export). I can see there is a FAQ on flipped images but this is regarding flipped images in slicer, not the export. I wonder if anyone else has run into this problem (and solved it)?</p>
<p>Thanks</p>

---

## Post #2 by @Juicy (2021-06-21 07:49 UTC)

<p>I don’t know exactly what you mean, or anything about the other software (MRIcron) but maybe it has something to do with an RAS to LPS coordinate system change. Last I remember slicer uses RAS meaning the positive x direction is toward the right, positive y is toward the anterior and positive z is toward superior. Many other softwares use LPS which is obviously opposite in the x and y directions.</p>
<p>If all else fails you could possibly flip the coordinate system in the x and y directions in slicer before you export the segment by applying the following linear transform. I know that this does not seem like an elegant solution unfortunately:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bdf816cc362634547377671b4a7e6eb76c162c9.png" alt="image" data-base62-sha1="meURIo1YdA2yyZHPyetaO13Xmjv" width="537" height="370"></p>

---

## Post #3 by @Juicy (2021-06-21 08:05 UTC)

<p>This may help?</p>
<aside class="quote quote-modified" data-post="1" data-topic="10446">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">Model files are now saved in LPS coordinate system</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    While Slicer uses RAS coordinate system internally, images, transforms, and markups files are stored in LPS coordinate system, because DICOM and all medical image computing software (maybe except a few very old ones) uses LPS coordinate system in files. 
However, Slicer has been still using its internal RAS coordinate system in mesh files (STL, VTK, VTP, OBJ, PLY), which <a href="https://issues.slicer.org/view.php?id=4445" rel="noopener nofollow ugc">caused issues when interfacing with third-party software</a>. 
Starting from tomorrow (Slicer-4.11.0-2020-02-26, revision 28794), …
  </blockquote>
</aside>


---
