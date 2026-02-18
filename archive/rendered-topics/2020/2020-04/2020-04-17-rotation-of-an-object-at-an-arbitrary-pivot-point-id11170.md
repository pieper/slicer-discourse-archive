# Rotation of an object at an arbitrary pivot point

**Topic ID**: 11170
**Date**: 2020-04-17
**URL**: https://discourse.slicer.org/t/rotation-of-an-object-at-an-arbitrary-pivot-point/11170

---

## Post #1 by @glesage (2020-04-17 23:21 UTC)

<p>I am developing an ultrasound system with an inertial tracker attached to a linear array ultrasound probe as shown in the first figure of powerpoint and slide notes. <a href="https://1drv.ms/p/s!Ao_mcYEsQIFVhAKLDa4UKb8rVNFQ?e=B12guY" rel="nofollow noopener">https://1drv.ms/p/s!Ao_mcYEsQIFVhAKLDa4UKb8rVNFQ?e=B12guY</a> . I am using the Witmotion inertial sensor, usb frame grabber, and the plus toolkit to acquire the image and tracking data. In slicer I can see the motion of the tracker and appropriate expected motion of the tracked image in the 3D window. I want to be able to use the probe as rectal ultrasound, with the anus as a pivot point at an arbitrary point somewhere along the probe length, which in real life experience as a retired gastroenterologist is generally true. With a fixed probe pivot point, the inertial tracker estimates both the probe translations and rotations.</p>
<p>My question is how to I set up transformation matrixes so that I use a fixed pivot point for the ultrasound probe as shown in my first figure. The second powerpoint slide shows the effect of a pivot point on probe and image positions as determined by the inertial tracker. I understand that rotations can be done with objects not at (0,0,0) origin using a translation of the object to origin, rotational transformation and then translation of object back to its original position.  I don’t see a provision how to do this using plus toolkit and slicer. Some direction would be greatly appreciated.</p>
<p>I made YouTube demo for my mechanical engineer son to explain what I was doing, which shows setup for anyone who is interested. <a href="http://www.youtube.com/watch?v=3ft-Hl0ToMY&amp;feature=youtu.be" rel="nofollow noopener">www.youtube.com/watch?v=3ft-Hl0ToMY&amp;feature=youtu.be</a></p>

---

## Post #2 by @lassoan (2020-04-17 23:37 UTC)

<p>You can set adjust the rotation point position by putting the ProbeToReference transform under a new transform (ReferenceToRAS), which contains a simple translation. Setting up appropriate transformations for your system is explained in detail in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>

---
