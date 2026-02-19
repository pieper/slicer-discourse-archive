---
topic_id: 13800
title: "How To Reslice Polydata Insert Into Imagedata"
date: 2020-10-01
url: https://discourse.slicer.org/t/13800
---

# How to reslice polydata insert into imagedata?

**Topic ID**: 13800
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/how-to-reslice-polydata-insert-into-imagedata/13800

---

## Post #1 by @11111 (2020-10-01 16:31 UTC)

<p>Hey guys, I am now building a medical project and need some tips.<br>
This project is for surgeon. A doctor need to implant bone nail and interactive with nails.</p>
<p>I have bone image data from CT, and STL file of nails.<br>
I can read both of object, but I don’t know how do implement this project better.<br>
So I come to ask.</p>
<p>Here is the function I need to do</p>
<ol>
<li>insert nail into bone and the nail can be moved<br>
I add nail to the position I want and active with vtklinewidget2 for calculate the rotate angle this origin position</li>
<li>I need to reslice whole 3D in window result to 2D slice image, Like below. Here comes the problem.<br>
I can do reslice with reslicewidget , but when nail is implant. I am not sure how to show slice of nail and set it at right postion.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89774fc3deed409b18c29600b0233f7c0836738c.jpeg" alt="image" data-base62-sha1="jC52jwIny7pfaHN9XxBePrryh1a" width="685" height="500"><br>
Should I concat both of object to imagedata or polydata?<br>
Is it possible to make slice without extension, only using origin VTK package?</li>
</ol>

---

## Post #2 by @pieper (2020-10-01 18:02 UTC)

<p>Looking at this code might help:</p>
<aside class="quote quote-modified" data-post="33" data-topic="1073">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-install-pedicle-screws-simulator-extension/1073/33">How to install pedicle screws simulator extension?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Feel free to send any questions to this forum. 

So far we are OK here - Canada has not been hit very hard yet.
  </blockquote>
</aside>


---

## Post #3 by @11111 (2020-10-02 06:29 UTC)

<p>Is it reslice base on NRMLmarkupNosw?</p>

---
