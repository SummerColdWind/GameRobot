# Bot 插件


`bot`插件的本质为`plugins`目录下的软件包，实际上，`GameRobot`的内置方法也是由插件实现的

当`GameRobot`试图解析一个字典时，它会遍历每一个插件，直至被匹配，然后执行

让我们开始编写一个`bot`插件，首先在`plugins`目录下创建：
```
├─test
│  ├─__init__.py
│  └─plugin.py
```
编辑`plugin.py`时，你应该：
 - 创建一个名为`Plugin`的类
 - 这个类可以继承`plugins.interface.PluginInterface`
 - 或者，不继承此抽象类，实现`__repr__`和`perform`方法就够了

> “如果它走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子。”

 - `__repr__`应该提供此插件一个简短的描述，例如：
```python
def __repr__(self):
    return 'A test plugin only.'
```

 - `perform`负责解析字典，然后实现相应的功能
 - 无论如何解析，最终没有匹配时 **必须** 抛出`RuntimeError`，解释器会捕获此错误，然后继续执行下去
