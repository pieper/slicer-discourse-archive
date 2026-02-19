---
topic_id: 28496
title: "Monailabel And 3D Slicer Image Together On One Docker"
date: 2023-03-21
url: https://discourse.slicer.org/t/28496
---

# MonaiLabel and 3D Slicer Image together on one docker.

**Topic ID**: 28496
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/monailabel-and-3d-slicer-image-together-on-one-docker/28496

---

## Post #1 by @lenlobo (2023-03-21 14:01 UTC)

<p>Hello,<br>
I am quite new to Monai and Slicer, facing some difficulties here at the moment. I know there is a MonaiLabel docker image, and there is a 3dSlicer docker image. I want to run both of these together on a server and make them communicate or work together.<br>
I have figured the way to run MonaiLabel image and start the server, but cannot find or find a way to start  the 3d slicer on the server and then connect it with MonaiLabel.<br>
Question in specific would be, is this possible?<br>
Or how to setup a docker in a such a way that both images (if they exist) load onto the server.</p>

---

## Post #2 by @pieper (2023-03-21 20:24 UTC)

<p>If you really want two different docker instances to communicate over the a network, it is really more of a docker question, so you may need to ask their support or an appropriate forum.  Exposing ports and so forth is very docker-specific.  But if you run Slicer inside a docker instance there’s no reason you couldn’t install MONAI Label inside that same instance, just as you would on a desktop or on a virtual machine.</p>

---
