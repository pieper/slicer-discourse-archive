---
topic_id: 16278
title: "Export Formats For Markups"
date: 2021-03-01
url: https://discourse.slicer.org/t/16278
---

# Export formats for markups

**Topic ID**: 16278
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/export-formats-for-markups/16278

---

## Post #1 by @anromero (2021-03-01 02:42 UTC)

<p>Could someone please explain the difference between the export options for fixed landmarks (fiducials) and semiLM patches in 3D Slicer? I’m not familiar with the .mrk.json, .json, .fcsv, and *.fcsv formats or the advantage of using one over the other. I’m planning to import these files into R for GM analysis using the geomorph package for analysis.</p>
<p>Additionally, I’m currently exporting these as .fcsv files, but I’m not able to make excel recognize and separate the file contents correctly. I’ve tried opening the app and using the open option and selecting the file, but it just opens without separating the contents into cells by commas. Any advice on this topic would be appreciated as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c31925469279983b3b6882d8c52f9696477be02.jpeg" data-download-href="/uploads/short-url/aS2uExKhR92KT1m7fnkF9Zrajlw.jpeg?dl=1" title="Screen Shot 2021-02-28 at 3.28.52 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c31925469279983b3b6882d8c52f9696477be02_2_690x445.jpeg" alt="Screen Shot 2021-02-28 at 3.28.52 PM" data-base62-sha1="aS2uExKhR92KT1m7fnkF9Zrajlw" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c31925469279983b3b6882d8c52f9696477be02_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c31925469279983b3b6882d8c52f9696477be02_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c31925469279983b3b6882d8c52f9696477be02_2_1380x890.jpeg 2x" data-dominant-color="B8B9CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-28 at 3.28.52 PM</span><span class="informations">3562×2298 852 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-03-01 03:43 UTC)

<p>First off, if you want to read markups into R, we have a few simple convenience functions that you might find useful. <a href="https://github.com/muratmaga/SlicerMorph_Rexamples" class="inline-onebox">GitHub - muratmaga/SlicerMorph_Rexamples: Some functions to import SlicerMorph data into R</a> (look at read.markups.fcsv.R and read.markups.json.R).</p>
<p>Another option is to use the <strong>log_parser.R</strong> script. Recent versions of GPA module in SlicerMorph writes a simple log file that contains important information such as the number of landmark, input file locations etc (see the readme.MD in the link above for details).</p>
<p>Finally, <strong>geomorph_regression.R</strong> provides an example of how to use procrustes aligned coordinates from SlicerMorph in R. It also shows an example of directly reading the original coordinates into R (to show that results are identical either way).</p>
<aside class="quote no-group" data-username="anromero" data-post="1" data-topic="16278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anromero/48/10120_2.png" class="avatar"> anromero:</div>
<blockquote>
<p>Additionally, I’m currently exporting these as .fcsv files, but I’m not able to make excel recognize and separate the file contents correctly.</p>
</blockquote>
</aside>
<p>You might find it easier to process them in R with the scripts I provided above. But if you want to see the contents in Excel, just use the <strong>Text to Columns</strong> option under Data (and choose comma as separator).</p>
<aside class="quote no-group" data-username="anromero" data-post="1" data-topic="16278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anromero/48/10120_2.png" class="avatar"> anromero:</div>
<blockquote>
<p>I’m not familiar with the .mrk.json, .json, .fcsv, and *.fcsv formats or the advantage of using one over the other.</p>
</blockquote>
</aside>
<p>If you are only doing landmarks (whether semi or anatomical LMs) and your goal is shape analysis in R, then the difference between fcsv and json is not much. However, if you are using other Markup types such as lines, closed curves, planes, etc., and particularly if you are making measurements from them, fcsv <strong>cannot store</strong> these measurements, while JSON can. For example, if you create a line with two Fiducal markups that is 10 mm long, if you save this file as fcsv and load it back into Slicer, all you will get will be the coordinates of the two control points that used in making the line. There won’t be a length measurement, there won’t be a visualization of that line segment. If you save it as json, they will be restored next time you load that into Slicer.</p>

---

## Post #3 by @anromero (2021-03-01 15:10 UTC)

<p>Great, thank you! This is exactly what I needed to know.</p>

---

## Post #4 by @anromero (2021-03-02 13:03 UTC)

<p>I’m so grateful for your infinite patience.</p>
<p>New problem: I accidentally saved the file after I applied the text to columns function, and now when I try and reload the file into 3D Slicer it won’t read the fiducial coordinates. I tried using the TEXTJOIN function to rejoin the text into a single column with the comma delimiter in Excel, but that isn’t making any difference. I realize this is more of an Excel help kind of question, but I’m hoping you might have some ideas for how I can make the file readable for 3D Slicer again.</p>

---

## Post #6 by @muratmaga (2021-03-02 16:59 UTC)

<p>Well as you discovered, that’s one reason not to use excel.</p>
<ol>
<li>In excel save your original fcsv in csv format using save as.</li>
<li>Open the csv file in notepad (or a simple text editor) and paste these on top of the file (including the # sign)</li>
<li>save and try opening in Slicer now.</li>
</ol>
<blockquote>
<pre><code># Markups fiducial file version = 4.13
# CoordinateSystem = LPS
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
</code></pre>
</blockquote>

---

## Post #7 by @anromero (2021-03-02 18:23 UTC)

<p>I certainly have discovered a lot in the last 12 hours, including the sheer panic. I will not be saving those edited files again. Thank you, thank you, thank you! Maybe it’s time to lose the incessant need to meticulously check my data at every step.</p>

---

## Post #8 by @muratmaga (2021-03-02 18:37 UTC)

<aside class="quote no-group" data-username="anromero" data-post="7" data-topic="16278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anromero/48/10120_2.png" class="avatar"> anromero:</div>
<blockquote>
<p>o lose the incessant need to meticulously check my data at every step.</p>
</blockquote>
</aside>
<p>You should do that, particularly when you are learning the software and creating a workflow.</p>
<p>The thing is you really shouldn’t be editing those fcsv, but just looking at the contents to make yourself familiar with the format, and what you are exporting. For that a notepad editor would suffice. Better use something like R where you can programmatically read them and don’t worry about overwriting the files…</p>
<p>If you are editing them to make some changes, that’s pretty much  something you shouldn’t do.</p>

---

## Post #9 by @anromero (2021-03-02 18:44 UTC)

<p>Got it. Wasn’t doing any editing, just wanting to see what was in them in a way that didn’t make my eyes cross. But it’s easy enough to import them and do that in R, I suppose. Thanks again!</p>

---

## Post #10 by @lassoan (2021-03-02 19:06 UTC)

<p>It takes just 2-3 commands to read or write control points from/to csv file - see examples <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#use-markups-json-files-in-any-python-environment">here</a>.</p>
<p>While this is really easy to do, maybe we should expose csv (not fcsv) import/export of markups control point coordinates somewhere on the GUI.</p>

---

## Post #11 by @muratmaga (2021-03-02 19:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="16278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>While this is really easy to do, maybe we should expose csv (not fcsv) import/export of markups control point coordinates somewhere on the GUI.</p>
</blockquote>
</aside>
<p>I would discourage this, because there is already enough confusion about LPS/RAS and how the format is changed thru times and how control points displayed in Markups module versus saved in file. Without those headers saved in the file, it would be a big headache.</p>

---

## Post #12 by @lassoan (2021-03-02 19:12 UTC)

<p>I don’t mean it as a save format, strictly as an import/export format. But I fully agree that if we can educate people to move away from csv and use json instead then that’s much better.</p>

---

## Post #13 by @lassoan (2021-03-02 20:35 UTC)

<p>By the way, Excel can import json files very nicely as a data source, the same way as it can generate live table views from various other databases (see step-by-step instructions below). So, Excel’s limitation is not that it cannot load JSON files, but in what analysis it can do on them and that you need to use the GUI or VBA (or maybe C#), which are not that well suited for data analysis.</p>
<hr>
<p>Step-by-step instructions for importing a markups json file (*.mrk.json) into Excel as a live data source:</p>
<ul>
<li>In the ribbon, choose Data / Get data / From file / From JSON, and select the *.mrk.json file</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a5700de4b382f5df7866af285608cd5bfbbce84.png" data-download-href="/uploads/short-url/jJOihk7O4EKJj0UOUPxKhiESMRu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5700de4b382f5df7866af285608cd5bfbbce84_2_244x250.png" alt="image" data-base62-sha1="jJOihk7O4EKJj0UOUPxKhiESMRu" width="244" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5700de4b382f5df7866af285608cd5bfbbce84_2_244x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5700de4b382f5df7866af285608cd5bfbbce84_2_366x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5700de4b382f5df7866af285608cd5bfbbce84_2_488x500.png 2x" data-dominant-color="E4E8E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">713×728 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><code>= Table.SplitColumn(#"Extracted Values1", "Column1.position", Splitter.SplitTextByDelimiter(";", QuoteStyle.Csv), {"Column1.position.1", "Column1.position.2", "Column1.position.3"})</code></p>
<ul>
<li>Click on “List” in “Markups” row</li>
<li>Click on “Record”</li>
<li>Click on “List” in “controlPoints” row</li>
<li>Click “To Table”, click OK</li>
<li>Click on the field selector and choose the fields you want in the table, for example “label”, “position” and “positionStatus”</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf601991c793c0a2b166e3ba1f4304011cad8360.png" data-download-href="/uploads/short-url/tAwJdV35WLWF4RxOMutGpqgP6EM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf601991c793c0a2b166e3ba1f4304011cad8360.png" alt="image" data-base62-sha1="tAwJdV35WLWF4RxOMutGpqgP6EM" width="578" height="500" data-dominant-color="EDF1EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">812×702 26.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Split position column by clicking on the field selector and then choosing “Extract values…”</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d392aac0df53e280d3bce42bbb2f408cca652476.png" alt="image" data-base62-sha1="ubEYGNh2p8NZkNqYgSNOPKuVmgC" width="329" height="204"></p>
<ul>
<li>Choose semicolon as delimiter and click OK</li>
<li>Click “Split column”  / “By delimiter”, make sure semicolon is used as delimiter and then click OK</li>
<li>Click Close&amp;Load</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fbcb1d0bbfbfd5e733a63e557169f0adde67f3b.png" data-download-href="/uploads/short-url/2fdrb22PHZTwnHWIbQtxFdk92xt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fbcb1d0bbfbfd5e733a63e557169f0adde67f3b.png" alt="image" data-base62-sha1="2fdrb22PHZTwnHWIbQtxFdk92xt" width="690" height="430" data-dominant-color="D4DCD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1153×720 62.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You only need to do this once, from this point the markups json file acts as a database (you can update table content from the json file with a single click or enable auto-refresh, etc.), you can change the input json file, etc.</p>

---

## Post #14 by @rsookias (2022-03-15 13:41 UTC)

<p>I don’t get an “Export as” option in the menu, just export to DICOM. Am I missing a module or something? I’m new to Slicer FYI (sorry!).</p>

---

## Post #15 by @ebrahim (2022-03-15 13:48 UTC)

<p>In the latest Slicer preview version there should be “Export to file…”</p>

---

## Post #16 by @rsookias (2022-03-15 13:52 UTC)

<p>Hm, well I just downloaded Slicer today, so should be the latest (4.11.20210226)</p>

---

## Post #17 by @jamesobutler (2022-03-15 14:37 UTC)

<p><a class="mention" href="/u/rsookias">@rsookias</a> See the following post below.</p><aside class="quote quote-modified" data-post="2" data-topic="22157">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/issue-saving-fiducials/22157/2">Issue saving fiducials</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Export as…” was previously available as part of the SlicerMorph extension. It was recently <a href="https://github.com/SlicerMorph/SlicerMorph/commit/56ca0f827c3999dc547f726d46db3fff506602a1" rel="noopener nofollow ugc">removed</a> from SlicerMorph because the feature is now available in the latest Slicer Preview. Since SlicerMorph specifies to the use latest version of its extension in both Slicer stable (4.11.20210226) and latest Slicer Preview that means “Export As…” is no longer available from SlicerMorph when using Slicer stable. You will need to switch to using latest Slicer Preview available from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slic…</a>
  </blockquote>
</aside>


---

## Post #18 by @rsookias (2022-03-15 14:54 UTC)

<p>Great! That solved it. And is there any way to bulk export fiducials? E.g. I have 20 landmarks…</p>

---

## Post #19 by @muratmaga (2022-03-15 15:36 UTC)

<aside class="quote no-group" data-username="rsookias" data-post="18" data-topic="16278">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/9f8e36/48.png" class="avatar"> rsookias:</div>
<blockquote>
<p>bulk export fiducials? E.g. I have 20 landmarks</p>
</blockquote>
</aside>
<p>You mean you’ve 20 fiducial objects you would like to convert to a format (e.g., from fcsv to json or vice versa). Load all of them into SLicer, and use the Save (Ctrl + S) command.</p>

---

## Post #20 by @rsookias (2022-03-15 15:43 UTC)

<p>Ah, yes, good idea. Thanks!</p>

---

## Post #21 by @ebrahim (2022-03-15 15:59 UTC)

<p>Also if you put them under one folder in the Slicer data browser then you can export that folder using “Export to file…”</p>

---
