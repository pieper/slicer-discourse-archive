# Use of 'sequences' for 3D ultrasound spatial calibration and acquisition

**Topic ID**: 13294
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/use-of-sequences-for-3d-ultrasound-spatial-calibration-and-acquisition/13294

---

## Post #1 by @AurelieS (2020-09-02 10:04 UTC)

<p>Hi,</p>
<p>I am doing 3D ultrasound using an Optitrack motion capture system and an USB module streaming the video feed from a SuperShearingImaging ultrasound :</p>
<ul>
<li>First, I use FCAL for the temporal and stylus calibrations</li>
<li>Then, I use PlusServer + 3D Slicer + SlicerIGT for the spatial calibration and for acquisitions.</li>
</ul>
<p>To record my live acquisitions, I use the module ‘Sequences’.<br>
I don’t quite understand how it works, and I feel that maybe I am missing some steps or missing a simpler way to do it :</p>
<ul>
<li>
<p>I have the following hierarchy in ‘Data’:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/481a24e00dd1a6d1229e24945bba74e8b4b04ab0.png" alt="Picture1" data-base62-sha1="ahQofSxOq2QqdvK5Xwh9Ipjxf7W" width="386" height="359"></p>
</li>
<li>
<p>For the recording of the spatial calibration, I create a calibration_spatial’ sequence, then add three nodes : Image_Image , ProbeToTracker , StylusToTracker.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e46e148364a7099f8c1a018d0a1d99500b1a1711.png" alt="Picture2" data-base62-sha1="wAMHWPvVvWvk9zGojH9V2BnuVGx" width="602" height="184"></p>
</li>
<li>
<p>I do not tick ‘rename’ and ‘save changes’ since if I do, I loose my live image of the ultrasound.</p>
</li>
<li>
<p>Then, I click record and I perform my calibration. I stop the recording</p>
</li>
<li>
<p>Finally, I tick ‘rename’ and ‘save changes’.</p>
</li>
<li>
<p>I go to the Fiducial Wizard, calculate my ImageToProbe matrix using the data from the sequence.</p>
</li>
<li>
<p>To go back to live visualisation, it is quite a pain : I have to uncheck the view of all the data from the calibration, check the view for all my ‘live’ data, and redo the hierarchy since the ‘live’ data has been relocated to the ‘Scene’ master.</p>
</li>
<li>
<p>then I redo the hierarchy using ‘ImageToProbe’ in order to visualise my ultrasound image in the 3D view.</p>
</li>
<li>
<p>To do an acquisition of a volume, I go to ‘Sequences’, add two nodes ‘Image_Image’ and ‘ProbeToTracker’, I do not check ‘rename’ and ‘save changes’, do my recording, stop the recording, and finally check ‘rename’ and ‘save changes’.</p>
</li>
<li>
<p>Then again, if I want to go back to my ‘live’ images, I need to set again the hierarchy.</p>
</li>
</ul>
<p>Am I doing this the right way ? Is there a simpler way to switch between ‘live’ and a recorded sequence ?<br>
Why the hierarchy is reset each time I record a sequence ?</p>
<p>Thanks in advance,<br>
Cheers<br>
Aurélie</p>

---

## Post #2 by @lassoan (2020-09-02 14:24 UTC)

<p>I think you can do things in a much simpler way.</p>
<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>do not tick ‘rename’ and ‘save changes’ since if I do, I loose my live image of the ultrasound.</p>
</blockquote>
</aside>
<p>Rename just changes the node name to include timestamp. It does not affect visibility.</p>
<p>Save changes means that if you make changes to a recorded frame then it is saved in the sequ nce. This does not affect visibility either.</p>
<p>Can you take a screen capture video that shows how the image disappears for you?</p>
<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>Finally, I tick ‘rename’ and ‘save changes’</p>
</blockquote>
</aside>
<p>This is not necessary. Actually, it makes things simpler if you keep them disabled because then you can use the same transform hierarchy for record and replay.</p>
<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>To go back to live visualisation, it is quite a pain : I have to uncheck the view of all the data from the calibration, check the view for all my ‘live’ data, and redo the hierarchy since the ‘live’ data has been relocated to the ‘Scene’ master.</p>
</blockquote>
</aside>
<p>This is not necessary. OpenIGTLink can update the same sequence proxy nodes. Just keep “Save changes” turned off to make sure you don’t change any recorded data. [quote=“AurelieS, post:1, topic:13294”]<br>
then I redo the hierarchy using ‘ImageToProbe’ in order to visualise my ultrasound image in the 3D view<br>
[/quote]</p>
<p>Not necessary. The same node hierarchy can be used by live display and replay. [quote=“AurelieS, post:1, topic:13294”]<br>
To do an acquisition of a volume, I go to ‘Sequences’, add two nodes ‘Image_Image’ and ‘ProbeToTracker’, I do not check ‘rename’ and ‘save changes’, do my recording, stop the recording, and finally check ‘rename’ and ‘save changes’.<br>
[/quote]</p>
<p>Not necessary. You can reconstruct a volume without recording it. [quote=“AurelieS, post:1, topic:13294”]<br>
Then again, if I want to go back to my ‘live’ images, I need to set again the hierarchy.<br>
[/quote]</p>
<p>Not necessary, as the same hierarchy can be used for record and replay.</p>
<aside class="quote no-group" data-username="AurelieS" data-post="1" data-topic="13294">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> AurelieS:</div>
<blockquote>
<p>Why the hierarchy is reset each time I record a sequence ?</p>
</blockquote>
</aside>
<p>What do you do when you record a sequence? Just click on record button? What exactly is being reset?</p>

---

## Post #3 by @AurelieS (2020-09-03 11:20 UTC)

<p>The thing is, if I do not check ‘Rename’ when I record a sequence, when I play back the sequence I just recorded, I feel like the software is trying to display both live images (from the trackers and the ultrasound) and the recorded images, so the images are very messy, and I cannot put my fiducials to do my spatial calibration for example. I feel that is logical since a same node, for example image_image, will then be used both for ‘live’ and for the recorded sequence.</p>
<p>When I check ‘Rename’, the software immediately creates a new node linked to the recorded with a timestamp between brackets <span class="chcklst-box fa fa-square-o fa-fw"></span>. So if I check ‘Rename’ before the recording, I loose the ‘live’ image and tracking :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/092a6e05928dd9a2d2dcb0c4b1f9a6e1f1a69830.png" data-download-href="/uploads/short-url/1j5cyNPDW8gzATTLB6iVXQgBgKQ.png?dl=1" title="Image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/092a6e05928dd9a2d2dcb0c4b1f9a6e1f1a69830_2_690x230.png" alt="Image1" data-base62-sha1="1j5cyNPDW8gzATTLB6iVXQgBgKQ" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/092a6e05928dd9a2d2dcb0c4b1f9a6e1f1a69830_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/092a6e05928dd9a2d2dcb0c4b1f9a6e1f1a69830_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/092a6e05928dd9a2d2dcb0c4b1f9a6e1f1a69830_2_1380x460.png 2x" data-dominant-color="7F7984"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image1</span><span class="informations">1690×565 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But if I check ‘Rename’ after the recording, that is fine because this time I can see the recorded images when I replay a sequence, however the initial ‘live’ nodes are ejected from the transform hierarchy and the recorded nodes take their place as seen in theses pictures :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4afcf27ab9dbeb61e0c576498df8f21c62d8facc.png" data-download-href="/uploads/short-url/aHngIz3DoNwbQsDj5mqONPCVwMQ.png?dl=1" title="Image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4afcf27ab9dbeb61e0c576498df8f21c62d8facc_2_690x344.png" alt="Image2" data-base62-sha1="aHngIz3DoNwbQsDj5mqONPCVwMQ" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4afcf27ab9dbeb61e0c576498df8f21c62d8facc_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4afcf27ab9dbeb61e0c576498df8f21c62d8facc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4afcf27ab9dbeb61e0c576498df8f21c62d8facc.png 2x" data-dominant-color="AEAFB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image2</span><span class="informations">831×415 58.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e8ddaefb74f2083645f2f561c3f8a065a6704df.png" data-download-href="/uploads/short-url/8VnwE9I3DkI8bAytGIIE2xzZkAL.png?dl=1" title="Image3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8ddaefb74f2083645f2f561c3f8a065a6704df_2_690x429.png" alt="Image3" data-base62-sha1="8VnwE9I3DkI8bAytGIIE2xzZkAL" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e8ddaefb74f2083645f2f561c3f8a065a6704df_2_690x429.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e8ddaefb74f2083645f2f561c3f8a065a6704df.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e8ddaefb74f2083645f2f561c3f8a065a6704df.png 2x" data-dominant-color="9F9FA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image3</span><span class="informations">902×562 75.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6798d9a9815997e0905931c92e8dec36657291fc.png" data-download-href="/uploads/short-url/eMsETsYPxuMIRx7mkhw6m1iUoVe.png?dl=1" title="Image4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6798d9a9815997e0905931c92e8dec36657291fc_2_690x480.png" alt="Image4" data-base62-sha1="eMsETsYPxuMIRx7mkhw6m1iUoVe" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/6798d9a9815997e0905931c92e8dec36657291fc_2_690x480.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6798d9a9815997e0905931c92e8dec36657291fc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6798d9a9815997e0905931c92e8dec36657291fc.png 2x" data-dominant-color="B1B1B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image4</span><span class="informations">802×558 74.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So when I need to go back ‘live’, I need to redo the hierarchy :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9dd4784df77cb53819c47f121aec470bafc410.png" data-download-href="/uploads/short-url/y2TMNBwKoaENBVtmMgZptGpX2bC.png?dl=1" title="Image5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee9dd4784df77cb53819c47f121aec470bafc410_2_690x482.png" alt="Image5" data-base62-sha1="y2TMNBwKoaENBVtmMgZptGpX2bC" width="690" height="482" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee9dd4784df77cb53819c47f121aec470bafc410_2_690x482.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9dd4784df77cb53819c47f121aec470bafc410.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9dd4784df77cb53819c47f121aec470bafc410.png 2x" data-dominant-color="AEAFB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image5</span><span class="informations">805×563 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>PS1 : when I record a sequence I just click the “record” button, then click again to stop the recording.<br>
PS2 : I saw that I could do live reconstruction but I would like to record the volume reconstruction.</p>
<p>Thanks,<br>
Aurélie</p>

---

## Post #4 by @lassoan (2020-09-03 11:58 UTC)

<p>You can deactivate the OpenIGTLink connection if you want to work with recorded data, and activate the connection if you want to show live data.</p>
<p><a class="mention" href="/u/ungi">@ungi</a> What is your usual workflow?</p>
<p>If we find that common tasks are inconvenient to do then we can improve things (for example, add OpenIGTLink connection activate button on the toolbar or other modules GUI).</p>

---

## Post #5 by @ungi (2020-09-03 14:45 UTC)

<p>Several topics here…</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> said, you need to disable the OpenIGTLink connection (uncheck active) when playing back recorded sequences. A toolbar icon for OpenIGTLink activation switch sounds like a good idea, although I never really felt the need. A typical user is either recording or playing back data, but not switch rapidly between the two. I have never used the rename option in Sequences.</p>
<p>If you have a special use case e.g. you need to replay the recorded sequence immediately after the recording is stopped, then I recommend writing a small module just for your application. It shouldn’t take more than a few dozen lines of code. It could automatically deactivate the connection and replay the recorded sequence.</p>
<p>Volume reconstruction and recording works at the same time. Again, if you don’t want to start these two functions in two separate modules, then you need a small module that starts both when you press a button. Maybe more modules could implement their own toolbars, so users could add more functions to their personal toolbars for the functions they use. Maybe we could add this as part of the default module wizard to motivate more people. But that kind of change would take a long time.</p>
<p>You do need a different transform hierarchy for calibration. But calibration should not be done frequently. And it’s always a good idea to just record calibration data, save, and process it later offline. That way you will have your calibration image sequence archived. And precise calibration requires patience. It is easier when the live hardware is not running next to you.</p>

---

## Post #6 by @AurelieS (2020-09-03 15:12 UTC)

<p>Thank you so much for your responses, it is very clear !<br>
I did not think of activating / deactivating the OpenIGTLink connection, I will try this in my workflow.</p>

---
