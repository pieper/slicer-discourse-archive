# Collaborative planning in Virtual Reality

**Topic ID**: 14841
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/collaborative-planning-in-virtual-reality/14841

---

## Post #1 by @justdcinaus (2020-12-02 02:58 UTC)

<p>Hi<br>
I was wondering if there was any further follow up to the older topic <a href="https://discourse.slicer.org/t/collaborative-surgery-planning-in-virtual-reality/6407" class="inline-onebox">Collaborative surgery planning in virtual reality</a> ?</p>
<p>I have managed to get a good internal view of a heart using volume rendering by removing the lumen using masking - turning the volume hollow.  Our interventional cardiologist was quite impressed with the ability to basically lean into the model and see the relationship between the RV outflow tract and the coronary artery.  Originally he’d asked me to make a print, however viewing it in this manner was quicker and also made the decision on where to cut the model redundant.</p>
<p>Ideally being able to have two people looking at the same view would be of interest.<br>
(if there has been no further development I’ll have a try at getting it going myself)</p>
<p>David</p>

---

## Post #2 by @mohan.kosireddy (2020-12-02 07:03 UTC)

<p>Hi David, This is Mohan. I am interested to work with you. I have been visualizing some of the  Radiology DICOM models in AR. I am interested in Collaboration &amp; single session meetups sharing the medical data digitally using AR &amp; VR.  Reply me, we take it further.</p>

---

## Post #3 by @lassoan (2020-12-03 04:55 UTC)

<p><a class="mention" href="/u/mohan.kosireddy">@mohan.kosireddy</a> what software do you use / plan to develop?</p>
<p><a class="mention" href="/u/justdcinaus">@justdcinaus</a> We use virtual reality for RVOT and other cardiac device implant evaluations extensively. Since single-user setup is trivial and other users can see the Slicer desktop screen and the the live virtual reality stream, we have making collaborative views easier to set up has not been high priority. For now, we can help with setting up shared scenes between multiple workstations and giving advice on how to automate this scene setup using Python scripting.</p>

---

## Post #4 by @mohan.kosireddy (2020-12-03 05:55 UTC)

<p>I use Blender, Autodesk Maya for 3D model enrichment apart from Slicer.<br>
For augmented reality, I use Unity3d. Hardware : Magic Leap, Hololens</p>

---

## Post #5 by @lassoan (2020-12-03 06:15 UTC)

<aside class="quote no-group" data-username="mohan.kosireddy" data-post="4" data-topic="14841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohan.kosireddy/48/9043_2.png" class="avatar"> mohan.kosireddy:</div>
<blockquote>
<p>I use Unity3d</p>
</blockquote>
</aside>
<p>Unity3D has great hardware support (only Unreal engine comes close) but it is very limited when it comes to displaying and interacting with medical images.</p>
<p>There are use cases where Unity3D’s hardware support is essential (HoloLens, Magic Leap) and basic visualization capabilities can be enough - for example patient communication, medical training, and some simple interventional uses.</p>
<p>However, for surgical planning, you need more powerful tools than what gaming engines can provide. For example, in 3D Slicer’s virtual reality implementation you can display 4D CT or echo image of the beating heart (moving in 3D) using volume rendering while you are placing your device. You can complete the full workflow in one software environment, from DICOM import to final virtual reality visualization and interactions, no need for segmentation (as sophisticated volume rendering is available), no need for data exporting, uploading to the device, etc.</p>
<p>If the goal is surgical planning then I would not recommend to redevelop all the planning tools in a gaming engine (Unity3D or Unreal) but instead to use/customize/extend 3D Slicer’s Virtual Reality extension.</p>

---

## Post #6 by @vet0282 (2020-12-03 19:59 UTC)

<p>Hi Andras,</p>
<p>I wonder if there is any possibility to have AR. My understanding is the virtual reality extension does not support AR. So, I was thinking of Unity3D for AR.<br>
I do more orthopedics and would love to register ‘3D surgical planning (implant positioning, osteotomy location/angle, etc)’ to the real patient based on anatomical landmarks, shape matching, or external coordinate systems. I understand hardware support is necessary.<br>
Basically, I am interested in using AR for navigating surgery.</p>
<p>Thanks in advance.</p>
<p>Sun</p>

---

## Post #7 by @lassoan (2020-12-03 20:39 UTC)

<aside class="quote no-group" data-username="vet0282" data-post="6" data-topic="14841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vet0282/48/8747_2.png" class="avatar"> vet0282:</div>
<blockquote>
<p>I wonder if there is any possibility to have AR. My understanding is the virtual reality extension does not support AR. So, I was thinking of Unity3D for AR.</p>
</blockquote>
</aside>
<p>Unity3D is reasonable choice today for displaying and interacting with surface models in AR.</p>
<aside class="quote no-group" data-username="vet0282" data-post="6" data-topic="14841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vet0282/48/8747_2.png" class="avatar"> vet0282:</div>
<blockquote>
<p>I am interested in using AR for navigating surgery</p>
</blockquote>
</aside>
<p>You can certainly create a simple AR application that displays the surgical plan somewhere in the field of view. This is somewhat useful because the surgeon does not need to look up to an overhead monitor, but also somewhat less convenient because you need to wear a bulky device.</p>
<p>The big promise of AR is in-situ visualization, i.e., showing a virtual needle guide or intended location for an implant, so that you can align physical objects with virtual objects/guides. Unfortunately, based on my own experience and what I learned from discussions with other research groups papers: AR headsets that are available today are not suitable for this. Headsets today are not optimized for interaction within reaching distance (30-80cm) but the minimum distance is much farther (200cm for HoloLens, 100-200cm for Magic leap), therefore you cannot see a virtual object and a real object at the same position (your eye cannot focus on both objects at the same time). Tracking stability is not sufficient yet: we would need tracking accuracy of about 0.1mm or so to have total system accuracy of 1mm, but virtual objects on a HoloLens device may easily drift 5-10 millimeters (you can of course add external tracking, but that’s add a whole lot of other issues).</p>

---

## Post #8 by @sarvpriya1985 (2020-12-04 00:19 UTC)

<p>Hi David,</p>
<p>Would you pls let me know how you managed to make the heart hollow. I have tried to use volume rendering and then using thresholds to try make heart hollow. Can you pls let me know how you implement tmasking the lumen and  then hollowing heart. Would like to apply this approach.</p>
<p>Thanks<br>
Sarv</p>

---

## Post #9 by @cshreyas (2021-02-06 19:43 UTC)

<p>Hello All,<br>
I am trying to integrate Magic Leap (VR initially) with Slicer for detecting bur hole using MRI images. Has anyone been able to integrate Slicer with Magic leap?</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2021-02-07 04:59 UTC)

<p>We (and several other groups) used the HoloLens for burr hole placement (see <a href="http://perk.cs.queensu.ca/sites/perkd7.cs.queensu.ca/files/Baum2020a.pdf">paper</a>, <a href="https://engineering.queensu.ca/news/2018/09/queens-students-developing-new-neurosurgical-aid.html">video</a>). Since minimum user interaction was needed (patient registration and after that just show/hide the skin surface, brain, and planned drill hole) and Unity already supported the HoloLens, we decided to use Slicer for creating the models and use Unity for displaying them in AR. After initial feasibility was demonstrated on dozens of phantom studies and 15 patient cases, we put the project on hold, because while the system worked for this simple, non-demanding clinical application, we were not confident that currently available technology can be effectively used for more difficult procedures (where higher accuracy and more complex user actions are needed and an AR system could have significant clinical utility).</p>
<p>Since we did not proceed further from initial feasibility, we did not complete our live Slicer/Unity bridge for sending of models and transforms to Unity from Slicer. Still, you might find bits and pieces of the software that we developed useful: <a href="https://github.com/PerkLab/HololensQuickNav">HololensQuickNav</a>, <a href="https://github.com/PerkLab/OpenIGTLinkUnity">OpenIGTLinkUnity</a></p>
<p>Thomas Muender and his team from Uni Bremen worked on a Slicer/Unity bridge, too. See<br>
<a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/SlicerToUnity/">Project week page</a> and <a href="https://github.com/thomasMuender/SlicerToUnity">repository</a>.</p>
<p><a class="mention" href="/u/amine_ziane">@Amine_Ziane</a> recently asked about using Unity for zSpace device - see <a href="https://discourse.slicer.org/t/transfer-scene-files-from-3dslicer-to-unity3d/15729/17" class="inline-onebox">transfer scene files from 3DSlicer to Unity3D - #17 by Amine_Ziane</a>. Maybe you can try to work together.</p>

---

## Post #11 by @cshreyas (2021-02-07 18:03 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , Thanks a lot for the information.<br>
My actual goal is to use MRI images and create path planing for neuro robots. I am exploring options to import 3D Slicer images to Magic leap.</p>
<p>After browsing through various discussions in this forum few options pops up.</p>
<ol>
<li>As you mentioned, create bridge between 3D Slicer and Unity3D</li>
<li>Create bridge between 3DSlicer and Unreal engine.</li>
</ol>
<p><a class="mention" href="/u/amine_ziane">@Amine_Ziane</a> , I would glad to collaborate. Please let me know.</p>

---

## Post #12 by @lassoan (2021-02-07 18:42 UTC)

<aside class="quote no-group" data-username="cshreyas" data-post="11" data-topic="14841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/e56c9b/48.png" class="avatar"> cshreyas:</div>
<blockquote>
<p>My actual goal is to use MRI images and create path planing for neuro robots. I am exploring options to import 3D Slicer images to Magic leap.</p>
</blockquote>
</aside>
<p>Surgical planning typically occurs before the procedure in desktop 3D environment (but immersive virtual reality looks promising, too). Augmented reality in the operating room is extremely limited due to constraints on available time, space, sterility requirements, etc. What is your planned workflow?</p>

---

## Post #13 by @Amine_Ziane (2021-02-07 18:58 UTC)

<p>Would you help me to make my Volume rendering thanks to my MRI images I have in unity ? please</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5deed1f4aa1bc88e59704b179524353ec79a612e.jpeg" data-download-href="/uploads/short-url/doY4CxbDGhRBpD13QxwJtvXHOxM.jpeg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deed1f4aa1bc88e59704b179524353ec79a612e_2_472x248.jpeg" alt="image.jpg" data-base62-sha1="doY4CxbDGhRBpD13QxwJtvXHOxM" width="472" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deed1f4aa1bc88e59704b179524353ec79a612e_2_472x248.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deed1f4aa1bc88e59704b179524353ec79a612e_2_708x372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5deed1f4aa1bc88e59704b179524353ec79a612e_2_944x496.jpeg 2x" data-dominant-color="353535"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1319×692 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @cshreyas (2021-02-07 19:07 UTC)

<p>Thats true. Augmented reality in operating room would be great but doubt the effectiveness with current limited AR capabilities and resolutions for life critical applications.</p>
<p>In my opinion, focusing in VR could be a good start for now.</p>

---

## Post #15 by @lassoan (2021-02-07 19:10 UTC)

<aside class="quote no-group" data-username="Amine_Ziane" data-post="13" data-topic="14841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amine_ziane/48/8989_2.png" class="avatar"> Amine_Ziane:</div>
<blockquote>
<p>Would you help me to make my Volume rendering thanks to my MRI images I have in unity ?</p>
</blockquote>
</aside>
<p>You can try to display exported surface models instead of using volume rendering. Structures are easy to visualize using volume rendering are most often easy to segment, too.</p>
<p>Native volume rendering packages in Unity are extremely limited. They cannot reproduce the same results as VTK, but if your specific needs are fulfilled by any of the volume rendering packages available for Unity then you can certainly use them. I cannot help with more specifics, such as which Unity asset to use, and how - I just remember that what we used was an inexpensive package that you could get for a few ten $ and it could do simple opacity mapping and plane clipping. If you deploy to desktop then you may be able to use VTK in Unity via Activiz (Kitware’s paid C# wrapper for VTK).</p>

---

## Post #16 by @cshreyas (2021-02-07 19:12 UTC)

<p>yes, I can explore the options.</p>

---

## Post #17 by @Amine_Ziane (2021-02-07 21:18 UTC)

<p>okay thanks, so how can I display the exported surface models instead of using volume rendering in untiy3D ?</p>

---

## Post #18 by @lassoan (2021-02-08 05:55 UTC)

<p>See response here: <a href="https://discourse.slicer.org/t/transfer-scene-files-from-3dslicer-to-unity3d/15729/22" class="inline-onebox">transfer scene files from 3DSlicer to Unity3D - #22 by lassoan</a></p>

---
