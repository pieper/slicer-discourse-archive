# How to segment two different mandible on two CBCT in different settings and overlay to show difference

**Topic ID**: 21198
**Date**: 2021-12-24
**URL**: https://discourse.slicer.org/t/how-to-segment-two-different-mandible-on-two-cbct-in-different-settings-and-overlay-to-show-difference/21198

---

## Post #1 by @Koen (2021-12-24 13:48 UTC)

<p>Hi all,</p>
<p>I have the following question. How can you segment the mandible in two different scan with different settings into one model to show what different there is pre and post surgery.</p>
<p>It are two cone beam CT scans. Manuel segmentation is an option how ever I would like to do both in the same way so it is best to compare them and show what difference there is.</p>
<p>Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"> !</p>

---

## Post #2 by @mohammed_alshakhas (2021-12-29 16:03 UTC)

<p>Option 1<br>
Register the two images cbct 1 over cbct 2 .<br>
Then render the images to visualize the differences</p>
<p>Option 2<br>
Segment both mandibles , transform to models .<br>
Then register models</p>
<p>Registration is process of superimposition of   two images or models . This can be Manual or semiautomatic .</p>
<p>I believe option 1 is better since cbct is very noisy and segmentation is not very easy or accurate based in it .<br>
if you are concern with dental details , You must scan models since teeth won’t be that clear .</p>

---

## Post #3 by @Koen (2021-12-30 07:25 UTC)

<p>Hi Momhammed,</p>
<p>Thank you for your answer. I will try option 1 first, and then see if that is sufficient.</p>

---

## Post #4 by @MAXFAXSURGEON (2022-02-04 12:58 UTC)

<p>I need also to compare the condyle shapes and location after surgery and also to evaluate remodeling after one year: I am using T1, T2 and T3 CT:<br>
I am doing this comparative study using both ITK-SNAP and 3D Slicer to do cranial base segmentation then registration then segmentation of the mandible for registered CT then modeling mandible then clipping the condyle for the measurements using 3D SPHARM… do you recommend an easier method then this lengthy procedure?</p>

---
