# iPhone_quickly

在 Mac 上使用 iPhone 镜像玩游戏
<br/>
通过按键映射操控手机游戏
<br/>
当前示例为通过操控 iPhone 镜像玩游戏

### 文件结构
```
|- src
    |- game_board.py # 激活游戏满班
    |- keyboard_listener.py # 按键监听
    |- keyboard_mappings.py # 按键映射
    |- mian.py # 程序入口
    |- mouse_ctrl.py # 鼠标控制
```

### 环境
```
    MacOS
    Python3
    所有坐标都是当前应用程序的坐标
```


### 使用方法
```
python main.py
```

### 坐标矫正
修改 keyboard_mappings.py 中的坐标
```
    button_attr: 拖动技能
    key_mappings: 点击技能
```
程序启动后可以通过数字按键 0 获取当前鼠标所在位置(相对于当前应用的位置)


