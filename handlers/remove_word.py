from configs import Config
async def rw(capt):
  for i in Config.REMOVE_WORD:
    capt1 = capt.replace(f"{i}","")
    capt = capt1
  return capt
