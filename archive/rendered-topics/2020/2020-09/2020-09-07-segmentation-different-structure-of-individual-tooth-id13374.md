# segmentation different structure of individual tooth

**Topic ID**: 13374
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/segmentation-different-structure-of-individual-tooth/13374

---

## Post #1 by @HAFIZAL (2020-09-07 14:04 UTC)

<p>Hi guys, I am new with this app. I did try the watershed effect for tooth segmentation. I am going to do a research project measuring volume of the tooth. But, my area of interest is the different structure of teeth, specific to measure volume of enamel and root. I want to ask suggestion if you guys have any suggestion to segmented it. I found the enamel part (the red one) is very small and hard to detect the border. I attach with my screenshot of my area of interest. Thank you if you guys could help me.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4810e68332f7849cc66ad7d39c621202ebdb93a6.png" data-download-href="/uploads/short-url/ahwAo1WQzrh8ckM9ZxJlobHdCHY.png?dl=1" title="Screenshot (312)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4810e68332f7849cc66ad7d39c621202ebdb93a6_2_690x305.png" alt="Screenshot (312)" data-base62-sha1="ahwAo1WQzrh8ckM9ZxJlobHdCHY" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4810e68332f7849cc66ad7d39c621202ebdb93a6_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4810e68332f7849cc66ad7d39c621202ebdb93a6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4810e68332f7849cc66ad7d39c621202ebdb93a6.png 2x" data-dominant-color="424140"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (312)</span><span class="informations">894×396 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-07 15:14 UTC)

<p>To get the root volume, I would recommend to segment the entire tooth as described in these topics:</p>
<aside class="quote quote-modified" data-post="1" data-topic="9775">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/teeth-segmentaion/9775">Teeth Segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Is there a easier way of segmenting multiple  teeth easily like shown here from a CBCT ? 

  <a href="https://www.youtube.com/watch?v=MFzFKGKx29Q" target="_blank" rel="noopener">
    [3D Tooth Segmentation Tool: How to segment many teeth easily]
  </a>


I tried thresholding and grow from seed, fill between slices and filling holes and applying smoothes. 
While we can segment out single tooth after spending like 15 minutes on 1 teeth with good results  it is not easy to do this for all the teeth. Is there a easier way like as shown here in the youtube ? 
Also if someone has done tee…
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="7420">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/6de8d8/48.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/segmentation-algorithm-used-in-3d-slicer/7420">Segmentation algorithm used in 3D Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Hi, 
I’m using 3D Slicer for tooth segmentation and I’ve created an  stl model from ct scan (DICOM). 
I’ve done that using Segment editor module. 
Can someone tell me which segmentation algorithm is used in slicer to create an stl model from ct scan?
  </blockquote>
</aside>

<p>You should be able to then split the segment between the root and enamel using thresholding. If the image quality is not sufficiently good then you may need apply smoothing and/or apply manual touch-ups. You may also try Grow from seeds and Watershed effects with seeds placed in the enamel and outside.</p>
<p><a class="mention" href="/u/manjula">@manjula</a> have you tried to segment the enamel? Do you have any specific suggestions?</p>

---

## Post #3 by @manjula (2020-09-07 16:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/hafizal">@HAFIZAL</a></p>
<p>I have very limited experience in isolating teeth only. I have not tried to segment the enamel specifically but I felt i was much easier compared to roots even with thresholding.</p>
<p>The project I seek help with you before was to measure the preoperative and postoperative root resorption with the existing CBCT data.<br>
We did a few cases and we were not satisfied with the results that we were getting and we abandoned the project.  I think it was primarily due to the quality of the CBCT and what we were measuring was very small amount of resorption and reliably segmenting the root only was not very predictable.</p>
<p>From my limited experience, I feel the hardest part is separating between the root dentine/cementum with the PDL.  If we are segmenting above the alveolar bone it should be much easier just to segment out the enamel only as it is air is around it.</p>
<p>Sorry i was not been able to be much help on this.</p>

---

## Post #4 by @HAFIZAL (2020-09-08 07:20 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/manjula">@manjula</a>  for your help. I really appreciate it. I’ll try to do that. I think, I need to adjust the brightness of the image so I can see clearly the border between enamel and dentine.</p>

---

## Post #5 by @Ugi_Mikla (2020-10-03 00:48 UTC)

<p>Hi! I’ve been doing segmentation of teeth only with the thresholding and grow from seeds. I’ve not been able to distinguish cement from dentin in the images at all.(and it’s microCT), but i managed to segment enamel, dentine and pulp quite easily with the segment editor.</p>

---

## Post #6 by @lassoan (2020-10-03 02:50 UTC)

<p>It would be great if you could post a few screenshots to show what you can achieve using a microCT, and if you have any questions then let us know.</p>

---

## Post #7 by @muratmaga (2020-10-03 04:22 UTC)

<p>Yes, that will be great if you can share your workflow.</p>

---

## Post #8 by @Ugi_Mikla (2020-10-09 13:50 UTC)

<p>I have some to do next week, I will share some</p>

---

## Post #9 by @HAFIZAL (2020-10-27 15:55 UTC)

<p>Hello guys, I just want to share my result of my efforts in measuring volume of different structure of the tooth.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b696124f2886de1bb0cd2fc15ef6265b2bd07730.png" data-download-href="/uploads/short-url/q3eqqYcBrIGvaFzl37uBM3Ontde.png?dl=1" title="Screenshot (336)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b696124f2886de1bb0cd2fc15ef6265b2bd07730_2_690x387.png" alt="Screenshot (336)" data-base62-sha1="q3eqqYcBrIGvaFzl37uBM3Ontde" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b696124f2886de1bb0cd2fc15ef6265b2bd07730_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b696124f2886de1bb0cd2fc15ef6265b2bd07730_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b696124f2886de1bb0cd2fc15ef6265b2bd07730.png 2x" data-dominant-color="8C8CA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (336)</span><span class="informations">1366×768 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e6b348508020aa44b3428034edd596e4dc7de57.png" data-download-href="/uploads/short-url/6CDEh9ZVLveBTMc9xIxXH52TMiP.png?dl=1" title="Screenshot (337)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e6b348508020aa44b3428034edd596e4dc7de57_2_690x387.png" alt="Screenshot (337)" data-base62-sha1="6CDEh9ZVLveBTMc9xIxXH52TMiP" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e6b348508020aa44b3428034edd596e4dc7de57_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e6b348508020aa44b3428034edd596e4dc7de57_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e6b348508020aa44b3428034edd596e4dc7de57.png 2x" data-dominant-color="AFAEAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (337)</span><span class="informations">1366×768 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2020-10-27 16:32 UTC)

<p>Those are looking nice <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>If you want to get smoother results, you might want to increase the resolution of the segmentation compared to the CT.  Search the forum for terms like “upsample” or  “supersample” and “segmentation” for examples.  Depending on memory you might also need to use CropVolume around the tooth.</p>

---

## Post #11 by @Reham_Hassan (2020-11-10 15:07 UTC)

<p>Hi Hafizal,<br>
i would like to ask how did you reach to this result, i have a microct, and with thresholding and paint i end up with the teeth embedded partially in the bone<br>
would u please share your recipe<br>
thank u <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #12 by @Ugi_Mikla (2021-12-14 03:25 UTC)

<p>Hey guys, after some hard training in segmentation of teeth in microCT i have achieved some nice results.<br>
This is how I do It:</p>
<ol>
<li>I use thresholding for dentin</li>
<li>i use thresholding for enamel</li>
<li>I use Islands to remove voxels inmersed in tissue that doesnt correspond for each segment</li>
<li>I use smoothing &gt; closing : to fill the holes of the erased little islands</li>
<li>I use thresholding for the pulp (and that just selects the background also…but…)</li>
<li>I start to manually erase all the conections between the background and the canal system (that takes time depending on how complicated the anatomy is)</li>
</ol>
<p>Also I use some manual tools to make it look better and spend some time correcting little details,</p>
<p>I’ll see if I can post a picture here and I invite you tu share yours<br>
Also I’m open to recieve some ideas on how to improve my work.</p>
<p>Thanks, and good luck!</p>
<p>Eugenia<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea9c2a8d65eaa996d24094ad6ee26eb9311bf34.jpeg" data-download-href="/uploads/short-url/km3vFmeq54nPOJXCsS7oH7DYvOI.jpeg?dl=1" title="models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea9c2a8d65eaa996d24094ad6ee26eb9311bf34_2_690x455.jpeg" alt="models" data-base62-sha1="km3vFmeq54nPOJXCsS7oH7DYvOI" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea9c2a8d65eaa996d24094ad6ee26eb9311bf34_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ea9c2a8d65eaa996d24094ad6ee26eb9311bf34_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8ea9c2a8d65eaa996d24094ad6ee26eb9311bf34.jpeg 2x" data-dominant-color="0B0908"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">models</span><span class="informations">1377×909 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97a0ebb07c40770d49ee75961b6b2a31d913a7e9.jpeg" data-download-href="/uploads/short-url/lDmRSiNisecXYlBDs2WHffgbO4x.jpeg?dl=1" title="segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a0ebb07c40770d49ee75961b6b2a31d913a7e9_2_690x455.jpeg" alt="segmentation" data-base62-sha1="lDmRSiNisecXYlBDs2WHffgbO4x" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a0ebb07c40770d49ee75961b6b2a31d913a7e9_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97a0ebb07c40770d49ee75961b6b2a31d913a7e9_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97a0ebb07c40770d49ee75961b6b2a31d913a7e9.jpeg 2x" data-dominant-color="080809"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation</span><span class="informations">1377×909 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @muratmaga (2021-12-14 04:27 UTC)

<p>This looks real good, thanks for sharing the steps. Would be possible to share a sample data and the actual settings (e.g., threshold values), that goes with the data. How long is it taking you to do the segmentation?</p>

---

## Post #14 by @Ugi_Mikla (2021-12-14 14:46 UTC)

<p>Here I can share the acquisition and reconstruction  details: The equipment was a Bruker Skyscan 1272<br>
[Acquisition]<br>
Data Directory=D:<br>
Filename Prefix=14~01<br>
Filename Index Length=8<br>
Number Of Files=  315<br>
Number Of Rows=  672<br>
Number Of Columns= 1008<br>
Partial Width=OFF<br>
Image crop origin X=0<br>
Image crop origin Y=0<br>
Camera binning=4x4<br>
Image Rotation=-0.35000<br>
Optical Axis (line)=  300<br>
Camera to Source (mm)=273.83609<br>
Object to Source (mm)=200.89000<br>
Source Voltage (kV)=  80<br>
Source Current (uA)= 125<br>
Image Pixel Size (um)=26.413040<br>
Scaled Image Pixel Size (um)=26.413040<br>
Image Format=TIFF<br>
Depth (bits)=16<br>
Reference Intensity=57000<br>
Camera position=far<br>
Exposure (ms)=1350<br>
Rotation Step (deg)=0.600<br>
Use 360 Rotation=NO<br>
Scanning position=19.949 mm<br>
Frame Averaging=ON (1)<br>
Random Movement=ON (30)<br>
Flat Field Correction=ON<br>
Geometrical Correction=ON<br>
Filter=Al 1mm<br>
Gantry direction=CC<br>
Rotation Direction=CC<br>
Type of Detector Motion=STEP AND SHOOT<br>
Scanning Trajectory=ROUND<br>
Number Of Horizontal Offset Positions=1<br>
Number of connected scans=2<br>
Current scan number=2<br>
Number of lines to be reconstructed=503<br>
Study Date and Time=23 Sep 2020  14h:52m:29s<br>
Scan duration=0h:25m:46s<br>
Maximum vertical TS=5.0</p>
<p>[Reconstruction]<br>
Reconstruction Program=NRecon<br>
Program Version=Version: 1.7.3.1<br>
Program Home Directory=C:\SkyScan1272\SkyScan1272<br>
Reconstruction engine=GPUReconServer<br>
Engine version=Version: 1.7.3<br>
Reconstruction from batch=No<br>
Postalignment Applied=1<br>
Connected Reconstruction (parts)=2<br>
Sub-scan post alignment [0]=1.000000<br>
Sub-scan post alignment [1]=-0.500000<br>
Sub-scan scan length [0]=504<br>
Sub-scan scan length [1]=503<br>
Used extra rotation per scan(deg)= 0.000  0.000<br>
Used extra shift in X per scan(micron)= 0.000  13.629<br>
Used extra shift in Y per scan(micron)= 0.000  10.525<br>
Reconstruction servers= DESKTOP-A4MIU3L<br>
Option for additional DICOM format=ON<br>
Dataset Origin=SkyScan1272<br>
Dataset Prefix=14~01<br>
Dataset Directory=D:<br>
Output Directory=D:\Rec<br>
Time and Date=<br>
First Section=106<br>
Last Section=993<br>
Reconstruction duration per slice (seconds)=0.162376<br>
Total reconstruction time (505 slices) in seconds=82.000000<br>
Section to Section Step=1<br>
Sections Count=888<br>
Result File Type=TIF<br>
Result File Header Length (bytes)=12<br>
Result Image Width (pixels)=448<br>
Result Image Height (pixels)=416<br>
Pixel Size (um)=26.41304<br>
Reconstruction Angular Range (deg)=189.00<br>
Use 180+=OFF<br>
Angular Step (deg)=0.6000<br>
Smoothing=0<br>
Smoothing kernel=2 (Gaussian)<br>
Ring Artifact Correction=2<br>
Draw Scales=OFF<br>
Object Bigger than FOV=OFF<br>
Reconstruction from ROI=ON<br>
ROI Top (pixels)=700<br>
ROI Bottom (pixels)=284<br>
ROI Left (pixels)=208<br>
ROI Right (pixels)=658<br>
ROI reference length=1008<br>
Filter cutoff relative to Nyquist frequency=100<br>
Filter type=0<br>
Filter type description=Hamming (Alpha=0.54)<br>
Undersampling factor=1<br>
Threshold for defect pixel mask (%)=0<br>
Beam Hardening Correction (%)=30<br>
CS Static Rotation (deg)=0.00<br>
CS Static Rotation Total(deg)=0.00<br>
Minimum for CS to Image Conversion=0.000000<br>
Maximum for CS to Image Conversion=0.080086<br>
HU Calibration=ON<br>
HU Calibration scale=65535<br>
BMP LUT=0<br>
Cone-beam Angle Horiz.(deg)=7.582436<br>
Cone-beam Angle Vert.(deg)=5.059059<br>
Automatic matching in Z=50<br>
Automatic matching in X/Y=50<br>
Automatic matching in rotation=5.000000<br>
Automatic fusion=1</p>
<p>I dont think I can  share the uCT as it’s not my property, i just borrow it to learn.</p>
<p>Although it looks good I’m looking foward to improve it as I’m not yet satisfied with the results.<br>
I tried with another uCT from other teeth but they’re not always the same threshold values.<br>
In this case I got this grey values.<br>
<strong><strong>I still dont know what it means that the thresholding values are &lt;0</strong>  and if it’s necessary to change that. The gray values start from -1000.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c274ef28d0c4643432f358911dd4aaf85cebcd0.png" data-download-href="/uploads/short-url/mhoHBbZg6KxQfAprsOVGQ3bpzMs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c274ef28d0c4643432f358911dd4aaf85cebcd0_2_690x388.png" alt="image" data-base62-sha1="mhoHBbZg6KxQfAprsOVGQ3bpzMs" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c274ef28d0c4643432f358911dd4aaf85cebcd0_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c274ef28d0c4643432f358911dd4aaf85cebcd0_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c274ef28d0c4643432f358911dd4aaf85cebcd0_2_1380x776.png 2x" data-dominant-color="A4A5A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 336 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As I know nothing about programming but my aim is to create an all in one automatic segmmentation for teeth i know I still have to work a lot in it.</p>
<p>I tried using the Bruker software but it’s licensed, so I’m trying to figure out how to do it with 3dslicer so I can share with the my university community.<br>
Images obtained from CtAn Bruker are amazing, they use automatic thresholding segmentation to do it. But still, I find that the program they have to visualize 3D models quite slow and poor. Also, if you doesn’t give you the chance to save the scene, so you have to start and finish in the same session. And multirradicular teeth only can be done by generating a model for each one of the roots. The pro is that you can automate a set list of tasks and save it so it can be done automatically in a bunch of Ct’s. So you can let it running and go get some coffee.<br>
Slicer’s much better on it cause u can save unfinished work and apparently it’s full of usefull tools I still dont know how to use, hahah</p>
<p>Still dont understand, however, how with simply thresholding in CTAn they can get this amazing images as seen in Dr. Versiani’s blogspot. If it has to do with the acquisition or reconstruction parameters maybe<br>
<a href="http://rootcanalanatomy.blogspot.com/" class="onebox" target="_blank" rel="noopener nofollow ugc">http://rootcanalanatomy.blogspot.com/</a></p>
<p>That’s what I want to achieve with slicer.</p>
<p>Hope you find this useful.<br>
Keep in touch and share!</p>
<p>Rgrds!</p>

---

## Post #15 by @Ugi_Mikla (2021-12-14 14:50 UTC)

<p>The first 5 steps of the segmentation might take me 15 minutes, but then when i start manually correcting, i can be there for hours</p>

---

## Post #16 by @lassoan (2021-12-14 17:54 UTC)

<p>The image looks very noisy. Probably you can make the segmentation much easier by applying some filtering (e.g., Curveature or Gradient Anisotropic Diffusion modules, or various filters in Simple Filters module) before starting the segmentation.</p>
<p>If your only goal is visualization then you can get very high quality pictures with minimum amount of work (without any segmentation) using Volume Rendering module. However, that does not help if you need to do quantitative analysis (measure volume, etc.).</p>

---

## Post #17 by @muratmaga (2021-12-14 18:19 UTC)

<aside class="quote no-group" data-username="Ugi_Mikla" data-post="14" data-topic="13374">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ugi_mikla/48/7603_2.png" class="avatar"> Ugi_Mikla:</div>
<blockquote>
<p>Still dont understand, however, how with simply thresholding in CTAn they can get this amazing images as seen in Dr. Versiani’s blogspot. If it has to do with the acquisition or reconstruction parameters maybe</p>
</blockquote>
</aside>
<p>Based on the log file, you chose to not to do any smoothing during reconstruction. As <a class="mention" href="/u/lassoan">@lassoan</a> commented out that’s why you have such a noisy, pixelated looking dataset. I find a minimum amount of smoothing in Nrecon to be beneficial for the quality of the data. You can also do that with slicer of course.</p>
<p>Looks like you are reconstructing as DICOM and chose to use HU (hounsfield unit, <a href="https://www.ncbi.nlm.nih.gov/books/NBK547721/" class="inline-onebox">Hounsfield Unit - StatPearls - NCBI Bookshelf</a>). In that case -1000 represents density of air, 0 density of water so forth. It shouldn’t have an effect on threshold calculations. It has been a while, but as I recall the automatic thresholding tool in CTAN uses OTSU method. That algorithm is available in Slicer in the Segment Editor tool.</p>

---

## Post #18 by @Juan_Cruz_Smart_Anat (2022-02-03 04:31 UTC)

<p>Hola Ugi me gustaría hablarte de un proyecto en el cual podríamos trabajar que te parece la idea?</p>

---

## Post #19 by @Juan_Cruz_Smart_Anat (2022-02-03 04:32 UTC)

<p>Hello Ugi, I would like to tell you about a project we could work on, what do you think of the idea?</p>

---
