---
topic_id: 24612
title: "Segmentation Scheme"
date: 2022-08-03
url: https://discourse.slicer.org/t/24612
---

# Segmentation scheme

**Topic ID**: 24612
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/segmentation-scheme/24612

---

## Post #1 by @radiodid (2022-08-03 06:16 UTC)

<p>I need to perform the same segmentation example on a huge number of images. Is there a way to create a common sample that I could use every time for different images?</p>
<p>Sorry if this is somewhere on the forum, but I couldn’t find it</p>

---

## Post #2 by @pieper (2022-08-03 13:47 UTC)

<p>If you mean you want to use a consistent set of names/colors for the segmentations, then just create an empty segmentation with the names you want and save it as a .seg.nrrd.  Reload it for each new volume you want to segment.</p>

---

## Post #3 by @sannpeterson (2022-08-04 01:36 UTC)

<p>What do you use as the master volume when creating an empty segmentation?</p>

---

## Post #4 by @pieper (2022-08-04 13:43 UTC)

<p>You don’t need a master volume if all you want to do is create the list of names/colors.  You can set the master volume and when you load each dataset (you may need to also set the geometry before segmenting).</p>

---

## Post #5 by @sannpeterson (2022-08-10 21:48 UTC)

<p>I can’t figure out how to create a list of labels and colors without having to set a master volume. Do you mind walking me through the step? I would greatly appreciate it!</p>

---

## Post #6 by @pieper (2022-08-11 15:07 UTC)

<p>Sorry, I wasn’t really clear.  What I meant was that you don’t need to save the master volume you can just save the empty segmentation file with the segments set up with names and colors.  You do need to have a master volume for reference because it’s used to define the geometry of the segmentation (although you can change it later if you need to).</p>

---

## Post #7 by @radiodid (2022-08-11 15:48 UTC)

<p>Please tell me how can I save it in the master volume or edit it later in the master volume?</p>

---

## Post #8 by @pieper (2022-08-11 17:15 UTC)

<p>What I mean is that you can load up an example volume of the type you want to segment and use it as the master volume to create a segmentation.  You can set the names, colors, and other properties of the segments you want in your scheme.  Then save the segmentation as a .seg.nrrd file that you can then load along with each volume you want to segment.  If that’s not helping perhaps I’m not understanding your question.</p>

---

## Post #9 by @sannpeterson (2022-08-12 02:33 UTC)

<p>Thanks so much! You have no idea how much time you have saved me <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---
