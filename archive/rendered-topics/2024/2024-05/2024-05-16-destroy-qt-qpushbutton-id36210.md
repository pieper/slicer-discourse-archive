---
topic_id: 36210
title: "Destroy Qt Qpushbutton"
date: 2024-05-16
url: https://discourse.slicer.org/t/36210
---

# Destroy qt.QPushButton

**Topic ID**: 36210
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/destroy-qt-qpushbutton/36210

---

## Post #1 by @dfajtai (2024-05-16 17:23 UTC)

<p>I have successfully created a module based on the SimpleFilters module. It works fine if I have one “custom” filter. By this, I mean that there is only one element in the<br>
<a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/e82fc598bc010505e994b7ce22d953a9899a175c/SimpleFilters/SimpleFilters.py#L141" rel="noopener nofollow ugc">combo box</a>.</p>
<p>When I add more than one, I need to handle the switching between the different layouts. Emptying the layout is done by calling the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/e82fc598bc010505e994b7ce22d953a9899a175c/SimpleFilters/SimpleFilters.py#L1158" rel="noopener nofollow ugc">destroy</a> function. I implemented the same procedure in a class mimicking the capabilities of the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/e82fc598bc010505e994b7ce22d953a9899a175c/SimpleFilters/SimpleFilters.py#L558" rel="noopener nofollow ugc">FilterParameters</a> class in a… bit duck-taped way.</p>
<p>It worked fine - until I tried to remove a <a href="https://doc.qt.io/qt-6/qpushbutton.html" rel="noopener nofollow ugc">qt.QPushButton</a> type widget. Doing this completely crashes the Slicer, exiting with no trace of the error. Adding ‘try-catch’ can not catch the error. If I execute Slicer from a terminal, all I see is</p>
<pre><code class="lang-auto">Switch to module:  "Welcome"
Switch to module:  "CustomFilters"
Switch to module:  ""
Switch to module:  ""
error: [/local_data/Programs/Slicer-5.2.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #2 by @cpinter (2024-05-17 09:01 UTC)

<p>Qt does not really have a good solution for completely deleting widgets. You may try to do it by removing it from its layout then calling <code>deleteLater()</code>, but I recommend simply hiding it: <code>button.visible = False</code>.</p>

---

## Post #3 by @dfajtai (2024-05-17 11:14 UTC)

<p>The fun part is that I just tried to simulate a similar scenario with a dummy “filter” whose layout contains just a single button, and the crash did not occur. Then, when I started to add more elements, the error occurred in the same way.</p>
<p>This will not cause a crash:</p>
<pre><code class="lang-auto">class DummyFilter(CustomFilter):
  filter_name = "Dummy Filter"
  short_description = "Just a dummy"
  tooltip = "Just a dummy"

  def __init__(self):
    super().__init__()
    self.filter_name = DummyFilter.filter_name
    self.short_description = DummyFilter.short_description
    self.tooltip = DummyFilter.tooltip   
    
  def createUI(self, parent):
    parametersFormLayout = super().createUI(parent)
    UI = CustomFilterUI(parent = parametersFormLayout)

    dummy_btn = qt.QPushButton("Dummy btn")
    UI.widgets.append(dummy_btn)
    
    UI.addWidgetWithToolTip(dummy_btn,{"tip":"Dummy btn clicked"})
    dummy_btn.connect('clicked(bool)', self.on_dummy_btn)
    
    self.UI = UI
    return UI
    
  def on_dummy_btn(self):
      print("Dummy btn clicked")
 
  def execute(self, ui = None):
    super().execute(ui = ui)
</code></pre>
<p>While this will:</p>
<pre><code class="lang-auto">class DummyFilter(CustomFilter):
  filter_name = "Dummy Filter"
  short_description = "Just a dummy"
  tooltip = "Just a dummy"

  def __init__(self):
    super().__init__()
    self.filter_name = DummyFilter.filter_name
    self.short_description = DummyFilter.short_description
    self.tooltip = DummyFilter.tooltip
    
  def createUI(self, parent):
    parametersFormLayout = super().createUI(parent)
    UI = CustomFilterUI(parent = parametersFormLayout)

    dummy_btn = qt.QPushButton("Dummy btn")
    UI.widgets.append(dummy_btn)
    
    UI.addWidgetWithToolTip(dummy_btn,{"tip":"Dummy btn clicked"})
    dummy_btn.connect('clicked(bool)', self.on_dummy_btn)
    
    # clip widget    
    UI.clip_widget = ctk.ctkRangeWidget()
    UI.widgets.append(UI.clip_widget)
    
    UI.addWidgetWithToolTipAndLabel(UI.clip_widget,{"tip":"Values outside the 'clip range' will be set to the given 'clip range'",
                      "label":"Input clip range"})
    UI.clip_widget.enabled = False
    
    UI.clip_widget.connect("valuesChanged(double,double)",
                                lambda min,max, widget=UI.clip_widget, name = 'clip': self.onRangeChanged(name,widget,min,max))
    
    self.UI = UI
    return UI
  
  
    
  def on_dummy_btn(self):
      print("Dummy btn clicked")
      
  def onRangeChanged(self, name, widget, min_val, max_val):
    if name == "clip":
      print(f"clip: {min_val} - {max_val}")
 
  def execute(self, ui = None):
    super().execute(ui = ui)
</code></pre>
<p>Then I noticed, that in my duck-taped code, I forgot to implement storing of the connections made on-flight. Oddly, this will not result in a crush - if there is only one widget on the layout.</p>
<p>So… to make the previously mentioned destroy function work properly, one should make sure that every connection is stored in the widgetConnections list.</p>

---

## Post #4 by @SANTIAGO_PENDON_MING (2025-02-05 07:49 UTC)

<p>Hi, I’ve noticed a very similar problem deleting QPushButtons. The point   in my case is, that sometimes the deleting process  instantly crashes the Slicer App with no TraceBack.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>  my process has too many buttons creations/deletions to be hide I think so, do you find any new way to manage the QPushButton ?</p>
<p><a class="mention" href="/u/dfajtai">@dfajtai</a> what do you refer when you say:</p>
<blockquote>
<p>So… to make the previously mentioned destroy function work properly, one should make sure that every connection is stored in the widgetConnections list.</p>
</blockquote>
<p>My actual code is:</p>
<pre><code class="lang-auto">class SegmentTracerUI:
    def __init__(self):
        self.widgetConnections = []
        slicer.util.mainWindow().setStatusBar(None)
 
        

    def createDockInterface(self, title="ST Assistant"):
        """Crea el dock widget y lo agrega a la interfaz."""
        self.dock_widget = qt.QDockWidget(title)
        self.dock_widget.setObjectName("SegmentTracerDockWidget")
        
        # Contenedor y layout
        dock_content = qt.QWidget()
        self.dock_layout = qt.QVBoxLayout(dock_content)
        
        # Label de bienvenida
        self.label = qt.QLabel("Welcome to SegmentTracer.")
        self.label.setFont(qt.QFont("Times", 11))
        self.dock_layout.addWidget(self.label)
        
        self.dock_widget.setWidget(dock_content)
        slicer.util.mainWindow().addDockWidget(qt.Qt.LeftDockWidgetArea, self.dock_widget)

    def create_button(self, function, text, type, args=[]):
        button = qt.QPushButton(text)
        
        # Guardar la conexión en la lista
        connection = button.clicked.connect(
            lambda: self.on_button_pressed(type, function, args)
        )
        self.widgetConnections.append(connection)
        
        self.dock_layout.addWidget(button)
        slicer.app.processEvents()
        return button


    def fastRemoveButtons(self):
        
        for button, connection in self.widgetConnections:
            button.clicked.disconnect(connection)  # 🔹 Desconectar antes de eliminar
            button.hide()
            self.dock_layout.removeWidget(button)
            button.deleteLater()
        self.widgetConnections.clear()  # 🔹 Vaciar la lista
        slicer.app.processEvents()
</code></pre>
<p>I’m not sure how to solve it right now, so if you have any idea to, at least, not crash the Slicer App it would be great.</p>

---

## Post #5 by @cpinter (2025-02-05 11:47 UTC)

<p>I stick to my former advice. Deletion is of widgets is not something robust, so just hide what you don’t need. If you need to create tens of thousands of buttons then maybe revise the design.</p>

---

## Post #6 by @dfajtai (2025-02-07 13:34 UTC)

<p>I was trying to explain why my sample code kept breaking. I believe the solution was to store every connection in the <code>widgetConnections</code> list. That way, when the <code>destroy</code> function is called, all connections can be properly removed before the <code>Qt.PushButton</code> itself is destroyed.</p>
<p>Does this make sense?</p>

---
