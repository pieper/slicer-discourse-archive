# Matlab Bridge Extension

**Topic ID**: 314
**Date**: 2017-05-15
**URL**: https://discourse.slicer.org/t/matlab-bridge-extension/314

---

## Post #1 by @Alba_Garcia_de_la_Ca (2017-05-15 18:48 UTC)

<p>Operating system: ubuntu 16.04<br>
Slicer version: 4.6 | 4.7<br>
Expected behavior: Matlab bridge executes Matlab properly<br>
Actual behavior: There is an error calling Matlab</p>
<p>Hi everyone!</p>
<p>I am trying to call a script from Matlab through MatlabBridge extension. I generate my module with <em>matlab module generator</em> from Developer tools category. My module is perfectly created.<br>
When I restart slic3r to edit my module and execute it, it starts working and Matlab calling appears but disappears after few seconds; process is completed with errors. When I open the log, the following error appears:<br>
_Failed to connect to server 127.0.0.1:4100</p>
<p>Waiting for Matlab startup … 59sec<br>
ERROR: Cannot connect to the server</p>
<p>VolumeAdj completed with errors_</p>
<p>Do you know why this could happen, if I am doing something wrong?</p>
<p>I look forward to hearing from you. Thanks in advance.</p>
<p>Sincerely,</p>
<p>Alba.</p>

---

## Post #2 by @lassoan (2017-05-15 20:14 UTC)

<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge#Troubleshooting">troubleshooting instructions</a> on the module’s webpage. Specifically:</p>
<ul>
<li>Check if firewall settings enable Matlab to open a server port 4100</li>
<li>Run MatlabServer from the Matlab GUI as described in “<em>I would like to add breakpoints and do step-by-step debugging in Matlab</em>” and check if you receive incoming requests and if any error messages are displayed</li>
</ul>

---

## Post #3 by @Alba_Garcia_de_la_Ca (2017-05-23 18:42 UTC)

<p>Thank you!</p>
<p>I have followed the steps, but I still cannot run matlabbridge extension.<br>
I have generated a module which I called Module_ex that executes the thresholding example. I have downloaded the MRHead sample data.<br>
I have checked that my firewall is not blocking the connection with port 4100:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18fbf5f33845b5a4bccaac59237e97af7c701cf4.png" alt="image" data-base62-sha1="3z1hwFoPVYS8MmFbo2Kt8AP3eni" width="526" height="220"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/0154d8a907f9be78fd8b3fcc20da1c73a80bc057.png" width="552" height="278"></p>
<p>But I still receive the same error I showed in the first post.</p>
<p>After this, I have executed the debug mode following the troubleshooting instructions and I obtain this messages:</p>
<pre><code>&gt;&gt; cli_commandserver
Starting OpenIGTLink command server at port 4100
Waiting for client connections...
Client connected
 Execute command: cd('/home/alba/.config/NA-MIC/Extensions-25516/MatlabModules'); cli_argswrite('/tmp/Slicer/6792_F0fE1FtcRD.params',Module_ex(cli_argsread({'--returnparameterfile','/tmp/Slicer/6792_F0fE1FtcRD.params','--threshold','50','--inputvolume','/tmp/Slicer/GHJC_vtkMRMLScalarVolumeNodeB.nrrd','--outputvolume','/tmp/Slicer/GHJC_vtkMRMLScalarVolumeNodeC.nrrd'})));
 Response (sent to device ACK): ERROR: Command execution failed. Error using fprintf
Invalid file identifier. Use fopen to generate a valid file identifier.
Error in nrrdwrite (line 59)
fprintf(fid,'NRRD0005\n');


Error in cli_imagewrite (line 7)
nrrdwrite(outputFilename, img);


Error in Module_ex (line 20)
cli_imagewrite(inputParams.outputvolume, img);

Error in cli_commandserver (line 91)
                response=evalc(cmd);
</code></pre>
<p>It says I have an invalid file identifier but I do not understand where or how I should generate a valid one.</p>
<p>Thanks in advance!<br>
Regards ^<br>
Alba : )</p>

---

## Post #4 by @lassoan (2017-05-23 19:22 UTC)

<p>The error occurs when the MatlabBridge tries to write the output volume to /tmp/Slicer/GHJC_vtkMRMLScalarVolumeNodeC.nrrd because of permissions, disk space, or some other issue.</p>
<p>See for example this page for a few ideas: <a href="https://stackoverflow.com/questions/10606373/what-causes-an-invalid-file-identifier-in-matlab">https://stackoverflow.com/questions/10606373/what-causes-an-invalid-file-identifier-in-matlab</a></p>

---

## Post #5 by @Alba_Garcia_de_la_Ca (2017-08-03 19:22 UTC)

<p>Good evening,</p>
<p>I have been working on that matlab-slicer issue, I have research in the stackoverflow link and on my own, but I have not been able to solve it; every folde has all kind of permissions (r w x), matlab and slicer are run as an administrator (root user), and I don not know how to change the path for output data for this extension.</p>
<p>However, I have only reproduced this error on ubuntu, and although I would like to solve it I am working now with iOS.</p>
<p>Thank you so much for all! : )<br>
Regards,<br>
Alba</p>

---

## Post #6 by @lassoan (2017-08-03 19:40 UTC)

<p>Probably your temporary folder is read-only (<a href="https://issues.slicer.org/view.php?id=4340">https://issues.slicer.org/view.php?id=4340</a>). The workaround is to go to menu: Edit / Application settings / Modules, and then select a writeable directory as <code>Temporary directory</code>.</p>

---

## Post #7 by @Alba_Garcia_de_la_Ca (2017-08-08 20:15 UTC)

<p>Good evening,</p>
<p>Thank you so so much!!, really. It finally worked when I changed the tmp directory, but I do not understand why it did not work on the default tmp path even though it had all permissions.</p>
<p>Now I am calling my real code with the extension. I have a function called outliers_step1.m which is located in the MatlabModules path, and then I have my module with the .m file which executes some code lines and then calls the function, but when I run commandserver with breakpoints it shows me this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/287ec24f8a44ec2345472c74859f03ec5b976d91.png" data-download-href="/uploads/short-url/5MeG5e3l7CwzxxVyNd6ohBV4NYR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/287ec24f8a44ec2345472c74859f03ec5b976d91.png" alt="image" data-base62-sha1="5MeG5e3l7CwzxxVyNd6ohBV4NYR" width="690" height="92" data-dominant-color="F7F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1266×169 6.47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is my module .m file:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a3afec8a100432e14960048cabddc59d392c3d2.png" data-download-href="/uploads/short-url/aAFJeoqbgOUJG8unnfSuJ6IgWK6.png?dl=1" title="j" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a3afec8a100432e14960048cabddc59d392c3d2_2_690x148.png" alt="j" data-base62-sha1="aAFJeoqbgOUJG8unnfSuJ6IgWK6" width="690" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a3afec8a100432e14960048cabddc59d392c3d2_2_690x148.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a3afec8a100432e14960048cabddc59d392c3d2_2_1035x222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a3afec8a100432e14960048cabddc59d392c3d2.png 2x" data-dominant-color="32342C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">j</span><span class="informations">1167×251 60 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance,<br>
Have a nice day,<br>
Alba</p>

---

## Post #8 by @Alba_Garcia_de_la_Ca (2017-09-04 19:51 UTC)

<p>Good evening,</p>
<p>I still obtain the same error, and I do not understand why it is saying that fragment of code is a function because the function is outliers_step1.m. Do you know if I should place the function in another path? It is actually located in the MatlabModules folder with other functions from Nifti toolbox which I use and does not cause any trouble.</p>
<p>This is my function code:</p>
<p>function [outlierst1_ut,outlierst1_br1,outlierst1_br2,outlierst1_lv1,outlierst1_lv2,outlierst1_pl]=outliers_s1(detJgw,plmask83,lv1mask83,lv2mask83,br1mask83,br2mask83,uterusB3,tlpl,thpl,tllv,thlv,tlbr,thbr)<br>
%for twin data:  detJgw is the determinant of jacobian matrix;<br>
%lv1mask,lv2mask,br1mask,br2mask,uterusmask are the masks for livers,<br>
%brains and uterus;tlpl,thpl,tllv,thlv,tlbr,thbr are the thresholds for<br>
%over compression and over expansion for placenta, liver, and brain<br>
%outlierst1_* are the volumes after outlier rejection<br>
%%%function [gwuter,gwuter_0,gwbr1,gwbr1_0,gwbr2,gwbr2_0,gwlv1,gwlv1_0,gwlv2,gwlv2_0,gwpl,gwpl_0]=outliers_step1(detJgw,plmask,lv1mask,lv2mask,br1mask,br2mask,uterusmask,tlpl,thpl,tllv,thlv,tlbr,thbr)<br>
[x,y,z,t]=size(detJgw);<br>
edjgw_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;0  count0=count0+1;end,end,edjgw_0(a,d)=count0;end,end,end<br>
edjgw_tlpl=zeros(t,z);for a=1:t for d=1:z counttlpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;tlpl &amp;&amp; double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;0 counttlpl=counttlpl+1;end,end,edjgw_tlpl(a,d)=counttlpl;end,end,end<br>
edjgw_thpl=zeros(t,z);for a=1:t for d=1:z countthpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;thpl countthpl=countthpl+1;end,end,edjgw_thpl(a,d)=countthpl;end,end,end<br>
for a=1:t gwuter(a)=sum(edjgw_thpl(a,:)+edjgw_tlpl(a,:)+edjgw_0(a,:));end<br>
%for a=1:t gwuter_0(a)=sum(edjgw_0(a,:));end<br>
outlierst1_ut=find(gwuter==0);</p>
<p>br1s(:,:,:)=smooth3(br1mask83(:,:,:),‘box’,7); %evaluate a bigger region<br>
for b=1:x for c=1:y for d=1:z if br1s(b,c,d)&gt;0 br1cs(b,c,d)=1; else br1cs(b,c,d)=0; end,end,end,end<br>
edjgwbr1_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwbr1_0(a,d)=count0;end,end,end<br>
edjgwbr1_tlbr=zeros(t,z);for a=1:t for d=1:z counttlbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;tlbr &amp;&amp; double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;0 counttlbr=counttlbr+1;end,end,edjgwbr1_tlbr(a,d)=counttlbr;end,end,end<br>
edjgwbr1_thbr=zeros(t,z);for a=1:t for d=1:z countthbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;thbr countthbr=countthbr+1;end,end,edjgwbr1_thbr(a,d)=countthbr;end,end,end<br>
for a=1:t gwbr1(a)=sum(edjgwbr1_thbr(a,:)+edjgwbr1_tlbr(a,:)+edjgwbr1_0(a,:));end<br>
%for a=1:t gwbr1_0(a)=sum(edjgwbr1_0(a,:));end<br>
outlierst1_br1=find(gwbr1==0);</p>
<p>br2s(:,:,:)=smooth3(br2mask83(:,:,:),‘box’,7);<br>
for b=1:x for c=1:y for d=1:z if br2s(b,c,d)&gt;0 br2cs(b,c,d)=1; else br2cs(b,c,d)=0; end,end,end,end<br>
edjgwbr2_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwbr2_0(a,d)=count0;end,end,end<br>
edjgwbr2_tlbr=zeros(t,z);for a=1:t for d=1:z counttlbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&lt;tlbr &amp;&amp; double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&gt;0 counttlbr=counttlbr+1;end,end,edjgwbr2_tlbr(a,d)=counttlbr;end,end,end<br>
edjgwbr2_thbr=zeros(t,z);for a=1:t for d=1:z countthbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&gt;thbr countthbr=countthbr+1;end,end,edjgwbr2_thbr(a,d)=countthbr;end,end,end<br>
for a=1:t gwbr2(a)=sum(edjgwbr2_thbr(a,:)+edjgwbr2_tlbr(a,:)+edjgwbr2_0(a,:));end<br>
%for a=1:t gwbr2_0(a)=sum(edjgwbr2_0(a,:));end<br>
outlierst1_br2=find(gwbr2==0);</p>
<p>lv1s(:,:,:)=smooth3(lv1mask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if lv1s(b,c,d)&gt;0 lv1cs(b,c,d)=1; else lv1cs(b,c,d)=0; end,end,end,end<br>
edjgwlv1_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwlv1_0(a,d)=count0;end,end,end<br>
edjgwlv1_tllv=zeros(t,z);for a=1:t for d=1:z counttllv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&lt;tllv &amp;&amp; double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&gt;0 counttllv=counttllv+1;end,end,edjgwlv1_tllv(a,d)=counttllv;end,end,end<br>
edjgwlv1_thlv=zeros(t,z);for a=1:t for d=1:z countthlv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&gt;thlv countthlv=countthlv+1;end,end,edjgwlv1_thlv(a,d)=countthlv;end,end,end<br>
for a=1:t gwlv1(a)=sum(edjgwlv1_thlv(a,:)+edjgwlv1_tllv(a,:)+edjgwlv1_0(a,:));end<br>
%for a=1:t gwlv1_0(a)=sum(edjgwlv1_0(a,:));end<br>
outlierst1_lv1=find(gwlv1==0);</p>
<p>lv2s(:,:,:)=smooth3(lv2mask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if lv2s(b,c,d)&gt;0 lv2cs(b,c,d)=1; else lv2cs(b,c,d)=0; end,end,end,end<br>
edjgwlv2_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwlv2_0(a,d)=count0;end,end,end<br>
edjgwlv2_tllv=zeros(t,z);for a=1:t for d=1:z counttllv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&lt;tllv &amp;&amp; double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&gt;0 counttllv=counttllv+1;end,end,edjgwlv2_tllv(a,d)=counttllv;end,end,end<br>
edjgwlv2_thlv=zeros(t,z);for a=1:t for d=1:z countthlv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&gt;thlv countthlv=countthlv+1;end,end,edjgwlv2_thlv(a,d)=countthlv;end,end,end<br>
for a=1:t gwlv2(a)=sum(edjgwlv2_thlv(a,:)+edjgwlv2_tllv(a,:)+edjgwlv2_0(a,:));end<br>
%for a=1:t gwlv2_0(a)=sum(edjgwlv2_0(a,:));end<br>
outlierst1_lv2=find(gwlv2==0);</p>
<p>pls(:,:,:)=smooth3(plmask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if pls(b,c,d)&gt;0 plcs(b,c,d)=1; else plcs(b,c,d)=0; end,end,end,end<br>
edjgwpl_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwpl_0(a,d)=count0;end,end,end<br>
edjgwpl_tlpl=zeros(t,z);for a=1:t for d=1:z counttlpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&lt;tlpl &amp;&amp; double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&gt;0 counttlpl=counttlpl+1;end,end,edjgwpl_tlpl(a,d)=counttlpl;end,end,end<br>
edjgwpl_thpl=zeros(t,z);for a=1:t for d=1:z countthpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&gt;thpl countthpl=countthpl+1;end,end,edjgwpl_thpl(a,d)=countthpl;end,end,end<br>
for a=1:t gwpl(a)=sum(edjgwpl_thpl(a,:)+edjgwpl_tlpl(a,:)+edjgwpl_0(a,:));end<br>
%for a=1:t gwpl_0(a)=sum(edjgwpl_0(a,:));end<br>
outlierst1_pl=find(gwpl==0);</p>
<p>Thank you so much,<br>
Have a nice day,<br>
Alba!</p>

---

## Post #9 by @lassoan (2017-09-06 03:47 UTC)

<p>The issue is most likely that your filename is <code>outliers_step1.m</code> and the function name is <code>outliers_s1</code>.</p>

---

## Post #10 by @Alba_Garcia_de_la_Ca (2017-09-07 20:49 UTC)

<p>Do you mean that they have similar names? or that an m is missing? no m is missing, function’s name is outliers_s1.m and filename is outliers_step1.m</p>
<p>Thank you!</p>
<p>Alba</p>

---

## Post #11 by @lassoan (2017-09-08 13:31 UTC)

<p>Matlab function name must match the .m filename.</p>

---

## Post #12 by @Alba_Garcia_de_la_Ca (2017-09-09 11:52 UTC)

<p>Oh, I understand now. They match their names, see:</p>
<p>This is my script who calls the function: outliers_s1.m<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04aaa7634f08a6bc3c922996abc12213b0553764.png" data-download-href="/uploads/short-url/Fhx72h8U33iUIj5VGGKwtQhNY0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04aaa7634f08a6bc3c922996abc12213b0553764_2_690x205.png" alt="image" data-base62-sha1="Fhx72h8U33iUIj5VGGKwtQhNY0" width="690" height="205" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04aaa7634f08a6bc3c922996abc12213b0553764_2_690x205.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04aaa7634f08a6bc3c922996abc12213b0553764_2_1035x307.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04aaa7634f08a6bc3c922996abc12213b0553764.png 2x" data-dominant-color="3B403F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1364×406 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And this is the function (outliers_s1.m), you can see the .m file match the function’s name:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45b3b6cdebc2a484b5b039826e3f5de0849ca46e.png" data-download-href="/uploads/short-url/9WBYPlME3r0jeHNBQ4P31LIf30W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45b3b6cdebc2a484b5b039826e3f5de0849ca46e_2_690x353.png" alt="image" data-base62-sha1="9WBYPlME3r0jeHNBQ4P31LIf30W" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45b3b6cdebc2a484b5b039826e3f5de0849ca46e_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45b3b6cdebc2a484b5b039826e3f5de0849ca46e_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45b3b6cdebc2a484b5b039826e3f5de0849ca46e.png 2x" data-dominant-color="3D4444"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1365×700 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I still obtain the error my script Outliers_step1.m is being called as a function:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f83a74369440079c4b2118fc8c5f47aab58d6a7b.png" data-download-href="/uploads/short-url/zpVEhrjGlhmJ92N2QZN3vBvjiSD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f83a74369440079c4b2118fc8c5f47aab58d6a7b.png" alt="image" data-base62-sha1="zpVEhrjGlhmJ92N2QZN3vBvjiSD" width="690" height="182" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1015×269 7.36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I believe script’s name and function’s name do not have to match, do they?</p>
<p>Thank you so much<br>
Alba</p>

---

## Post #13 by @lassoan (2017-09-09 12:04 UTC)

<p>I don’t see the complete error message. What is the rest of the message after “…cli_argswrite(’/usr/local/bin/Slicer/MATLAB…”?</p>
<p>I suspect that your Slicer Matlab module name is Outliers_step1, which must be a function (because it gets input parameters as function arguments and may provide results in return value).</p>

---

## Post #14 by @Alba_Garcia_de_la_Ca (2017-09-11 21:17 UTC)

<p>Hi!</p>
<p>This is the full message (I cleaned some useless data):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89a254ccb965315d013d06d8e56e7b37a11cdc53.png" data-download-href="/uploads/short-url/jDzcNYd3cdsMNzeRJ9ka3CbuuJR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89a254ccb965315d013d06d8e56e7b37a11cdc53.png" alt="image" data-base62-sha1="jDzcNYd3cdsMNzeRJ9ka3CbuuJR" width="690" height="118" data-dominant-color="F6F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×170 5.38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Yes, but I define the function in a script and then I call this function which returns several parameters in another script, so the function is defined in outliers_s1.m and I call it after loading some data in the outliers_step1.m script. Is that not correct then?</p>
<p>Thank you!<br>
Alba</p>

---

## Post #15 by @lassoan (2017-09-11 21:26 UTC)

<aside class="quote no-group" data-username="Alba_Garcia_de_la_Ca" data-post="14" data-topic="314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alba_garcia_de_la_ca/48/181_2.png" class="avatar"> Alba_Garcia_de_la_Ca:</div>
<blockquote>
<p>Is that not correct then?</p>
</blockquote>
</aside>
<p>It is not. The function definition in the file that is created by the MatlabBridge’s module generator must not be changed, but you can call any other functions or scripts from that function.</p>

---

## Post #16 by @Alba_Garcia_de_la_Ca (2017-09-12 20:46 UTC)

<p>HI!,</p>
<p>Ok. I was performing that way because in Matlab I can run it that way, I had the same structure, the outliers_s1.m function and the Outliers_step1.m script who called outliers_s1. function (I did that because my Matlab 2014b was giving me trouble).</p>
<p>Now I have implemented the code all in one, this way:</p>
<p>function [outlierst1_ut,outlierst1_br1,outlierst1_br2,outlierst1_lv1,outlierst1_lv2,outlierst1_pl]=Outliers_step1(detJgw,plmask83,lv1mask83,lv2mask83,br1mask83,br2mask83,uterusB3,tlpl,thpl,tllv,thlv,tlbr,thbr)</p>
<p>detJgw=zeros(110,110,80,82);<br>
tlpl = 0.5; thpl=1.5; tllv=0.7; thlv=1.3; tlbr=0.8; thbr=1.2;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/plmask83.nii’));plmask83=ans.img;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/lv1mask83.nii’));lv1mask83=ans.img;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/lv2mask83.nii’));lv2mask83=ans.img;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/br1mask83.nii’));br1mask83=ans.img;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/br2mask83.nii’));br2mask83=ans.img;<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/uterus_B3.nii’));uterusB3=ans.img;</p>
<p>for a=4:6<br>
load_nii(sprintf(‘/usr/local/bin/Slicer/elastix_/oddevenB01/tmeosh_%d/spatialJacobian.nii’,a));detJgw(:,:,2:2:80,a)=ans.img;<br>
load_nii(sprintf(‘/usr/local/bin/Slicer/elastix_/oddevenB01/tmoosh_%d/spatialJacobian.nii’,a));detJgw(:,:,1:2:79,a)=ans.img;<br>
end<br>
%for twin data:  detJgw is the determinant of jacobian matrix;<br>
%lv1mask,lv2mask,br1mask,br2mask,uterusmask are the masks for livers,<br>
%brains and uterus;tlpl,thpl,tllv,thlv,tlbr,thbr are the thresholds for<br>
%over compression and over expansion for placenta, liver, and brain<br>
%outlierst1_* are the volumes after outlier rejection<br>
%%%function [gwuter,gwuter_0,gwbr1,gwbr1_0,gwbr2,gwbr2_0,gwlv1,gwlv1_0,gwlv2,gwlv2_0,gwpl,gwpl_0]=outliers_step1(detJgw,plmask,lv1mask,lv2mask,br1mask,br2mask,uterusmask,tlpl,thpl,tllv,thlv,tlbr,thbr)<br>
[x,y,z,t]=size(detJgw);<br>
edjgw_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;0  count0=count0+1;end,end,edjgw_0(a,d)=count0;end,end,end<br>
edjgw_tlpl=zeros(t,z);for a=1:t for d=1:z counttlpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;tlpl &amp;&amp; double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;0 counttlpl=counttlpl+1;end,end,edjgw_tlpl(a,d)=counttlpl;end,end,end<br>
edjgw_thpl=zeros(t,z);for a=1:t for d=1:z countthpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;thpl countthpl=countthpl+1;end,end,edjgw_thpl(a,d)=countthpl;end,end,end<br>
for a=1:t gwuter(a)=sum(edjgw_thpl(a,:)+edjgw_tlpl(a,:)+edjgw_0(a,:));end<br>
%for a=1:t gwuter_0(a)=sum(edjgw_0(a,:));end<br>
outlierst1_ut=find(gwuter==0);</p>
<p>br1s(:,:,:)=smooth3(br1mask83(:,:,:),‘box’,7); %evaluate a bigger region<br>
for b=1:x for c=1:y for d=1:z if br1s(b,c,d)&gt;0 br1cs(b,c,d)=1; else br1cs(b,c,d)=0; end,end,end,end<br>
edjgwbr1_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwbr1_0(a,d)=count0;end,end,end<br>
edjgwbr1_tlbr=zeros(t,z);for a=1:t for d=1:z counttlbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;tlbr &amp;&amp; double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;0 counttlbr=counttlbr+1;end,end,edjgwbr1_tlbr(a,d)=counttlbr;end,end,end<br>
edjgwbr1_thbr=zeros(t,z);for a=1:t for d=1:z countthbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;thbr countthbr=countthbr+1;end,end,edjgwbr1_thbr(a,d)=countthbr;end,end,end<br>
for a=1:t gwbr1(a)=sum(edjgwbr1_thbr(a,:)+edjgwbr1_tlbr(a,:)+edjgwbr1_0(a,:));end<br>
%for a=1:t gwbr1_0(a)=sum(edjgwbr1_0(a,:));end<br>
outlierst1_br1=find(gwbr1==0);</p>
<p>br2s(:,:,:)=smooth3(br2mask83(:,:,:),‘box’,7);<br>
for b=1:x for c=1:y for d=1:z if br2s(b,c,d)&gt;0 br2cs(b,c,d)=1; else br2cs(b,c,d)=0; end,end,end,end<br>
edjgwbr2_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwbr2_0(a,d)=count0;end,end,end<br>
edjgwbr2_tlbr=zeros(t,z);for a=1:t for d=1:z counttlbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&lt;tlbr &amp;&amp; double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&gt;0 counttlbr=counttlbr+1;end,end,edjgwbr2_tlbr(a,d)=counttlbr;end,end,end<br>
edjgwbr2_thbr=zeros(t,z);for a=1:t for d=1:z countthbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br2cs(b,c,d))&gt;thbr countthbr=countthbr+1;end,end,edjgwbr2_thbr(a,d)=countthbr;end,end,end<br>
for a=1:t gwbr2(a)=sum(edjgwbr2_thbr(a,:)+edjgwbr2_tlbr(a,:)+edjgwbr2_0(a,:));end<br>
%for a=1:t gwbr2_0(a)=sum(edjgwbr2_0(a,:));end<br>
outlierst1_br2=find(gwbr2==0);</p>
<p>lv1s(:,:,:)=smooth3(lv1mask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if lv1s(b,c,d)&gt;0 lv1cs(b,c,d)=1; else lv1cs(b,c,d)=0; end,end,end,end<br>
edjgwlv1_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwlv1_0(a,d)=count0;end,end,end<br>
edjgwlv1_tllv=zeros(t,z);for a=1:t for d=1:z counttllv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&lt;tllv &amp;&amp; double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&gt;0 counttllv=counttllv+1;end,end,edjgwlv1_tllv(a,d)=counttllv;end,end,end<br>
edjgwlv1_thlv=zeros(t,z);for a=1:t for d=1:z countthlv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv1cs(b,c,d))&gt;thlv countthlv=countthlv+1;end,end,edjgwlv1_thlv(a,d)=countthlv;end,end,end<br>
for a=1:t gwlv1(a)=sum(edjgwlv1_thlv(a,:)+edjgwlv1_tllv(a,:)+edjgwlv1_0(a,:));end<br>
%for a=1:t gwlv1_0(a)=sum(edjgwlv1_0(a,:));end<br>
outlierst1_lv1=find(gwlv1==0);</p>
<p>lv2s(:,:,:)=smooth3(lv2mask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if lv2s(b,c,d)&gt;0 lv2cs(b,c,d)=1; else lv2cs(b,c,d)=0; end,end,end,end<br>
edjgwlv2_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwlv2_0(a,d)=count0;end,end,end<br>
edjgwlv2_tllv=zeros(t,z);for a=1:t for d=1:z counttllv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&lt;tllv &amp;&amp; double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&gt;0 counttllv=counttllv+1;end,end,edjgwlv2_tllv(a,d)=counttllv;end,end,end<br>
edjgwlv2_thlv=zeros(t,z);for a=1:t for d=1:z countthlv=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(lv2cs(b,c,d))&gt;thlv countthlv=countthlv+1;end,end,edjgwlv2_thlv(a,d)=countthlv;end,end,end<br>
for a=1:t gwlv2(a)=sum(edjgwlv2_thlv(a,:)+edjgwlv2_tllv(a,:)+edjgwlv2_0(a,:));end<br>
%for a=1:t gwlv2_0(a)=sum(edjgwlv2_0(a,:));end<br>
outlierst1_lv2=find(gwlv2==0);</p>
<p>pls(:,:,:)=smooth3(plmask83(:,:,:),‘box’,9);<br>
for b=1:x for c=1:y for d=1:z if pls(b,c,d)&gt;0 plcs(b,c,d)=1; else plcs(b,c,d)=0; end,end,end,end<br>
edjgwpl_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwpl_0(a,d)=count0;end,end,end<br>
edjgwpl_tlpl=zeros(t,z);for a=1:t for d=1:z counttlpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&lt;tlpl &amp;&amp; double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&gt;0 counttlpl=counttlpl+1;end,end,edjgwpl_tlpl(a,d)=counttlpl;end,end,end<br>
edjgwpl_thpl=zeros(t,z);for a=1:t for d=1:z countthpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(plcs(b,c,d))&gt;thpl countthpl=countthpl+1;end,end,edjgwpl_thpl(a,d)=countthpl;end,end,end<br>
for a=1:t gwpl(a)=sum(edjgwpl_thpl(a,:)+edjgwpl_tlpl(a,:)+edjgwpl_0(a,:));end<br>
%for a=1:t gwpl_0(a)=sum(edjgwpl_0(a,:));end<br>
outlierst1_pl=find(gwpl==0);</p>
<p>It is the same, but loading parameters in the function. Now, while debugging I do not obtain an error, but the script stays running without stop so it is not ok. When I stop the module in slicer I obtain this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87cd04da5f1f48a2b07eb5ff1316df88bd205f84.png" data-download-href="/uploads/short-url/jnlHZHDygxpImZPPHzpQwGh90gs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87cd04da5f1f48a2b07eb5ff1316df88bd205f84_2_690x416.png" alt="image" data-base62-sha1="jnlHZHDygxpImZPPHzpQwGh90gs" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87cd04da5f1f48a2b07eb5ff1316df88bd205f84_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87cd04da5f1f48a2b07eb5ff1316df88bd205f84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87cd04da5f1f48a2b07eb5ff1316df88bd205f84.png 2x" data-dominant-color="E8EAED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">751×453 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But I guess it is caused due to the interruption</p>
<p>Do you know what could be happening?</p>
<p>Thank you so much,<br>
Alba</p>

---

## Post #17 by @Alba_Garcia_de_la_Ca (2017-09-13 21:17 UTC)

<p>Hi again!</p>
<p>Sorry if I am doing so many questions, or if they are simple or easy. Calling this function and the following is the last step to end my final degree.</p>
<p>Now I call another function, but it says an input parameter is referenced and not found, but it is not the case:</p>
<p>Function Outliers_step2.m:</p>
<p>%%function [outlierst2,regmask_or]=outlier_step2(regdata,refframe,mask,outlierst1)<br>
function [outlierst2,regmask,outlier,smoothmask]=outlier_step2(regdata,refframe,mask,outlierst1)<br>
%Input<br>
%regdata: registered data set, refframe: reference frame number, mask: used<br>
for a=1:5<br>
load_untouch_nii(sprintf(‘/usr/local/bin/Slicer/elastix_/nonrigid_%d/result.0.nii’,a));regdata(:,:,:,a)=ans.img;<br>
end<br>
refframe= 31;<br>
%mask to calculate the average signal, outlierst1: at the end, to exclude the ones<br>
load_untouch_nii(sprintf(‘012115/uterus_B3.nii’));mask=ans.img;<br>
outlierst1 = load(sprintf(‘/usr/local/bin/Slicer/outlierst1_ut.mat’))<br>
%rejected due to over deformation.<br>
%Output<br>
%outlierst2 are the volumes after outlier rejection<br>
%regmask: updated mask showing corrected region with 1 and outlier voxels<br>
%with 2,outlier: number of outlier voxels for each time frame,<br>
%smoothmask:original mask<br>
[x,y,z,t]=size(regdata);<br>
%smoothmask=zeros(x,y,z);<br>
%smask(:,:,:)=smooth3(mask(:,:,:),‘box’,3);<br>
%for b=1:x for c=1:y for d=1:z if smask(b,c,d)&gt;0.5 smoothmask(b,c,d)=1; else smoothmask(b,c,d)=0; end,end,end,end<br>
smoothmask=mask(:,:,:);</p>
<p>regmask=zeros(x,y,z,t);<br>
regmasked=zeros(x,y,z,t);<br>
for k=1:t<br>
regmask(:,:,:,k)=smoothmask(:,:,:);<br>
regmasked(:,:,:,k)=double(smoothmask(:,:,:)).*double(regdata(:,:,:,k));<br>
end<br>
Mref=regmasked(:,:,:,refframe);<br>
%med=sort(nonzeros(Mref(:)));<br>
%Qmid=floor(nnz(med)/2)+1;<br>
%Qmidv=med(Qmid);<br>
mb=mean(nonzeros(Mref(:)));<br>
sb=std(nonzeros(Mref(:)));<br>
mdummy=mb;<br>
%mdummy=Qmidv;<br>
sdummy=sb;<br>
outlier=zeros(1,t);<br>
regmaskedn=regmasked;</p>
<p>for k=refframe:(t-1)<br>
for a=1:x<br>
for b=1:y<br>
for c=1:z<br>
if abs(regmaskedn(a,b,c,k)-regmaskedn(a,b,c,k+1))&gt;mdummy<br>
regmask(a,b,c,k+1)=2;<br>
regmaskedn(a,b,c,k+1)=regmaskedn(a,b,c,k);<br>
outlier(k+1)=outlier(k+1)+1;<br>
end</p>
<pre><code>        end
    end
end
for a=2:(x-1)
    for b=2:(y-1)
        for c=2:(z-1)
            if regmask(a-1,b+1,c,k+1)==2 &amp;&amp; regmask(a-1,b,c,k+1)==2 &amp;&amp; regmask(a-1,b-1,c,k+1)==2 &amp;&amp; ...
                    regmask(a,b+1,c,k+1)==2 &amp;&amp; regmask(a,b,c,k+1)==1 &amp;&amp; regmask(a,b-1,c,k+1)==2 &amp;&amp; ...
                    regmask(a+1,b+1,c,k+1)==2 &amp;&amp; regmask(a+1,b,c,k+1)==2 &amp;&amp; regmask(a+1,b-1,c,k+1)==2
</code></pre>
<p>%                         regmask(a-1,b+1,c-1,k+1)==2 &amp;&amp; regmask(a-1,b,c-1,k+1)==2 &amp;&amp; regmask(a-1,b-1,c-1,k+1)==2 &amp;&amp; …<br>
%                         regmask(a,b+1,c-1,k+1)==2 &amp;&amp; regmask(a,b,c-1,k+1)==2 &amp;&amp; regmask(a,b-1,c-1,k+1)==2 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c-1,k+1)==2 &amp;&amp; regmask(a+1,b,c-1,k+1)==2 &amp;&amp; regmask(a+1,b-1,c-1,k+1)==2 &amp;&amp; …<br>
%                         regmask(a-1,b+1,c+1,k+1)==2 &amp;&amp; regmask(a-1,b,c+1,k+1)==2 &amp;&amp; regmask(a-1,b-1,c+1,k+1)==2 &amp;&amp; …<br>
%                         regmask(a,b+1,c+1,k+1)==2 &amp;&amp; regmask(a,b,c+1,k+1)==2 &amp;&amp; regmask(a,b-1,c+1,k+1)==2 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c+1,k+1)==2 &amp;&amp; regmask(a+1,b,c+1,k+1)==2 &amp;&amp; regmask(a+1,b-1,c+1,k+1)==2</p>
<pre><code>                regmask(a,b,c,k+1)=2;
                regmaskedn(a,b,c,k+1)=regmaskedn(a,b,c,k);
                outlier(k+1)=outlier(k+1)+1;
            end
        end
    end
end
for a=2:(x-1)
    for b=2:(y-1)
        for c=2:(z-1)
            if regmask(a-1,b+1,c,k+1)==1 &amp;&amp; regmask(a-1,b,c,k+1)==1 &amp;&amp; regmask(a-1,b-1,c,k+1)==1 &amp;&amp; ...
                    regmask(a,b+1,c,k+1)==1 &amp;&amp; regmask(a,b,c,k+1)==2 &amp;&amp; regmask(a,b-1,c,k+1)==1 &amp;&amp; ...
                    regmask(a+1,b+1,c,k+1)==1 &amp;&amp; regmask(a+1,b,c,k+1)==1 &amp;&amp; regmask(a+1,b-1,c,k+1)==1
</code></pre>
<p>%                         regmask(a-1,b+1,c-1,k+1)==1 &amp;&amp; regmask(a-1,b,c-1,k+1)==1 &amp;&amp; regmask(a-1,b-1,c-1,k+1)==1 &amp;&amp; …<br>
%                         regmask(a,b+1,c-1,k+1)==1 &amp;&amp; regmask(a,b,c-1,k+1)==1 &amp;&amp; regmask(a,b-1,c-1,k+1)==1 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c-1,k+1)==1 &amp;&amp; regmask(a+1,b,c-1,k+1)==1 &amp;&amp; regmask(a+1,b-1,c-1,k+1)==1 &amp;&amp; …<br>
%                         regmask(a-1,b+1,c+1,k+1)==1 &amp;&amp; regmask(a-1,b,c+1,k+1)==1 &amp;&amp; regmask(a-1,b-1,c+1,k+1)==1 &amp;&amp; …<br>
%                         regmask(a,b+1,c+1,k+1)==1 &amp;&amp; regmask(a,b,c+1,k+1)==1 &amp;&amp; regmask(a,b-1,c+1,k+1)==1 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c+1,k+1)==1 &amp;&amp; regmask(a+1,b,c+1,k+1)==1 &amp;&amp; regmask(a+1,b-1,c+1,k+1)==1<br>
regmask(a,b,c,k+1)=1;<br>
outlier(k+1)=outlier(k+1)-1;<br>
end<br>
end<br>
end<br>
end<br>
M=regmaskedn(:,:,:,k+1);<br>
%med=sort(nonzeros(M(:)));<br>
%Qmid=floor(nnz(med)/2)+1;<br>
%Qmidv=med(Qmid);<br>
%mdummy=Qmidv;<br>
mdummy=mean(nonzeros(M(:)));<br>
sdummy=std(nonzeros(M(:)));<br>
end</p>
<p>for k=refframe:-1:2<br>
for a=1:x<br>
for b=1:y<br>
for c=1:z<br>
if abs(regmaskedn(a,b,c,k)-regmaskedn(a,b,c,k-1))&gt;mdummy<br>
regmask(a,b,c,k-1)=2;<br>
regmaskedn(a,b,c,k-1)=regmaskedn(a,b,c,k);<br>
outlier(k-1)=outlier(k-1)+1;<br>
end</p>
<pre><code>        end
    end
end
for a=2:(x-1)
    for b=2:(y-1)
        for c=2:(z-1)
            if regmask(a-1,b+1,c,k-1)==2 &amp;&amp; regmask(a-1,b,c,k-1)==2 &amp;&amp; regmask(a-1,b-1,c,k-1)==2 &amp;&amp; ...
                    regmask(a,b+1,c,k-1)==2 &amp;&amp; regmask(a,b,c,k-1)==1 &amp;&amp; regmask(a,b-1,c,k-1)==2 &amp;&amp; ...
                    regmask(a+1,b+1,c,k-1)==2 &amp;&amp; regmask(a+1,b,c,k-1)==2 &amp;&amp; regmask(a+1,b-1,c,k-1)==2 
</code></pre>
<p>%                         regmask(a-1,b+1,c-1,k-1)==2 &amp;&amp; regmask(a-1,b,c-1,k-1)==2 &amp;&amp; regmask(a-1,b-1,c-1,k-1)==2 &amp;&amp; …<br>
%                         regmask(a,b+1,c-1,k-1)==2 &amp;&amp; regmask(a,b,c-1,k-1)==2 &amp;&amp; regmask(a,b-1,c-1,k-1)==2 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c-1,k-1)==2 &amp;&amp; regmask(a+1,b,c-1,k-1)==2 &amp;&amp; regmask(a+1,b-1,c-1,k-1)==2 &amp;&amp; …<br>
%                         regmask(a-1,b+1,c+1,k-1)==2 &amp;&amp; regmask(a-1,b,c+1,k-1)==2 &amp;&amp; regmask(a-1,b-1,c+1,k-1)==2 &amp;&amp; …<br>
%                         regmask(a,b+1,c+1,k-1)==2 &amp;&amp; regmask(a,b,c+1,k-1)==2 &amp;&amp; regmask(a,b-1,c+1,k-1)==2 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c+1,k-1)==2 &amp;&amp; regmask(a+1,b,c+1,k-1)==2 &amp;&amp; regmask(a+1,b-1,c+1,k-1)==2<br>
regmask(a,b,c,k-1)=2;<br>
regmaskedn(a,b,c,k-1)=regmaskedn(a,b,c,k);<br>
outlier(k-1)=outlier(k-1)+1;<br>
end<br>
end<br>
end<br>
end<br>
for a=2:(x-1)<br>
for b=2:(y-1)<br>
for c=2:(z-1)<br>
if regmask(a-1,b+1,c,k-1)==1 &amp;&amp; regmask(a-1,b,c,k-1)==1 &amp;&amp; regmask(a-1,b-1,c,k-1)==1 &amp;&amp; …<br>
regmask(a,b+1,c,k-1)==1 &amp;&amp; regmask(a,b,c,k-1)==2 &amp;&amp; regmask(a,b-1,c,k-1)==1 &amp;&amp; …<br>
regmask(a+1,b+1,c,k-1)==1 &amp;&amp; regmask(a+1,b,c,k-1)==1 &amp;&amp; regmask(a+1,b-1,c,k-1)==1<br>
%                         regmask(a-1,b+1,c-1,k-1)==1 &amp;&amp; regmask(a-1,b,c-1,k-1)==1 &amp;&amp; regmask(a-1,b-1,c-1,k-1)==1 &amp;&amp; …<br>
%                         regmask(a,b+1,c-1,k-1)==1 &amp;&amp; regmask(a,b,c-1,k-1)==1 &amp;&amp; regmask(a,b-1,c-1,k-1)==1 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c-1,k-1)==1 &amp;&amp; regmask(a+1,b,c-1,k-1)==1 &amp;&amp; regmask(a+1,b-1,c-1,k-1)==1 &amp;&amp; …<br>
%                         regmask(a-1,b+1,c+1,k-1)==1 &amp;&amp; regmask(a-1,b,c+1,k-1)==1 &amp;&amp; regmask(a-1,b-1,c+1,k-1)==1 &amp;&amp; …<br>
%                         regmask(a,b+1,c+1,k-1)==1 &amp;&amp; regmask(a,b,c+1,k-1)==1 &amp;&amp; regmask(a,b-1,c+1,k-1)==1 &amp;&amp; …<br>
%                         regmask(a+1,b+1,c+1,k-1)==1 &amp;&amp; regmask(a+1,b,c+1,k-1)==1 &amp;&amp; regmask(a+1,b-1,c+1,k-1)==1<br>
regmask(a,b,c,k-1)=1;<br>
outlier(k-1)=outlier(k-1)-1;<br>
end<br>
end<br>
end<br>
end<br>
M=regmaskedn(:,:,:,k-1);<br>
% med=sort(nonzeros(M(:)));<br>
% Qmid=floor(nnz(med)/2)+1;<br>
% Qmidv=med(Qmid);<br>
% mdummy=Qmidv;<br>
mdummy=mean(nonzeros(M(:)));<br>
sdummy=std(nonzeros(M(:)));<br>
end<br>
tv=nnz(smoothmask);<br>
orvols=find(outlier(outlierst1)&lt;tv*5/100); %threshold %5 of voxels<br>
outlierst2=outlierst1(orvols);</p>
<p>for a=1:t for b=1:x for c=1:y for d=1:z if regmask(b,c,d,a)==0 || regmask(b,c,d,a)==2 regmask_or(b,c,d,a)=0; else regmask_or(b,c,d,a)=1;end,end,end,end,end</p>
<p>% for a=1:t regmask_ors(:,:,:,a)=smooth3(regmask_or(:,:,:,a),‘box’,3);end<br>
% for a=1:t for b=1:x for c=1:y for d=1:z if regmask_ors(b,c,d,a)&gt;0.5 regmask_orsc(b,c,d,a)=1; else regmask_orsc(b,c,d,a)=0; end,end,end,end,end</p>
<p>And the xml from matlabbridge for that module is the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac4fc39a7cf311b64db9e3560c27e9d758373270.png" data-download-href="/uploads/short-url/oAl19JGk1IkSDAORjBKqfupSQA8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4fc39a7cf311b64db9e3560c27e9d758373270_2_690x239.png" alt="image" data-base62-sha1="oAl19JGk1IkSDAORjBKqfupSQA8" width="690" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4fc39a7cf311b64db9e3560c27e9d758373270_2_690x239.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac4fc39a7cf311b64db9e3560c27e9d758373270_2_1035x358.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac4fc39a7cf311b64db9e3560c27e9d758373270.png 2x" data-dominant-color="363D3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1349×469 86.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you know waht could be happening?</p>
<p>Thank you so much,<br>
Alba</p>

---

## Post #18 by @lassoan (2017-09-13 21:45 UTC)

<p>It’s very difficult to browse and understand the long code files that you include in your message. Could you please upload all relevant files to a GitHub repository and just copy-paste the link here? Thanks!</p>

---

## Post #19 by @Alba_Garcia_de_la_Ca (2017-09-14 04:36 UTC)

<p>Of course!</p>
<p>This is the files I use in Matlab for Outliers_step1 (they work), their names are outliers_s1.m for the function, and out_step1_2.m for the script who load parameters and calls the function:</p>
<p>outliers_s1.m</p><aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/outliers_s1.m">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/outliers_s1.m" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/outliers_s1.m" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/outliers_s1.m</a></h4>


      <pre><code class="lang-m">function [outlierst1_ut,outlierst1_br1,outlierst1_br2,outlierst1_lv1,outlierst1_lv2,outlierst1_pl]=outliers_s1(detJgw,plmask83,lv1mask83,lv2mask83,br1mask83,br2mask83,uterusB3,tlpl,thpl,tllv,thlv,tlbr,thbr) 
%for twin data:  detJgw is the determinant of jacobian matrix;
%lv1mask,lv2mask,br1mask,br2mask,uterusmask are the masks for livers,
%brains and uterus;tlpl,thpl,tllv,thlv,tlbr,thbr are the thresholds for
%over compression and over expansion for placenta, liver, and brain 
%outlierst1_* are the volumes after outlier rejection
%%%function [gwuter,gwuter_0,gwbr1,gwbr1_0,gwbr2,gwbr2_0,gwlv1,gwlv1_0,gwlv2,gwlv2_0,gwpl,gwpl_0]=outliers_step1(detJgw,plmask,lv1mask,lv2mask,br1mask,br2mask,uterusmask,tlpl,thpl,tllv,thlv,tlbr,thbr)
[x,y,z,t]=size(detJgw);
edjgw_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;0  count0=count0+1;end,end,edjgw_0(a,d)=count0;end,end,end
edjgw_tlpl=zeros(t,z);for a=1:t for d=1:z counttlpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&lt;tlpl &amp;&amp; double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;0 counttlpl=counttlpl+1;end,end,edjgw_tlpl(a,d)=counttlpl;end,end,end
edjgw_thpl=zeros(t,z);for a=1:t for d=1:z countthpl=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(uterusB3(b,c,d))&gt;thpl countthpl=countthpl+1;end,end,edjgw_thpl(a,d)=countthpl;end,end,end
for a=1:t gwuter(a)=sum(edjgw_thpl(a,:)+edjgw_tlpl(a,:)+edjgw_0(a,:));end
%for a=1:t gwuter_0(a)=sum(edjgw_0(a,:));end
outlierst1_ut=find(gwuter==0);

br1s(:,:,:)=smooth3(br1mask83(:,:,:),'box',7); %evaluate a bigger region
for b=1:x for c=1:y for d=1:z if br1s(b,c,d)&gt;0 br1cs(b,c,d)=1; else br1cs(b,c,d)=0; end,end,end,end
edjgwbr1_0=zeros(t,z);for a=1:t for d=1:z count0=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;0  count0=count0+1;end,end,edjgwbr1_0(a,d)=count0;end,end,end
edjgwbr1_tlbr=zeros(t,z);for a=1:t for d=1:z counttlbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&lt;tlbr &amp;&amp; double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;0 counttlbr=counttlbr+1;end,end,edjgwbr1_tlbr(a,d)=counttlbr;end,end,end
edjgwbr1_thbr=zeros(t,z);for a=1:t for d=1:z countthbr=0; for b=1:x for c=1:y  if double(detJgw(b,c,d,a)).*double(br1cs(b,c,d))&gt;thbr countthbr=countthbr+1;end,end,edjgwbr1_thbr(a,d)=countthbr;end,end,end
</code></pre>



  This file has been truncated. <a href="https://github.com/albagcs/Final-Degree/blob/master/outliers_s1.m" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>out_step1_2.m</p><aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/out_step1_2.m">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/out_step1_2.m" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/out_step1_2.m" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/out_step1_2.m</a></h4>


      <pre><code class="lang-m">%example 
detJgw=zeros(110,110,80,82);
tlpl = 0.5; thpl=1.5; tllv=0.7; thlv=1.3; tlbr=0.8; thbr=1.2;
load_untouch_nii(sprintf('plmask83.nii'));plmask83=ans.img;
load_untouch_nii(sprintf('lv1mask83.nii'));lv1mask83=ans.img;
load_untouch_nii(sprintf('lv2mask83.nii'));lv2mask83=ans.img;
load_untouch_nii(sprintf('br1mask83.nii'));br1mask83=ans.img;
load_untouch_nii(sprintf('br2mask83.nii'));br2mask83=ans.img;
load_untouch_nii(sprintf('012115/uterus_B3.nii'));uterusB3=ans.img;

for a=1:82
    disp('Hola, mundo')
    load_nii(sprintf('elastix/oddevenB01/tmeosh_%d/spatialJacobian.nii',a));detJgw_B14(:,:,2:2:80,a)=ans.img;
    load_nii(sprintf('elastix/oddevenB01/tmoosh_%d/spatialJacobian.nii',a));detJgw_B14(:,:,1:2:79,a)=ans.img;
end
[outlierst1_ut,outlierst1_br1,outlierst1_br2,outlierst1_lv1,outlierst1_lv2,outlierst1_pl]=outliers_s1(detJgw_B14,plmask83,lv1mask83,lv2mask83,br1mask83,br2mask83,uterusB3,tlpl,thpl,tllv,thlv,tlbr,thbr);


</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And this is the one for Slicer’s module of Matlab Bridge</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.m">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.m" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.m" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/Outliers_step1.m</a></h4>


      <pre><code class="lang-m">function [outlierst1_ut,outlierst1_br1,outlierst1_br2,outlierst1_lv1,outlierst1_lv2,outlierst1_pl]=Outliers_step1(detJgw,plmask83,lv1mask83,lv2mask83,br1mask83,br2mask83,uterusB3,tlpl,thpl,tllv,thlv,tlbr,thbr) 


detJgw=zeros(110,110,80,82);
tlpl = 0.5; thpl=1.5; tllv=0.7; thlv=1.3; tlbr=0.8; thbr=1.2;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/plmask83.nii'));plmask83=ans.img;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/lv1mask83.nii'));lv1mask83=ans.img;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/lv2mask83.nii'));lv2mask83=ans.img;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/br1mask83.nii'));br1mask83=ans.img;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/br2mask83.nii'));br2mask83=ans.img;
load_untouch_nii(sprintf('/usr/local/bin/Slicer/uterus_B3.nii'));uterusB3=ans.img;

for a=4:6
    load_nii(sprintf('/usr/local/bin/Slicer/elastix_/oddevenB01/tmeosh_%d/spatialJacobian.nii',a));detJgw(:,:,2:2:80,a)=ans.img;
    load_nii(sprintf('/usr/local/bin/Slicer/elastix_/oddevenB01/tmoosh_%d/spatialJacobian.nii',a));detJgw(:,:,1:2:79,a)=ans.img;
end
%for twin data:  detJgw is the determinant of jacobian matrix;
%lv1mask,lv2mask,br1mask,br2mask,uterusmask are the masks for livers,
%brains and uterus;tlpl,thpl,tllv,thlv,tlbr,thbr are the thresholds for
%over compression and over expansion for placenta, liver, and brain 
</code></pre>



  This file has been truncated. <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.m" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.xml">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.xml" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.xml" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/Outliers_step1.xml</a></h4>


      <pre><code class="lang-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;Matlab&lt;/category&gt;
  &lt;title&gt;Outliers_step1&lt;/title&gt;
  &lt;description&gt;&lt;![CDATA[Perform a simple image processing and image statistics computation in Matlab.]]&gt;&lt;/description&gt;
  &lt;version&gt;0.0.0.1&lt;/version&gt;
  &lt;documentation-url&gt;http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/MatlabBridge&lt;/documentation-url&gt;
  &lt;license/&gt;
  &lt;contributor&gt;Andras Lasso (PerkLab)&lt;/contributor&gt;
  &lt;acknowledgements&gt;&lt;![CDATA[SparKit is a project funded by Cancer Care Ontarioand the Ontario Consortium for Adaptive Interventions in Radiation Oncology (OCAIRO) to provide free, open-source toolset for radiotherapy and related image-guided interventions.]]&gt;&lt;/acknowledgements&gt;
  &lt;parameters&gt;
    &lt;label&gt;Processing Parameters&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Parameters for the processing]]&gt;&lt;/description&gt;
    
  &lt;/parameters&gt;
  &lt;parameters&gt;
    &lt;label&gt;IO&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
    
  &lt;/parameters&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step1.xml" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The error in this module in slicer is, after putting all in the same function file, it stays running and no ends until I stop manually the module in Slicer, and then it shows me the error:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a3d74ab331214b5ad03fab22bd39cf9b65a46bc.png" alt="image" data-base62-sha1="1sArsWJEkoosmD64jEZP0gjvQtK" width="690" height="416"></p>
<p>This is the code for Outliers_step2 in Slicer’s module of Matlab Bridge</p><aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.m">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.m" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.m" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/Outliers_step2.m</a></h4>


      <pre><code class="lang-m">function outputParams=Outliers_step2(inputParams)
% Example function that returns the minimum and maximum voxel value in a volume
% and performs thresholding operation on the volume.
%
% Parameters:
%  inputParams.threshold: threshold value
%  inputParams.inputvolume: input image filename
%  inputParams.outputvolume: output image filename, result of the processing
%  outputParams.min: image minimum value
%  outputParams.max: image maximum value
%

img=cli_imageread(inputParams.inputvolume);

outputParams.min=min(min(min(img.pixelData)));
outputParams.max=max(max(max(img.pixelData)));

img.pixelData=(double(img.pixelData)&gt;inputParams.threshold)*100;

cli_imagewrite(inputParams.outputvolume, img);
</code></pre>



  This file has been truncated. <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.m" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubblob" data-onebox-src="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.xml">
  <header class="source">

      <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.xml" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.xml" target="_blank" rel="noopener nofollow ugc">albagcs/Final-Degree/blob/master/Outliers_step2.xml</a></h4>


      <pre><code class="lang-xml">&lt;?xml version="1.0" encoding="utf-8"?&gt;
&lt;executable&gt;
  &lt;category&gt;Matlab&lt;/category&gt;
  &lt;title&gt;Outliers_step2&lt;/title&gt;
  &lt;description&gt;&lt;![CDATA[Perform a simple image processing and image statistics computation in Matlab.]]&gt;&lt;/description&gt;
  &lt;version&gt;0.0.0.1&lt;/version&gt;
  &lt;documentation-url&gt;http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/MatlabBridge&lt;/documentation-url&gt;
  &lt;license/&gt;
  &lt;contributor&gt;Andras Lasso (PerkLab)&lt;/contributor&gt;
  &lt;acknowledgements&gt;&lt;![CDATA[SparKit is a project funded by Cancer Care Ontarioand the Ontario Consortium for Adaptive Interventions in Radiation Oncology (OCAIRO) to provide free, open-source toolset for radiotherapy and related image-guided interventions.]]&gt;&lt;/acknowledgements&gt;
  &lt;parameters&gt;
    &lt;label&gt;Processing Parameters&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Parameters for the processing]]&gt;&lt;/description&gt;
    
  &lt;/parameters&gt;
  &lt;parameters&gt;
    &lt;label&gt;IO&lt;/label&gt;
    &lt;description&gt;&lt;![CDATA[Input/output parameters]]&gt;&lt;/description&gt;
    
  &lt;/parameters&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/albagcs/Final-Degree/blob/master/Outliers_step2.xml" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The error for this last outliers_step2 is the following:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f303c8f21fe19b1a633036553329a1021437feb.png" data-download-href="/uploads/short-url/fRClqneoevOz4G4iYeFL7JpseL1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f303c8f21fe19b1a633036553329a1021437feb.png" alt="image" data-base62-sha1="fRClqneoevOz4G4iYeFL7JpseL1" width="690" height="187" data-dominant-color="F8F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">981×267 7.52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much,<br>
Alba</p>

---

## Post #20 by @Alba_Garcia_de_la_Ca (2017-09-17 20:34 UTC)

<p>Could have been code clearer in that way?</p>
<p>Thank you!<br>
Alba</p>

---

## Post #21 by @lassoan (2017-09-18 00:14 UTC)

<p>The generated launcher (.bat or .sh) files are missing from <a href="https://github.com/albagcs/Final-Degree">https://github.com/albagcs/Final-Degree</a>. Could you please upload them?</p>
<p>Also, Outliers_step1.xml and Outliers_step2.xml files are almost empty. You need to specify input and output parameters in these files.</p>
<p>Let me know when you uploaded/updated these files and I have another look.</p>

---

## Post #22 by @Alba_Garcia_de_la_Ca (2017-09-18 16:53 UTC)

<p>Hi!</p>
<p>.sh files are already in the repository !</p>
<p>Yes, they are empty because I do not need any input parameter. I made another module which worked and it also had empty input and output. Dou you think it could be the problem?</p>
<p>Thank you so much!<br>
Nice day,<br>
Alba</p>

---

## Post #23 by @Alba_Garcia_de_la_Ca (2017-09-20 22:11 UTC)

<p>Hi!</p>
<p>Have you seen anything weird in that .sh files? I guess the problem is not there, but I am not 100% sure.</p>
<p>Nice day!<br>
Alba</p>

---

## Post #24 by @lassoan (2017-09-21 01:14 UTC)

<p>The .sh files look fine.</p>
<p>Your algorithm need input files, but you hardcode the input paths in your instead of getting it from Slicer. It should not cause any trouble other than your module is not usable in general, just for those fixed inputs. You can leave those for now.</p>
<p>However, your module must return something that Slicer. What outputs your module generates that you would like to show in Slicer?</p>
<aside class="quote no-group" data-username="Alba_Garcia_de_la_Ca" data-post="19" data-topic="314">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alba_garcia_de_la_ca/48/181_2.png" class="avatar"> Alba_Garcia_de_la_Ca:</div>
<blockquote>
<p>it stays running and no ends until I stop manually the module in Slicer</p>
</blockquote>
</aside>
<p>Make sure the module is called and the computation is completed. Do step-by-step debugging as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge#Troubleshooting" class="inline-onebox">Documentation/Nightly/Extensions/MatlabBridge - Slicer Wiki</a></p>

---

## Post #25 by @Alba_Garcia_de_la_Ca (2017-09-23 12:37 UTC)

<p>Hi!</p>
<p>Yes, I know it is not usable in general but my concrete case now, I am working on that when the basic process is working fine.</p>
<p>My module <strong>Outliers_step1</strong> should generate arrays which indicate what volumes should user discard in his/her algorithm.</p>
<p>My module <strong>Outliers_step2</strong> has the following outputs:</p>
<pre><code>%rejected due to over deformation.
%outlierst2 are the volumes after outlier rejection
%regmask: updated mask showing corrected region with 1 and outlier voxels
%with 2, outlier: number of outlier voxels for each time frame,
%smoothmask:original mask
</code></pre>
<p>I have recorded a video showing the debugging for Outliers_step1, I do not understand why it is stopped at that point, no error is showed, it just stays running in loop:</p>
<div class="lazyYT" data-youtube-id="-72yaxu-Wmk" data-youtube-title="debug" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>I am working with another changes in Outliers_step2</p>
<p>Thank you so much,<br>
Nice day!<br>
Alba</p>

---

## Post #26 by @lassoan (2017-09-23 18:47 UTC)

<p>The video was very useful. Unfortunately, you stooped the step-by-step debugging before getting to the code line that took a very long time to complete. Could you post a video that shows which line exactly takes so long? Use the “step into” debug command to follow step into the called methods.</p>

---

## Post #27 by @Alba_Garcia_de_la_Ca (2017-09-24 21:52 UTC)

<p>I am glad it was useful!</p>
<p>Here is the other video.  I added a new breakpoint and I saw the line which takes so long is the 23, but I do not why because it is just to extract size and assign parameters matrix and detJgw is properly created (it did not give an error on the command line when with the step in debugging when creating detJgw matrix ):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bd4f82a519241c2c4e77f0eee7b849b71c451be.png" data-download-href="/uploads/short-url/1GFxiembjIJM1J5zK1TeDWguVu6.png?dl=1" title="debug" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd4f82a519241c2c4e77f0eee7b849b71c451be_2_690x387.png" alt="debug" data-base62-sha1="1GFxiembjIJM1J5zK1TeDWguVu6" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd4f82a519241c2c4e77f0eee7b849b71c451be_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0bd4f82a519241c2c4e77f0eee7b849b71c451be_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bd4f82a519241c2c4e77f0eee7b849b71c451be.png 2x" data-dominant-color="CBCDD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">debug</span><span class="informations">1366×768 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The video is as the other one but showing the error in line 23:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Qv5hcyBi6cw" data-video-title="debug2" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Qv5hcyBi6cw" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Qv5hcyBi6cw/hqdefault.jpg" title="debug2" width="" height="">
  </a>
</div>

<p>Thank you so much!</p>
<p>Nice day,<br>
Alba</p>

---

## Post #28 by @lassoan (2017-09-25 03:43 UTC)

<p>Thanks for the additional information. Based on the video we still only know that the long computation is somewhere between line 23 and line 27. Instead of clicking on “Continue” button (that runs until you hit the next breakpoint), you should have kept clicking “Step in” (that executes the next command, stepping inside any function that is called). That would have taken you to the exact line of code that takes so long to compute. What is the size of your data set that you load into Matlab?</p>

---

## Post #29 by @Alba_Garcia_de_la_Ca (2017-09-28 06:25 UTC)

<p>Hi!</p>
<p>It seems I have finally achieved it!. The error was I was creating my detJgw with size (110,110,80,82) but I was performing a little example by not using all the volumes in my data set (82) so I changed the size here to (110,110,80,3) and it worked. Now I am trying to execute the module with all my volumes.</p>
<p>I am dealing with outliers_step 2 module, I am investigating more about why it still fails.</p>
<p>Thank you so much!<br>
Nice day,<br>
Alba</p>

---
