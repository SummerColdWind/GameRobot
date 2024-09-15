# Bot 语法

> `GameRobot`设计的初衷就是`简单`，如果您之前有过任何语言的编程基础，那么可以无障碍地上手Bot语法。
即使您之前从未接触过编程语言，阅读完本文档后也可以完全精通此语法。

<hr>

### 1.快速上手

`bot`语法的基本格式为`method arg1=value1 arg2=value2 ...`

`method`是需要调用的方法，例如打印的`print`，鼠标点击的`mouse_click`，抓取句柄的`handle`和截图的`capture`等等

方法的具体参数应查看相应插件的文档

示例代码
```bot
handle title="记事本"
handle_child cls="RichEditD2DPT"
capture save="notepad"
ocr image="notepad" save=ocr
print text=$ocr
```
 - 第一行: 使用`handle`方法获取了标题为`记事本`的窗口句柄
 - 第二行: 使用`handle_child`方法获取了之前的父窗口中，类名为`RichEditD2DPT`的子窗口句柄
 - 第三行: 对子窗口截图，将截图保存名为`notepad`的变量
 - 第四行: 使用`ocr`方法对图片变量`notepad`进行文字识别，然后将识别结果保存名为`ocr`的变量
 - 第五行: 使用`print`方法打印变量`ocr`的内容到控制台

`$var`的意思是获取名为`var`的变量的值。事实上，很多方法都有`save`参数，表明将结果保存的变量名称

使用`exec`方法来执行原生`Python`语句，并且命名空间与`bot`同步，例如：

```bot
exec a = "Hello, GameRobot!"
print text=$a
```

或者同时执行多行语句：
```bot
exec
    a = 10
    for i in range(a):
        print(i)
end
```
当语句结束时，使用`end`标识，否则会引发意料之外的错误

`GameRobot`不存在语法检查，也不存在错误提示，它假定每个用户执行的`bot`脚本都是正确的



### 2.条件控制
```bot
if $boolean
    print text="You did."
else
    print text="False"
done
```
使用`if`方法完成判断逻辑，其语法为`if`后跟随变量`$var`，后续为条件符合时执行的语句，直至`else`

`else`后为条件不符合时执行的语句，直至`end`

同样的，`end`标志着一个判断语句的结束。

### 3.循环语句
```bot
for 10
    print text="Hi"
end
    
while boolean
    print text="Hello"
    sleep duration=1000
end
```
使用`for`方法完成固定次数的循环，使用`while`方法完成条件循环

`while`后跟随`变量名`，没有`$`


## bot语法的本质是什么？

本质上，`GameRobot`解释器会先将纯文本的`bot`脚本解析为`json`格式，
由`Python`读取后的格式为`list[dict[str, Any]]`，即字典组成的列表，
然后循环或者递归解析每一个字典

这些字典的格式应该为`{'type': 'any_str', **kwargs}`，`type`指明了调用的方法

## 我该如何知道这些方法的参数是什么？

本项目的文档还在建设中。内置插件:
 - base
 - [window](../plugins/window/window.md)
 - capture
 - [mouse](../plugins/mouse/mouse.md)
 - [keyboard](../plugins/keyboard/keyboard.md)
 - image
 - ocr
 - ddt

## 没有我想要的功能怎么办？

`GameRobot`只实现了一些基本的功能，并且还在开发当中，您可以通过编写[插件](bot%20plugin.md)来自由地实现更多功能


