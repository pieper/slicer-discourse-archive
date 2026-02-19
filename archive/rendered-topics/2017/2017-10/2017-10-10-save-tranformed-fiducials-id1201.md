---
topic_id: 1201
title: "Save Tranformed Fiducials"
date: 2017-10-10
url: https://discourse.slicer.org/t/1201
---

# Save tranformed fiducials

**Topic ID**: 1201
**Date**: 2017-10-10
**URL**: https://discourse.slicer.org/t/save-tranformed-fiducials/1201

---

## Post #1 by @hgueziri (2017-10-10 14:33 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.7.0 Nightly Build 2017-10-08<br>
Expected behavior: Save transformed coordinates of a fiducial list<br>
Actual behavior: Save untransformed coordinates of a fiducial list</p>
<p>Hi guys,<br>
I am trying to save a list of transformed fiducials in an .fcsv file. Here is what I am doing:</p>
<ul>
<li>Create a new list of fiducials named <strong>F</strong> and add markups</li>
<li>Clone <strong>F</strong> and name the new node <strong>F_transformed</strong>
</li>
<li>Create a new Linear transform <strong>T</strong> (say with a simple translation) and apply <strong>T</strong> to <strong>F_transformed</strong><br>
On 3D Slicer everything seems to work fine and the fiducials are transformed. But, when I save the fiducials in a .fcsv file and open the files, F.fcsv and F_transformed.fcsv have the exact same coordinates.</li>
</ul>
<p>Is there something I am missing on how slicer manage fcsv files?</p>
<p>Thanks,</p>

---

## Post #2 by @pieper (2017-10-10 15:08 UTC)

<p>Hi -</p>
<p>In the Transform Hierarchy tab of the Data module you can right click on F and you’ll have the option to “Harden” the transform.  This will apply the values and take the list out from the transform.  then you can save the updated values.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @hgueziri (2017-10-10 15:25 UTC)

<p>Perfect. That’s exactly what I wanted to do.</p>
<p>Thanks Steve</p>

---
