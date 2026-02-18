# How to rotate OrthogonalSlicesDeg in slices?

**Topic ID**: 20892
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/how-to-rotate-orthogonalslicesdeg-in-slices/20892

---

## Post #1 by @jumbojing (2021-12-02 23:27 UTC)

<p>在插件中,我用Ctrl + Alt + Left-click-and-drag在不同的Slice里找到了一个合适vector, 我想移动这个vector, 想了很多方法都不理想, 其中包括:<a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L275-L303" rel="noopener nofollow ugc">rotateOrthogonalSlicesDeg</a>, 可是这个方法,只能在一个Slice里面旋转,当我改变Slice后,原来那个slice的角度就归零了…谁有好的方法帮我?</p>
<blockquote>
<p>In my plug-in, I used Ctrl + Alt + Left-click-and-drag to find a suitable vector(include position and angle) from different slices. I wanted to move this vector’s position and keep its angle, I had try to some methods, but not ideal, for example: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L275-L303" rel="noopener nofollow ugc">rotateOrthogonalSlicesDeg</a>, but this method can only be rotated in a slice,  when I change the angle in another slice, the angle of  the previous slice reset…Who has a good way to help me?</p>
</blockquote>

---

## Post #2 by @jumbojing (2021-12-02 23:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>我的具体思路是: 通过Ctrl + Alt + Left-click-and-drag的方法, 找到一个矢量, 返回并保存这个矢量的位置和在三个slice(RAS) 角度, 利用<a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L275-L303" rel="noopener nofollow ugc">rotateOrthogonalSlicesDeg</a> 找回这个视图,</p>
<blockquote>
<p>My specific idea is: Find a vector by Ctrl + Alt + Left-click-and-drag from slices, return and save the position of this vector and the angle of the three slices (RAS), use the <a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L275-L303" rel="noopener nofollow ugc">rotateOrthogonalSlicesDeg</a>   to retrieve this vector views (sense) or  move this vector’s position and succeed its angle…</p>
</blockquote>

---

## Post #3 by @jumbojing (2021-12-03 23:07 UTC)

<p>好吧…我自己解决了这个问题…贡献我的代码:<br>
From:<a href="https://github.com/SlicerHeart/SlicerHeart/blob/76572a78835e657e01d576af0f82d5729867b6b7/ValveAnnulusAnalysis/HeartValveLib/ValveModel.py#L967-L1021" rel="noopener nofollow ugc">setSlicePositionAndOrientation</a></p>
<pre><code class="lang-auto">  def orthoReset(PIP,nor,ax):

    RNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
    YNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeYellow")
    GNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeGreen")
    # Rslice
    RNode.SetSliceToRASByNTP(-nor[0][0],-nor[0][1],-nor[0][2], 
                             -ax[0][0],-ax[0][1],-ax[0][2], 
                             PIP[0], PIP[1], PIP[2], 0)

    YNode.SetSliceToRASByNTP(-nor[2][0],-nor[2][1],-nor[2][2], 
                             -ax[2][0],-ax[2][1],-ax[2][2], 
                             PIP[0], PIP[1], PIP[2], 0)

    GNode.SetSliceToRASByNTP(-nor[1][0],-nor[1][1],-nor[1][2], 
                             -ax[1][0],-ax[1][1],-ax[1][2], 
                             PIP[0], PIP[1], PIP[2], 0)
    return True
</code></pre>
<p>其中, ax和nor通过<code>GetSliceToRAS</code>获取,其中ax为第一列, nor为第三列,比如:</p>
<pre><code class="lang-auto">    axialSliceToRas = axialNode.GetSliceToRAS()
    axR = [
        axialSliceToRas.GetElement(0, 0),
        axialSliceToRas.GetElement(1, 0),
        axialSliceToRas.GetElement(2, 0),
    ]
    norR = [
        axialSliceToRas.GetElement(0, 2),
        axialSliceToRas.GetElement(1, 2),
        axialSliceToRas.GetElement(2, 2),
    ]
    x1 = [
        axialSliceToRas.GetElement(0, 3),
        axialSliceToRas.GetElement(1, 3),
        axialSliceToRas.GetElement(2, 3),
    ]
</code></pre>
<p>From:<a href="https://github.com/SlicerHeart/SlicerHeart/blob/5be64b4b68fcbfbdc7ed463913f52a74208b6d07/ValveView/ValveView.py#L213-L273" rel="noopener nofollow ugc">getPlaneIntersectionPoint</a></p>

---
