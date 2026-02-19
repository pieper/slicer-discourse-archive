---
topic_id: 29500
title: "How To Realize The Movement Of Mask Roi Through 3Dsclicer Wi"
date: 2023-05-17
url: https://discourse.slicer.org/t/29500
---

# How to realize the movement of mask/roi through 3dsclicer without changing the size and shape of mask/roi

**Topic ID**: 29500
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/how-to-realize-the-movement-of-mask-roi-through-3dsclicer-without-changing-the-size-and-shape-of-mask-roi/29500

---

## Post #1 by @ending (2023-05-17 07:43 UTC)

<p>Hello, everyone<br>
How to realize the movement of mask/roi through 3dsclicer without changing the size and shape of mask/roi？<br>
Please provide me with detailed steps to achieve this operation, thank you all.<br>
Look forward to your reply</p>

---

## Post #2 by @lassoan (2023-05-17 16:08 UTC)

<p>You can create a transform in Transforms module and then apply that to the segmentation.</p>
<p>The transform is applied to all segments in the segmentation, so if you want to move only one segment then you can move that segment into a separate segmentation, apply the transform, and then move the segment back to the original segmentation.</p>

---

## Post #4 by @ending (2023-05-19 03:08 UTC)

<p>Thank you for your answer</p>
<p>However, since I am not familiar with this function of 3dslicer and still do not know how to implement this process, could you please provide more detailed operation steps? Thanks!</p>
<p>Looking forward to your reply again</p>

---

## Post #5 by @muratmaga (2023-05-19 05:43 UTC)

<p>See these two documents:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html</a></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_1/Transforms/Transforms.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_1/Transforms/Transforms.md" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_1/Transforms/Transforms.md" target="_blank" rel="noopener">SlicerMorph/Spr_2021/blob/main/Day_1/Transforms/Transforms.md</a></h4>


      <pre><code class="lang-md">## Transforms
Being able to transform any of the data nodes (volumes, models, markups and ROIs) is one of the most powerful features of 3D Slicer. It is a complex module with many different options that are dependent on the type of the transform (e.g., linear or non-linear)

We will be using the `Transform` module mostly to manually align a volume or a mesh to an orientation, e.g., to bring scans/specimens into some sort of anatomical orientation. You have seen in `CropVolume` that you can use a ROI to subset a portion of your datasets. But sometimes you need more flexibility in orienting the ROI than simply moving the handles. In such case you can put your ROI node under a transform and rotate and modify it as you need. 

Let's look at the basic of the `Transform` module:

1. Go to `Data` Module, and load a 3D model. For this tutorial, I am using the Gorilla skull in the SlicerMorph `Sample Data` module but you can use any 3D model you like.
2. Make sure you are in the **Subject Hierarchy** tab of the `Data` module
3. Right-click on your 3D model node and choose **Clone**. This will create a copy of your existing model.
4. Adjust the colors of these models by clicking on the color square such that they are easily distinguished.
5. Click on the layout icon and choose **Dual 3D**
6. Click on the pin to bring 3D view settings, and the lock the two viewers. This way 3D view will be sync and any camera movement (i.e., moving specimen in 3D space will be changing both views). Rotate the specimen in one view and note that's reflected in the other viewer.
7. You can adjust the size of the 3D views by dragging the bar separating slice views from 3D viewers and moving up and down (indicated by yellow rectangle). At this point you are probably seeing only one of the specimens in both views.

&lt;img src="Transforms1.png"&gt;

8. To decide which model will be shown in which 3D view (#1 or #2), you need to go to `Models` module, and expand the **Display** section and find the **View** option (Refer to the `Modules` section if you need to refresh your memory). By default, all models are shown in all views, and since they overlap, you are only seeing one of them. Set the Clone to view #2, and the original to view #1. If you set it correctly, you should have something similar to the view above.  

9. Now switch to the **Transform Hierarchy** of the `Data` module 
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_1/Transforms/Transforms.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
