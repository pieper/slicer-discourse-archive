---
topic_id: 22961
title: "How To Interpret The Getmtime Output And Write An Igs Mha Fi"
date: 2022-04-14
url: https://discourse.slicer.org/t/22961
---

# How to interpret the GetMTime() output and write an igs.mha file?

**Topic ID**: 22961
**Date**: 2022-04-14
**URL**: https://discourse.slicer.org/t/how-to-interpret-the-getmtime-output-and-write-an-igs-mha-file/22961

---

## Post #1 by @Srijeet_Chatterjee (2022-04-14 12:09 UTC)

<p>Hello everyone,</p>
<p>I am trying to use the OpenIGTLink to record frames and use detection algorithms like Aruco. Ideally I should be able to store each transformation matrix every time the frames are updated. I used the GetMTime() to obtain the modified time for logging the data.</p>
<p>I wanted to know if there’s a way to store the transformation matrices as an igs.mha file at the same time how to interpret the time stamps from the GetMTime() function for logging the data. Would be great if anyone could please share some ideas. Thank you !!</p>
<p>Best regards,<br>
Srijeet</p>

---

## Post #2 by @lassoan (2022-04-14 20:08 UTC)

<p>I think we haven’t implemented saving of recorded sequences into igs.mha/igs.nrrd file because these igs files usually store multiple sequences. However, you could very easily implement an exporter in Python: you iterate through a sequence and write out the matrices to the output igs file. The igs file is just a text file, should be no problem writing it, but if you have any questions then let us know.</p>
<aside class="quote no-group" data-username="Srijeet_Chatterjee" data-post="1" data-topic="22961">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/srijeet_chatterjee/48/12027_2.png" class="avatar"> Srijeet_Chatterjee:</div>
<blockquote>
<p>at the same time how to interpret the time stamps from the GetMTime() function for logging the data</p>
</blockquote>
</aside>
<p><code>GetMTime()</code> does not provide a physical timestamp, it is just a counter that is incremented continuously. Its only meaning is that larger value means that it happened later. Physical timestamps are recorded in the sequence nodes (in the index value). If you receive the transform from OpenIGTLink then I think you also find an absolute timestamp value in the transform node attributes.</p>

---

## Post #3 by @Srijeet_Chatterjee (2022-04-21 07:59 UTC)

<p>Thanks a lot, I could write a text file in igs format. However, getting the time stamps is still an issue. I am not receiving any transforms from the OpenIGTLink, to be specific the transforms are outputs from the Aruco library that’s needs to synch with the video time stamps from the OpenIGTLink Frames. The OpenIGTLink videos are recorded using the Plus-Server and there are time stamps for each frame saved when recording is  made. Ideally, I want to catch the same time stamps and store the values and the matrices from the Aruco library output. Just that for further use, both can be synched on the basis of time stamps.</p>

---
