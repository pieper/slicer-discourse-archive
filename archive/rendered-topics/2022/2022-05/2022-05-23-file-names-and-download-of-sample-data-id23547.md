# File names and download of sample data

**Topic ID**: 23547
**Date**: 2022-05-23
**URL**: https://discourse.slicer.org/t/file-names-and-download-of-sample-data/23547

---

## Post #1 by @Jacqueline_Webb (2022-05-23 19:49 UTC)

<p>Problem report for Slicer 5.1.0-2022-05-22 macosx-amd64: [please describe expected and actual behavior]<br>
I am not seeing the file names of sample data, and when I click on the sample data file it is not clear where the sample data is download. Help?</p>

---

## Post #2 by @pieper (2022-05-23 19:55 UTC)

<p>It’s not clear what are you trying to accomplish, but  SampleData is downloaded to a temp cache and loaded directly in Slicer.  For me on linux it’s in ~/.cache/NA-MIC/Slicer/SlicerIO/.  You can find the path in the Application Settings in the Cache pane.</p>

---

## Post #3 by @muratmaga (2022-05-24 15:44 UTC)

<aside class="quote no-group" data-username="Jacqueline_Webb" data-post="1" data-topic="23547">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jacqueline_webb/48/15045_2.png" class="avatar"> Jacqueline_Webb:</div>
<blockquote>
<p>I am not seeing the file names of sample data, and when I click on the sample data file it is not clear where the sample data is download. Help?</p>
</blockquote>
</aside>
<p>Sample Data is always downloaded to the path specified in the Cache settings of the APplication Settings. Unfortunately, by default this is usually a temporary folder specified by the OS, and can be buried quite a bit. If you need to access the files, you can reset this folder to whereever you want (perhaps like a folder on your desktop, like shown in the screenshot).</p>
<p>Go to <strong>Edit-&gt;Application Settings-&gt;Cache</strong> section, click on the Cache location button and set it to a folder that’s convenient.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1ed39a98bf600ea12b94bb6c2825c20b0e430ed4.png" alt="image" data-base62-sha1="4oHGmQKd1CZGrehVa2xWBcWuo8k" width="667" height="213"></p>

---
