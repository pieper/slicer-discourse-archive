# Load 3D ultrasound from Samsung .mvl or DICOM files

**Topic ID**: 16784
**Date**: 2021-03-21
**URL**: https://discourse.slicer.org/t/load-3d-ultrasound-from-samsung-mvl-or-dicom-files/16784

---

## Post #1 by @B1z4rr3 (2021-03-21 12:28 UTC)

<p>hello I am not able to load the dicom files, the three windows all appear in axial … can you help me?</p>

---

## Post #2 by @lassoan (2021-03-24 17:59 UTC)

<p>Most likely your files are not 3D volumes, just pictures taken of renderings of volumes. If you share your data sets (or at least the DICOM header of your data sets) then we can give more specific advice.</p>

---

## Post #3 by @B1z4rr3 (2021-03-26 11:33 UTC)

<p>Hello, could you send me your email to send the documents to you?  thanks</p>

---

## Post #4 by @lassoan (2021-03-26 15:20 UTC)

<p>You can upload the files somewhere and send the link to me in a private message.</p>

---

## Post #5 by @B1z4rr3 (2021-03-26 19:00 UTC)

<p>Here are the files! Thank you for the help!</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="16" height="16">
      <a href="https://wetransfer.com/downloads/4bf801d6cc372fcc8a5077864a3b91e120210324215613/9dead7" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://wetransfer.com/downloads/4bf801d6cc372fcc8a5077864a3b91e120210324215613/9dead7" target="_blank" rel="noopener nofollow ugc">24032021-175346_20210324181732_1 and 42 more files</a></h3>

<p>43 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2021-03-27 01:05 UTC)

<p>The folder contains DICOM files and proprietary Samsung .mvl files.</p>
<p>The DICOM parser failed to find any DICOM files because an invalid file catalog (DICOMDIR file) was placed in the folder (the DICOMDIR referred to non-existing subfolders). After removing the DICOMDIR file, indexing of the files succeeded and the images showed up in the DICOM browser. Unfortunately, these files are just videos of the 3D rendering, not 3D volumes. These files are not usable for 3D printing.</p>
<p>The .mvl file seem to contain full 3D data, but in a proprietary format. In the past, we successfully loaded volumes from Samsung .mvl files, but these ones are encoded with an unknown image compression or encryption algorithms. Therefore, we don’t know how to load them.</p>
<p>Contact Samsung and try to ask for a converter that create files in any standard file format (DICOM, nrrd, metaimage, etc.); an <a href="https://github.com/MedicalUltrasound/Image3dAPI">Image3dAPI</a>-compliant codec, or specification of the file format. It is not very likely that they would provide any of these, but it is important for them to know that their customers need this.</p>
<p>If you find that Samsung does not intend to fulfill your needs then you may choose to go to other manufacturers. For example, GE makes easily available an Image3dAPI-compliant codec, which allows its users to access the 3D ultrasound data.</p>

---

## Post #7 by @B1z4rr3 (2021-03-27 12:51 UTC)

<p>thank you for the help we’re clearly very new at this! do you know how to correctly save the DICOM 3D Data in a Samsung machine? could you send us a video ou something like that of how we can correctly save the files?</p>

---

## Post #8 by @lassoan (2021-03-27 19:07 UTC)

<p>I asked Samsung representatives at a trade show, about 2 years ago and they told me that they do not allow users to access the 3D image data outside their own software. They did not provide documentation for their proprietary data format and did not offer export of 3D image data to DICOM or any other standard image format.</p>
<p>The situation might have changed since then. Maybe they still do not give you access to 3D image data but maybe at least they can export STL. You need to contact them, let them know what you need, and see what they can offer now. If they still think that it is OK to deny access to your own 3D data then you may tell them that other 3D ultrasound vendors offer this, for example via the open <a href="https://github.com/MedicalUltrasound/Image3dAPI">Image3dAPI</a>.</p>

---

## Post #9 by @David_Fromholtz (2022-08-03 02:46 UTC)

<p>Was there any more development for the Raw Image Guess to become automated?  I have some mvl ultrasound files i am trying to extract 3d volume data and its very pain staking. Really wish Samsung would just make that ‘Export STL’ button haha!</p>

---

## Post #10 by @lassoan (2022-08-03 06:54 UTC)

<p>I’m not aware that Samsung made any progress in this. Please let your Samsung sales representative know that you need 3D/4D image export feature into open file formats.</p>
<p>In general, companies try to avoid data export features into open file formats because they prefer to lock users into only use their proprietary software (and of course it takes resources to develop, maintain, and support features). However, if enough customers ask for data export feature (even refuse to buy the product if it cannot export to open file formats) then companies may have enough incentives to change their current practice.</p>

---
