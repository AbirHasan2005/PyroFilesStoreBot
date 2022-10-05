from configs import Config
async def rw(capt):
  for i in Config.remove_word:
    capt1 = capt.replace("i","")
    capt = capt1
  return capt
