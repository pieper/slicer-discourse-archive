# Fiducial RAS Coordinates to MATLAB

**Topic ID**: 12530
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/fiducial-ras-coordinates-to-matlab/12530

---

## Post #1 by @gaurav_bhide (2020-07-14 13:15 UTC)

<p>Hello,</p>
<p>OS - Windows 10<br>
Slicer Version - 4.10.2</p>
<p>I have the slicer installed with the MATLAB Bridge extension. I have my own DICOM Image that I load on the 3D slicer. Then I have placed a few fiducials.</p>
<p>I want to transfer these fiducial coordinates to MATLAB because I would like to use those coordinates. Is there a way I can transfer these fiducial coordinates to MATLAB ? Just as a variable or a vector maybe ?</p>
<p>Also for future reference, is there more help regarding this on slicer wiki ? I saw the basic matlab bridge help page but it was quite basic that way.</p>
<p>Best,<br>
Gaurav</p>

---

## Post #2 by @lassoan (2020-07-14 14:00 UTC)

<p>Several <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/Examples/">example modules</a> pass fiducials to Matlab from Slicer.</p>
<p>You can find more details in the <a href="https://www.slicer.org/w/img_auth.php/a/a7/MatlabBridgeTutorial.pdf">How to create, run, customize Matlab modules</a> tutorial on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">extension’s documentation page</a>.</p>
<p>I would recommend to move on from Matlab to Python, as Python has so many more and much better tools for medical image computing, you can implement complete application workflows (from server-side processing to end-user GUI), there are no licensing hassles, etc. I’ve implemented Slicer’s MatlabBridge extension because 5-10 years ago it still made sense to use Matlab for some problems, but nowadays it is very hard to justify choosing Matlab over Python.</p>

---

## Post #3 by @gaurav_bhide (2020-07-15 09:38 UTC)

<p>Hello Andras,</p>
<p>Thank you for your reply. My actual worry was not to pass the variables to MATLAB but rather store them in the workspace. For eg - I used the FillAroundSeeds example program to place fiducials. Now in the MATLAB script FillAroundSeeds.m, there is a specific variable called ‘seeds_LPS’ and I wanted to save this variable in my workspace.</p>
<p>Solution - Was quite easy actually. I used the MATLAB ‘save’ command and added it to the FillAroundSeeds.m file so that whenever 3D slicer runs the matlab module, I will automatically have the LPS coordinates of the fiducial saved as a data file. I can then load this into the variable space.</p>
<p>Thank you for your help!<br>
Best,<br>
Gaurav</p>
<p>PS - The reason I am using MATLAB is that I have a whole other robot kinematics related script and a few other supplementary scripts running in MATLAB. So I don’t want to change them.</p>

---
