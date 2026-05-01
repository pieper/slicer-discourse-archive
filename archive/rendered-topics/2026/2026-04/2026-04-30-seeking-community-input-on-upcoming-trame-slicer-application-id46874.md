---
topic_id: 46874
title: "Seeking Community Input On Upcoming Trame Slicer Application"
date: 2026-04-30
url: https://discourse.slicer.org/t/46874
---

# Seeking Community Input on Upcoming trame‑slicer Applications

**Topic ID**: 46874
**Date**: 2026-04-30
**URL**: https://discourse.slicer.org/t/seeking-community-input-on-upcoming-trame-slicer-applications/46874

---

## Post #1 by @Thibault_Pelletier (2026-04-30 07:05 UTC)

<p>Hi everyone!</p>
<p>Following the discussions on the <a href="https://github.com/KitwareMedical/trame-slicer" rel="noopener nofollow ugc">trame-slicer repo</a> regarding <a href="https://github.com/KitwareMedical/trame-slicer/issues/81" rel="noopener nofollow ugc">Jupyter integration</a> and <a href="https://github.com/KitwareMedical/trame-slicer/issues/79" rel="noopener nofollow ugc">first class citizen applications in trame-slicer</a> we will be adding applications to the trame-slicer package starting the future minor version (1.11.0).</p>
<p>We’d love your input on which initial applications would be most valuable to include.<br>
If you have a specific workflow, tool, or apps you’d like to see supported, please share your thoughts so we can prioritize accordingly!</p>
<p>Best,<br>
Thibault</p>
<p>PS: Recap links for those who don’t know what trame-slicer is</p>
<ul>
<li><a href="https://www.kitware.com/trame-slicer-announcement/" rel="noopener nofollow ugc">trame-slicer blogpost</a></li>
<li><a href="https://www.linkedin.com/posts/3dslicer-medicalvisualisation-trame-share-7442143154838982656-w1ax?utm_source=share&amp;utm_medium=member_desktop&amp;rcm=ACoAAARPuogBqy03ssJuGa9vh3xFFxp_L97Ox-8" rel="noopener nofollow ugc">slicer now pip installable annoucement</a></li>
</ul>

---

## Post #2 by @mapepe18 (2026-04-30 22:02 UTC)

<p>Hi there,</p>
<p>Nice to hear about that. Here goes some suggestions to make a stronger app based on the current segmentation or medical_viewer app.</p>
<p>upgrades:</p>
<p>-in scrollable bars (slices in each view, the contrast windowing, segmentation opacity…) have some kind of value counter visible. So for example you can see which slice number you are in in each view, which image values are you setting in the contrast, etc. This could be small values beside the bars.</p>
<p>-Button with function to load a segmentation file (guess it shoulf match the loaded image for this to make sense) which I guess should activate corresponding new labels in the segmentation editor from the loaded segmentation.</p>
<p>-Button to save the current segmentation in a file.</p>
<p>-Display information on the image, maybe spacing and size which is typical useful info.</p>
<p>-New shapes for the segmentation brush (like square)</p>
<p>-The mpr crosshair could also show the pixel value of the image it is locaten on at some place</p>
<p>Bigger upgrades:</p>
<p>-What about being able to load multiple images at the same time? Thinking like itk-snap which allows to have a ‘main image’ that set the space reference and then you can upload several images and quickly change views between them in said space by clicking on them from a list. So also show the list of images and upon clicking change the view to them.</p>
<p>-Incorporating some AI for segmentation, for example based on nn-interactive or medsam. There seems to be someone that already did an app with nninteractive. Could be nice.</p>
<p>-Alternative image/segmentation uploading method. For some applications it could be useful to automatically open a predefined image/segmentation from defined path that could be as an input to the app itself in the code, instead of manually opening them.</p>
<p>I’m new with the trame framework and just started exploring the app, so if I missed a function that I already described then nothing to add.</p>
<p>Those are additions on the already available apps. Not really new apps, I just think on segmentation as the most useful tool. Also maybe a an app based on registration could be interesting too (probably way harder too).</p>
<p>Those are some ideas, hope they are good ones. I’ll keep thinking on new things.</p>
<p>Regards and thanks for the amazing work!</p>

---

## Post #3 by @Thibault_Pelletier (2026-05-01 04:02 UTC)

<p>Hi <a class="mention" href="/u/mapepe18">@mapepe18</a>,</p>
<p>Thanks for the feedbacks!<br>
I think that your suggestions definitely make sense and are features that are currently available in Slicer (except square brush) but missing in trame-slicer !</p>
<p>I will be tracking them in our backlog <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
