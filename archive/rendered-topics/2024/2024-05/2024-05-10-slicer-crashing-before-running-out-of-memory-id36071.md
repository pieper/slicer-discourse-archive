# Slicer crashing before running out of memory

**Topic ID**: 36071
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/slicer-crashing-before-running-out-of-memory/36071

---

## Post #1 by @Dave_Matthews (2024-05-10 17:22 UTC)

<p>First off, thanks Murat and Andras for all your work in developing this program and offering so much help to the community in using it!</p>
<p>I’ve been using slicer for a few years to do micro-CT scans of bones, largely without issue. However, lately I’ve started working with DICE-CT images and have been increasingly running into issues where the computer crashes while there still appears to be plenty of RAM available.<br>
For reference, I am running a Windows 11 system with 128gb of memory as well as a good processor and graphics card (24GB of RAM on the card).</p>
<p>Here is a link to one of the datasets that has given me trouble:<br>
<a href="https://drive.google.com/drive/folders/1iSmk92HOYNRLLgk7SIuiC3D6YI9RCdtQ?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1iSmk92HOYNRLLgk7SIuiC3D6YI9RCdtQ?usp=sharing</a></p>
<p>I also included two log files of examples of times when the program crashed. Every time it crashes there is no record of the crash in the log files as far as I can tell, but I might just not be seeing it.</p>
<p>I have had issues at many points in the process. It has crashed when segmenting (specifically when using the flood fill tool with “show 3D” turned off). It has also crashed when I tried the “create models from visible segments” option. And finally, it sometimes crashes when I try to load the MRML scene file.</p>
<p>Throughout all of this I have been able to monitor my memory usage, and the RAM is never full when it crashes. It has often been crashing when I am using ~80GB of RAM, but sometimes it is higher or lower.</p>
<p>I updated all of my drivers and ran diagnostics on the memory sticks, but none of it indicates any hardware problems or helps the issue. I know that the file is pretty large, but I’m nowhere near maxing out my hardware so I’m not sure why that would be a problem.</p>
<p>Thanks for any thoughts or suggestions!<br>
Dave</p>

---

## Post #2 by @muratmaga (2024-05-10 18:11 UTC)

<p>So I tried this data with full resolution in a powerful cloud instance, and I cannot reproduce a crash during segmentation and/or model export. I do not know exactly what you are doing as processing, so it would be better if you can share the scene as MRB prior to crash and tell us what the step is.</p>
<p>The log files you provided has no information about crash.</p>

---

## Post #3 by @lassoan (2024-05-10 19:21 UTC)

<p>The most important advice I would give is that you don’t need to segment the image at full resolution. Goal of the segmentation is to just designate regions of the image and you don’t have to capture all small details in the segmentation. If you downsample the input image by a factor of 2x … 6x along each axis (using Crop volume module) you will get a small volume that is still perfectly suitable for designating regions in your image. This results in 10x … 200x less memory usage and approximately that much speedup of various operations (i.e., an operation that took a minute will just take a second). When your segmentation is ready, you can combine the low-resolution segmentation with your full-resolution volume using Colorize volume module.</p>
<p>For example, after performing some random segmentation at 6x lower resolution and using that for coloring of the original CT:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d68d71b928dab0c5e19e4b4ad98f09dc6c792900.jpeg" data-download-href="/uploads/short-url/uC1dJChqb1fXhvgt3Dofkd73Zo4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d68d71b928dab0c5e19e4b4ad98f09dc6c792900_2_690x415.jpeg" alt="image" data-base62-sha1="uC1dJChqb1fXhvgt3Dofkd73Zo4" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d68d71b928dab0c5e19e4b4ad98f09dc6c792900_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d68d71b928dab0c5e19e4b4ad98f09dc6c792900_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d68d71b928dab0c5e19e4b4ad98f09dc6c792900_2_1380x830.jpeg 2x" data-dominant-color="38332A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1156 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>About the crashes: I cannot reproduce any crash on Windows with the latest Slicer Preview Release, with 64 GB RAM. What operating system do you use? Did the application actually crash or just hang? Do you load the image using ImageStacks module or just the default “Add data” window? Do you convert these JPEG images from RGB to grayscale? I could not get over 40GB memory usage - could you provide step-by-step instructions on what you did exactly to consume that much memory?</p>

---

## Post #4 by @Dave_Matthews (2024-05-10 21:52 UTC)

<p>Thank you both for your responses! I didn’t realize that you could apply a low resolution segmentation to a high resolution volume, that is incredibly useful to know.</p>
<p>I tried to recreate the issue so I could save the scene file, but it appears to have gotten worse. Previously the program would just close itself with no warning or error message displayed (which explains why the logs don’t show any errors). Now it is displaying the following error if I try to save any segmentation as a model or if I try to show a segmentation in 3D:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b463a026aa02cfd584d7edbca106daab1d5f9b72.jpeg" data-download-href="/uploads/short-url/pJNoh0Slf1Z0aQk7LWvZdRHbCi6.jpeg?dl=1" title="Memory error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b463a026aa02cfd584d7edbca106daab1d5f9b72_2_690x388.jpeg" alt="Memory error" data-base62-sha1="pJNoh0Slf1Z0aQk7LWvZdRHbCi6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b463a026aa02cfd584d7edbca106daab1d5f9b72_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b463a026aa02cfd584d7edbca106daab1d5f9b72_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b463a026aa02cfd584d7edbca106daab1d5f9b72_2_1380x776.jpeg 2x" data-dominant-color="2B2C2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Memory error</span><span class="informations">1920×1080 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So the current workflow (on Windows 11) that is repeatably creating the above error is that I use the ImageStacks module to load in the volume in B&amp;W at full resolution with isotropic scaling. Then I go into the segment editor and create a new segment where I apply the threshold tool (80-255). Then I go back to the data module, right click on the segment, and click “export visible segments to model”. That’s when it throws the error “Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing virtual memory size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad array new length”. Previously it would think for a few minutes and then fully crash and close out the program.</p>
<p>As you can see, it was not using much memory when this occurred (29/128GB). Does this mean that it’s likely to be a hardware issue?</p>

---

## Post #5 by @lassoan (2024-05-11 15:54 UTC)

<p>Hardware issues are extremely rare. Most common root cause of problems is between the keyboard and display or sometimes in the software.</p>
<p>In this case, it is a mix of a few things.</p>
<p>First of all, thresholding can create a  very noisy surface, with hundreds of millions points and occluding relevant details. So, after threeholding of noisy data always apply a smoothing filter.</p>
<p>You’ve also discovered an issue in the VTK library’s vtkWindowedSincPolyDataFilter - the smoothing filter that is used on the surface extraction output. For certain size of large (but not too large inputs) it uses incorrect ID type, which causes integer overflow that leads to the exception that you saw in the popup. We’ll work with VTK developers to fix it. Until then, you can disable surface smoothing or use surface nets smoothing, which is not impacted by the vtkWindowedSincPolyDataFilter bug.</p>
<p>By enabling “Experimental / Use surface nets” option in the “Show 3D” button menu you also make surface generation about 10x faster.</p>

---

## Post #6 by @lassoan (2024-05-11 22:31 UTC)

<p>Update:</p>
<p>Thresholding between 80-255 created a model that consists of over 180 million points and 360 million cells. An average model is under 100 thousand points, so this model is unusually large.</p>
<p>I’ve submitted a bug report to VTK library anyway: <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/19346" class="inline-onebox">vtkWindowedSincPolyDataFilter crashes for large input data (#19346) · Issues · VTK / VTK · GitLab</a></p>
<p>Without smoothing the segmentation looks like this (really noisy):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d8a468d750fc5a58ee5643202a164178794132.jpeg" data-download-href="/uploads/short-url/9ovbK4wKGYKKNwkDkA9LXutt0QO.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d8a468d750fc5a58ee5643202a164178794132_2_690x223.jpeg" alt="image" data-base62-sha1="9ovbK4wKGYKKNwkDkA9LXutt0QO" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d8a468d750fc5a58ee5643202a164178794132_2_690x223.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d8a468d750fc5a58ee5643202a164178794132_2_1035x334.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d8a468d750fc5a58ee5643202a164178794132_2_1380x446.jpeg 2x" data-dominant-color="252925"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1424×462 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After median filtering with 5mm kernel size:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed4be3381b552237b03edf709be5cf223133a306.jpeg" data-download-href="/uploads/short-url/xRdKqG3wupMhQjU9DTLe9J1tDQa.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4be3381b552237b03edf709be5cf223133a306_2_690x223.jpeg" alt="image" data-base62-sha1="xRdKqG3wupMhQjU9DTLe9J1tDQa" width="690" height="223" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4be3381b552237b03edf709be5cf223133a306_2_690x223.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4be3381b552237b03edf709be5cf223133a306_2_1035x334.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed4be3381b552237b03edf709be5cf223133a306_2_1380x446.jpeg 2x" data-dominant-color="252725"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1424×462 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This smoothed segmentation is more meaningful and the generated mesh is about 10x smaller (under 40 million points and cells). Since the image is so noisy, it may also make sense to apply some smoothing (e.g., Curvature anisotropic diffusion) before segmentation.</p>

---

## Post #7 by @muratmaga (2024-05-12 02:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="36071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Experimental / Use surface nets” option in the “Show 3D” button</p>
</blockquote>
</aside>
<p>Yes, I should have mentioned that’s the option I used.</p>

---

## Post #8 by @Dave_Matthews (2024-05-17 15:19 UTC)

<p>I’ve been playing around with this a lot and just wanted to say thanks again to you both. “Use Surface Nets” has worked exceptionally well for me, and the denoising filters also make a huge difference without a noticeable impact on quality. Between these options I haven’t had any more issues with crashing and the whole process has become substantially faster.</p>
<p>Thanks so much!</p>

---
