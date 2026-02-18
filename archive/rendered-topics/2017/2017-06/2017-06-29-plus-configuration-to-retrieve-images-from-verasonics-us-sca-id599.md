# Plus configuration to retrieve images from Verasonics US scanner and perform 3D reconstruction

**Topic ID**: 599
**Date**: 2017-06-29
**URL**: https://discourse.slicer.org/t/plus-configuration-to-retrieve-images-from-verasonics-us-scanner-and-perform-3d-reconstruction/599

---

## Post #1 by @Tiffas (2017-06-29 17:04 UTC)

<p>Hi,</p>
<p>I use a Verasonics ultrasound scanner which sends, using OpenIGTLink protocol, images to an other computer on which Slicer runs. On the Verasonics side I have a OpenIGTLink client (coded with Matlab, unfortunately I have to use it) and on the Slicer side I use the OpenIGTLinkIF module to create a server.</p>
<p>I now want to reconstruct 3D volume from the Verasonics images.<br>
First question : is there a Slicer module that takes an image and a transform streams and compute a volume from them ?</p>
<p>My understanding is that such a module does not exit, I have to use Plus Toolkit to perform 3D reconstruction.<br>
If my understanding is correct, in order to have Plus performing 3D reconstruction I have, inter alia, to create a device of type OpenIGTLinkVideo in the xml config file that Plus uses. The problem is such a device is supposed to be a server yet on the Verasonics side I have an OpenIGTLink client.<br>
Second question : is there a way to tell Plus that it will receive images from an OpenIGTLink client ?</p>
<p>Thanks, Loïc</p>

---

## Post #2 by @lassoan (2017-06-30 13:41 UTC)

<aside class="quote no-group" data-username="Tiffas" data-post="1" data-topic="599">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ba9def/48.png" class="avatar"> Tiffas:</div>
<blockquote>
<p>is there a Slicer module that takes an image and a transform streams and compute a volume from them ?</p>
</blockquote>
</aside>
<p>Unfortunately, volume reconstruction is only available in Plus. Slicer can act both as a client as a server (you can set it up in OpenIGTLinkIF module), so you can use it to act as a server to receive images from your Matlab code and allow PlusServer to connect: Matlab (Client) → Slicer (Server) → PlusServer (OpenIGTLinkVideo device). Going through an extra step may add some time delay but you can give it a try.</p>

---

## Post #3 by @jbassinot (2018-08-07 23:37 UTC)

<p>Hi,</p>
<p><a class="mention" href="/u/tiffas">@Tiffas</a> did you manage to perform 3D reconstruction ?<br>
Is there any new tool for connecting Verasonics to Plus ?</p>
<p>Thanks for your help,<br>
Julien</p>

---

## Post #4 by @lassoan (2018-08-08 05:50 UTC)

<p>Without programming, the only way to acquire images from a Verasonics scanner is to use a framegrabber device. If you are willing to do some C++ programming then you can implement an interface for it in Plus toolkit. For more information, contact Plus developers at <a href="http://www.plustoolkit.org">www.plustoolkit.org</a>.</p>

---

## Post #5 by @Tiffas (2018-09-05 11:19 UTC)

<p>Hi Julien,</p>
<p>To perform 3D reconstruction with the Plus toolkit, Verasonics must send images which comply with the OpenIGTLink protocol. So I implemented functions in Matlab to send images in the OpenIGTLink format on local network. Then I used them in the Verasonics UDisplay function so that a newly reconstructed image is sent on the network. Finally I created a xml configuration file for Plus and it worked !</p>

---

## Post #6 by @Tiffas (2018-09-05 11:25 UTC)

<p>I read again my original post, actually I was able to create a server on the Verasonics side.</p>

---

## Post #7 by @Teresa_Gadda (2021-01-26 04:49 UTC)

<p>Sorry for reviving an old thread but I want to do this exact thing too.  Do you happen to have the MATLAB code you used to send images in the OpenIGTLink format?  I’d prefer not to reinvent the wheel if it’s not necessary.  Thanks for thinking about it!</p>

---

## Post #8 by @lassoan (2021-01-26 13:18 UTC)

<p>If you can use Python in Matlab then you can send images to Slicer using our <a href="https://github.com/lassoan/pyigtl">pyigtl</a> package.</p>

---

## Post #9 by @Teresa_Gadda (2021-01-27 19:23 UTC)

<p>SUPER HELPFUL TIP!  Thanks so much!</p>
<p>It took some messing around but I got it working.  One tip for other people who might find this thread and try this method is that when you call this python library from Matlab it doesn’t seem to shut the python down cleanly when it finishes executing, so the python doesn’t know to stop the server and just keeps running it in the background and blocks reconnection to the slicer client.</p>
<p>For example, when I ran example_image_server.py from Matlab, after I killed it I would have to restart slicer and matlab to get it to work a second time.</p>
<p>As a work around I just made sure to explicitly call server.stop() on any server I started instead of relying on shutdown of the python app to call it.</p>
<p>Thanks again Andras!!!</p>

---
