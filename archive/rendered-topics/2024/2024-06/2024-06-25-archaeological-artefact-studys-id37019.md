---
topic_id: 37019
title: "Archaeological Artefact Studys"
date: 2024-06-25
url: https://discourse.slicer.org/t/37019
---

# Archaeological Artefact Studys

**Topic ID**: 37019
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/archaeological-artefact-studys/37019

---

## Post #1 by @gavotny (2024-06-25 21:13 UTC)

<p>Hi I am an archaeologist experimenting with photogrammetry and 3d modeling, I came across your software while trying to find ways to interrogate my models for dimension info. I was wondering if there was a way to change the units of measurement within your application to match my models. They are taken in meters is there a way to change or amend the scale within the app?</p>
<p>Also is there a way to cross section a 3D model, essentially doing the reverse of the segment approach of your software.</p>

---

## Post #2 by @muratmaga (2024-06-25 21:27 UTC)

<p>If you know for a fact that the units of your 3D models are in meters, then you can set the default units from millimeters to meters in Slicer (Edit-&gt;Application Settings-&gt;Units).</p>
<p>Unfortunately not all modules of Slicer supports this custom units. So your mileage may vary.</p>
<p>Another approach that will guaranteed to work, is to create a meter to millimeter transformation (go to transforms module, create a new transform called m2mm, and set the first three diagonals values to 1000). You can then assign your 3D model to this transform, and then when you measure distances they should be reported in correct mm values.</p>

---

## Post #3 by @gavotny (2024-06-26 08:45 UTC)

<p>Thanks so much. That makes a lot of sense, and I can give that a try. You guys are quick at getting back to me!</p>

---

## Post #4 by @cpinter (2024-06-26 10:32 UTC)

<aside class="quote no-group" data-username="gavotny" data-post="1" data-topic="37019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b9e5f3/48.png" class="avatar"> gavotny:</div>
<blockquote>
<p>Also is there a way to cross section a 3D model, essentially doing the reverse of the segment approach of your software.</p>
</blockquote>
</aside>
<p>Can you please elaborate? I’m trying to imagine the reverse of segmentation but it gets me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> The only thing that comes to mind from cross section are the 2D (MPR) views, but you can already see those.</p>
<p>This is an interesting use case. If it’s not an inconvenience I’d love to hear a bit about the project.</p>

---

## Post #5 by @gavotny (2024-06-26 14:46 UTC)

<p>Hi, of course, I can elaborate. I’m not sure I’m getting it right, but I assume the software builds a 3D model from medical scan data of some sort. I am essentially starting from the end. I have built 3D scans of archaeological artefacts, namely flint tools, and would like to be able to view them in cross-section if that makes sense. I am mainly trying to gain as much dimensional info about the artefacts as possible to help determine if physical dimensions are a factor in the tools selected by early humans.</p>
<p>I could be getting this all wrong, but if I am, please let me know, and thanks for getting back to me.</p>

---

## Post #6 by @chir.set (2024-06-26 14:52 UTC)

<aside class="quote no-group" data-username="gavotny" data-post="5" data-topic="37019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b9e5f3/48.png" class="avatar"> gavotny:</div>
<blockquote>
<p>I am essentially starting from the end.</p>
</blockquote>
</aside>
<p>Can you share at least one of your models so that people here may better understand your workflow?</p>

---

## Post #7 by @muratmaga (2024-06-26 14:54 UTC)

<aside class="quote no-group" data-username="gavotny" data-post="5" data-topic="37019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b9e5f3/48.png" class="avatar"> gavotny:</div>
<blockquote>
<p>would like to be able to view them in cross-section if that makes sense</p>
</blockquote>
</aside>
<p>To see the cross-sections of a 3D model in slices, all you have to do is to enable the slice views:</p>
<p>What modality these 3D models are generated from? If something like photogrammetry or other surface scanning, there wouldn’t be any internal structure to see, simply a shell.</p>
<p>If they were CT scanned somewhere, and then there will be some internal detail, but most of the information will be lost during the volumetric segmentation to generation of closed-surface representation. You can expect to see something like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14b5ab4b497ec025791f252dd79408062650143e.png" data-download-href="/uploads/short-url/2XcLY5WXNIkFjwA3ST6mIrVsFSS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14b5ab4b497ec025791f252dd79408062650143e_2_690x401.png" alt="image" data-base62-sha1="2XcLY5WXNIkFjwA3ST6mIrVsFSS" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14b5ab4b497ec025791f252dd79408062650143e_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14b5ab4b497ec025791f252dd79408062650143e_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14b5ab4b497ec025791f252dd79408062650143e_2_1380x802.png 2x" data-dominant-color="7C7B7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2406×1400 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @gavotny (2024-06-26 15:06 UTC)

<p>Hi,<br>
That’s great to know. My models were built using photogrammetry and are of stone artefacts, so there’s no internal structure per se, but the cross-sections may give me a more visual representation of the sharp cutting edges vs. the blunt or hafted sides, etc. I had loaded models in already but couldn’t see a cross section in those panels, is there something I need to enable?</p>
<p>Thanks,<br>
Gavin.</p>

---

## Post #9 by @gavotny (2024-06-26 15:09 UTC)

<p>Sorry, how would I share the model, just an image of it in the app or through the model itself?</p>

---

## Post #10 by @cpinter (2024-06-26 15:20 UTC)

<p>So you basically have STLs (or OBJs or similar)? It is complicated to get cross-sections of models without images, as Slicer’s assumption is that every workflow starts with an image. There have been other topics here on the forum about this, but I think there was no good solution.</p>
<p>A simple hack that I suggest is:</p>
<ul>
<li>Load CTChest from Sample Data module</li>
<li>Volume render it</li>
<li>Enable interaction on the CTChest node (right-click eye and choose Interaction)</li>
<li>Move it so that it fully overlaps your model</li>
<li>Window/level so that it’s all black (to remove confusing medical data)</li>
<li>Now you can slice away</li>
</ul>
<p>Let us know if this is good enough or you need higher resolution or if you encounter other problems.</p>
<aside class="quote no-group" data-username="gavotny" data-post="9" data-topic="37019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b9e5f3/48.png" class="avatar"> gavotny:</div>
<blockquote>
<p>how would I share the model</p>
</blockquote>
</aside>
<p>Sharing one would be useful. I suggest dropping a google drive link or whatever cloud storage you use.</p>

---

## Post #11 by @muratmaga (2024-06-26 16:00 UTC)

<p>Another option is to load a copy of the STL as a segmentation object, and then convert the segmentation to a labelmap. That will give you a volume and slices that you can interact…</p>
<p>We have a tool in SlicerMorph to combine those two steps. I haven’t looked at it for a while, but it is called <code>ImportSurfaceToSegment</code>.</p>

---

## Post #12 by @gavotny (2024-06-27 09:12 UTC)

<p>Thanks for that, I’ve had a play around with what you suggested but think I’m missing a step or something and can’t quite get it to work as I’m not familiar with the software. I have added a couple of models below so that you can have a look. I’ll keep trying though.</p>
<p><a href="https://drive.google.com/file/d/1f4NcOS1RObkCr4dluU6Ajde8eWUsS6uc/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">AE0259 AREA N D4 855-5448 BLADE.stl - Google Drive</a>, <a href="https://drive.google.com/file/d/1jxhRgsHcuijs6u8Fl0hoCDlPv2jdbaOK/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">AE0259 AREA N D4 855-5448 BLADE.obj - Google Drive</a></p>

---

## Post #13 by @gavotny (2024-06-27 09:12 UTC)

<p>Thanks for this I’ll have a go at attempting it!</p>

---

## Post #14 by @chir.set (2024-06-27 09:53 UTC)

<aside class="quote no-group" data-username="gavotny" data-post="1" data-topic="37019">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b9e5f3/48.png" class="avatar"> gavotny:</div>
<blockquote>
<p>if there was a way to change the units of measurement</p>
</blockquote>
</aside>
<p>In ‘Application settings / Units’, if you select in ‘Advanced options’ the ‘Meter’ preset for ‘Length’ and set a coefficient of 1000, measurements appear in ‘m’ as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e623583412d0fa398efd60b27a8a186643664f6e.png" data-download-href="/uploads/short-url/wPTxHmZuD22PRSPB4YQqyXs4TfM.png?dl=1" title="monster" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e623583412d0fa398efd60b27a8a186643664f6e_2_690x282.png" alt="monster" data-base62-sha1="wPTxHmZuD22PRSPB4YQqyXs4TfM" width="690" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e623583412d0fa398efd60b27a8a186643664f6e_2_690x282.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e623583412d0fa398efd60b27a8a186643664f6e_2_1035x423.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e623583412d0fa398efd60b27a8a186643664f6e.png 2x" data-dominant-color="454640"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">monster</span><span class="informations">1280×524 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t know if that’s what you require.</p>

---

## Post #15 by @muratmaga (2024-06-27 15:37 UTC)

<p>This is what your data looks like if it is loaded as is into Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f742a20da925eedac96e96f796ca5a0404ad61c.jpeg" data-download-href="/uploads/short-url/6LNjZQBHyQs0E974vlcKJOdQ5fS.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f742a20da925eedac96e96f796ca5a0404ad61c_2_324x500.jpeg" alt="image" data-base62-sha1="6LNjZQBHyQs0E974vlcKJOdQ5fS" width="324" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f742a20da925eedac96e96f796ca5a0404ad61c_2_324x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f742a20da925eedac96e96f796ca5a0404ad61c_2_486x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f742a20da925eedac96e96f796ca5a0404ad61c_2_648x1000.jpeg 2x" data-dominant-color="BEBF93"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×1082 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is my suggested method of creating a scaling transform (m2mm) and assign the object to it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2d12e2b49a90a47a68f85160eea449433ea6b97.jpeg" data-download-href="/uploads/short-url/rNqNmbVmpvX8uK5pGGVXLVSg3LF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2d12e2b49a90a47a68f85160eea449433ea6b97_2_690x483.jpeg" alt="image" data-base62-sha1="rNqNmbVmpvX8uK5pGGVXLVSg3LF" width="690" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2d12e2b49a90a47a68f85160eea449433ea6b97_2_690x483.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2d12e2b49a90a47a68f85160eea449433ea6b97_2_1035x724.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2d12e2b49a90a47a68f85160eea449433ea6b97.jpeg 2x" data-dominant-color="CACCC0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1224×858 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what <a class="mention" href="/u/chir.set">@chir.set</a> suggested by modifiying the coefficients field of the Units settings to 1000, but keeping the unit as mm (this is actually works better than my suggestion changing the unit to meters)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/790085bc11e6c640e34df2da35276464d3134db7.jpeg" data-download-href="/uploads/short-url/hgqTnjOhZzr9bc69Ie5D8BQ3bTN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/790085bc11e6c640e34df2da35276464d3134db7_2_363x500.jpeg" alt="image" data-base62-sha1="hgqTnjOhZzr9bc69Ie5D8BQ3bTN" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/790085bc11e6c640e34df2da35276464d3134db7_2_363x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/790085bc11e6c640e34df2da35276464d3134db7_2_544x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/790085bc11e6c640e34df2da35276464d3134db7_2_726x1000.jpeg 2x" data-dominant-color="BCBC8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">786×1080 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Each of these have their own drawbacks. In the first one you can mentally do the change by multiplying the reported values by 1000. In second one, you have to remember to put the object under this transform every time you want to take a measurement. In the third one, every dataset that will be loaded will have their coordinates multiplied by 1000 (not just your data).</p>
<p>So which one is the optimum solution for you depends on what you want to do.</p>

---

## Post #16 by @gavotny (2024-07-11 10:00 UTC)

<p>Hi, Sorry I’m late responding your message, this is interesting how can I load the stl as a segmentation object?</p>

---

## Post #17 by @gavotny (2024-07-11 10:01 UTC)

<p>Thanks very much for your detailed response. I shall try them out and see what works best. You’ve all been very helpful, and it’s great to have a community like this.</p>

---
