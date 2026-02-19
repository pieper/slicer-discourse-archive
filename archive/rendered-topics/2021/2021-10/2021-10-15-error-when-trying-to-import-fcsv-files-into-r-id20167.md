---
topic_id: 20167
title: "Error When Trying To Import Fcsv Files Into R"
date: 2021-10-15
url: https://discourse.slicer.org/t/20167
---

# Error when trying to import .fcsv files into R

**Topic ID**: 20167
**Date**: 2021-10-15
**URL**: https://discourse.slicer.org/t/error-when-trying-to-import-fcsv-files-into-r/20167

---

## Post #1 by @KassandraFord (2021-10-15 09:04 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.13.0 2021-09-28</p>
<p>Expected behavior: Normal import of landmark files from 3D Slicer into R.</p>
<p>Actual behavior: I have exported .fscv files many times previously, but with my most recent update of Slicer, I have noticed a difference in the exported file. There is now an extra “,2,0” at the end of each of my lines (see below).</p>
<p>When I try to import these files into R using the SlicerMorphR function, this is what happens:</p>
<blockquote>
<p>read.markups.fcsv(‘C:/Users/ieeusr/Dropbox/2021 Bern Postdoc/Ford Cichlid CT Projects/October CT Scan work/LM10/FCSV/10618LM10.fcsv’)<br>
Error in read.table(file = file, header = header, sep = sep, quote = quote,  :<br>
more columns than column names</p>
</blockquote>
<p>If I manually go through and remove the “,2,0” then the code works. Is this a glitch on my end? Why would there be extra columns in the fcsv files that never used to be there? Any help would be appreciated. I would prefer not to have to manually make this change for each landmarked specimen. I looked at other topics and couldn’t find this exact issue.</p>
<p>Example of an .fcsv file:</p>
<h1><a name="p-68092-markups-fiducial-file-version-413-1" class="anchor" href="#p-68092-markups-fiducial-file-version-413-1" aria-label="Heading link"></a>Markups fiducial file version = 4.13</h1>
<h1><a name="p-68092-coordinatesystem-lps-2" class="anchor" href="#p-68092-coordinatesystem-lps-2" aria-label="Heading link"></a>CoordinateSystem = LPS</h1>
<h1><a name="p-68092-columns-idxyzowoxoyozvissellocklabeldescassociatednodeid-3" class="anchor" href="#p-68092-columns-idxyzowoxoyozvissellocklabeldescassociatednodeid-3" aria-label="Heading link"></a>columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID</h1>
<p>1,29.65279769897461,13.65184211730957,3.372030019760132,0,0,0,1,1,1,0,F-1,2,0<br>
2,34.794578552246094,12.737242698669434,13.382527351379395,0,0,0,1,1,1,0,F-2,2,0<br>
3,22.55841636657715,15.646979331970215,9.831713676452637,0,0,0,1,1,1,0,F-3,2,0<br>
4,31.035322189331055,15.069230079650879,6.504773139953613,0,0,0,1,1,1,0,F-4,2,0<br>
5,21.087736129760742,15.504058837890625,10.906620979309082,0,0,0,1,1,1,0,F-5,2,0<br>
6,26.08745765686035,13.417610168457031,1.3079973459243774,0,0,0,1,1,1,0,F-6,2,0<br>
7,24.097469329833984,14.466565132141113,12.538121223449707,0,0,0,1,1,1,0,F-7,2,0<br>
8,22.628808975219727,15.07335090637207,6.525925159454346,0,0,0,1,1,1,0,F-8,2,0<br>
9,23.887413024902344,15.117673873901367,13.572751998901367,0,0,0,1,1,1,0,F-9,2,0<br>
10,18.867982864379883,15.637434959411621,12.724960327148438,0,0,0,1,1,1,0,F-10,2,0<br>
11,15.60151481628418,12.834794998168945,12.662357330322266,0,0,0,1,1,1,0,F-11,2,0<br>
12,28.533113479614258,16.992637634277344,9.358516693115234,0,0,0,1,1,1,0,F-12,2,0<br>
13,26.06395721435547,17.159423828125,20.18193244934082,0,0,0,1,1,1,0,F-13,2,0<br>
14,26.498821258544922,11.234350204467773,25.304378509521484,0,0,0,1,1,1,0,F-14,2,0<br>
15,30.305736541748047,17.156003952026367,14.74747085571289,0,0,0,1,1,1,0,F-15,2,0<br>
16,33.4499397277832,12.253012657165527,14.878305435180664,0,0,0,1,1,1,0,F-16,2,0<br>
17,37.67984390258789,11.818439483642578,19.22917366027832,0,0,0,1,1,1,0,F-17,2,0<br>
18,43.603546142578125,10.957157135009766,32.72006607055664,0,0,0,1,1,1,0,F-18,2,0<br>
19,32.26897048950195,16.83575439453125,27.08075714111328,0,0,0,1,1,1,0,F-19,2,0<br>
20,34.74290466308594,18.95842170715332,35.62769317626953,0,0,0,1,1,1,0,F-20,2,0<br>
21,31.860864639282227,18.91301155090332,29.206375122070312,0,0,0,1,1,1,0,F-21,2,0<br>
22,30.518049240112305,18.613792419433594,29.496912002563477,0,0,0,1,1,1,0,F-22,2,0<br>
23,16.559288024902344,16.96553611755371,29.972938537597656,0,0,0,1,1,1,0,F-23,2,0<br>
24,11.709182739257812,14.750580787658691,29.30148696899414,0,0,0,1,1,1,0,F-24,2,0<br>
25,17.482887268066406,15.203636169433594,15.637514114379883,0,0,0,1,1,1,0,F-25,2,0</p>

---

## Post #2 by @muratmaga (2021-10-15 16:34 UTC)

<p>This is not a glitch on your end, it is one of the shortcomings of the fcsv format that cannot accommodate the new changes to do Markups module. You have couple options:</p>
<ol>
<li>
<p>You can start using JSON as your format to save markup files. This would be the best option going forward for you. SlicerMorphR R package has a read.markups.json that should help you read the landmark coordinates.</p>
</li>
<li>
<p>You can continue to use fcsv with a modified read function. Something like this should work:<br>
<code>lms &lt;-read.csv('path.to.fcsv', skip=3, header=FALSE)[,2:4]</code><br>
However, you may miss out all the new features we introduced like LM templates, ability to designate missing LMs, reset their coordinates etc (they might work to some extend, but I don’t think we test fcsv thoroughly anymore).</p>
</li>
<li>
<p>You can use the import/export table of the Markups module to export your coordinates as a regular csv or a tab separated table.</p>
</li>
</ol>
<p>Out of these options, I would suggest exploring whether switching to JSON has any other consequences for you (like compatibility with tother programs). If you are only working with SlicerMorph and R, I think <span class="hashtag">#1</span> is the way to go.</p>

---

## Post #3 by @hherhold (2021-10-15 16:37 UTC)

<p>This may not be helpful, but from a Python point of view (and knowing some R), switching my code from handling fcsv to json was remarkably easy. It wound up being about 10 lines shorter and easier to read and maintain. I’d highly recommend using json instead of fcsv.</p>

---

## Post #4 by @KassandraFord (2021-10-15 19:12 UTC)

<p>Thanks! I’ll work to move over to JSON instead of fscv. I appreciate the response!</p>

---
