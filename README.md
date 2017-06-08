# cocoa_package




该脚本是cocoapods打包类库cocoapods-packager的一个延伸，提供了更方便快捷的操作方式。
简化操作过程，运行该脚本并选择的打包方式如lib,framework，即可打出相应的包。相应的子模块也会生成对应的子包。

# 运行环境：
    python 2.7


## 运行该脚本的前期工作
安装cocoapods的插件[cocoapods-packager](https://github.com/CocoaPods/cocoapods-packager)
```sh
sudo gem install cocoapods-packager
```
cocoapods_packager的使用操作可以前往[cocoapods-packager](https://github.com/CocoaPods/cocoapods-packager)github学习。

## 使用说明
打开命令终端，切换到.podspec文件所在文件夹下
执行
```sh
python cocoa_package.py
```
或者进行工具有安装：
```sh
pip install cocoa_packer

```
安装完后，执行 cocoa_packer
将会得到一个命令行的交互界面，选择要打包的格式
```
 please check package method

 => library
    framework

```
选择完后，就先去喝杯咖啡，回来，就已经打好了。

