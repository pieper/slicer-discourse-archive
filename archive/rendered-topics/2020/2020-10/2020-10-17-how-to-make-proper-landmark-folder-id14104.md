---
topic_id: 14104
title: "How To Make Proper Landmark Folder"
date: 2020-10-17
url: https://discourse.slicer.org/t/14104
---

# How to make proper landmark folder

**Topic ID**: 14104
**Date**: 2020-10-17
**URL**: https://discourse.slicer.org/t/how-to-make-proper-landmark-folder/14104

---

## Post #1 by @hajime_osaki (2020-10-17 18:33 UTC)

<p>Hello.<br>
I have put lamdmarks  in some models created by segmentation editor. I’m trying to parse them on GPA , but they aren’t recognized when I select the landmark folder I choose. I think it’s probably a storage format issue …please let me know how to do it.Any helps on this is greatly appreciated.</p>

---

## Post #2 by @muratmaga (2020-10-17 18:39 UTC)

<p>Landmark needs to be saved in fcsv format. İf you are using a recent version, the default is json. Make sure you change that to fcsv when you are saving or use export as from the data module.</p>

---

## Post #3 by @hajime_osaki (2020-10-18 02:31 UTC)

<p>Thank you for your teaching! I have changed it  to FCSV and saved it, but, the message “warning: fcsv file format only stores control point coordinates and a limited set of display properties” is displayed. And then,  when I select the landmark folder in GPA, the fcsv in the folder is not recognized …</p>

---

## Post #4 by @muratmaga (2020-10-18 03:40 UTC)

<p>You can ignore that warning message. I am not entirely sure what you mean by</p>
<aside class="quote no-group" data-username="hajime_osaki" data-post="3" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/b3f665/48.png" class="avatar"> hajime_osaki:</div>
<blockquote>
<p>when I select the landmark folder in GPA, the fcsv in the folder is not recognized</p>
</blockquote>
</aside>
<p>What is not recognized? Are you getting an error message (Ctrl + 0). You need to have multiple fcsv files (belonging to multiple specimens) in that folder for GPA to work. You may want to review the instructions <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_3/GPA/GPA.md#mouse-dataset">for GPA here</a></p>

---

## Post #5 by @hajime_osaki (2020-10-21 09:52 UTC)

<p>Thanks a lot. I don’t know how I can say…,<br>
this is Python Interactor’s message when I try to execute GPA<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffbed022314dc603d3f0fd93d57b223ead8b4dfb.jpeg" data-download-href="/uploads/short-url/AuqzkZKBCEXcPEHZyjOnx6LirxN.jpeg?dl=1" title="キャプチャ" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffbed022314dc603d3f0fd93d57b223ead8b4dfb_2_690x104.jpeg" alt="キャプチャ" data-base62-sha1="AuqzkZKBCEXcPEHZyjOnx6LirxN" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffbed022314dc603d3f0fd93d57b223ead8b4dfb_2_690x104.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffbed022314dc603d3f0fd93d57b223ead8b4dfb_2_1035x156.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffbed022314dc603d3f0fd93d57b223ead8b4dfb.jpeg 2x" data-dominant-color="F6EBEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">キャプチャ</span><span class="informations">1067×161 53.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @muratmaga (2020-10-21 15:04 UTC)

<p>Again this is only part of the log. In this window, if you click CTRL+A it will select all the text, and then you can do CTRL+C and CTRL+V to copy and paste. By the way, are you using non-English characters in your filename?</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> can this be a non-ascii filename issue?</p>

---

## Post #7 by @lassoan (2020-10-21 20:42 UTC)

<p>What do you see in the first few lines of the application log (menu: Help / Report a bug)? In particular, what is the content of the line starting with “Operating system”?</p>
<p>This is important because you need to use a recent Windows10 version if you want to use unicode strings in text files or you want to use directory and file names that contain non-ASCII characters. If you cannot update to latest Windows10 then move your data into files and folders that do not have any special characters in their name.</p>

---

## Post #8 by @smrolfe (2020-10-22 18:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> can this be a non-ascii filename issue?</p>
</blockquote>
</aside>
<p>I think it may be due to a non-ascii character in the fcsv file. <a class="mention" href="/u/hajime_osaki">@hajime_osaki</a> if you can share a sample landmark file in addition to the error log that would be helpful.</p>

---

## Post #9 by @lassoan (2020-10-23 02:15 UTC)

<p><a class="mention" href="/u/smrolfe">@smrolfe</a> you are right, the error occurs in <code>for row in datafile</code>, which means that the file contains string that does not use UTF-8 encoding (e.g., may use some Japanese code page) or the application does not support UTF-8 code page because the application is not recent enough.</p>
<p>This is yet another example of why we need to get rid of this old .fcsv format. This error could not have happened with the new .json file format:</p>
<ol>
<li>
<p>Text encoding is specified in json standard (<a href="https://tools.ietf.org/html/rfc8259">it is required to be UTF-8</a>), therefore it is always known how to decode the file content.</p>
</li>
<li>
<p>The 10-line handcrafted Python code that parses the csv file is relatively complex and very fragile. In contrast, parsing the json file is a single command and you can get any content from the file incredibly easily.</p>
</li>
</ol>
<p>Read and parse markup json file:</p>
<pre><code class="lang-python">import json
with open('path/to/my.mrk.json') as f:
    json_data=json.loads(f.read())
</code></pre>
<ol start="3">
<li>The parser contains the comment <em>“Imports the landmarks from a .fcsv file. Does not import sample if a  landmark is -1000”</em>. I think it is obvious that just bad this is. We should do better. And fortunately, we can: markup json file includes <code>positionStatus</code> property for each control point, which is accessible simpy as <code>controlPoint["positionStatus"]</code>.</li>
</ol>
<p>Print position and status of each control point:</p>
<pre><code class="lang-python">for controlPoint in json_data["markups"][0]["controlPoints"]:
  print("position: {0}, defined: {1}".format(controlPoint["position"], controlPoint["positionStatus"] == "defined"))
</code></pre>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/smrolfe">@smrolfe</a> Please move away from fragile and inflexible legacy formats, especially because we now support modern and sustainable file format.</p>

---

## Post #10 by @muratmaga (2020-10-23 03:43 UTC)

<p>We will move to json, but not immediately.</p>
<p>For one, we (as in my lab) have thousands of datasets that already collected, and archived and converting them takes time. I remember when Slicer 4 released in 2012 and made the decision that each fiducial file is going to be saved as a single acsv file, it took years to stabilize around fcsv, and we had to do the similar conversion.</p>
<p>As for designating -1000 as a missing landmark, that’s a legacy of Slicer not being able to generate a blank fiducial. That has been a request of mine way before we started the SlicerMorph project, we still can’t do it. Since we have to maintain landmark order and numbers across dataset, we had to invent a way to encode this, and we have to make that known. Switching to JSON will not fix this problem.</p>
<p>Landmarks are a very important part of morphometric analysis. FCSV is not perfect, but it is easy and labs (not just mine) that use Slicer for data collection has been using it for a while, and forcing them to use JSON will make their historical data being inaccessible to GPA module.</p>

---

## Post #11 by @lassoan (2020-10-23 04:19 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I remember when Slicer 4 released in 2012 and made the decision that each fiducial file is going to be saved as a single acsv file, it took years to stabilize around fcsv, and we had to do the similar conversion.</p>
</blockquote>
</aside>
<p>Many decisions in Slicer development turn out well, while some others don’t. We are not always smart enough and/or not always lucky - it is hard to predict what technologies become mainstream in 5-10 years.</p>
<p>We aim to preserve Slicer’s backward compatibility with hardware, software, and data formats for at least 5 years (so you don’t have to upgrade, if you don’t want to), which is consistent with industry standard for long-term support timeline (typically 3-5 years).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>That has been a request of mine way before we started the SlicerMorph project, we still can’t do it.</p>
</blockquote>
</aside>
<p>We have implemented all the infrastructure for this, and the only thing missing is exposing it on the GUI - about a few days of work. I thought your team was working on it and assumed that it was delayed because it was not that important. If you need help with this then let me know.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>FCSV is not perfect, but it is easy and labs (not just mine) that use Slicer for data collection has been using it for a while, and forcing them to use JSON will make their historical data being inaccessible to GPA module.</p>
</blockquote>
</aside>
<p>If we could demonstrate clear advantages of using a richer and more standard file format then I think users would transition voluntarily. Probably some more features (landmark placement templates with undefined point positions, etc.), better documentation, training, and examples (e.g., to show how easy it is to create data tables from json files) would help.</p>
<p>What is important is to provide as good support for json as for fcsv, in all modules. There should not be modules that can only accept fcsv format and not json.</p>
<p>I would also add standard csv export (single-line header, columns in first row) option for better compatibility with table-based analysis. This should also help in reducing usage of the proprietary fcsv format.</p>

---

## Post #12 by @muratmaga (2020-10-23 04:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Many decisions in Slicer development turn out well, while some others don’t. We are not always smart enough and/or not always lucky - it is hard to predict what technologies become mainstream in 5-10 years.</p>
</blockquote>
</aside>
<p>I am not saying json would be a poor decision. I think its benefits, particularly for measurement type markups will overweight its complications in the long run. It will happen, but will take time as there will<br>
be inertia among groups, due to similar concerns to mine. When the switch to json first tabled on discourse earlier this year, I did probe the morphometrics community through the listserv, and there was a push back from other groups that use Slicer for types of research similar to ours. That’s mostly due to lack familiarity with the format, and JSON being quite verbose.  Saving 3 control points in fcsv is 6 lines, same thing in json is 74. People who are used to looking flat files for a long time, that nested structure do appear confusing at first, and it seem like unnecessarily complex format to extract 9 coordinates.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>which is consistent with industry standard for long-term support timeline (typically 3-5 years).</p>
</blockquote>
</aside>
<p>That is a far too short time for types of research (natural history) that our community does <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #13 by @lassoan (2020-10-23 13:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>When the switch to json first tabled on discourse earlier this year, I did probe the morphometrics community through the listserv, and there was a push back from other groups that use Slicer for types of research similar to ours.</p>
</blockquote>
</aside>
<p>I think the main issue is that it is new and people just don’t know how much simpler and more efficient it actually is to work with json files than with csv. The main idea is that you can store all data in json (any number of markups, any metadata) and generate a table view from any parts of it, using a single line of code.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Saving 3 control points in fcsv is 6 lines, same thing in json is 74.</p>
</blockquote>
</aside>
<p>Yes, json is verbose, but it is not that bad. Many of the elements are optional (see <a href="https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json">schema</a>). A minimal file consists of 1-2 lines of header, one row per fiducial, and one closing line, something like this:</p>
<pre data-code-wrap="json"><code class="lang-json">{"@schema": "https://raw.githubusercontent.com/slicer/slicer/master/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#",
"markups": [{"type": "Fiducial", "coordinateSystem": "LPS", "controlPoints": [
    { "label": "F-1", "position": [-53.388409961685827, -73.33572796934868, 0.0] },
    { "label": "F-2", "position": [49.8682950191571, -88.58955938697324, 0.0] },
    { "label": "F-3", "position": [-25.22749042145594, 59.255268199233729, 0.0] }
]}]}
</code></pre>
<p>Manual editing is not much worse either, because all modern text editors help json editing with features syntax highlighting, automatic formatting, validation, etc.</p>
<p>Running analysis on a json file should be as simple as on a csv file, because you can read it into a dataframe using a single line of code. For example, getting a table of control point labels and positions : using pandas (<code>pip_install('pandas'); import pandas as pd</code>):</p>
<pre data-code-wrap="python"><code class="lang-python">controlPointsTable = pd.DataFrame.from_dict(pd.read_json(input_json_filename)['markups'][0]['controlPoints'])
</code></pre>
<p>Result:</p>
<pre data-code-wrap="txt"><code class="lang-txt">&gt;&gt;&gt; controlPointsTable
  label                                        position
0   F-1  [-53.388409961685824, -73.33572796934868, 0.0]
1   F-2     [49.8682950191571, -88.58955938697324, 0.0]
2   F-3   [-25.22749042145594, 59.255268199233726, 0.0]
</code></pre>
<p>Splitting the position vector column and into separate xyz columns and write it to csv takes 3 lines:</p>
<pre data-code-wrap="python"><code class="lang-python">controlPointsTable[['x','y','z']] = pd.DataFrame(controlPointsTable['position'].to_list())
del controlPointsTable['position']
controlPointsTable.to_csv(output_csv_filename)
</code></pre>
<p>Resulting csv file:</p>
<pre data-code-wrap="csv"><code class="lang-csv">,label,x,y,z
0,F-1,-53.388409961685824,-73.33572796934868,0.0
1,F-2,49.8682950191571,-88.58955938697324,0.0
2,F-3,-25.22749042145594,59.255268199233726,0.0
</code></pre>

---

## Post #14 by @hherhold (2020-10-23 13:45 UTC)

<p>For what it’s worth, I had planned on taking half a day to convert my code that uses fcsv to using json. It took me about 15 minutes.</p>

---

## Post #15 by @hherhold (2020-10-23 13:47 UTC)

<p>Oh, and that includes keeping in the old code - basically I check for a json file, if it exists, I use that, otherwise it parses the old fcsv file. (This is a script that runs through a hundred scans or so to tally what fiducials/markups have been placed on what scan, and where.)</p>

---

## Post #16 by @muratmaga (2020-10-23 15:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Running analysis on a json file should be as simple as on a csv file, because you can read it into a dataframe using a single line of code. For example, getting a table of control point labels and positions : using pandas ( <code>pip_install('pandas'); import pandas as pd</code> ):</p>
</blockquote>
</aside>
<p>We maintain SlicerMorph primarily for 3D landmark digitization and for basic shape analysis and visualization. Most of our users end up using R shape analysis packages for more complex analysis they want to do. It looks like, it is going to be fairly straightforward to read coordinates directly from Json as a data matrix like we currently do with fcsv. We will show it in our next user check-in (this week). But again, it will take time.</p>
<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The main idea is that you can store all data in json (any number of markups, any metadata) and generate a table view from any parts of it, using a single line of code.</p>
</blockquote>
</aside>
<p>Does this mean, you guys are planning to switch to saving all markups generated in a scene to a single json file? Currently every node is saved as a distinct file. I would prefer keeping the current behavior.</p>
<p>Also I still do not see a <a href="https://discourse.slicer.org/t/add-unit-to-the-fcsv-header/13716/2">units tag in the json</a>.</p>

---

## Post #17 by @muratmaga (2020-10-23 15:44 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="14" data-topic="14104" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>For what it’s worth, I had planned on taking half a day to convert my code that uses fcsv to using json. It took me about 15 minutes.</p>
</blockquote>
</aside>
<p>This is not a big deal for your own data, it becomes complicated when you have collaborators because everyone has to update their workflow at the same time.</p>

---

## Post #18 by @hherhold (2020-10-23 15:54 UTC)

<p>Yeah, I’m pretty spoiled with a user base of… one. I didn’t mean to sound insensitive to issues of keeping many others happy.</p>

---

## Post #19 by @lassoan (2020-10-23 15:57 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Does this mean, you guys are planning to switch to saving all markups generated in a scene to a single json file?</p>
</blockquote>
</aside>
<p>We need to keep one-to-one mapping between MRML node and data file for scene <em>saving</em>, so we don’t plan to change the current save/load behavior. However, we can <em>export</em> an entire folder of markups into a single file, and <em>import</em> an entire group of markups from a single file (don’t try it, not implemented yet, but can be implemented anytime, with a few-hour effort).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Also I still do not see a <a href="https://discourse.slicer.org/t/add-unit-to-the-fcsv-header/13716/2">units tag in the json</a>.</p>
</blockquote>
</aside>
<p>This has not been implemented yet. I’ve added a ticket to make sure we don’t forget about it: <a href="https://github.com/Slicer/Slicer/issues/5261" class="inline-onebox">Save length unit in markups files · Issue #5261 · Slicer/Slicer · GitHub</a></p>
<p>Again, the beauty of json is that we can make such changes in a clean and backward compatible way: we add a new “length unit” property, describe its type, valid values, etc. and the default value, so that we know how to interpret all those files which were created before this field was introduced. Such mechanisms can help with keeping all older mkp.json files valid and well defined, even as the format evolves. We can of course still make bad decisions and need to live with the consequences, but at least we have a number of mechanisms to properly handle some unavoidable mistakes.</p>

---

## Post #20 by @smrolfe (2020-10-23 18:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="14104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We have implemented all the infrastructure for this, and the only thing missing is exposing it on the GUI - about a few days of work. I thought your team was working on it and assumed that it was delayed because it was not that important. If you need help with this then let me know.</p>
</blockquote>
</aside>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>.  We still plan to work on this although the project got moved back due to other deadlines.</p>

---
