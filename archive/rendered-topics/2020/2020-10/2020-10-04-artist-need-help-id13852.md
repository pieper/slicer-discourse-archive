# Artist need help

**Topic ID**: 13852
**Date**: 2020-10-04
**URL**: https://discourse.slicer.org/t/artist-need-help/13852

---

## Post #1 by @Hugolivet (2020-10-04 15:22 UTC)

<p>Hi! My name is Hugo Livet, I am a french artist working with drawing and sculpture.<br>
I’m trying to use Slicer to make a 3D object from a drawing animation. I have a png sequence of images made of black dots on a transparent background and I would like to turn it into an STL file. I tried to follow some YouTube tutorials, but it doesn’t work with my images.<br>
I would like to see each frame on top of each other, but I need to have only the dots visible…<br>
When I try to render I can’t see the dots, just some big black shape…<br>
Can someone help me? I’m a total beginner, and I need some advices!<br>
Thanks</p>

---

## Post #2 by @pieper (2020-10-04 15:39 UTC)

<p>Hi -</p>
<p><a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md">This tutorial about ImageStacks</a> should help.<br>
If you are still having troupble you can share examples of the kind the data I’m sure someone can help you.</p>

---

## Post #3 by @Hugolivet (2020-10-06 13:16 UTC)

<p>Thank you !!<br>
I finally works (almost). I converted my black dots into white dots on black background and followed the tutorial. I also had a resolution problem that I fixed by cropping and isotropic spacing. Now I have a pretty nice preview on slicer.<br>
So to export an STL file, I made a segmentation using threshold, still looking good, but when I try to open my STL or OBJ file with a 3d software it doesn’t work… It works without interpolation but then my resolution is too low and the points just turn into sharp lines…<br>
The files are huge (1 to 2 GB), but I have a i7-6700k 4.00Ghz computer with 6gb nvidia+32Gb ram so it should be able to open it I guess.</p>
<p>Any idea ?</p>

---

## Post #4 by @pieper (2020-10-06 13:30 UTC)

<p>I don’t know about your other software, but it would be good to test a small example and if that works then probably the size of the data is the issue.  You can downsample on import with ImageStacks or smooth the segmentation more before exporting.  There are many options to explore, but what works best is hard for us to guess.</p>

---

## Post #5 by @Hugolivet (2020-10-07 11:21 UTC)

<p>Thank you Steve !<br>
I cropped a small part and it worked ! So the size was the issue…<br>
Thanks for your help !</p>

---
