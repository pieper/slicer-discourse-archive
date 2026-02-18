# How do you create and extend trajectories on Slicer?

**Topic ID**: 18583
**Date**: 2021-07-08
**URL**: https://discourse.slicer.org/t/how-do-you-create-and-extend-trajectories-on-slicer/18583

---

## Post #1 by @Timothy_Minicozzi_20 (2021-07-08 15:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: I would like to try to extend a line from the end of a stylus tip modeled by a needle (in order to see the trajectory that is planned by the stylus at that angle. The goal would be to have the needle model in blue, and then an extension of the needle model at the same angle in red). I would also like to model a desired trajectory given an entry and target point (I imagine this would be easier and quite doable, just a model of a line connecting the two points). Are there any modules, etc that would facilitate this?<br>
Actual behavior: I’ve tried gyro guide and path explorer but have been unsuccessful.</p>

---

## Post #2 by @Timothy_Minicozzi_20 (2021-07-08 17:50 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39517121a3cdf52f891e570640e85dd2018e83d0.png" alt="Screenshot (450)" data-base62-sha1="8b3HFq0Nem76EDttYNVO8S86W5y" width="505" height="386"><br>
For instance, the blue line shows the stylus and the red shows the planned trajectory.</p>

---

## Post #3 by @lassoan (2021-07-11 15:31 UTC)

<p>You can create a thinner needle or cylinder model (using Create Models module in SlicerIGT extension) and add it under the same StylusTipTo… transform as your current needle model. If you want, you can add a transform between this additional needle model and the StylusTipTo… transform, for example to offset the tip.</p>

---

## Post #4 by @Timothy_Minicozzi_20 (2021-07-12 17:01 UTC)

<p>Thank you! I did that and it worked beautifully!</p>

---
