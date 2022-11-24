import re
# str= "faffafaffffjffafhsahfyihsfi ysfhsiyffiyffhhfi +91 9861588931 sgfjgsjgf jsgfjgsfgsuhihda"
#
# s= re.match("[+]\d[91]\s\d{10}",str)
#
# if s:
#     print(s)
#
# a=re.findall("[y]\w+", str)
# print(a)

srt="all, IPL 2022 Live Cricket Score Of Today's Match on NDTV SportsLive Updates of Today Match between Mumbai Indians vs Sunrisers Hyderabad from Wankhede Stadium, Mumbai. Check commentary and full scoreboard of the match.NDTVSportsUpdated: May 17, 2022 08:44 PM ISTRead"
s=re.compile(r"Mu\w+")
dd=s.search(srt)
ee=s.match(srt)
ff=s.findall(srt)
print(f"for search: {dd}")
print(f"for match: {ee}")
print(f"for findall: {ff}")

