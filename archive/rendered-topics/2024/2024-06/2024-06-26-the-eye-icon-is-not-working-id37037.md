# The eye icon is not working

**Topic ID**: 37037
**Date**: 2024-06-26
**URL**: https://discourse.slicer.org/t/the-eye-icon-is-not-working/37037

---

## Post #1 by @ebin1234 (2024-06-26 11:28 UTC)

<p>Hello, I added a markup node (ASIS_L)using a button.But the eye icon corresponding to the node in data module is not working while pressing it.  But the eye icon corresponding to other nodes are working.How to enable the eye icon of ASIS_L ?.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dc69e808089a6b3d758802648e4b77d29ff892e.png" alt="Screenshot 2024-06-26 132557" data-base62-sha1="hWFdQD1XVxJYET828gcOaVecVH0" width="548" height="82"></p>

---

## Post #2 by @cpinter (2024-06-26 11:58 UTC)

<p>This is a very basic function that I can confirm that it works. Can you post a video please so that we can see all the details? Thanks!</p>

---

## Post #3 by @ebin1234 (2024-06-26 12:18 UTC)

<p>Hello, I am posting the video .<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ace172aab47eaba129d48a00ef462d78cc6a351.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91204d474bbc8f52ec92a16c61b9c692000651da.png">
  </div><p></p>

---

## Post #4 by @cpinter (2024-06-26 12:23 UTC)

<p>Thanks, but I suppose you have a 2D or 3D view where you don’t see the change you want to see. It does not show in the video unfortunately. What I’d like to see is:</p>
<ol>
<li>How you create the markup and where it shows up</li>
<li>How do you tell that the eye does not work</li>
</ol>
<p>Update: Please use the latest Slicer, because we don’t typically fix bugs in old Slicers just the current one.</p>

---

## Post #5 by @ebin1234 (2024-06-26 13:15 UTC)

<p>Hello, I am posting videos contains 2d and 3d views. When clicking the eye-icon of ASIS_L, this point has no toggiling effect in both views. I updated the name of this markup node from ASIS_L_1 to ASIS_L using an observer via place markup button. There is a button called visibility is used to toggle the visibility of this node. But if I create a markup node using markup module in 3d slicer,it is working fine . you can see all this things in the attached videos…<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8d4f16a96e4e5b474f74b351dcf5d0194e4a19b.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32812a14b178df1918159c0699e1ee8d727e4fdb.jpeg">
  </div><p></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bc30eccda61210bd322bc3d542f05e461ff7d06.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2afb830e3b50d575fd48edd75b7b462d76a2d3b0.jpeg">
  </div><p></p>

---

## Post #6 by @cpinter (2024-06-26 13:22 UTC)

<p>This seems to be an issue in your module and not in Slicer core. I suggest looking at the Python console for error or otherwise debug your module.</p>

---

## Post #7 by @ebin1234 (2024-06-26 13:44 UTC)

<p>Thank you. It is due to error and I got it.</p>

---
