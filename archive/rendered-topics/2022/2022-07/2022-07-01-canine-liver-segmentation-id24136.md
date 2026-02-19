---
topic_id: 24136
title: "Canine Liver Segmentation"
date: 2022-07-01
url: https://discourse.slicer.org/t/24136
---

# Canine Liver Segmentation

**Topic ID**: 24136
**Date**: 2022-07-01
**URL**: https://discourse.slicer.org/t/canine-liver-segmentation/24136

---

## Post #1 by @sandigeeup (2022-07-01 09:49 UTC)

<p>Hi, I am segmenting a Canine liver. Sadly, this is not as easy as segmenting a human liver as the canine liver has 4 lobes and 4 sub lobes. Also because of the way the liver is in situ, the lobes overlap and are deeply fissured. This is leaving me with an issue because the liver lobes although attached are quite individual features. But because the tissue is the same and they overlap in the abdomen, I don’t get any individual features of the anatomy, it’s on big blob. Should I mark out on the CT each lobe by individual colours? or is there something I’m missing here? also is it possible to rotate the CTs in the frame to flip them round?</p>

---

## Post #2 by @RafaelPalomar (2022-07-04 07:00 UTC)

<p>Hello.</p>
<p>I have been working on planning of liver resections (humans) and we don’t separate the lobes; all the parenchyma is a single object. We have a couple of tools for liver analysis and resection planning <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SlicerLiver/" rel="noopener nofollow ugc">here</a>. They will be released as a Slicer extension soon; you can have a look at it and see if it is something your use case could benefit from. If the lobes are completely indistinguishable maybe you could separate them by virtual cuts (either planes or a deformable surfaces), but of course, this would be only an approximation.</p>
<p>There is also a great extension for liver anatomy annotation <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" rel="noopener nofollow ugc">here</a>, maybe it does have some useful tools for your case.</p>
<p>When it comes to seeing rotated 2D views, below in the picture I have rotated the coronal plane around. I have marked with a red circle the button that enables the plane rotation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa418f9e93c154eb8aec61d6a6349adeb3c67c67.jpeg" data-download-href="/uploads/short-url/zHRPy2q7JupCSuh6fv99wNiNJUH.jpeg?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa418f9e93c154eb8aec61d6a6349adeb3c67c67_2_690x388.jpeg" alt="screenshot" data-base62-sha1="zHRPy2q7JupCSuh6fv99wNiNJUH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa418f9e93c154eb8aec61d6a6349adeb3c67c67_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa418f9e93c154eb8aec61d6a6349adeb3c67c67_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fa418f9e93c154eb8aec61d6a6349adeb3c67c67_2_1380x776.jpeg 2x" data-dominant-color="757376"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1920×1080 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I hope this helps.</p>
<p>Regards.</p>

---

## Post #3 by @lassoan (2022-07-04 12:26 UTC)

<p>We used Surface Cut effect (in SegmentEditorExtraEffects extension) for cutting up the liver to segments manually. You may give it a try.</p>
<p>You could also train deep learning models to automate parts or the whole segmentation process.</p>
<p>So, as you can see, there are many existing tools and potential approaches. The best method heavily depends on your requirements - how many cases you need to segment, what exactly you need to segment, for what purpose, with what accuracy, what time constraints, what skills the operator can expect to have, etc.</p>

---

## Post #4 by @sandigeeup (2022-07-04 13:17 UTC)

<p>Hei, Andras, Thank you for your response and the recommendation. I will try this. It is for my thesis, so the pressure is on!! I must segment a healthy and abnormal Canine Liver and vessels+ gall bladder; it is not easy as the liver in situ overlaps. Also, the vessels are proving exceedingly difficult to segment. It has taken me 3 days just to get a basic segmentation. As part of my thesis, I also need to find a way to measure the tumour as a percentage of liver volume, so I need to do that before I use the surface cut effect, I think.</p>

---

## Post #5 by @hherhold (2022-07-04 13:36 UTC)

<p>Manual segmentation is needed for some things and it can be time consuming. Just for comparison, segmenting detailed tracheal architectures of some insects has taken a couple of weeks per scan. Though it could be I’m just a glutton for punishment.</p>

---

## Post #6 by @sandigeeup (2022-07-04 14:06 UTC)

<p>Thank you, Rafael. This project is for my thesis. The parenchyma in the canine is not a single object. I did try the formed surfaces and it sort of looked ok. But I have to model these and retop in 3dmax, and texture to look like a real liver, then use unity as an aid to present canine liver with and without tumours. I’m finding a really difficult to get the vessels right, any advice? thanks S:)</p>

---

## Post #7 by @sandigeeup (2022-07-04 14:08 UTC)

<p>A couple of weeks, that’s madness!! Good luck, show us your work when you are done, would be interested to see it.</p>

---

## Post #8 by @hherhold (2022-07-04 14:52 UTC)

<p>In progress… submitting soon.</p>
<p>One specimen - Madagascar hissing cockroach respiratory system:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8598f74798b4d10e09bf6f2bfc0e7676b9680958.jpeg" data-download-href="/uploads/short-url/j3RembbZplbRUpySWMP2ga9jpOw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8598f74798b4d10e09bf6f2bfc0e7676b9680958_2_690x215.jpeg" alt="image" data-base62-sha1="j3RembbZplbRUpySWMP2ga9jpOw" width="690" height="215" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8598f74798b4d10e09bf6f2bfc0e7676b9680958_2_690x215.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8598f74798b4d10e09bf6f2bfc0e7676b9680958_2_1035x322.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8598f74798b4d10e09bf6f2bfc0e7676b9680958_2_1380x430.jpeg 2x" data-dominant-color="CEAE8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×600 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @sandigeeup (2022-07-04 15:01 UTC)

<p>Omg, now I see why that’s amazing!! Well done! What type of data set did you use?</p>

---

## Post #10 by @hherhold (2022-07-04 15:52 UTC)

<p>It’s a micro-CT scan at about 30 micron resolution. Segmented in Slicer (manually, using various techniques), models exported to Blender, and rendered using RenderMan (Pixar). (You don’t need RenderMan, I’m just a huge fan.)</p>

---

## Post #11 by @sandigeeup (2022-07-04 16:17 UTC)

<p>Nice! I will export mine to 3DS Max to model and retop, texture, may use ZBrush for retop though, heard it’s super quick and efficient. I have not used Blender yet, although I wish I had, just not enough time to learn something new at this stage, how easy is it?</p>

---

## Post #12 by @hherhold (2022-07-04 16:35 UTC)

<p>All 3D packages have a learning curve, and they all have their user interface quirks. Blender has had a reputation for having a steeper learning curve than most, but this is largely historical, as a lot of work has gone into the UI (and pretty much every other area of Blender) in the last 3-4 years. My reasons for using blender have been largely financial - I didn’t have the money at the time to invest in a 3D package, so Blender was it, and after several years sunk into it I have no intentions of switching. I have a colleague who used LightWave for years but switched to Blender after NewTek basically end-of-lifed LightWave, and after coming up to speed on it, he likes it a lot. Broadly speaking, there aren’t many features left that make one 3D app substantially better than the others, so I’d say if it works for you, stick with what you have.</p>
<p>That said, there are <em>a ton</em> of Blender tutorials out there. Blender Guru’s Beginner series on YouTube is a commonly cited one that I like a lot (<a href="https://www.blenderguru.com" rel="noopener nofollow ugc">https://www.blenderguru.com</a>).</p>
<p>ZBrush is indeed very powerful, although some of my models are too large for it (approaching or more than 100 million polys). I’ve not spent as much time with it as I should - it has quite the learning curve as well, and I’d <em>HIGHLY</em> recommend a drawing tablet with it.</p>
<p>I’d also recommend that drawing tablet for use with Slicer if you’re doing a lot of manual segmentation. My Wacom Intuos Pro (size medium) has many many <em>many</em> miles on it.</p>

---

## Post #13 by @sandigeeup (2022-07-04 16:43 UTC)

<p>Hmmm, yeah once I have this project out the way and my master is done I won’t have access to 3dSMax, I’ll have to find a replacement. Blender and Maya are the top suggestions, although Maya is also with Autodesk, so cost-prohibitive. I have an Apple Mac Pro and Wacom Intuos Pro, so I need to make them work for me. How are you using your Wacom, I’ve had mine for a few yrs. and barely opened the box!!</p>

---

## Post #14 by @hherhold (2022-07-04 16:47 UTC)

<p>I use it for doing all manual segmentations - painting with thresholded brush, masking, etc. I have the buttons hot-keyed to Slicer functions so I basically never take my hands of the stylus or mouse while working. Saves a lot of time for detail work.</p>
<p>I basically use only open-source software (with the exception of RenderMan, which I use because I’m a fanboi). <a class="mention" href="/u/muratmaga">@muratmaga</a> (SlicerMorph) has called this approach “future proofing” yourself, which I have found to be a perfect description - I know that I will not rely on proprietary software in the future to look at my data or do my work.</p>

---

## Post #15 by @hherhold (2022-07-04 16:50 UTC)

<p>Maya is great for character animation, and somewhat for modeling. Though Blender is catching up rapidly in these areas, and if you’re not using the feature set that Maya excels in, it’s not clear what the extra cost buys you.</p>
<p>Expressing opinions on 3D packages has been known to start arguments in certain circles (not here, however). I’ll close with “stick with what works for you”.</p>

---

## Post #16 by @sandigeeup (2022-07-04 16:57 UTC)

<p>Maya will be another lesson to learn. Yeah, I don’t get into those debates, and defo will use what I know… for this process anyway. Thanks for the chat, great to know someone knows what they are doing!!</p>

---

## Post #17 by @sandigeeup (2022-07-04 17:00 UTC)

<p>Just unleashed my Wacom…not sure what to do next…but will work it out <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @hherhold (2022-07-04 17:07 UTC)

<p>It’s pretty handy in Slicer.</p>
<p>I need to spend more time with ZBrush, but it seems like it should be bundled with a tablet. If you’re doing any detailed re-topo or surface painting work, I think it will be <em>very</em> useful.</p>

---

## Post #19 by @sandigeeup (2022-07-04 18:40 UTC)

<p>Yeah, I invested in my iPad Pro this year and have a great dell laptop and the Wacom, so I’m sort of geared up for success…just need to figure out all the processes at each stage to get where I need to be.</p>

---
