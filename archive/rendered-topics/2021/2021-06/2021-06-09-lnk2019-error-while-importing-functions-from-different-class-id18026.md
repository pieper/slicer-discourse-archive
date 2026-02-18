# LNK2019 error while importing functions from different class

**Topic ID**: 18026
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/lnk2019-error-while-importing-functions-from-different-class/18026

---

## Post #1 by @trash_imp (2021-06-09 04:30 UTC)

<ul>
<li>
<p>I wanted to access the functions in <code>qSlicerApplication</code> and <code>qSlicerLayoutManager</code> in <code>qMRMLThreeDViewControllerWidget</code> class.</p>
</li>
<li>
<p>when a Button in <code>qMRMLThreeDViewControllerWidget</code> is clicked an action <code>ViewLayoutOneUp3DAction</code> should be triggred.</p>
</li>
<li>
<p>Includes:</p>
</li>
</ul>
<pre><code class="lang-auto">#include "../../../Base/QTGUI/qSlicerApplication.h"
#include "../../../Base/QTGUI/qSlicerLayoutManager.h"
</code></pre>
<ul>
<li>code for QToolButton in <code>qMRMLThreeDViewControllerWidget.cxx</code> :</li>
</ul>
<pre><code class="lang-auto">  void qMRMLThreeDViewControllerWidgetPrivate::init()
{
  Q_Q(qMRMLThreeDViewControllerWidget);
  this-&gt;Superclass::init();

  q-&gt;setupMenuActions();

  this-&gt;CenterToolButton = new QToolButton(q);
  this-&gt;CenterToolButton-&gt;setAutoRaise(true);
  this-&gt;CenterToolButton-&gt;setDefaultAction(this-&gt;ViewLayoutOneUp3DAction);
  this-&gt;CenterToolButton-&gt;setFixedSize(15, 15);
  this-&gt;BarLayout-&gt;insertWidget(2, this-&gt;CenterToolButton); 
}

void qMRMLThreeDViewControllerWidget::setupMenuActions() {
    Q_D(qMRMLThreeDViewControllerWidget);
    d-&gt;ViewLayoutOneUp3DAction-&gt;setData(vtkMRMLLayoutNode::SlicerLayoutOneUp3DView);
}

void qMRMLThreeDViewControllerWidgetPrivate::setupPopupUi()
{
  Q_Q(qMRMLThreeDViewControllerWidget);

  this-&gt;Superclass::setupPopupUi();

QObject::connect(this-&gt;ViewLayoutOneUp3DAction, SIGNAL(triggered(QAction*)),
                   q, SLOT(ThreeDViewOnly(QAction*)));
}

void qMRMLThreeDViewControllerWidget::ThreeDViewOnly(QAction* action)
{
    this-&gt;setLayout(action-&gt;data().toInt());
}

void qMRMLThreeDViewControllerWidget::setLayout(int layout)
{
    qSlicerApplication::application()-&gt;layoutManager()-&gt;setLayout(layout);
}
</code></pre>
<ul>
<li>Declaration in  <code>qMRMLThreeDViewControllerWidget.h</code>:</li>
</ul>
<pre><code class="lang-auto">Public slots:
 virtual void ThreeDViewOnly(QAction* action);
 virtual void setLayout(int);

protected:
    virtual void setupMenuActions();

</code></pre>
<ul>
<li>Error encountered:</li>
</ul>
<pre><code class="lang-auto">![Screenshot (326)|690x153](upload://eRFkvTJKPRV2gd3jRz8SeWJR7VS.png)
</code></pre>

---

## Post #2 by @lassoan (2021-06-09 04:46 UTC)

<p>MRML is an independent library from Slicer. You cannot call any qSlicer… classes from qMRML… classes, because MRML does not know about Slicer. The original reason to keep MRML library independent from Slicer is to allow building other applications from it, but this modulatization also makes the code easier to maintain and for example distribute MRML as an independent Python package.</p>
<p>This just means that you are not allowed to call Slicer methods from MRML classes, but you can still emit events from MRML classes that the application can process. See for example how node editing is implemented (search for <code>nodeedit</code> in the Slicer source code).</p>
<p>I guess you are trying to implement the <a href="https://github.com/Slicer/Slicer/issues/1409">maximize view</a> feature. We would like to have this in Slicer core and it would be great if you could contribute it - it would save us implementation time and it would save you maintenance time. Temporarily maximizing a view could be implemented as a function in the layout manager: when the maximize button is clicked in a view controller then the layout manager would hide (not remove) all the other view widgets, which would make the selected view widget take the entire layout space. <code>qMRMLLayoutManager</code> is in MRML, so you would probably you could use direct methods calls (would not need to communicate through events).</p>

---

## Post #3 by @lassoan (2021-06-12 13:17 UTC)

<p>10 posts were split to a new topic: <a href="/t/add-button-to-maximize-view/18092">Add button to maximize view</a></p>

---
