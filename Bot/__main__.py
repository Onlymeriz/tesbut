from Bot import *



app.run()
for all_module in ALL_MODULES:
        importlib.import_module("Bot.modules" + all_module)