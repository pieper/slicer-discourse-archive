---
topic_id: 2953
title: "Slicer 4 8 1 Load Fiducial File"
date: 2018-05-28
url: https://discourse.slicer.org/t/2953
---

# Slicer 4.8.1 - Load Fiducial File

**Topic ID**: 2953
**Date**: 2018-05-28
**URL**: https://discourse.slicer.org/t/slicer-4-8-1-load-fiducial-file/2953

---

## Post #1 by @Carlo (2018-05-28 18:11 UTC)

<p>Hi all,<br>
I’m a new developer in 3D Slicer and I’m practicing it. I have Ubuntu 16.04 LTS and 3D Slicer 4.8.1. I need to load a Fiducial File (.fcsv), an MRI/CT Image (.nii.gz). For this reason I go in the File -&gt; Add Data dialog and I choose the Fiducial File or the Images. The problem is that after nothing happen. Can you tell me what can be the reason?</p>
<p>PS: the Fiducial File is something like this:</p>
<p><em># Markups fiducial file version = 4.4</em><br>
<em># CoordinateSystem = 0</em><br>
<em># columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID</em><br>
<em>vtkMRMLMarkupsFiducialNode_0,-42.5917,11.5141,58.0895,0,0,0,1,1,1,0,H’,vtkMRMLScalarVolumeNode10</em><br>
<em>vtkMRMLMarkupsFiducialNode_1,7.26908,5.32096,45.9853,0,0,0,1,1,1,0,H’,vtkMRMLScalarVolumeNode10</em></p>

---

## Post #2 by @lassoan (2018-05-28 18:25 UTC)

<p>Do markup fiducial and volume nodes show up in the Data module?</p>

---

## Post #3 by @pieper (2018-05-28 18:42 UTC)

<p>Looks like you have an unpaired single quote that could cause a problem in your fcsv file (as H’ in the field before the node id)</p>
<p>Some other suggestions:</p>
<ul>
<li>check the error log after loading</li>
<li>try loading sample data, add fiducials in Slicer, then save in .nii.gz and .fcsv and confirm that you can reload correctly
<ul>
<li>check what’s different about your data from the data Slicer saves</li>
</ul>
</li>
</ul>

---

## Post #5 by @Carlo (2018-06-01 18:38 UTC)

<p>I’m not sure but I think that my Slicer installation is corrupted since I tryed to install the Slicer Windows edition in my Windows 10 partition and it works good (I can load all files whitout problem).</p>
<p>After this test I uninstalled my Slicer Linux edition (I simply removed the installation directory and then I executed the shell command “rm -f ~/.config/www.na-mic.org/” for reset the configuration). But after a new installation nothing changed.</p>

---

## Post #6 by @ihnorton (2018-06-01 19:15 UTC)

<p>Please check the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ErrorLog">error log</a>.</p>

---
