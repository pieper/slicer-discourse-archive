# Saving overlayed images 

**Topic ID**: 22503
**Date**: 2022-03-14
**URL**: https://discourse.slicer.org/t/saving-overlayed-images/22503

---

## Post #1 by @Prisc (2022-03-14 16:29 UTC)

<p>Hello,</p>
<p>I need help please!<br>
I have loaded 2 sets of data MRI and CTscans.<br>
The MRI is visible:show in slice views as foreground and the CT scan is in the background. (data module)<br>
I have translated one volume so they can be overlayed(using volumes module)<br>
This issue that I am facing is that i could not find a way to save those two volumes as one volume with them overlayed.<br>
Could you help me please solving this issue? Thank you!</p>

---

## Post #2 by @lassoan (2022-03-15 03:42 UTC)

<p>What would like to achieve: export images/video of slice or 3D views (for example, to show in a presentation); or blend the two volumes create a new volume for further analysis?</p>

---

## Post #3 by @Prisc (2022-03-15 08:50 UTC)

<p>Hello, thank you for your reply.<br>
I would like to use the stack for further processing.<br>
I should be able to see the different strucures of the MRI and CT scan slices that i overlayed in one file for calculations.<br>
Thank you</p>

---

## Post #4 by @Prisc (2022-03-15 15:03 UTC)

<p>I have been trying to look for solutions using ‘registration’ module ( I just recently started using slicer). Given data: CT slices of the entire body and MRI of a part of the brain I have manually moved the MRI over the CT. I need to provide a volume (all the axial slices) like the one in the screenshot but I cannot find a way to save the volume that I am seeing.<br>
Is it because the volumes module does not create a new volume of the foreground and background data overlayed and it is just used for visual ?</p>
<p>Thanks alot in advance !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3dcddb08dc3d8164cb59b787401cb15ca9461546.jpeg" data-download-href="/uploads/short-url/8OKauLGxaQ23ixQVxxJyARJlEto.jpeg?dl=1" title="ss slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcddb08dc3d8164cb59b787401cb15ca9461546_2_690x301.jpeg" alt="ss slicer" data-base62-sha1="8OKauLGxaQ23ixQVxxJyARJlEto" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcddb08dc3d8164cb59b787401cb15ca9461546_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcddb08dc3d8164cb59b787401cb15ca9461546_2_1035x451.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcddb08dc3d8164cb59b787401cb15ca9461546_2_1380x602.jpeg 2x" data-dominant-color="303139"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ss slicer</span><span class="informations">1901×831 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Prisc (2022-03-15 16:32 UTC)

<p>Again I am very sorry for the many replies, just to make sure I share what i have tried and did not succeed.<br>
i have saved the scene but this is not what i need and have done transformations for manual registration and again the output is not what is requested.<br>
My goal is to have 1 volume of the axial view overlayed in a tiff format preferably for calculation purposes.<br>
Thank you again</p>

---

## Post #6 by @mikebind (2022-03-15 16:53 UTC)

<p>You are correct that the slice views show the volumes combined just for visualization and do not create a merged volume.</p>
<p>To create a merged volume, I would suggest using the “Resample Scalar/Vector/DWI Volume”   module to resample the smaller image volume (the MRI) into the same grid as the larger image volume (the CT), by using the CT as the “reference” volume.   Once you have two image volumes with aligned voxel grids, you can combine them to achieve the exact blending effect you want in a single image volume.  I’m not sure what that is, but if you can specify, we can help guide you in how to accomplish that. For example, do you want to show only the MRI where the MRI is present, or do you want to show a blend of the MRI and the CT?  If a blend, how much of each?</p>

---

## Post #7 by @Prisc (2022-03-16 10:06 UTC)

<p>Thank you so much for your reply !It sure helps a lot.</p>
<p>So the first step  “Resample Scalar/Vector/DWI Volume” is in order to have the same resolution, grid size.( I have in prior in order to merge set the resolution on the MRI to be isotropic and equal to the CT) once I have the volumes I would like to have a volume that shows a blend of the MRI and the CT that  preserve the best contrast possible.(Brain MRI and entire body CT, while still keeping all the CT)</p>
<p>Thank you. I hope I am expressing myself well enough !!</p>

---

## Post #8 by @Prisc (2022-03-16 13:03 UTC)

<p>The needed output for my calculations is merged/blended slices of MRI and CT scan.<br>
In other words, I need to blend the MRI slices with the matching CT slices and keep the remaining CT slices that do not match while keeping the best contrast for recognising the bony structures from the CT and the brain from the MRI.</p>
<p>The screenshot shown above shows the the MRI slices translated to the corresponding part of the CT. I need this result to be blended.</p>
<p>Thank you again for the help !</p>

---

## Post #9 by @Prisc (2022-03-16 15:03 UTC)

<p>Hello, i think I have figured out what i needed !<br>
Thanks alot</p>

---

## Post #10 by @mikebind (2022-03-16 17:14 UTC)

<p>If you have a few minutes to share what ended up working for you, it may be helpful to others who search this forum in the future. Thanks!</p>

---

## Post #11 by @lassoan (2022-03-16 20:47 UTC)

<aside class="quote no-group" data-username="Prisc" data-post="9" data-topic="22503" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/prisc/48/14660_2.png" class="avatar"> Prisc:</div>
<blockquote>
<p>Hello, i think I have figured out what i needed !<br>
Thanks alot</p>
</blockquote>
</aside>
<p>Deleting posts after you got your problem solved is not fair towards those who invested time into working with you. Community members helped you under the assumption that their ideas and suggestions will help everyone else who will have similar questions in the future.</p>
<p>This is more than just an assumption. Our statistics show that in fact each post is read by 200 people on average, so the person who helped you could potentially help 200 others, if the discussion is properly preserved.</p>
<p>Therefore, please either restore your deleted posts or give us a summary as <a class="mention" href="/u/mikebind">@mikebind</a> asked above.</p>

---
