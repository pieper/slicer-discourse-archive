# Set points for seed grow

**Topic ID**: 5298
**Date**: 2019-01-07
**URL**: https://discourse.slicer.org/t/set-points-for-seed-grow/5298

---

## Post #1 by @anandmulay3 (2019-01-07 13:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> i need a small help -  i want to place seed points in script to use seedgrow from a batch script , How can i get those points? for a testing purpose where can i find those location points in slicer editor window?</p>

---

## Post #2 by @brhoom (2019-01-07 14:14 UTC)

<p>place some fiducials points  in your image then save them. The saved fcsv file can be opened as text file.</p>
<p>You can also fine information about the points in the “Markups” module.</p>

---

## Post #3 by @anandmulay3 (2019-01-16 11:20 UTC)

<p>Thanks <a class="mention" href="/u/brhoom">@brhoom</a> , it works for now for my script testing purpose.<br>
Now i’m looking for a way where i can set those points in external window where i can add those points in those series images and relate it in my slicer script.<br>
<a class="mention" href="/u/lassoan">@lassoan</a>  Any idea to get this thing done?</p>

---

## Post #4 by @lassoan (2019-01-16 12:52 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="3" data-topic="5298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>external window</p>
</blockquote>
</aside>
<p>What is an “external window”? A different process?</p>

---

## Post #5 by @anandmulay3 (2019-01-16 13:00 UTC)

<p>yes , i mean a separate application window , from which i’ll pass the inputs to my seedgrow model creation script.</p>

---

## Post #6 by @lassoan (2019-01-17 05:52 UTC)

<p>Separate application window in Slicer? Above you wrote that you would like to place seed points from a batch script but now you are talking about another window.</p>
<p>Could you tell us what would you like to achieve? For example: Are you trying to use Slicer’s segmentation tools from MATLAB-based GUI? Or you have some manually annotated data sets and would like to use that information in Slicer?</p>

---

## Post #7 by @anandmulay3 (2019-01-17 07:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Yes i’m using a seed points from batch script , but here i’m developing a application to view image series through which he can set some seed points and those points i want to pass to a batch script .</p>
<p>i’m trying to make a image viewer which will generate a 3d models using batch scripts.</p>

---

## Post #8 by @lassoan (2019-01-22 21:16 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="7" data-topic="5298">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>here i’m developing a application to view image series through which he can set some seed points and those points i want to pass to a batch script</p>
</blockquote>
</aside>
<p>Why don’t you use 3D slicer to view image series and set seed points? Note that you can fully customize appearance of the application. For example, you can choose to show a file selector popup and a single slice viewer and an OK button.</p>

---
