---
topic_id: 26071
title: "Integration Of 3D Slicer In Google Cloud Shell"
date: 2022-11-04
url: https://discourse.slicer.org/t/26071
---

# Integration of 3d slicer in Google Cloud Shell

**Topic ID**: 26071
**Date**: 2022-11-04
**URL**: https://discourse.slicer.org/t/integration-of-3d-slicer-in-google-cloud-shell/26071

---

## Post #1 by @Binita_Shrestha (2022-11-04 14:24 UTC)

<p>Hi everyone,<br>
Hope everyone is doing well.<br>
I would like to know how we can run 3dslicer using docker in google platform (GCS).<br>
I have tried running docker command to run 3d slicer on google cloud shell, using command</p>
<p>docker run -p 8888:8888 -p49053:49053 -v “$PWD”:/home/sliceruser/work --rm -ti lassoan/slicer-notebook:latest<br>
and I am able to open notebook in browser with provided link.<br>
However, when I tried to create a new notebook for slicer or python by clicking on “New” and selecting “Slicer5.0”, it prompts me error saying “Cannot create a new notebook” as shown below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e968639eb179b3cfc292d7348a6eb8931b91c04c.png" data-download-href="/uploads/short-url/xiOU0lvKAtvQUa35TWh71Td12eU.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e968639eb179b3cfc292d7348a6eb8931b91c04c_2_690x283.png" alt="error" data-base62-sha1="xiOU0lvKAtvQUa35TWh71Td12eU" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e968639eb179b3cfc292d7348a6eb8931b91c04c_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e968639eb179b3cfc292d7348a6eb8931b91c04c_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e968639eb179b3cfc292d7348a6eb8931b91c04c_2_1380x566.png 2x" data-dominant-color="AFAFB1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">2993×1231 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Please do let me know, if anyone has successfully run 3d slicer in google cloud.<br>
Thanks</p>

---

## Post #2 by @pieper (2022-11-04 14:35 UTC)

<p>You can run a slicer desktop environment <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">with these instructions</a>, but you can also run a full Jupyter/Slicer stack using the instructions <a href="https://developer.nvidia.com/blog/monai-drives-medical-ai-on-google-cloud-with-medical-imaging-suite/">Google provides for their Medical Imaging Suite</a>.</p>

---

## Post #3 by @Binita_Shrestha (2022-11-07 04:30 UTC)

<p>Hi ,<br>
I tried with first option , which gives me error message as shown.<br>
Is there any steps I need to take before executing this command?<br>
And with second option of google medical imaging suite , I have tried creating jupyter notebook instance. When I launch the jupyter notebook, there is no option of slicer under new menu, from where I can launch 3d slicer.<br>
Please advise me on this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/667a6301eeef9e4055e4b2c776592d35eff0a0a5.png" data-download-href="/uploads/short-url/eCyUGTsmXaMzoiuDqo3epr2JnrD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667a6301eeef9e4055e4b2c776592d35eff0a0a5_2_690x154.png" alt="image" data-base62-sha1="eCyUGTsmXaMzoiuDqo3epr2JnrD" width="690" height="154" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667a6301eeef9e4055e4b2c776592d35eff0a0a5_2_690x154.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667a6301eeef9e4055e4b2c776592d35eff0a0a5_2_1035x231.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/667a6301eeef9e4055e4b2c776592d35eff0a0a5_2_1380x308.png 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2350×525 72.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2022-11-07 13:27 UTC)

<p>it looks like you changed the <code>--image-project</code> option to be your project, but this didn’t need to be changed since the <code>slicer</code> images are in the <code>idc-sandbox-000</code> project.  Your account’s currently configured billing project is used be default so you don’t need to put it on the command line.  Note there are some <a href="https://github.com/ImagingDataCommons/IDC-Docs/pull/48">draft instructions</a> for creating a VM without a GPU if that fits your use case (it’s much cheaper).</p>
<p>I’m not sure about the Google suite, but probably you can find support from them.  It’s brand new so I guess they’ll want feedback.</p>

---

## Post #5 by @Binita_Shrestha (2022-11-08 04:14 UTC)

<p>Thank you for the reply.<br>
Following the draft instruction of creating vm without gpu addition, the instance  is created  and running successfully<br>
When running this command,</p>
<blockquote>
<p>gcloud compute ssh ${VMNAME} – -L 6080:localhost:6080<br>
it prompts message saying “bind [::1]:6080: Cannot assign requested address” as shown in image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed043f848a3601dc3df18168d3efb9e981312338.png" data-download-href="/uploads/short-url/xOKgfifNSBU94xvB974jGTmQh0k.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed043f848a3601dc3df18168d3efb9e981312338_2_652x500.png" alt="image" data-base62-sha1="xOKgfifNSBU94xvB974jGTmQh0k" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed043f848a3601dc3df18168d3efb9e981312338_2_652x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed043f848a3601dc3df18168d3efb9e981312338_2_978x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed043f848a3601dc3df18168d3efb9e981312338_2_1304x1000.png 2x" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×1465 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>However it takes me inside vm and inside it I run all commands as shown and when I try to visit link<br>
<a href="http://localhost:6080/vnc.html?autoconnect=true" rel="noopener nofollow ugc">http://localhost:6080/vnc.html?autoconnect=true</a><br>
Its not reachable and desktop is not accessible.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/088f40b5493ec59ae5fd9e7e74840cf67f074735.png" data-download-href="/uploads/short-url/1dIJIyZKrT8OZ0uSttxFql165g1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088f40b5493ec59ae5fd9e7e74840cf67f074735_2_690x249.png" alt="image" data-base62-sha1="1dIJIyZKrT8OZ0uSttxFql165g1" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088f40b5493ec59ae5fd9e7e74840cf67f074735_2_690x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088f40b5493ec59ae5fd9e7e74840cf67f074735_2_1035x373.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/088f40b5493ec59ae5fd9e7e74840cf67f074735_2_1380x498.png 2x" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×692 51.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please let me know if I missed something.<br>
Thanks</p>

---

## Post #6 by @pieper (2022-11-08 13:57 UTC)

<p>Looks like you are close <a class="mention" href="/u/binita_shrestha">@Binita_Shrestha</a>.  When it says it cannot bind the address that usually means there’s another process using the port.  For me that happens if I have another ssh session running, maybe from an earlier login attempt or reusing the same port for a different virtual machine.  Doing <code>ps -ef | grep 6080</code> may help you identify the process and kill it, or if you aren’t familiar with that you could just reboot your local machine to clean out the old process.</p>
<p>Or you can use a different localhost port.  That is, try using <code>6081:localhost:6080</code> in the ssh command and then connect to <code>http://localhost:6081/vnc.html?autoconnect=true</code> in your local client browser.</p>

---

## Post #7 by @Binita_Shrestha (2022-11-08 22:18 UTC)

<p>Thanks Steve,<br>
Actually I tried changing the port and checked for the process used by the port 6080, but that didn’t get rid of this error.<br>
However I will try again with boot and see how it goes and let you know.<br>
Thanks</p>

---
