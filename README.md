# KUNNKA
## 通过主站的bapis_python 项目中的python proto描述文件生成接口定义代码。
### 步骤：
1. python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. data/dm.proto # 生成python pb描述文件
2. 执行