---
topic_id: 37864
title: "How To Import Stl As Ras Coordinate System"
date: 2024-08-13
url: https://discourse.slicer.org/t/37864
---

# How to import STL as RAS coordinate system?

**Topic ID**: 37864
**Date**: 2024-08-13
**URL**: https://discourse.slicer.org/t/how-to-import-stl-as-ras-coordinate-system/37864

---

## Post #1 by @calvinsuzuki (2024-08-13 23:59 UTC)

<p>When I export a CT as STL and then re-import, the X and Y end up inverted.<br>
This issue is fixed when I select the coordinate system as RAS:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08fd13eb7ce00e95b03782608ee45fb76cc523f5.png" alt="image" data-base62-sha1="1hw2gd2Z6SsMUXzQb04VvVSdbQp" width="309" height="190"><br>
But I’m looking to import this STL using a script.<br>
I want to prevent the user to do it by itself, since it will always have to select RAS.<br>
Is there a way to import STL as RAS only using script?<br>
If I use <em>loadModel</em>, it imports as LPS by default.</p>
<p>How this mentioned header works?</p>
<ul>
<li><strong>STereoLithography</strong> (.stl): Format most commonly used for 3D printing. Default coordinate system: LPS. Coordinate system (LPS/RAS) can be specified in header.</li>
</ul>

---

## Post #2 by @lassoan (2024-08-14 07:52 UTC)

<p>I would not recommend using RAS coordinate system in any files. Slicer used to do this and it led to many compatibility issues, because the medical imaging community has pretty much agreed on using LPS coordinate system and millimeters as units (probably due to DICOM standard). Instead, you can invert the sign of the first two coordinates before writing to STL to have all the coordinates in LPS.</p>
<p>If you decide to stick to RAS coordinate system anyway, then make sure to include <code>SPACE=RAS</code> in the STL file header, in the comment field. Slicer recognizes this text and will interpret the coordinates as RAS.</p>
<p>You can specify coordinate system in the model file reader or in the Models module logic <code>AddModel</code> method, but the two other solutions that I described above are better, as they avoid hardcoding uncommon data conventions in your processing workflow.</p>

---

## Post #3 by @calvinsuzuki (2024-08-15 01:52 UTC)

<p>Thanks a lot, Andras!<br>
To my case, it worked well to update the header, but I duly noted your recommendation.</p>

---
