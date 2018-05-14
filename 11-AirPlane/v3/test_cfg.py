import configparser

#第一步生成相应ConfigParser的实例
cfg  = configparser.ConfigParser()

# 生成实例后需要读入相应的配置文件
cfg.read("test_cfg.cfg")

sp_name = cfg.get("SmallPlane", "name")
print(sp_name)

sp_width = cfg.getint("SmallPlane", "width")
print(sp_width)



