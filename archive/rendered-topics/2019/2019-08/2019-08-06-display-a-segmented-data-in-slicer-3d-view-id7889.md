# Display a segmented data in Slicer 3D view

**Topic ID**: 7889
**Date**: 2019-08-06
**URL**: https://discourse.slicer.org/t/display-a-segmented-data-in-slicer-3d-view/7889

---

## Post #1 by @mikecsu (2019-08-06 06:39 UTC)

<p>Operating system:win 10<br>
Slicer version:4.10<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi，everyone.</p>
<p>I would like to know"  Is it possible to display a segmented data with " nrrd " format  in slicer 3D view ?“.<br>
Here " segmented data” means , it is not segmented by slicer (i didn’t use the " Segment Editor " module to do this work.)  The below pic shows how my " segmented data" looks like( i open it with ITK-SNAP):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d3e131be6910e6e403a6ac81669510138453b44.png" data-download-href="/uploads/short-url/8JM7rjHxmHSdSTDNeRAPgiMnkTq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d3e131be6910e6e403a6ac81669510138453b44.png" alt="image" data-base62-sha1="8JM7rjHxmHSdSTDNeRAPgiMnkTq" width="670" height="500" data-dominant-color="484849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">960×716 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Black pixel value   0<br>
Grey pixel value   1<br>
White pixel value   2</p>
<p>There are 3 parts  basically.</p>
<p>I noticed some differences when i do the segmentation work with slicer(using "Segment editor ")  as well as without slicer (using my own method to obtain segmented results).</p>
<p>With slicer ,  i can oabtain results with the following pic， we can see the segmented result is the “Segmentation.seg.nrrd” file and " iDose (1)  Processed-SimpleITK.nrrd"  is the voulme data.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7693441faba750d69dde25eefa2089e7259c1bae.png" alt="image" data-base62-sha1="gUXRaYGd3A5ZZfOKpGpdnnn9BHE" width="500" height="96"></p>
<p>Without slicer, i have the following files, " idose(1)-wxy.nrrd"  is the volume data , “Segment_1.nrrd” is my " segmented data".<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c9be4b60689fcd31c2bf3e87f1a2323ab260bcc.png" alt="image" data-base62-sha1="455mTnTXGcSk9FZiKByXgyY2QJC" width="501" height="59"></p>
<p>Then ,here is my question, how am i able to convert “Segment_1.nrrd”  to “Segment_1.Seg.nrrd”( i guess the data should be in “.Seg.nrrd”  format  for all the segmented data to correctly display in slicer views ），so i can display my " segmented data" correctly in slicer view.</p>
<p>Is there anything i can do to achieve this goal ?</p>
<p>Any help would be appreciated.</p>

---

## Post #2 by @lassoan (2019-08-07 03:14 UTC)

<p>You can load ITKSnap segmentation as labelmap then convert it to segmentation:</p>
<ul>
<li>Use “Add data” dialog, click on “Show options”, check “labelmap” checkbox, click OK</li>
<li>Go to “Data” module, right-click on the labelmap volume, and choose “Convert labelmap to segmentation node”</li>
</ul>
<p>Segmentation is saved as a 4D nrrd file. If your segments don’t overlap each other then you can export them as a single 3D merged labelmap and save that:</p>
<ul>
<li>Go to “Data” module, right-click on the segmentation node, and choose “Export visible segments to binary labelmap”</li>
<li>Use “Save data” to save the exported labelmap to .nrrd file</li>
</ul>

---

## Post #3 by @mikecsu (2019-08-08 03:20 UTC)

<p>Thank you  so much <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
