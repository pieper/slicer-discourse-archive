# Segmenting Canon Ultrasound volumes 

**Topic ID**: 31240
**Date**: 2023-08-19
**URL**: https://discourse.slicer.org/t/segmenting-canon-ultrasound-volumes/31240

---

## Post #1 by @Ladnewg (2023-08-19 08:49 UTC)

<p>Hi !<br>
I am currently working on an ultrasound project.<br>
I use the equipment: following Aplio I700 Canon with Smart Sensor 3D mode: Magnetic tracking system.<br>
I acquired a series of images of a ghost in order to calculate a volume but I cannot import the file into 3D Slicer, or at least there is no consistency in the orientation of the slices in space.</p>
<p>The errors message are :  Image spacing may need to be calibrated for accurate size measurements.<br>
Multi-frame image.if slice orientation or spacing is non uniform the the image may be displayed incorrectly. Use with caution.</p>
<p>Liens du fichier : <a href="https://drive.google.com/drive/folders/1TvS1Xg2D-0GTgNEaaiMTyxijH3TRaSUn?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">DICOM - Google Drive</a></p>
<p>Thank you for your answers.</p>

---

## Post #2 by @lassoan (2023-08-19 10:06 UTC)

<p>Unfortunately, ultrasound imaging device manufacturers often do not let users access 3D image data that they acquire. Users of most imaging modalities (such as CT, MRI, PET, etc.) would not accept this absurd situation, but for some reason ultrasound users got used to this and don’t raise their voice. The result is what you are experiencing now: you acquire 3D image data but you can view and process it only by using the manufacturer’s own software.</p>
<p>The best solution would be to stop purchasing 3D ultrasound equipment if it does not give you access to the data that you acquire. That would be the only thing to motivate ultrasound device manufacturers to change their current practice.</p>
<p>You can try to contact Canon to get access to their Image3dAPI codec and then you can use <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">SlicerHeart extension to import 3D ultrasound data</a>.</p>
<p>Another option is to do some manual work to figure out the image format by trial and error using RawImageGuess as shown here:</p>
<aside class="quote" data-post="2" data-topic="9400">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4bbf92/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/mvl-file-and-rawimageguess/9400/2">MVL File and RawImageGuess</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    my slicer crashes (4.10.2 and 4.11) when i try to upload MVL file even if my RawImageGuess extension was already installed. any idea?
  </blockquote>
</aside>


---

## Post #3 by @Anjusha_K (2023-10-06 18:15 UTC)

<p>Ultrasound data saved in raw dicom format will not be able to load in external viewers. While doing dicom export of Sensor 3D, please select export in voxel format. This data can be loaded in any external viewers.</p>

---
