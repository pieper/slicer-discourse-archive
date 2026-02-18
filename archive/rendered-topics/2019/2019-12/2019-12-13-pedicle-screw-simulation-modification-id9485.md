# Pedicle Screw Simulation Modification

**Topic ID**: 9485
**Date**: 2019-12-13
**URL**: https://discourse.slicer.org/t/pedicle-screw-simulation-modification/9485

---

## Post #1 by @manjula (2019-12-13 12:34 UTC)

<p>I came across the Pedicle Screw simulator when i was trying to figure out the segment interaction with mouse pointer.<br>
Developers of this module have done something great both clinicians and researchers both will benefit from and can be evolved in to other specialties. I change the script a bit and replaced the screw vtk files with dental implants i wanted and the results are amazing and applications are many. ( don’t judge the implant placement by the photo, it was just for demonstration… <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> )</p>
<p>I am wondering is it legal or ethical to take this module and develop it as a a  separate  module  for</p>
<ol>
<li>surgical planning of dental implants</li>
<li>Maxillofacial bone Reconstruction</li>
</ol>
<p>because i think 90 % of the code is simply applicable to any place… just a little bit of editing is needed to make it applicable to the above scenarios.  So our contribution for the code will be very limited apart from the data base of implant models. So is it something that i can try to do or do i need to contact the original developers for this ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e05177704a06c4abb7721ce635d98ec5fe26084.jpeg" data-download-href="/uploads/short-url/mxUlEb2bkV4GQu2HgnY2MKJKo6g.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e05177704a06c4abb7721ce635d98ec5fe26084_2_685x500.jpeg" alt="Screenshot_1" data-base62-sha1="mxUlEb2bkV4GQu2HgnY2MKJKo6g" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e05177704a06c4abb7721ce635d98ec5fe26084_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e05177704a06c4abb7721ce635d98ec5fe26084_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e05177704a06c4abb7721ce635d98ec5fe26084_2_1370x1000.jpeg 2x" data-dominant-color="686775"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1390×1014 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @aiden.zhu (2019-12-13 16:36 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/license.html" class="onebox" target="_blank" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/license.html</a></p>

---

## Post #3 by @pieper (2019-12-13 18:17 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> - I agree, this is a very cool module and has a lot of potential applications.</p>
<p><a class="mention" href="/u/aiden.zhu">@aiden.zhu</a> you are right about the Slicer license being free to use an bulid on without restrictions.  However the PedicleScrewSimulator repository doesn’t include a software license file so it would be good to have an explicit statement from the developers.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/ungi">@ungi</a> - you have both contributed to the code - do you know if it’s intended to be under the Slicer license?  If so can we add it explicitly?</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/smclach/PedicleScrewSimulator" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/4388491?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/smclach/PedicleScrewSimulator" target="_blank">smclach/PedicleScrewSimulator</a></h3>

<p>3D Slicer module for pedicle screw insertion training - smclach/PedicleScrewSimulator</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @manjula (2019-12-13 19:30 UTC)

<p>I was wondering that even though 3D Slicer is open source does all the module by default become  under BSD licences ? and also about the copyleft properties of such modules ?</p>
<p>My confusion came from even though i did not read the 3D Slicer licencing is that far as i understand is BDS style is non - copy left unlike GPL. So Can 3D Slicer claim a module built on that if the authors of that module does not explicitly state it ? becuse far as i understand from BDS style is that we can completely ignore the  original 3D Slicer developers if we choose to do so.</p>

---

## Post #5 by @ungi (2019-12-13 19:31 UTC)

<p>Some people from the original team (Sunnybrook Research Institute in Toronto) are still working on this project, but apparently not in this repository. I stayed in touch with them, but not contributed code directly. I will ask them what is going on now. I’m quite sure the code was free to use for every purpose when I talked to them.<br>
The current Slicer modules allow very rapid development of such applications. Often just saving a Slicer scene is enough, no need for coding. If we identify functions that are commonly used between such modules, we could put them in e.g. the SlicerIGT extension. I’m open to participating in a discussion about that.</p>

---

## Post #6 by @pieper (2019-12-13 20:33 UTC)

<p>Good questions <a class="mention" href="/u/manjula">@manjula</a> - We do carefully avoid GPL code in software that we distribute for <a href="https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883/15">reasons discussed here</a>.</p>
<p>Since this pedicle screw simulation code isn’t a Slicer Extension the issue hadn’t come up yet and this repository didn’t explicitly state.  It’s okay for people to write Slicer code and offer<br>
it under any license they choose, but we can’t redistribute it under the terms of GPL without triggering the copyleft for everyone.</p>
<p>Since this repository is not under our control we really can’t assume anything about the license terms and are best off getting an explicit statement from the authors.</p>

---

## Post #7 by @lassoan (2019-12-14 02:32 UTC)

<p>I’ve worked on this module quite a bit. I’m sure all the authors will be comfortable with adding a BSD license to the repository (that will explicitly give permission to reuse and modification). I’ll send a pull request with the proposed change.</p>
<p>I haven’t realized how general this module actually is. It would be nice if you would not clone it but just enhance the module to make it serve your needs. This way we would significantly reduce bugfix and maintenance workload.</p>

---

## Post #8 by @manjula (2019-12-14 09:01 UTC)

<p>Thank you Prof <a class="mention" href="/u/lassoan">@lassoan</a> . I will try to work on this module to suite our purposes,our goal is to make it as a simulator  and research tool for,</p>
<ol>
<li>Dental Implants</li>
<li>Maxillofacial reconstruction - Fractures, Orthognathic surgery etc…</li>
</ol>
<p>because this module already have essential elements for them.</p>
<p>The major conflict or interest would come if we are to include a dental implant bank to the module as even though we already work with quite a number of dental implant manufacturers and designs on many research projects all   implants designs in stl format is been handed over to us with non disclosure agreements.  Our plan of work around is to include a feature to upload the implant/s your self  so it is the clinician/researcher is under the contractual obligations not the developers. And they can use it for surgical planning or research and the original design will not be made public unless they want them to.  This is our basic concept for now.</p>

---

## Post #9 by @pieper (2019-12-14 14:18 UTC)

<aside class="quote no-group" data-username="manjula" data-post="8" data-topic="9485">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>Our plan of work around is to include a feature to upload the implant/s your self so it is the clinician/researcher is under the contractual obligations not the developers.</p>
</blockquote>
</aside>
<p>That makes perfect sense to me.  Let’s see if we can make this tool work really well for your needs.</p>

---

## Post #10 by @lassoan (2019-12-16 00:54 UTC)

<p>I’ve added a license file to my PedicleScrewSimulator repository (<a href="https://github.com/lassoan/PedicleScrewSimulator">https://github.com/lassoan/PedicleScrewSimulator</a>), which I have been developing and maintaining in the last 5 years and is distributed in Slicer’s extension manager. The MIT license states that any usage and modifications are permitted.</p>
<p>Adding an option to import and use additional screw model files sounds like a good idea. You may also draw some simple generic dental screws and bundle those models with the extension. If you have any suggestion to improve the module or make it more generic then please send <a href="https://github.com/lassoan/PedicleScrewSimulator/pulls">pull requests</a>.</p>

---

## Post #11 by @manjula (2019-12-16 07:11 UTC)

<p>dear prof <a class="mention" href="/u/lassoan">@lassoan</a>. that is indeed good news.  myself and few of my colleagues will start working on this. we will keep the and the rest updated on this.</p>

---

## Post #12 by @manjula (2019-12-17 11:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
This is regarding file format for the models. (Implants)</p>
<p>I am designing some  generic dental implants for the module. I use FreeCAD and Blender for this.</p>
<p>What should be the file format ? vtk or stl etc… ? is there a significant advantage of keeping the models in vtk format as in the case for now ?</p>
<p>We want to enable the user to import the dental implant they want to use for the case and i think most of the files are in stl format so we will have to work with stl.</p>
<p>In the case vtk has great advantage over stl should we implement to convert stl --&gt; vtk ? will it give more problems ?</p>

---

## Post #13 by @lassoan (2019-12-17 13:37 UTC)

<p>Slicer can read/write STL, VTK, VTP,  PLY, and OBJ, so there is no need to restrict to only a single file type.</p>
<p>STL cannot store surface normals or colors, so if you design your own models then it is better to save them in VTK, VTP, PLY, or maybe OBJ.</p>

---

## Post #14 by @manjula (2019-12-17 14:21 UTC)

<p>Thank you for the reply. I try VTK and definitely PLY and OBJ works well for me.</p>
<p>What i meant to ask was if we allow the users to import their own implants in stl format will it affect the calculations ? (the grading step ? the percentage of cortical bone contact etc… since the implant is in stl format ? hence the question about the need to convert stl --&gt; vtk)  If stl models will work the way vtk inside this module during the grading step my question is not relevant.</p>

---

## Post #15 by @lassoan (2019-12-18 19:41 UTC)

<p>Geometry (point locations and cells) is stored with the same accuracy in all these formats, so quantitative results are not impacted by the choice of file format.</p>

---

## Post #16 by @Basil_Berinyuy (2024-12-09 14:46 UTC)

<p>Hello, I am currently using the Pediclescrewsimulator extension to insert screws into the spine with a particular length and trajectory. When I load the CT scan with the pediclescrewsimulator module, the space origin (coordinates) immidiately changes. This is a big problem because when I try to match this with the annotated data of the spine (Same CT) they have completely different space origins. Does anyone maybe know how to use the pediclescrewsimulator but without changing the original space origin coordinates of the CT?</p>
<p>Thanks a lot for your response.</p>

---
