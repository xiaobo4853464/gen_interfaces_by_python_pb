# KUNNKA
## 直播接口自动化生成每个服务的调用对象
### 步骤：
1. python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. data/dm.proto # 生成python pb描述文件
2. 执行