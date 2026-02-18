# Saving the model after Fiducial registration Model with CBCT

**Topic ID**: 30895
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/saving-the-model-after-fiducial-registration-model-with-cbct/30895

---

## Post #1 by @YOU_DDS (2023-08-01 03:04 UTC)

<p>Operating system:<br>
Slicer version:</p>
<p>I have follow your advice in the picture and it work as you have said but I have trouble saving that STL file into that registration location so that if I want to check that case next time I will only need to import the file inside 3D slicer and I don’t need to redo the registration again.</p>
<p>Do you have any suggestion for my case?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21e7d40ac5979c8d24763791cb0bdb5b5f5b8f48.jpeg" data-download-href="/uploads/short-url/4PWrFKi1wgqJtp1s0csu24AD0hy.jpeg?dl=1" title="IMG_2029" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21e7d40ac5979c8d24763791cb0bdb5b5f5b8f48_2_473x500.jpeg" alt="IMG_2029" data-base62-sha1="4PWrFKi1wgqJtp1s0csu24AD0hy" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21e7d40ac5979c8d24763791cb0bdb5b5f5b8f48_2_473x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21e7d40ac5979c8d24763791cb0bdb5b5f5b8f48_2_709x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21e7d40ac5979c8d24763791cb0bdb5b5f5b8f48.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_2029</span><span class="informations">873×922 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2023-08-02 04:34 UTC)

<p>You can use the “Export to file” feature (right-click menu in Data module) and enable “Apply transforms” option. Alternatively, you can harden the transform on the model (right-click on the transform column of the model in Data module) before saving the model (using menu: File / Save Data).</p>

---

## Post #4 by @YOU_DDS (2023-08-04 01:51 UTC)

<p>I have already find the answer, Thank you.</p>

---

## Post #5 by @YOU_DDS (2023-08-22 02:04 UTC)

<p>For those who might face the same problem. What you need to do is going to Data click on the node of the transformed model you want to save it and then click export and then you will see a tab pop up then tick on the save with transform box and finally click save.</p>
<p>This is how I do. Good luck for your project.</p>

---
