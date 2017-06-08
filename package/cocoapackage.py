#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/7 下午3:56
# @Author  : 袁平华
# @Site    : 
# @File    : cocoapackage.py
# @Software: PyCharm Community Edition

'''依据cocoapods的spec文件生成所有spec 或者subspec的framework'''

import os
import re
import shutil
import sys

from  pick import pick

rootdir = os.getcwd ( )


# rootdir = '/Users/yuanpinghua/Desktop/GPUImage/GPUImage'

def auto_recogonize_spec_file():
    """
    读取当前spec文件路径
    :return: spec ,path
    """
    for root, dirs, files in os.walk (rootdir):
        for file in files:
            if os.path.splitext (file)[1] == '.podspec':
                print(os.path.join (root, file))
                return os.path.splitext (file)[0], os.path.join (root, file)
    return None, None


def auto_analysis_spec(specfile):
    """
    识别spec里的所有subpec,如果没有sub，直接返回主spec
    :param specfile: spece文件路径
    :return: list 数组
    """
    with open (specfile, 'r') as file:
        spec = []
        for line in file.readlines ( ):
            if '.subspec' in line:
                line = line.replace ("'", '"')
                match = re.findall (ur'\s+"(\w+)"\s+', line)
                if match is not None:
                    spec.append (match[0])
                print (line)

    return spec


def auto_extract_version(specfile):
    """
    提取cocoapods文件的version
    :param specfile:文件路径
    :return:版本号
    """
    with open (specfile, 'r')as file:
        for line in file.readlines ( ):
            if '.version' in line:
                line = line.replace ("'", '"')
                version = re.findall (ur'"([0-9.]*)"', line)[0]
                return version


def auto_copy_rename_framewok(frameworkpath, subspec_name):
    """
    移动生成好的framework，并重新命名
    :param frameworkpath: framework路径
    :param subspec_name: 新的framework名字
    :return: 
    """
    findit = False
    path = None
    contentlist = os.listdir (frameworkpath)
    for item in contentlist:
        if os.path.splitext (item)[1] == '.framework':
            path = os.path.join (frameworkpath, item)
            findit = True
            break

    if findit:
        shutil.move (path, os.path.join (os.getcwd ( ), subspec_name + '.framework'))


def auto_copy_rename_lib(libpath, subspec_name):
    """
    移动生成好的library，并重新命名
    :param libpath:library路径
    :param subspec_name:新的名字
    :return:
    """
    findit = False
    path = None
    for root, dirs, files in os.walk (libpath):
        for file in files:
            if os.path.splitext (file)[1] == '.a':
                path = os.path.join (root, file)
                findit = True
                break
        if findit:
            break

    if findit:
        shutil.move (path, os.path.join (os.getcwd ( ), subspec_name + '.a'))


def auto_package_spec(type, spec, subspce):
    """
    开始打包
    :param type: .a ／framework
    :param spec:  spec 名字
    :param subspce: subspec名字
    :return:
    """
    # assert (type is None,"fdsafasdf")fdsafasdf
    if type == '.a':
        if subspce:
            cmd = 'pod package %s --library --force --subspecs=%s ' % (spec, subspce)
        else:
            cmd = 'pod package %s --library --force'

    else:
        if subspce:
            cmd = 'pod package %s  --force --subspecs=%s ' % (spec, subspce)
        else:
            cmd = 'pod package %s  --force'

    print (cmd)
    status = os.system (cmd)
    return status


def auto_create_lib():
    """
    生成library
    :return:
    """
    specname, specfile = auto_recogonize_spec_file ( )
    if specfile is None:
        print ("Can't find .podspec file")
        sys.exit (1)

    sublist = auto_analysis_spec (specfile)
    version = auto_extract_version (specfile)
    if (sublist is not None and len (sublist) > 0):
        for subspec in sublist:
            status = auto_package_spec ('.a', specfile, subspec)
            print  ("status = %s" % (status))
            if status == 0:
                libpath = os.path.join (os.path.join (os.getcwd ( ), specname + '-' + version), 'ios')
                auto_copy_rename_lib (libpath, specname + '_' + subspec)
            else:
                print ('package failed')
    else:
        auto_package_spec ('.a', specfile, None)
        libpath = os.path.join (os.path.join (rootdir, specname + '-' + auto_extract_version (specfile)), 'ios')
        auto_copy_rename_lib (libpath, specname)


def auto_create_framework():
    """
    生成framework
    :return:
    """
    specname, specfile = auto_recogonize_spec_file ( )
    if specfile is None:
        print ("Can't find .podspec file")
        sys.exit (1)

    sublist = auto_analysis_spec (specfile)
    version = auto_extract_version (specfile)
    if (sublist is not None and len (sublist) > 0):
        for subspec in sublist:
            status = auto_package_spec ('.framework', specfile, subspec)
            print  ("status = %s" % (status))
            if status == 0:
                libpath = os.path.join (os.path.join (os.getcwd ( ), specname + '-' + version), 'ios')
                auto_copy_rename_framewok (libpath, specname + '_' + subspec)
            else:
                print ('package failed')
    else:
        auto_package_spec ('.framwork', specfile, None)
        libpath = os.path.join (os.path.join (rootdir, specname + '-' + auto_extract_version (specfile)), 'ios')
        auto_copy_rename_framewok (libpath, specname)


if __name__ == '__main__':
    package_method = ['library', 'framework']

    method, index = pick (package_method, "please check package method", indicator='=>')
    if index == 0:
        auto_create_lib ( )
    else:
        auto_create_framework ( )
