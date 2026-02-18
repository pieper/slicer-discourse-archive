# Rat Lungs Trouble

**Topic ID**: 7331
**Date**: 2019-06-27
**URL**: https://discourse.slicer.org/t/rat-lungs-trouble/7331

---

## Post #1 by @ryann199 (2019-06-27 03:29 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.8.1<br>
Expected behavior: I’m working with a DICOM file of rat’s lungs and according to my PI the file sizes are very large and because of that the program runs very slowly. I’ve tried to do several different techniques I’ve seen online such as cutting out certain segments using the scissors tool under the segment editor module (for some reason the ‘erase outside’ doesn’t do anything), I’ve also tried cropping the volume using the crop volume module (although it runs and creates a new save when I try to render that under the volume rendering module it doesn’t load anything) and I’ve also tried an extension called “Slicer - AirwaySegmentation” and that doesn’t result in anything either. The overall goal is to get different renderings of the lobes and if possible, the bronchi in order to calculate volumes and diameters. If there are any suggestions I would love feedback, I’m extremely new to Slicer 3D so some directions could go over my head if there isn’t enough detail. I greatly appreciate the help!<br>
Actual behavior: N/A</p>

---

## Post #2 by @lassoan (2019-06-27 03:41 UTC)

<p>To improve speed, crop the volume to the relevant region of interest and/or decrease resolution (increase “Spacing scale” parameter). After cropping, remove the original, non-cropped volume to conserve memory. Erasing segments will not make segmentation faster. Scissors effect will not modify or crop the original volume, so it will not make anything faster either.</p>
<p>What are the dimensions of the volume after cropping? (you can see that in Volumes module / Volume information section)</p>
<p>What would you like to segment in the lung? What would you like to use the segmentation for? Can you attach screenshots of how things look now and an example of what you would like to have?</p>

---

## Post #3 by @ryann199 (2019-06-27 16:37 UTC)

<p>I tried to crop it again yet it won’t actually save the cropped ROI. Instead it’ll make the ‘cropped volume’ and when I check it in the volume information it simply comes out as image dimensions: 0,0,0 whereas the original file comes out as 1024, 1024, 1024.</p>
<p>Also, how do you remove the original, non-cropped volume?</p>
<p>I would like to segment each section of the lung out, such as having a separate segment for each lobe along with one for the bronchi. This would be to calculate the volume of each segment and repeat this process for other lungs in the future.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3917c510e7965e2d5ecd63ed9a7baf8999177d31.jpeg" alt="Screenshot%20from%202019-06-27%2009-34-10" data-base62-sha1="8948PcXD5GMbXu0BnRXmwi8OAgh" width="321" height="438"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be4895be3c0c7104f8f20a3659dd5309343d39aa.jpeg" alt="0-S0012369216416132-mmc4" data-base62-sha1="r9kennGGSQVEUb34Rz9R11swtjY" width="337" height="190"></p>
<p>I’m not sure if those images work but the first should be what the rats lungs are now and the second is an online image of what I would like them to look like.</p>
<p>Thank you again.</p>

---

## Post #4 by @ryann199 (2019-06-28 18:16 UTC)

<p>I have yet to get a reply, I have tried the crop volume several times and it hasn’t created a new volume for me. Can I please have assistance on my issue as I haven’t been able to find any help elsewhere online.</p>

---

## Post #5 by @Leon (2019-06-28 19:34 UTC)

<p><a class="mention" href="/u/ryann199">@ryann199</a></p>
<aside class="quote no-group" data-username="ryann199" data-post="3" data-topic="7331">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/d78d45/48.png" class="avatar"> ryann199:</div>
<blockquote>
<p>Also, how do you remove the original, non-cropped volume?</p>
</blockquote>
</aside>
<p>Go to the ‘Data’ module. Click right on the original dataset and choose delete.<br>
Actually your cropped volume should also be there. If not, then something when wrong.<br>
I suggest that you try it again, but then just use the default settings. Works fine with me.</p>
<p>Good luck.</p>

---

## Post #6 by @lassoan (2019-06-28 22:37 UTC)

<aside class="quote no-group" data-username="ryann199" data-post="3" data-topic="7331">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/d78d45/48.png" class="avatar"> ryann199:</div>
<blockquote>
<p>it’ll make the ‘cropped volume’ and when I check it in the volume information it simply comes out as image dimensions: 0,0,0 whereas the original file comes out as 1024, 1024, 1024.</p>
</blockquote>
</aside>
<p>Most probably you have run out of memory. Increase virtual memory/swap size may fix it.</p>
<p>Check the application log (X icon in the lower right corner) to check if there was any error or warning message.</p>

---

## Post #7 by @ryann199 (2019-07-01 22:20 UTC)

<p>Now seeing it I do believe that the computer runs out of memory. Thank you very much!</p>

---
