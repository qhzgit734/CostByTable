# Python环境配置

## Miniconda

1. 下载安装
[https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/?C=M&amp;O=D](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/?C=M&O=D)  
管理员运行安装，安装时选all users，不添加环境变量。安装完，在高级系统设置中添加系统环境变量

|变量名|path|path|path|
|------|----|----|----|
|变量值|D:\soft\Miniconda|D:\soft\Miniconda\Scripts|D:\soft\Miniconda\Library\bin|

2. 使用powershell需初始化conda:
`conda init powershell`
3. 去除powershell（base)环境默认启动
`conda config --set auto_activate_base False`
4. 生成.condarc文件
`conda config --set show_channel_urls yes`
5. conda配置镜像地址
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
```

## Python编译器
