---
topic_id: 5781
title: "3D Slicer Cloud Computing Again"
date: 2019-02-14
url: https://discourse.slicer.org/t/5781
---

# 3D Slicer + Cloud computing (again)

**Topic ID**: 5781
**Date**: 2019-02-14
**URL**: https://discourse.slicer.org/t/3d-slicer-cloud-computing-again/5781

---

## Post #1 by @gcsharp (2019-02-14 15:40 UTC)

<p>Hello Slicers,</p>
<p>I would like information on how to use 3D Slicer for visualization on a cloud platform such as Amazon AWS or Google Cloud.  This is for an educational course on medical image processing, using a cloud provider for deep learning.  If I understand correctly, one possibility is to give each student a virtual machine with OpenGL [1].  Is there any other option?</p>
<p>[1] <a href="https://discourse.slicer.org/t/want-to-use-slicer-which-is-installed-on-cloud-virtual-machine/4116" class="inline-onebox">Want to use , slicer which is installed on cloud virtual machine</a></p>

---

## Post #2 by @muratmaga (2019-02-14 16:06 UTC)

<p>We use vnc + virtualgl.<br>
<a href="https://virtualgl.org/vgldoc/2_1_1/" class="onebox" target="_blank" rel="nofollow noopener">https://virtualgl.org/vgldoc/2_1_1/</a></p>

---

## Post #3 by @pieper (2019-02-14 17:09 UTC)

<p>Hi <a class="mention" href="/u/gcsharp">@gcsharp</a> - the  <a href="https://dit4c.github.io/" rel="nofollow noopener">dit4c</a> folks in Australia set up some nice docker infrastructure for this.</p>
<p>I use their approach as the basis for my <a href="https://github.com/pieper/SlicerDockers" rel="nofollow noopener">SlicerDockers</a> which give you a full Slicer environment running in any container service.  You can even install new versions of Slicer and extensions inside the VM and all is accessible via a browser (using noVNC).  I find the performance very acceptable.</p>

---

## Post #4 by @gcsharp (2019-04-22 14:13 UTC)

<p>I now have some more information.  The class will use Google colab.</p>
<p>Could it be possible to upload the 3D Slicer jupyter kernel into Google colab?  If not, what method could you suggest for 3D visualization?  Installing local 3D Slicer is not an option.</p>

---

## Post #5 by @pieper (2019-04-22 18:36 UTC)

<p>I haven’t tried, but it looks like you could set up each user with a virtual machine running the slicer as described here under “Connecting to a runtime on a Google Compute Engine instance” at this page <a href="https://research.google.com/colaboratory/local-runtimes.html" rel="nofollow noopener">https://research.google.com/colaboratory/local-runtimes.html</a></p>

---

## Post #6 by @lassoan (2019-04-22 18:53 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Installing local 3D Slicer is not an option</p>
</blockquote>
</aside>
<p>I’m just curious, why it is not an option? Will participates use their phones and tablets? Or 32-bit Windows XP computers?</p>

---

## Post #7 by @gcsharp (2019-04-22 19:14 UTC)

<p>Thanks Steve, I will take a look.  That might work.</p>
<p>There are multiple instructors, each using different toolsets.  So the decision was made to use cloud resources with needed toolsets pre-installed.</p>

---

## Post #8 by @lassoan (2019-04-22 19:27 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="7" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>use cloud resources with needed toolsets pre-installed</p>
</blockquote>
</aside>
<p>Could Slicer be a pre-installed tool?</p>
<p>If you cannot install it then you you can run it using docker using this command <code>docker run -d -p 8080:8080 --name slicer stevepieper/slicer</code>. You can then access Slicer in your web browser by opening <code>localhost:8080</code> page clicking on the “X11 Session” button.</p>
<p>If absolutely any installation (even docker) is impossible then you can run Slicer using binder. For example, by opening this notebook: <a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master?filepath=01_Data_Loading_and_Visualization.ipynb" class="inline-onebox">Binder</a> (there are some more <a href="https://github.com/Slicer/SlicerNotebooks">here</a>)</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Would you be able to update this <a href="https://github.com/ihnorton/dockerfiles/tree/master/slicer2binder">Slicer binder dockerfile</a> to include similar VNC access as your Slicer docker images?</p>

---

## Post #9 by @gcsharp (2019-04-22 19:45 UTC)

<p>Yes, I think a VM with Slicer pre-installed would be acceptable.</p>
<p>Docker could potentially be an option.  But there would also need to be a way to get local access the output data, which is stored in Google colab/Google drive.</p>
<p>Same thing for mybinder.  How would you access the files on Google?</p>

---

## Post #10 by @fedorov (2019-04-22 20:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can run it using docker</p>
</blockquote>
</aside>
<p>The docker images would need to be downloaded, and can be very very large. Often times, even downloading Slicer binary is a hassle to plan for an event with unknown network quality, docker will be much worse. Installing docker can also be tricky.</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> - whatever you end up doing, would be really great if you could share the instructions and your experience after the event! Instructions on setting up Google Cloud VM + Colab and Slicer would be a great resource to have!</p>

---

## Post #11 by @lassoan (2019-04-22 21:12 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>event with unknown network quality</p>
</blockquote>
</aside>
<p>If the network quality is unknown then of course you cannot even consider using any cloud-based resources and you need to have all software and data locally.</p>

---

## Post #12 by @pieper (2019-04-22 21:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Would you be able to update this <a href="https://github.com/ihnorton/dockerfiles/tree/master/slicer2binder">Slicer binder dockerfile</a> to include similar VNC access as your Slicer docker images?</p>
</blockquote>
</aside>
<p>Yes, that should be doable.  But I looked around a little bit and I don’t think it can be used with google colab unless you also do an ssh tunnel on your localhost and doesn’t sound like Greg will be allowed to do that.  I didn’t see anyway to connect colab to anything but your local machine.</p>
<p>I was able to install SlicerJupyter within the dockerized Slicer for testing.  By default jupyter servers are only available on localhost, but it looks like it’s possible to configure them to be public.  So basically <a class="mention" href="/u/gcsharp">@gcsharp</a> if you wanted to take that approach we could set up a dockerfile that starts up a jupyter notebook server which could run on any container service (e.g. it’s just a few clicks on Google).  Then you would just start as many as you need and hand out IP addresses and passwords to the students.   Of course you could also let them connect to the Slicer desktop via noVNC if you want to let them use Slicer directly.</p>

---

## Post #13 by @fedorov (2019-04-22 21:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the network quality is unknown then of course you cannot even consider using any cloud-based resources and you need to have all software and data locally.</p>
</blockquote>
</aside>
<p>Not necessarily. If both your compute resources and data are on the cloud, I would actually think your network demands become a lot less stringent. I don’t think you need a high-end network to interact with a cloud-based notebook and visualize view image slices, and some summary data. Depends on what exactly the tutorial will aim to do, I guess.</p>

---

## Post #14 by @gcsharp (2019-04-22 21:25 UTC)

<p>Agree.  But I anticipate the network access will be stable.</p>
<p>FYI, this is for AAPM summer school.  Students will be doing interactive programming for deep learning, image registration, image segmentation, CAD, etc.  It’s a very ambitious program for AAPM; they have never tried something like this before.  (<a href="https://w3.aapm.org/meetings/2019SS/" rel="nofollow noopener">https://w3.aapm.org/meetings/2019SS/</a>)</p>

---

## Post #15 by @fedorov (2019-04-22 21:41 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="9" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Same thing for mybinder. How would you access the files on Google?</p>
</blockquote>
</aside>
<p>Google has all kinds of APIs, including python libraries for accessing data in their storage buckets, DICOMweb, etc. I have close to zero experience, but I know they exist, and I can look up few pointers if you cannot find. But it will be another learning curve. Maybe it is most practical to have a public shared folder on Google Drive? Wouldn’t this work?</p>

---

## Post #16 by @lassoan (2019-04-22 22:28 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="9" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>But there would also need to be a way to get local access the output data, which is stored in Google colab/Google drive. Same thing for mybinder.</p>
</blockquote>
</aside>
<p>For binder: the GitHub repository can contain all notebooks and data in the same repository and will be downloaded to the computer that runs Jupyter.</p>
<p>A downside of binder (and other free services, such as google colab) is that there is no quality of service guarantee: you cannot control how long does it take for an instance to start and your instance can be stopped anytime for any reason (the notebook will be still available in your browser, so you don’t lose your work, but you need to start a new instance, copy the saved notebook content, etc.). Usually it is not a problem, but it is a risk.</p>
<aside class="quote no-group quote-modified" data-username="gcsharp" data-post="14" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>It’s a very ambitious program for AAPM; they have never tried something like this before. (<a href="https://w3.aapm.org/meetings/2019SS/" class="inline-onebox">2019 AAPM Summer School Meeting</a>)</p>
</blockquote>
</aside>
<p>It seems that <a href="https://w3.aapm.org/meetings/2019SS/documents/packinglistSS.pdf">participants will bring their own laptop and will need to install up to 8GB of software anyway</a>, so they may just as well install Slicer locally. Things will be faster and much lower chance of things not working. You can always set up a few cloud Slicer instances (e.g., a couple of docker instances running on a few machines) just in case some people have problems on their computer.</p>

---

## Post #17 by @pieper (2019-04-23 01:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="5781">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>so they may just as well install Slicer locally. Things will be faster and much lower chance of things not working. You can always set up a few cloud Slicer instances (e.g., a couple of docker instances running on a few machines) just in case some people have problems on their computer.</p>
</blockquote>
</aside>
<p>Yes, at this point we have held probably hundreds of trainings this way and by now incompatible laptops are very rare.  But conference wifi issues are still pretty common.</p>

---
