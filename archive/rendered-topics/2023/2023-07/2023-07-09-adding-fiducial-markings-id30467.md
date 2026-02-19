---
topic_id: 30467
title: "Adding Fiducial Markings"
date: 2023-07-09
url: https://discourse.slicer.org/t/30467
---

# Adding Fiducial Markings

**Topic ID**: 30467
**Date**: 2023-07-09
**URL**: https://discourse.slicer.org/t/adding-fiducial-markings/30467

---

## Post #1 by @sulaimanvesal (2023-07-09 05:27 UTC)

<p>Hi,</p>
<p>I am working on prostate biopsy and I do have the x,y,z information of 16 cores top and bottom for both MRI and Ultrasound. I want to use python to automatically create a fiducial markers for bottom and tip of each biopsy cores, connect them with a line and plot them on 3D slicer automatically for a cohort of 1000 cases.</p>
<p>I understood that we can use the following command to add a marker:</p>
<pre><code class="lang-auto">slicer.modules.markups.logic().AddFiducial(
df_row['coretipX'].values[0], df_row['coretipY'].values[0], df_row['coretipZ'].values[0]
)
</code></pre>
<p>However, this does not show anything on the 3D slicer scene. And I checked markup modules → control points, and it show empty values for RAS. Although, the marker is created.</p>
<p>Thanks for the help.</p>

---

## Post #2 by @rbumm (2023-07-09 05:43 UTC)

<p>This should work:</p>
<pre><code class="lang-auto"># create new markups node
markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
markupsNode.SetName("YourNodeName")

# add fiducial 
markupsNode.CreateDefaultDisplayNodes()
markupsNode.AddFiducial(50.,48.,-173.)
</code></pre>

---

## Post #3 by @sulaimanvesal (2023-07-09 16:50 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I tried your code, but still I don’t see any of markers on 3D view nor on the panels. Would it be an issue of volume orientations (.e.g. my MRI images are not in RAS orientation)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c5d4fb3338821ee7cce392ed144f257b7c1db39.jpeg" data-download-href="/uploads/short-url/mjgp2VN6Z9qPpQ2a8Upv7VB2cYx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5d4fb3338821ee7cce392ed144f257b7c1db39_2_690x319.jpeg" alt="image" data-base62-sha1="mjgp2VN6Z9qPpQ2a8Upv7VB2cYx" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5d4fb3338821ee7cce392ed144f257b7c1db39_2_690x319.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5d4fb3338821ee7cce392ed144f257b7c1db39_2_1035x478.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5d4fb3338821ee7cce392ed144f257b7c1db39_2_1380x638.jpeg 2x" data-dominant-color="65656F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×889 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My points:</p>
<pre><code class="lang-auto">(x, y, z) Tip-&gt; 13.622, -25.451, 54.307
(x, y, z) Bot-&gt; 14.918, -13.143, 41.999
</code></pre>

---

## Post #4 by @rbumm (2023-07-09 18:59 UTC)

<p>Strange.<br>
Could you manually add the markups where you would expect them and compare them with the values you provided above?</p>

---

## Post #5 by @lassoan (2023-07-10 14:20 UTC)

<p>The screenshot shows that you are using a very old Slicer version. Please use the latest Slicer Stable Release (or the latest Slicer Preview Release, if there is any specific feature or fix that is not included in the stable version).</p>

---

## Post #6 by @sulaimanvesal (2023-07-13 19:58 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I upgraded the 3D slicer to the latest version. I can see the fluidical markers on Jyupter notebook but when I save the 3D Slicer scene the markers don’t show up. Therefore I did another trick to save the markers as numpy array and export as fcsv files. This solved the issue to some extend.</p>
<p>I have another question, is there any 3D Slicer python function that allows to save fiducial markers into segmentation output or volume output?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ee27dbeb0fbeccde88b1b104f236c74982d9cf4.jpeg" data-download-href="/uploads/short-url/bfQuRFI5A0eZ2GvjxvfJZzK61N2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ee27dbeb0fbeccde88b1b104f236c74982d9cf4_2_690x377.jpeg" alt="image" data-base62-sha1="bfQuRFI5A0eZ2GvjxvfJZzK61N2" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ee27dbeb0fbeccde88b1b104f236c74982d9cf4_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ee27dbeb0fbeccde88b1b104f236c74982d9cf4_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ee27dbeb0fbeccde88b1b104f236c74982d9cf4.jpeg 2x" data-dominant-color="1B1B1D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×700 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2023-07-15 15:35 UTC)

<p>If you save the markups and then load them then they show up. It works the same way when you use the desktop user interface or notebook. If you provide a code snippet that reproduces the unexpected behavior then we can have a look at it.</p>

---
