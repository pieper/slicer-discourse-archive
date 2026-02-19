---
topic_id: 34984
title: "Adding Color Property To Fcsv Files Created In Matlab"
date: 2024-03-19
url: https://discourse.slicer.org/t/34984
---

# Adding color property to fcsv files created in matlab

**Topic ID**: 34984
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/adding-color-property-to-fcsv-files-created-in-matlab/34984

---

## Post #1 by @FatihSogukpinar (2024-03-19 19:50 UTC)

<p>Hi all,</p>
<p>In Matlab, I have a function to create .fcsv files to visualize my recording sites in Slicer. Now, I want to be able to add color property to the each recording site.<br>
I cannot do this manually using Markups module, since I have 100’s of recording sites, and also I want to be able to use continuous color coding.</p>
<p>How can achieve this ? I can also create another that stores color information; I don’t have to store it in the fcsv file. I can also use Python if that is what is needed.</p>
<p>Thanks a lot !</p>
<p>fid = fopen([name2save ‘.fcsv’],‘w’);<br>
%fprintf(fid,‘# Markups fiducial file version = 4.10 \n’);<br>
fprintf(fid,‘# Markups fiducial file version = 4.11 \n’);<br>
fprintf(fid,‘# CoordinateSystem = RAS \n’);<br>
fprintf(fid,‘# columns = id,x,y,z,ow,ox,oy,oz,Vis,Sel,Lock,Name,Description \n’);<br>
%               id  x  y  z owoxoyozV S L N    Desc<br>
fprintf(fid,‘id_%i,%f,%f,%f,0,0,0,1,1,0,1,%i,electrode%i \r\n’,pp’);<br>
fid=fclose(fid);</p>

---

## Post #2 by @muratmaga (2024-03-19 19:54 UTC)

<p>You should use JSON format for markups if you want the individual files to retain the color property.</p>

---

## Post #3 by @FatihSogukpinar (2024-03-19 20:05 UTC)

<p>I see, if my understanding is right, this the related documentation ?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups</a></p>
<p>Thanks a lot ! (Tesekkurler <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>

---

## Post #4 by @muratmaga (2024-03-19 20:38 UTC)

<p>You can find the full schema here; <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json" class="inline-onebox">Slicer/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.3.json at main · Slicer/Slicer · GitHub</a></p>
<p>display color is the property you will need to set.</p>

---
