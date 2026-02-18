# Markups module lagging when placing anatomical landmarks

**Topic ID**: 27529
**Date**: 2023-01-29
**URL**: https://discourse.slicer.org/t/markups-module-lagging-when-placing-anatomical-landmarks/27529

---

## Post #1 by @meganfveltri (2023-01-29 17:43 UTC)

<p>Hello! I’m hoping to get some clarification on some issues I’ve been having with markups in Slicer. I am very new to using the program so any help is appreciated.</p>
<p>I have two ages of mouse skulls (E17.5 and P28) for which we have CT scan data, and the volume rendering shows all the external structures of the head. TIFF stacks were imported using the SlicerMorph module for both ages, and the image spacing was added from our voxel sizes as shown in our .pcr files. I landmarked both using the markups module. For the E17.5, I had no issues creating only a volume rendering, adjusting the shift to see the skull, and landmarking directly on the rendering of the skull (possibly because there is less bone at this age). I also had no issues with Slicer lagging/not responding or with the markups module lagging at all.</p>
<p>For the P28 I was having trouble visualizing the skull structures I needed to see in the volume rendering before placing a landmark in the markups module. My solution was to segment out the skull and save it as a model, then landmark directly on the model itself. When I did this though, I ran into a couple of issues.</p>
<p>First, the markups module began lagging and taking 15-20 seconds to place a landmark, and I often had to re-take landmarks that were not placed properly due to the lag. Second, Slicer stopped responding, and I often had to wait until the program finished whatever it was doing before adjusting landmarks or moving the model around.</p>
<p>At one point, the program would switch back and forth between the fiducial tool (where the landmark displays as a green dot) and attempting to place a landmark for a minute or two before it placed the landmark, after which I had to edit the placement because of the lagging. It was almost as if my placement of the landmark didn’t register in Slicer, and I had to be careful not to click anywhere else until the landmark was placed.</p>
<p>For reference, the computer I was using is a high-powered machine that is capable of handling large amounts of data and even running Avizo without any issues (512 RAM, 64-bit OS, 2.20 GHz, and an additional 1.81 TB of SSD for local data storage). All data is saved locally so that importing large files does not disrupt processing power in these programs.  Additionally, the data we use is typically between 5-25 microns.</p>
<p>Is there possibly an issue with the image spacing in SlicerMorph? For example, I sometimes have to convert the voxel size to mm or to um depending on what program I am using. I believe SlicerMorph asks for mm. Or is this an issue with having multiple nodes in the data tree (model, segmentation, volume rendering, markups) even if the visibility is off for the ones I am not actively using? Lastly, does the coordinate system change at all when landmarking on a model versus a volume rendering? All the data is cropped and reoriented in Dragonfly and Fiji before saving as TIFF files so that file sizes are cut down and easily viewable in Avizo or Slicer.</p>

---

## Post #2 by @jamesobutler (2023-01-29 18:11 UTC)

<p>Hi <a class="mention" href="/u/meganfveltri">@meganfveltri</a> to help others diagnose your issue can you provide the version of Slicer that you are using? Also providing details of when you installed SlicerMorph or last updated the extension.</p>

---

## Post #3 by @lassoan (2023-01-29 18:54 UTC)

<p>Most likely the displayed meshes are too complex and therefore 3D point picking takes too long. There are several solutions for this, but to suggest what to do, we would need a little bit more information.</p>
<p>How many points have you placed?<br>
Do you place the points on segmentations or on models?<br>
How many segments or models do you have?<br>
If you export the segmentation to a model then what is the number of points in the mode;?</p>

---

## Post #4 by @muratmaga (2023-01-29 22:02 UTC)

<p><a class="mention" href="/u/meganfveltri">@meganfveltri</a> please provide the information <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> asked as this will help narrow down the issue. As for your questions below:</p>
<aside class="quote no-group" data-username="meganfveltri" data-post="1" data-topic="27529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/meganfveltri/48/18211_2.png" class="avatar"> meganfveltri:</div>
<blockquote>
<p>Is there possibly an issue with the image spacing in SlicerMorph? For example, I sometimes have to convert the voxel size to mm or to um depending on what program I am using. I believe SlicerMorph asks for mm. Or is this an issue with having multiple nodes in the data tree (model, segmentation, volume rendering, markups) even if the visibility is off for the ones I am not actively using? Lastly, does the coordinate system change at all when landmarking on a model versus a volume rendering? All the data is cropped and reoriented in Dragonfly and Fiji before saving as TIFF files so that file sizes are cut down and easily viewable in Avizo or Slicer.</p>
</blockquote>
</aside>
<p>Incorrect spacing should not alter the display performance. But always enter spacing informaiton to ImageStacks in millimeters, as that’s what we expect (so 5 micron will be entered as 0.005).</p>
<p>Your computer sounds powerful enough that having multiple objects in the scene shouldn;t be too much of a concern for available resources. but to rule out that you can export your segmentation as a 3D model (e.g., in OBJ format), close everything and load only that into the scene and see if that makes a difference.</p>
<p>If you are landmarking in Slicer, landmarking in model vs volume rendering will not affect the coordinate system. I prefer to do landmarking in volume rendering mostly because the anatomical detail I obtain from the volume rendering is usually superior to the 3D model representation of its segmentation.</p>
<p>Finally, I would <strong>discourage</strong> cropping your raw data in Dragonfly or Fiji. You should be able to do that as easily in <code>ImageStacks</code> module of SlicerMorph, by specifying the ROI you would like to import. In fact one way to deal with performance issues, is to only import the relevant sections of a large dataset into Slicer using the <code>ImageStacks</code>. Because the coordinate system is preserved, later if you import another section from the same image sequence, you will be able to continue segmenting (or landmarking) without worrying about whether things continue to line up in physical world. You will not be able to do this if you use FIJI for cropping your images. You can see our tutorial on ImageStacks and specifically how to use the ROI option to import data <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks#using-roi-with-image-stacks">here:</a></p>

---

## Post #5 by @meganfveltri (2023-01-30 15:40 UTC)

<p>Hi James,</p>
<p>I am currently running Slicer version 5.2.1 r31317 and SlicerMorph version 5813db0 (2022-12-01). We downloaded both at in the middle of December 2022.</p>

---

## Post #6 by @muratmaga (2023-01-30 15:54 UTC)

<aside class="quote no-group" data-username="meganfveltri" data-post="5" data-topic="27529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/meganfveltri/48/18211_2.png" class="avatar"> meganfveltri:</div>
<blockquote>
<p>I am currently running Slicer version 5.2.1 r31317 and SlicerMorph version 5813db0 (2022-12-01). We downloaded both at in the middle of December 2022.</p>
</blockquote>
</aside>
<p>It will be great if you can share your dataset as well.</p>

---

## Post #7 by @meganfveltri (2023-01-30 16:00 UTC)

<p>I’ve updated the Slicer Morph extension today.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> here are the answers to your questions:</p>
<p>The E17.5 skull has 34 landmarks. The P28 skull has 32. For the P28 I placed the landmarks on the model. I segmented out the cranium and saved it as a model, then landmarked the model. Therefore, I have one segment and one model. By the number of points in the model do you mean the number of landmarks? If so, there are 32 landmarks.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a><br>
For background, we crop and reorient all of our data as part of our data transformation pipeline since most of these scans are going to another collaborator for additional processing and it helps to cut down processing power and file sizes in dropbox. We also do this so that we can process our bone phantom which is scanned with the specimens so that we can maintain consistency in the bone threshold across all the specimens in a particular scan range. Our specimens are usually scanned three at a time, so we need to crop each individual specimen out from the raw data for processing later. That way we can visualize one specimen at a time versus three at a time and have to figure out which specimens are which. So the data for P28, for example, has already been cropped to the relevant ROI and TIFF slices that I want to analyze. Can you elaborate on what you said here: “Because the coordinate system is preserved, later if you import another section from the same image sequence, you will be able to continue segmenting (or landmarking) without worrying about whether things continue to line up in physical world.” ? Am I correct in thinking that if we crop data in Dragonfly or Fiji prior to landmarking that the coordinate system can be disturbed between specimens since they are imported as separate image stacks?</p>
<p>Thanks again for all of your help!</p>

---

## Post #8 by @muratmaga (2023-01-30 16:08 UTC)

<aside class="quote no-group" data-username="meganfveltri" data-post="7" data-topic="27529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/meganfveltri/48/18211_2.png" class="avatar"> meganfveltri:</div>
<blockquote>
<p>The E17.5 skull has 34 landmarks. The P28 skull has 32. For the P28 I placed the landmarks on the model. I segmented out the cranium and saved it as a model, then landmarked the model. Therefore, I have one segment and one model. By the number of points in the model do you mean the number of landmarks? If so, there are 32 landmarks.</p>
</blockquote>
</aside>
<p>Thanks. <a class="mention" href="/u/lassoan">@lassoan</a> was asking about the point size of the model. For that, right click on the model object and choose “Edit Properties” (which will take you to Models module).<br>
Expand the information tab, and report the values under points and cells.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df41981e7debede0d3cd7598d17572204fe05f12.png" data-download-href="/uploads/short-url/vR10FMcmwdjtwqCK9gKwEZy0e9I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df41981e7debede0d3cd7598d17572204fe05f12.png" alt="image" data-base62-sha1="vR10FMcmwdjtwqCK9gKwEZy0e9I" width="690" height="244" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×329 7.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will post another response to your other inquiry a little later.</p>

---

## Post #9 by @meganfveltri (2023-01-30 16:32 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d1fe8743dcb33592879c131ffd72f09cad7faaf.png" data-download-href="/uploads/short-url/dhOLzNuenAxYeHn2hto5J0USsvJ.png?dl=1" title="Screenshot 2023-01-30 113142" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d1fe8743dcb33592879c131ffd72f09cad7faaf.png" alt="Screenshot 2023-01-30 113142" data-base62-sha1="dhOLzNuenAxYeHn2hto5J0USsvJ" width="690" height="286" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-01-30 113142</span><span class="informations">793×329 7.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Maybe too many points?</p>

---

## Post #10 by @meganfveltri (2023-01-30 16:38 UTC)

<p>What is the best way to share the dataset? Box?<br>
Also, would you prefer just the .tiff files or the entire scene/model/segmentation/markups for the P28 skull?</p>

---

## Post #11 by @muratmaga (2023-01-30 17:11 UTC)

<p>Yes, that’s a fairly large model. Here are a few things you can do to possibly speed up the interactions.</p>
<p>Go to Markups module and expand the display tab and navigate to the section that says <strong>3D Display,</strong> and change the placement mode to the unconstrained. By default this snap to the visible surface which makes sure that the points are always on the vertex on the model (which slows down things).</p>
<p>Also, navigate further down to Control Points tab and click the lock sign that says interactions (the left one). This will disable any mouse mode interaction with the points already created, but should speed up mouse movements. If you need to interact with them for any reason, you can turn off the lock.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cc144f718d56dbbb0ad026f329651aba2b4255.png" data-download-href="/uploads/short-url/jetdzQHePX4S48hQLsyoDsT0PAx.png?dl=1" title="Screen Shot 2023-01-30 at 9.07.32 AM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cc144f718d56dbbb0ad026f329651aba2b4255_2_679x500.png" alt="Screen Shot 2023-01-30 at 9.07.32 AM" data-base62-sha1="jetdzQHePX4S48hQLsyoDsT0PAx" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86cc144f718d56dbbb0ad026f329651aba2b4255_2_679x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cc144f718d56dbbb0ad026f329651aba2b4255.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86cc144f718d56dbbb0ad026f329651aba2b4255.png 2x" data-dominant-color="E3E3E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-01-30 at 9.07.32 AM</span><span class="informations">1016×748 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @muratmaga (2023-01-30 17:11 UTC)

<aside class="quote no-group" data-username="meganfveltri" data-post="10" data-topic="27529">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/meganfveltri/48/18211_2.png" class="avatar"> meganfveltri:</div>
<blockquote>
<p>What is the best way to share the dataset? Box?</p>
</blockquote>
</aside>
<p>Please share both the tiff stack and the segmentation. If you do not want to publicly share it on the cloud and provide a link for everyone in the list, you can share it with me here: <a href="http://faculty.uw.edu/maga/data_dropbox">http://faculty.uw.edu/maga/data_dropbox</a>.</p>

---

## Post #13 by @meganfveltri (2023-01-30 19:24 UTC)

<p>Thanks so much for all your help. I will double-check with the rest of the lab that I can share the data, then let you know. We’re meeting to discuss this tomorrow during our lab meeting.</p>

---

## Post #14 by @meganfveltri (2023-01-31 16:56 UTC)

<p>Hi Murat,</p>
<p>I’ve uploaded the tiff stack and segmentation. Let me know if you need anything else! Thanks again for all your help.</p>

---

## Post #15 by @muratmaga (2023-01-31 18:05 UTC)

<p>There are few things going on.</p>
<p>First, I can replicate the extreme lag when placing the landmarks on 3D models, and that’s directly related to the size of the model. My suggestions of disabling the interactions and other things didn’t help much, so I would like to hear what <a class="mention" href="/u/lassoan">@lassoan</a> suggest to improve that. So hold on that one.</p>
<p>There are other things you should do that will make your life easier. I noticed that the tiff stack contains very tight intensity ranges (min = -0.0086, max =0.0765), and the data is represented as a float32 data type. In my experience this is very uncommon for microCT datasets. Most of the time mCT are either 8 bit (if it’s a dry skull) with 256 discrete intensities or, 16 bit (usually soft tissue, or contrast enhanced) with 65K discrete values. Float uses much more memory than either of these. So here the steps you can do rescale and cast your image with almost no loss in detail.</p>
<ol start="0">
<li>
<p>Import your data with ImageStacks as usual.</p>
</li>
<li>
<p>under the Module finder search for <code>SimpleFilters</code></p>
</li>
<li>
<p>Filters search option type **rescale **</p>
</li>
<li>
<p>Enter 0 as output minimum and 255 as output maximum, and create new output volume and hit apply<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d688f336830f262dc6c40a14e6e81347ffaa815.png" data-download-href="/uploads/short-url/dkkqaSOL6u4VYfyIZuEyODMVacJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d688f336830f262dc6c40a14e6e81347ffaa815.png" alt="image" data-base62-sha1="dkkqaSOL6u4VYfyIZuEyODMVacJ" width="517" height="234" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×451 10.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>After this is completed type <strong>Cast</strong></p>
</li>
<li>
<p>As the input volume choose the output volume you specified in the previous step.</p>
</li>
<li>
<p>Set the Output pixel type to uint8_t (unsigned 8 bit, since we choose 0-255 range in the previous step).</p>
</li>
<li>
<p>Set the output volume same as the input volume and hit apply</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3833be39dbb7d7af81ab637b1c399e8b005aa4.png" data-download-href="/uploads/short-url/zQofY6IrwmR2V2EJR8QOLz7yaQA.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3833be39dbb7d7af81ab637b1c399e8b005aa4.png" alt="image" data-base62-sha1="zQofY6IrwmR2V2EJR8QOLz7yaQA" width="517" height="183" data-dominant-color="F2F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">999×356 8.42 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After these operations you will have a new 8 bit volume. Air background would be around 0, soft tissue surrounding the skull will be 60-90 range, and the bone will be about 100+ values (I just poked around, these may not be entirely true). After this operations notice that how fast the volume rendering will become. You will have to create new set of volume rendering properties for this volume. If you find that the 255 intensity range is not sufficient, you can go back to the rescaling step and enter the range 0-65535 and then in the case choose uint16_t (unsigned 16 bit). Make sure to save the final volume as NRRD file so that you don’t have to repeat these steps.</p>
<p>These will not impact the slowness you encounter during the landmarking of the 3D model from segmentation. Unless <a class="mention" href="/u/lassoan">@lassoan</a> have other suggestions, if you have feel like you need to the landmarking on the model, you will need to use a slightly lower resolution for faster picking.</p>
<p>(3D model on the left, volume rendering on the right dervied from this 8 bit data)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18a3500b95bd4b04e372e0ebcc9151463ca3607b.jpeg" data-download-href="/uploads/short-url/3vXm0XbGPCsC3kYkYPNRzhFzRt9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18a3500b95bd4b04e372e0ebcc9151463ca3607b_2_475x375.jpeg" alt="image" data-base62-sha1="3vXm0XbGPCsC3kYkYPNRzhFzRt9" width="475" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18a3500b95bd4b04e372e0ebcc9151463ca3607b_2_475x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18a3500b95bd4b04e372e0ebcc9151463ca3607b_2_712x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18a3500b95bd4b04e372e0ebcc9151463ca3607b_2_950x750.jpeg 2x" data-dominant-color="727382"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1841×1451 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I will comment on the ImageStacks and ROI operations in the next one.</p>

---

## Post #16 by @muratmaga (2023-01-31 18:22 UTC)

<p>Here is an example of how you can use ImageStack’s ROI functionality to reduce your memory footprint and partially import datasets. This would have more sense if you had the original data, where there are multiple specimens scanned side by side (which I think you are scanning them). But still demonstrates the concept.</p>
<ol>
<li>Proceed with ImageStacks as before, but choose to import half-resolution quality.</li>
<li>Volume render the half-resolution set and create an ROI in volume rendering that only contains Left Mandible.</li>
<li>Go back to ImageStacks and then change these settings:
<ul>
<li>Output Volume: Create a new output volume as and set it as Left Mandible</li>
<li>Set Region of interest to the new ROI you created in step <span class="hashtag">#2</span>
</li>
<li>change the resolution to full resolution.</li>
</ul>
</li>
</ol>
<p>These changes reduces the memory footprint to 1/8th of the original dataset. Hit load files to import this new volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7f20682f17682c31b84396c13caa2c3be7c5662.jpeg" data-download-href="/uploads/short-url/qffUGaAkskhG5BD6KNc7uqyixiO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f20682f17682c31b84396c13caa2c3be7c5662_2_690x375.jpeg" alt="image" data-base62-sha1="qffUGaAkskhG5BD6KNc7uqyixiO" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f20682f17682c31b84396c13caa2c3be7c5662_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f20682f17682c31b84396c13caa2c3be7c5662_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7f20682f17682c31b84396c13caa2c3be7c5662_2_1380x750.jpeg 2x" data-dominant-color="919095"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Go ahead and create a single landmark on the tip of the left incisor.</p>
<p>Repeat these procedures to import the Right mandible, create a single point on the right mandible as well. Then go ahead and import the full dataset (at any resolution) without the ROI and notice that both of these points are indeed in correct spot for incisors on the full dataset. That’s because Slicer preserves the correct offset for the partial volumes you created. Of course, save the data as NRRD file right after the import (so that you don’t repeat the steps).</p>
<p>If you did the cropping of left and right mandible in ImageJ and then bring those datasets to Slicer, you wouldn’t be able to do this, because ImageJ will not preserve the full coordinate system. That’s why I say there is really no reason to do the cropping in ImageJ. In future, we will add the option to put the ROI under transform (so that you can crop in the oblique orientations) as well.</p>

---

## Post #17 by @meganfveltri (2023-01-31 19:20 UTC)

<p>This is all very helpful. Thank you so much! I am hoping to get back to this on Thursday to play around with the scans and try landmarking again. I will reply then and let you all know how it goes.</p>

---

## Post #18 by @meganfveltri (2023-06-20 18:48 UTC)

<p>Hi everyone. Just wanted to give an update. <a class="mention" href="/u/muratmaga">@muratmaga</a> 's recommendations to simple filter the data have worked well. The landmark lagging issue has been resolved. Thanks!</p>

---
