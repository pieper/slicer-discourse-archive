# Creating a sequence of Volumes and labelmap overlaid

**Topic ID**: 14481
**Date**: 2020-11-07
**URL**: https://discourse.slicer.org/t/creating-a-sequence-of-volumes-and-labelmap-overlaid/14481

---

## Post #1 by @OscarD (2020-11-07 20:15 UTC)

<p>Hello, slicers!</p>
<p>Firstly, I am sorry if this is a naive question.</p>
<p>I want to create a 3-Dimensional Time Lapse of 3D volumes with label maps overlaid at each time point.</p>
<p>I have tried the following:</p>
<ul>
<li>
<p>I have a 4D (x,y,z,n frames) matrix that I converted into a .nrrd file. I can sucessfully load it into Slicer as a sequence and display a 3D+time movie for the n=50 frames</p>
</li>
<li>
<p>I have n=50 3D volumes which are label maps. These volumes are n individual .nrrd files (I can save them as.mhd files as wel) and I can load them into Slicer as labelmaps.<br>
They are named as L_frame1.nrrd … L_frame50.nrrd</p>
</li>
<li>
<p>3D volumes and each 3D volume of my 4D matrix have same size and same spacing.<br>
So if V is my 4D matrix (x,y,z,time), size(V(:,:,:,t)) = size(L_framei) and same for spacing</p>
</li>
</ul>
<p>Objectives :</p>
<ul>
<li>I would like to link each frame of the sequence to the corresponding 3D labelmap matrices.</li>
</ul>
<p>I guess, I can overlay manually each frame and each labelmap volume and record the volume rendering scene in a sequence but it will be long to do it for my 50 frames.</p>
<p>Versions</p>
<ul>
<li>Slicer : 4.11.0</li>
<li>Computer : Windows 10</li>
</ul>
<p>Thank you for your help</p>
<p>Best wishes</p>

---

## Post #2 by @lassoan (2020-11-07 20:38 UTC)

<p>You can load your individual 3D volumes into the scene and add them to a sequence in Sequences module. For 50 volumes you need to click the mouse 50 times, so it should take about 30 seconds.</p>
<p>You can write a for loop in Python to automate this but if your are new to Slicer then probably it will take tens of minutes to implement it. You can find here examples that could help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Sequences">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Sequences</a></p>

---

## Post #3 by @OscarD (2020-11-11 16:25 UTC)

<p>Great thank you ! it works</p>

---
