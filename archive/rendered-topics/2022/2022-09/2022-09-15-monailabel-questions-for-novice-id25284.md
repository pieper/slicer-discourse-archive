# MonaiLabel Questions for Novice

**Topic ID**: 25284
**Date**: 2022-09-15
**URL**: https://discourse.slicer.org/t/monailabel-questions-for-novice/25284

---

## Post #1 by @stevenagl12 (2022-09-15 21:02 UTC)

<p>This is probably a stupid question, but how do you work with Monai Label with data on your own device? Do you have to set up a dicom server like Orthanc and access it locally? Also, if you have a folder on your desktop with a bunch of nrrd files containing the segmentations how can you access those segmentations to train your model?</p>

---

## Post #2 by @muratmaga (2022-09-15 21:37 UTC)

<p>You can work on the MonaiLabel on your own, there is no requirement that the MonaiServer needs to be remote. You don’t need to to setup a DICOM server. That is pushed directly from the MonaiLabel module within Slicer via standard http protocols. Apart from making sure the Monai server is working correctly, there is nothing else. See <a href="https://github.com/Project-MONAI/MONAILabel#installation" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---

## Post #3 by @stevenagl12 (2022-09-16 13:57 UTC)

<p>I guess I am not understanding the instructions. Do you need to both install the Monai Label extension and the python package in order to run a local monai label server? Currently, when I click on the button to start the server it says:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0df87631433329bc70741f91173388cbee087e2.png" alt="image" data-base62-sha1="tNMdMcIpWg3kZsrC9a7DBcLSlp0" width="506" height="101"><br>
It also doesn’t give me any options to direct the server towards any files on my actual computer, whether they are image files or nrrd labelmaps for annotations.</p>

---

## Post #4 by @muratmaga (2022-09-16 16:40 UTC)

<p>Yes, those are two separate steps.</p>
<p>MonaiLabel extension in Slicer is technical a client to the MonaiLabel server. MonaiLabel server can be on your own machine, or on the cloud. But you have to install that, it can be a bit involved.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> created a <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.md" rel="noopener nofollow ugc">nice step-by-step instruction in the last project week</a>. You may want to try those.</p>

---

## Post #5 by @stevenagl12 (2022-09-16 17:01 UTC)

<p>Alright thank you very much.</p>

---

## Post #6 by @diazandr3s (2022-09-19 03:57 UTC)

<p>Hi <a class="mention" href="/u/stevenagl12">@stevenagl12</a>,</p>
<p>Sorry, I just saw this post. As <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned, MONAI Label can work locally as well.</p>
<p>You may find useful this video tutorial on how to install and use MONAI Label: <a href="https://www.youtube.com/watch?v=8y1OBQs2wis&amp;list=PLtoSVSQ2XzyD4lc-lAacFBzOdv5Ou-9IA" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label - Installation with PyPi, Docker, and GitHub - YouTube</a></p>
<p><code>Also, if you have a folder on your desktop with a bunch of nrrd files containing the segmentations how can you access those segmentations to train your model?</code></p>
<p>This is a very good question, if you organize the folders like this (<a href="https://youtu.be/wtiEe_jiUzg?t=3268" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label Workshop - Project Week - YouTube</a>), you could train a MONAI Label app as you wish.</p>
<p>If you have more questions related to MONAI Label, you may find the MONAI Label discussion section useful: <a href="https://github.com/Project-MONAI/MONAILabel/discussions" class="inline-onebox" rel="noopener nofollow ugc">Discussions · Project-MONAI/MONAILabel · GitHub</a></p>
<p>I hope this helps</p>

---
