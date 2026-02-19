---
topic_id: 2789
title: "Slicer 4 8 1 Crashes Upon Loading A Volume"
date: 2018-05-09
url: https://discourse.slicer.org/t/2789
---

# Slicer 4.8.1 crashes upon loading a volume

**Topic ID**: 2789
**Date**: 2018-05-09
**URL**: https://discourse.slicer.org/t/slicer-4-8-1-crashes-upon-loading-a-volume/2789

---

## Post #1 by @zjx1805 (2018-05-09 17:42 UTC)

<p>I am having trouble loading a volume into slicer 4.8.1 on my desktop. Adding the volume through ‘Data’ module is fine and the slice views also show up correctly. However, the slicer will crash most of the time after I click the ‘Volume’ module or accessing/changing its IJKToRASMatrix through python interpreter or simply rotating the 3D rendered volume.  I am suspecting it is due to its coordinate system because</p>
<ol>
<li>In very few times where slicer did not crash after I click the ‘Volume’ module, I saw that it seems to have a LPS coordinate system, i.e., its IJKToRASMatrix is [[-0.25, 0, 0, 0], [0, -0.25, 0, 0], [0, 0, 0.25, 0], [0, 0, 0, 1]].</li>
<li>When I use the Swiss skull stripping module to extract the brain, everything is successful (i.e., it gives the correct brain mask and brain volume) but you can clearly see that the brain mask and the brain volume is in RAS coordinates (i.e., front/back, left/right are inverted w.r.t the problematic volume from the slice view)</li>
</ol>
<p>Due to the confidentiality reason I could not share this data but I could upload whatever log that might be useful in diagnosing this issue. BTW, I tested the same volume on Slicer 4.8.1 on my old laptop and it also crashes. But everthing seems to be fine on Slicer 4.9.0 nightly build (05/02) on my laptop, i.e., the crash never happens and the brain mask from skull stripping align perfectly with data volume on slice view. So it seems that it is not related to video card bug but in fact due to this problematic volume and Slicer 4.9.0 nightly build seems to have fixed this issue. However, as I mentioned in my earlier post, Slicer 4.9.0 nightly build does not display properly on my desktop and my old laptop is not powerful enough to run the analysis so I have to stick to slicer 4.8.1 on my desktop. So any help is greatly appreciated!</p>

---

## Post #2 by @lassoan (2018-05-09 17:47 UTC)

<p>There have been hundreds of fixes and improvements since 4.8.1 version, so it would be difficult to find what exactly was the issue. One possible reason can be presence of invalid values (NaN) in the volume. You may try to get rid of them by applying thresholding or some other operations that don’t change a voxels values other than the NaN values.</p>

---

## Post #3 by @zjx1805 (2018-05-09 18:02 UTC)

<p>Thank you Iassoan for such a quick reply! I checked the data using Matlab and unfortunately there is no NaN in the volume. I am wondering if Slicer keeps an internal log recording what happens just before the crash or you need the actual data to find out the reason?</p>

---

## Post #4 by @lassoan (2018-05-09 18:56 UTC)

<p>You can check what is logged in current and previous sessions in menu: Help / Report a bug, but it may or may not contain enough information. It would be more useful to attach a debugger when the crash happens to see a stack trace (which method you were in when the crash happened). However, this investigation is a waste of time in the long run, since the issue has been already fixed. It would be more beneficial to further investigate why Qt5 and VTK9 does not work on your computer. You can ask on Paraview mailing list (again, if you have asked already), try different GPU driver versions, remove the GPU or try another one, etc.</p>

---

## Post #5 by @zjx1805 (2018-05-09 20:53 UTC)

<p>Thank you for your suggestion. I have already posted the issue on Paraview forum <a href="https://www.cfd-online.com/Forums/paraview/201588-paraview-display-issue-windows.html" rel="nofollow noopener">here</a> but so far no one replies. So I guess I had to wait and hope that someday the video card driver update or windows update would magically fix this issue…</p>

---

## Post #6 by @lassoan (2018-05-09 22:16 UTC)

<p>You can post again on their mailing list every couple of days until you get answer.</p>

---

## Post #7 by @ihnorton (2018-05-10 13:37 UTC)

<p>You should probably post on the <a href="https://www.paraview.org/mailman/listinfo/paraview">Paraview mailing list</a>. I doubt any developers are active in that forum.</p>

---

## Post #8 by @zjx1805 (2018-05-10 14:43 UTC)

<p>Thank you ihnorton! I have posted the issue on their mailing list by sending the question to <a href="mailto:paraview@public.kitware.com">paraview@public.kitware.com</a>. Hopefully I would get some answers from the developers.</p>

---
