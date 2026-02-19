---
topic_id: 8210
title: "Can Erase Segment But Not Draw"
date: 2019-08-28
url: https://discourse.slicer.org/t/8210
---

# Can erase segment but not draw

**Topic ID**: 8210
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/can-erase-segment-but-not-draw/8210

---

## Post #1 by @JoeCrozier (2019-08-28 16:49 UTC)

<p>Slicer 4.11.0<br>
Windows 10 Pro</p>
<p>Hello, hopefully this question has not been answered before.  If so, please point me in the right direction.<br>
I have a patient I am trying to create segmentation for, in order to 3d print the results.  I am working off two different MRI scans of the patient, one of these volumes is Axial, one coronal.  I created the segmentation off of the Coronal scan, like so:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/953ae22d659c02f9919c3b1fd5fb149fa24758a2.png" data-download-href="/uploads/short-url/li9iCPGkWNIsKz06mbdRM39AMym.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/953ae22d659c02f9919c3b1fd5fb149fa24758a2_2_690x322.png" alt="image" data-base62-sha1="li9iCPGkWNIsKz06mbdRM39AMym" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/953ae22d659c02f9919c3b1fd5fb149fa24758a2_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/953ae22d659c02f9919c3b1fd5fb149fa24758a2_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/953ae22d659c02f9919c3b1fd5fb149fa24758a2_2_1380x644.png 2x" data-dominant-color="7E7F86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1830×856 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But sometimes I’ll jump over to the axial view (by loading that volume) to cross reference what I’m doing.  When I’ve loaded that axial volume I have two questions:<br>
1-  It seems to get all blocky (like the below picture), anything I can do to fix that?<br>
2- I can use the “erase” segment editor tool to erase things that are clearly in the wrong spot, but if I try to “paint” a segment, it seems to only work if my paint diameter is 3% or over, if its 2% or smaller I’ll paint and nothing shows up. When I do get something to show up using the right diameter brush it seems off center of where I painted. Any ideas?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cb75663de6dae4621861bbc3918251ebeca51aa.jpeg" data-download-href="/uploads/short-url/aWF5mkiSzkwcyneQ5v3V4GVX3DQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cb75663de6dae4621861bbc3918251ebeca51aa_2_690x345.jpeg" alt="image" data-base62-sha1="aWF5mkiSzkwcyneQ5v3V4GVX3DQ" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cb75663de6dae4621861bbc3918251ebeca51aa_2_690x345.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cb75663de6dae4621861bbc3918251ebeca51aa_2_1035x517.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4cb75663de6dae4621861bbc3918251ebeca51aa_2_1380x690.jpeg 2x" data-dominant-color="898A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1731×868 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @aiden.zhu (2019-08-28 17:11 UTC)

<p>Have you tried draw a circle and then right-click mouse to accept it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5b7444291e9c505ac5be241a875d029928f6eaf.png" alt="image" data-base62-sha1="wM9ZeIwygXf2wcLntOkxDXyBwhV" width="492" height="169"></p>
<p>Or try to update the slicer to see how it goes.</p>

---

## Post #3 by @JoeCrozier (2019-08-28 17:20 UTC)

<p>That helps workaround the “not working” problem, but it still comes out blocky, see below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cc55352b7a248b059d63b210f7d57956f491ed3.png" alt="image" data-base62-sha1="8FBpNz3fEETg48oBznD9fPjEyXN" width="146" height="141"></p>

---

## Post #4 by @aiden.zhu (2019-08-28 17:26 UTC)

<p>could you check the two scans volume-info firstly to see if they are matched? When you do cross-reference, is there any resampling ?</p>

---

## Post #5 by @cpinter (2019-08-28 17:35 UTC)

<p>You selected the DWI volume as master but you’re segmenting the anatomical MRI.</p>
<p>Either create a new segment and choose the proper master, or change the geometry of the existing one (click the box icon next to the master selector and choose the MRI as reference - you can make it isotropic etc too there).</p>

---
