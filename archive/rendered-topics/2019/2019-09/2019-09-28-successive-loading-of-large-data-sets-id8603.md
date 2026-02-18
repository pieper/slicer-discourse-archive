# Successive loading of large data sets

**Topic ID**: 8603
**Date**: 2019-09-28
**URL**: https://discourse.slicer.org/t/successive-loading-of-large-data-sets/8603

---

## Post #1 by @Michael_Ef (2019-09-28 13:13 UTC)

<p>Dear all,</p>
<p>I’d like to render a quite big stack of histological images. Due to the size I am not even able to convert the vector volume to a scalar volume in full resolution (memory allocation issues on a machine with 32gb ram). Therefore I was wondering if I could cut the image data into pieces, process them one by one and subsequently display these partial volumes in one scene mapping their spacial orientation somehow. Or is it even possible to load the desired volume when the user zooms into a specific region (assuming there is a low resolution model of the whole data set displayed at start)?<br>
Is it conceivable that I can achieve this in Slicer?</p>
<p>Thanks in advance!</p>
<p>Regards,<br>
Michael</p>

---

## Post #2 by @muratmaga (2019-09-28 16:10 UTC)

<p>If you are running out of memory, you can try to increase the virtual memory size and then things usually work (but slowly).</p>
<p>The other alternative is to open the stack in fiji and save it as a NRRD stack, then load that into Slicer. We will be working on a import tool that will offer more conveniences to users working with non-medical image sequences, but that will take awhile.</p>
<p>However, you should keep in mind that if your dataset is very big, you may run into other difficulties in visualizing, segmenting etc, and you need equally resource-rich computer. Rule of thumb is about 6-10 times large memory than your dataset.</p>

---

## Post #3 by @Michael_Ef (2019-09-29 11:12 UTC)

<p>Hello Murat,</p>
<p>thanks for your reply. I’ve already tried to increase the virtual memory, but i was still running into memory problems. I will try to convert the data to a nrrd stack. hopefully this works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Jep, i already experienced that. Therefore my question if it is possible to split the data / volume and just load the needed data.</p>
<p>Regards,<br>
Michael</p>

---

## Post #4 by @muratmaga (2019-09-29 16:54 UTC)

<p>There isn’t a function that lets you import a ROI from a large stack during the time of import (at least one that I am aware of). That’s something we would like to address soon-ish with the import tool.</p>
<p>Meanwhile, probably your simplest option is to load the original stack to Fiji, crop just the region would like to work on and save it is NRRD.</p>
<p>If you need to retain the spatial relationships preserved, another alternative might be creating NHDR headers for chunks of your data (let’s day for every 50 slides or something) and define the offset. I never tried to do that, but I think in theory it should be possible.<br>
<a href="http://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="nofollow noopener">http://teem.sourceforge.net/nrrd/format.html</a></p>

---
