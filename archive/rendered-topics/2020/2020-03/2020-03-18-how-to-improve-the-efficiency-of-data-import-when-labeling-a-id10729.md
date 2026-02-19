---
topic_id: 10729
title: "How To Improve The Efficiency Of Data Import When Labeling A"
date: 2020-03-18
url: https://discourse.slicer.org/t/10729
---

# How to improve the efficiency of data import when labeling a large amount of data?

**Topic ID**: 10729
**Date**: 2020-03-18
**URL**: https://discourse.slicer.org/t/how-to-improve-the-efficiency-of-data-import-when-labeling-a-large-amount-of-data/10729

---

## Post #1 by @RayCui (2020-03-18 12:00 UTC)

<p>When I check and modify the labeled data, I found that it took more time to import the data. Raw data and labeled data are imported in groups. I found:</p>
<ol>
<li>If I import a large amount of data at once, the slicer will take a long time and take up too much memory.</li>
<li>If I import only part of the data groups at a time, I need to import it multiple times.<br>
In addition, when I check and modify the labeled data, I often need to switch to display different data pairs, especially when there are many members in the data group, it is very time consuming.</li>
</ol>
<p>How should I do to improve the efficiency of data import?<br>
I think of a way is to write the correspondence of each group of data to csv, and then import the csv file, select each piece of data of csv to switch the data group. Is there an extension can achieve this? Can anyone give me some advice?</p>

---

## Post #2 by @lassoan (2020-03-18 13:30 UTC)

<aside class="quote no-group" data-username="RayCui" data-post="1" data-topic="10729">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>If I import a large amount of data at once, the slicer will take a long time and take up too much memory.</p>
</blockquote>
</aside>
<p>The more data you load, the more memory will be used. If memory usage gets close the amount of physical RAM installed in your computer, operations will start to slow down by a factor of 10x-100x. If you need to visualize a lot of data sets at once then you can either install more RAM or downscale your data (e.g., using Crop Volume module).</p>
<aside class="quote no-group" data-username="RayCui" data-post="1" data-topic="10729">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raycui/48/4517_2.png" class="avatar"> RayCui:</div>
<blockquote>
<p>I think of a way is to write the correspondence of each group of data to csv, and then import the csv file, select each piece of data of csv to switch the data group. Is there an extension can achieve this?</p>
</blockquote>
</aside>
<p>To review items one by one in a large data set collection, you can use <a href="https://github.com/JoostJM/SlicerCaseIterator">Case Iterator</a> extension.</p>

---

## Post #3 by @RayCui (2020-03-19 12:19 UTC)

<p>Thank you, Andras.<br>
The <a href="https://github.com/JoostJM/SlicerCaseIterator" rel="nofollow noopener">Case Iterator </a> extension is helpful.</p>

---
