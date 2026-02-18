# How to import a labelmap directly for model generation?

**Topic ID**: 12747
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/how-to-import-a-labelmap-directly-for-model-generation/12747

---

## Post #1 by @KKad (2020-07-27 13:29 UTC)

<p>Hello Slicer Community!<br>
I’m a very new user, I’m interested in using the Model Maker module to generate a 3D mesh for a biomechanical finite element analysis.  I have 5 materials and around 100 3D parts and they’re supposed to be sharing interfaces.</p>
<p>I currently have a series of 2D arrays (matlab or python) specifying material/part indexes (one array for each slice). I assume this is what’s called the label map.</p>
<p>Question 1: I’m having trouble figuring out how to import the label map data as I understand that it’s normally produced from the segmentation step (which was already done outside slicer in my case as I already have the label data). I’ve tried to search for the proper file format to import but was not successful.</p>
<p>Bonus Question 2: How would the model maker handle labels that only show up in 1 slice only? Does it ignore or will it throw an error?</p>
<p>Bonus Question 3: If the volumes are in contact how would the model maker handle shared interfaces? I need the mesh to be conforming (interface nodes between materials must be shared)</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2020-07-27 13:38 UTC)

<aside class="quote no-group" data-username="KKad" data-post="1" data-topic="12747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kkad/48/7610_2.png" class="avatar"> KKad:</div>
<blockquote>
<p>I’ve tried to search for the proper file format to import but was not successful.</p>
</blockquote>
</aside>
<p>Slicer can understand DICOM and most research file formats, but I would recommend NRRD file format, as it is very simple and Slicer stores segmentation in this file format by default anyway.</p>
<aside class="quote no-group" data-username="KKad" data-post="1" data-topic="12747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kkad/48/7610_2.png" class="avatar"> KKad:</div>
<blockquote>
<p>How would the model maker handle labels that only show up in 1 slice only? Does it ignore or will it throw an error?</p>
</blockquote>
</aside>
<p>You don’t need Model maker module anymore. If you load a surface mesh or labelmap into a segmentation node that you can get any representation out of it. See more details here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="KKad" data-post="1" data-topic="12747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kkad/48/7610_2.png" class="avatar"> KKad:</div>
<blockquote>
<p>If the volumes are in contact how would the model maker handle shared interfaces? I need the mesh to be conforming (interface nodes between materials must be shared)</p>
</blockquote>
</aside>
<p><a href="https://github.com/lassoan/SlicerSegmentMesher#segment-mesher-extension">SegmentMesher</a> extension’s Cleaver2 mesher generates such multi-material meshes.</p>

---

## Post #3 by @KKad (2020-07-27 19:47 UTC)

<p>Hello Andras,<br>
Thank you very much for the answer!<br>
Cleaver sounds like a good option, but from reading the documentation it seems that I can’t input more than 8 volumes? My geometry includes 5 materials but in the range of 50-100 or so parts/volumes.</p>
<p>Do you know if slicer offers an alternative for this sort of geometry?<br>
Thank you!</p>

---

## Post #4 by @lassoan (2020-07-27 20:18 UTC)

<p>There is no limitation on the number of volumes. Use SegmentMesher extension (which uses Cleaver2). Maybe you have found some old Cleaver extension documentation, but limitation of that is not applicable anymore.</p>

---

## Post #5 by @KKad (2020-07-27 23:16 UTC)

<p>Hi Andras,<br>
Thanks again for the clarification! I have downloaded SegmentMesher and plan to use it in the next few days on simplified datasets.</p>
<p>One question about the extension, I am correct in assuming that the label map should be labelled with the specific volume index I want? I can either label with volume index or material index (X materials, but X*10 volumes!)</p>
<p>And I checked the doc that specified a maximum limit, you are correct that it was old documentation (Slicer 4.3 to be exact.)</p>
<p>Thanks again!</p>

---

## Post #6 by @lassoan (2020-07-28 00:06 UTC)

<p>Few ten volumes should not be a problem. Few hundred is not a problem for segmentations module, hopefully it is not an issue for the mesher either. Just try things and let us know if something does not work as expected.</p>

---
