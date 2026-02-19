---
topic_id: 14155
title: "3D Freehand Ultrasound Saving Data Using Sequences"
date: 2020-10-20
url: https://discourse.slicer.org/t/14155
---

# 3D freehand ultrasound - saving data using sequences

**Topic ID**: 14155
**Date**: 2020-10-20
**URL**: https://discourse.slicer.org/t/3d-freehand-ultrasound-saving-data-using-sequences/14155

---

## Post #1 by @LoganWade (2020-10-20 09:26 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2</p>
<p>Hi, I have been trying to get Slicerigt to work for a about a week now. Things are coming along slowly but I am quite confused what is the best way to save my data.</p>
<p>I am collecting position tracking data using Optitrack and streaming data using Motive (1.10.3). I am collecting Ultrasound data using Telemed (Echo Blaster 128*. I am using the 32bit Telemed version of PLUS. I am currently performing stylus calibration and temporal calibration in fcal and then performing spatial calibration in Slicer.</p>
<p>Trying to replicate the U31 tutorial I believe I need to record data for the spatial calibration using the sequence module. My issue is how is data meant to be saved? In the tutorial, the data is saved as a .mrb file. However in many other examples data appears to simply be saved as a .mha file and then imported as a sequence metafile? I would really love some clarification on what the best workflow is to collect data. Should I be saving each calibration or experimental trial as a .mrb file? Or should they be saved as .mha file? Should data instead be recorded through the Plus Remote Module and then import the .mha file at sequence metafile? I find this last one problematic because it does not appear to account for the ReferenceToRAS transform I have to include due to how Motive streams data. In the forum post ‘Use of ‘sequences’ for 3D ultrasound spatial calibration and acquisition’ by AurelieS, she mentions that she is recording live acquisitions using the model Sequences. However how is the data saved from this point?</p>
<p>Additionally, when I try to collect more than one sequence it does not appear to reset the previous sequence, instead it just adds to the previous sequence. Is this meant to function in this way? How then do you collect multiple trials?</p>
<p>The tutorials have been great but an overview of the entire process would be really helpful. So in a research setting where my standard workflow would be to set up the hardware. Perform stylus, temporal and spatial calibration. Participant arrives and then collect 8-10 trials. What would be the ideal workflow?</p>
<p>With that in mind here is where I have gotten to so far</p>
<ol>
<li>
<p><strong>Start fCal with generic configuration file (.xml)</strong></p>
</li>
<li>
<p><strong>Perform Stylus and temporal calibration in fCal</strong></p>
</li>
<li>
<p><strong>Save calibrations to a new configuration file (.xml)</strong></p>
</li>
<li>
<p><strong>Start PLUS SERVER with new configuration file</strong></p>
</li>
</ol>
<p><em>Plus Server</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73f391613e38d609ff01eb088b72a7c27a531701.png" alt="PlusServer" data-base62-sha1="gxKKyslFAVlKRytOSXRAROOZYo9" width="283" height="233"></p>
<ol start="5">
<li><strong>Open generic scene (.mrml) that has my data hierarchy already set up?</strong> (Is this bad practice?)<br>
I do this because I have to include an additional transform that accounts for motive streaming data where X axis is Anterior, Y axis is mediolateral and Z axis is vertical. Having a generic scene with a transform that swaps the X and Y axis saves me having to redo this every time</li>
</ol>
<p>*Note this generic scene does not include the transform file for StylusTipToStylus (.h5). If I have assumed this correctly, this will be obtained from the stylus calibration recorded within the new configuration file (.xml), correct?</p>
<p><em>Generic Scene</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e61f0b3e280ac0d83bb2445209a5c7b5b75288e5.png" data-download-href="/uploads/short-url/wPKkqytBy4fHn5YvyvwlYPjrgd7.png?dl=1" title="Generic Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e61f0b3e280ac0d83bb2445209a5c7b5b75288e5_2_690x321.png" alt="Generic Scene" data-base62-sha1="wPKkqytBy4fHn5YvyvwlYPjrgd7" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e61f0b3e280ac0d83bb2445209a5c7b5b75288e5_2_690x321.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e61f0b3e280ac0d83bb2445209a5c7b5b75288e5_2_1035x481.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e61f0b3e280ac0d83bb2445209a5c7b5b75288e5_2_1380x642.png 2x" data-dominant-color="9A9BB4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Generic Scene</span><span class="informations">1909×890 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>Files in Generic Scene</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68114d46f0777b96f440aa4c5275627111597644.png" data-download-href="/uploads/short-url/eQCJ0JOVYqWGzqWWSXm13hib4X2.png?dl=1" title="FileGeneric" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68114d46f0777b96f440aa4c5275627111597644_2_517x212.png" alt="FileGeneric" data-base62-sha1="eQCJ0JOVYqWGzqWWSXm13hib4X2" width="517" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68114d46f0777b96f440aa4c5275627111597644_2_517x212.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68114d46f0777b96f440aa4c5275627111597644_2_775x318.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68114d46f0777b96f440aa4c5275627111597644.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">FileGeneric</span><span class="informations">848×349 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="6">
<li><strong>Create a sequence browser node and then populate a sequence proxy node for each of my elements.</strong> I have done 4 here based on the forum post from AurelieS (Use of ‘sequences’ for 3D ultrasound spatial calibration and acquisition). Do I need another node for StylusTipToStylus?</li>
</ol>
<p><em>Sequence Setup</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a82c1bc2a715b7fe0e6aff622dc5108175ee302.png" data-download-href="/uploads/short-url/3MwyG5gs5yMWABea8QvXqulZlkK.png?dl=1" title="Sequence" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a82c1bc2a715b7fe0e6aff622dc5108175ee302.png" alt="Sequence" data-base62-sha1="3MwyG5gs5yMWABea8QvXqulZlkK" width="544" height="500" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sequence</span><span class="informations">668×613 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="7">
<li><strong>Collect data as performed in Tutorial U31 using the record button seen above and save the data.</strong><br>
How should the data be saved? I have managed to save it as a .mrb file which can then be opened for spatial calibration to be performed. Or does this need to be saved as a .mha file and if so, how is that done in slicer?<br>
The reason I am confused about this is when trying to follow Tutorial U32, on slide 3, where you create a new .mha file that includes the ImageToReference for all frames. If you save the sequence using .mrb file then you will not have the correct files for this command correct? How was ElbowUltrasoundSweep.mha saved? Was is saved using slicer or PLUS? It does not appear to have a scene attached with it so does that mean it was saved using the Plus Remote? Should I be setting up sequences and then saving the data (not sure how to do this), or should I just be using the Plus Remote record tool to create the .mha file  and then add in my ReferenceToRAS transform later?<br>
<em>Calibration</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77b69a0806737ce314783b8679039f92a62e252f.png" data-download-href="/uploads/short-url/h522yImqAQFeDFWvPT1hYDC73P1.png?dl=1" title="Calibration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77b69a0806737ce314783b8679039f92a62e252f_2_690x338.png" alt="Calibration" data-base62-sha1="h522yImqAQFeDFWvPT1hYDC73P1" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77b69a0806737ce314783b8679039f92a62e252f_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77b69a0806737ce314783b8679039f92a62e252f_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77b69a0806737ce314783b8679039f92a62e252f_2_1380x676.png 2x" data-dominant-color="74747A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Calibration</span><span class="informations">1920×943 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p><em>Save as MRB</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85d3a249f27f16cf5f53c555aca407f35361b75c.png" data-download-href="/uploads/short-url/j5SVu8XITJDlZisr571dYh1Nzsw.png?dl=1" title="MRB" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d3a249f27f16cf5f53c555aca407f35361b75c_2_690x306.png" alt="MRB" data-base62-sha1="j5SVu8XITJDlZisr571dYh1Nzsw" width="690" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d3a249f27f16cf5f53c555aca407f35361b75c_2_690x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d3a249f27f16cf5f53c555aca407f35361b75c_2_1035x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85d3a249f27f16cf5f53c555aca407f35361b75c_2_1380x612.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MRB</span><span class="informations">1752×777 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>8)<strong>Next steps are to follow U32 and U33, however as I am saving my data as .mrb I am stuck here.</strong> Next steps are to follow U32 and U33, but i ahve not been able to complete these steps due to issues saving data.<br>
U32 states that I should probably be using the 64 build of PLUS. Should I be using the 32 bit Telemed version to record and then using the 64 bit for reconstruction?<br>
*Note – link on slide 2 of U33 is broken.</p>
<p>Thanks so much for sticking this post out! Really appreciate all the work everyone has done on the software.</p>
<p>Much appreciated,</p>
<p>Logan</p>

---

## Post #2 by @Sunderlandkyl (2020-10-20 14:07 UTC)

<p>Unfortunately 3D Slicer does not save the IJKToRAS transform for recorded volume sequence, so you will lose the ImageToReference tracking information if you save a recording of Image_Reference. A workaround is to send the ImageToReference transform separately and send the image using EmbeddedTransformToFrame=“Image”. You will also have to record the ImageToReference transform. Using a scene with the transforms already set up is fine.</p>
<p>For U32 and U33, you should record/reconstruct the ultrasound entirely in Plus. The PlusRemote module in SlicerOpenIGTLink can be used to control the recording and volume reconstruction over OpenIGTLink.</p>
<p>This isn’t a part of the tutorial, but you might also be interested to know that the SlicerIGSIO extension can reconstruct volumes from a sequence or in real-time from within Slicer: <a href="https://discourse.slicer.org/t/real-time-3d-ultrasound-volume-reconstruction-using-slicerigt-extension/11197/2" class="inline-onebox">Real-time 3D ultrasound volume reconstruction using SlicerIGT extension</a></p>

---

## Post #3 by @lassoan (2020-10-20 14:48 UTC)

<p>Volume sequences in the scene <em>can</em> have varying IJKToRAS transform. However, varying IJKToRAS can be saved only in sequence bundle (.mrb) format and not in standard nrrd file format (.nrrd or .seq.nrrd). We could save into .igs.nrrd format as well, but I’m not sure how much it would help in what you want to achieve (I haven’t read the post above in detail).</p>

---

## Post #4 by @LoganWade (2020-10-21 12:28 UTC)

<p>Sorry i am not familar with what IJK is referring to? From what you have said, i need to collect data using PlusRemote which will give me a .mha file that has the sequences (ProbeToTracker, StylusToTracker, ReferenceToTracker). From this point i will need to add back in my additional transform (TrackerToRAS which switches the x and y axis). Is this correct?</p>

---
