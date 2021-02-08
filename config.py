import configparser

config = configparser.ConfigParser()
config["server"] = {}
config["bot"] = {}

config["server"]["host"] = input("(1/4) IP: ")
config["server"]["port"] = input("(2/4) Port: ")
config["server"]["channel"] = input("(3/4) Channel: ")
config["bot"]["username"] = input("(4/4) Bot username: ")

with open("configuration.ini", "w") as config_file:
    config.write(config_file)
