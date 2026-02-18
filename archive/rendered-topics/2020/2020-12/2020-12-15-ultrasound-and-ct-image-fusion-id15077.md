# Ultrasound and CT image fusion

**Topic ID**: 15077
**Date**: 2020-12-15
**URL**: https://discourse.slicer.org/t/ultrasound-and-ct-image-fusion/15077

---

## Post #1 by @Nsangu (2020-12-15 18:13 UTC)

<p>Greetings.</p>
<p>My name is Augustine, A medical Physicist from Zambia. Iam working on trying to fuse US images with CT and I have a lot of questions. My area of interest is the pelvic region (the cervix) in particular.</p>
<p>I have gone through a few videos on US registration just to get familiar with the software. I hope you can help me</p>
<p>Many thanks</p>
<p>Augustine</p>

---

## Post #2 by @cpinter (2020-12-15 18:34 UTC)

<p>Hi there! Yes we’ll help as we can <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Feel free to ask your questions one by one.</p>
<p>Is your ultrasound data a 3D reconstructed volume from tracked ultrasound?</p>

---

## Post #3 by @Nsangu (2020-12-15 20:20 UTC)

<p>Hi Pinter <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I am very new to 3DSlicer. The following are the details of the Ultrasound machine<br>
Brand: Haiyang<br>
Model: Digital color doppler, ultrasonic diagnostic system. It is a 3D ultrasound machine.</p>
<p>My first question: How do I verify that PLUS is properly installed? Upon watching a few videos, I notice with some versions, “remote plus” can be accessed from IGT. I cannot see “remote plus” via IGT when I launch 3Dslicer on my laptop. However I do have plus server launcher from start up menu.</p>

---

## Post #4 by @Nsangu (2020-12-15 20:21 UTC)

<p>I have not even started data acquisition yet. Which would be easier to fuse? 3D data or frames?</p>

---

## Post #5 by @cpinter (2020-12-16 10:13 UTC)

<p>First of all make sure that you use the latest nightly Slicer version and the latest Plus. Then install the <code>SlicerIGT</code> and <code>SlicerOpenIGTLink</code> extensions from the Extension Manager. The <code>Plus Remote</code> module will appear in the IGT category.</p>
<p>I don’t have experience with 3D ultrasound machines and their data but I guess that would be preferred to frames, because if you acquire frames then you’ll need to use an external position tracker, which seems unnecessary given that you have the 3D US machine.</p>
<p>Once you have the 3D ultrasound volume and the CT in Slicer, then you can try the registration. I have doubts about automatic registration, although you can try the <code>General Registration (Elastix)</code> module from the <code>SlicerElastix</code> extension. If it doesn’t work, then you can try landmark registration, or if you need to do it anyway, then (structure-based) segment registration after you segmented the cervix in each image.</p>

---

## Post #6 by @Nsangu (2020-12-16 20:38 UTC)

<p>Thank you so much. The software is installed and am ready to start. I will give feedback as soon as possible.</p>

---

## Post #7 by @lassoan (2020-12-17 07:06 UTC)

<p>We need to know a bit more of your setup to give meaningful advice. What is the clinical application - HDR catheter placement using ultrasound guidance? Which applicator do you use? Do you use an endocavity ultrasound transducer or are you trying to image through the skin? What is your current clinical workflow? Do you use any planning and guidance software? Can you retrieve 3D ultrasound volume from your imaging system and can your guidance software import 3D images to display it fused with the live ultrasound image?</p>

---

## Post #8 by @Nsangu (2020-12-17 08:49 UTC)

<p>Thank you for the question.</p>
<p>At the Cancer Diseases Hospital, Zambia (population of about 18million people), we have 1 Linear accelerator, 2 Cobalt-60 machines, 2 brachytherapy afterloader (nucletron), 2 CT scanners and 1 MRI - This is the only cancer referral center in the country.</p>
<p>We perform on average 15 insertions per day at brachytherapy, all our insertions are ultrasound guided (with most patients treated with pre planned “standard” plans and a few cases 3D planned). We have the Ring applicator set, fletcher, modified ring applicator set (the vienna) etc - We have both CT/MR compatible applicators and the ordinary applicators.</p>
<p>The planning system is Oncentra brachy, but unfortunately it does not have the license for image fusion or an applicator library. We have a 3D ultrasound machine.</p>
<p>Background<br>
For brachytherapy, the separation of imaging modalities across different suites prolongs the workflow thereby restricting the number of patients that can realistically be treated to an average of 2-3/day( 3D planning). In high disease burden environments, like Zambia, up 15 patients may be simulated per week and  an average of 10 patients/day must undergo brachytherapy procedures to prevent excessively long waiting lists. A possible solution to this problem is the use of ultrasound technology fused with CT for 3D planning. Multiple studies have demonstrated the feasibility of using ultrasound 3D brachytherapy planning in the treatment of cervical cancer.</p>
<p>We are trying to image the cervix fuse it with CT images, contour and export to the treatment planning system for planning.</p>
<ol>
<li>
<p>Our first huddle is to properly fuse the Ultrasound images with CT and later contour the region of interest. I am not sure our TPS will display fused images. will confirm.</p>
</li>
<li>
<p>Dicom send/export on the ultrasound machine  is only enabled during real time scanning, whether I can retrieve 3D volume, I doubt but I can check.</p>
</li>
</ol>
<p>Is this something 3Dslicer can help me achieve?</p>

---

## Post #9 by @lassoan (2020-12-19 06:50 UTC)

<aside class="quote no-group" data-username="Nsangu" data-post="8" data-topic="15077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/7c8e57/48.png" class="avatar"> Nsangu:</div>
<blockquote>
<p>Our first huddle is to properly fuse the Ultrasound images with CT and later contour the region of interest. I am not sure our TPS will display fused images. will confirm.</p>
</blockquote>
</aside>
<p>If you can get the 3D ultrasound images from your ultrasound system then fusion should be no problem.</p>
<aside class="quote no-group" data-username="Nsangu" data-post="8" data-topic="15077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/7c8e57/48.png" class="avatar"> Nsangu:</div>
<blockquote>
<p>Dicom send/export on the ultrasound machine is only enabled during real time scanning, whether I can retrieve 3D volume, I doubt but I can check.</p>
</blockquote>
</aside>
<p>You need to find a way to get the 3D ultrasound images out of your system. Either DICOM or research formats work. You may need to contact your ultrasound device representative to help you with the data export (you may need to buy extra license for 3D data export).</p>

---

## Post #10 by @Nsangu (2020-12-20 18:40 UTC)

<p>Many thanks Lassoan<br>
I will revert.</p>

---

## Post #11 by @lassoan (2020-12-23 20:53 UTC)

<p>Let us know if we can help with anything. The difficult part is to get images out of the closed commercial imaging and planning systems. Once we get over that hurdle, everything you need is already available in Slicer.</p>

---

## Post #12 by @Nsangu (2020-12-28 13:38 UTC)

<p>Hallo</p>
<p>We have a team looking at the ultrasound machine and I am confident we will manage to get 3D data out of the machine. My other question:</p>
<ol>
<li>How do I configure 3Dslicer to receive images. In Plus remote, I can create PlusServerLauncher, Which shows Launcher node, Hostname and Port. Which of these is the AEtitle? Is there a step by step procedure of how to configure this server so that i can receive images from the ultrasound?</li>
</ol>
<p>I need to enter these details into the Dicom portal of the Ultrasound machine</p>
<p>Many thanks and merry christmas</p>

---

## Post #13 by @lassoan (2020-12-30 05:49 UTC)

<p>Plus toolkit is for receiving live ultrasound images, primarily tracked 2D images.</p>
<p>If your ultrasound system sends images via DICOM then you don’t need Plus toolkit. Instead, you can use 3D Slicer’s DICOM receiver (C-STORE SCP).To enable that, go to DICOM module / DICOM networking section and check “Storage listener”. Server details:</p>
<ul>
<li>Hostname: the computer’s name or IP address where Slicer runs</li>
<li>Port: displayed next to the “Storage listener” checkbox (11112 by default)</li>
<li>AE Title: <code>STORESCP</code>
</li>
</ul>

---

## Post #14 by @Nsangu (2021-01-05 13:18 UTC)

<p>Lassoan</p>
<p>Happy new year<br>
The dicom Configuration were done and successful. Still working on the 3D dicom data export from our machine. Meanwhile I have been trying to configure 3Dslicer to receive live ultrasound images using plus tool kit. The procedure provided on self help do not apply to the latest software that I have installed. For example, I am not able to select/ capture device ID in plus remote/ plus remote control but there is a procedure for the previous 3Dslicer software version. If there is a link to the procedure of configuring 3Dslicer to receive live ultrasound images, that would be helpful. Thanks</p>

---

## Post #15 by @lassoan (2021-01-06 03:21 UTC)

<p>What image capture device do you use to capture live ultrasound images?</p>

---

## Post #16 by @Nsangu (2021-01-06 12:17 UTC)

<p>We have gotten feedback from the manufacturer of the Ultrasound. They have just informed us that the machine can only export AVI format of images obtained with a 3D ultrasound probe.</p>
<p>We have trans abdominal probes (2D and 3D). Do I need additional equipment in order to acquire images in real time using the plus tool kit? Now that I cannot get 3D data out of the ultrasound, what options do I have in trying to fuse US images and CT images??</p>

---

## Post #17 by @lassoan (2021-01-06 13:56 UTC)

<aside class="quote no-group" data-username="Nsangu" data-post="16" data-topic="15077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/7c8e57/48.png" class="avatar"> Nsangu:</div>
<blockquote>
<p>We have gotten feedback from the manufacturer of the Ultrasound. They have just informed us that the machine can only export AVI format of images obtained with a 3D ultrasound probe.</p>
</blockquote>
</aside>
<p>This means that you do not have access to the 3D data, just a series of 2D screenshots of the image that the ultrasound system renders. Unfortunately, this is the expected behavior. With a very few exceptions, users do not get access to 3D/4D data. You will not be able to take advantage of your 3D probe, but you may still use it as a 2D probe.</p>
<aside class="quote no-group" data-username="Nsangu" data-post="16" data-topic="15077">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/7c8e57/48.png" class="avatar"> Nsangu:</div>
<blockquote>
<p>We have trans abdominal probes (2D and 3D). Do I need additional equipment in order to acquire images in real time using the plus tool kit? Now that I cannot get 3D data out of the ultrasound, what options do I have in trying to fuse US images and CT images??</p>
</blockquote>
</aside>
<p>To acquire 3D volumes with a 2D probe, you need an image capture device to acquire images and a position tracker to get position and orientation of each acquired image slice. You can choose devices from the list available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/Configuration.html">here</a>.</p>
<p>If you use a trans-abdominal probe then probably the most suitable tracking device is an optical tracker, such as an <a href="https://www.optitrack.com/cameras/v120-duo/">Optitrack Duo</a>.</p>
<p>To recommend an imaging device, we need to know what kind of video output your ultrasound system has (HDMI, S-video, …).</p>
<p>Once you have the image acquisition and position tracker hardware, you need to create a configuration file for Plus that describe what hardware and acquisition settings to use, then calibrate them using tools provided by Plus toolkit and SlicerIGT extension.</p>

---
