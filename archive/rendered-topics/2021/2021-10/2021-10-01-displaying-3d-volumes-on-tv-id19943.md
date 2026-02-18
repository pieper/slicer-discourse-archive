# Displaying 3D volumes on TV

**Topic ID**: 19943
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/displaying-3d-volumes-on-tv/19943

---

## Post #1 by @justdcinaus (2021-10-01 00:17 UTC)

<p>Good (appropriate timezone greeting) to you all.<br>
I am going to do a short one hour presentation to a team at a local hospital on 3D volume from CT studies using DICOM files and our Oculus Rift as a viewing tool.<br>
This has gone well in the past, however the limitation is that only one person at a time can get the spatial affect.<br>
So - given that I can cast to a 4K TV in our presentation room, is it possible to output in such a way that we can buy some cheap Virtual Reality glasses (either LCD or the older red/blue models) and have everyone wear them while I’m showing the models?<br>
Thanks<br>
David</p>

---

## Post #2 by @lassoan (2021-10-01 02:18 UTC)

<p>To allow an audience see what the person in the VR headset sees, we usually just enable screen mirroring in SteamVR. Then you can arrange the screen so that people can see the regular desktop 3D Slicer window and another window showing the immersive view.</p>
<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=stereo%20viewing#d-view">enable stereoscopic 3D viewing using few-dollar red-and-blue glasses</a> but that does not even come close to the immersive experience. I would not recommend demoing this very poor stereoscopic rendering mode along with virtual reality, as people might think that the two are somehow related and virtual reality is just some stereo rendering mode.</p>

---

## Post #3 by @justdcinaus (2021-10-05 01:59 UTC)

<p>Thanks Andras<br>
Agreed I’ve had good results with screen mirroring in SteamVR but as you stated not much comes close to the immersive experience.<br>
Unfortunately with a room full of staff getting everyone a chance to experience that experience is time consuming, so I was hoping for an experience that was better than screen mirroring and shareable.<br>
I’ll get myself a set of glasses and trial your suggestion of enabling stereoscopic 3D viewing.</p>

---

## Post #4 by @lassoan (2021-10-05 12:30 UTC)

<p>Showing a low-quality red-blue stereo image could make the audience lose interest. I would recommend to set aside time after your presentation to make people try it. Based on our experience with virtual reality demos:</p>
<ul>
<li>if somebody tries VR first then use it only for viewing - don’t give them controllers, just let them explore by moving their head around</li>
<li>have at least 2 people doing the demo: one dedicated to help the person wearing the headset (people can feel lost and alone when they put on the headset and need a lot of attention), another person explaining things to the people standing in line for trying it out</li>
</ul>

---
