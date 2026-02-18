# SpatialLabs stereoscopic display

**Topic ID**: 34800
**Date**: 2024-03-09
**URL**: https://discourse.slicer.org/t/spatiallabs-stereoscopic-display/34800

---

## Post #1 by @Mark_Ryan (2024-03-09 16:44 UTC)

<p>I recently purchased the SpatialLabs monitor - the pro version and was wondering if anyone had experience with this or something similar.  The display works with 2 eye tracking cameras and a lenticular display to show a 3 dimensional image without requiring glasses.  The software is relatively barebones but so far I have been able to view STL and OBJ files successfully.  There is also developer notes of how to integrate with OpenXR and Unreal engine but I have limited experience with those.</p>
<p>I would like to find a way to view volume renderings in the display somehow., since that would allow viewing in the OR without 3D glasses or other specialized hardware.  I found some prior forum posts about OpenXR integration into 3D slicer but I’m not sure what had come of it. Basically seems like I have to make the program think that its output is either going to a VR headset or a stereoscopic display.  Any suggestions?</p>

---

## Post #2 by @lassoan (2024-03-09 17:14 UTC)

<p>Recent efforts in stereo viewing focused on AR/VR headsets, because these devices made most 3D displays obsolete. Headsets are more portable, cheaper (Meta Quest headset is $300-500), provide larger field of view (full immersion), and offer full 6-degree-of-freedom viewing and interaction. When you need to see the surrounding real world then you can use an AR headset, such as the HoloLens. Both AR and VR headsets are usable in Slicer view the <a href="https://github.com/KitwareMedical/SlicerVirtualReality">SlicerVirtualReality extension</a>.</p>
<p>For headset-free viewing you can use holographic displays, such as the <a href="https://lookingglassfactory.com/">LookingGlass</a>, which is already supported by Slicer. Holographic displays have the advantage that they can be viewed by many viewers (no head tracking is needed).</p>
<p>Single-user 3D displays don’t really have much place anymore other than maybe they can try to compete in price or image resolution. I think such monitors (such as the zSpace) are already usable with Slicer (maybe via SlicerVirtualReality extension?). If SpatialLabs provide OpenXR interface then you can probably use SlicerVirtualReality extension. Otherwise you can ask the manufacturer to contact Kitware about how they could add VTK support to their monitor.</p>

---

## Post #3 by @Mark_Ryan (2024-03-10 22:01 UTC)

<p>I appreciate the response…I’ve used the looking glass, but hardware requirements are steep and price rises dramatically once you move beyond the Portrait device.  The spatial displays seem like a better intra-operative option, since resolution and performance are better on most hardware and there is no need to wear specialized glasses or VR headsets. If you haven’t tried using one of the eye-tracking monitors I highly recommend it.  Main drawback is that it’s 1 viewer at a time, but thats less of a concern using in the OR as reference.</p>
<p>Will definitely try your suggestions. The volume renderings give a lot more detail than the segmentations (at least when I do it) and would be great to see how it looks on there.</p>

---

## Post #4 by @lassoan (2024-03-10 22:24 UTC)

<p>Slicer can now display volume rendering directly in the HoloLens2. The huge advantage of augmented reality headsets compared to 3D displays is that you can place the volume inside the patient at the correct physical location and use it for guidance. Simply manually aligning the visible skin surface can be sufficiently accurate for larger, superficial targets. There are software libraries for automatic alignment and more accurate tracking, but those are not yet integrated into Slicer.</p>

---

## Post #5 by @Mark_Ryan (2024-03-11 00:52 UTC)

<p>Unfortunately it seems like resolution on the AR goggles isn’t quite there yet. The Ultraleap is pretty good but viewing window is small . Hololens 2 has similar issues but we have investigators who use it for telestrating during simple procedures.  Use VR and AR (Quest 2 and Quest 3 passthrough) with MedicalHolodeck program for planning approach and 3D slicer for fast volume rendering or segmentation/printing.</p>
<p>Had been struggling with a good intraoperative solution for a roadmap-type reference, since most of my partners wouldn’t be willing to wear hardware/goggles in the OR. These seem to fit that need - have 2 cameras which t ack eye and head movements and adjust the view to your position. Illusion is very convincing and have trialed some segmentations with it and had good results. Problem is those take time and sometimes volume renderings get the job done. Version I’m using is Acer SpatialLabs View Pro, but there are nicer versions made by Sony and others.</p>
<p>Looking glass product is excellent (I have a LKG Go preordered), but cost/size is an issue and requires significant graphics hardware to render from so many angles. It’s the only non-goggles solution I’m aware of with group viewing though.</p>
<p>Thanks again for your response. I don’t have any programming experience so your replies here and in the forums have been very helpful. If you know of any AR overlay capabilities for laparoscopy I would be very interested to hear about it since most of my cases are done that way (pediatric surgery).</p>

---

## Post #6 by @lassoan (2024-03-11 02:55 UTC)

<p>The HoloLens2 is excellent for in situ visualization. Both the field of view and resolution is sufficient.</p>
<p>If you just want to display 3D images somewhere above the patient then a 3D monitor is usable for that. However, stereopsis is only one of the many depth cues (you also perceive depth from lighting, motion, occlusion, size, texture, etc), so while using a stereo display improves depth perception, it is not a game changer. The proof for this is that despite the 3D TV boom in the early 2010s when stereo displays were available at a very low pricepoint at many sizes, using various technologies (including active glasses, passive glasses, and without glasses), it still did not get traction in clinical use. It is still possible that 3D monitors will make a comeback (maybe because you find some really good applications), but right now it seems that augmented reality headsets have more potential.</p>

---

## Post #7 by @Mark_Ryan (2024-03-11 12:54 UTC)

<p>I might just have to give the Hololens 2 another try then. Still fairly cumbersome in the OR but not too many options.  An I’ve learned that the only way to really assess these devices is to wear them yourself.  The listed display resolution is 1440x936, whereas the one I’m using is a 4K display with each eye field receiving 1920x1080. How detailed are these images when viewing through the device?  The best use cases in pediatrics are things like conjoined twins and tumors with complex, irregular vasculature.  Those can be really painful to segment, and some of the vessels are 1-2 mm in diameter (the IVC on some of these kids is around 1-1.5 cm).</p>
<p>The view on the spatial display reminds me a little of the old active shutter glasses and 3D, especially in programs that aren’t optimized for stereoscopic display (looks like a bunch of cardboard cutouts moving in parallel).  Also if you don’t optimize focal length it’s easy to end up cross-eyed. 10 years ago I owned both a 3D vision monitor and a 3D television , but the technology seems to have improved significantly since then.  Again thanks for your insight - not much experience with this kind of thing in pediatric surgery world so its nice to discuss with someone who knows this stuff.</p>

---

## Post #8 by @lassoan (2024-03-11 14:49 UTC)

<p>How useful do you find the additional depth cue of the 3D monitor? What is that you can see on the 3D monitor that you cannot already see on a regular 2D monitor? You can perceive depth more directly and slightly move your head to see a bit behind structures, but I’m wondering if this is something really significant.</p>
<p>Regardless of resolution, price, ease of use, etc. - 3D monitors cannot compete with the HoloLens unless they make the image appear as floating inside the patient. The main challenge in using the HoloLens is not about image quality, but</p>
<ul>
<li>how conveniently (and quickly and accurately) you can align the virtual model with the patient</li>
<li>how to keep the model position and shape up-to-date during the procedure as things move around</li>
<li>how to interact with the device: there are many options - hand gestures, voice commands, controller in sterile bag - but each has its own limitations</li>
<li>how to wear it: it is quite comfortable, but you may still want to flip it up or remove from your head beause it still darkens the view a little bit or may add some extra glare, and may be in the way if you want to use a microscope</li>
</ul>
<p>Still, if you think seeing the 3D model inside the patient in the correct physical location could be useful then it is worth a try. You would need a technician to help with it in the OR (prepare the visualization, put and remove the device from your head, help with controls, etc.)</p>

---

## Post #9 by @Mark_Ryan (2024-03-11 19:54 UTC)

<p>From what I’ve seen, just putting the volume renderings or segmentations on the OR monitors can be difficult to interpret unless you’re able to move the model.  Our current solution to this is to connect our laptop workstation (RTX 4070 with 64 GB RAM) to the DVI or HDMI port on the boom in the OR. The image can then be shown through as many displays as we would like in the OR, usually between 2 and 4.  Movement of the model is done using a Leap Motion 2 controller, which allows you to manipulate the model and preserve sterility. What the 3D display does is minimize the amount of manipulation required to gain an understanding of the image.</p>
<p>I think we might be using these for different things. For us, AR overlay during open surgery  may not add much because the structures are small in general, and you can usually identify the limits of solid organ tumors on palpation.  The challenging open situations for us are ones in which there are complex networks of aberrant vessels within a tumor.  The visual fidelity on the Hololens may not be enough to overlay multiple 2-3 mm vessels and follow with manipulations of the tumor about its axis (but I would be happy to be proven wrong).</p>
<p>For us the focus is on the preoperative planning phase or providing a roadmap for reference in the OR .  The VR headsets provide good pictures for the first part but are not great for the second.  The other consideration for us is that a lot of our complex cases are done under magnification with loupes on.  Transitioning to the Hololens and back throughout the case would be cumbersome and might be difficult to maintain sterility.  I’m curious how you and others have dealt with this in the past.</p>
<p>Do you have particular cases where you find this to be especially helpful? There is some overlap between adult and pediatric surgery but I’m always interested in finding new ways to  improve how we do things.  A lot of our complex cases are done under laparoscopy or robotically (choledochal cysts, anorectal malformations, etc).  AR solutions that provide overlay data during laparoscopy or open with under 2.5-3.5x magnification would be ideal, but I don’t think those technologies exist  yet.  Thanks again for answering my questions.  I’m still learning as I go here.</p>

---

## Post #10 by @lassoan (2024-03-12 05:41 UTC)

<aside class="quote no-group" data-username="Mark_Ryan" data-post="9" data-topic="34800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_ryan/48/69613_2.png" class="avatar"> Mark_Ryan:</div>
<blockquote>
<p>What the 3D display does is minimize the amount of manipulation required to gain an understanding of the image</p>
</blockquote>
</aside>
<p>This is indeed useful. I would just add that there are many other ways to improve depth cues or make the images easier to interpret. For example, we recently added colored volume rendering and ambient shadows (see some example images <a href="https://discourse.slicer.org/t/improve-ambient-occlusion-in-volume-rendering/33590/6">here</a> and <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981">here</a>), which can be used in addition or instead of stereo volume rendering to greatly improve understanding of the 3D renderings.</p>
<aside class="quote no-group" data-username="Mark_Ryan" data-post="9" data-topic="34800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_ryan/48/69613_2.png" class="avatar"> Mark_Ryan:</div>
<blockquote>
<p>I think we might be using these for different things. For us, AR overlay during open surgery may not add much because the structures are small in general, and you can usually identify the limits of solid organ tumors on palpation</p>
</blockquote>
</aside>
<p>I agree, these are two quite distinct use cases. The HoloLens is already proven to be useful for large and superficial targets, for low-accuracy applications (e.g., give confidence to surgeons in determining skin incison location), but may not be ideal for microsurgeries.</p>
<aside class="quote no-group" data-username="Mark_Ryan" data-post="9" data-topic="34800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_ryan/48/69613_2.png" class="avatar"> Mark_Ryan:</div>
<blockquote>
<p>AR solutions that provide overlay data during laparoscopy or open with under 2.5-3.5x magnification would be ideal, but I don’t think those technologies exist yet.</p>
</blockquote>
</aside>
<p>Lots of solutions were developed for displaying image overlay in laparoscopes or microscopes in the past 20 years, but they have not become widely used clinically - probably because they did not work that well in practice. Seeing recent progress in imaging AI, it is quite likely that real-time AI image annotations will become available in products of all the large laparoscopy vendors within a few years.</p>
<p>To add AR to surgical loupes, maybe the easiest solution could be to use digital loupes (like <a href="https://www.nueyes.com/nuloupes">nuloupes</a> or <a href="https://www.mantishealth.com/">mantis</a>) and external tracking.</p>

---

## Post #11 by @Mark_Ryan (2024-05-21 15:21 UTC)

<p>Have been intermittently working on making volume rendering output translate to this monitor but without success at the moment.  I use a program called MedicalHolodeck for viewing volume renderings in VR with excellent results. If I create segmentations I can view them easily using the viewer included by SpatialLabs.  The quality of the volume rendering images I get in 3D Slicer is excellent, but there are just limits to viewing 3D images on a 2D screen, even with the additions to improve depth cues.</p>
<p>I’ve reached out to the display company to see if they have any ideas, but I don’t have high hopes for that one.  They do have extensions for Unreal Engine, Unity, and NVIDIA Omniverse that allow you to view images within the editor in stereoscopic 3D on the monitor.  So it definitely seems possible.  Since the VR extension to 3D slicer allows for OpenXR output it seems like there should be a way to transfer that to the display.</p>
<p>If you haven’t tried one of these types of displays, I highly recommend it.  The clarity is much better than the smaller holographic displays (haven’t gotten to try the large ones for budget reasons) and the hardware requirements are significanty reduced.  Most importantly, it avoids the need to wear glasses or VR goggles to get a true 3D image.  It even alters the perspective on the image based on your head and eye movements. The only major drawback is that only one user can view it at a time since it relies on eye tracking, in which case the hologram is a better option.</p>
<p>I may just have to make my own extension to 3D Slicer to make this possible, but I don’t even know where to begin with that.  Any help is appreciated, as always.</p>

---

## Post #12 by @lassoan (2024-05-21 16:22 UTC)

<p>If SpatialLabs supports OpenXR then you don’t need to do anything, Slicer can already show 3D volume rendering on those screens! You can configure 3D display on that screen similarly to all other OpenXR-compatible displays as described <a href="https://github.com/KitwareMedical/SlicerVirtualReality?tab=readme-ov-file#setup">here</a>.</p>

---

## Post #13 by @Mark_Ryan (2024-07-25 00:22 UTC)

<p>Thought I’d provide an update - was able to get basic functionality using SteamVR as the default XR runtime and using the SlicerVR extension. There is an “AcerXR” setting in the display’s software that allows transmission of VR data to the monitor.</p>
<p>The head tracking is off and still have to figure out controls, but the static images are three dimensional and pretty compelling. Definitely recommend giving it a shot. The stuttering in the video has to do with the phone alternately capturing images being sent to each eye, but unfortunately these kind of things don’t translate well to video.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b050a97d2345f3e7996c73dde0ecd8434dacf26.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b6d5e11e862b437314b925579ce9150d7c063f4.jpeg">
  </div><p></p>

---

## Post #14 by @Mark_Ryan (2024-07-25 18:57 UTC)

<p>Submitted this in the developers area for the SlicerVR extension:</p>
<p>Slicer 5.6.2 crashed whenever I would attempt to connect to the hardware.</p>
<p>However, yesterday I tried the extension again using the 5.7 preview build and was able to connect by setting StearmVR as the default OpenXR runtime and enabling AcerXR (their included OpenXR extension).  I’ve attached a short video to show it functioning in the display, but there is some distortion due to picking up the images being sent to each eye.  The device changes the viewing angle with head movement, so you are able to look around corners within a certain viewing angle.</p>
<p>I’ve gotten this far, but I’m a surgeon with no programming background.  I wanted to see if any of the developers thought these ideas would be possible:</p>
<ol>
<li>
<p>The image moves with my head movement rather than being static.  So as long as I don’t move my head the image is good, but I lose the ability to look at the object from different angles.  Obviously this software was designed with a VR headset in mind, but I was hoping there was some way to alter the camera(s) to keep the image in one place.</p>
</li>
<li>
<p>For obvious reasons, there is not any functionality if I try to manipulate the image using the mouse.  I am able to change opacity/presets for the volume rendering, which updates right away.  However, if I rotate the image I have to then switch to the VR options tab and click on “set virtual reality view to match reference view”.  Is there any way to manipulate the image directly using the mouse?  Would I have more luck with an XBox controller?  I have a Quest 3 I can use, but I’m not sure if I can pair the controllers without also using the headset as a display.</p>
</li>
<li>
<p>The view shown in the 3D window within 3D slicer does not match the one on the 3D monitor.  I have to position the rendering at the very bottom of the window for it to appear.  I’ve setting the camera to a point on the image and centering the view, but no luck so far.  I suspect the perspective on a VR headset is different somehow.</p>
</li>
</ol>
<p>Anyway, thank you for all your hard work on this extension.  If you haven’t tried one of these monitors I highly recommend it.  The images are compelling and not needing glasses makes it far more accessible.  If there is any tech I would bring into the OR so far, this is it.</p>
<p><a href="https://github.com/user-attachments/assets/e1448a96-9ec3-4371-b297-caacb1e20774" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/user-attachments/assets/e1448a96-9ec3-4371-b297-caacb1e20774</a></p>

---

## Post #15 by @lassoan (2024-09-04 03:24 UTC)

<p>Thanks for the update, very nice progress! It is good to know that this sort of works.</p>
<p>If head tracking is disabled then there is very limited possibility to look around corners. If head tracking is enabled then the 3D content should appear to be stationary in 3D, and if that position is near the screen then you should be able to look around corners.</p>
<p>In the first video where the model moved off the screen as you were moving, so head tracking must have been enabled. But since the model moved a lot and did not rotate much, most likely its position and size were not set correctly (it was very far from the screen and to compensate for that, its physical size was set to be very large).</p>
<aside class="quote no-group" data-username="Mark_Ryan" data-post="14" data-topic="34800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_ryan/48/69613_2.png" class="avatar"> Mark_Ryan:</div>
<blockquote>
<p>if I rotate the image I have to then switch to the VR options tab and click on “set virtual reality view to match reference view”.</p>
</blockquote>
</aside>
<p>This indicates that the object was very far from the camera (probably the same issue as the previous).</p>
<aside class="quote no-group" data-username="Mark_Ryan" data-post="14" data-topic="34800">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_ryan/48/69613_2.png" class="avatar"> Mark_Ryan:</div>
<blockquote>
<p>I have to position the rendering at the very bottom of the window for it to appear.</p>
</blockquote>
</aside>
<p>This may be again the same issue.</p>
<p>Overall, it is possible that all three problems are due to that “set virtual reality view to match reference view” needs to be tuned/fixed for this device: the object position (focal point position of the desktop 3D view’s camera) should appear near the screen plane of the stereo display.</p>

---

## Post #16 by @Mark_Ryan (2024-09-04 04:18 UTC)

<p>Thanks for responding. Will see if there is a way to adjust the viewpoint independently from the VR camera. Right now the reference button is the only method on have to refresh changes within the display.</p>
<p>You’re right that likely the object is far away, so any head movements are exaggerated on the display. The display excels when objects are placed just in front of the plane of the screen, since the object will appear to project into the space between you and the display. Will have to see if there is something in the VR plugin I can tweak to change that.</p>
<p>Have also tried the 16 inch looking glass OLED screen, and quality is good in 3D slicer 5.2 and 5.4. Lose out on some of the options present in the newer versions, but seems like those were the last ones to have holographic display extensions. Supposedly they are working on an update for the newer displays.</p>

---
