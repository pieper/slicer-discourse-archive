---
topic_id: 9668
title: "Cant Get It To Install On My Chromebook"
date: 2019-12-31
url: https://discourse.slicer.org/t/9668
---

# Can't get it to install on my Chromebook

**Topic ID**: 9668
**Date**: 2019-12-31
**URL**: https://discourse.slicer.org/t/cant-get-it-to-install-on-my-chromebook/9668

---

## Post #1 by @Logan_Quinn (2019-12-31 06:54 UTC)

<p>Operating system: Version 79.0.3945.86 (Official Build) (64-bit) Using the Linux (beta) feature.<br>
Slicer version: 4.10.2<br>
Expected behavior: Following instruction at <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ#How_to_install_Slicer_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/FAQ#How_to_install_Slicer_.3F</a> I type in the 1st line updating the version number as instructed:<br>
$ tar xzvf ~/Downloads/Slicer-4.10.2-linux-amd64.tar.gz -C ~/<br>
Actual behavior: error message<br>
“tar (child): /home/dragonbeary/Downloads/Slicer-4.10.2-linux-amd64.tar.gz: Cannot open: No such file or directory<br>
tar (child): Error is not recoverable: exiting now<br>
tar: Child returned status 2<br>
tar: Error is not recoverable: exiting now”</p>
<p>Expected behavior: I am able to unpack the file with another app (Wicked Good Unarchiver) so that I have the folder “Slicer-4.10.2-linux-amd64” so then I try typing in the 2nd line if the instructions:<br>
$ cd ~/Slicer-4.10.2-linux-amd64<br>
Actual behavior: error message “-bash: cd: /home/dragonbeary/Slicer-4.10.2-linux-amd64: No such file or directory”</p>
<p>Expected behavior: Finally I do discover I have somehow produce a “Slicer” file sitting in my Downloads folder, so I type in the 3rd line of the instructions:<br>
$ ./Slicer<br>
Actual behavior: error message: “-bash: ./Slicer: Permission denied”</p>
<p>My brain is now melting down, can someone help me figure out how to install Slicer on my Chromebook so I can check out my MRI images? During this learning process I was able to install an unrelated linux app, so the Linux (beta) feature does appear to be functioning correctly. Although I’ve been planning to learn Linux, I’m a total newbie with working with terminals and programming code stuff.</p>
<p>Thanks,</p>
<p>-Logan</p>

---

## Post #2 by @Logan_Quinn (2020-01-01 05:52 UTC)

<p>I think I just need to know how to get around this error message: “-bash: ./Slicer: Permission denied”</p>

---

## Post #3 by @pieper (2020-01-01 18:04 UTC)

<p>I just tried on a google pixel book and Slicer runs if unpacked onto the linux file system but no graphics are displayed (there are error messages related to the version of OpenGL shader language not being supported).</p>
<p><a class="mention" href="/u/logan_quinn">@Logan_Quinn</a>, if your goal is just to look at MRI dicom files, you might be better off with <a href="http://slicedrop.com">slicedrop.com</a> or <a href="http://viewer.ohif.org/local">viewer.ohif.org/local</a>, both of which support loading images from your local file system and run entirely in the browser (not as many features as Slicer, but good for quick image viewing).</p>

---

## Post #4 by @Logan_Quinn (2020-01-01 19:42 UTC)

<p>I was hoping to be able to view the MRI images in 3D to get a better sense of the size, shape and location of the tumor on my skull that’s pressing against my right 6th cranial nerve. I’ve tried using a couple of the free apps available but even they don’t work very well at viewing the slices, have to load each one separately. Started to convert the images into png’s so I can view them with Chomebook’s Gallery app, but 570 images is making that a long tedious project. I will check out the two options you mentioned. Hmmm… of the two the second link is more useful But doesn’t seem to offer the 3D feature I was hoping to have. The slicedrop app sorta offers a 3D, but only 3 slices at a time, which doesn’t really help me locate the tumor and see it as a 3D object.</p>

---

## Post #5 by @pieper (2020-01-01 20:52 UTC)

<p>Sorry that the chromebook option isn’t working.  Any workaround I know of would only get you deeper into the linux world.</p>
<p>Maybe the easiest is to borrow a windows machine from someone?  Or <a href="https://azure.microsoft.com/en-us/pricing/details/virtual-machines/windows/">rent one from microsoft</a> if you can find a way to access it via your chromebook.  You can also rent linux virtual machines from Amazon or Google and access Slicer via a browser if you want to try that route.</p>

---

## Post #6 by @Logan_Quinn (2020-01-01 22:37 UTC)

<p>I don’t mind the idea of delving deeper into learning more about linux in general. Have actually posted a request for help with this issue in the Chromebook linux (beta) help forum, coming at it from both sides, computer side there and software side here. Perhaps between the two a solution can be arrived at.</p>
<p>I can’t afford to be renting or buying stuff as I’m on a fixed SSI income. Even my new chromebook I’m using was a B-day gift from a friend. If you know of any workarounds I’d like to try them, also curious about being able to use Slicer via a browser, which is basically what chromebook is. I didn’t see a browser option on the 3DSlicer website, just Windows, Mac and Linux. Since my chromebook has a Linux (beta) option I thought I would be able to install the Linux option using that, but unable to get it installed yet. But maybe instead I need to use a Windows or Mac browser emulator instead? hmmm…</p>

---

## Post #7 by @lassoan (2020-01-01 23:05 UTC)

<p>Trial with several months worth of virtual machine time is available for free on Azure and probably on Google Cloud and Amazon, too. On Azure, you can create a virtual machine with default settings (Standard D2s v3, Ubuntu) and configure remote desktop access as described <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-remote-desktop">here</a>. This is all for free. For me, the “Standard D2s v3” machine was quite slow, but when I’ve set screen resolution to lower (1280x1024, High Color) then it has become usable.</p>
<p>You may also go over to a public library, sit down at a computer, and install Slicer (no admin rights are needed for installing Slicer preview releases).</p>

---

## Post #8 by @pieper (2020-01-02 19:13 UTC)

<p>Hi <a class="mention" href="/u/logan_quinn">@Logan_Quinn</a> - I’ll outline a way to get access to Slicer in the cloud - it’s not ideal for all uses but might suit your situation since it is free and will let you access Slicer from your chromebook browser.</p>
<p>You can get $300 free cloud credit from google through their cloud (<a href="https://cloud.google.com/">https://cloud.google.com/</a>).</p>
<p>Once you have an account, go to the console and select the Compute Engine and pick Create Instance.  There are many options but most don’t matter.  As Andras said, you probably want to get more than just the default, so try, for example, 4 core and 15G of memory (this is only thirteen cents an hour, so your $300 will last a long time unless you forget to turn the machine off).</p>
<p>Be sure to turn on the HTTP option like so:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91cb8ecdb3dc711f8f9a8d6bc36d90a4efbd8eca.png" alt="image" data-base62-sha1="kNLlWbxhAG7XN80e1q2Td0usXFM" width="461" height="91"></p>
<p>Once you click create it should only take a few minutes to start up and then you should see it on the list of running VM instances.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3fe8f741009644df96f941aae17d37729a122b2.png" data-download-href="/uploads/short-url/noLdGyJJOUVsS2x82eBdEWRoJtE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3fe8f741009644df96f941aae17d37729a122b2_2_690x57.png" alt="image" data-base62-sha1="noLdGyJJOUVsS2x82eBdEWRoJtE" width="690" height="57" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3fe8f741009644df96f941aae17d37729a122b2_2_690x57.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3fe8f741009644df96f941aae17d37729a122b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3fe8f741009644df96f941aae17d37729a122b2.png 2x" data-dominant-color="F6F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">880×73 8.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Click on the SSH button and a new window will pop up.</p>
<p>Once it logs in, you can enter this line:</p>
<pre><code class="lang-auto">docker run -p 80:8080 stevepieper/slicer
</code></pre>
<p>You should see some diagnostic output which is normal.</p>
<p>From there you can open a new browser tab and enter the text of the “External IP” into the address bar and you should connect.  Click the “X11 Session” button and it should take you to a running instance of Slicer that you can play with.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9cb8507a76d9b86ee89ef3b08edb9818a536121.png" alt="image" data-base62-sha1="qvCmZCenaLEv8k3Hj9YutC2oy77" width="381" height="252"></p>
<p>(<a href="http://35.225.73.173/x11/vnc.html?autoconnect=true&amp;path=x11/websockify">Here is a running example</a> on my account - I’ll leave it up for a bit if you want to try it, but eventually I’ll delete it and remember that it’s public so don’t put anything confidential there).</p>
<p>Note that this does not generate a secure site and what you do on this machine won’t be saved permanently, but it’s enough for experimenting.  You can use the File Management button on the first web page to upload and download data (e.g. your MRI and any data you create in Slicer).</p>
<p>Use the “Stop” button to shut down the machine when you aren’t using it.</p>
<p>Hope that helps,<br>
Steve</p>

---
