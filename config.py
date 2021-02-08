import configparser

config = configparser.ConfigParser()
config["server"] = {}
config["bot"] = {}

config["server"]["host"] = input("(1/3) IP: ")
config["server"]["port"] = input("(2/3) Port: ")
config["bot"]["username"] = input("(3/3) Bot username: ")

with open("configuration.ini", "w") as config_file:
    config.write(config_file)
