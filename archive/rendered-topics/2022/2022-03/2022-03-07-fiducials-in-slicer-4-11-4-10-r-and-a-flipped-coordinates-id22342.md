---
topic_id: 22342
title: "Fiducials In Slicer 4 11 4 10 R And A Flipped Coordinates"
date: 2022-03-07
url: https://discourse.slicer.org/t/22342
---

# Fiducials in Slicer-4.11. / 4.10 "R" and "A" flipped coordinates?

**Topic ID**: 22342
**Date**: 2022-03-07
**URL**: https://discourse.slicer.org/t/fiducials-in-slicer-4-11-4-10-r-and-a-flipped-coordinates/22342

---

## Post #1 by @CST (2022-03-07 09:39 UTC)

<p>Dear all,</p>
<p>I use Slicer to create Fiducials/annotate landmarks in nifti images for a project. I have multiple computers to work on. After annotating them on computer 1 with Slicer 4.11. I open them on computer 2 with Slicer 4.10 and the points are displayed flipped. When I check the coordinates under the module Markups, they are still the same as in the fcsv file, but I noticed, that in Slicer 4.10. the A coordinates are positive when they are negative in the fcsv file and negative when they are positive in the fcsv in R and A direction.</p>
<p>my point in fcsv file:</p>
<blockquote>
<p>Markups fiducial file version = 4.11<br>
CoordinateSystem = LPS<br>
columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID<br>
1,-0.0034653465346536905,-10.54306930693069,-19.5,0,0,0,1,1,1,0,chiasma,vtkMRMLScalarVolumeNode2</p>
</blockquote>
<p>So they same fcsv file looks like this in both Slicers:</p>
<ul>
<li>Slicer 4.11:        R=   +0.003       A=   +10.5       S=   -19.5</li>
<li>Slicer 4.10. markup     R=  -0.003      A=   -10.5      S=   -19.5</li>
</ul>
<p>Is there something I do wrong? How can I create files that are the same across versions in Slicer?</p>

---

## Post #2 by @CST (2022-03-08 10:17 UTC)

<p>In case someone else will ever have this issue. Slicer 4.10. fcsv files look like this:</p>
<blockquote>
<p>Markups fiducial file version = 4.10<br>
CoordinateSystem = 0</p>
</blockquote>
<p>If I read them into Slicer 4.11. the points are were I would expect them. If I load a fcsv file created with 4.11. into 4.10. it will not take into account LPS System (?) and one has to adjust/flip the files before. The LPS Coordinate System is the one expected by ANTs/ITK so it actually saves you some time if you want to apply transfroms to the fcsv files.</p>

---

## Post #3 by @dzenanz (2022-03-08 14:29 UTC)

<p>Here is what I came up with to handle the situation. Upon reading, the coordinates are converted to LPS, unless they are already LPS:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/HASI/blob/0f50ab50d6fb532f4276ca88b244dd3c000a0155/src/hasi/mouse_femur_tibia_ct_morphometry.py#L39-L67">
  <header class="source">

      <a href="https://github.com/KitwareMedical/HASI/blob/0f50ab50d6fb532f4276ca88b244dd3c000a0155/src/hasi/mouse_femur_tibia_ct_morphometry.py#L39-L67" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/HASI/blob/0f50ab50d6fb532f4276ca88b244dd3c000a0155/src/hasi/mouse_femur_tibia_ct_morphometry.py#L39-L67" target="_blank" rel="noopener nofollow ugc">KitwareMedical/HASI/blob/0f50ab50d6fb532f4276ca88b244dd3c000a0155/src/hasi/mouse_femur_tibia_ct_morphometry.py#L39-L67</a></h4>



    <pre class="onebox">      <code class="lang-py">
        <ol class="start lines" start="39" style="counter-reset: li-counter 38 ;">
            <li>def read_slicer_fiducials(filename):</li>
            <li>    file = open(filename, 'r')</li>
            <li>    lines = file.readlines()</li>
            <li>    lines.pop(0)  # Markups fiducial file version = 4.11</li>
            <li>
            </li>
<li>    coordinate_system = lines[0][-4:-1]</li>
            <li>    if coordinate_system == 'RAS' or coordinate_system[-1:] == '0':</li>
            <li>        ras = True</li>
            <li>    elif coordinate_system == 'LPS' or coordinate_system[-1:] == '1':</li>
            <li>        ras = False</li>
            <li>    elif coordinate_system == 'IJK' or coordinate_system[-1:] == '2':</li>
            <li>        raise RuntimeError('Fiducials file with IJK coordinates is not supported')</li>
            <li>    else:</li>
            <li>        raise RuntimeError('Unrecognized coordinate system: ' + coordinate_system)</li>
            <li>
            </li>
<li>    lines.pop(0)  # CoordinateSystem = 0</li>
            <li>    lines.pop(0)  # columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID</li>
            <li>
            </li>
<li>    fiducials = []</li>
            <li>    for line in lines:</li>
        </ol>
      </code>
    </pre>


  This file has been truncated. <a href="https://github.com/KitwareMedical/HASI/blob/0f50ab50d6fb532f4276ca88b244dd3c000a0155/src/hasi/mouse_femur_tibia_ct_morphometry.py#L39-L67" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @lassoan (2022-03-09 07:04 UTC)

<p><a class="mention" href="/u/cst">@CST</a> Is there a specific reason for using a very old Slicer version? You are missing out on hundreds of fixes and new features if you use a Slicer version that was released several years ago.</p>

---
