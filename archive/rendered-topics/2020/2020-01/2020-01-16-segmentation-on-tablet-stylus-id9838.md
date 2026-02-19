---
topic_id: 9838
title: "Segmentation On Tablet Stylus"
date: 2020-01-16
url: https://discourse.slicer.org/t/9838
---

# Segmentation on Tablet/stylus

**Topic ID**: 9838
**Date**: 2020-01-16
**URL**: https://discourse.slicer.org/t/segmentation-on-tablet-stylus/9838

---

## Post #1 by @sarvpriya1985 (2020-01-16 15:32 UTC)

<p>Hi,</p>
<p>Are there any recommendations regarding segmentation using stylus/using a tablet. Which device/hardware is best to buy that would work slicer effectively.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @hherhold (2020-01-16 16:11 UTC)

<p>I have a Wacom Intuos Pro, medium size tablet. I program the buttons on the pen and tablet to switch segmentation tools. I find it invaluable.</p>

---

## Post #3 by @lassoan (2020-01-16 16:23 UTC)

<p>We test Segment Editor with Microsoft Surface Book and Pen, but it’s good to hear that it works well with Wacom tablets, too.</p>

---

## Post #4 by @sarvpriya1985 (2020-01-16 18:21 UTC)

<p>Thanks. Is it able to handle volume dicom ct data set. I mean the cost of this tablet is almost 1/4 th of surface pro.</p>
<p>Thanks<br>
Sarv</p>

---

## Post #5 by @sarvpriya1985 (2020-01-16 18:40 UTC)

<p>Thanks. I work with cardiac ct data sets. As I mentioned the cost of this is less so more affordable. Just wanna confirm if this czz a n handle 4d volume data set.</p>
<p>Thanks</p>

---

## Post #6 by @hherhold (2020-01-16 19:00 UTC)

<p>I should amend my specs - my Wacom drawing tablet is hooked up to a MacBook Pro, I’m not using an all-in-one style tablet.</p>

---

## Post #7 by @lassoan (2020-01-16 19:12 UTC)

<p>You can borrow a friend’s Surface Book or drop into a Microsoft store to try which configuration is strong enough for your data sets. You can install Slicer without admin rights on computers that are on display (I’ve done that to try the Surface Studio) and download your data from dropbox or onedrive.</p>

---

## Post #8 by @sarvpriya1985 (2020-01-16 19:50 UTC)

<p>Thanks for the info. So it’s the Mac or windows based hardware which drives the Wacom tablet. Just to be sure if I understood you correctly.</p>
<p>Andras will try to see surface pro. I hope that will work.</p>
<p>Thanks</p>

---

## Post #9 by @muratmaga (2020-01-16 20:00 UTC)

<p>Do you have tutorial about programming keys in wacom for Slicer? it is a question comes often in the workshop/tutorials and I have no experience.</p>

---

## Post #10 by @hherhold (2020-01-16 20:29 UTC)

<p>Sure, I just use the standard shortcuts for slicer in Segment Editor (Esc, space, 1, 3, !, i, @ and so on). The tablet I use has 8 programmable buttons on the left side, and in System Preferences -&gt; Wacom Tablet, you click on “Functions”, and then you can change the function of each button to “Keystroke…”</p>
<p>I generally switch a lot between paint, scissors, and island effects, turning on and off intensity masking with ‘i’ to speed things up a little bit (fewer compares) so those are the ones I map to the programmable tablet buttons.</p>
<p>I used to map all of these to a programmable 5 button left-handed mouse, but the drivers are 32 bit and it doesn’t work properly under MacOS 10.15 (yet). The beauty of this is that you can keep your left hand on the mouse and right hand on the stylus, and you never have to take your hands off the “controls” to change functions. It only takes a couple of seconds to take your hand off, push a button, and go back, but if you do that 200 times a day, over the course of a month, that’s over 2 hours just moving your hands. Programmable buttons on the stylus pad are <em>almost</em> as good, but I got pretty used to my programmable mouse.</p>
<p>Hope this helps!</p>

---

## Post #11 by @ungi (2020-01-17 14:39 UTC)

<p>I have a large Wacom Pro (the distances are about the same on the tablet as on the monitor), and a 10.4’ medium size Wacom Intuos tablet. I actually prefer the medium size one. I can always zoom in and out in Slicer if I need to scale the effect of your motions. And the mediums size tablet easily fits on my desk besides keyboard and mouse. The light weight can be a big advantage too.<br>
I also use the Wacom software to set up custom keys for the shortcuts in segmentations. You can also write simple custom modules in Slicer in a few hours. E.g. I use a module that steps a sequence browser when I press a letter, and I assigned that letter to the lower pen button. I just recorded a video using this setup:</p>
<div class="lazyYT" data-youtube-id="zlrUFaP9q1w" data-youtube-title="Fast ultrasound segmentation for generating AI training data" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
