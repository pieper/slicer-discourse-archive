# Different coordinate systems when exporting stl files from 3D Slicer to matlab

**Topic ID**: 2491
**Date**: 2018-04-02
**URL**: https://discourse.slicer.org/t/different-coordinate-systems-when-exporting-stl-files-from-3d-slicer-to-matlab/2491

---

## Post #1 by @Clara_Korting (2018-04-02 10:46 UTC)

<p>Hej,</p>
<p>I am using 3D Slicer 4.8.1 to create models of muscles of the lower leg. I just stumbled upon a problem which is the following.</p>
<p>I export the models from slicer as .stl files. I then read and display those files into Matlab using the function stlread. Additionally, the images I use for creating the models contain markers. I manually read out the position of those markers using the data probe in 3D slicer. My goal is to create a plane in matlab going through the marker positions and cutting my volume as well. The plane is created in the position to be expected within matlab but the stl volume appears in a completely different position.</p>
<p>I’ve read that there were other people having problems with the coordinate system when exporting stl models but I couldn’t find out how to solve this when importing the volume into Matlab. Is there a way to maintain the slicer coordinate system when exporting the models? Or is there a transformation that can be done after exporting models to transform the model back to its slicer coordinates?</p>
<p>Thank you very much in advance!</p>
<p>Kind regards,<br>
Clara</p>

---

## Post #2 by @pieper (2018-04-02 11:59 UTC)

<p>Hi Clara -</p>
<p>This page describes the way Slicer manages coordinate systems:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>With the most recent versions of Slicer (the current nightly) there’s also an export widget that lets you chose the space for the exported models:</p>
<aside class="quote quote-modified" data-post="1" data-topic="2428">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentation directly to STL or OBJ files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We often received questions about how to export segmentation to STL file for 3D printing. We’ve added a simplified, dedicated tool to make this step easier. 
1-minute demo video: 

  <a href="https://www.youtube.com/watch?v=WfuYPVYA5cA" target="_blank" rel="noopener">
    [Export Slicer image segmentation to STL or OBJ file]
  </a>


Main features: 

Export STL file: each segment as a separate file or all segments merged into a single mesh
Export OBJ file: all segments are saved in one file, segment colors and opacities are preserved
Export all or visible segments only
Coordinate sy…
  </blockquote>
</aside>

<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @lassoan (2018-04-02 13:06 UTC)

<p>Also note that You can run your Matlab functions directly from Slicer using MatlabBridge extension:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>

---

## Post #4 by @lassoan (2018-04-02 13:41 UTC)

<p>Could you describe the end goal of your project? You may be able to do most processing in Slicer and do only you very specific processing in Matlab (or even port that to Python for completely removing dependency on proprietary software).</p>

---

## Post #5 by @Clara_Korting (2018-04-02 14:30 UTC)

<p>Thank you for all the suggestions!</p>
<p>The general aim of my project is to determine muscle parameters such as fascicle length and pennation angels from DTI data of the lower leg. For this I use DSI studio for fascicle tracking and overlay the resulting tracts with the segmented muscle models within matlab. A custom written matlab program then determines, among other things,  the correct end points of the fascicles based on their intersection with the anatomical muscle boundaries.</p>
<p>The problem I have described now is part of the project where I am trying to compare muscle parameters from US data with parameters from DTI tracking to see if DTI tracking yields reasonable results. For this markers were applied on the leg which can be seen on the MRI images. The same marker points were tracked during the US image acquisition using a vicon system. The goal is to find the intersection of the 2D ultrasound plane with the 3D muscle model. This information is then used to track fascicles in the location of the intersecting plane within the muscle to compare US parameters to DTI parameters.</p>
<p>Before using 3D Slicer my research group used the software mimics for segmentation which is why all the matlab code for transformiations between the US and MRI coordinate systems as well as muscle parameter measurements already exist. I only now realised that the stl models created by 3D slicer and displayed in matlab are in a different coordinate system than the data within 3D slicer. Using the data probe in 3DSlicer to obtain the marker positions thus can’t be used for the US to MRI coordinate transformation if the model is not in the same coordinate system.</p>
<p>Additionally, I have noticed that my data gets mirrored along the y-z plane when importing it into 3D slicer (the left leg appearing to be the right and vice versa) which might also be part of the problem. This also happens when displaying it in itk snap but not when using mricro. It’s not directly connected to my question maybe but I thought it’s worth mentioning.</p>
<p>Thanks again! Please, let me know if anything is unclear.</p>
<p>Best, Clara</p>

---

## Post #6 by @lassoan (2018-05-09 04:07 UTC)

<p>I’ve just noticed that I have written an answer a month ago but have not posted it… Here it is:</p>
<p>Thank you very much for writing about your project, it sounds very exciting.</p>
<aside class="quote no-group" data-username="Clara_Korting" data-post="5" data-topic="2491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/clara_korting/48/813_2.png" class="avatar"> Clara_Korting:</div>
<blockquote>
<p>The same marker points were tracked during the US image acquisition using a vicon system.</p>
</blockquote>
</aside>
<p>You might be interested in <a href="http://www.slicerigt.org/">SlicerIGT extension</a>, which can connect to a wide range of tracking and ultrasound imaging systems and display positions and images in real-time in Slicer, record and replay synchronized data streams, reconstruct 3D volumes from tracked 2D ultrasound, etc. It can also do ultrasound spatial calibration, automatic temporal calibration (of image and tracking data streams), and various other calibrations. We don’t support Vicon tracking systems, but instead the magnitude less expensive <a href="http://www.optitrack.com/">OptiTrack</a> - for example, an OptiTrack Duo costs $2300; and a number of medical-grade optical and electromagnetic trackers (NDI, Ascension, Claron, etc.) and other sensors - <a href="https://plustoolkit.github.io/features">see complete list here</a>.</p>
<aside class="quote no-group" data-username="Clara_Korting" data-post="5" data-topic="2491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/clara_korting/48/813_2.png" class="avatar"> Clara_Korting:</div>
<blockquote>
<p>I only now realised that the stl models created by 3D slicer and displayed in matlab are in a different coordinate system than the data within 3D slicer.</p>
</blockquote>
</aside>
<p>I think the only difference should be the LPS/RAS coordinate system switch, which you have already noticed (x and y coordinates are inverted; which corresponds to a 180-degree rotation or two mirrorings). If you notice anything else then let us know.</p>
<aside class="quote no-group" data-username="Clara_Korting" data-post="5" data-topic="2491">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/clara_korting/48/813_2.png" class="avatar"> Clara_Korting:</div>
<blockquote>
<p>Using the data probe in 3DSlicer to obtain the marker positions</p>
</blockquote>
</aside>
<p>I would not recommend to use the Data Probe for this purpose. It is difficult to get accurate 3D position just by hovering the mouse over a position then typing coordinate values. Markups module is developed for the purpose of marking landmark points in images and models. You can zoom in, adjust the position of markers in orthogonal planes, save the positions into a csv file. You can also send markup point positions directly to Matlab using MatlabBridge. Note that you can register CT to ultrasound coordinate system using Fiducial Registration Wizard module of SlicerIGT extension, which allows you to see alignment in real-time, supports rigid, affine, and warping registration, can deal with missing and arbitrarily ordered landmarks, supports data point recording directly from the tip of a tracked pointing tool.</p>

---
