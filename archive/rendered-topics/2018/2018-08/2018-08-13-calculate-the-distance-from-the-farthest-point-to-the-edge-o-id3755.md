# Calculate the distance from the farthest point to the edge of the radiation field

**Topic ID**: 3755
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/calculate-the-distance-from-the-farthest-point-to-the-edge-of-the-radiation-field/3755

---

## Post #1 by @aseman (2018-08-13 11:53 UTC)

<p>Slicer version: 4.8.1<br>
Hi 3D slicer experts<br>
I work with radiation fields and organs such as heart and lungs. in some slices heart lies in the field and I want to calculate the distance between the farthest point (blue point in following figure)and the edge of the radiation field (wich is shown with a red arrow) in the total  heart volume that  is located inside the field. in the other word , what is the maximum distance that  the heart is inside the field?<br>
1- wich  module should I use?<br>
2- Is this distance ,the Hausdorff Distance?<br>
thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/263b03fce00bcc831eba3778b4b1aed053e22272.png" alt="picture3" data-base62-sha1="5scAdxFzT3y0CZCoK3yw8puHkUG" width="248" height="288"></p>

---

## Post #2 by @aseman (2018-08-22 17:35 UTC)

<p>Hi 3D slicer experts<br>
Unfortunately , I didn’t recieve any feedbacks for my question. Is there a module or another software that I can use to calculate the maximum length of heart in the radiation field(in the other word , the red arrow length in the above figure)?<br>
thanks a lot</p>

---

## Post #3 by @cpinter (2018-08-22 18:04 UTC)

<ol>
<li>There is no such module</li>
<li>It is not the Hausdorff distance, because between the heart and the beam it would be 0.</li>
</ol>
<p>Please give us more information about this distance, because as far as I understand your description the distance would be not the red arrow. Are there any geometric constraints you didn’t mention?<br>
Once we know what you’d like to achieve, the solution will be probably a combination of features in various modules and some python scripting.</p>

---

## Post #4 by @aseman (2018-08-25 11:45 UTC)

<p>Hi<br>
Thank you for your guidance.Unfortunately, I couldn’t find another geometric constraint .In fact, I have two series of CT images , one in normal breathing and another in deep breathing(which in deep breathing , the heart moves posteriorly, and goes away from the radiation field as well as the chest wall) . I decided to get the heart distance from the chest wall(for deep and free breathing) rather than finding the length of heart in the radiation field.<br>
if the chest wall be contoured:<br>
1- can I get the distance between the heart and chest wall?<br>
2-and, can this be done using the model to model distance module?<br>
thanks a lot</p>

---
