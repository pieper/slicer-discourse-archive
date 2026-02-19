---
topic_id: 19586
title: "Create Line Profile For Given Coordinates Not Markup Points"
date: 2021-09-09
url: https://discourse.slicer.org/t/19586
---

# Create line profile for given coordinates not markup points

**Topic ID**: 19586
**Date**: 2021-09-09
**URL**: https://discourse.slicer.org/t/create-line-profile-for-given-coordinates-not-markup-points/19586

---

## Post #1 by @M.Odaba (2021-09-09 03:26 UTC)

<p>I went through the Python code of the Line Profile, it only accepts the location of markup points manually created on the views to create a line profile. I need to create the line profiles out of know coordinates in the 3D space. Do you know how I can use my own points (using x,y,z coordinates) instead of manually selecting the markup points? Thanks.</p>

---

## Post #2 by @lassoan (2021-09-09 04:18 UTC)

<p>Markup points positions are specified using physical coordinates already. You can type the coordinates in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#panels-and-their-use">Markups module’s Control points section</a>, or copy-paste the coordinates values from the clipboard, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html">load them from a text, csv, or json file</a>, or <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#how-to-draw-a-curve-using-control-points-stored-in-a-numpy-array">set them from a numpy array</a>.</p>

---

## Post #3 by @M.Odaba (2021-09-09 23:24 UTC)

<p>Would you explain in detail what you meant by “Markup points positions are specified using physical coordinates already”?<br>
I think my question is more about when I have the markup points and they should be used as the inputs of the Line Profile. How the Line Profile code can import the list of given points and create the lines/tables?<br>
Thanks a lot.</p>

---

## Post #4 by @lassoan (2021-09-10 03:16 UTC)

<aside class="quote no-group" data-username="M.Odaba" data-post="3" data-topic="19586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e9c0ed/48.png" class="avatar"> M.Odaba:</div>
<blockquote>
<p>I think my question is more about when I have the markup points and they should be used as the inputs of the Line Profile</p>
</blockquote>
</aside>
<p>You can draw a line (placing the endpoints anywhere) and then go to Markups module and type the point coordinates. If you don’t want to type them then write the point coordinates in one of the file formats that I linked above and load that file.</p>
<aside class="quote no-group" data-username="M.Odaba" data-post="3" data-topic="19586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e9c0ed/48.png" class="avatar"> M.Odaba:</div>
<blockquote>
<p>create the lines/tables?</p>
</blockquote>
</aside>
<p>If you click on “Compute intensity profile” then the table and plot are created automatically. If you want to drive this from Python entirely (no GUI at all) then you can instantiate and use the <code>LineProfileLogic</code> class.</p>

---
