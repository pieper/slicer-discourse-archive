# Distance measurement for tumor treatment

**Topic ID**: 36198
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/distance-measurement-for-tumor-treatment/36198

---

## Post #1 by @Mouadh_Ben_Nasr (2024-05-16 05:35 UTC)

<p>Hello ,<br>
I am working to 3D modeling of distance between a tumor and its largely treated zone.<br>
I have already registered modalities of patients which are segmented using medical software.<br>
« Substract » Boolean operators are used to separate the volumes.<br>
I am using the ModeltoModel model and Hausdroff distance to  calculate the distance to the normal liver.<br>
However, I tried to use the Thermoablation margin extension,<br>
I got several questions : for the ModelToModel distance, the signed distance between tumor ( as reference) and normal liver shall be acceptable? Does this correspond to the Average surface distance ?<br>
As for Hausdroff distance, I don’t get a minimum from the available module  (which I read because of its use for evaluating overlapping volumes). The maximum are usually greater than the ModelToModel distance (because it takes the maximum of the minimum).<br>
Are there other metrics for distance evaluation?<br>
Thanks a lot!</p>

---
