# Resolution in 3dslicer

**Topic ID**: 5272
**Date**: 2019-01-04
**URL**: https://discourse.slicer.org/t/resolution-in-3dslicer/5272

---

## Post #1 by @Pilar (2019-01-04 10:52 UTC)

<p>Hi 3D Slicer experts,</p>
<p>I have a doubt about 3DSLicer.</p>
<p>What is the level of image resolution used by the program? How many points does 3DSlicer use in each image? 10,000, 100,000, 500,000,…<br>
Or in the case that it could change according to the type of file that you use, where can I find out?<br>
In the case that it says the area of the image, where can I find out the points registered by square millimeters?</p>
<p>Thank you in advance</p>
<p>Pilar</p>

---

## Post #2 by @cpinter (2019-01-04 14:25 UTC)

<blockquote>
<p>How many points does 3DSlicer use in each image?</p>
</blockquote>
<p>Exactly as many as the resolution of the image. For a CT, it can be 512x512x400, for histology it can be 50000x30000, etc. What kind of image do you use? And why do you think it is not shown with the correct resolution?<br>
(Note that by default the image in the 2D viewers is interpolated, you can turn it off in the small window that opens when you hover the icon in top left corner of the viewer)</p>
<blockquote>
<p>Or in the case that it could change according to the type of file that you use, where can I find out?</p>
</blockquote>
<p>In the Data module right-click the image you want to see the details of, and select Edit properties. It will take you to the Volumes module and select your image. There you’ll see all the metadata of the image.</p>
<blockquote>
<p>In the case that it says the area of the image, where can I find out the points registered by square millimeters?</p>
</blockquote>
<p>Where does it say the area of the image? What registered points are you talking about?</p>

---
