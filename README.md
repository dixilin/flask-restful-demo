# 安装依赖包
```shell
pip install -r requirements.txt
```


## 初始化
### MacOS/Linux
```shell
mkdir myproject
cd myproject
python3 -m venv .venv
```

### Windows
```shell
mkdir myproject
cd myproject
py -3 -m venv .venv
```

## 激活虚拟环境
### MacOS/Linux
```shell
. .venv/bin/activate
```
### Windows
```shell
.venv\Scripts\activate
```

## 数据库模型创建及更新
```shell
# 第一次初始化时使用
flask db init 
# 后面每次修改数据库字段时使用
flask db migrate
flask db upgrade
```

## 项目依赖包导出
```shell
pip freeze -l > requirements.txt
```