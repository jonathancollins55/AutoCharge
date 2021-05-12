import kasa as ks
import asyncio

async def switch_smartPlug(ip_addr):
    plug = ks.SmartPlug(ip_addr)
    await plug.update()
    if plug.is_on:
        await plug.turn_off()
        return
    await plug.turn_on()

asyncio.run(switch_smartPlug('192.168.1.165'))