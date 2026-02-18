# Harden transform on large segmentation hangs 3D Slicer

**Topic ID**: 5643
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/harden-transform-on-large-segmentation-hangs-3d-slicer/5643

---

## Post #1 by @Ben_George (2019-02-05 16:13 UTC)

<p>Hi</p>
<p>I am having some problems with 3D Slicer hanging when trying to perform ‘harden transform’ on large segmentations.</p>
<p>Specifically, I have some whole body PET/CT images with associated segmentations. If I create a simple linear transformation and apply it to the CT and PET volumes and segmentation, all is fine. When I use the harden transform button, everything goes as expected for the two volumes. However, when I click it with the segmentation selected, 3D Slicer hangs and eventually needs force quitting.</p>
<p>Is there any way that I can try and debug this to determine what the issue might be? I have tried using the python interface to harden the transform, but with the same result. I’m not sure how to get any more fine-grained knowledge of what is going on under the hood.</p>
<p>This is in 3D Slicer 4.10 and 4.10.1 on MacOS.</p>
<p>Please let me know if you need any further information.</p>
<p>Ben</p>

---

## Post #2 by @cpinter (2019-02-05 16:31 UTC)

<p>Thanks for the report. Is there anything in the log? You can access application logs in About / Report an error.</p>
<p>If the log is not helpful then we’ll need an mrb scene file so that we can debug it.</p>

---

## Post #3 by @lassoan (2019-02-05 17:18 UTC)

<aside class="quote no-group" data-username="Ben_George" data-post="1" data-topic="5643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ben_george/48/2992_2.png" class="avatar"> Ben_George:</div>
<blockquote>
<p>I’m not sure how to get any more fine-grained knowledge of what is going on under the hood.</p>
</blockquote>
</aside>
<p>You can get more insight by building Slicer in debug mode and breaking the execution during the long processing. It is probably simpler to share an anonymized sample data set where we can reproduce the issue.</p>

---

## Post #4 by @Ben_George (2019-02-06 13:04 UTC)

<p>Hi</p>
<p>I can recreate the issue with the segmentation file linked below. Instructions:</p>
<ul>
<li>Load segmentation</li>
<li>Create new Linear Transform</li>
<li>Set LR shift of 5 mm (any shift causes the issue)</li>
<li>Apply the transform to the ‘13 RTSTRUCT PT_MidTreat’ node</li>
<li>Click ‘Harden Transform’ button</li>
</ul>
<p>At this stage, I get the dreaded beach ball and 3D Slicer hangs. MacOS says the application is not responding and I need for Force Quit it.</p>
<p>I have also linked to the log I get from following the above instructions.</p>
<p>I came across the issue whilst trying to use the Segmentation Registration module. However, I managed to narrow it down to a problem with this step when applied to this segmentation (and similar ones from other patients).</p>
<p>Segmentation: <a href="https://unioxfordnexus-my.sharepoint.com/:u:/g/personal/donc0432_ox_ac_uk/EeaunYq4Sx9KgA1lpcNUSAUBnC8IB4brG2v0VhsJroMWlQ?e=7MoW7c" rel="nofollow noopener">https://unioxfordnexus-my.sharepoint.com/:u:/g/personal/donc0432_ox_ac_uk/EeaunYq4Sx9KgA1lpcNUSAUBnC8IB4brG2v0VhsJroMWlQ?e=7MoW7c</a></p>
<p>Log file: <a href="https://unioxfordnexus-my.sharepoint.com/:t:/g/personal/donc0432_ox_ac_uk/ER44kqRSRKpPp0uSOga5YokBXDKYzg28DCb-6PUT-C7lZQ?e=p9xpP0" rel="nofollow noopener">https://unioxfordnexus-my.sharepoint.com/:t:/g/personal/donc0432_ox_ac_uk/ER44kqRSRKpPp0uSOga5YokBXDKYzg28DCb-6PUT-C7lZQ?e=p9xpP0</a></p>
<p>Please let me know if you need any other information.</p>
<p>Ben</p>

---

## Post #5 by @pieper (2019-02-06 13:17 UTC)

<p>Thanks for the info Ben.  One more thing you can try: since you are using a mac, you can open the Activity Monitor, select the Slicer process, and then choose the Sample Process action (from the gear shaped toolbar icon menu).  That will tell what the application is doing.</p>

---

## Post #6 by @lassoan (2019-02-06 13:35 UTC)

<p>Could you please also send the .vtp files of each segment? The attached .vtm file is just an index of which files store the segments.</p>

---

## Post #7 by @Ben_George (2019-02-06 13:57 UTC)

<p>Hi</p>
<p>Thanks for the quick reply. Below are links to:</p>
<ul>
<li>the DICOM RTSTRUCT file form which the segmentations come from. I get the same issue if I load this file and try to apply a transformation.</li>
<li>A sample process output from MacOS activity monitor</li>
</ul>
<p>RTSTRUCT: <a href="https://unioxfordnexus-my.sharepoint.com/:u:/g/personal/donc0432_ox_ac_uk/EWFRKBv6xYZLuHqmtEkvwR4Bn9vKHM0AJFlCh9wNLMHDsw?e=YQiLwa" rel="nofollow noopener">https://unioxfordnexus-my.sharepoint.com/:u:/g/personal/donc0432_ox_ac_uk/EWFRKBv6xYZLuHqmtEkvwR4Bn9vKHM0AJFlCh9wNLMHDsw?e=YQiLwa</a></p>
<p>Process sample: <a href="https://unioxfordnexus-my.sharepoint.com/:t:/g/personal/donc0432_ox_ac_uk/EfaYJcimSypKoCTDIPtZc-UBz6LFnVoR4P9pAmDbI4rbdQ?e=FyQFwy" rel="nofollow noopener">https://unioxfordnexus-my.sharepoint.com/:t:/g/personal/donc0432_ox_ac_uk/EfaYJcimSypKoCTDIPtZc-UBz6LFnVoR4P9pAmDbI4rbdQ?e=FyQFwy</a></p>
<p>Ben</p>

---

## Post #8 by @lassoan (2019-02-06 14:36 UTC)

<p>Thank you, I could reproduce the issue with the data set that you provided.</p>
<p>On my computer (4-year-old desktop i7) it takes several minutes to apply a transform, but the operation completes successfully.</p>
<p>There is probably some things that are not optimized well, because if I go to Segmentations module, make “Closed surface” the master representation then transformations are immediately completed. You can use this as a workaround for now if you don’t want to wait several minutes each time you harden the transform. I’ve added a ticket to SlicerRT to track this issue: <a href="https://github.com/SlicerRt/SlicerRT/issues/102" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/102</a></p>

---

## Post #9 by @Ben_George (2019-02-06 15:26 UTC)

<p>Thanks for looking into this for me.</p>
<p>It seems that I just wasn’t patient enough! I just tried it again and waited longer and it does (eventually) complete. It to complete it takes 5-7 minutes on my MacBook Pro.</p>
<p>Making ‘closed surface’ the master also fixes this issue for me. What is going on behind the scenes when ‘closed surface’ is made the master? I’ve not looked into what this mean until now.</p>

---

## Post #10 by @lassoan (2019-02-06 15:51 UTC)

<p>DICOM RTSTRUCT stores each segment as a set of planar contours. This representation is essentially useless for any further processing (the RT community is trying to move away from it, but there are lots of legacy systems out there, so it may take decades), so we convert it to closed surface for 3D visualization and binary labelmap for editing. All these different representations are automatically kept in sync.</p>
<p>The issue seems to be that during transformation of the planar contour representation the closed surface conversion is re-run many times. We should prevent these updates until the transformation is completed. <a class="mention" href="/u/cpinter">@cpinter</a> will probably fix this soon.</p>

---

## Post #11 by @cpinter (2019-02-06 15:59 UTC)

<p>Indeed, I will fix this in a few days. Please hang on!</p>

---

## Post #12 by @cpinter (2019-02-06 21:19 UTC)

<p><a class="mention" href="/u/ben_george">@Ben_George</a> I fixed the problem. Please try tomorrow’s nightly</p>

---
