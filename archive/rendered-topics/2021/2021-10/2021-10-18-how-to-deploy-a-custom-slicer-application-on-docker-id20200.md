---
topic_id: 20200
title: "How To Deploy A Custom Slicer Application On Docker"
date: 2021-10-18
url: https://discourse.slicer.org/t/20200
---

# How to deploy a custom slicer application on docker?

**Topic ID**: 20200
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/how-to-deploy-a-custom-slicer-application-on-docker/20200

---

## Post #1 by @qiqi5210 (2021-10-18 07:21 UTC)

<p>Hello, everyone, slicerjupiter and slicerdocker, which I recently learned, are really good functions. I use slicerjupiter to display the main window, which will be displayed locally, but not on the web page. Running slicerdocker, the main window will be displayed on the web page. I read the information and learned that it may be related to noVNC, How can I deploy  a custom slicer application to docker and display the window on the web?</p>

---

## Post #2 by @lassoan (2021-10-19 03:43 UTC)

<p>I’ve updated the slicer-notebook docker image for the latest Slicer Preview Release. I’ve tested it locally on Windows and Linux and remotely using binder. It works very well Give it a try in your web browser now by clicking [here] (<a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master" class="inline-onebox">Binder</a>).</p>
<p>If you run Jupyter server without docker then there is no need for remote desktop access - Jupyter will start a Slicer instance locally and you can interact with it as usual. You can snap Jupyter to the left and Slicer to the right side of your screen or use two monitors to see the notebook and the Slicer GUI at the same time.</p>

---

## Post #3 by @qiqi5210 (2021-10-19 06:19 UTC)

<p>Thank you, Dr. lassoan. I still want to know what I can do to deploy a custom slicer application to docker. I know little about this and I hope you can give me a case or process. Thank you again.</p>

---

## Post #4 by @qiqi5210 (2021-10-19 10:23 UTC)

<p>I found the slicerdocker image creation file in GitHub. Can I install the slicer custom program locally during the installation step, as shown in the screenshot below? Do I have any errors in this process? Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f94ce54697588809262f5bed1e9a17ed0ff6abbb.png" data-download-href="/uploads/short-url/zzpDzkp4jI1oz4ErUb8iT97DLOb.png?dl=1" title="2021-10-19 18-21-40屏幕截图" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f94ce54697588809262f5bed1e9a17ed0ff6abbb_2_690x138.png" alt="2021-10-19 18-21-40屏幕截图" data-base62-sha1="zzpDzkp4jI1oz4ErUb8iT97DLOb" width="690" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f94ce54697588809262f5bed1e9a17ed0ff6abbb_2_690x138.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f94ce54697588809262f5bed1e9a17ed0ff6abbb_2_1035x207.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f94ce54697588809262f5bed1e9a17ed0ff6abbb.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-10-19 18-21-40屏幕截图</span><span class="informations">1265×253 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-10-19 13:54 UTC)

<p>Yes, instead of downloading the installer using curl, you can use an installer from a local folder or upload your extension to the web and update the download link.</p>
<p>You will also need SlicerJupyter extension if you want to use Slicer as a Jupyter kernel, so you need to update install.sh accordingly. Since you probably don’t want to set up an extension server, you could either get the SlicerJupyter extension package from a local folder or download it using curl.</p>

---

## Post #6 by @qiqi5210 (2021-10-19 14:14 UTC)

<p>Thanks for your help. I’ll do what you say.</p>

---

## Post #7 by @qiqi5210 (2021-10-20 07:14 UTC)

<p>Unfortunately, I made an error during the operation. I don’t know why such errors occur. I’m not very familiar with docker. Is there a problem with the dockerfile I wrote? I just added the name of the local slicer installation package, which is the Linux version installation package I downloaded from the official website, and then commented out the subsequent network downloads. Is this error because the slicer installation package has not been unzipped?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4785a4b502a8de5ec10a3aca6cf487f2d655e01b.png" data-download-href="/uploads/short-url/acIegguDVzMV9ciyh4eaM27aQif.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4785a4b502a8de5ec10a3aca6cf487f2d655e01b.png" alt="image" data-base62-sha1="acIegguDVzMV9ciyh4eaM27aQif" width="690" height="120" data-dominant-color="212020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1552×272 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14975e51fc2a97ef08d8ccacd4528f7c795f5932.png" data-download-href="/uploads/short-url/2W9QZP3bm1h27nMMrCFZFLX2bv4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14975e51fc2a97ef08d8ccacd4528f7c795f5932.png" alt="image" data-base62-sha1="2W9QZP3bm1h27nMMrCFZFLX2bv4" width="690" height="190" data-dominant-color="EAEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×233 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01184a3e43f85e7cf95ae2ead909f318caeb01a5.png" data-download-href="/uploads/short-url/9Gw9qIa6ECDvSCaMMFXWsGk7gF.png?dl=1" title="2021-10-20 151411" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01184a3e43f85e7cf95ae2ead909f318caeb01a5_2_690x168.png" alt="2021-10-20 151411" data-base62-sha1="9Gw9qIa6ECDvSCaMMFXWsGk7gF" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01184a3e43f85e7cf95ae2ead909f318caeb01a5_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01184a3e43f85e7cf95ae2ead909f318caeb01a5_2_1035x252.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01184a3e43f85e7cf95ae2ead909f318caeb01a5_2_1380x336.png 2x" data-dominant-color="2F313F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-10-20 151411</span><span class="informations">1796×438 80.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2021-10-20 14:51 UTC)

<p>The problem is that Slicer does not seem to be installed (or at least not in the expected location). Not unzipping the downloaded package would cause this. I would recommend to start from the official, working image and just change one thing at a time and then you will know exactly where things went wrong.</p>

---

## Post #9 by @muratmaga (2021-10-20 16:57 UTC)

<p>Now that Slicer is fully portable, I actually find it easier not to put the Slicer download/extract and move to the dockerfile, but place it on the host and mount it with the --volume runtime option in docker. For me, it makes life easier as it removes complexity from docker build and can incorporate changes (if necessary) more easily (no longer necessary to rebuild the docker to update the slicer version or make changes)</p>

---

## Post #10 by @lassoan (2021-10-20 18:37 UTC)

<p>I find docker essential when I need a fully self-contained image that will run on a remote system, such as binder.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> if you already have the binaries extracted on the local computer then what is the advantage of running Slicer via docker instead of running it directly?</p>

---

## Post #11 by @muratmaga (2021-10-20 21:14 UTC)

<p>Docker still provides a consistency and a virtualization for users. Regardless of what updates happen on the host (unless it is a docker specific issue), knowing that docker image will work creates a safety buffer.</p>
<p>To be sure, in the lab for ourselves we use a physical system (+virtualGL). We user docker for workshops -and hopefully soon- for external people to work on their own data.</p>
<p>Since all docker users are the same, fixing any issue for once fixes for everyone else. (I am use a sysadmin more knowledgeable than me can essentially replicate this at the host level. I just don’t have time).</p>
<p>(I never used binder, every comment I made is in context of running a host for interactive session).</p>

---

## Post #12 by @lassoan (2021-10-21 02:01 UTC)

<p>I see, thank you for the clarification, this makes sense.</p>
<p>I mostly use Windows where Slicer is very much self-contained and shared library incompatibilities are extremely rare, so it was not obvious for me how the runtime environment inside and outside docker would be different. I guess on linux things are less predictable due to the many different distros and versions.</p>

---
