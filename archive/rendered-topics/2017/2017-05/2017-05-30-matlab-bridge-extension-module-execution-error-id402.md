---
topic_id: 402
title: "Matlab Bridge Extension Module Execution Error"
date: 2017-05-30
url: https://discourse.slicer.org/t/402
---

# Matlab bridge extension - Module execution error

**Topic ID**: 402
**Date**: 2017-05-30
**URL**: https://discourse.slicer.org/t/matlab-bridge-extension-module-execution-error/402

---

## Post #1 by @Marina_CM (2017-05-30 13:39 UTC)

<p>Operating system: iOS10.3.2<br>
Slicer version: 4.6.2<br>
Expected behavior: Matlab module executes properly<br>
Actual behavior: “Completed with errors”</p>
<p>Dear team,</p>
<p>I’m trying to create a Matlab module for Slicer with Matlab Bridge.</p>
<p>I get an error when trying to write the info from a matrix M into the img.pixelData param.<br>
This is a part of the algorithm:</p>
<p>function outputParams=TFG(inputParams)</p>
<p>% Parameters:<br>
%  inputParams.threshold: threshold value<br>
%  inputParams.inputvolume: input image filename<br>
%  inputParams.outputvolume: output image filename, result of the processing<br>
%  outputParams.distancia: points distance</p>
<p>img = cli_imageread(inputParams.inputvolume);</p>
<p><strong>M = img.pixelData;</strong></p>
<p>S = size(M);</p>
<p>img.pixelData = M;<br>
cli_imagewrite(inputParams.outputvolume, img);</p>
<p>I get the error:</p>
<p><strong>expr: syntax error</strong><br>
<strong>Failed to execute Matlab function: TFG, received the following error message:</strong><br>
<strong>ERROR: Command execution failed. Field assignment to a non-structure array object.</strong></p>
<p><strong>Error in TFG (line 102)</strong><br>
<strong>img.pixelData(1) = M;</strong></p>
<p><strong>Error in cli_commandserver (line 91)</strong><br>
<strong>response=evalc(cmd);</strong></p>
<p><strong>Error in run (line 86)</strong><br>
<strong>evalin(‘caller’, [script ‘;’]);</strong></p>
<p>​Do you know how can I fix it?​</p>
<p>​Thank you very much, <img src="https://emoji.discourse-cdn.com/twitter/relaxed.png?v=9" title=":relaxed:" class="emoji" alt=":relaxed:"></p>
<p>King regards,​</p>
<p>Marina C.</p>

---

## Post #2 by @lassoan (2017-05-30 13:55 UTC)

<p>Probably M is processed and its type is changed. Do you modify M? In TFG function, which one is line 102? It seems that you have 20-30 lines here but Matlab complains that the error occurs in line 102.</p>
<p>Could you please add <code>whos('M')</code> after line <code>M = img.pixelData;</code> and also before line <code>img.pixelData = M;</code> and write me what is the output?</p>

---

## Post #3 by @Marina_CM (2017-05-30 16:39 UTC)

<p>Thank you for your quick response Andras <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>I’ve added those whos(‘M’) lines, but I’ve not been able to see any output.</p>
<p>This is the complete code:</p>
<p><strong>img = cli_imageread(inputParams.inputvolume);</strong></p>
<p><strong>M = img.pixelData;</strong><br>
<strong>whos(‘M’)</strong><br>
<strong>S = size(M);</strong><br>
<strong>z = S(3);</strong><br>
<strong>L = [];</strong><br>
<strong>p=1;</strong></p>
<p><strong>for i=1:z</strong><br>
**	if (nnz(M(:,:,i))&gt;1)**<br>
**		L§ = i;**<br>
**		p=p+1;**<br>
**	end**<br>
<strong>end</strong></p>
<p><strong>N = [];</strong></p>
<p><strong>for i=1:p-1</strong><br>
**	n = nnz(M(:,:,L(i)));**<br>
**	N(i, 1) = n;**<br>
**	N(i, 2) = L(i);**<br>
<strong>end</strong></p>
<p><strong>[V, I] = max(N(:,1));</strong><br>
<strong>l = N(I,2);</strong></p>
<p><strong>C = M(:,:, l);</strong><br>
<strong>im = image©;</strong><br>
<strong>img = mat2gray©;</strong><br>
<strong>imbw = im2bw(img, 0.2);</strong></p>
<p><strong>%nonz = find(img);</strong></p>
<p><strong>%close</strong><br>
<strong>originalBW = imbw;</strong><br>
<strong>imshow(originalBW);</strong><br>
<strong>se = strel(‘disk’,10);</strong><br>
<strong>closeBW = imclose(originalBW,se);</strong><br>
<strong>figure, imshow(closeBW)</strong></p>
<p><strong>BW2 = bwmorph(closeBW,‘remove’);</strong><br>
<strong>%figure</strong><br>
<strong>%imshow(BW2)</strong><br>
<strong>[row,col] = find(BW2==true);</strong></p>
<p><strong>%codigo distancia</strong></p>
<p>x = row;<br>
y = col;<br>
count = 1;<br>
distance = [];<br>
for i=1:length(x)-1<br>
for j=1:length(x)<br>
distance(count) = sqrt((x(i) - x(j))^2 + (y(i) - y(j))^2);<br>
Matrix(count, : ) = [x(i) y(i) x(j) y(j) distance(count)];<br>
count = count +1;<br>
end<br>
end<br>
<strong>SortedMatrix = sortrows(Matrix, 5);</strong><br>
<strong>MaxDis = SortedMatrix(size(Matrix, 1), :);</strong><br>
<strong>%fprintf(‘Coordinates of maximum distnace are (x1, y1) = (%d, %d) and (x2, y2) = (%d, %d)\n’, MaxDis(1), MaxDis(2), MaxDis(3), MaxDis(4))</strong><br>
<strong>%fprintf(‘Maximum distance = %d\n’, MaxDis(5))</strong></p>
<p><strong>%Point1 = [MaxDis(1), MaxDis(2)];</strong><br>
<strong>%Point2 = [MaxDis(3), MaxDis(4)];</strong></p>
<p><strong>BW2_int = int16(BW2);</strong></p>
<p><strong>closeBW_int = int16(closeBW);</strong></p>
<p>*<em>multiplica = closeBW_int.<em>BW2_int;</em></em></p>
<p><strong>grupo = find(multiplica);</strong></p>
<p><strong>multiplica(MaxDis(1),MaxDis(2)) = 20;</strong><br>
<strong>multiplica(MaxDis(3),MaxDis(4)) = 20;</strong><br>
<strong>figure</strong><br>
<strong>image(multiplica)</strong><br>
<strong>M(:,:,:)=0;</strong><br>
<strong>M(:,:, l)=multiplica;</strong><br>
<strong>figure</strong><br>
<strong>image(M(:,:,l))</strong></p>
<p><strong>outputParams.distancia=MaxDis(5);</strong></p>
<p><strong>whos(‘M’)</strong><br>
<strong>img.pixelData = M;</strong></p>
<p><strong>%nrrdwrite(inputParams.outputvolume, img);</strong></p>
<p><strong>cli_imagewrite(inputParams.outputvolume, img);</strong></p>
<p>Thank you in advance,</p>
<p>Marina C.</p>

---

## Post #4 by @lassoan (2017-05-30 20:14 UTC)

<p>The problem is that you overwrite <code>img</code> variable in this line:</p>
<pre><code>img = mat2gray(C);
</code></pre>
<p>Choose different name for the temporary variable and it should work well.</p>

---

## Post #5 by @Marina_CM (2017-05-30 21:01 UTC)

<p>Thank you very much for your help, it worked!</p>
<p>I hope to keep learning and be able to help others in the future.</p>
<p>Best regards,</p>
<p>Marina C.</p>

---

## Post #6 by @lassoan (2017-06-02 16:37 UTC)

<p>2 posts were split to a new topic: <a href="/t/relationship-between-pixels-and-mm-from-matlab/427">Relationship between pixels and mm from Matlab</a></p>

---
