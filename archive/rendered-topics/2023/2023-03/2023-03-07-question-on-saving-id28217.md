# Question on saving

**Topic ID**: 28217
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/question-on-saving/28217

---

## Post #1 by @bcolbert (2023-03-07 14:07 UTC)

<p>I am segmenting structures in fish. Once segmented, I develop a model (ply) which I will eventually use in a multi-species analysis. Once structures are segmented, I have saved using both the MRB and from saving the individual scene files (e.g, *.mrml, *.png, *.vp, etc.).</p>
<p>I have recently found when saved as individual scenes they are less stable and I am having to go back and segment. Is there a best practice for how to save work? Apologies for the basic question but I’m trying to learn on the fly and have no one in my lab doing this type of work.</p>

---

## Post #2 by @hherhold (2023-03-07 14:24 UTC)

<p>the MRB file is a zip-format file of all the files (mrml, .seg.nrrd, .ply, etc) and is useful for archiving or transferring an entire project to someone.</p>
<p>Typically I make a separate directory for each specimen (I work on insects) and I almost never use MRBs - they take longer to load and save. I find that when I lose work or have to re-segment something, it’s because I wasn’t paying attention and saved to the wrong directory. It takes a little more attention to make sure your save dir is correct, but in the end it’s faster (only modified files are saved) and it’s much more flexible.</p>
<p>Hope this helps - where Slicer puts files is one of the parts of the program that is a bit different than other apps and takes a little getting used to. But once you’re comfortable with it, it is very flexible.</p>

---

## Post #3 by @bcolbert (2023-03-07 15:55 UTC)

<p>This is helpful, thanks. I am finding when I am capable of loading scenes from previous segmentations, I am losing the ability to zoom in on 2D slices. Is that typical or am I doing something wrong?</p>

---

## Post #4 by @hherhold (2023-03-07 15:57 UTC)

<p>Doesn’t sound typical… I do this kind of thing all the time.</p>
<p>Is this loading a scene from a previous segmentation right after starting slicer, or are you loading one on top of another?</p>

---

## Post #5 by @muratmaga (2023-03-07 17:32 UTC)

<aside class="quote no-group" data-username="bcolbert" data-post="3" data-topic="28217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<p>s that typical or am I doing something wrong?</p>
</blockquote>
</aside>
<p>No that is not typical at all. Can you share a problematic scene packaged as a MRB file?</p>

---

## Post #6 by @bcolbert (2023-03-07 19:21 UTC)

<p>You should be able to access with the below link. When I open the series of files saved I get the following error. This is reoccurring in other folders.</p>
<p>Error: Loading D:/Carp Images/Unstained/Grass8-31_4_Rec/Tripus/2022-04-01-Scene.mrml -  load failed.</p>
<p><code>https://drive.google.com/drive/u/0/folders/1QrwwigehebT4BXrqV5WFgD9binvZNHvH</code></p>

---

## Post #7 by @muratmaga (2023-03-07 19:58 UTC)

<p>I didn’t get any error emssage loading the mrb file. However, your scene has multiple problems (I am not sure if mrb is exactly like your scene):</p>
<p>You have multiple duplicated datasets (like two volumes, two segmentation). In addition to taking resources (everything loaded into the scene uses computer memory), this might create room for error.</p>
<p>I never have seen a Scene file being listed and loaded as a object inside the workspace (the red highlight). So I am not sure whats going on in there either.</p>
<p>But things do line up. So I suspect when your segmentation is not lining up, you are confusing yourself and looking at different datasets (since there are two of each).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5300f50a2cf81cf2a4c2dc478515f03bd8f7e173.jpeg" data-download-href="/uploads/short-url/bQhGd24g4XP2eXXQuwPZbIHCxQn.jpeg?dl=1" title="Screen Shot 2023-03-07 at 11.49.04 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5300f50a2cf81cf2a4c2dc478515f03bd8f7e173_2_690x496.jpeg" alt="Screen Shot 2023-03-07 at 11.49.04 AM" data-base62-sha1="bQhGd24g4XP2eXXQuwPZbIHCxQn" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5300f50a2cf81cf2a4c2dc478515f03bd8f7e173_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5300f50a2cf81cf2a4c2dc478515f03bd8f7e173_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5300f50a2cf81cf2a4c2dc478515f03bd8f7e173_2_1380x992.jpeg 2x" data-dominant-color="ACAEBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-07 at 11.49.04 AM</span><span class="informations">2034×1464 646 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Try getting rid of the duplicate objects, and then go to Save As and click the checkbox I highlighted and then click the <strong>change directory for selected files</strong> button and save everything into a new folder you created. Then, try loading the MRML file from that location and see if you are getting the error again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355488ad50d2f5434dab62fd66bc2b2a530ec445.png" data-download-href="/uploads/short-url/7BMpYvJ4fwRLd1EqFwrriptnErz.png?dl=1" title="Screen Shot 2023-03-07 at 11.56.04 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355488ad50d2f5434dab62fd66bc2b2a530ec445_2_690x288.png" alt="Screen Shot 2023-03-07 at 11.56.04 AM" data-base62-sha1="7BMpYvJ4fwRLd1EqFwrriptnErz" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355488ad50d2f5434dab62fd66bc2b2a530ec445_2_690x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355488ad50d2f5434dab62fd66bc2b2a530ec445_2_1035x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355488ad50d2f5434dab62fd66bc2b2a530ec445_2_1380x576.png 2x" data-dominant-color="E9E7E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-07 at 11.56.04 AM</span><span class="informations">1770×740 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @muratmaga (2023-03-07 20:01 UTC)

<p>Also when you are loading, remember you only need to drag and drop the MRML file (not the whole contents of the folder) into Slicer. MRML file has pointers to those objects, and will load them (or will throw an error if it cannot find the file). If you are both dragging and the MRML file, and the segmentations, volumes etc in the folder, that’s where the duplicaiton might be coming from.</p>

---

## Post #9 by @pieper (2023-03-07 21:50 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="28217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>only need to drag and drop the MRML file (not the whole contents of the folder) into Slicer</p>
</blockquote>
</aside>
<p>Agreed, this sounds like what would lead to the observed duplication behavior.  The volume node with the name of the scene file is probably the screen capture of the UI that is saved automatically when you save a mrml scene.</p>

---

## Post #10 by @bcolbert (2023-03-07 23:41 UTC)

<blockquote>
<p>Also when you are loading, remember you only need to drag and drop the MRML file (not the whole contents of the folder) into Slicer.</p>
</blockquote>
<p>This was clearly part of the problem. I opened just the MRML file, saved the new scene in a new folder, closed the previous scene, and opened this new saved. I no longer get the error upon opening but I still am unable to zoom in and out on a particular slice. This is critical for me to properly segment and I am sure I am making a very basic error, I just don’t know what.</p>

---

## Post #11 by @muratmaga (2023-03-07 23:56 UTC)

<aside class="quote no-group" data-username="bcolbert" data-post="10" data-topic="28217">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<p>am unable to zoom in and out on a particular slice.</p>
</blockquote>
</aside>
<p>This is weird, and I don’t think it has anything to do with your scene. but just to rule out the scene issue, can you try this:</p>
<ol>
<li>Start a new slicer session (with nothing loaded)</li>
<li>Just load the segmentation and the volume file from the folder (drag and drop). Do NOT choose the MRML file.</li>
</ol>
<p>See if you can zoom in/out slice. If it is fixed, just save the contents as a new MRML file. And try opening from that.</p>
<p>If problem still persists, send me a direct message and let’s see if we can find a time to meet remotely.</p>

---
