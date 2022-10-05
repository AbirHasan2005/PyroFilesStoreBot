from configs import Config
async def rw(capt):
  for i in Config.REMOVE_WORD:
    try:
      capt1 = capt.replace(f"{i}","")
      capt = capt1
    except:
      pass
  return capt
