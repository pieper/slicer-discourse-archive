---
topic_id: 16401
title: "How To Run Slicer On The Cloud And Access In A Web Browser"
date: 2021-03-06
url: https://discourse.slicer.org/t/16401
---

# How to run Slicer on the cloud and access in a web browser

**Topic ID**: 16401
**Date**: 2021-03-06
**URL**: https://discourse.slicer.org/t/how-to-run-slicer-on-the-cloud-and-access-in-a-web-browser/16401

---

## Post #1 by @rbumm (2021-03-06 11:25 UTC)

<p>How could I not know about this Binder <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> ?? Amazing</p>

---

## Post #2 by @rbumm (2021-03-06 12:13 UTC)

<p>Would be glad if you could give a recommendation for a Slicer capable cloud provider if that is possible here … Thank you Andras</p>

---

## Post #3 by @lassoan (2021-03-06 12:50 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> what are your latest recommendations for this?</p>

---

## Post #4 by @pieper (2021-03-06 14:44 UTC)

<p>At this point I would say <a href="https://aws.amazon.com/workspaces">Amazon Workspaces</a> is the perhaps the easiest way to get a cloud installation of Slicer, although it is still very enterprise-focused, somewhat flakey, and may be expensive for routine use.  It provides a standard windows machine where you install the regular Slicer app and extensions just like you would on a local machine.  If you just boot it up when you need it (it takes several minutes longer than it should) and then shut it down when you are done it’s a very cost effective way to do things.  You still need a reasonably fast network but the interactivity is pretty good in my experience.  Amazon also has something called App Streaming, which is also windows, but without the usual desktop features, so it’s not clear how practical that will be for getting real work done.</p>
<p>Depending on your needs there are also custom virtual machine and container images <a href="https://projectweek.na-mic.org/PW34_2020_Virtual/Projects/Slicer_in_Cloud_Environments/">that are described here</a>.  Some would be better for batch processing or faster startup times.  GPU drivers in the linux VMs is a constant headache as are boot times.  Sometimes you can get a docker instance to boot within a minute, which makes it more practical for on-demand use.  On my local linux machine I can boot a docker instance of slicer almost as fast as a native executable (under 10 seconds) but the cloud providers are always slower because it seems they allocate a VM first to run the container.</p>
<p>For the SlicerMorph workshop <a class="mention" href="/u/muratmaga">@muratmaga</a> is running about 15 docker instances per-VM on Azure so that users effectively timeshare CPU and memory.  I’m curious to hear how that approach works out in practice.</p>
<p>So cloud usage of Slicer is very promising, but there are practical issues with the current options.</p>

---

## Post #5 by @muratmaga (2021-03-06 16:11 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="16401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For the SlicerMorph workshop <a class="mention" href="/u/muratmaga">@muratmaga</a> is running about 15 docker instances per-VM on Azure so that users effectively timeshare CPU and memory. I’m curious to hear how that approach works out in practice.</p>
</blockquote>
</aside>
<p>I will let you know next week <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @pieper (2021-03-06 18:35 UTC)

<p>I should say also that if you are comfortable with the cloud computing consoles you can also boot Windows VMs.  They come with server/datacenter versions of windows, sometimes very locked down by default, but with the right configuration they can feel just like a PC.  In the past I’ve been able to get Slicer and even a whole Slicer development environment installed to build from source.  But I’m biased towards linux in spite of the gpu driver issues.</p>

---

## Post #7 by @muratmaga (2021-03-08 23:45 UTC)

<p>We just finished the first day running SlicerMorph workshop on the Cloud. This note is for sharing the experience with other folks interested in running Slicer as an remote interactive desktop application (not thru Jupyter notebooks or binder).</p>
<ol>
<li>
<p>We are using this docker <a href="https://github.com/SlicerMorph/SlicerMorphCloud/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorphCloud: Docker for running SlicerMorph on Cloud</a>, which provides a simple openbox WM, with a file browser, Slicer, R/Rstudio and Firefox. (same docker can be used for GPU accelerated setups with Nvidia cards too). Docker image is huge though (about 25GB).</p>
</li>
<li>
<p>For every 10-12 students, we have spun a HB120rs_v2 node on Azure (480GB of RAM, 120 non-threaded cores. No GPU. About $3.5/h). Each node also have a 1.2TB persistent storage as their work area and workshops data.</p>
</li>
<li>
<p>We spun individual containers for every attendee. Every user gets a one-time use password and a unique URL (both of which unfortunately changes if have to restart their instance).</p>
</li>
<li>
<p>They use Firefox installed inside the docker to bring data in (e.g., from MorphoSource or from their dropbox account).</p>
</li>
<li>
<p>In my experience, dedicated TurboVNC clients gives a much more interactive experience then noVNC running in a web browser (both in terms of bandwidth usage and image quality).</p>
</li>
<li>
<p>User experience is highly dependent on their bandwidth and connection quality (for example for me it is as good as being in the lab that use LAN settings). We could have improved this a bit more by spinning nodes in other geographical areas and cluster the people accordingly. Next round we might do that. And if users are beyond firewall, ephemeral tcp ports we use sometimes are blocked and unfortunately that’s not something we can do about (apart from finding a better solution for having distinct accounts for everyone).</p>
</li>
</ol>
<p>Today, out of ~40 users only 1-2 needed their docker instance restarted (which is mostly due to a design issue where if you exit out of the WM session by choosing Exit from window manager’s popup menu, it kills the VNC session. We need to remove that menu). And I ran my entire tutorial (~4h) using only the cloud instance.</p>
<p>But right now usage is lightweight. Tomorrow is segmentation and we will see if we encounter any more issues.</p>
<p>Overall, we managed to cover the materials much faster, because we didn’t get bogged down strange OS specific issues (locales, folders with non-ascii characters, desktops hijacked by cloud file share, missing libraries) that we had to troubleshoot over zoom connection.  To be clear, these issues continue to happen on desktops (as we encourage them to have a local computer as a backup) but didn’t take it away from workshop time.</p>
<p>Overall, the experience can be improved with more careful planning (this was our first attempt, so we are also learnign). But Slicer on the cloud as an interactive application, is a very real thing.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>CONTAINER</th>
<th>NAME</th>
<th>CPU</th>
<th>%</th>
<th>MEM</th>
<th>USAGE</th>
<th>/</th>
<th>LIMIT</th>
<th>MEM</th>
<th>%</th>
<th>NET</th>
<th>I/O</th>
<th>BLOCK</th>
</tr>
</thead>
<tbody>
<tr>
<td>04fe810bc45c</td>
<td>0.01%</td>
<td>1.162GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.16%</td>
<td>423MB</td>
<td>/</td>
<td>3.08GB</td>
<td>778MB</td>
<td>/</td>
<td>401MB</td>
<td>118</td>
</tr>
<tr>
<td>7367b651ded8</td>
<td>0.07%</td>
<td>5.619GiB</td>
<td>/</td>
<td>100GiB</td>
<td>5.62%</td>
<td>3.08GB</td>
<td>/</td>
<td>4.26GB</td>
<td>17.3MB</td>
<td>/</td>
<td>309MB</td>
<td>727</td>
</tr>
<tr>
<td>9a29d3cc4f67</td>
<td>0.00%</td>
<td>56.1MiB</td>
<td>/</td>
<td>100GiB</td>
<td>0.05%</td>
<td>60.8kB</td>
<td>/</td>
<td>691kB</td>
<td>41kB</td>
<td>/</td>
<td>0B</td>
<td>55</td>
</tr>
<tr>
<td>3bb70ca00cb0</td>
<td>0.05%</td>
<td>1.025GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.02%</td>
<td>75.7MB</td>
<td>/</td>
<td>572MB</td>
<td>222MB</td>
<td>/</td>
<td>67.8MB</td>
<td>130</td>
</tr>
<tr>
<td>850f145587ea</td>
<td>0.09%</td>
<td>886.3MiB</td>
<td>/</td>
<td>100GiB</td>
<td>0.87%</td>
<td>443MB</td>
<td>/</td>
<td>806MB</td>
<td>10.8MB</td>
<td>/</td>
<td>416MB</td>
<td>302</td>
</tr>
<tr>
<td>545cc4fcb27c</td>
<td>0.09%</td>
<td>1.004GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.00%</td>
<td>36.8MB</td>
<td>/</td>
<td>42.8MB</td>
<td>11.5MB</td>
<td>/</td>
<td>86.8MB</td>
<td>236</td>
</tr>
<tr>
<td>307d4b87f8ea</td>
<td>0.05%</td>
<td>3.378GiB</td>
<td>/</td>
<td>100GiB</td>
<td>3.38%</td>
<td>1.5GB</td>
<td>/</td>
<td>2.18GB</td>
<td>239MB</td>
<td>/</td>
<td>493MB</td>
<td>546</td>
</tr>
<tr>
<td>065a1b06903c</td>
<td>5.33%</td>
<td>1.902GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.90%</td>
<td>1.97GB</td>
<td>/</td>
<td>2.65GB</td>
<td>17.1MB</td>
<td>/</td>
<td>508MB</td>
<td>649</td>
</tr>
<tr>
<td>8e674178b5d7</td>
<td>0.06%</td>
<td>3.557GiB</td>
<td>/</td>
<td>100GiB</td>
<td>3.56%</td>
<td>544MB</td>
<td>/</td>
<td>3.46GB</td>
<td>12.7MB</td>
<td>/</td>
<td>289MB</td>
<td>361</td>
</tr>
<tr>
<td>234ae464a44f</td>
<td>0.05%</td>
<td>1.376GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.38%</td>
<td>3.25GB</td>
<td>/</td>
<td>978MB</td>
<td>4.72GB</td>
<td>/</td>
<td>303MB</td>
<td>275</td>
</tr>
<tr>
<td>ccd3167e3bbd</td>
<td>2.32%</td>
<td>1.489GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.49%</td>
<td>482MB</td>
<td>/</td>
<td>1.48GB</td>
<td>24.3MB</td>
<td>/</td>
<td>174MB</td>
<td>512</td>
</tr>
<tr>
<td>baa4337b35ca</td>
<td>0.05%</td>
<td>1.321GiB</td>
<td>/</td>
<td>100GiB</td>
<td>1.32%</td>
<td>425MB</td>
<td>/</td>
<td>1.33GB</td>
<td>568MB</td>
<td>/</td>
<td>343MB</td>
<td>278</td>
</tr>
</tbody>
</table>
</div>

---

## Post #8 by @pieper (2021-03-08 23:53 UTC)

<p>Very useful to know - thanks for the detailed report and glad you know the workshop went so well.</p>

---

## Post #9 by @mau_igna_06 (2021-11-17 14:30 UTC)

<p>Hi. First of all: thank you very much to the creators of <a href="https://github.com/SlicerMorph/SlicerMorphCloud/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorphCloud: Docker for running SlicerMorph on Cloud</a></p>
<p>I corrected the download links of the dockerfile and edited the nogpu.sh file here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/mauigna06/SlicerMorphCloud/tree/succesfulBuildDockerImage">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/mauigna06/SlicerMorphCloud/tree/succesfulBuildDockerImage" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/mauigna06/SlicerMorphCloud/tree/succesfulBuildDockerImage" target="_blank" rel="noopener nofollow ugc">GitHub - mauigna06/SlicerMorphCloud at succesfulBuildDockerImage</a></h3>

  <p><a href="https://github.com/mauigna06/SlicerMorphCloud/tree/succesfulBuildDockerImage" target="_blank" rel="noopener nofollow ugc">succesfulBuildDockerImage</a></p>

  <p><span class="label1">Docker for running SlicerMorph on Cloud. Contribute to mauigna06/SlicerMorphCloud development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>So now it builds successfully.</p>
<p>Following the instructions of README.md I created a container for one user executing:<br>
<code>for user in $(cat users); do ./nogpu.sh $user ; done &gt; instance-table.csv</code></p>
<p>When I access the link given to me I get the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f915b144df20b9f78dfcd5a983c32efe05707b25.png" data-download-href="/uploads/short-url/zxvmGY4NWOi69eLRuGXt53QceQl.png?dl=1" title="Captura de pantalla de 2021-11-17 04-49-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f915b144df20b9f78dfcd5a983c32efe05707b25_2_690x387.png" alt="Captura de pantalla de 2021-11-17 04-49-27" data-base62-sha1="zxvmGY4NWOi69eLRuGXt53QceQl" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f915b144df20b9f78dfcd5a983c32efe05707b25_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f915b144df20b9f78dfcd5a983c32efe05707b25_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f915b144df20b9f78dfcd5a983c32efe05707b25.png 2x" data-dominant-color="E9E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla de 2021-11-17 04-49-27</span><span class="informations">1366×768 73.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can you help understand what is happening? Do I need to edit these lines?</p><aside class="onebox githubblob" data-onebox-src="https://github.com/mauigna06/SlicerMorphCloud/blob/35cef65a4fb6236d17e03a31594ff7083c849b98/Dockerfile#L70-L71">
  <header class="source">

      <a href="https://github.com/mauigna06/SlicerMorphCloud/blob/35cef65a4fb6236d17e03a31594ff7083c849b98/Dockerfile#L70-L71" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/mauigna06/SlicerMorphCloud/blob/35cef65a4fb6236d17e03a31594ff7083c849b98/Dockerfile#L70-L71" target="_blank" rel="noopener nofollow ugc">mauigna06/SlicerMorphCloud/blob/35cef65a4fb6236d17e03a31594ff7083c849b98/Dockerfile#L70-L71</a></h4>



    <pre class="onebox"><code class="lang-">
      <ol class="start lines" start="70" style="counter-reset: li-counter 69 ;">
          <li>&amp;&amp; sed -i 's/^# \$wm =.*/\$wm = \"openbox-session\";/g' /etc/turbovncserver.conf \</li>
          <li>&amp;&amp; sed -i 's/^# \$noVNC =.*/\$noVNC = \"\/home\/docker\/noVNC\";/g' /etc/turbovncserver.conf \</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I also created an ubuntu installation on my hard-disk and executed each one of the docker commands. Then I try launching a vncserver and access the corresponding link and it yields the same result “File Not Found”. So I suspect maybe there is some configuration that could be corrected.</p>
<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #10 by @muratmaga (2021-11-17 16:29 UTC)

<p>First comment, that’s a bit outdated and a was a very early attempt, and not particularly flexible to use.</p>
<p>Is accessing through a web browser a must? When we did the workshop, I did not like the performance of noVNC, which used 2-5 times more bandwidth than turbovnc, and was less interactive. So now are using TurboVNC dedicated client, which interacts nicely with the session manager of TurboVNC server and handles some of the complexities of starting the individual sessions. But this means your users need to install Turbovnc software.</p>
<p>In the script above, users file should contain the usernames of your cloud uses, and instance table ends up containing the specific URL (hostname + port) and the one time password associated with authentication.</p>
<p>I again, I wouldn’t do (and we are not doing) this way now. TurboVNC session manager is handling all the authentication via SSH. I also stopped putting the Slicer inside the container, for two reasons:</p>
<ol>
<li>Updating slicer requires rebuilding the container</li>
<li>You will need to map persistent storage for your users to keep their data between sessions anyways (unless it is a short course or something).</li>
</ol>
<p>So I simply copy the fully functional Slicer folder to their persistent storage, which also gives them the flexibility of installing additional extensions (not have to do this everytime their docker instance starts).</p>

---

## Post #11 by @muratmaga (2021-11-17 17:20 UTC)

<p>take a look at this branch <a href="http://github.com/SlicerMorph/SlicerMorphCloud/tree/eglbackend" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorphCloud/tree/eglbackend</a></p>
<p>This is what we are using now. Couple things to consider. We want the ability the to be able to size the user’s session to match their data (perhaps they need GPU, perhaps they need large RAM etc), and also provide analytics platform (mainly R), so there is probably a lot of unnecessary clutter for you.</p>
<p>You should probably delete all R related lines in the dockerfile to cut down your build time (unless you need it of course). I directly <a href="https://app.box.com/shared/static/s8ivm5y86bhozsjwc5ajw8vf83t7kjk5.gz" rel="noopener nofollow ugc">download the Slicer image</a> onto the host and unpack to the users persistent storage .</p>

---

## Post #12 by @mau_igna_06 (2021-11-17 18:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="16401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is accessing through a web browser a must? When we did the workshop, I did not like the performance of noVNC, which used 2-5 times more bandwidth than turbovnc, and was less interactive.</p>
</blockquote>
</aside>
<p>Hi Murat. Thanks for the answer. We are not bandwidth-constrained and we would prefer to use a web browser.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="16401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In the script above, users file should contain the usernames of your cloud uses, and instance table ends up containing the specific URL (hostname + port) and the one time password associated with authentication.</p>
</blockquote>
</aside>
<p>I made these few changes to your main branch in my fork: <a href="https://github.com/mauigna06/SlicerMorphCloud/pull/1/files" class="inline-onebox" rel="noopener nofollow ugc">Successful build docker image by mauigna06 · Pull Request #1 · mauigna06/SlicerMorphCloud · GitHub</a><br>
I know the main branch worked well for you in the classes you gave. Do you have any idea why the web-browser shows “File Not Found” considering I followed the instructions step-by-step?</p>

---

## Post #13 by @muratmaga (2021-11-17 18:23 UTC)

<p>Not sure, are you running the docker and the client on the same box? Is that really the hostname? Did you try replacing the with localhost (if it is local). We would manually change the first to match the IP address of the box to connect.</p>

---

## Post #14 by @mau_igna_06 (2021-11-17 18:46 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="16401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Not sure, are you running the docker and the client on the same box?</p>
</blockquote>
</aside>
<p>I’m running the docker container and the web-browser on the same computer.</p>
<blockquote>
<p>Is that really the hostname?</p>
</blockquote>
<p>Yes, that’s the hostname: it is what appears first on my terminal after “root@”</p>
<blockquote>
<p>We would manually change the first to match the IP address of the box to connect.</p>
</blockquote>
<p>I changed the link to: <code>http://127.0.0.1:49156/vnc.html?host=127.0.0.1&amp;port=49155&amp;resize=remote</code> and the result is “File Not Found”</p>
<p>But if I stop the container the same link shows this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7782a4d6f32187322dae1cd1bca28079a14e1f1.png" data-download-href="/uploads/short-url/zjdo3EVzcKyVWuGVTmejzMpRrqh.png?dl=1" title="Captura de pantalla de 2021-11-17 10-30-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7782a4d6f32187322dae1cd1bca28079a14e1f1_2_690x387.png" alt="Captura de pantalla de 2021-11-17 10-30-42" data-base62-sha1="zjdo3EVzcKyVWuGVTmejzMpRrqh" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7782a4d6f32187322dae1cd1bca28079a14e1f1_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7782a4d6f32187322dae1cd1bca28079a14e1f1_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7782a4d6f32187322dae1cd1bca28079a14e1f1.png 2x" data-dominant-color="E6E5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla de 2021-11-17 10-30-42</span><span class="informations">1366×768 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It says “Cannot connect” on the heading and “Try again” in the blue button.</p>
<p>So I think TurboVNC is working but needs some extra configuration because when the container was live it showed the “File Not Found” page and the small VNC icon on the top of the firefox’s tab.</p>

---

## Post #15 by @muratmaga (2021-11-17 18:52 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="14" data-topic="16401">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>So I think TurboVNC is working but needs some extra configuration because when the container was live it showed the “File Not Found” page and the small VNC icon on the top of the firefox’s tab.</p>
</blockquote>
</aside>
<p>I suspect you are correct. But it is hard to debug, because the entire VNC session lives in the docker container. I guess you can jump into the running docker container and take a look at the log file under /home/docker/.vnc to see what file is missing, or what the actual error is.</p>
<p>That was one of the reasons why we moved away from this.</p>

---
