# Importing Landmarks from excel file into 3D Slicer

**Topic ID**: 17910
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/importing-landmarks-from-excel-file-into-3d-slicer/17910

---

## Post #1 by @HodaGH (2021-06-01 20:09 UTC)

<p>Hello,</p>
<p>I have an excel sheet with landmarks specified I believe in itk-snap . As suggested here: <a href="https://discourse.slicer.org/t/export-formats-for-markups/16278/6" class="inline-onebox">Export formats for markups - #6 by muratmaga</a><br>
I saved as .csv file (excel doesn’t have .fcsv) and added the suggested code to the beginning of the file but only a table with ID’s get exported. I don’t know how to change the code to read my headers.<br>
the file can be found here <a href="https://drive.google.com/file/d/1ERvpmIvjQEQuFQe18L-37ymFTrK6qUVK/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1ERvpmIvjQEQuFQe18L-37ymFTrK6qUVK/view?usp=sharing</a></p>
<p>Thanks for any hint.</p>

---

## Post #2 by @muratmaga (2021-06-02 05:44 UTC)

<p>In that thread, original poster has the data in the correct format with all the field, and while saving as csv, they accidentally removed the special fcsv header. So pasting it, fixed the problem.</p>
<p>That won’t work for you, as you will need to rearrange your data. Currently you have each sample in a row. You will have to convert data such that each specimen is a single fcsv, where the each row is a single landmark. This is best done programmatically.</p>
<p>If you an R user, you can do devtools::install_packages(‘SlicerMorph/SlicerMorphR’) and then use the write.markups.fcsv() function to write fcsv files (after you rearrange the data in the way described above).</p>

---

## Post #3 by @HodaGH (2021-06-03 07:09 UTC)

<p>Thanks a lot for your reply. Sorry I’m not familiar ,where should I use this devtools::install_packages(‘SlicerMorph/SlicerMorphR’)</p>

---

## Post #4 by @muratmaga (2021-06-03 08:29 UTC)

<p>That’s an R package. If you are not familiar with R, you can disregard.</p>
<p>You can reorganize the data manually as well.</p>

---

## Post #5 by @HodaGH (2021-06-03 13:30 UTC)

<p>I reorganized the data with excel formulas and tried to import the csv file. Slicer import it as a table and reads the data but in the fiducial registration wizard doesn’t recognize the fiducial file.</p>

---

## Post #6 by @muratmaga (2021-06-03 13:42 UTC)

<p>There are some differences between fcsv and csv file. For example, this is what fcsv file looks like containing a single LM (F-1) located at coordinates 1, 2, 3</p>
<pre><code class="lang-auto"># Markups fiducial file version = 4.11
# CoordinateSystem = LPS
# columns = id,x,y,z,ow,ox,oy,oz,vis,sel,lock,label,desc,associatedNodeID
1,1,2,3,0,0,0,1,1,1,0,F-1,,
</code></pre>
<p>You have to edit your csv file using this format, then rename them as fcsv and you should be able to read it into Slicer as markups (as oppose to take) correctly.</p>

---

## Post #7 by @lassoan (2021-06-05 17:22 UTC)

<p>As a quick experiment, I’ve <a href="https://github.com/Slicer/Slicer/pull/5677">implemented table export/import feature in Markups module</a>. This allows conversion between CSV files and markups control points.</p>
<p>                    <a href="https://user-images.githubusercontent.com/307929/120899625-b2610580-c5fe-11eb-8ef3-bd0eb533a0e1.png" target="_blank" rel="noopener" class="onebox">
            <img src="https://user-images.githubusercontent.com/307929/120899625-b2610580-c5fe-11eb-8ef3-bd0eb533a0e1.png" width="690" height="417">
          </a>

</p>
<p>There could be many things to improve related to this, such as:</p>
<ul>
<li>import/export from/to clipboard</li>
<li>flexible column mapping</li>
<li>option to clear out the target node before adding the new points (currently points are always appended)</li>
<li>export/import all control point measurements - curvature, etc.</li>
<li>add a mode to import/export measurements instead of control points</li>
<li>save markups name and type to the table so that many markups can be stored in a single table</li>
<li>allow loading csv file directly as markups</li>
</ul>
<p>Implementing all these would be a lot of work, but I may be able find time to implement a few of those, so it would be useful to get feedback on which features are wanted the most.</p>

---

## Post #8 by @lassoan (2021-06-06 18:54 UTC)

<p>FYI, the table export/import is available in today’s Slicer Preview Release. Any feedback is welcome.</p>

---

## Post #9 by @muratmaga (2021-06-07 15:35 UTC)

<p>I just tried and got this error message:</p>
<pre><code class="lang-auto">"Table" Reader has successfully read the file "C:/Users/murat/Desktop/test_table.csv" "[0.01s]"
setViewLabel should be called before setViewNode !
setViewLabel should be called before setViewNode !
setViewLabel should be called before setViewNode !
setViewLabel should be called before setViewNode !
Switch to module: "Markups"
Generic Warning: In D:\D\P\Slicer-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.cxx, line 1748
vtkSlicerMarkupsLogic::ImportControlPointsFromTable failed: Invalid markupsNode or tableNode.
</code></pre>
<p>Markups node is populated, but they are 0,0,0</p>
<p>here are the contents of the csv file:</p>
<p>|M1|-9.150921822|-22.86759949|7.407970428|<br>
|M2|-9.103624344|-25.06776237|10.3398838|<br>
|M3|-7.095143318|-18.17201233|11.3801918|<br>
|M4|-9.170223236|-17.20416832|11.93351269|<br>
|M5|-9.065729141|-17.70404434|11.78754807|<br>
|M6|-9.344167709|-16.48130608|7.361549377|<br>
|M7|-11.22470284|-18.25616074|11.31808662|<br>
|M8|-3.935972214|-15.5256691|8.035143852|<br>
|M9|-14.49450397|-15.58605385|7.946472645|<br>
|M10|-3.270830631|-12.43230247|6.841721535|<br>
|M11|-6.151437759|-12.95347023|11.44103241|<br>
|M12|-12.09773731|-12.9262743|11.54073048|<br>
|M13|-15.24338341|-12.45711899|6.929478645|<br>
|M14|-8.975575447|-9.588539124|11.80789948|<br>
|M15|-9.160082817|-5.779891491|10.60149002|<br>
|M16|-9.007077217|-2.824546337|8.692295074|<br>
|M17|-6.019548416|-17.7469883|10.51934433|<br>
|M18|-6.579883575|-19.12015343|7.670481682|<br>
|M19|-6.695315361|-13.83416176|11.27579689|<br>
|M20|-6.948893547|-12.08451462|5.264913559|<br>
|M21|-3.752249718|-8.844957352|7.841619968|<br>
|M22|-5.002905846|-5.621376514|8.7119627|<br>
|M23|-11.12182045|-20.84689522|9.683402061|<br>
|M24|-12.28719139|-17.59350777|10.56907272|<br>
|M25|-11.69880581|-13.72665119|11.33343792|<br>
|M26|-12.64149475|-12.85103416|8.05005455|<br>
|M27|-14.40844536|-8.798666|7.85973835|<br>
|M28|-13.38345718|-5.59616518|8.764681816|<br>
|M29|-8.828820229|-22.00113678|7.368155479|<br>
|M30|-12.3915844|-18.19547272|9.618013382|<br>
|M31|-7.220074654|-17.74337578|7.051663876|<br>
|M32|-10.33326912|-20.38110733|7.131398201|<br>
|M33|-9.389846802|-22.01970482|7.390283585|<br>
|M34|-11.49119377|-19.4066124|7.344583511|<br>
|M35|-7.708600044|-20.17664719|7.100816727|<br>
|M36|-8.358551025|-20.27204132|7.255236626|<br>
|M37|-7.177659035|-20.56736755|9.717757225|<br>
|M38|-9.757544518|-16.44082642|6.664048672|<br>
|M39|-6.000197411|-18.1774292|9.445129395|<br>
|M40|-11.01899815|-17.78924561|6.879428387|<br>
|M41|-8.738926888|-16.73945427|6.708190918|<br>
|M42|-9.848192215|-15.44428253|6.469041348|<br>
|M43|-7.845579147|-14.36761284|5.635435581|<br>
|M44|-8.55123806|-15.80703354|6.548315525|<br>
|M45|-14.98413658|-13.41439247|6.521261215|<br>
|M46|-9.265712738|-13.31762218|5.219259262|<br>
|M47|-10.74543667|-13.94102669|5.519832611|<br>
|M48|-7.185830116|-13.74380779|5.619788647|<br>
|M49|-3.381908178|-13.40026093|6.416231632|<br>
|M50|-14.70256138|-11.20371246|7.282434464|<br>
|M51|-11.40052605|-11.96435547|5.255110264|<br>
|M52|-9.004154205|-15.01675415|6.191643715|<br>
|M53|-3.735332012|-11.28477383|7.158238888|<br>
|M54|-8.945774078|-8.538723946|4.375735283|<br>
|M55|-9.213869095|-5.81755352|3.644111633|</p>

---

## Post #10 by @lassoan (2021-06-07 18:15 UTC)

<p>This is not a csv (comma-separated value) file. In a csv file, values are separated by commas. Header row is missing, so there is no way of knowing what field corresponds to what.</p>
<p>Expected column names are display as tooltip of the import option, but probably the simplest is to export a markup to a table and save it to file and then have a look at the file.</p>
<p>Minimal .csv file example:</p>
<pre><code class="lang-nohighlight">label,r,a,s
F-1,79.3014,17.4631,-10.2143
F-2,-32.809,-33.7369,-10.2143
F-3,-0.146917,6.9286,18.8581
</code></pre>
<p>Example .csv file with all supported fields:</p>
<pre><code class="lang-nohighlight">label,r,a,s,defined,selected,visible,locked,description
F-1,79.3014,17.4631,-10.2143,1,1,1,0,
F-2,-32.809,-33.7369,-10.2143,1,1,1,0,
F-3,-0.146917,6.9286,18.8581,1,1,1,0,
</code></pre>

---
