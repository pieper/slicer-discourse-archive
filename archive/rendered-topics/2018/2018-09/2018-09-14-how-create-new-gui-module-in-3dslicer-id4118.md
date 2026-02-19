---
topic_id: 4118
title: "How Create New Gui Module In 3Dslicer"
date: 2018-09-14
url: https://discourse.slicer.org/t/4118
---

# How create new GUI module in 3DSlicer?

**Topic ID**: 4118
**Date**: 2018-09-14
**URL**: https://discourse.slicer.org/t/how-create-new-gui-module-in-3dslicer/4118

---

## Post #1 by @shahrokh (2018-09-14 14:54 UTC)

<p>Hi dear users and developers.</p>
<p>How can I create new module for 3DSlicer?</p>
<p>I want create new module that is accessible for 3DSlicer users. This module can used in the radiotherapy research. Plastimatch is used in this module.</p>
<p>What are the steps in the process?<br>
Please guide me.<br>
Shahrokh</p>

---

## Post #2 by @timeanddoctor (2018-09-14 15:12 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Module" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Module</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules</a><br>
<a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Programming" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.8/Training#Programming</a></p>

---

## Post #3 by @pieper (2018-09-14 15:12 UTC)

<p>You can checkout this demo:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer</a></p>

---

## Post #4 by @lassoan (2018-09-14 15:15 UTC)

<aside class="quote no-group" data-username="shahrokh" data-post="1" data-topic="4118">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar"> shahrokh:</div>
<blockquote>
<p>This module can used in the radiotherapy research</p>
</blockquote>
</aside>
<p>What the module will do?</p>

---

## Post #5 by @shahrokh (2018-09-14 15:22 UTC)

<p>This module can used in the dosimetry in radiotherapy with the name of “EPID Dosimetry”. With this module, users can calculate 3D absorbed dose in CT using EPID images of water slab phantom… The results of it can compare with RTDose of TPS with SlicerRT module.</p>

---

## Post #6 by @shahrokh (2018-09-14 15:25 UTC)

<p>Also using this module,“EPID Dosimetry”, dosimetrists can do quality assurance of TPS.</p>

---

## Post #7 by @lassoan (2018-09-14 15:37 UTC)

<p>Sounds good. Note that there are extensions for TPS quality assurance using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/GelDosimetry">3D gel dosimetry</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/FilmDosimetry">film dosimetry</a> developed by <a class="mention" href="/u/cpinter">@cpinter</a>. You can start by extending or cloning&amp;modifying these extensions.</p>

---

## Post #8 by @cpinter (2018-09-14 15:58 UTC)

<p>Right. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/FilmDosimetry">Film dosimetry</a> is a working prototype for 2D dosimetry. Please check it out before starting your own module from scratch. We’re planning to improve it in the near future so if you have specific requests then we’ll take them into account as well. Thanks!</p>

---

## Post #9 by @shahrokh (2018-09-15 07:30 UTC)

<p>Dear Csaba</p>
<p>Excuse me to later reply. I hope this work will be done with your help and comments in the form of a partnership. I’m trying to prepare a flowchart including plastimatch commands and practical measurement to create a new module in order to patient dosimetry and double check TPS.</p>
<p>Thanks a lot.<br>
Shahrokh</p>

---
