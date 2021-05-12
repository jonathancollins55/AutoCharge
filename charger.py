import kasa as ks
import asyncio
import psutil
from dotenv import dotenv_values

environment_vars = dotenv_values('keys.env')

#Toggles the smartPlug on or off
async def switch_smartPlug(ip_addr):
    if ip_addr == None: return
    if not(isinstance(ip_addr,str)): return

    #Initialize the plug and await the update
    plug = ks.SmartPlug(ip_addr)
    await plug.update()
    if plug.is_on:
        await plug.turn_off()
        return
    await plug.turn_on()

async def switchPlug_whenBatteryLow(ip_addr):
    if ip_addr == None: return
    if not(isinstance(ip_addr,str)): return

    #Get battery percentage
    battery = psutil.sensors_battery()
    threshold_percentage = bool(battery.percent > 30)

    #Turn plug on of battery is less than 30%
    plug = ks.SmartPlug(ip_addr)
    await plug.update()
    if threshold_percentage:
        await plug.turn_off()
        return
    await plug.turn_on()

asyncio.run(switchPlug_whenBatteryLow(environment_vars.get('Plug_ip_addr')))
# asyncio.run(switch_smartPlug(environment_vars.get('Plug_ip_addr')))