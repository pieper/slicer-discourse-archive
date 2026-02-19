---
topic_id: 29718
title: "Strange Conversion Between Planer Contours To Binary Labelma"
date: 2023-05-30
url: https://discourse.slicer.org/t/29718
---

# Strange conversion between planer contours to binary labelmap

**Topic ID**: 29718
**Date**: 2023-05-30
**URL**: https://discourse.slicer.org/t/strange-conversion-between-planer-contours-to-binary-labelmap/29718

---

## Post #1 by @sotarad (2023-05-30 05:35 UTC)

<p>Hi,all.<br>
I’m troubled with converting planer contour (master) into binary lebelmap.<br>
Finally, I want to do segment registration that reflected patient’s body shrink.<br>
So, I make new segmentation that reproduced body shrink using by shrink function in segment editor.<br>
When use the function, I have to convert master into binary lebelmap.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6cf1c0d350e87bc6b6de400b53f0298d59aaf626.png" alt="image" data-base62-sha1="fxLwhA7iePQBovrEKNMvu71yqDI" width="498" height="127"></p>
<p>But, some segmaentations can’t be converted accurately like a uploaded pictures.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81f5b9fcd7e6e26ff7573755e89f7cb3229e6fd7.png" alt="Untitled" data-base62-sha1="ixG3JRc2aqFoZA35EGyfhT3chRd" width="361" height="189"></p>
<p>Could you tell me reasons for that thing and solutions.</p>

---

## Post #2 by @lassoan (2023-05-30 19:55 UTC)

<p>It looks like your input contours are messed up, but of course there is also a chance that Slicer’s contour interpolation method can be improved. What software did you use to create the contours? Can you share the DICOM RTSTRUCT file (upload somewhere and post the link here)?</p>

---

## Post #3 by @sotarad (2023-05-31 02:29 UTC)

<p>Thanks for comment, Dr.lassoan.<br>
The data what I used is Kanazawa University’s registration-based database.<br>
So, the data isn’t created by me.<br>
The open database explained that contouring data is manually segmented by radiation oncologist and software used only mentions MIM.<br>
I can send the URLs about the data, but probably you can’t view the data because the data only available in Japan and used Japan IP addres.<br>
If you could use the database, please continue to help me.<br>
database link : <a href="https://takemuralab.net/dirdb2/" rel="noopener nofollow ugc">https://takemuralab.net/dirdb2/</a><br>
paper about database : <a href="https://www.jstage.jst.go.jp/article/jjrt/76/5/76_2020_JSRT_76.5.500/_pdf" rel="noopener nofollow ugc">https://www.jstage.jst.go.jp/article/jjrt/76/5/76_2020_JSRT_76.5.500/_pdf</a><br>
patient data : H&amp;N No.6 PLAN1 in the database</p>

---

## Post #4 by @lassoan (2023-05-31 03:02 UTC)

<p>I could not register. You can upload a sample data set to somewhere (dropbox, onedrive, google drive, etc.) and post the link here.</p>

---

## Post #5 by @sotarad (2023-05-31 08:44 UTC)

<p>Thanks for trying.<br>
I’ll upload in onedrive.<br>
But my organization limit the access.<br>
If it’s not a problem, could you tell me mail addres used in onedrive to message.<br>
I’ll let you available to share.</p>

---

## Post #6 by @lassoan (2023-05-31 13:43 UTC)

<p>You can send the download link to me and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> (who will most likely to the actual investigation) as private message. You can send a private message to someone by clicking on the username and then clicking on the “Message” button.</p>

---

## Post #7 by @Sunderlandkyl (2023-06-01 02:13 UTC)

<p><a class="mention" href="/u/sotarad">@sotarad</a> I’ll investigate at the issue once you are able to send the dataset.</p>
<p>You could also try the workaround in this post: <a href="https://discourse.slicer.org/t/retrieving-statistics-from-rtstruct-and-scalar-volume-binary-labelmap-representation-computation-is-very-slow/28100/5" class="inline-onebox">Retrieving statistics from RTSTRUCT and scalar volume - binary labelmap representation computation is very slow - #5 by Sunderlandkyl</a>.</p>

---

## Post #8 by @sotarad (2023-06-02 02:13 UTC)

<p>Thank for give me an advice!<br>
I tried to make CTV segmentation to shrink after create ribbon model, but I can’t do that good.<br>
Strange line disappeared, but shrinking segmentation couldn’t be seen shrunk from master data.<br>
Is my data set bad ??</p>

---

## Post #9 by @Sunderlandkyl (2023-06-02 15:14 UTC)

<p>I’ve taken a look at the dataset, and I don’t think that it is bad.</p>
<p>I don’t see any major issues with the conversion from planar contours to closed surfaces, except that the contours are quite dense. Due to the density, triangles in the mesh are quite long and thin, which may be causing issues in the surface to labelmap conversion.</p>
<aside class="quote no-group" data-username="sotarad" data-post="8" data-topic="29718">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e47c2d/48.png" class="avatar"> sotarad:</div>
<blockquote>
<p>I tried to make CTV segmentation to shrink after create ribbon model, but I can’t do that good.<br>
Strange line disappeared, but shrinking segmentation couldn’t be seen shrunk from master data.</p>
</blockquote>
</aside>
<p>Did you make the binary labelmap into the master representation after converting from ribbon model?</p>

---

## Post #10 by @sotarad (2023-06-06 06:34 UTC)

<p>I did that again, so had successfully converted binary lebelmap exactly.<br>
Thanks for giving advices to me!!</p>

---
