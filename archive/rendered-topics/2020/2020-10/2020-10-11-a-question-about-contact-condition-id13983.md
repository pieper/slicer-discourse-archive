# A question about contact condition

**Topic ID**: 13983
**Date**: 2020-10-11
**URL**: https://discourse.slicer.org/t/a-question-about-contact-condition/13983

---

## Post #1 by @xxl (2020-10-11 02:46 UTC)

<p>Hello.I’m new here and want to know whether the contact coordinates generated in 3D slicer are individual space or standard space.</p>

---

## Post #2 by @xxl (2020-10-11 02:40 UTC)

<p>Hello.I want to know whether the contact coordinates generated in Slicer are individual space or standard space.Looking forward to your reply!</p>

---

## Post #3 by @Andinet_Enquobahrie (2020-10-11 13:18 UTC)

<p>Hi <a class="mention" href="/u/xxl">@xxl</a></p>
<p>I am not sure why you mean by contact coordinate or individual space.</p>
<p>The following wiki page has a good description of coordinate system setup in 3D Slicer</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="15" height="15">
      <a href="https://www.slicer.org/wiki/Coordinate_systems" target="_blank" rel="noopener nofollow ugc">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="15" height="15">

<h3><a href="https://www.slicer.org/wiki/Coordinate_systems" target="_blank" rel="noopener nofollow ugc">Coordinate systems - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>After reviewing this information, please let’s know if you have specific questions as it relates to the coordinate system setup.</p>
<p>-Andinet</p>

---

## Post #4 by @lassoan (2020-10-11 18:48 UTC)

<p>Slicer uses the coordinate system of the image that you load, unless you change it. If you load an image from DICOM then you will get coordinates in that individual scan’s coordinate system. If you load a nifti file in MNI space then points are in that coordinate system.</p>
<p>If you want to have the image in some standard coordinate system then there are many registration techniques available in Slicer that can help, such as simple AC-PC alignment, automatic image registration, manual landmark registration, etc.</p>

---

## Post #5 by @xxl (2020-10-12 03:01 UTC)

<p>We would like to set the SEEG contact positions in slicer and export them to a text file.Then we will import it in brainstorm.As far as I know,  all the contacts should be in the MNI coordinates.So I want to know whether Slicer can help me.Can you give me some better suggestions?</p>
<p>Thank you for your help!</p>

---
