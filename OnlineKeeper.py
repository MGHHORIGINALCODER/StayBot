from javascript import *
import time
import threading
import random
mineflayer = require("mineflayer")
pathfinder = require("mineflayer-pathfinder")
                    
class BOT():
    def __init__(self):
        self.MoonWalkB=False
        self.JumpingOn=False
        self.start_bot()
    def MoonWalk(self,bot):
        

        
        
        
        
        
        
        while self.MoonWalkB:

            goal = pathfinder.goals.GoalBlock(random.randint(-64,64), random.randint(64,80), random.randint(-64,64))
                    
                    
            bot.pathfinder.setGoal(goal)

            if not self.MoonWalkB: 
                break

            
            time.sleep(0.5)
    def start_bot(self):
        print("🔌 Connecting bridge to server...")
        bot = mineflayer.createBot({
            "host": "play.akservers.co.uk",
            "port": 25565,
            "username": "gladose199",
            "auth": "offline",
            "version": "1.20.1",             
            "brand": "vanilla",               
            "fakeHost": "play.akservers.co.uk",
            "skipValidation": True,           
            "hideErrors": False
        })
    
    
        
        @On(bot, "spawn")
        def handle_spawn(this):
            print("Spawned!")

        @On(bot, "physicsTick")
        def handle_physics(this):
           
            if bot.entity.isCollidedHorizontally:
                bot.setControlState('jump', True)
                return

        
    
        @On(bot, "chat")
        def handle_chat(this, username, message, translate, jsonMsg):
            if username == bot.username:
                return
    
            print(f"[CHAT] <{username}> {message}")
            if message.startswith("!LoopWalk"):
                if not bot.pathfinder:
                    bot.chat("My pathfinder module is still syncing! Wait 3 seconds and try again.")
                    return
                if not self.MoonWalkB:
                    self.MoonWalkB = True
                    mcData = require('minecraft-data')(bot.version)
                    movements = pathfinder.Movements(bot, mcData)
                    movements.canDig = True  
                    bot.pathfinder.setMovements(movements)
                            
                    threading.Thread(target=self.MoonWalk, args=(bot,), daemon=True).start()
                    bot.chat("Walking :3")
                else:
                    bot.chat("I am already walking :3")
            
    
    
        @On(bot, "kicked")
        def handle_kick(this, reason, loggedIn):
            print(f"❌ Handshake Drop! Raw Engine Output: {reason}", flush=True)
            self.MoonWalkB = False
            time.sleep(30)
            self.start_bot()
    
        @On(bot, "error")
        def handle_error(this, err):
            print(f"💥 Exception: {err}", flush=True)

BOT()
while True:
    time.sleep(1)
