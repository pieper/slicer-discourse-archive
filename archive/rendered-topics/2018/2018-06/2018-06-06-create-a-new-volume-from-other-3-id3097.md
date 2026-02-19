---
topic_id: 3097
title: "Create A New Volume From Other 3"
date: 2018-06-06
url: https://discourse.slicer.org/t/3097
---

# Create a new volume from other 3 

**Topic ID**: 3097
**Date**: 2018-06-06
**URL**: https://discourse.slicer.org/t/create-a-new-volume-from-other-3/3097

---

## Post #1 by @Jeronimo_Sanchez_Sto (2018-06-06 18:34 UTC)

<p>I have 3 volumes:<br>
SAG OK<br>
AXIAL OK<br>
COR OK</p>
<p>Each one is a complete volume, but they have a better resolution only in one direction. When i render each one a full skull i shown but with awefull resolution<br>
I need to pick the Sagital part from SAG OK, the Axial part from AXIAL OK and the Coronal part from COR OK to create a new volume. How can i do it?</p>
<p>Thanks!</p>

---

## Post #2 by @fedorov (2018-06-06 19:07 UTC)

<p>This is a common question, but unfortunately there is no readily available tool or approach you could use to easily combine these three volumes into a single “super-resolution” volume.</p>
<p>See earlier related post here: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941">Combining volumes - what am I missing?</a></p>

---

## Post #3 by @cpinter (2018-06-06 19:21 UTC)

<p>A quick idea that others who are more experienced in such matters will hopefully comment:</p>
<ul>
<li>Create a volume that has the highest resolution in each axis</li>
<li>Fill in the slices from the other volumes in the proper planes</li>
<li>Use a <a href="https://github.com/PlusToolkit/PlusLib/blob/master/src/PlusVolumeReconstruction/vtkPlusFillHolesInVolume.h">fill holes filter</a> to interpolate the empty areas (the boxes between the slices)</li>
<li>Downsample as needed</li>
</ul>

---

## Post #4 by @fedorov (2018-06-06 19:43 UTC)

<p>I agree with <a class="mention" href="/u/cpinter">@cpinter</a>, there are definitely things you can do to explore. But the key issue with any of the approaches to combining those volumes into a single one will be that you will either lose the resolution (or blur your data) that you have in-plane for the individual source volumes, or you will have inconsistent resolution in different locations of the super-resolution image.</p>
<p>You can check out this survey for the intro to the topic (I didn’t read it, but I trust the authors did a good job surveying the field): <a href="https://link.springer.com/article/10.1007/s00138-014-0623-4">https://link.springer.com/article/10.1007/s00138-014-0623-4</a>. As the authors point out from the outset, “superresolution […] has been a very attractive research topic over the last two decades”, which says something on its own…</p>

---
