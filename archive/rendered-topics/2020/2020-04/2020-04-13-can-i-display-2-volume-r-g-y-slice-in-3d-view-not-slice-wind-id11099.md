---
topic_id: 11099
title: "Can I Display 2 Volume R G Y Slice In 3D View Not Slice Wind"
date: 2020-04-13
url: https://discourse.slicer.org/t/11099
---

# Can I display 2 volume（R,G,Y slice） in 3d view not slice windows?

**Topic ID**: 11099
**Date**: 2020-04-13
**URL**: https://discourse.slicer.org/t/can-i-display-2-volume-r-g-y-slice-in-3d-view-not-slice-windows/11099

---

## Post #1 by @timeanddoctor (2020-04-13 12:19 UTC)

<p>Can I display 2 or more volumes（Red,Green,Yellow slice） in 3d view not slice windows?</p>

---

## Post #2 by @cpinter (2020-04-13 12:58 UTC)

<p>You can show the slices in the 3D view using the eye button in the slice view controllers.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b88b51b1eed5e77e04eab2303213c4c5c86ec49d.png" alt="image" data-base62-sha1="qkyllSXWEongWbxtczoknOcEmKx" width="179" height="84"><br>
You can show more than one volume in these the same way as in the 2D views. If you set the foreground and background, then the slices in the 3D views will show the same picture as in the 2D views but in their respective spacial locations.</p>
<p>Alternatively you can show more than one volume using volume rendering, which can be done in the Volume Rendering module by turning on visibility for more than one volume.</p>

---

## Post #3 by @timeanddoctor (2020-04-14 10:21 UTC)

<p>Thanks  cpinter.<br>
What I am doing is to display two volume (2 pictures with a long distance origin points and  no overlap) in 3d view window at the same time.<br>
for example：</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7ca1ef2df8de90adf0d4941700d581494f82af2.png" alt="image" data-base62-sha1="zm2YAqp2JFzIVzgUp1yT6QLKino" width="666" height="357"></p>

---
