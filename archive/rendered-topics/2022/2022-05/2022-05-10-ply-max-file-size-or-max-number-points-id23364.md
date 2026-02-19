---
topic_id: 23364
title: "Ply Max File Size Or Max Number Points"
date: 2022-05-10
url: https://discourse.slicer.org/t/23364
---

# PLY max file size or max number points

**Topic ID**: 23364
**Date**: 2022-05-10
**URL**: https://discourse.slicer.org/t/ply-max-file-size-or-max-number-points/23364

---

## Post #1 by @ferhue (2022-05-10 23:47 UTC)

<p>Hello,<br>
I am planning to import some large PLY files into 3D Slicer and convert them to contours on top of a CT scan.</p>
<p>I wanted to ask if there is any <code>a priori</code> limitation on the number of points or maximum file size of the PLY that can be imported. (In the sense of, the file_size is maybe stored as an integer, so maximum file size would be 4 GB. Just an example.). Or there is no real limitation apart from your max RAM memory?</p>
<p>Thanks in advance for the help.</p>

---

## Post #2 by @hherhold (2022-05-11 03:14 UTC)

<p>I guess it depends on your definition of “large”. I do micro-CT scanning of insects, and my scans tend to be fairly high resolution (relatively speaking). I routinely make models over 10 million polygons, and I’ve exported models from segmentations as large as 70 million polys. My preferred machine has 128GB of RAM, but I also use a second machine with 64GB that is quite useable (if not ideal).</p>
<p>Hope this helps.</p>

---

## Post #3 by @ferhue (2022-05-11 10:19 UTC)

<p>Thanks for the reply!<br>
I then understand that your resulting PLY file size can be close to 64 GB on your HDD, is that right.</p>
<p>My question is, if you then try to re-import that large PLY file size into 3DSlicer, does it work? Maybe it allows exporting it to PLY, but when importing, there is somewhere an overflow.</p>
<p>Best regards.</p>

---

## Post #4 by @hherhold (2022-05-11 11:00 UTC)

<p>My file with 70 million polys is 1.74GB. A 64GB PLY file would likely be massive.</p>
<p>All of my PLY files can be re-loaded into Slicer (and I do so on a regular basis), and I also use them in Blender.</p>
<p>Data size issues can sometimes be addressed by considering what questions you’re trying to answer. I <em>can</em> do a scan that is sub-micron resolution of an ant, but at tens of gigabytes of volume data, is that necessary? I’ve found that with appropriate down-sampling, cropping, and so on, I can make files that are, while still rather large, at least more manageable.</p>
<p>Hope this helps!</p>

---

## Post #5 by @ferhue (2022-05-11 11:31 UTC)

<p>Thanks!<br>
Yes, I agree that downsampling is advisable.<br>
I was just asking this because a vendor is going to provide me with some PLY files of a phantom, and he was asking me if I have any limitation on the file size, to prevent giving me files that then would crash on importing. Of course, I could do also the down-sampling later, but if I know the max-size-without-crash in advance is e.g. 2 GB, then I would tell him to not go above that, to store HDD space on first place.</p>

---

## Post #6 by @hherhold (2022-05-11 11:47 UTC)

<p>Yeah, I don’t know of any specific limits Slicer has on file sizes or numbers of polygons. I do know some applications do - ZBrush, for example, tops out at 100 million polys (discovered that when I went over).</p>

---

## Post #7 by @lassoan (2022-05-11 12:31 UTC)

<p>Slicer uses VTK to manage meshes and VTK uses 64-bit IDs to identify points and cells, which means that we can store up to 2^64 = 18 quintillion points or cells per mesh. If you want to store just the coordinates of this many points then you need minimum 100 million terabyte of RAM (but in general we recommend to have 10x more RAM than your data size).</p>
<p>Commercial software often impose hard limits on mesh size to avoid getting bad reputation and/or error reports due to slowdown, hang, or crash due to too large meshes. In Slicer we do not impose such limits, so you’ll experience slowdown, hang, or crash if you load a mesh that your computer cannot handle.</p>
<p>In summary, I can confirm what <a class="mention" href="/u/hherhold">@hherhold</a>’s described above, that mesh size is practically only limited by the amount of RAM (and computational power) of your computer.</p>

---
