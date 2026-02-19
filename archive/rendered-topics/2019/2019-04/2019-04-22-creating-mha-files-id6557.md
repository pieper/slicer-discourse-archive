---
topic_id: 6557
title: "Creating Mha Files"
date: 2019-04-22
url: https://discourse.slicer.org/t/6557
---

# Creating .mha files 

**Topic ID**: 6557
**Date**: 2019-04-22
**URL**: https://discourse.slicer.org/t/creating-mha-files/6557

---

## Post #1 by @xaris_komninos (2019-04-22 18:50 UTC)

<p>Hi,</p>
<p>I want to reconstruct the volume of a kidney, in real time, using a sequence of 2D Ultrasound images.<br>
The 2D images are obtained by a probe and the position of the probe is given by the kinematics of the da vinci robot. How could I write the .mha files that are needed for the reconstruction?Should I use Python or Matlab, or Slicer can do it more easily?</p>
<p>Thank you for your time,<br>
Harris</p>

---

## Post #2 by @lassoan (2019-04-23 03:19 UTC)

<p>Slicer with <a href="http://www.slicerigt.org/" rel="nofollow noopener">SlicerIGT extension</a> and <a href="http://plustoolkit.org" rel="nofollow noopener">Plus toolkit</a> is very well suited for this job. They provide not just offline volume reconstruction but also real-time tracked ultrasound visualization and <a href="https://www.youtube.com/watch?v=lfZeXabDjMg" rel="nofollow noopener">live volume reconstruction</a>. Probably <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorial page</a> is a good starting point.</p>
<p>Specification of sequence metafiles that can be used by Plus toolkit’s ultrasound volume reconstructor is available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html" rel="nofollow noopener">here</a>. There are also many <a href="https://github.com/PlusToolkit/PlusLibData" rel="nofollow noopener">tracked ultrasound sequence files</a> that you can use as examples.</p>
<p>If you want to take full advantage of the platform’s real-time visualization and processing capabilities, then first, you need to get the end-effector positions from the DaVinci system as a synchronized data stream with the ultrasound image. We are helping the VISE team at Vanderbilt to get a robust and high-performance solution to this. We’ll probably revive the DaVinci interface in Plus toolkit, which will allow acquisition of tracked ultrasound data, recording to file, live volume reconstruction, and streaming to 3D Slicer for interactive visualization. I think the plan is to make all this openly available.</p>
<p>Next step is spatial calibration of the tracked ultrasound (determine transformation between the image coordinate system and the robot end effector’s coordinate system). This can be done using Plus toolkit’s fCal calibration system.</p>
<p>Inaccuracy of tool position estimation from the robot kinematics may be significant, especially when the ultrasound probe shaft bends because it gets into contact with tissue. To compensate for this error, you might want to use an external electromagnetic or optical tracker (Plus toolkit already supports this), or use endoscopic camera-based tracking (Plus toolkit already provides 2D barcode based tracking using ArUco library, which might be applicable).</p>
<p>If you could arrange a visit at Vanderbuilt or attend the <a href="https://na-mic.github.io/ProjectWeek/PW31_2019_Boston/" rel="nofollow noopener">project week in Boston</a> then probably you could learn quite quickly what’s available already and how to use them.</p>

---

## Post #3 by @xaris_komninos (2019-04-23 10:05 UTC)

<p>Thank you for your help and you guidance.<br>
As I am in London I can not attend to the project week in Boston. I will send them an email and I hope they will help me.<br>
Otherwise, do you think getting the US images and the tracked data and making the .mha or .mhd files for the volume reconstruction could be in real time?</p>

---

## Post #4 by @lassoan (2019-04-23 18:32 UTC)

<p>If you write all the frames to a file then Plus volume reconstructor will need to read the file, paste all slices into a volume, then save the result to a file. This all will probably take at least 5-10 seconds (depending a lot on how many frames do you acquire and the resolution of the output volume). If you acquire ultrasound data in Plus (or stream tracked ultrasound data to Plus in real-time) then you don’t need to write input images to file, Plus does not have to read from file, reconstruction can be done while data is acquired, so you only need to wait for writing/sending the reconstructed volume (typically does not take more than a few seconds).</p>

---

## Post #5 by @xaris_komninos (2019-04-24 10:46 UTC)

<p>Regarding the second option, how can I acquire ultrasound data in Plus? As I read, in the config file I have to set to devices: one for US images and one for the tracking data. For the device with the tracking data I will only have a sequence of  positions of the da vinci end effector. Is there a guidance on how to write this part of config file?</p>

---

## Post #6 by @lassoan (2019-04-24 23:23 UTC)

<p>Plus will support daVinci joint encoder based tracking in about a month. If you need a solution earlier then contact the Vanderbilt group.</p>

---

## Post #7 by @xaris_komninos (2019-04-26 10:00 UTC)

<p>Thank you again for all your help.</p>
<p>I will to make the reconstruction firstly online. I have one sequnce of pictures (.png format) for the ultrasound images and I want to convert them to .mha file to provide them as input in the PLUS toolkit . What do you think would be the best way?<br>
It would be better to have them in another format? I collect them via bk5000 ultrasound cart.</p>

---

## Post #8 by @lassoan (2019-04-26 12:35 UTC)

<p>You can use <a href="http://plustoolkit.org" rel="nofollow noopener">Plus toolkit</a> to acquire images directly in mha format.</p>
<p>If you have license to use the OEM interface of your bk5000 system then you may be able to acquire images directly from the BK software (see instructions <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceBkProFocus.html" rel="nofollow noopener">here</a>). If your system does not support this then you can use a framegrabbers (all devices that are compatible with Microsoft Media Foundation should work, see more information <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html" rel="nofollow noopener">here</a>).</p>

---

## Post #9 by @xaris_komninos (2019-04-26 13:24 UTC)

<p>I have collected some data, US images (png format) and positions of the end effector and I would like to reconstruct the 3D volume offline with these data. When I collected the data I didn’t know that the apropriate format is .mha and now it is not easy to collect again new data. My question is, could I convert the image and position data into .mha file to make a simulation in PLUS toolkit?</p>
<p>(I tried to convert a sequence of images in .mha via ImageJ but now I can’t combine them with the position data)</p>

---

## Post #10 by @lassoan (2019-04-26 13:39 UTC)

<aside class="quote no-group" data-username="xaris_komninos" data-post="9" data-topic="6557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xaris_komninos/48/3508_2.png" class="avatar"> xaris_komninos:</div>
<blockquote>
<p>I tried to convert a sequence of images in .mha via ImageJ but now I can’t combine them with the position data</p>
</blockquote>
</aside>
<p>That should be no problem at all. You can write the position data to a text file and copy it to the metaimage header using a text editor. If your text editor has trouble with editing a file that contains binary data then save the metaimage in mhd format (header+binary data in two separate files).</p>
<p>Alternatively, you can use <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationEditSequenceFile.html">EditSequenceFile</a> tool in Plus toolkit (included in the installation package) to add transforms from a file to an existing sequence file, using <code>MIX</code> operation.</p>

---

## Post #11 by @xaris_komninos (2019-05-16 14:34 UTC)

<p>Hi,</p>
<p>The last 20 days I was trying to synchronize the data from the da vinci and the ultrasound images and to compute the calibration matrix between  the end effector and the image. Now I would like to make the 3D reconstruction. I tried after our previous conversation to write manually the .mhd file and to make the .raw file from a sequence of images and it works.<br>
How could I write the .mhd and .raw files using  Matlab and these files to be read from Slicer3D toolkit to make the reconstruction?<br>
I read that there is a matlab function (write_mhd) and that MatlabBridge  can read files  (in nrrd format). Is this a correct way to have the 3D reconstruction or it would be better to use the source code of Slicer 3D and not the toolkit?</p>
<p>Thank you for your time.</p>

---

## Post #12 by @lassoan (2019-05-17 03:25 UTC)

<p>You can easily create mhd files in any programming language (it is just a text file) and there is a nrrd writer in MatlabBridge that you can start from.</p>
<p>If you used only Plus and Slicer for data collection and volume reconstruction then things should be much simpler and faster. DaVinci interface was just fixed up this week and it should work well now. Please discuss with the Vanderbilt team directly for details.</p>

---

## Post #13 by @xaris_komninos (2019-05-20 12:52 UTC)

<p>I sent to Vaderbili team but they did not reply to me.</p>
<p>I created the .mhd file and the coresponding .raw file and I followed the  Ultrasound Volume Reconstruction in Slicer 3D tutorial using their  configuration file. Despite the fact that I can see my US images moving in the scene (with Volume Reslice Driver) when I push the scout scan button in Plus remote, it doesn not creat the volume. It records frames but it does not show the volume. What could be the problem?</p>
<p>Thank you.</p>

---

## Post #14 by @xaris_komninos (2019-06-03 09:56 UTC)

<p>Hi,</p>
<p>I have two questions:</p>
<ol>
<li>
<p>In Plus Remote, when I put the scout scan button it creates a volume that is saved in a .mha file. When I import this file in Volume Rendering module is like parallel slices and  the volume is repeated. (Maybe because I scanned more time ). How can I visualise  the correct part of the volume?</p>
</li>
<li>
<p>I read your manuscript about the Volume reconstruction and I would like to know if there is a library that you used for the reconstruction algorithm or if you ipmlemented it from scratch.</p>
</li>
</ol>
<p>Thank you for your time,<br>
Harris</p>

---

## Post #15 by @lassoan (2019-06-04 04:03 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you advise?</p>

---

## Post #16 by @Sunderlandkyl (2019-06-04 13:17 UTC)

<p><a class="mention" href="/u/xaris_komninos">@xaris_komninos</a> have you tried using live volume reconstruction?<br>
The scout scan is mainly used to quickly identify the region of interest for use in the live volume reconstruction, which performs a more comprehensive volume reconstruction.</p>
<p>The documentation on the volume reconstructor is here: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmVolumeReconstruction.html" rel="nofollow noopener">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/AlgorithmVolumeReconstruction.html</a></p>
<p>Recently the volume reconstruction code was migrated from Plus to the IGSIO library so that it can be used in other applications (<a href="https://github.com/IGSIO/IGSIO/" rel="nofollow noopener">https://github.com/IGSIO/IGSIO/</a>)</p>

---

## Post #17 by @xaris_komninos (2019-06-04 15:50 UTC)

<p>I tried to use live volume reconstruction (after scout scan) but it doesn’t show the volume. I follow exactly the same steps as the tutorial.</p>
<p>I see that you have a ‘VolumeReconstructionTest’ project. Is this a way to set my configuration file , my tracked ultrasound images in order to get  the volume reconstruction? This volume will be visualised or saved?</p>

---

## Post #18 by @Sunderlandkyl (2019-06-04 17:27 UTC)

<p>If you have a recorded sequence from Plus, you can use the recorded volume with <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationVolumeReconstructor.html" rel="nofollow noopener">VolumeReconstructor.exe</a> in Plus ( essentially the same as VolumeReconstructionTest).</p>
<p>Can you upload your Plus log file showing the volume reconstruction?</p>

---

## Post #19 by @xaris_komninos (2019-06-04 20:36 UTC)

<p>I have only used Slicer 3D. Do you mean I have to use fCal to record the sequence and  try reconstruct the volume?</p>

---

## Post #20 by @xaris_komninos (2019-06-04 21:40 UTC)

<p>I tried again in Slicer and it works.</p>
<p>I can see the rendered volume , but how can I export this volume? The only file that I have is the .mha file from Scout Scan which is not the volume that I want to show. Can I export it in order to use in other applications or I can only visualise the volume?</p>
<p>Thanks a lot for your help!!</p>

---

## Post #21 by @Sunderlandkyl (2019-06-04 23:50 UTC)

<p>The live volume reconstruction is saved in the same directory as the scout scan. The default name in PlusRemote is: LiveReconstructedVolume.mha.</p>

---

## Post #22 by @xaris_komninos (2019-06-05 10:40 UTC)

<p>Yes I tried this. It is only a 4kB file and the when I open it in a text editor , the image part of the file is full of NULL. I tried it to load it in Slicer and to see it in volume rendering but it does not work.</p>

---

## Post #23 by @Sunderlandkyl (2019-06-05 13:22 UTC)

<p>Did you enable volume rendering in Slicer for the loaded volume?</p>
<ul>
<li>Open “Volume Rendering” module</li>
<li>Select loaded volume</li>
<li>Click on eye icon</li>
</ul>

---

## Post #24 by @xaris_komninos (2019-06-05 13:42 UTC)

<p>Yes, I did exactly this and I can not see the volume.  Maybe is a problem with the .mha file?It is very small.</p>

---

## Post #25 by @Sunderlandkyl (2019-06-05 13:44 UTC)

<p>Could you send me your Plus log?</p>

---

## Post #26 by @xaris_komninos (2019-06-05 13:54 UTC)

<p>I am trying to upload it but it says: Sorry, the file you are trying to upload is not authorized (authorized extensions: jpg, jpeg, png, gif).My file is .txt. Can I send it to you somewhere else?</p>

---

## Post #27 by @Sunderlandkyl (2019-06-05 16:19 UTC)

<p>I took a look at the files you sent me. Besides one minor comment on the config file (Compound=On, should be CompoundMode=“MEAN”/“LINEAR”/etc), there does appear to be a problem with the volume reconstruction.</p>
<p>I noticed that Plus sends/saves the correctly reconstructed volume, and then immediately overwrites it with an empty one.</p>
<p>I’ll investigate more and report back.</p>

---

## Post #28 by @xaris_komninos (2019-06-05 16:31 UTC)

<p>Thank you a lot for your help.</p>
<p>Cheers.</p>

---

## Post #29 by @Sunderlandkyl (2019-06-07 13:21 UTC)

<p>OK, I committed a fix to SlicerOpenIGTLink.Could you update and try again?</p>
<p>The fix is available both the Stable and Nightly versions.</p>

---

## Post #30 by @xaris_komninos (2019-06-07 15:05 UTC)

<p>Do you mean to download : <a href="https://github.com/openigtlink/SlicerOpenIGTLink" rel="nofollow noopener">https://github.com/openigtlink/SlicerOpenIGTLink</a> the module and somehow to use it from Slicer 3D?</p>

---

## Post #31 by @xaris_komninos (2019-06-07 15:16 UTC)

<p>I did not build Slicer from source.  Do I have to do it in order to put the updated Slicer3dIGT module?</p>

---

## Post #32 by @Sunderlandkyl (2019-06-07 15:30 UTC)

<p>No, you do not need to download it.<br>
I made the commit last night, so the fix should be available if you update your SlicerOpenIGTLink extension. (<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Updating_installed_extensions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Updating_installed_extensions</a>)</p>

---

## Post #33 by @xaris_komninos (2019-06-07 16:11 UTC)

<p>It works.Really thank you for your help!!!</p>
<p>Could I ask you some more questions?<br>
I tried IGSIO library and and the VolumeRecontructorTest project and it reconstructs the volume.</p>
<p>1)How can I render this volume in the same project? I tried the renderer of VTK and it works  but I was wondering if you use another way to render the volume instead of reading the .mha file . Or if you use a way , as in Slicer 3D, to render the volume at the same time with the reconstruction process.</p>

---

## Post #34 by @Sunderlandkyl (2019-06-07 17:22 UTC)

<p>I’m not sure I understand your question. Could you elaborate?</p>

---

## Post #35 by @xaris_komninos (2019-06-07 20:43 UTC)

<p>Sorry!</p>
<p>I used IGSIO library to reconstruct a volume because I want to make an application in cpp. Now I would like to render this volume ( .mha file). I found a way to do it using a class of vtk library which reads the .mha file and it renders it. But I would like to to avoid the "Reading " step. Is there a way to render the  “reconstructor object”?( class vtkIGSIOVolumeReconstructor)</p>
<p>I want to avoid saving the reconstructed volume and reading the volume. After the reconstruction, I want directly to render it.</p>

---

## Post #36 by @Sunderlandkyl (2019-06-10 13:17 UTC)

<p>You could use: <a href="https://github.com/IGSIO/IGSIO/blob/2658e5518dd54930a3e704a08c3962f1ee3ba530/Source/VolumeReconstruction/vtkIGSIOVolumeReconstructor.h#L82" rel="nofollow noopener">vtkIGSIOVolumeReconstructor::GetReconstructedVolume(vtkImageData* volume)</a>.</p>
<p>This should return the vtkImageData without writing it to file, so you can perform the volume rendering on that.</p>
<p><a href="https://github.com/IGSIO/SlicerIGSIO/blob/master/VolumeReconstruction/Logic/vtkSlicerVolumeReconstructionLogic.cxx" rel="nofollow noopener">The SlicerIGSIO extension does this to reconstruct volume sequences</a>.</p>

---

## Post #37 by @xaris_komninos (2019-06-11 09:53 UTC)

<p>Thank you a lot for your help and your time!</p>
<p>Cheers!</p>

---

## Post #38 by @xaris_komninos (2019-06-13 21:50 UTC)

<p>Hi,</p>
<p>I used Aruco markers in order to track the probe. I print some from : <a href="http://chev.me/arucogen/" rel="nofollow noopener">http://chev.me/arucogen/</a><br>
with dictionary 4x4. I did the data collection and I tried to detect them using the Aruco library that I found in PLUS github , but it can not detect them. I realize that it only detects classic Aruco markers and some other types. Do you know what I can do to detect aruco markers from 4x4 dictionary?</p>
<p>Thank you</p>

---

## Post #39 by @lassoan (2019-06-14 04:30 UTC)

<p>ArUco version in Plus supports 12 different dictionaries (see details and how to choose dicitionary <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceOpticalMarkerTracker.html" rel="nofollow noopener">here</a>). I’m not sure what kind of markers that online generator creates, but you can easily create a variety of markers using the <code>aruco_print_marker</code> tool bundled with Plus or just use the marker sheet that you can download from the link above.</p>

---

## Post #40 by @xaris_komninos (2019-06-19 13:23 UTC)

<p>Do you know if ARUCO library handles stereo camera ? We have a stereo camera from the da Vinci and we would like to test if we can improve the tracking using the stereo instead of use a single camera.</p>

---

## Post #41 by @lassoan (2019-06-19 14:56 UTC)

<p>Main limitation of ArUco’s tracking is inaccuracy in estimating how far is the marker from the camera, as it completely relies on measuring the marker size and so a single pixel error in marker corner estimation can lead to millimeters or centimeters of errors. With a stereo setup, you can estimate distance from triangulation instead, which should be much more accurate. Therefore, yes, I would expect that with a stereo camera you can significantly improve on ArUco’s single-camera tracking.</p>

---

## Post #42 by @ahmed_elshreif (2019-08-13 14:47 UTC)

<p>Which team in Vanderbilt?</p>

---

## Post #43 by @lassoan (2019-08-13 15:33 UTC)

<p><a href="https://engineering.vanderbilt.edu/me/faculty-staff/robert-webster.php" rel="nofollow noopener">Bob Webster</a>’s group works on <a href="http://research.vuse.vanderbilt.edu/MEDLab/research/surgical-gps" rel="nofollow noopener">developing ultrasound guidance for daVinci robot using Slicer/SlicerIGT</a> .</p>

---

## Post #44 by @xaris_komninos (2019-09-06 18:56 UTC)

<p>Hi,</p>
<p>I have 2 questions after working on IGSIO and Slicer 3D.</p>
<ol>
<li>
<p>Does the Slicer3D do an automatic scaling? From the tracker we obtain the position of the probe in meters and despite the fact that I multiply by 1000 to convert them in mm (to render the volume in Slicer), the volume appears to another part of the scene without being scaled .</p>
</li>
<li>
<p>I tried to set as ImageToProbe matrix the identity matrix but I am getting an error . I realize that the error is because it can not compute the ouput extent . Does Slicer have any limit on this ?</p>
</li>
</ol>

---

## Post #45 by @Sunderlandkyl (2019-09-06 19:20 UTC)

<ol>
<li>Where are you setting the dimensions and spacing of the image?</li>
<li>What error are you seeing?</li>
</ol>

---

## Post #46 by @xaris_komninos (2019-09-06 19:57 UTC)

<ol>
<li>In the VolumeReconstructorTest.cxx , I set for each frame the “ProbeToReference” matrix and the “ImageToProbe” is set reading the configuration file. I calculate the ProbeToReference by the tracker and  it is computed in meters. So I multiply only the translation part of this matrix with 1000.<br>
The dimensions and the spacing of the image are read in the configuration file.</li>
</ol>
<p>2.I am not getting an error. It crashes after the oupout: " Set Volume Output extent"  .<br>
As I can not use the identity matrix for the ImageToProbe , I use one matrix of your examples and it works. But it is not the transformation that I want.</p>

---

## Post #47 by @xaris_komninos (2019-09-07 17:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6c4fa525fef1338a09a679c8dd30bd722d582cf.png" data-download-href="/uploads/short-url/zd1tO36LDPj1crX9llvwAqM2Fen.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6c4fa525fef1338a09a679c8dd30bd722d582cf.png" alt="image" data-base62-sha1="zd1tO36LDPj1crX9llvwAqM2Fen" width="690" height="57" data-dominant-color="180303"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">979×81 6.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thi is the error.</p>

---

## Post #48 by @xaris_komninos (2019-09-07 19:26 UTC)

<p>I think I solved the 2nd problem. I changed the “Ouptut Space” from “0.5 0.5 0.5” to “1 1 1” and it is working.</p>
<p>Could you help me to the question 1?</p>

---

## Post #49 by @xaris_komninos (2019-09-10 09:12 UTC)

<p>Do you know the relation between mm and pixels in slicer3D?</p>

---

## Post #50 by @pieper (2019-09-10 11:22 UTC)

<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #51 by @kristjanq (2020-04-25 12:20 UTC)

<p>Related to <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationEditSequenceFile.html" rel="nofollow noopener">EditSequenceFile</a>: as we had a discourse about merging image data with transform data, this might be the option!</p>
<p>One problem: when the EditSequenceFile.exe, the window disappears within sec?!<br>
The Plus version is the latest stable version.</p>

---

## Post #52 by @jamesobutler (2020-04-25 13:08 UTC)

<p><a class="mention" href="/u/kristjanq">@kristjanq</a> I’m assuming you just double clicked on the EditSequenceFile exe? It does not have a GUI and is just a command line tool. So you should open up any terminal window and then call to run EditSequenceFile.exe followed with the appropriate command line flags.</p>

---

## Post #53 by @kristjanq (2020-04-25 13:37 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> Acctually I double-clicked the corresponding  .exe. But as you explained I had to run it through Comand Promt, it worked!</p>

---
