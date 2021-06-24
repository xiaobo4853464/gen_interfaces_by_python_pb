from copy import deepcopy

TYPE_CPP2PY = {
    7: "bool",
    5: "float",
    8: "ENUM",
    6: "float",
    1: "int",
    2: "int",
    # 10: "Message",
    10: "list",
    9: "str",
    3: "int",
    4: "int"
}


def _type_converter(_type_num: int):
    """

    :param _type_num: protobuf标准提供的cpp_type标识
    :return:对应的python类型
    """
    return TYPE_CPP2PY[_type_num]


class MessageCaller:
    """
        protobuf message映射表：支持简单message类型，复杂message类型，map类型，enum类型
    """

    def __init__(self, pb):
        """

        :param pb: pb2.py内容 file描述符
        """
        self.package = ""
        self.org_messages = pb.DESCRIPTOR.message_types_by_name.values()  # message列表
        self.org_enum = pb.DESCRIPTOR.enum_types_by_name.values()  # enum列表
        self.enum_map = dict()  # 枚举字典
        self.messages_map = dict()  # message字典
        self._message_register()  # 信息初始化

    def _message_register(self):
        """
        按顺序优先BSF，全局信息获取不到的再DFS
        """
        # message类型处理
        # 先注册message
        for item in self.org_messages:
            self.messages_map[item.name] = {"name": item.name}
        for item in self.org_messages:
            _fields = self._fields_processor(item.fields)

            self.messages_map[item.name] = {"name": item.name, "type": "Message", "fields": _fields}
        # print(self.messages_map)
        # enum类型处理
        for item in self.org_enum:
            # print(item.name)
            temp = (item.values_by_name.values())

            _value_list = []
            for _item in temp:
                # print(_item.name)
                _value_list.append(_item.name)
            self.enum_map[item.name] = {"name": item.name, "type": "ENUM", "enum_value": _value_list}
        # print(self.enum_map)

    def _fields_processor(self, _fields):
        """
        BSF建立映射
        :param _fields: 指定 message 的参数域 fields 描述符
        """
        _fields_list = []
        for item in _fields:
            # 简单message，只由基本类型组成
            if not item.message_type:
                _fields_list.append(
                    {item.name if not item.message_type else item.message_type.name: _type_converter(item.cpp_type)})
            # 复杂类型，嵌套其他message构成，并且已经存在于message字典中
            elif item.message_type.name in self.messages_map:
                _fields_list.append({item.message_type.name: _type_converter(item.cpp_type)})
            # 如果检测map中检测不到对应类型，转 DFS 递归建立
            elif item.message_type.name not in self.messages_map:
                # _temp = complex_message_parser(item.message_type)
                self._inside_message_processor(item.message_type)
                # print(_temp)
            else:
                print("what?" + item.name)
        return _fields_list

    def _inside_message_processor(self, _message):
        """
        message DFS 解决_message_register中全局信息不足的问题
        :param _message:需要递归解析的message（描述符）
        """
        if not _message:
            return
        else:
            _temp_dict = dict()
            _temp_dict['name'] = _message.name
            _temp_dict['fields'] = []
            try:
                for _item in _message.fields:
                    if _item.message_type:
                        if _item.message_type.name not in self.messages_map:  # 参数列表中 出现message字典中不存在的message，递归解析
                            self._inside_message_processor(_item)
                        _temp_dict['fields'].append({_item.message_type.name: _type_converter(_item.cpp_type)})
                    else:
                        _temp_dict['fields'].append({_item.name: _type_converter(_item.cpp_type)})
                self.messages_map[_message.name] = _temp_dict
            except Exception as EA:
                print(EA)
            print("dfs:", _temp_dict)
            return _temp_dict

    def all_message(self):
        """

        :return: 包含enum和message的总字典
        """
        __temp = deepcopy(self.messages_map)
        __temp.update(self.enum_map)
        return __temp

    def find_message_by_name(self, name):
        """

        :param name: 需要查询的message或enum
        :return:查询到的message或enum字典
        """
        __temp = self.all_message()
        try:
            _cursor = __temp[name]
        except Exception as EA:
            print(EA, "\n", name + "not found!")
            return
        return _cursor


class ServiceCaller:
    def __init__(self, pb):
        """
        auto load service and message parser
        :param pb: pb file
        """
        self.service_dict = dict()
        self.message_dict = dict()
        self.proto_org = pb
        self._message_parser()
        self._service_parser()

    def call_all_services(self) -> dict:
        """

        :return: 返回所有service的总字典
        """
        return self.service_dict

    def call_service_name(self) -> str:
        t = self.proto_org.DESCRIPTOR.package
        parts = handle_for_service_name(t)
        return ".".join(parts)

    def call_service_by_name(self, name):
        """

        :param name: service名称字符串
        :return:特定service的描述字典
        """
        temp = self.service_dict.get(name)
        if len(temp) == 0:
            print("ERR in getting service")
        return temp

    def call_all_messages(self):
        """

        :return: 返回所有message（递归化）
        """
        return self.message_dict

    def call_message_by_name(self, name):
        """

        :param name: message名称字符串
        :return: 特定message的描述字典
        """
        try:
            temp = self.message_dict[name]
            return temp
        except AttributeError as e:
            print(e)
            return None

    def _service_parser(self):
        """
        产生services字典

        :return: service字典，生成到对象中 ||

        dict结构：
        {
            name:str,
            full_name:str,
            input:list,
            output:list
        }
        """
        _all_services_dict = dict()
        _temp_service = self.proto_org
        for item in _temp_service.DESCRIPTOR.services_by_name.values():

            for _item in item.methods:
                _in_paras = []
                _out_paras = []

                _temp_service_dict = dict()
                _temp_service_dict['name'] = _item.name
                # _temp_service_dict['full_name'] = str(_item.full_name).replace('Package.', 'Package/')
                # 替换
                temppath = str(_item.full_name).replace('Package.', 'Package/')
                temp = temppath.split(".")
                temp.pop(-1)
                pre = ".".join(temp)
                _temp_service_dict['full_name'] = f"{pre}/{_item.name}"
                # 替换

                # 遍历service解析 输入 输出 参数
                for _item_in in _item.input_type.fields:
                    tag = 'required' if 'required' in _item_in._serialized_options.decode(errors='ignore') else 'optional'
                    _in_paras.append({_item_in.name: (_type_converter(_item_in.cpp_type), tag)})
                for _item_out in _item.output_type.fields:
                    tag = 'required' if 'required' in _item_out._serialized_options.decode(errors='ignore') else 'optional'
                    _out_paras.append({_item_out.name: (_type_converter(_item_out.cpp_type), tag)})
                _temp_service_dict['input'] = _in_paras
                _temp_service_dict['output'] = _out_paras
                _all_services_dict[_item.name] = _temp_service_dict
            # print(_all_services_dict)
            self.service_dict = _all_services_dict

    def _message_parser(self):
        _temp_message_dict = dict()
        _temp_message = self.proto_org.DESCRIPTOR.message_types_by_name.values()
        for item in _temp_message:
            _temp = complex_message_parser(item, item.name)
            _temp_message_dict[item.name] = _temp
        self.message_dict = _temp_message_dict


def complex_message_parser(_message, upstream_name="", enable_instance_name=True):
    """

    :param enable_instance_name: 是否启用实例化名称
    :param upstream_name: 需要继承的上游名称
    :param _message: protobuf message 描述符
    :return: dict(message)
    """
    if not _message:
        return
    else:
        _temp_dict = dict()
        # upstream_name继承调用者name，解决name字段存在的类型名问题，全部替换为实例名
        if upstream_name and enable_instance_name is True:
            _temp_dict['name'] = upstream_name
        else:
            _temp_dict['name'] = _message.name
        _temp_dict['fields'] = []
        try:
            for _item in _message.fields:
                # if _item.message_type:
                #     _temp_dict['fields'].append(
                #         complex_message_parser(_message=_item.message_type, upstream_name=_item.name))  # 递归解析
                # else:
                #     _temp_dict['fields'].append({_item.name: _type_converter(_item.cpp_type)})

                # 只要一层
                # _temp_dict['fields'].append({_item.name: _type_converter(_item.cpp_type)})

                tag = 'required' if 'required' in _item._serialized_options.decode(errors='ignore') else 'optional'
                _temp_dict['fields'].append({_item.name: (_type_converter(_item.cpp_type), tag)})
                # 先读取cpp_type
                # 再通过映射生成python类型
        except AttributeError as EA:

            print('ERR:', EA)
        return _temp_dict


def handle_for_service_name(name):
    temp = name.split(".")
    t_str = temp[-1]
    idx = t_str.rfind("v")
    if idx != -1 and t_str[idx + 1:].isdigit():
        temp.remove(t_str)
    return temp

# def nested_parser():
#     """
#
#     :return: 嵌套类型字典
#     """
#     __temp = data.api_pb2.DESCRIPTOR.message_types_by_name.values()
#     for item in __temp:
#         __temp = item.nested_types_by_name.values()
#         if __temp:
#             for _item in __temp:
#                 # print(_item.name)
#                 _temp_dict = complex_message_parser(_item)
#                 # print(_temp_dict)
#
#
# def messages_reader(pb=data.api_pb2):
#     """
#
#     :param pb: pb2.py file描述符 (test_default=data.api_pb2)
#     :return: dict(pb)
#     """
#     _message_dict = dict()
#     temp_message = pb.DESCRIPTOR.message_types_by_name.values()
#     for item in temp_message:
#         _temp = complex_message_parser(item, enable_instance_name=False)
#         _message_dict[item.name] = _temp
#     return _message_dict


# if __name__ == "__main__":
#     pc = PbCaller(data.api_pb2)
#     print(pc.call_all_services())
#     print(pc.call_service_by_name("CreatePackage"))
# mp = MessageMap(data.api_pb2)
# _temp = mp.all_message()
# print(_temp)
# print(mp.find_message_by_name("UploadMode"))
